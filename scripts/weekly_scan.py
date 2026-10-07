"""Weekly scan of every holding. No model calls.

For each holding it reads every daily close since the last run (stockanalysis.com history page) and:
  - flags a price move beyond +/-`weekly_flag_move_pct` (any close vs the reference close),
  - flags an earnings release or new filing dated in the window (stockanalysis.com filings page),
  - flags a CORE invalidation trigger whose `check` is met (stockanalysis.com statistics page),
  - TACTICAL exits, mechanically: the FIRST close that crossed the stop or target (up to the time limit)
    is the fill; if none and the time limit has passed, the last close is the fill,
  - CORE positions above `trim_above_pct` get a mechanical TRIM back to that cap.
Unflagged holdings get a one-line "no material change" entry. Mechanical exits/trims are written as
trade requests and applied later in the run by portfolio.py (so a failed run applies nothing).

Usage:
    python scripts/weekly_scan.py [--asof YYYY-MM-DD] [--out runs/<date>]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402
from fetch_data import Fetcher  # noqa: E402
from portfolio import Market, load_state, mark, totals  # noqa: E402


# --------------------------------------------------------------------------- flag rules (pure)
def reference_close(rows: list[dict], last_run: str | None, entry_close_date: str | None) -> dict | None:
    """The close the week is measured from: the last close before the previous run, or the entry
    close if the position was opened later. rows ascending, completed closes only."""
    if last_run is None:  # first scan: measure from the entry close
        return next((r for r in rows if r["date"] == entry_close_date), rows[0] if rows else None)
    cands = [r for r in rows if r["date"] < last_run]
    ref = cands[-1] if cands else None
    if entry_close_date and (ref is None or entry_close_date > ref["date"]):
        ref = next((r for r in rows if r["date"] == entry_close_date), ref)
    return ref


def window(rows: list[dict], ref: dict) -> list[dict]:
    return [r for r in rows if r["date"] > ref["date"]]


def price_move(ref: dict, win: list[dict], threshold_pct: float) -> dict:
    moves = [(r["close"] / ref["close"] - 1) * 100 for r in win]
    worst = max(moves, key=abs) if moves else 0.0
    return {"flag": abs(worst) > threshold_pct, "max_move_pct": worst,
            "last_move_pct": moves[-1] if moves else 0.0}


def tactical_exit(win: list[dict], plan: dict, asof: str) -> dict | None:
    """First close at/below stop or at/above target (on or before the time limit) -> exit there.
    Otherwise, if the time limit has passed, exit at the last close."""
    limit = plan["time_limit"]
    for r in win:
        if r["date"] > limit:
            break
        if r["close"] <= plan["stop"]:
            return {"fill_date": r["date"], "close": r["close"], "why": f"stop {plan['stop']} crossed"}
        if r["close"] >= plan["target"]:
            return {"fill_date": r["date"], "close": r["close"], "why": f"target {plan['target']} reached"}
    if limit < asof and win:
        last = win[-1]
        return {"fill_date": last["date"], "close": last["close"], "why": f"time limit {limit} passed"}
    return None


def trigger_hits(triggers: list[dict], stats: dict) -> tuple[list[dict], list[str]]:
    """Returns (hits, unchecked). Only `statistics` checks are mechanical; others need a review."""
    hits, unchecked = [], []
    for t in triggers or []:
        chk = t.get("check")
        if not chk or chk.get("source") != "statistics":
            unchecked.append(t.get("text", ""))
            continue
        val = (stats.get(chk["field"]) or {}).get("value")
        if val is None:
            unchecked.append(f"{t.get('text', '')} [data unavailable: {chk['field']}]")
            continue
        hit = val < chk["value"] if chk["op"] == "<" else val > chk["value"]
        if hit:
            hits.append({"text": t.get("text", ""), "field": chk["field"], "value": val,
                         "threshold": f"{chk['op']} {chk['value']}"})
    return hits, unchecked


def events_in_window(events: list[dict], after: str, asof: str) -> list[dict]:
    return [e for e in events if after < e["date"] < asof]


# --------------------------------------------------------------------------- scan
def scan(state: dict, mkt: Market, fetcher, cfg: dict, asof: str) -> dict:
    last_run = state.get("last_scan")
    thr = cfg["agents"]["weekly_flag_move_pct"]
    out = {"asof": asof, "last_run": last_run, "flagged": [], "reinitiate": [], "review": [],
           "unflagged": [], "exits": [], "trims": [], "mechanical_requests": [], "notes": []}
    for t, h in sorted(state["holdings"].items()):
        hist = mkt.history(t)
        ref = reference_close(hist["rows"], last_run, h.get("entry_close_date"))
        if ref is None:
            raise DataError(hist["url"], "history.close", f"no reference close for {t}")
        win = window(hist["rows"], ref)
        mv = price_move(ref, win, thr)
        last = win[-1] if win else ref
        fig = {"ref_date": ref["date"], "ref_close": ref["close"], "last_date": last["date"],
               "last_close": last["close"], "currency": hist["currency"],
               "max_move_pct": round(mv["max_move_pct"], 2), "week_move_pct": round(mv["last_move_pct"], 2),
               "source_url": hist["url"]}
        if h["type"] == "TACTICAL":
            ex = tactical_exit(win, h["exit_plan"], asof)
            if ex:
                out["exits"].append({"ticker": t, **ex, "source_url": hist["url"]})
                out["mechanical_requests"].append({
                    "ticker": t, "action": "SELL", "position_type": "TACTICAL", "fill_date": ex["fill_date"],
                    "reason": f"mechanical exit: {ex['why']} (close {ex['close']} {hist['currency']} on {ex['fill_date']})"})
                continue  # exits need no review
        reasons = []
        if mv["flag"]:
            reasons.append(f"price move {mv['max_move_pct']:+.1f}% vs {ref['date']} close (limit ±{thr}%)")
        fil = fetcher.section(t, "filings")
        evs = events_in_window(fil["data"]["events"], ref["date"], asof)
        if evs:
            reasons.append("new release/filing: " + "; ".join(f"{e['date']} {e['title']} ({', '.join(e['types'])})" for e in evs))
            fig["filings_url"] = fil["source_url"]
        if h["type"] == "CORE":
            st = fetcher.section(t, "statistics")
            hits, unchecked = trigger_hits(h.get("triggers") or [], st["data"])
            if hits:
                reasons.append("core trigger hit: " + "; ".join(f"{x['text']} ({x['field']} = {x['value']} {x['threshold']})" for x in hits))
                fig["statistics_url"] = st["source_url"]
                out["reinitiate"].append(t)
            if unchecked:
                out["notes"].append(f"{t}: triggers without a mechanical check (reviewed when flagged): {unchecked}")
        if reasons:
            from fact_sheet import is_sell_side
            fig["recent_headlines"] = [  # from the history page already downloaded; no extra request
                {k: n[k] for k in ("title", "source", "ago", "url")}
                for n in hist.get("news") or [] if not is_sell_side(n)][:8]
            out["flagged"].append({"ticker": t, "type": h["type"], "reasons": reasons, "figures": fig})
            if t not in out["reinitiate"]:
                out["review"].append(t)
        else:
            out["unflagged"].append({"ticker": t, "line": f"{t}: no material change ({fig['ref_close']}→{fig['last_close']} "
                                                          f"{hist['currency']}, {fig['week_move_pct']:+.1f}%)"})
    # mechanical trims of oversized core positions (weights at latest closes)
    work = json.loads(json.dumps(state))
    mark(work, mkt)
    pv = totals(work)["total"]
    cap = cfg["core"]["trim_above_pct"]
    exited = {e["ticker"] for e in out["exits"]}
    for t, h in work["holdings"].items():
        w = h["market_value_usd"] / pv * 100
        if h["type"] == "CORE" and w > cap and t not in exited:
            out["trims"].append({"ticker": t, "weight_pct": round(w, 2)})
            out["mechanical_requests"].append({
                "ticker": t, "action": "TRIM", "position_type": "CORE", "conviction": h["conviction"],
                "target_weight_pct": cap, "reason": f"mechanical trim: core weight {w:.2f}% above {cap}%"})
    trimmed = {x["ticker"] for x in out["trims"]}
    out["unflagged"] = [u for u in out["unflagged"] if u["ticker"] not in trimmed]  # reported as trims instead
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    cfg = load_config()
    f = Fetcher(cfg)
    try:
        res = scan(load_state(ROOT / "portfolio" / "state.json", cfg), Market(f, a.asof, cfg), f, cfg, a.asof)
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    out = Path(a.out) if a.out else ROOT / "runs" / a.asof
    out.mkdir(parents=True, exist_ok=True)
    (out / "scan.json").write_text(json.dumps(res, indent=1))
    (out / "requests-mechanical.json").write_text(json.dumps(res["mechanical_requests"], indent=1))
    print(json.dumps({"flagged_for_review": res["review"], "reinitiate": res["reinitiate"],
                      "mechanical_exits": [e["ticker"] for e in res["exits"]], "trims": [x["ticker"] for x in res["trims"]],
                      "unflagged": len(res["unflagged"]), "scan": str(out / "scan.json")}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
