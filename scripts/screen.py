"""Weekly screen: rank the universe and pick this week's new initiations. No model calls.

For every screenable stock in universe/universe.csv (minus holdings and names researched in the
last `exclude_researched_days`), read its stockanalysis.com statistics page and score three pillars
by percentile rank within the screened set (config [screen]):
    quality, valuation, momentum (price vs 50/200-day computed from the page's own quote and averages)
Core score = mean(quality, valuation). Tactical score = momentum, only for names whose earnings date
falls inside `tactical_earnings_window_days`.

A page that fails to load or parse is EXCLUDED and listed in the report (never guessed). Pages are
cached per day, so an interrupted run resumes where it stopped.

Usage:
    python scripts/screen.py [--asof YYYY-MM-DD] [--limit N]
Writes reports/screen/<date>.md (ranked tables with source URLs) and reports/screen/<date>.json (picks).
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
    window_end = (dt.date.fromisoformat(asof) + dt.timedelta(days=sc["tactical_earnings_window_days"])).isoformat()
    rows = []
    for t, d in metrics.items():
        ed = d.get("earnings_date")
        rows.append({"ticker": t, "quality": q[t], "valuation": v[t], "momentum": m[t],
                     "core": st.mean([q[t], v[t]]) if q[t] is not None and v[t] is not None else None,
                     "tactical": m[t] if m[t] is not None and ed and asof < ed <= window_end else None,
                     "earnings_date": ed})
    return rows


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
    for kind, n in (("core", sc["core_picks"]), ("tactical", sc["tactical_picks"])):
        ranked = sorted((r for r in rows if r[kind] is not None), key=lambda r: -r[kind])
        for r in ranked:
            if len([p for p in picks if p["type"] == kind.upper()]) >= n or len(picks) >= cap:
                break
            if r["ticker"] not in {p["ticker"] for p in picks}:
                picks.append({"ticker": r["ticker"], "type": kind.upper(), "score": round(r[kind], 1)})
    return picks


def run(fetcher, cfg: dict, asof: str, limit: int | None = None, state: dict | None = None) -> dict:
    held = set((state or {}).get("holdings", {}))
    recent = recently_researched(cfg["screen"]["exclude_researched_days"], asof)
    uni = [r for r in read_universe() if r["screen"] == "yes" and r["ticker"] not in held
           and Ticker(r["ticker"]).slug not in recent]
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
    return {"asof": asof, "screened": len(metrics), "failed": failed, "excluded_held": sorted(held),
            "excluded_recent": sorted(recent), "rows": rows, "names": names, "picks": pick(rows, cfg)}


def report_md(res: dict, top: int = 15) -> str:
    def f(x):
        return "n/a" if x is None else f"{x:.0f}"

    lines = [f"# Screen — {res['asof']}",
             f"Screened {res['screened']} stocks; {len(res['failed'])} pages failed (excluded, listed below). "
             "Scores are percentiles (0-100) within the screened set; all inputs from each stock's "
             "stockanalysis.com statistics page.", "",
             "## This week's picks for initiation"]
    for p in res["picks"]:
        lines.append(f"- {p['ticker']} ({res['names'].get(p['ticker'], '')}): {p['type']}, score {p['score']} — "
                     f"{page_url(p['ticker'], 'statistics/')}")
    for kind in ("core", "tactical"):
        ranked = sorted((r for r in res["rows"] if r[kind] is not None), key=lambda r: -r[kind])[:top]
        lines += ["", f"## Top {kind} scores", "| # | Ticker | Name | Score | Quality | Valuation | Momentum | Earnings | Source |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(ranked, 1):
            lines.append(f"| {i} | {r['ticker']} | {res['names'].get(r['ticker'], '')} | {f(r[kind])} | {f(r['quality'])} | "
                         f"{f(r['valuation'])} | {f(r['momentum'])} | {r['earnings_date'] or 'n/a'} | "
                         f"{page_url(r['ticker'], 'statistics/')} |")
    if res["failed"]:
        lines += ["", "## Failed pages (excluded)"] + [f"- {x['ticker']}: {x['url']} ({x['field']})" for x in res["failed"]]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--limit", type=int)
    a = ap.parse_args(argv)
    cfg = load_config()
    if not (ROOT / "universe" / "universe.csv").exists():
        print("ERROR: universe/universe.csv not found. Build it first: bin/py scripts/universe.py build", file=sys.stderr)
        return 2
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    res = run(Fetcher(cfg), cfg, a.asof, a.limit, state)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{a.asof}.md").write_text(report_md(res))
    (OUT / f"{a.asof}.json").write_text(json.dumps({k: res[k] for k in ("asof", "screened", "failed", "picks")}, indent=1))
    print(json.dumps({"screened": res["screened"], "failed": len(res["failed"]), "picks": res["picks"],
                      "report": str((OUT / f"{a.asof}.md").relative_to(ROOT))}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
