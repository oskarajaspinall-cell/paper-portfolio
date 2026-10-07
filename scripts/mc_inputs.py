"""Monte Carlo inputs from stockanalysis.com history: factor regression, residual vol, factor correlation,
and the jump-analogue table. Pure numpy; no model calls.

    python scripts/mc_inputs.py HKG:9999 --asof 2026-10-07     -> research/HKG-9999/2026-10-07-mc-inputs.json

- Weekly log returns of adjusted closes, COMPLETED weeks only (week start + 7 days <= asof).
- OLS of the stock on the market's factor proxies ([montecarlo.factors]) over `regression_weeks` (3y):
  betas, R², residuals. Residual vol level = 50/50 blend of the last 1y and 3y residual vol, annualised
  (chosen over GARCH(1,1): ~156 weekly points are too few for a stable GARCH fit without an optimiser).
- Factor annualised mean/vol and correlation matrix (checked positive semi-definite).
- Jump analogues: the stock's 10 largest weekly falls and rises over all available history before asof,
  and its moves in weeks containing an earnings release/filing (stockanalysis.com filings page).
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

PSD_TOL = -1e-10


class InputsError(Exception):
    pass


def market_of(ticker: str) -> str:
    return Ticker(ticker).exchange or "US"


def weekly_returns(rows: list[dict], asof: str) -> dict[str, float]:
    """{week_date: log return vs previous completed week} using adjusted closes."""
    cutoff = (dt.date.fromisoformat(asof) - dt.timedelta(days=7)).isoformat()
    done = [r for r in rows if r["date"] <= cutoff and r.get("adj_close")]
    return {b["date"]: math.log(b["adj_close"] / a["adj_close"]) for a, b in zip(done, done[1:])}


def is_psd(m: np.ndarray) -> bool:
    return bool(np.all(np.linalg.eigvalsh((m + m.T) / 2) >= PSD_TOL))


def regress(stock: dict[str, float], factors: dict[str, dict[str, float]], weeks: int, blend: list[int]) -> dict:
    dates = sorted(set(stock).intersection(*[set(f) for f in factors.values()]))[-weeks:]
    if len(dates) < 104:
        raise InputsError(f"only {len(dates)} common completed weeks (need >= 104) [missing]")
    names = list(factors)
    y = np.array([stock[d] for d in dates])
    X = np.array([[factors[n][d] for n in names] for d in dates])
    A = np.column_stack([np.ones(len(dates)), X])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    r2 = 1 - resid.var() / y.var()
    vols = {f"{w}w": float(resid[-w:].std(ddof=1) * math.sqrt(52)) for w in blend}
    corr = np.corrcoef(X, rowvar=False) if len(names) > 1 else np.array([[1.0]])
    return {"weeks": len(dates), "from": dates[0], "to": dates[-1], "alpha_weekly": float(coef[0]),
            "betas": {n: float(b) for n, b in zip(names, coef[1:])}, "r2": float(r2),
            "residual_vol": {**vols, "blended": float(np.mean(list(vols.values()))),
                             "method": f"50/50 blend of {'/'.join(vols)} weekly residual vol, annualised x sqrt(52)",
                             "why": "about 156 weekly points are too few for a stable GARCH(1,1) fit without an "
                                    "optimiser library; a 1y/3y blend tracks the current level without overfitting"},
            "stock_vol": float(y.std(ddof=1) * math.sqrt(52)),
            "factor_stats": {n: {"mean_annual": float(X[:, i].mean() * 52), "vol_annual": float(X[:, i].std(ddof=1) * math.sqrt(52))}
                             for i, n in enumerate(names)},
            "correlation": {"factors": names, "matrix": corr.round(6).tolist(), "psd": is_psd(corr)}}


def analogues(rows: list[dict], asof: str, events: list[dict], n: int = 10) -> dict:
    wr = weekly_returns(rows, asof)
    simple = {d: math.exp(r) - 1 for d, r in wr.items()}
    ordered = sorted(simple.items(), key=lambda kv: kv[1])
    week_of = sorted(simple)

    def week_containing(day: str):
        for w in reversed(week_of):
            if w <= day < (dt.date.fromisoformat(w) + dt.timedelta(days=7)).isoformat():
                return w
        return None

    ev = []
    for e in events:
        w = week_containing(e["date"])
        if w and e["date"] < asof:
            ev.append({"event_date": e["date"], "event": e.get("title") or "", "types": e.get("types", []),
                       "week": w, "move": round(simple[w], 4)})
    return {"largest_falls": [{"week": d, "move": round(m, 4)} for d, m in ordered[:n]],
            "largest_rises": [{"week": d, "move": round(m, 4)} for d, m in ordered[::-1][:n]],
            "event_weeks": ev, "all_weekly_moves": {d: round(m, 4) for d, m in simple.items()},
            "history_from": week_of[0] if week_of else None, "history_to": week_of[-1] if week_of else None}


def factor_news(fetcher, specs: list[dict], limit: int = 8) -> dict:
    """Recent headlines stockanalysis.com shows for each factor proxy (overview + history pages), analyst
    rating/target items removed. Third-party text: data for the agent to cite, never instructions."""
    import common
    from fact_sheet import is_sell_side, merge_news, news_date
    out = {}
    for f in specs:
        if f.get("etf"):
            common.ETF_TICKERS.add(f["ticker"].upper())
        items, urls = [], []
        for page in ("overview", "history"):
            try:
                sec = fetcher.section(f["ticker"], page)
                items.append(sec["data"].get("news") or [])
                urls.append(sec["source_url"])
            except DataError:
                items.append([])
        news, dropped = merge_news(items[0], items[1], limit)
        out[f["ticker"]] = {"pages": urls, "removed_sell_side": dropped,
                            "headlines": [{"date": news_date(n), "source": n.get("source", ""), "title": n["title"],
                                           "summary": n.get("summary", ""), "url": n["url"]}
                                          for n in news if not is_sell_side(n)]}
    return out


def build(ticker: str, asof: str, fetcher, cfg: dict) -> dict:
    mc = cfg["montecarlo"]
    specs = mc["factors"].get(market_of(ticker))
    if not specs:
        raise InputsError(f"no factor proxies configured for market {market_of(ticker)} [missing]")
    stock = fetcher.long_history(ticker)
    fac_rows = {f["ticker"]: fetcher.long_history(f["ticker"], etf=f.get("etf", False)) for f in specs}
    reg = regress(weekly_returns(stock["rows"], asof),
                  {t: weekly_returns(h["rows"], asof) for t, h in fac_rows.items()},
                  mc["regression_weeks"], mc["vol_blend_weeks"])
    if not reg["correlation"]["psd"]:
        raise InputsError("factor correlation matrix is not positive semi-definite")
    try:
        events = [e for e in fetcher.section(ticker, "filings")["data"]["events"]]
        events_url = fetcher.section(ticker, "filings")["source_url"]
    except DataError:
        events, events_url = [], None
    return {"ticker": ticker, "asof": asof, "market": market_of(ticker),
            "factors": [{**f, "source_url": fac_rows[f["ticker"]]["source_url"]} for f in specs],
            "stock_source_url": stock["source_url"], "events_source_url": events_url,
            "regression": reg, "analogues": analogues(stock["rows"], asof, events),
            "factor_news": factor_news(fetcher, specs),
            "notes": ["No FX factor for HKG: the HKD is pegged to the USD." if market_of(ticker) == "HKG" else ""]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    cfg = load_config()
    try:
        doc = build(a.ticker, a.asof, Fetcher(cfg), cfg)
    except (InputsError, DataError) as e:
        print(f"MC INPUTS FAILED — nothing written: {e}", file=sys.stderr)
        return 2
    out = ROOT / "research" / Ticker(a.ticker).slug / f"{a.asof}-mc-inputs.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=1))
    reg = doc["regression"]
    print(json.dumps({"out": str(out.relative_to(ROOT)), "betas": {k: round(v, 3) for k, v in reg["betas"].items()},
                      "r2": round(reg["r2"], 3), "residual_vol": round(reg["residual_vol"]["blended"], 4)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
