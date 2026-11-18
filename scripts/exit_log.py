"""What happened to stocks after we trimmed or sold them (owner request 2026-11-18). No model calls.

    python scripts/exit_log.py update [--asof D]

Every TRIM/SELL in portfolio/ledger.csv is one row in portfolio/exits.csv, measured from its fill price:
- since_*: the sold stock's USD return and SPY's from the fill to the latest close (refreshed every run);
  kept_usd = what the sold shares gained (+) or lost (-) since, i.e. what selling cost (+) or saved (-).
- vs_replacement_since: for a swap, the bought stock's return minus the sold one's over the same days.
- 1/3/6/12-month ret/spy/excess/hit as in decisions.csv (decision_log.update); a HIT = the sold stock lagged SPY.
kind: swap (sold to fund another buy), sizing (cut to the conviction-3 size), research (the research said so).
shortcut: fills are at the open but SPY is taken at that day's close; use SPY's open if the history ever carries it.
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
import decision_log as DL  # noqa: E402

LEDGER = ROOT / "portfolio" / "ledger.csv"
LOG = ROOT / "portfolio" / "exits.csv"
COLS = (["date", "ticker", "type", "decision", "shares", "kind", "replaced_by", "currency", "fill_price", "price_date",
         "price_usd", "spy_close", "usd", "since_date", "since_ret", "since_spy", "since_excess", "kept_usd",
         "vs_replacement_since"]
        + [f"{k}_{h}m" for h in DL.HORIZONS for k in ("ret", "spy", "excess", "hit")])


def kind_of(reason: str) -> tuple[str, str]:
    m = re.match(r"replaced by (\S+?):\s", reason or "")
    if m:
        return "swap", m.group(1)
    return ("sizing" if (reason or "").startswith("conviction 3 sizing") else "research"), ""


def usd_price(r: dict) -> float:
    return float(r["fill_price"]) * (float(r["fx_usd_per_unit"]) if r.get("fx_usd_per_unit") else 1.0)


def rebuild(ledger: list[dict], old: list[dict], mkt) -> list[dict]:
    """One row per ledger TRIM/SELL; rows already in `old` keep their filled outcomes."""
    keep = {(r["date"], r["ticker"], r["decision"]): r for r in old}
    spy = mkt.cfg["portfolio"]["benchmark"]
    rows = []
    for t in ledger:
        if t["side"] not in ("TRIM", "SELL"):
            continue
        key = (t["date"], t["ticker"], t["side"])
        if key in keep:
            rows.append(keep[key])
            continue
        kind, rep = kind_of(t.get("reason", ""))
        rows.append({"date": t["date"], "ticker": t["ticker"], "type": t["type"], "decision": t["side"],
                     "shares": t["shares"], "kind": kind, "replaced_by": rep, "currency": t["currency"],
                     "fill_price": t["fill_price"], "price_date": t["date"], "price_usd": round(usd_price(t), 6),
                     "spy_close": mkt.quote(spy, t["date"])["close"], "usd": t["gross_usd"]})
    return rows


def since(rows: list[dict], ledger: list[dict], mkt, asof: str) -> list[str]:
    """Refresh the since-exit figures to the latest close on/before `asof`."""
    notes = []
    buys = {(t["date"], t["ticker"]): t for t in ledger if t["side"] in ("BUY", "ADD")}

    def ret(ticker, price_usd, start):
        q = mkt.quote(ticker, asof)
        return q["price_usd"] * DL.split_factor(mkt, ticker, start, q["date"]) / price_usd - 1, q["date"]

    for r in rows:
        try:
            DL.since_one(r, mkt, asof)
        except DataError as e:
            notes.append(f"{r['ticker']} {r['date']}: [data unavailable] ({e.field})")
            continue
        sr = r["since_ret"] / 100
        r["kept_usd"] = round(float(r["usd"]) * sr, 2)
        b = buys.get((r["date"], r["replaced_by"])) if r.get("replaced_by") else None
        if b:
            try:
                r["vs_replacement_since"] = round((ret(b["ticker"], usd_price(b), b["date"])[0] - sr) * 100, 2)
            except DataError as e:
                notes.append(f"{b['ticker']} {b['date']}: [data unavailable] ({e.field})")
    return notes


def write(rows: list[dict], path: Path = LOG):
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in COLS})
    tmp.replace(path)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["update"])
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    from portfolio import Market, price_provider
    cfg = load_config()
    mkt = Market(Fetcher(cfg), a.asof, cfg, price_provider(cfg))
    ledger = DL.read(LEDGER)
    try:
        rows = rebuild(ledger, DL.read(LOG), mkt)
        notes = since(rows, ledger, mkt, a.asof) + DL.update(rows, mkt, a.asof)
    except (DataError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    write(rows)
    print(json.dumps({"rows": len(rows), "notes": notes}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
