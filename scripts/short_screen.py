"""Shadow short candidates (owner 2026-11-18; SHADOW ONLY: nothing here trades). No model calls.

    python scripts/short_screen.py [--asof D]     -> reports/short-screen/<date>.json and .md

A candidate is the latest CORE AVOID at conviction <= [short].max_conviction, at most max_age_days old, whose
fact sheet shows earnings at a cyclical peak (ROIC or operating margin far above its own 5-year median, with a
positive margin) and that passes the guards (short interest, size, takeover, results due, held / on the buy watch).
Each gets a confidence score 0-7 (`confidence`); it QUALIFIES when the score is at least min_confidence and the
trend has turned (close below a falling 50-day average). Fair value is not used: a DCF on peak earnings makes a
peaking cyclical look fairly priced (replay 2026-11-18: with it, none of SNDK, WDC, VLO, NVDA passed).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

OUT = ROOT / "reports" / "short-screen"
TAKEOVER = re.compile(r"takeover|cash bid|tender offer|merger agreement|definitive agreement|to be acquired|buyout",
                      re.I)
MONTHS = {m: i + 1 for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                                          "Dec"])}


def _num(s: str) -> float | None:
    m = re.search(r"(-?[\d,]+\.?\d*)", s.replace("+", ""))
    return float(m.group(1).replace(",", "")) if m else None


def fact_sheet_signals(md: str) -> dict:
    """The fields the screen needs from a fact sheet's markdown (first annual table only)."""
    d: dict = {}
    for line in md.splitlines():
        if line.startswith("Sector:"):
            m = re.search(r"Industry: ([^\[·]+)", line)
            d["industry"] = m.group(1).strip() if m else ""
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 2:
            continue
        k = c[0]
        if k.startswith("Short interest (% float)"):
            d["short_interest"] = _num(c[1])
        elif k.startswith("vs 200-day MA"):
            d["vs_200d"] = _num(c[1])
        elif k.startswith("12-month (52-week) change"):
            d["change_12m"] = _num(c[1])
        elif k.startswith("Next earnings date"):
            m = re.search(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})", c[1])
            d["next_results"] = dt.date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2))).isoformat() if m else None
        elif len(c) >= 8 and k in ("ROIC", "Operating margin") and k not in d:
            hist = [v for v in (_num(x) for x in c[1:6]) if v is not None]
            ttm = _num(c[6])
            d[k] = {"ttm": ttm, "peak_pp": None if ttm is None or not hist else ttm - st.median(hist)}
    return d


def confidence(sig: dict, conviction: int, cfg: dict) -> int:
    """0-7: how strong the peak-cycle short case is (owner 2026-11-18: only the shorts we are most confident in)."""
    s = cfg["short"]
    rp = (sig.get("ROIC") or {}).get("peak_pp")
    mp = (sig.get("Operating margin") or {}).get("peak_pp")
    pts = 0
    if rp is not None:
        pts += 2 if rp >= s["roic_peak_pp_strong"] else 1 if rp >= s["roic_peak_pp"] else 0
    if mp is not None:
        pts += 2 if mp >= s["margin_peak_pp_strong"] else 1 if mp >= s["margin_peak_pp"] else 0
    pts += conviction == 1
    pts += (sig.get("vs_200d") or -999) >= s["stretched_200d_pct"]
    pts += (sig.get("change_12m") or -999) >= s["parabolic_12m_pct"]
    return int(pts)


def peak_cycle(sig: dict, cfg: dict) -> bool:
    s = cfg["short"]
    rp = (sig.get("ROIC") or {}).get("peak_pp")
    om = sig.get("Operating margin") or {}
    if (om.get("ttm") or 0) <= 0:
        return False  # shrinking losses are not a peak (ASTS, ONDS, CRWV showed +147-467pp)
    return (rp is not None and rp >= s["roic_peak_pp"]) or (om.get("peak_pp") or -999) >= s["margin_peak_pp"]


def trend_turned(closes: list[float]) -> bool:
    """Close below its 50-day average and the 50-day lower than 5 sessions ago (don't short strength)."""
    if len(closes) < 55:
        return False
    sma = sum(closes[-50:]) / 50
    return closes[-1] < sma < sum(closes[-55:-5]) / 50


def adr_map() -> dict[str, str]:
    """Foreign ticker -> its US-listed share with listed options (universe/adr_map.csv)."""
    p = ROOT / "universe" / "adr_map.csv"
    if not p.exists():
        return {}
    with p.open() as fh:
        return {r["ticker"]: r["adr"] for r in csv.DictReader(fh)}


def guards(sig: dict, eval_md: str, market_cap_usd_bn: float | None, asof: str, held: bool, watched: bool,
           cfg: dict, ticker: str = "", adr: str | None = None) -> list[str]:
    s, out = cfg["short"], []
    ex = Ticker(ticker).exchange if ticker else None
    if ex in s.get("restricted_markets", []) and not adr:
        out.append(f"shorting restricted in {ex} and no US-listed share")
    if (sig.get("short_interest") or 0) > s["max_short_interest_pct"]:
        out.append(f"crowded: short interest {sig['short_interest']:g}%")
    if market_cap_usd_bn is not None and market_cap_usd_bn < s["min_market_cap_usd_bn"]:
        out.append(f"small: ${market_cap_usd_bn:.1f}bn")
    if TAKEOVER.search(eval_md):
        out.append("takeover / bid mentioned in the research")
    nr = sig.get("next_results")
    if nr and asof <= nr <= (dt.date.fromisoformat(asof) + dt.timedelta(days=s["results_blackout_days"] + 2)).isoformat():
        out.append(f"results due {nr}")
    if held:
        out.append("held")
    if watched:
        out.append("on the buy watchlist")
    return out


def screen(asof: str, cfg: dict, mkt) -> list[dict]:
    s = cfg["short"]
    cut = (dt.date.fromisoformat(asof) - dt.timedelta(days=s["max_age_days"])).isoformat()
    latest: dict[str, dict] = {}
    with (ROOT / "portfolio" / "decisions.csv").open() as fh:
        for r in csv.DictReader(fh):
            latest[r["ticker"]] = r
    caps = {}
    with (ROOT / "universe" / "universe.csv").open() as fh:
        for r in csv.DictReader(fh):
            try:
                caps[r["ticker"]] = float(r["market_cap_usd"]) / 1e9
            except (TypeError, ValueError):
                pass
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    import entry_watch
    watched = {r["ticker"] for r in entry_watch.read()}
    adrs = adr_map()
    out = []
    for t, r in latest.items():
        if r["type"] != "CORE" or r["decision"] != "AVOID" or int(r["conviction"] or 9) > s["max_conviction"] or r["date"] < cut:
            continue
        ev = ROOT / r["evaluation"]
        fs = ev.parent / f"factsheet-{ev.name[:10]}.md"
        if not fs.exists():
            continue
        sig = fact_sheet_signals(fs.read_text())
        if not peak_cycle(sig, cfg):
            continue
        g = guards(sig, ev.read_text() if ev.exists() else "", caps.get(t), asof, t in state.get("holdings", {}),
                   t in watched, cfg, t, adrs.get(t))
        try:
            closes = [x["close"] for x in mkt.history(t)["rows"] if x.get("close") and x["date"] <= asof]
            q = mkt.quote(t, asof)
        except DataError as e:
            g.append(f"no prices ({e.field})")
            closes, q = [], None
        score = confidence(sig, int(r["conviction"]), cfg)
        turned = trend_turned(closes)
        out.append({"ticker": t, "decided": r["date"], "conviction": int(r["conviction"]), "evaluation": r["evaluation"],
                    "industry": sig.get("industry", ""), "confidence": score, "trend_turned": turned, "guards": g,
                    "roic_peak_pp": (sig.get("ROIC") or {}).get("peak_pp"),
                    "margin_peak_pp": (sig.get("Operating margin") or {}).get("peak_pp"),
                    "vs_200d": sig.get("vs_200d"), "change_12m": sig.get("change_12m"),
                    "short_interest": sig.get("short_interest"), "adr": adrs.get(t), "close": q and q["close"], "close_date": q and q["date"],
                    "currency": q and q["currency"],
                    "qualifies": not g and turned and score >= s["min_confidence"]})
    out.sort(key=lambda c: (-c["qualifies"], -c["confidence"], c["ticker"]))
    return out


def render_md(asof: str, cands: list[dict], cfg: dict) -> str:
    s = cfg["short"]
    L = [f"# Shadow short screen — {asof}", "",
         f"SHADOW ONLY: nothing here trades. Qualifies = confidence >= {s['min_confidence']}/7, trend turned, no guard.", "",
         "| Ticker | Researched | Conv. | Confidence | ROIC / margin vs 5y | vs 200-day | 12m | Trend turned | Guards | Qualifies |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    f = lambda x, d=0: "–" if x is None else f"{x:+.{d}f}"  # noqa: E731
    for c in cands:
        L.append(f"| {c['ticker']} | {c['decided']} | {c['conviction']} | {c['confidence']} | {f(c['roic_peak_pp'])} / "
                 f"{f(c['margin_peak_pp'])} | {f(c['vs_200d'])}% | {f(c['change_12m'])}% | {'yes' if c['trend_turned'] else 'no'} | "
                 f"{'; '.join(c['guards']) or '–'} | {'**yes**' if c['qualifies'] else 'no'} |")
    if not cands:
        L.append("| – | | | | | | | | | none |")
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    cfg = load_config()
    from fetch_data import Fetcher
    from portfolio import Market, price_provider
    mkt = Market(Fetcher(cfg), a.asof, cfg, price_provider(cfg))
    cands = screen(a.asof, cfg, mkt)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{a.asof}.json").write_text(json.dumps({"asof": a.asof, "candidates": cands}, indent=1))
    (OUT / f"{a.asof}.md").write_text(render_md(a.asof, cands, cfg))
    print(json.dumps({"candidates": len(cands), "qualify": [c["ticker"] for c in cands if c["qualifies"]]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
