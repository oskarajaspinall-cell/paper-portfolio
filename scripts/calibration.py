"""Calibration loop (owner-approved 2026-11-09). Weekly, no model calls.

Measures how our verdicts have actually done and feeds a small, gated correction back into the scorecard:
- excess return of every resolved CORE decision vs its SECTOR benchmark (US sector SPDR ETF; not SPY, so a
  sector's own swing isn't read as a bad call) and vs SPY, at 1, 3 and 6 months, grouped by conviction;
- the share of 4+ verdicts over the last `window` new-name decisions, with an alert outside [band_lo, band_hi]%;
- the quick-check (prescreen) skips' later 1-month return vs SPY (did skipping cost us winners?).

Feedback (scorecard offset, reports/calibration/latest.json), applied by scripts/scorecard.py ONLY when the gate
is met: at least `min_n` resolved decisions at `horizon` in BOTH the 4+ and the 3 group. Estimates are shrunk toward
zero (mean x n / (n + shrink_k)), and the offset is capped at +/-1 point:
- 4+ verdicts trail their sector by more than `tighten_pp` (shrunk)          -> -1 (a 4 gets harder)
- 4+ AND 3 verdicts both beat their sector by more than `loosen_pp` (shrunk) -> +1 (we reject winners)
Otherwise 0. Sector-level penalties are deliberately not used: too few decisions per sector, and marking a sector
down after it underperforms is the opposite of a value process.

Usage: python scripts/calibration.py [--asof YYYY-MM-DD]   -> reports/calibration/<date>.json/.md + latest.json
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

OUT = ROOT / "reports" / "calibration"
SECTOR_ETF = {"Technology": "XLK", "Financials": "XLF", "Healthcare": "XLV", "Consumer Discretionary": "XLY",
              "Consumer Staples": "XLP", "Energy": "XLE", "Industrials": "XLI", "Materials": "XLB",
              "Utilities": "XLU", "Real Estate": "XLRE", "Communication Services": "XLC"}
HORIZONS = {"1m": 30, "3m": 91, "6m": 182}


def settings(cfg: dict) -> dict:
    c = cfg.get("calibration", {})
    return {"window": int(c.get("window", 50)), "band_lo": float(c.get("band_lo", 2)), "band_hi": float(c.get("band_hi", 10)),
            "min_n": int(c.get("min_n", 30)), "horizon": c.get("horizon", "3m"), "shrink_k": float(c.get("shrink_k", 30)),
            "tighten_pp": float(c.get("tighten_pp", 5)), "loosen_pp": float(c.get("loosen_pp", 5))}


def sector_of(ticker: str) -> str | None:
    d = ROOT / "research" / Ticker(ticker).slug
    js = sorted(d.glob("factsheet-*.json"))
    if js:
        try:
            return json.loads(js[-1].read_text()).get("sector")
        except ValueError:
            pass
    md = sorted(d.glob("factsheet-*.md"))
    m = re.search(r"^Sector: ([^\[(·]+)", md[-1].read_text(), re.M) if md else None
    return m.group(1).strip() if m else None


def close_on(rows: list[dict], day: str) -> float | None:
    prior = [r for r in rows if r["date"] <= day]
    return prior[-1]["adj_close"] if prior else None


def shrunk(xs: list[float], k: float) -> float | None:
    return st.mean(xs) * len(xs) / (len(xs) + k) if xs else None


def build(asof: str, cfg: dict, fetcher) -> dict:
    s = settings(cfg)
    rows = [r for r in csv.DictReader((ROOT / "portfolio" / "decisions.csv").open()) if r["type"] == "CORE"]
    etfs: dict[str, list] = {}

    def etf_rows(sym):
        if sym not in etfs:
            try:
                etfs[sym] = fetcher.long_history(sym, etf=True, range_="5Y", period="Weekly")["rows"]
            except DataError:
                etfs[sym] = []
        return etfs[sym]

    groups: dict[str, dict] = {}
    for r in rows:
        g = "4+" if int(r["conviction"] or 0) >= 4 else str(r["conviction"])
        sec = sector_of(r["ticker"])
        etf = SECTOR_ETF.get(sec or "")
        for h, days in HORIZONS.items():
            if not r.get(f"ret_{h}"):
                continue
            ret, spy = float(r[f"ret_{h}"]), float(r[f"spy_{h}"])
            ex_sec = None
            if etf:
                e = etf_rows(etf)
                end = (dt.date.fromisoformat(r["date"]) + dt.timedelta(days=days)).isoformat()
                a, b = close_on(e, r["date"]), close_on(e, end)
                if a and b:
                    ex_sec = ret - (b / a - 1) * 100
            cell = groups.setdefault(g, {}).setdefault(h, {"vs_spy": [], "vs_sector": []})
            cell["vs_spy"].append(ret - spy)
            if ex_sec is not None:
                cell["vs_sector"].append(ex_sec)
    summary = {g: {h: {"n": len(c["vs_spy"]), "mean_vs_spy": st.mean(c["vs_spy"]) if c["vs_spy"] else None,
                       "n_sector": len(c["vs_sector"]),
                       "mean_vs_sector": st.mean(c["vs_sector"]) if c["vs_sector"] else None,
                       "shrunk_vs_sector": shrunk(c["vs_sector"], s["shrink_k"])}
                   for h, c in hs.items()} for g, hs in groups.items()}

    new = [r for r in rows if r["decision"] in ("BUY", "AVOID")][-s["window"]:]
    share = 100 * sum(int(r["conviction"] or 0) >= 4 for r in new) / len(new) if new else None
    alert = share is not None and not (s["band_lo"] <= share <= s["band_hi"])

    h = s["horizon"]
    four, three = (summary.get("4+") or {}).get(h) or {}, (summary.get("3") or {}).get(h) or {}
    gate = (four.get("n_sector") or 0) >= s["min_n"] and (three.get("n_sector") or 0) >= s["min_n"]
    offset = 0
    if gate:
        if four["shrunk_vs_sector"] < -s["tighten_pp"]:
            offset = -1
        elif four["shrunk_vs_sector"] > s["loosen_pp"] and three["shrunk_vs_sector"] > s["loosen_pp"]:
            offset = 1
    return {"asof": asof, "by_conviction": summary, "share_4plus_recent": share, "recent_window": len(new),
            "share_alert": alert, "band": [s["band_lo"], s["band_hi"]], "gate": {"horizon": h, "min_n": s["min_n"],
            "n_4plus": four.get("n_sector") or 0, "n_3": three.get("n_sector") or 0},
            "gate_met": gate, "score_offset": offset, "prescreen": prescreen_check(asof, fetcher)}


def prescreen_check(asof: str, fetcher, max_names: int = 60) -> dict:
    """Skipped names at least a month old: their next-month return vs SPY (a positive mean = skips cost winners)."""
    from portfolio import Market
    rows = []
    for f in sorted((ROOT / "reports" / "prescreen").glob("20??-??-??.csv")):
        rows += [r for r in csv.DictReader(f.open()) if r["verdict"] == "SKIP" and r.get("price")]
    cut = (dt.date.fromisoformat(asof) - dt.timedelta(days=30)).isoformat()
    rows = [r for r in rows if r["asof"] <= cut][-max_names:]
    if not rows:
        return {"n": 0}
    spy = fetcher.long_history("SPY", etf=True, range_="1Y", period="Daily")["rows"]
    ex = []
    for r in rows:
        try:
            h = Market(fetcher, asof, load_config()).history(r["ticker"])["rows"]
        except (DataError, KeyError):
            continue
        end = (dt.date.fromisoformat(r["asof"]) + dt.timedelta(days=30)).isoformat()
        b = [x["close"] for x in h if x["date"] <= end][-1:] if h else []
        s0, s1 = close_on(spy, r["asof"]), close_on(spy, end)
        if b and s0 and s1:
            ex.append((b[0] / float(r["price"]) - 1) * 100 - (s1 / s0 - 1) * 100)
    return {"n": len(ex), "mean_excess_1m": st.mean(ex) if ex else None,
            "share_beat_spy": 100 * sum(x > 0 for x in ex) / len(ex) if ex else None}


def render_md(doc: dict) -> str:
    f = lambda x, d=1: "n/a" if x is None else f"{x:+.{d}f}"  # noqa: E731
    L = [f"# Calibration — {doc['asof']}", "",
         f"- 4+ share of the last {doc['recent_window']} new-name verdicts: {f(doc['share_4plus_recent'])}% "
         f"(target band {doc['band'][0]:g}-{doc['band'][1]:g}%)" + (" **ALERT: outside the band**" if doc["share_alert"] else ""),
         f"- Feedback gate ({doc['gate']['horizon']}, >= {doc['gate']['min_n']} resolved in each group): "
         f"4+ n={doc['gate']['n_4plus']}, 3 n={doc['gate']['n_3']} -> "
         + (f"met, scorecard offset {doc['score_offset']:+d}" if doc["gate_met"] else "not met (report only, offset 0)"),
         f"- Quick-check skips (1 month later vs SPY): n={doc['prescreen'].get('n', 0)}, mean "
         f"{f(doc['prescreen'].get('mean_excess_1m'))}pp, beat SPY {f(doc['prescreen'].get('share_beat_spy'), 0)}%", "",
         "| Conviction | Horizon | n | vs SPY (pp) | n (sector) | vs sector (pp) | shrunk vs sector |", "|---|---|---|---|---|---|---|"]
    for g in sorted(doc["by_conviction"], reverse=True):
        for h, c in doc["by_conviction"][g].items():
            L.append(f"| {g} | {h} | {c['n']} | {f(c['mean_vs_spy'])} | {c['n_sector']} | {f(c['mean_vs_sector'])} | "
                     f"{f(c['shrunk_vs_sector'])} |")
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    cfg = load_config()
    doc = build(a.asof, cfg, Fetcher(cfg))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{a.asof}.json").write_text(json.dumps(doc, indent=1))
    (OUT / f"{a.asof}.md").write_text(render_md(doc))
    (OUT / "latest.json").write_text(json.dumps(doc, indent=1))
    print(f"OK reports/calibration/{a.asof}.md gate_met={doc['gate_met']} offset={doc['score_offset']} "
          f"share_4plus={doc['share_4plus_recent']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
