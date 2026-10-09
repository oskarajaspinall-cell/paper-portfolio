"""Entry prices: the level at which we'd consider entering a conviction-3+ name (owner rule 2026-10-09).
No model calls.

    python scripts/entry_watch.py check [--asof D]    daily: latest close vs entry price -> hits
    python scripts/entry_watch.py backfill            seed names with no evaluator entry price (mechanical)
    python scripts/entry_watch.py list                print the watchlist with % to entry

`portfolio/entry_watch.csv`, one row per stock, written when a decision is logged (decision_log.py record):
the evaluator's `entry_price` (the price at which the same evidence would justify conviction 4) or, when it
gave none, the mechanical anchor = base fair value x (1 - [entry].margin_of_safety_pct). A null entry price
with a reason means price isn't the obstacle (falling quality, an unresolved legal/regulatory event): no row.
A close at/below the entry price is a HIT: listed in reports/entry-watch/<date>.md, a Mac notification, and
`state["entry_hits"]`, so the next weekly run (and the research loop) re-researches it FIRST, bypassing the
90-day rule. The price fell for a reason, so nothing is bought on price alone: the re-initiation decides.
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
        "evaluation", "last_close", "last_close_date", "pct_to_entry", "hit_date"]


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


def check(rows: list[dict], quote, asof: str) -> tuple[list[dict], list[dict]]:
    """Update each live row with its latest close; return (rows, hits). Expired rows are dropped."""
    live, hits = [], []
    for r in rows:
        if r.get("expires") and r["expires"] < asof:
            continue
        try:
            q = quote(r["ticker"])
        except DataError:
            live.append(r)
            continue
        e = float(r["entry_price"])
        r.update(last_close=q["close"], last_close_date=q["date"], pct_to_entry=round((e / q["close"] - 1) * 100, 2))
        if q["close"] <= e:
            r["hit_date"] = r.get("hit_date") or q["date"]
            hits.append(r)
        live.append(r)
    return live, hits


def notify(title: str, msg: str) -> None:
    subprocess.run(["osascript", "-e", f'display notification "{msg.replace(chr(34), "")}" with title "{title}"'],
                   capture_output=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "backfill", "list"])
    ap.add_argument("--asof", default=dt.date.today().isoformat())
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
    if a.cmd == "check":
        from fetch_data import Fetcher
        from portfolio import Market, price_provider
        mkt = Market(Fetcher(cfg, refresh=True), a.asof, cfg, price_provider(cfg))
        rows, hits = check(rows, mkt.quote, a.asof)
        write(rows)
        stp = ROOT / "portfolio" / "state.json"
        state = json.loads(stp.read_text())
        state["entry_hits"] = [{"ticker": h["ticker"], "hit_date": h["hit_date"], "close": h["last_close"],
                                "entry_price": float(h["entry_price"])} for h in hits]
        tmp = stp.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
        tmp.replace(stp)
        out = ROOT / "reports" / "entry-watch"
        out.mkdir(parents=True, exist_ok=True)
        near = sorted(rows, key=lambda r: -float(r.get("pct_to_entry") or -999))[:15]
        L = [f"# Entry watch — {a.asof}", "",
             f"{len(rows)} stocks watched; {len(hits)} at or below their entry price"
             + (": " + ", ".join(h["ticker"] for h in hits) + " (re-researched first next run)" if hits else "") + ".",
             "", "| Stock | Last close | Entry price | To entry | Source | Set |", "|---|---|---|---|---|---|"]
        L += [f"| {r['ticker']} | {r.get('last_close', '')} {r.get('currency', '')} | {r['entry_price']} | "
              f"{r.get('pct_to_entry', '')}% | {r['source']} | {r['set_date']} |" for r in near]
        (out / f"{a.asof}.md").write_text("\n".join(L) + "\n")
        if hits:
            notify("Paper portfolio: entry price hit", ", ".join(h["ticker"] for h in hits) + " -> re-research next run")
        print(json.dumps({"watching": len(rows), "hits": [h["ticker"] for h in hits]}))
        return 0
    for r in sorted(rows, key=lambda r: -float(r.get("pct_to_entry") or -999)):
        print(f"{r['ticker']:12} entry {r['entry_price']:>10} {r.get('currency', ''):4} close {r.get('last_close', '?'):>10} "
              f"to entry {r.get('pct_to_entry', '?')}%  ({r['source']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
