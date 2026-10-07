"""Calibration backtest for the Monte Carlo model. numpy only; no model calls.

For the last `backtest_quarters` quarter-ends whose 6-month outcome is already known, rebuild the model
using ONLY data available then (factor regression on up to 3 prior years of weekly returns, blended residual
vol, factor uncertainty = trailing factor volatility) with a FLAT base case (no historical research exists:
one scenario, expected idiosyncratic and factor moves 0, no jumps), simulate, and check whether the realised
3m and 6m returns fell inside P5-P95 (target ~90%) and P25-P75 (target ~50%).

    python scripts/mc_backtest.py HKG:9999 --asof 2026-10-07  -> research/HKG-9999/2026-10-07-mc-backtest.json/.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402
from mc_inputs import InputsError, market_of, regress, weekly_returns  # noqa: E402
from montecarlo import simulate  # noqa: E402


def quarter_ends(before: str, n: int) -> list[str]:
    d = dt.date.fromisoformat(before)
    out = []
    y, q = d.year, (d.month - 1) // 3  # current quarter index 0-3; step back to previous ends
    while len(out) < n:
        q -= 1
        if q < 0:
            q, y = 3, y - 1
        end = dt.date(y, 3 * q + 3, 1) + dt.timedelta(days=31)
        out.append((end.replace(day=1) - dt.timedelta(days=1)).isoformat())
    return sorted(out)


def price_on_or_before(rows: list[dict], day: str) -> dict | None:
    """Last completed weekly close on/before `day` (week start + 7 days <= day)."""
    done = [r for r in rows if (dt.date.fromisoformat(r["date"]) + dt.timedelta(days=7)).isoformat() <= day]
    return done[-1] if done else None


def realised(rows: list[dict], start: dict, weeks: int) -> float | None:
    i = next(k for k, r in enumerate(rows) if r["date"] == start["date"])
    return rows[i + weeks]["adj_close"] / start["adj_close"] - 1 if i + weeks < len(rows) else None


def backtest(stock_rows: list[dict], factor_rows: dict[str, list[dict]], asof: str, cfg: dict) -> dict:
    mc = cfg["montecarlo"]
    last_week = stock_rows[-1]["date"]
    eligible = []
    for q in quarter_ends(asof, 40):
        start = price_on_or_before(stock_rows, q)
        if start and realised(stock_rows, start, 26) is not None and (
                dt.date.fromisoformat(start["date"]) + dt.timedelta(weeks=26 + 1)).isoformat() <= last_week:
            eligible.append(q)
    dates = eligible[-mc["backtest_quarters"]:]
    trials = []
    for q in dates:
        try:
            reg = regress(weekly_returns(stock_rows, q), {t: weekly_returns(r, q) for t, r in factor_rows.items()},
                          mc["regression_weeks"], mc["vol_blend_weeks"])
        except InputsError as e:
            trials.append({"asof": q, "skipped": str(e)})
            continue
        order = reg["correlation"]["factors"]
        spec = {"scenarios": [("base", 1.0, 0.0, 0.0)], "betas": [reg["betas"][t] for t in order],
                "moves": [0.0] * len(order), "unc": [reg["factor_stats"][t]["vol_annual"] for t in order],
                "corr": reg["correlation"]["matrix"], "resid_vol": reg["residual_vol"]["blended"], "jumps": [], "tilt": 0.0}
        sim = simulate(spec, mc)
        start = price_on_or_before(stock_rows, q)
        row = {"asof": q, "start_week": start["date"], "regression_weeks": reg["weeks"], "r2": reg["r2"],
               "resid_vol": reg["residual_vol"]["blended"]}
        for h, weeks in (("3m", 13), ("6m", 26)):
            r = sim["h"][h]["ret"]
            p5, p25, p75, p95 = np.percentile(r, [5, 25, 75, 95])
            out = realised(stock_rows, start, weeks)
            row[h] = {"realised": out, "p5": float(p5), "p25": float(p25), "p75": float(p75), "p95": float(p95),
                      "in_p5_p95": bool(p5 <= out <= p95), "in_p25_p75": bool(p25 <= out <= p75)}
        trials.append(row)
    done = [t for t in trials if "skipped" not in t]
    cov = {h: {"in_p5_p95": sum(t[h]["in_p5_p95"] for t in done), "in_p25_p75": sum(t[h]["in_p25_p75"] for t in done),
               "n": len(done)} for h in ("3m", "6m")}
    return {"asof": asof, "method": "flat base case (no historical research): idiosyncratic and factor expected moves "
                                    "0, no jumps; factor regression and vol from data available at each date",
            "targets": {"in_p5_p95": 0.90, "in_p25_p75": 0.50}, "coverage": cov, "trials": trials}


def render_md(doc: dict, ticker: str) -> str:
    L = [f"## Monte Carlo calibration backtest — {ticker} ({doc['asof']})", doc["method"] + ".", "",
         "| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |", "|---|---|---|"]
    for h, c in doc["coverage"].items():
        if c["n"]:
            L.append(f"| {h} | {c['in_p5_p95']}/{c['n']} ({c['in_p5_p95'] / c['n']:.0%}) | "
                     f"{c['in_p25_p75']}/{c['n']} ({c['in_p25_p75'] / c['n']:.0%}) |")
    L += ["", "| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |", "|---|---|---|---|---|"]
    for t in doc["trials"]:
        if "skipped" in t:
            L.append(f"| {t['asof']} | skipped: {t['skipped']} | | | |")
            continue
        L.append(f"| {t['asof']} | {t['3m']['realised']:+.1%} | {t['3m']['p5']:+.1%} / {t['3m']['p95']:+.1%} | "
                 f"{t['6m']['realised']:+.1%} | {t['6m']['p5']:+.1%} / {t['6m']['p95']:+.1%} |")
    L.append("\nEight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.")
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    cfg = load_config()
    f = Fetcher(cfg)
    specs = cfg["montecarlo"]["factors"].get(market_of(a.ticker))
    if not specs:
        print(f"BACKTEST FAILED: no factor proxies for market {market_of(a.ticker)} [missing]", file=sys.stderr)
        return 2
    try:
        stock = f.long_history(a.ticker)["rows"]
        facs = {s["ticker"]: f.long_history(s["ticker"], etf=s.get("etf", False))["rows"] for s in specs}
    except DataError as e:
        print(f"BACKTEST FAILED: {e}", file=sys.stderr)
        return 2
    doc = backtest(stock, facs, a.asof, cfg)
    out = ROOT / "research" / Ticker(a.ticker).slug
    (out / f"{a.asof}-mc-backtest.json").write_text(json.dumps(doc, indent=1))
    (out / f"{a.asof}-mc-backtest.md").write_text(render_md(doc, a.ticker))
    print(json.dumps(doc["coverage"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
