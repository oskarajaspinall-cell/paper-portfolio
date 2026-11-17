"""Mechanical pre-screen before a full (AI) initiation: no model calls. A stock whose mechanical base-case
fair value (scripts/valuation.py, the same number the fact sheet shows) sits below the price by more than
`[screen].prescreen_min_base_upside_pct` cannot be "a good business at an attractive valuation", so it skips the
researcher / macro-overlay / evaluator sessions. Owner request 2026-10-12: research the universe more
efficiently. Every BUY to date had a base fair value above the price (+30% to +182% where measured).

A name that passes is then scored on the scorecard's measurable parts (`points_gate`, 2026-11-17): one that cannot
reach conviction 4 whatever the research finds is skipped too.

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


def trend_strong(ticker: str, fetcher, cfg: dict) -> str | None:
    """The scorecard's trend-strength test on the statistics page (cached by the screen): above the 200-day average
    but not overextended, with a real FCF yield. Such a name can reach conviction 4 without a discount."""
    from fetch_data import page_nodes, parse_info, parse_statistics
    from screen import stock_metrics
    from common import page_url
    sc = cfg["scorecard"]
    url = page_url(ticker, "statistics/")
    try:
        nodes = page_nodes(fetcher.html(url), url)
        m = stock_metrics(parse_statistics(nodes, url), parse_info(nodes, url))
    except DataError:
        return None
    ext, fcf = m.get("price_vs_sma200"), m.get("fcfYield")
    if ext is not None and 0 < ext <= sc["overextended_pct"] and fcf is not None and fcf >= sc["min_fcf_yield_pct"]:
        return f"price {ext:+.0f}% vs 200-day, FCF yield {fcf:.1f}%"
    return None


def check(ticker: str, asof: str, fetcher, cfg: dict) -> dict:
    """Owner request 2026-11-15: a price above fair value no longer skips a name with trend strength (the mandate is
    a good business that is working, so the scorecard can reach 4 without a discount)."""
    row = _check(ticker, asof, fetcher, cfg)
    if row["verdict"] == "SKIP":
        why = trend_strong(ticker, fetcher, cfg)
        if why:
            row = row | {"verdict": "PASS", "reason": f"{row['reason']}; passes on trend strength ({why})"}
    return points_gate(row, ticker, asof, fetcher, cfg)


def scorecard_points(ticker: str, asof: str, fetcher, cfg: dict) -> tuple[dict, bool] | None:
    """(the scorecard on the Python inputs alone, whether a reliable fair value was in it). The fact sheet's trends
    and the mechanical fair value, built in memory; judgement fields neutral (narrow moat, medium key risk, no
    decline explained, no analyst expected value)."""
    import fact_sheet
    import scorecard
    fvo: dict = {}
    fact_sheet.build(ticker, [], fetcher, asof, fvo)
    if not fvo.get("trends"):
        return None
    fv = fvo.get("fv") or {}
    d = {"decision": "BUY", "price_at_decision": fv.get("price"),
         "scorecard": {"decline_cause": "none", "moat": "narrow", "key_risk": "medium"}}
    res = scorecard.score(d, fvo["trends"], fv or None, cfg, scorecard.calibration_offset())
    return res, bool((fv.get("fair_value") or {}).get("base")) and valuation.is_reliable(fv)


def points_gate(row: dict, ticker: str, asof: str, fetcher, cfg: dict) -> dict:
    """Owner request 2026-11-17: a name that passed the fair-value gate still skips the AI steps when the scorecard
    cannot get it to conviction 4. Python sets the conviction and the evaluator can add at most 3 points to this
    estimate (a wide moat, a low key risk, a temporary decline), so:
    - quality level 0 (return on capital below `[scorecard].quality_lo`, or none published) fails the 4+ gate whatever
      the evaluator writes;
    - an estimate below `[screen].prescreen_min_points` is out of reach. Only with a reliable fair value: without one
      the evaluator's own expected value sets the valuation points and the estimate is too low to trust.
    Replay on the 318 new-name evaluations of 2026-11-08..16: 24% skipped (50 on quality, 26 on points), none of
    them reached conviction 4 and the highest real total among them was 7; the real total never beat the estimate
    by more than 3."""
    floor = float(cfg["screen"].get("prescreen_min_points", 0))
    if row["verdict"] != "PASS" or not floor:
        return row
    try:
        got = scorecard_points(ticker, asof, fetcher, cfg)
    except (DataError, KeyError, ValueError, ZeroDivisionError, TypeError):
        return row  # can't score it: full research decides
    if got is None:
        return row
    res, reliable = got
    if res["parts"]["quality_level"] == 0:
        return row | {"verdict": "SKIP", "reason": f"{row['reason']}; but {res['notes'][0]} is below the scorecard's "
                      "quality floor, which blocks conviction 4 whatever the research finds"}
    if reliable and res["total"] < floor:
        return row | {"verdict": "SKIP", "reason": f"{row['reason']}; but the scorecard's measurable parts give "
                      f"{res['total']:g} points (floor {floor:g}): conviction 4 is out of reach"}
    return row


def _check(ticker: str, asof: str, fetcher, cfg: dict) -> dict:
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
    if not valuation.is_reliable(fv):  # 2026-11-09: a broken blend can't skip a stock on its own (Mizrahi -99%)...
        why = "; ".join(valuation.reliability(fv)["reasons"])
        bases = [m["values"]["base"] for m in fv.get("methods", []) if m.get("status") == "ok" and m.get("values")
                 and (m["values"].get("base") or 0) > 0]
        if bases and max(bases) / fv["price"] - 1 < floor / 100:  # ...but if EVERY method says it's above value, skip
            return row | {"verdict": "SKIP", "reason": f"fair value unreliable ({why}) but every method's base is below "
                          f"the price (best {max(bases) / fv['price'] * 100 - 100:+.1f}%; floor {floor:+.0f}%)"}
        return row | {"verdict": "PASS", "reason": f"fair value unreliable ({why}): full research decides"}
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
