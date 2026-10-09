"""Decision log and hit rates. No model calls.

    python scripts/decision_log.py record <evaluation.md> [...] [--asof D]   append decisions
    python scripts/decision_log.py update [--asof D]                        fill matured outcomes
    python scripts/decision_log.py table                                    print the hit-rate table

Every evaluator decision is one row in portfolio/decisions.csv. Outcomes are the stock's USD return
minus SPY's return from the decision close to the close on/before 1, 3, 6 and 12 months later (all
prices from stockanalysis.com). A decision is a HIT when it was right about direction vs SPY:
BUY/ADD/HOLD -> beat SPY; AVOID/SELL/TRIM -> lagged SPY.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402
from fetch_data import Fetcher  # noqa: E402

LOG = ROOT / "portfolio" / "decisions.csv"
HORIZONS = (1, 3, 6, 12)
COLS = (["date", "ticker", "type", "decision", "conviction", "price", "currency", "price_date", "price_usd",
         "spy_close", "evaluation", "note", "fair_value_base"]
        + [f"{k}_{h}m" for h in HORIZONS for k in ("ret", "spy", "excess", "hit")])
POSITIVE = {"BUY", "ADD", "HOLD"}


def add_months(iso: str, m: int) -> str:
    d = dt.date.fromisoformat(iso)
    y, mo = divmod(d.month - 1 + m, 12)
    for day in (d.day, 30, 29, 28):
        try:
            return dt.date(d.year + y, mo + 1, day).isoformat()
        except ValueError:
            continue
    raise ValueError(iso)


def read(path: Path = LOG) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


def write(rows: list[dict], path: Path = LOG):
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in COLS})
    tmp.replace(path)


def decision_from_eval(md: str) -> dict:
    m = re.search(r"```json\s*(\{.*?\})\s*```\s*$", md.strip(), re.S)
    if not m:
        raise ValueError("no Decision json block at the end of the evaluation")
    return json.loads(m.group(1))


def record(eval_paths: list[str], mkt, asof: str, rows: list[dict]) -> list[dict]:
    """Append one row per evaluation (idempotent per evaluation path)."""
    seen = {r["evaluation"] for r in rows}
    spy = mkt.cfg["portfolio"]["benchmark"]
    for p in eval_paths:
        rel = str(Path(p).resolve().relative_to(ROOT)) if Path(p).is_absolute() else p
        if rel in seen:
            continue
        d = decision_from_eval(Path(p if Path(p).is_absolute() else ROOT / p).read_text())
        q = mkt.quote(d["ticker"], d["price_date"])
        s = mkt.quote(spy, d["price_date"])
        m = int(mkt.cfg["core"].get("min_buy_conviction", 1))
        note = ""
        if d["decision"] in ("BUY", "ADD") and int(d["conviction"]) < m:  # owner rule: never bought
            note = (f"relabelled {d['decision']}->AVOID: conviction {d['conviction']} is below the minimum {m} "
                    "to buy (owner rule); the trade was not made")
            d["decision"] = "AVOID"
        fvp = Path(p if Path(p).is_absolute() else ROOT / p)
        fvp = fvp.with_name(fvp.name.replace("-evaluation.md", "-valuation.json"))
        fv_base = ""
        if fvp.name.endswith("-valuation.json") and fvp.exists():  # inform-only fair value (scripts/valuation.py), kept so its accuracy can be measured later
            base = (json.loads(fvp.read_text()).get("fair_value") or {}).get("base")
            fv_base = "" if base is None else round(base, 4)
        try:  # entry price for conviction-3+ names (owner rule 2026-10-09)
            import entry_watch
            entry_watch.record_decision(dict(d, ticker=d["ticker"]), Path(p if Path(p).is_absolute() else ROOT / p),
                                        asof, mkt.cfg, q["currency"])
        except Exception as e:  # noqa: BLE001  never blocks the decision log
            note = (note + "; " if note else "") + f"entry watch not updated: {str(e)[:80]}"
        rows.append({"note": note, "fair_value_base": fv_base, "date": asof, "ticker": d["ticker"], "type": d["position_type"], "decision": d["decision"],
                     "conviction": d["conviction"], "price": d["price_at_decision"], "currency": q["currency"],
                     "price_date": d["price_date"], "price_usd": round(q["price_usd"], 6),
                     "spy_close": s["close"], "evaluation": rel})
    return rows


def update(rows: list[dict], mkt, asof: str) -> list[str]:
    """Fill outcomes whose horizon has passed. Returns notes for horizons that can no longer be priced."""
    notes = []
    spy = mkt.cfg["portfolio"]["benchmark"]
    for r in rows:
        for h in HORIZONS:
            if r.get(f"ret_{h}m") not in ("", None):
                continue
            end = add_months(r["price_date"], h)
            if end >= asof:
                continue
            try:
                q, s = mkt.quote(r["ticker"], end), mkt.quote(spy, end)
            except DataError as e:  # horizon older than the site's 6-month history page
                r[f"ret_{h}m"] = "n/a"
                notes.append(f"{r['ticker']} {r['price_date']} {h}m: [data unavailable] ({e.field})")
                continue
            ret = q["price_usd"] / float(r["price_usd"]) - 1
            sr = s["close"] / float(r["spy_close"]) - 1
            ex = ret - sr
            hit = ex > 0 if r["decision"] in POSITIVE else ex < 0
            r.update({f"ret_{h}m": round(ret * 100, 2), f"spy_{h}m": round(sr * 100, 2),
                      f"excess_{h}m": round(ex * 100, 2), f"hit_{h}m": int(hit)})
    return notes


def hit_table(rows: list[dict]) -> str:
    groups = [("All decisions", lambda r: True), ("CORE", lambda r: r["type"] == "CORE"),
              ("TACTICAL", lambda r: r["type"] == "TACTICAL")]
    groups += [(f"Conviction {c}", (lambda c: lambda r: str(r["conviction"]) == str(c))(c)) for c in range(1, 6)]
    head = "| Group | Decisions | " + " | ".join(f"{h}m hit rate" for h in HORIZONS) + " |"
    lines = [head, "|---|---|" + "---|" * len(HORIZONS)]
    for name, fn in groups:
        g = [r for r in rows if fn(r)]
        cells = []
        for h in HORIZONS:
            done = [r for r in g if r.get(f"hit_{h}m") not in ("", None)]
            hits = sum(int(r[f"hit_{h}m"]) for r in done)
            cells.append(f"{hits}/{len(done)} ({hits / len(done) * 100:.0f}%)" if done else "–")
        lines.append(f"| {name} | {len(g)} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["record", "update", "table"])
    ap.add_argument("evaluations", nargs="*")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    rows = read()
    if a.cmd == "table":
        print(hit_table(rows))
        return 0
    from portfolio import Market, price_provider
    cfg = load_config()
    mkt = Market(Fetcher(cfg), a.asof, cfg, price_provider(cfg))
    try:
        if a.cmd == "record":
            n0 = len(rows)
            record(a.evaluations, mkt, a.asof, rows)
            write(rows)
            print(f"recorded {len(rows) - n0} decision(s); {len(rows)} total")
        else:
            notes = update(rows, mkt, a.asof)
            write(rows)
            print(json.dumps({"rows": len(rows), "notes": notes}))
    except (DataError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
