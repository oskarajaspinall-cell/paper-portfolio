"""Macro regime -> cash reserve (owner rule 2026-10-09: cash is a holding). No model calls.

    python scripts/regime.py [--asof D]               score -> reports/regime/<D>.json and .md
    python scripts/regime.py --apply-view [--asof D]  merge the macro-strategist's checked view
                                                      (reports/regime/<D>-view.md, at most one notch)

Risk points from official FRED data (the day's macro snapshot) and the S&P 500 trend (stockanalysis.com
weekly chart data); thresholds in CLAUDE.md [cash_strategy]. 0-1 points = risk-on, 2-3 = neutral,
4+ = defensive. The regime sets the cash RESERVE (new buys can't take cash below it). When the S&P 500
falls far enough below its 52-week high, the reserve is released in steps (buy the dip). A missing
indicator scores 0 and is listed as [data unavailable]; nothing is guessed.
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


def score_indicators(snap: dict, spy: dict | None, cs: dict) -> list[dict]:
    """Each indicator: value, the rule, points. Missing data -> 0 points, flagged."""
    out = []

    def add(name, value, date, points, rule, source):
        out.append({"name": name, "value": value, "date": date, "points": points, "rule": rule, "source": source})

    hy = _series(snap, "BAMLH0A0HYM2")
    if hy:
        p = int(hy["value"] > cs["hy_spread_high"]) + int((hy.get("chg_3m") or 0) > cs["hy_widening_3m"])
        add("High-yield credit spread, %", hy["value"], hy["date"], p,
            f">{cs['hy_spread_high']} (+1); widened >{cs['hy_widening_3m']}pp in 3m (+1); 3m change {hy.get('chg_3m')}",
            FRED + "BAMLH0A0HYM2")
    else:
        add("High-yield credit spread, %", "[data unavailable]", None, 0, "", FRED + "BAMLH0A0HYM2")
    vix = _series(snap, "VIXCLS")
    if vix:
        p = 2 if vix["value"] > cs["vix_extreme"] else int(vix["value"] > cs["vix_high"])
        add("VIX", vix["value"], vix["date"], p, f">{cs['vix_high']} (+1), >{cs['vix_extreme']} (+2)", FRED + "VIXCLS")
    else:
        add("VIX", "[data unavailable]", None, 0, "", FRED + "VIXCLS")
    t10, t2 = _series(snap, "DGS10"), _series(snap, "DGS2")
    if t10 and t2:
        c = round(t10["value"] - t2["value"], 3)
        add("Yield curve, 10y - 2y, pp", c, max(t10["date"], t2["date"]), int(c < 0), "< 0 inverted (+1)",
            FRED + "DGS10, " + FRED + "DGS2")
    else:
        add("Yield curve, 10y - 2y, pp", "[data unavailable]", None, 0, "", FRED + "DGS10")
    ry = _series(snap, "DFII10")
    if ry:
        ch = ry.get("chg_3m")
        add("Real 10y yield, 3m change, pp", ch, ry["date"], int((ch or 0) > cs["real_yield_rise_3m"]),
            f"rose >{cs['real_yield_rise_3m']}pp in 3m (+1); level {ry['value']}%", FRED + "DFII10")
    else:
        add("Real 10y yield, 3m change, pp", "[data unavailable]", None, 0, "", FRED + "DFII10")
    if spy and spy.get("avg_40w"):
        below = spy["close"] < spy["avg_40w"]
        add("S&P 500 vs its 40-week (~200-day) average, %", round((spy["close"] / spy["avg_40w"] - 1) * 100, 2),
            spy["date"], int(below), "below the average (+1)", spy["source"])
    else:
        add("S&P 500 vs its 40-week (~200-day) average, %", "[data unavailable]", None, 0, "",
            (spy or {}).get("source", ""))
    return out


def regime_for(points: int, cs: dict) -> str:
    if points >= cs["defensive_from"]:
        return "defensive"
    return "neutral" if points >= cs["neutral_from"] else "risk_on"


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


def build(snap: dict, spy: dict | None, cfg: dict, asof: str) -> dict:
    cs = cfg["cash_strategy"]
    ind = score_indicators(snap, spy, cs)
    pts = sum(i["points"] for i in ind)
    reg = regime_for(pts, cs)
    dd = (spy or {}).get("drawdown_pct")
    mult = dip_multiplier(dd, cs)
    return {"asof": asof, "indicators": ind, "points": pts, "score_regime": reg, "final_regime": reg, "view": None,
            "spy": spy, "dip": {"drawdown_pct": dd, "multiplier": mult},
            "base_reserve_pct": cs["reserve_pct"][reg], "reserve_pct": round(cs["reserve_pct"][reg] * mult, 2)}


def apply_view(doc: dict, view: dict, cfg: dict) -> dict:
    """Merge a checked macro-strategist view: final regime at most `notch_override` from the score."""
    cs = cfg["cash_strategy"]
    i, j = REGIMES.index(doc["score_regime"]), REGIMES.index(view["final_regime"])
    if abs(i - j) > cs["notch_override"]:
        raise ValueError(f"view moves {abs(i - j)} notches (max {cs['notch_override']})")
    doc.update(final_regime=view["final_regime"], view=view, base_reserve_pct=cs["reserve_pct"][view["final_regime"]])
    doc["reserve_pct"] = round(doc["base_reserve_pct"] * doc["dip"]["multiplier"], 2)
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
    L = [f"# Cash strategy — {doc['asof']}",
         f"Regime **{LABEL[doc['final_regime']]}** (score {doc['points']} → {LABEL[doc['score_regime']]}"
         + (f"; macro view moved it to {LABEL[doc['final_regime']]}" if doc["final_regime"] != doc["score_regime"] else "")
         + f"). Cash reserve **{doc['reserve_pct']:g}%** of the portfolio (base {doc['base_reserve_pct']:g}%"
         + (f", × {doc['dip']['multiplier']:g} dip release: S&P 500 {doc['dip']['drawdown_pct']:.1f}% below its 52-week high"
            if doc["dip"]["multiplier"] < 1 else
            f"; S&P 500 {doc['dip']['drawdown_pct']:.1f}% below its 52-week high, no dip release"
            if doc["dip"]["drawdown_pct"] is not None else "") + ").",
         "New buys can't take cash below the reserve (they must name a holding to replace); nothing is sold to reach it.",
         "", "| Indicator | Value | Date | Points | Rule | Source |", "|---|---|---|---|---|---|"]
    for i in doc["indicators"]:
        L.append(f"| {i['name']} | {i['value']} | {i['date'] or ''} | {i['points']} | {i['rule']} | {i['source']} |")
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
    a = ap.parse_args(argv)
    cfg = load_config()
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
        doc = build(json.loads(snap_p.read_text()), spy, cfg, a.asof)
        write(doc)
    print(json.dumps({k: doc[k] for k in ("asof", "points", "score_regime", "final_regime", "reserve_pct")}
                     | {"drawdown_pct": doc["dip"]["drawdown_pct"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
