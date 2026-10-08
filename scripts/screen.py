"""Weekly screen: rank the universe and pick this week's new initiations. No model calls.

For every screenable stock in universe/universe.csv (minus holdings and names researched in the
last `exclude_researched_days`), read its stockanalysis.com statistics page and score three pillars
by percentile rank within the screened set (config [screen]):
    quality, valuation, momentum (price vs 50/200-day computed from the page's own quote and averages)
Core score = mean(quality, valuation). Stage 2: the top `deep_dive_top` core candidates also get
their ratios page (5-year history) read, adding a history pillar (valuation vs own 5y range,
ROIC/ROCE trend, worst-year ROIC); they are ranked by mean(quality, valuation, history).
Tactical (owner rule 2026-10-08, scripts/setups.py): two setups. Stage 1 from the statistics page:
post-earnings-drift candidates (results just reported, above the 50-day average) and pullback candidates
(uptrend intact, back near the 50-day average, RSI cooled, no earnings for a month). Stage 2 reads the
daily history of the top `tactical_check_top` of each to confirm the earnings reaction and size a
volatility stop (ATR). Picks alternate between the two setups.

A page that fails to load or parse is EXCLUDED and listed in the report (never guessed). Pages are
cached per day, so an interrupted run resumes where it stopped.

Usage:
    python scripts/screen.py [--asof YYYY-MM-DD] [--limit N] [--index SP500|FTSE100|ALLWORLD]
Writes reports/screen/<date>.md (ranked tables with source URLs) and reports/screen/<date>.json (picks).
With --index (an ad-hoc screen of one index, percentiles within that index) the files are
<date>-<index>.md/.json, so the weekly run's pick list is never replaced.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config, page_url  # noqa: E402
from fetch_data import Fetcher, page_nodes, parse_info, parse_statistics  # noqa: E402
import setups  # noqa: E402
from universe import read_universe  # noqa: E402

OUT = ROOT / "reports" / "screen"


def stock_metrics(stats: dict, info: dict) -> dict:
    """Flatten the statistics page into the numbers the screen uses (percent fields in percent)."""
    v = {k: (d or {}).get("value") for k, d in stats.items()}
    price = info["quote"].get("last") or info["quote"].get("prev_close")
    for k, ma in (("price_vs_sma200", "sma200"), ("price_vs_sma50", "sma50")):
        v[k] = (price / v[ma] - 1) * 100 if price and v.get(ma) else None
    ed = (stats.get("earningsdate") or {}).get("text")
    try:
        v["earnings_date"] = dt.datetime.strptime(ed, "%b %d, %Y").date().isoformat() if ed else None
    except ValueError:
        v["earnings_date"] = None
    v["price"] = price
    return v


def percentile_ranks(values: dict[str, float | None], higher_better: bool) -> dict[str, float]:
    """Percentile (0-100) of each non-missing value; ties share the average rank."""
    xs = sorted((x, t) for t, x in values.items() if x is not None)
    n = len(xs)
    out: dict[str, float] = {}
    i = 0
    while i < n:
        j = i
        while j + 1 < n and xs[j + 1][0] == xs[i][0]:
            j += 1
        pct = ((i + j) / 2) / (n - 1) * 100 if n > 1 else 50.0
        for k in range(i, j + 1):
            out[xs[k][1]] = pct if higher_better else 100 - pct
        i = j + 1
    return out


def pillar_scores(metrics: dict[str, dict], spec: list[str], min_metrics: int) -> dict[str, float | None]:
    ranks = []
    for m in spec:
        key, hb = (m[1:], False) if m.startswith("-") else (m, True)
        vals = {t: d.get(key) for t, d in metrics.items()}
        if not hb:  # a negative multiple/leverage is not "cheap"/"low"; treat as missing
            vals = {t: (x if x is not None and x > 0 else None) for t, x in vals.items()}
        ranks.append(percentile_ranks(vals, hb))
    out = {}
    for t in metrics:
        got = [r[t] for r in ranks if t in r]
        out[t] = st.mean(got) if len(got) >= min_metrics else None
    return out


def score(metrics: dict[str, dict], cfg: dict, asof: str) -> list[dict]:
    sc = cfg["screen"]
    q = pillar_scores(metrics, sc["quality"], sc["min_metrics_per_pillar"])
    v = pillar_scores(metrics, sc["valuation"], sc["min_metrics_per_pillar"])
    m = pillar_scores(metrics, sc["momentum"], sc["min_metrics_per_pillar"])
    trend = pillar_scores(metrics, ["ch1y", "price_vs_sma200"], 2)  # pullbacks: rank by the strength of the uptrend
    tc = cfg["tactical"]
    rows = []
    for t, d in metrics.items():
        rows.append({"ticker": t, "quality": q[t], "valuation": v[t], "momentum": m[t],
                     "core": st.mean([q[t], v[t]]) if q[t] is not None and v[t] is not None else None,
                     "pullback_cand": trend[t] if trend[t] is not None and setups.pullback_candidate(d, tc, asof) else None,
                     "drift_cand": d.get("price_vs_sma50") if setups.drift_candidate(d, tc, asof) else None,
                     "tactical": None, "setup": None, "setup_detail": None,
                     "earnings_date": d.get("earnings_date")})
    return rows


def tactical_check(rows: list[dict], fetcher, cfg: dict, asof: str) -> list[dict]:
    """Stage 2 for tactical: daily history for the top `tactical_check_top` candidates of each setup.
    Drift needs a confirmed earnings reaction; both need an ATR stop. Sets `tactical` (drift: the reaction
    size in %; pullback: the uptrend score), `setup` and `setup_detail`. Returns failed pages."""
    tc, n = cfg["tactical"], cfg["screen"].get("tactical_check_top", 0)
    drift = sorted((r for r in rows if r["drift_cand"] is not None), key=lambda r: -r["drift_cand"])[:n]
    pull = sorted((r for r in rows if r["pullback_cand"] is not None), key=lambda r: -r["pullback_cand"])[:n]
    failed, hist = [], {}
    for r in {id(x): x for x in drift + pull}.values():
        try:
            data = fetcher.section(r["ticker"], "history")["data"]
            hist[r["ticker"]] = [x for x in data["rows"] if x["date"] < asof]
        except DataError as e:
            failed.append({"ticker": r["ticker"], "url": e.url, "field": e.field})
    for r in drift:
        h = hist.get(r["ticker"])
        sig = setups.drift_signal(h, tc) if h else None
        p = setups.plan("drift", h, tc, sig) if sig else None
        if p:
            r.update(tactical=sig["jump_pct"], setup="drift", setup_detail=setups.describe("drift", p, sig))
    for r in pull:
        h = hist.get(r["ticker"])
        p = setups.plan("pullback", h, tc) if h and r["setup"] is None else None
        if p:
            r.update(tactical=r["pullback_cand"], setup="pullback", setup_detail=setups.describe("pullback", p))
    return failed


def history_metrics(ratios: dict) -> dict:
    """Second-stage figures from the ratios page (5 fiscal years + TTM), all 'higher is better':
    cheap_* = 100 - position of today's multiple in its own 5y range (100 = at its 5y low);
    roic_trend / roce_trend = change in percentage points from the oldest to the newest fiscal year;
    roic_min = the worst fiscal-year ROIC (%), i.e. consistency."""
    from fact_sheet import range_position, trend
    per = ratios["periods"]

    def series(key):
        vals = ratios["rows"].get(key) or [None] * len(per)
        cur = vals[per.index("TTM")] if "TTM" in per else None
        fy = [v for p, v in zip(per, vals) if p != "TTM"][::-1]  # oldest -> newest
        return cur, fy

    out = {}
    for key in ("pe", "evebitda", "pfcf", "pb"):
        cur, fy = series(key)
        rp = range_position(cur, fy)
        out[f"cheap_{key}"] = None if rp is None else 100 - rp["pos_pct"]
    for key in ("roic", "roce", "roe"):
        _, fy = series(key)
        d, _ = trend([None if v is None else v * 100 for v in fy])
        out[f"{key}_trend"] = d
    _, roic_fy = series("roic")
    vals = [v * 100 for v in roic_fy if v is not None]
    out["roic_min"] = min(vals) if len(vals) >= 3 else None
    _, roe_fy = series("roe")  # banks/insurers have no ROIC/EBITDA/FCF: ROE and P/B carry their history
    vals = [v * 100 for v in roe_fy if v is not None]
    out["roe_min"] = min(vals) if len(vals) >= 3 else None
    return out


def deep_dive(rows: list[dict], fetcher, cfg: dict) -> list[dict]:
    """Stage 2: read the ratios page for the top `deep_dive_top` core candidates and add a
    5-year 'history' pillar; core_deep = mean(quality, valuation, history). Returns failed pages."""
    sc = cfg["screen"]
    n = sc.get("deep_dive_top", 0)
    top = sorted((r for r in rows if r["core"] is not None), key=lambda r: -r["core"])[:n]
    hist, failed = {}, []
    for r in top:
        try:
            sec = fetcher.section(r["ticker"], "ratios")
            hist[r["ticker"]] = history_metrics(sec["data"])
        except DataError as e:
            failed.append({"ticker": r["ticker"], "url": e.url, "field": e.field})
    h = pillar_scores(hist, sc["history"], sc["min_metrics_per_pillar"]) if hist else {}
    checked = {r["ticker"] for r in top}
    for r in rows:
        r["history"] = h.get(r["ticker"])
        if r["history"] is not None:
            r["core_deep"] = st.mean([r["quality"], r["valuation"], r["history"]])
        elif r["ticker"] in checked:  # in the top N but no usable history: keep its stage-1 score, no penalty
            r["core_deep"] = r["core"]
        else:
            r["core_deep"] = None
    return failed


def core_rank_key(r: dict):
    """Deep-dived names rank first (by core_deep); the rest follow by the stage-1 core score."""
    return (r.get("core_deep") is not None, r.get("core_deep") if r.get("core_deep") is not None else r["core"])


def recently_researched(days: int, asof: str) -> set[str]:
    """Folder slugs of names with a REAL decision in the decision log within `days` (dry runs record
    no decisions, so their research never blocks a name)."""
    import csv
    log = ROOT / "portfolio" / "decisions.csv"
    if not log.exists():
        return set()
    cutoff = (dt.date.fromisoformat(asof) - dt.timedelta(days=days)).isoformat()
    with log.open() as fh:
        return {Ticker(r["ticker"]).slug for r in csv.DictReader(fh) if r.get("date", "") >= cutoff}


def pick(rows: list[dict], cfg: dict) -> list[dict]:
    sc, cap = cfg["screen"], cfg["agents"]["max_new_initiations_per_week"]
    picks: list[dict] = []
    ranked = sorted((r for r in rows if r["core"] is not None), key=core_rank_key, reverse=True)
    for r in ranked:
        if len(picks) >= min(sc["core_picks"], cap):
            break
        sc_ = r.get("core_deep") if r.get("core_deep") is not None else r["core"]
        picks.append({"ticker": r["ticker"], "type": "CORE", "score": round(sc_, 1)})
    # tactical: alternate the two setups, best first within each
    queues = {k: sorted((r for r in rows if r.get("setup") == k and r.get("tactical") is not None),
                        key=lambda r: -r["tactical"]) for k in ("drift", "pullback")}
    n_tac = 0
    while n_tac < sc["tactical_picks"] and len(picks) < cap and any(queues.values()):
        for k in ("drift", "pullback"):
            while queues[k] and queues[k][0]["ticker"] in {p["ticker"] for p in picks}:
                queues[k].pop(0)
            if queues[k] and n_tac < sc["tactical_picks"] and len(picks) < cap:
                r = queues[k].pop(0)
                picks.append({"ticker": r["ticker"], "type": "TACTICAL", "score": round(r["tactical"], 1),
                              "setup": k, "setup_detail": r["setup_detail"]})
                n_tac += 1
    return picks


def run(fetcher, cfg: dict, asof: str, limit: int | None = None, state: dict | None = None,
        index: str | None = None) -> dict:
    held = set((state or {}).get("holdings", {}))
    recent = recently_researched(cfg["screen"]["exclude_researched_days"], asof)
    uni = [r for r in read_universe() if r["screen"] == "yes" and r["ticker"] not in held
           and Ticker(r["ticker"]).slug not in recent
           and (index is None or index in r["indexes"].split(";"))]
    if limit:
        uni = uni[:limit]
    metrics, failed, names = {}, [], {}
    for r in uni:
        url = page_url(r["ticker"], "statistics/")
        try:
            nodes = page_nodes(fetcher.html(url), url)
            metrics[r["ticker"]] = stock_metrics(parse_statistics(nodes, url), parse_info(nodes, url))
            names[r["ticker"]] = r["name"]
        except DataError as e:
            failed.append({"ticker": r["ticker"], "url": e.url, "field": e.field})
    rows = score(metrics, cfg, asof)
    deep_failed = deep_dive(rows, fetcher, cfg)
    tac_failed = tactical_check(rows, fetcher, cfg, asof)
    return {"asof": asof, "screened": len(metrics), "failed": failed + deep_failed + tac_failed, "excluded_held": sorted(held),
            "excluded_recent": sorted(recent), "rows": rows, "names": names, "picks": pick(rows, cfg),
            "deep_dived": sum(1 for r in rows if r.get("history") is not None)}


def report_md(res: dict, top: int = 15) -> str:
    def f(x):
        return "n/a" if x is None else f"{x:.0f}"

    lines = [f"# Screen — {res['asof']}",
             f"Screened {res['screened']} stocks; {len(res['failed'])} pages failed (excluded, listed below). "
             "Scores are percentiles (0-100) within the screened set; inputs from each stock's "
             "stockanalysis.com statistics page. The top core candidates "
             f"({res.get('deep_dived', 0)} stocks) also had their ratios page read: History = valuation vs its own "
             "5-year range plus return-on-capital trend and consistency; their core score = mean(Quality, Valuation, "
             "History).", "",
             "## This week's picks for initiation"]
    for p in res["picks"]:
        lines.append(f"- {p['ticker']} ({res['names'].get(p['ticker'], '')}): {p['type']}"
                     + (f" ({p['setup']})" if p.get("setup") else "") + f", score {p['score']} — "
                     f"{page_url(p['ticker'], 'statistics/')}")
    for kind in ("core",):
        cands = [r for r in res["rows"] if r[kind] is not None]
        ranked = sorted(cands, key=core_rank_key, reverse=True)[:top]
        lines += ["", f"## Top {kind} scores", "| # | Ticker | Name | Score | Quality | Valuation | History | Momentum | Earnings | Source |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(ranked, 1):
            score_ = r.get("core_deep") if r.get("core_deep") is not None else r[kind]
            lines.append(f"| {i} | {r['ticker']} | {res['names'].get(r['ticker'], '')} | {f(score_)} | {f(r['quality'])} | "
                         f"{f(r['valuation'])} | {f(r.get('history'))} | {f(r['momentum'])} | {r['earnings_date'] or 'n/a'} | "
                         f"{page_url(r['ticker'], 'statistics/')} |")
    for k, title in (("drift", "Post-earnings drift"), ("pullback", "Pullback in uptrend")):
        tac = sorted((r for r in res["rows"] if r.get("setup") == k), key=lambda r: -r["tactical"])[:top]
        lines += ["", f"## Tactical setups: {title}", "| # | Ticker | Name | Setup and risk plan | Next earnings |", "|---|---|---|---|---|"]
        lines += [f"| {i} | {r['ticker']} | {res['names'].get(r['ticker'], '')} | {r['setup_detail']} | {r['earnings_date'] or 'n/a'} |"
                  for i, r in enumerate(tac, 1)] or ["| | none qualified this week | | | |"]
    if res["failed"]:
        lines += ["", "## Failed pages (excluded)"] + [f"- {x['ticker']}: {x['url']} ({x['field']})" for x in res["failed"]]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--limit", type=int)
    ap.add_argument("--index", choices=["SP500", "FTSE100", "ALLWORLD"], help="screen one index only (ad-hoc)")
    a = ap.parse_args(argv)
    cfg = load_config()
    if not (ROOT / "universe" / "universe.csv").exists():
        print("ERROR: universe/universe.csv not found. Build it first: bin/py scripts/universe.py build", file=sys.stderr)
        return 2
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    res = run(Fetcher(cfg), cfg, a.asof, a.limit, state, a.index)
    OUT.mkdir(parents=True, exist_ok=True)
    stem = a.asof + (f"-{a.index.lower()}" if a.index else "")
    (OUT / f"{stem}.md").write_text(report_md(res))
    (OUT / f"{stem}.json").write_text(json.dumps({k: res[k] for k in ("asof", "screened", "failed", "picks")}, indent=1))
    print(json.dumps({"screened": res["screened"], "failed": len(res["failed"]), "picks": res["picks"],
                      "report": str((OUT / f"{stem}.md").relative_to(ROOT))}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
