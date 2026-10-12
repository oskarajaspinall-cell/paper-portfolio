"""Mechanical pre-screen before a full (AI) initiation: no model calls. A stock whose mechanical base-case
fair value (scripts/valuation.py, the same number the fact sheet shows) sits below the price by more than
`[screen].prescreen_min_base_upside_pct` cannot be "a good business at an attractive valuation", so it skips the
researcher / macro-overlay / evaluator sessions. Owner request 2026-10-12: research the universe more
efficiently. Every BUY to date had a base fair value above the price (+30% to +182% where measured).

A stock whose fair value can't be computed passes (we can't judge it, so the full research decides). Each
verdict is appended to reports/prescreen/<asof>.csv. The screen re-runs free every day, so a stock that falls
below its fair value is picked up again.

Usage: prescreen.py TICKER [TICKER ...] [--asof YYYY-MM-DD]"""
import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import valuation  # noqa: E402
from common import ROOT, load_config  # noqa: E402
from fetch_data import DataError, Fetcher  # noqa: E402

FIELDS = ["ticker", "asof", "price", "base_fair_value", "base_upside_pct", "verdict", "reason"]


def check(ticker: str, asof: str, fetcher, cfg: dict) -> dict:
    floor = float(cfg["screen"]["prescreen_min_base_upside_pct"])
    row = {"ticker": ticker, "asof": asof, "price": "", "base_fair_value": "", "base_upside_pct": ""}
    try:
        fv, _ = valuation.compute(ticker, asof, fetcher, cfg)
        base, up = (fv.get("fair_value") or {}).get("base"), (fv.get("upside") or {}).get("base")
    except (DataError, KeyError, ValueError, ZeroDivisionError) as e:
        return row | {"verdict": "PASS", "reason": f"fair value unavailable ({str(e)[:120]}): full research decides"}
    if base is None or up is None:
        return row | {"verdict": "PASS", "reason": "no base fair value: full research decides"}
    row |= {"price": round(fv["price"], 4), "base_fair_value": round(base, 4), "base_upside_pct": round(up * 100, 1)}
    if up * 100 >= floor:
        return row | {"verdict": "PASS", "reason": f"base fair value {up * 100:+.1f}% vs price (floor {floor:+.0f}%)"}
    return row | {"verdict": "SKIP", "reason": f"price above base fair value ({up * 100:+.1f}%; floor {floor:+.0f}%)"}


def record(row: dict) -> None:
    out = ROOT / "reports" / "prescreen" / f"{row['asof']}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    new = not out.exists()
    with out.open("a", newline="") as fh:
        w = csv.DictWriter(fh, FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    args = ap.parse_args(argv)
    cfg, fetcher = load_config(), Fetcher()
    for t in args.tickers:
        row = check(t, args.asof, fetcher, cfg)
        record(row)
        print(f"{t}\t{row['verdict']}\t{row['reason']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
