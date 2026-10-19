"""Macro regime -> cash reserve (owner rule 2026-10-09: cash is a holding). No model calls.

    python scripts/regime.py [--asof D]               score -> reports/regime/<D>.json and .md
    python scripts/regime.py --apply-view [--asof D]  merge the macro-strategist's checked view
                                                      (reports/regime/<D>-view.md, at most one notch)
    python scripts/regime.py --dip [--asof D]         daily dip check (weekdays, bin/fill-pending; 2026-10-19):
                                                      S&P 500 daily close vs its 52-week high -> reports/regime/dip-<D>.json

A 0-100 stress score from official FRED data (the day's macro snapshot) and the S&P 500 trend
(stockanalysis.com weekly chart data): each indicator scores 0-1 between calm and stressed levels in CLAUDE.md
[cash_strategy.indicators], weighted. The score maps linearly to the cash RESERVE (5-35%; new buys can't take
cash below it), moving at most 5pp a week; the macro view may move it one notch (5pp). When the S&P 500
falls far enough below its 52-week high, the reserve is released in steps (buy the dip). A missing
indicator scores 0 and is listed as [data unavailable]; nothing is guessed.
The regime itself (score + macro view) is set weekly; the dip release is re-checked daily from daily closes, so
a sell-off releases the reserve the next morning instead of at the next weekly run (and a recovery restores it).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402

OUT = ROOT / "reports" / "regime"
REGIMES = ("risk_on", "neutral", "defensive")
LABEL = {"risk_on": "risk-on", "neutral": "neutral", "defensive": "defensive"}
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="


def _series(snap: dict, sid: str) -> dict | None:
    for s in snap.get("series", []):
        if s["id"] == sid and isinstance(s.get("value"), (int, float)):
            return s
    return None


# (key, label, FRED source or None, how the value is read). Anchors (calm, stressed) and weights: CLAUDE.md
# [cash_strategy.indicators]. 2026-10-19 (owner request "advance the cash reserve"): each indicator scores 0-1 on
# a sliding scale between its calm and stressed levels instead of a 0/1 threshold, so near-misses count and one
# indicator can't flip the reserve by a whole step. Fixed anchors, not percentiles: FRED serves only ~3 years of
# the high-yield spread, too short a history to rank against.
INDICATORS = [
    ("hy_spread", "High-yield credit spread, %", "BAMLH0A0HYM2"),
    ("hy_widening_3m", "High-yield spread, 3m change, pp", "BAMLH0A0HYM2"),
    ("vix", "VIX", "VIXCLS"),
    ("curve_10y_2y", "Yield curve, 10y - 2y, pp", "DGS10, DGS2"),
    ("real_yield_3m", "Real 10y yield, 3m change, pp", "DFII10"),
    ("spy_vs_40w", "S&P 500 vs its 40-week (~200-day) average, %", None),
    ("core_cpi_3m_ann", "US core CPI, 3m annualised, %", "CPILFESL"),
    ("fed_funds_3m", "Fed funds rate, 3m change, pp", "DFF"),
]


def indicator_values(snap: dict, spy: dict | None) -> dict[str, tuple]:
    """key -> (value, date) from the macro snapshot and the S&P 500 trend; missing -> absent."""
    v = {}
    hy = _series(snap, "BAMLH0A0HYM2")
    if hy:
        v["hy_spread"] = (hy["value"], hy["date"])
        if hy.get("chg_3m") is not None:
            v["hy_widening_3m"] = (hy["chg_3m"], hy["date"])
    vix = _series(snap, "VIXCLS")
    if vix:
        v["vix"] = (vix["value"], vix["date"])
    t10, t2 = _series(snap, "DGS10"), _series(snap, "DGS2")
    if t10 and t2:
        v["curve_10y_2y"] = (round(t10["value"] - t2["value"], 3), max(t10["date"], t2["date"]))
    ry = _series(snap, "DFII10")
    if ry and ry.get("chg_3m") is not None:
        v["real_yield_3m"] = (ry["chg_3m"], ry["date"])
    if spy and spy.get("avg_40w"):
        v["spy_vs_40w"] = (round((spy["close"] / spy["avg_40w"] - 1) * 100, 2), spy["date"])
    cpi = _series(snap, "CPILFESL")
    if cpi and cpi.get("chg_3m") is not None and cpi["value"] - cpi["chg_3m"] > 0:
        v["core_cpi_3m_ann"] = (round(((cpi["value"] / (cpi["value"] - cpi["chg_3m"])) ** 4 - 1) * 100, 2), cpi["date"])
    ff = _series(snap, "DFF")
    if ff and ff.get("chg_3m") is not None:
        v["fed_funds_3m"] = (ff["chg_3m"], ff["date"])
    return v


def slide(value: float, calm: float, stressed: float) -> float:
    """0 at (or beyond) the calm level, 1 at (or beyond) the stressed level, linear between."""
    return max(0.0, min(1.0, (value - calm) / (stressed - calm)))


def score_indicators(snap: dict, spy: dict | None, cs: dict) -> list[dict]:
    """Each indicator: value, its 0-1 stress score and weight. Missing data -> weight 0, flagged (never guessed)."""
    vals, out = indicator_values(snap, spy), []
    for key, name, fred in INDICATORS:
        a = cs["indicators"][key]
        src = (", ".join(FRED + x.strip() for x in fred.split(",")) if fred else
               (spy or {}).get("source", "https://stockanalysis.com/etf/spy/history/"))
        rule = f"calm {a['calm']} -> stressed {a['stressed']}"
        if key not in vals:
            out.append({"key": key, "name": name, "value": "[data unavailable]", "date": None, "score": None,
                        "weight": 0, "rule": rule, "source": src})
            continue
        val, date = vals[key]
        out.append({"key": key, "name": name, "value": val, "date": date,
                    "score": round(slide(val, a["calm"], a["stressed"]), 3), "weight": a.get("weight", 1),
                    "rule": rule, "source": src})
    return out


def stress_of(ind: list[dict]) -> float | None:
    """Weighted mean of the available scores, 0-100; None when too few indicators are available."""
    have = [i for i in ind if i["score"] is not None and i["weight"]]
    if len(have) < 5:
        return None
    return round(sum(i["score"] * i["weight"] for i in have) / sum(i["weight"] for i in have) * 100, 1)


def reserve_for(stress: float, cs: dict) -> float:
    lo, hi = cs["reserve_min_pct"], cs["reserve_max_pct"]
    return round((lo + (hi - lo) * stress / 100) * 2) / 2  # nearest 0.5pp


def regime_for(stress: float, cs: dict) -> str:
    """Label (for the macro view and reports): stress below the first band is risk-on, below the second neutral."""
    b1, b2 = cs["regime_bands"]
    return "risk_on" if stress < b1 else "neutral" if stress < b2 else "defensive"


def dip_multiplier(drawdown_pct: float | None, cs: dict) -> float:
    """Reserve multiplier from the S&P 500's drawdown below its 52-week high (stepwise release)."""
    m = 1.0
    for dd, mult in sorted(cs["dip_steps"]):
        if drawdown_pct is not None and drawdown_pct >= dd:
            m = mult
    return float(m)


def spy_trend(fetcher, asof: str) -> dict:
    h = fetcher.long_history("SPY", etf=True)
    rows = [r for r in h["rows"] if r["date"] < asof and r.get("close")]
    if len(rows) < 52:
        raise DataError(h["source_url"], "history", "fewer than 52 weekly closes")
    last = rows[-1]
    hi = max(r["close"] for r in rows[-52:])
    return {"close": last["close"], "date": last["date"], "avg_40w": sum(r["close"] for r in rows[-40:]) / 40,
            "high_52w": hi, "drawdown_pct": round((1 - last["close"] / hi) * 100, 2), "source": h["source_url"]}


def spy_dip_daily(fetcher, asof: str) -> dict:
    """The S&P 500 (SPY) daily close before asof vs its 52-week (252-session) high, stockanalysis.com."""
    h = fetcher.long_history("SPY", etf=True, range_="1Y", period="Daily")
    rows = [r for r in h["rows"] if r["date"] < asof and r.get("close")]
    if len(rows) < 200:
        raise DataError(h["source_url"], "history", "fewer than 200 daily closes")
    last, hi = rows[-1], max(r["close"] for r in rows[-252:])
    return {"close": last["close"], "date": last["date"], "high_52w": hi,
            "drawdown_pct": round((1 - last["close"] / hi) * 100, 2), "source": h["source_url"]}


def dip_doc(spy: dict, cfg: dict, asof: str) -> dict:
    return {"asof": asof, "spy": spy, "drawdown_pct": spy["drawdown_pct"],
            "multiplier": dip_multiplier(spy["drawdown_pct"], cfg["cash_strategy"])}


def latest_dip(asof: str, after: str, out: Path = OUT) -> dict | None:
    """The newest daily dip check dated after the weekly regime file (`after`) and on/before asof."""
    files = sorted(p for p in out.glob("dip-20??-??-??.json") if after < p.stem[4:] <= asof)
    return json.loads(files[-1].read_text()) if files else None


def build(snap: dict, spy: dict | None, cfg: dict, asof: str, prev: dict | None = None) -> dict:
    """Stress score -> reserve between [cash_strategy].reserve_min_pct and reserve_max_pct, moving at most
    max_weekly_change_pp from the previous weekly file's score reserve (no whipsaw). Too few indicators: last
    week's score reserve stands (or the fallback). The dip release multiplies the result."""
    cs = cfg["cash_strategy"]
    ind = score_indicators(snap, spy, cs)
    stress = stress_of(ind)
    prev = prev or {}  # a pre-2026-10-19 file has no score reserve: its final reserve is the starting point
    last = prev.get("score_reserve_pct", prev.get("base_reserve_pct"))
    if stress is None:
        raw, note = (last if last is not None else float(cs["fallback_reserve_pct"])), "too few indicators: previous reserve kept"
    else:
        raw, note = reserve_for(stress, cs), None
    score_res = raw
    if last is not None and stress is not None:
        cap = cs["max_weekly_change_pp"]
        score_res = max(last - cap, min(last + cap, raw))
    reg = regime_for(stress if stress is not None else 50.0, cs)
    dd = (spy or {}).get("drawdown_pct")
    mult = dip_multiplier(dd, cs)
    return {"asof": asof, "indicators": ind, "stress": stress, "unsmoothed_reserve_pct": raw,
            "previous_score_reserve_pct": last, "score_reserve_pct": score_res, "note": note,
            "score_regime": reg, "final_regime": reg, "view": None, "view_adjust_pp": 0,
            "spy": spy, "dip": {"drawdown_pct": dd, "multiplier": mult},
            "base_reserve_pct": score_res, "reserve_pct": round(score_res * mult, 2)}


def apply_view(doc: dict, view: dict, cfg: dict) -> dict:
    """Merge a checked macro-strategist view: each notch from the score's label moves the reserve by
    view_notch_pp (at most `notch_override` notches), kept within the min/max."""
    cs = cfg["cash_strategy"]
    i, j = REGIMES.index(doc["score_regime"]), REGIMES.index(view["final_regime"])
    if abs(i - j) > cs["notch_override"]:
        raise ValueError(f"view moves {abs(i - j)} notches (max {cs['notch_override']})")
    adj = (j - i) * cs["view_notch_pp"]
    base = max(cs["reserve_min_pct"], min(cs["reserve_max_pct"], doc["score_reserve_pct"] + adj))
    doc.update(final_regime=view["final_regime"], view=view, view_adjust_pp=adj, base_reserve_pct=base)
    doc["reserve_pct"] = round(base * doc["dip"]["multiplier"], 2)
    return doc


def view_from_md(md: str) -> dict:
    m = re.search(r"```json\s*(\{.*?\})\s*```\s*$", md.strip(), re.S)
    if not m:
        raise ValueError("no json block at the end of the view")
    return json.loads(m.group(1))


def latest(asof: str, out: Path = OUT) -> dict | None:
    """The most recent regime file dated on/before asof."""
    files = sorted(p for p in out.glob("20??-??-??.json") if p.stem <= asof)
    return json.loads(files[-1].read_text()) if files else None


def render_md(doc: dict) -> str:
    st = "n/a" if doc.get("stress") is None else f"{doc['stress']:g}"
    smooth = (f"; capped at a {doc['previous_score_reserve_pct']:g}% -> {doc['score_reserve_pct']:g}% weekly move "
              f"(unsmoothed {doc['unsmoothed_reserve_pct']:g}%)"
              if doc.get("previous_score_reserve_pct") is not None
              and doc["score_reserve_pct"] != doc["unsmoothed_reserve_pct"] else "")
    L = [f"# Cash strategy — {doc['asof']}",
         f"Stress score **{st}/100** ({LABEL[doc['score_regime']]}) → score reserve {doc['score_reserve_pct']:g}%"
         + smooth + (f"; {doc['note']}" if doc.get("note") else "")
         + (f"; macro view {doc['view_adjust_pp']:+g}pp ({LABEL[doc['final_regime']]})" if doc.get("view_adjust_pp") else "")
         + f". Cash reserve **{doc['reserve_pct']:g}%** of the portfolio"
         + (f" (× {doc['dip']['multiplier']:g} dip release: S&P 500 {doc['dip']['drawdown_pct']:.1f}% below its 52-week high)"
            if doc["dip"]["multiplier"] < 1 else
            f" (S&P 500 {doc['dip']['drawdown_pct']:.1f}% below its 52-week high, no dip release)"
            if doc["dip"]["drawdown_pct"] is not None else "") + ".",
         "New buys can't take cash below the reserve (they must name a holding to replace); nothing is sold to reach it.",
         "", "| Indicator | Value | Date | Stress (0-1) | Weight | Scale | Source |", "|---|---|---|---|---|---|---|"]
    for i in doc["indicators"]:
        sc = "" if i["score"] is None else f"{i['score']:.2f}"
        L.append(f"| {i['name']} | {i['value']} | {i['date'] or ''} | {sc} | {i['weight']} | {i['rule']} | {i['source']} |")
    if doc.get("view"):
        L += ["", "Macro view:"] + [f"- {r['text']} ({r['source']})" for r in doc["view"].get("reasons", [])]
    return "\n".join(L) + "\n"


def write(doc: dict, out: Path = OUT):
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{doc['asof']}.json").write_text(json.dumps(doc, indent=1))
    (out / f"{doc['asof']}.md").write_text(render_md(doc))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--apply-view", action="store_true")
    ap.add_argument("--dip", action="store_true")
    a = ap.parse_args(argv)
    cfg = load_config()
    if a.dip:
        from fetch_data import Fetcher
        try:
            d = dip_doc(spy_dip_daily(Fetcher(cfg, refresh=True), a.asof), cfg, a.asof)
        except DataError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"dip-{a.asof}.json").write_text(json.dumps(d, indent=1))
        wk = latest(a.asof)
        base = (wk or {}).get("base_reserve_pct", cfg["cash_strategy"]["fallback_reserve_pct"])
        print(json.dumps({"asof": a.asof, "spy_close": d["spy"]["close"], "close_date": d["spy"]["date"],
                          "high_52w": d["spy"]["high_52w"], "drawdown_pct": d["drawdown_pct"],
                          "multiplier": d["multiplier"], "weekly_regime": (wk or {}).get("final_regime"),
                          "reserve_pct": round(base * d["multiplier"], 2)}))
        return 0
    if a.apply_view:
        doc = json.loads((OUT / f"{a.asof}.json").read_text())
        doc = apply_view(doc, view_from_md((OUT / f"{a.asof}-view.md").read_text()), cfg)
        write(doc)
    else:
        snap_p = ROOT / "reports" / "macro" / f"{a.asof}.json"
        if not snap_p.exists():
            print(f"ERROR: no macro snapshot {snap_p.relative_to(ROOT)}; run scripts/macro_data.py first", file=sys.stderr)
            return 2
        from fetch_data import Fetcher
        try:
            spy = spy_trend(Fetcher(cfg), a.asof)
        except DataError as e:
            print(f"!! S&P 500 trend unavailable: {e}", file=sys.stderr)
            spy = None
        prev = latest((dt.date.fromisoformat(a.asof) - dt.timedelta(days=1)).isoformat())
        doc = build(json.loads(snap_p.read_text()), spy, cfg, a.asof, prev)
        write(doc)
    print(json.dumps({k: doc.get(k) for k in ("asof", "stress", "score_regime", "score_reserve_pct", "final_regime",
                                              "reserve_pct")}
                     | {"drawdown_pct": doc["dip"]["drawdown_pct"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
