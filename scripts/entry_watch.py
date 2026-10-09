"""Entry prices: the level at which we'd consider entering a conviction-3+ name (owner rule 2026-10-09).
No model calls.

    python scripts/entry_watch.py check [--asof D]    daily: latest close vs entry price -> hits
    python scripts/entry_watch.py backfill            seed names with no evaluator entry price (mechanical)
    python scripts/entry_watch.py intraday [--force]  weekdays ~10:30 New York: live prices vs entry prices (US stocks)
    python scripts/entry_watch.py list [--near]       print the watchlist with % to entry (--near: close-to-entry only)

`portfolio/entry_watch.csv`, one row per stock, written when a decision is logged (decision_log.py record):
the evaluator's `entry_price` (the price at which the same evidence would justify conviction 4) or, when it
gave none, the mechanical anchor = base fair value x (1 - [entry].margin_of_safety_pct). A null entry price
with a reason means price isn't the obstacle (falling quality, an unresolved legal/regulatory event): no row.
A close at/below the entry price is a HIT: listed in reports/entry-watch/<date>.md, a Mac notification, and
`state["entry_hits"]`, so the next weekly run (and the research loop) re-researches it FIRST, bypassing the
90-day rule. The price fell for a reason, so nothing is bought on price alone: the re-initiation decides.

INTRADAY (owner request 2026-10-09): `bin/entry-intraday` (launchd, weekdays) runs `intraday` about an hour after
the US open: live Yahoo prices (the owner-approved portfolio price source) for US-listed watch rows; a price
at/below the entry price is a hit (Mac notification, `state["entry_hits"]` with `intraday: true`) and is
re-researched at once by scripts/entry_research.py (at most [entry].intraday_max_research a day). Other markets
are closed by then; the daily close check covers them.

CLOSE TO ENTRY (owner request 2026-10-09): a stock whose close is within [entry].near_pct of its entry price (or
at/below it) is on the close-to-entry watchlist. `near_since` records when it entered the band (cleared when it
leaves); entering it triggers one Mac notification, and the daily report and dashboard list every such stock with
the evaluator's reason it isn't a buy yet. Information only: nothing is researched or bought because of it.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

WATCH = ROOT / "portfolio" / "entry_watch.csv"
COLS = ["ticker", "entry_price", "currency", "set_date", "expires", "conviction", "decision", "source", "basis",
        "evaluation", "last_close", "last_close_date", "pct_to_entry", "hit_date", "near_since"]


def read(path: Path = WATCH) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


def write(rows: list[dict], path: Path = WATCH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in sorted(rows, key=lambda r: r["ticker"]):
            w.writerow({k: r.get(k, "") for k in COLS})
    tmp.replace(path)


def anchor(valuation: dict, cfg: dict) -> float | None:
    """Mechanical entry price: base fair value less the margin of safety (quoted currency)."""
    base = (valuation.get("fair_value") or {}).get("base")
    if not base or base <= 0:
        return None
    return round(base * (1 - cfg["entry"]["margin_of_safety_pct"] / 100), 4)


def row_from_decision(d: dict, evaluation: str, asof: str, cfg: dict, valuation: dict | None,
                      currency: str = "") -> dict | None:
    """The watch row for one logged decision, or None (no row: below conviction 3, a BUY/ADD/SELL, or the
    evaluator said price isn't the obstacle)."""
    ec = cfg["entry"]
    if int(d.get("conviction") or 0) < ec["min_conviction"] or d.get("decision") in ("BUY", "ADD", "SELL"):
        return None
    if "entry_price" in d and d["entry_price"] is None:
        return None  # owner rule: price isn't the obstacle, so a lower price wouldn't change the decision
    price, source, basis = d.get("entry_price"), "evaluator", d.get("entry_basis") or ""
    if not isinstance(price, (int, float)):
        price = anchor(valuation or {}, cfg)
        source, basis = "mechanical", f"base fair value x (1 - {ec['margin_of_safety_pct']:g}% margin of safety)"
    if not price or (isinstance(d.get("price_at_decision"), (int, float)) and price >= d["price_at_decision"]):
        return None
    return {"ticker": d["ticker"], "entry_price": round(float(price), 4), "currency": currency,
            "set_date": asof, "expires": (dt.date.fromisoformat(asof) + dt.timedelta(days=ec["expiry_days"])).isoformat(),
            "conviction": d.get("conviction"), "decision": d.get("decision"), "source": source, "basis": basis,
            "evaluation": evaluation}


def upsert(rows: list[dict], new: dict | None, ticker: str) -> list[dict]:
    """Replace the stock's row (a fresh decision supersedes the old entry price; None removes it)."""
    out = [r for r in rows if r["ticker"] != ticker]
    return out + ([new] if new else [])


def record_decision(d: dict, evaluation_path: Path, asof: str, cfg: dict, currency: str = "") -> dict | None:
    """Called by decision_log.record for every logged decision."""
    vp = evaluation_path.with_name(evaluation_path.name.replace("-evaluation.md", "-valuation.json"))
    val = json.loads(vp.read_text()) if vp.name.endswith("-valuation.json") and vp.exists() else None
    rel = str(evaluation_path.relative_to(ROOT)) if evaluation_path.is_absolute() else str(evaluation_path)
    new = row_from_decision(d, rel, asof, cfg, val, currency or (val or {}).get("quote_currency", ""))
    write(upsert(read(), new, d["ticker"]))
    return new


def is_near(r: dict, near_pct: float) -> bool:
    """Close to entry: the latest close is within near_pct of the entry price, or at/below it."""
    try:
        return float(r.get("pct_to_entry")) >= -near_pct
    except (TypeError, ValueError):
        return False


def near(rows: list[dict], near_pct: float) -> list[dict]:
    """The close-to-entry watchlist, closest first."""
    return sorted((r for r in rows if is_near(r, near_pct)), key=lambda r: -float(r["pct_to_entry"]))


def why_not_yet(r: dict, n: int = 220) -> str:
    """The evaluator's rationale for the conviction-3 decision (what keeps it from being a buy), shortened."""
    try:
        from decision_log import decision_from_eval
        t = " ".join((decision_from_eval((ROOT / r["evaluation"]).read_text()).get("rationale") or "").split())
    except Exception:  # noqa: BLE001 - missing/old evaluation: show nothing rather than fail the daily job
        return ""
    return t if len(t) <= n else t[:n - 1].rsplit(" ", 1)[0] + "…"


def check(rows: list[dict], quote, asof: str, near_pct: float = 10) -> tuple[list[dict], list[dict], list[dict]]:
    """Update each live row with its latest close; return (rows, hits, entered), where `entered` are stocks that
    moved into the close-to-entry band this check. Expired rows are dropped."""
    live, hits, entered = [], [], []
    for r in rows:
        if r.get("expires") and r["expires"] < asof:
            continue
        try:
            q = quote(r["ticker"])
        except DataError:
            live.append(r)
            continue
        e = float(r["entry_price"])
        r.update(last_close=round(float(q["close"]), 4), last_close_date=q["date"],
                 pct_to_entry=round((e / q["close"] - 1) * 100, 2))
        if q["close"] <= e:
            r["hit_date"] = r.get("hit_date") or q["date"]
            hits.append(r)
        if is_near(r, near_pct):
            if not r.get("near_since"):
                r["near_since"] = q["date"]
                entered.append(r)
        else:
            r["near_since"] = ""
        live.append(r)
    return live, hits, entered


def in_check_window(now_ny: dt.datetime, cfg: dict) -> bool:
    """Weekday, within [entry].intraday_window_et of New York time (launchd fires at two UK times a day so one
    lands ~10:30 ET across the weeks when UK and US clocks change on different dates)."""
    lo, hi = cfg["entry"].get("intraday_window_et", ["10:15", "11:15"])
    return now_ny.weekday() < 5 and lo <= now_ny.strftime("%H:%M") <= hi


def intraday_hits(rows: list[dict], price_fn, today: str) -> tuple[list[dict], list[str]]:
    """US-listed rows whose live price today is at/below the entry price. Returns (hits, skipped notes).
    A stale price (no trade today: a holiday or a halt) is never a hit."""
    hits, notes = [], []
    for r in rows:
        if Ticker(r["ticker"]).exchange or r.get("expires", "9999") < today:
            continue
        try:
            q = price_fn(r["ticker"])
        except DataError as e:
            notes.append(f"{r['ticker']}: no live price ({str(e)[:80]})")
            continue
        if q["date"] != today:
            notes.append(f"{r['ticker']}: no trade today (last {q['date']})")
            continue
        if q["price"] <= float(r["entry_price"]):
            hits.append({"ticker": r["ticker"], "hit_date": today, "close": round(q["price"], 4),
                         "entry_price": float(r["entry_price"]), "intraday": True, "time": q["time"][11:16] + " ET",
                         "source_url": q["url"]})
    return hits, notes


def merge_hits(existing: list[dict], new: list[dict]) -> list[dict]:
    have = {h["ticker"] for h in existing}
    return existing + [h for h in new if h["ticker"] not in have]


def notify(title: str, msg: str) -> None:
    subprocess.run(["osascript", "-e", f'display notification "{msg.replace(chr(34), "")}" with title "{title}"'],
                   capture_output=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "backfill", "list", "intraday"])
    ap.add_argument("--force", action="store_true", help="intraday: run outside the New York time window")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--near", action="store_true", help="list: close-to-entry stocks only")
    a = ap.parse_args(argv)
    cfg = load_config()
    if a.cmd == "backfill":
        from decision_log import decision_from_eval
        with (ROOT / "portfolio" / "decisions.csv").open() as fh:
            latest = {}
            for r in csv.DictReader(fh):
                latest[r["ticker"]] = r  # last decision per stock
        rows, added = read(), 0
        have = {r["ticker"] for r in rows}
        for t, r in latest.items():
            if t in have or not r.get("evaluation"):
                continue
            ev = ROOT / r["evaluation"]
            if not ev.exists():
                continue
            d = decision_from_eval(ev.read_text())
            d["decision"], d["ticker"] = r["decision"], t  # the logged decision (relabels applied)
            vp = ev.with_name(ev.name.replace("-evaluation.md", "-valuation.json"))
            if not vp.exists() and int(d.get("conviction") or 0) >= cfg["entry"]["min_conviction"]:
                subprocess.run([str(ROOT / "bin" / "py"), "scripts/valuation.py", t, "--asof", ev.name[:10]],
                               cwd=ROOT, capture_output=True)
            val = json.loads(vp.read_text()) if vp.exists() else None
            new = row_from_decision(d, r["evaluation"], r["date"], cfg, val, (val or {}).get("quote_currency", ""))
            if new:
                rows, added = upsert(rows, new, t), added + 1
        write(rows)
        print(json.dumps({"added": added, "watching": len(rows)}))
        return 0
    rows = read()
    if a.cmd == "intraday":
        from zoneinfo import ZoneInfo
        now_ny = dt.datetime.now(ZoneInfo("America/New_York"))
        if not a.force and not in_check_window(now_ny, cfg):
            print(json.dumps({"skipped": f"outside the check window ({now_ny:%a %H:%M} New York)"}))
            return 0
        from prices import live_price
        today = now_ny.date().isoformat()
        hits, notes = intraday_hits(rows, live_price, today)
        stp = ROOT / "portfolio" / "state.json"
        state = json.loads(stp.read_text())
        held = set(state.get("holdings", {}))
        hits = [h for h in hits if h["ticker"] not in held]
        if hits:
            state["entry_hits"] = merge_hits(state.get("entry_hits") or [], hits)
            tmp = stp.with_suffix(".tmp")
            tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
            tmp.replace(stp)
            for r in rows:
                if r["ticker"] in {h["ticker"] for h in hits}:
                    r["hit_date"] = r.get("hit_date") or today
            write(rows)
            out = ROOT / "reports" / "entry-watch"
            out.mkdir(parents=True, exist_ok=True)
            L = [f"# Intraday entry check — {today} {now_ny:%H:%M} New York", "",
                 f"{len(hits)} US stock(s) traded at or below their entry price; each is re-researched now "
                 "(never bought on price alone).", "", "| Stock | Live price | Entry price | Time | Source |", "|---|---|---|---|---|"]
            L += [f"| {h['ticker']} | {h['close']:,.2f} | {h['entry_price']:,.2f} | {h['time']} | {h['source_url']} |" for h in hits]
            (out / f"{today}-intraday.md").write_text("\n".join(L + [""] + [f"- {n}" for n in notes]) + "\n")
            notify("Paper portfolio: entry price hit (intraday)",
                   ", ".join(h["ticker"] for h in hits) + " -> re-researching now")
        print(json.dumps({"checked_at": f"{now_ny:%H:%M} New York", "hits": [h["ticker"] for h in hits], "notes": notes}))
        return 0
    near_pct = float(cfg["entry"].get("near_pct", 10))
    if a.cmd == "check":
        from fetch_data import Fetcher
        from portfolio import Market, price_provider
        mkt = Market(Fetcher(cfg, refresh=True), a.asof, cfg, price_provider(cfg))
        rows, hits, entered = check(rows, mkt.quote, a.asof, near_pct)
        write(rows)
        stp = ROOT / "portfolio" / "state.json"
        state = json.loads(stp.read_text())
        pending = {r["ticker"] for r in rows if r.get("hit_date")}  # a re-research replaces the row (clears it)
        state["entry_hits"] = merge_hits(
            [{"ticker": h["ticker"], "hit_date": h["hit_date"], "close": h["last_close"],
              "entry_price": float(h["entry_price"])} for h in hits],
            [h for h in state.get("entry_hits") or [] if h.get("intraday") and h["ticker"] in pending])
        tmp = stp.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
        tmp.replace(stp)
        out = ROOT / "reports" / "entry-watch"
        out.mkdir(parents=True, exist_ok=True)
        close = near(rows, near_pct)
        fmt = lambda x: "" if x in (None, "") else f"{float(x):,.2f}"  # noqa: E731
        rest = [r for r in sorted(rows, key=lambda r: -float(r.get("pct_to_entry") or -999)) if r not in close][:15]
        L = [f"# Entry watch — {a.asof}", "",
             f"{len(rows)} stocks watched; {len(hits)} at or below their entry price"
             + (": " + ", ".join(h["ticker"] for h in hits) + " (re-researched first next run)" if hits else "")
             + f"; {len(close)} within {near_pct:g}% of it.", "",
             f"## Close to entry (within {near_pct:g}%)", "",
             "Information only: a stock is re-researched when it closes at or below its entry price, never bought on price.",
             "", "| Stock | Last close | Entry price | To entry | In range since | Why not a buy yet |", "|---|---|---|---|---|---|"]
        L += [f"| {r['ticker']}{' **HIT**' if r.get('hit_date') else ''} | {fmt(r.get('last_close'))} {r.get('currency', '')} | "
              f"{fmt(r['entry_price'])} | {float(r['pct_to_entry']):+.1f}% | {r.get('near_since', '')} | "
              f"{why_not_yet(r).replace('|', '/')} |" for r in close] or ["| none | | | | | |"]
        L += ["", "## Next closest", "", "| Stock | Last close | Entry price | To entry | Source | Set |", "|---|---|---|---|---|---|"]
        L += [f"| {r['ticker']} | {fmt(r.get('last_close'))} {r.get('currency', '')} | {fmt(r['entry_price'])} | "
              f"{r.get('pct_to_entry', '')}% | {r['source']} | {r['set_date']} |" for r in rest]
        (out / f"{a.asof}.md").write_text("\n".join(L) + "\n")
        if hits:
            notify("Paper portfolio: entry price hit", ", ".join(h["ticker"] for h in hits) + " -> re-research next run")
        new_near = [r for r in entered if r not in hits]
        if new_near:
            notify("Paper portfolio: close to entry price",
                   ", ".join(f"{r['ticker']} ({float(r['pct_to_entry']):+.1f}%)" for r in new_near)
                   + f" now within {near_pct:g}% of the entry price")
        print(json.dumps({"watching": len(rows), "hits": [h["ticker"] for h in hits],
                          "close_to_entry": [r["ticker"] for r in close], "entered": [r["ticker"] for r in new_near]}))
        return 0
    for r in (near(rows, near_pct) if a.near else sorted(rows, key=lambda r: -float(r.get("pct_to_entry") or -999))):
        print(f"{r['ticker']:12} entry {r['entry_price']:>10} {r.get('currency', ''):4} close {r.get('last_close', '?'):>10} "
              f"to entry {r.get('pct_to_entry', '?')}%  ({r['source']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
