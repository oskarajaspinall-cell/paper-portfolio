"""Portfolio risk: volatility-scaled core sizing and risk contributions. No model calls.

Design by Claude 2026-10-16 (config [core].vol_*):
- Core sizing: target = conviction size x clamp(ref_vol / vol, vol_scale_clamp), capped at trim_above_pct.
  vol = annualised volatility of the stock's last `vol_lookback_sessions` daily closes (its own currency);
  ref_vol = the median vol of the current core holdings (`ref_vol_pct` while fewer than 5 have a vol).
  A high-volatility name gets a smaller position than a defensive one at the same conviction; conviction
  still decides whether to buy and is still the main input to the size. Tactical sizing is unchanged.
- Risk report (inform-only, never trades): each holding's weight, volatility, marginal contribution to
  risk MCR_i = (S w)_i / sigma_p and share of portfolio variance RC_i = w_i x MCR_i / sigma_p, from a
  covariance of WEEKLY returns (weekly, so markets in different time zones line up).

Usage:
    python scripts/risk.py report [--asof YYYY-MM-DD]   -> reports/risk/<date>.md/.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402

OUT = ROOT / "reports" / "risk"
MIN_RETURNS = 60          # fewer daily returns than this -> no vol (size unscaled)
MIN_REF_HOLDINGS = 5      # fewer core holdings with a vol -> ref_vol_pct from config


def daily_vol(closes: list[float], lookback: int) -> float | None:
    """Annualised volatility (%) of daily log returns over the last `lookback` sessions."""
    c = [x for x in closes if x and x > 0][-(lookback + 1):]
    r = [math.log(b / a) for a, b in zip(c, c[1:])]
    return st.stdev(r) * math.sqrt(252) * 100 if len(r) >= MIN_RETURNS else None


def weekly_returns(rows: list[dict]) -> dict[str, float]:
    """ISO week -> simple return from the previous week's last close."""
    last: dict[str, float] = {}
    for r in sorted(rows, key=lambda r: r["date"]):
        y, w, _ = dt.date.fromisoformat(r["date"]).isocalendar()
        if r.get("close"):
            last[f"{y}-W{w:02d}"] = r["close"]
    ks = sorted(last)
    return {k: last[k] / last[p] - 1 for p, k in zip(ks, ks[1:])}


def covariance(series: dict[str, dict[str, float]]) -> tuple[list[str], list[list[float]]]:
    """Annualised covariance of weekly returns over the weeks every series has."""
    names = list(series)
    weeks = sorted(set.intersection(*(set(s) for s in series.values()))) if series else []
    if len(weeks) < 8:
        raise ValueError(f"only {len(weeks)} common weeks of returns")
    x = {n: [series[n][w] for w in weeks] for n in names}
    m = {n: st.mean(v) for n, v in x.items()}
    k = len(weeks) - 1
    return names, [[sum((a - m[i]) * (b - m[j]) for a, b in zip(x[i], x[j])) / k * 52 for j in names] for i in names]


def contributions(w: list[float], cov: list[list[float]]) -> dict:
    """MCR_i = (S w)_i / sigma_p; RC_i = w_i MCR_i / sigma_p (shares of variance, sum to 1)."""
    sw = [sum(cov[i][j] * w[j] for j in range(len(w))) for i in range(len(w))]
    var = sum(wi * x for wi, x in zip(w, sw))
    sp = math.sqrt(var) if var > 0 else 0.0
    return {"sigma_p": sp, "mcr": [x / sp if sp else 0.0 for x in sw],
            "rc": [wi * x / var if var else 0.0 for wi, x in zip(w, sw)]}


class Sizer:
    """Volatility scaling for core targets; vols are cached per run."""

    def __init__(self, mkt, cfg: dict):
        self.mkt, self.cfg, self._vol = mkt, cfg, {}

    def vol(self, ticker: str) -> float | None:
        if ticker not in self._vol:
            try:
                rows = self.mkt.history(ticker)["rows"]
            except (DataError, KeyError, AttributeError):
                rows = []
            self._vol[ticker] = daily_vol([r["close"] for r in rows], int(self.cfg["core"].get("vol_lookback_sessions", 126)))
        return self._vol[ticker]

    def ref_vol(self, state: dict, exclude: str | None = None) -> float:
        vs = [v for t, h in state["holdings"].items() if h["type"] == "CORE" and t != exclude
              for v in [self.vol(t)] if v]
        return st.median(vs) if len(vs) >= MIN_REF_HOLDINGS else float(self.cfg["core"].get("ref_vol_pct", 30))

    def scale(self, ticker: str, state: dict) -> tuple[float, str]:
        c = self.cfg["core"]
        if not c.get("vol_scaling"):
            return 1.0, "vol scaling off"
        v = self.vol(ticker)
        if not v:
            return 1.0, "no volatility (short history): unscaled"
        ref = self.ref_vol(state, exclude=ticker)
        lo, hi = c.get("vol_scale_clamp", [0.6, 1.4])
        k = min(max(ref / v, lo), hi)
        return k, f"vol {v:.0f}% vs reference {ref:.0f}% -> x{k:.2f}"

    def target(self, conviction: int, ticker: str, state: dict) -> tuple[float, str]:
        c = self.cfg["core"]
        base = float(c["conviction_size_pct"][str(conviction)])
        k, why = self.scale(ticker, state) if base else (1.0, "")
        return round(min(base * k, float(c["trim_above_pct"])), 2), why


def report(state: dict, mkt, cfg: dict, asof: str) -> dict:
    hs = state["holdings"]
    total = state["cash_usd"] + sum(h["market_value_usd"] for h in hs.values())
    sizer = Sizer(mkt, cfg)
    rows, series, failed = [], {}, []
    for t, h in hs.items():
        try:
            hist = mkt.history(t)["rows"]
        except DataError as e:
            failed.append(f"{t}: {e}")
            continue
        series[t] = weekly_returns(hist)
        base = float(cfg["core"]["conviction_size_pct"].get(str(h.get("conviction")), 0)) if h["type"] == "CORE" else None
        rows.append({"ticker": t, "type": h["type"], "sector": h["sector"], "conviction": h.get("conviction"),
                     "weight_pct": h["market_value_usd"] / total * 100, "vol_pct": sizer.vol(t),
                     "target_pct": h.get("target_pct", base)})
    out = {"asof": asof, "rows": rows, "failed": failed, "sigma_p_pct": None}
    try:
        names, cov = covariance(series)
    except ValueError as e:
        out["note"] = f"risk contributions unavailable: {e}"
        return out
    w = [next(r["weight_pct"] for r in rows if r["ticker"] == n) / 100 for n in names]
    c = contributions(w, cov)  # cash: zero variance, so it only scales sigma_p down
    out["sigma_p_pct"] = c["sigma_p"] * 100
    for n, m, rc in zip(names, c["mcr"], c["rc"]):
        r = next(r for r in rows if r["ticker"] == n)
        r.update(mcr_pct=m * 100, risk_share_pct=rc * 100)
        invested = sum(w)
        r["flag"] = bool(invested and rc > 2 * (r["weight_pct"] / 100 / invested))
    return out


def report_md(res: dict) -> str:
    f = lambda x, d=1: "n/a" if x is None else f"{x:.{d}f}"  # noqa: E731
    lines = [f"# Portfolio risk — {res['asof']}", "",
             "Informational (design by Claude 2026-10-16); never trades. Volatility: annualised, daily closes in each "
             "share's own currency. Risk share: % of portfolio variance, from a covariance of weekly returns. "
             "MCR = marginal contribution to risk. Flag = risk share more than 2x its share of invested money.", "",
             f"Portfolio volatility (cash included): {f(res['sigma_p_pct'])}%."
             + (f" {res['note']}." if res.get("note") else ""), "",
             "| Ticker | Type | Sector | Conv. | Weight % | Target % | Vol % | MCR % | Risk share % | Flag |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(res["rows"], key=lambda r: -(r.get("risk_share_pct") or 0)):
        lines.append(f"| {r['ticker']} | {r['type']} | {r['sector']} | {r['conviction'] or ''} | {f(r['weight_pct'])} | "
                     f"{f(r['target_pct'])} | {f(r['vol_pct'], 0)} | {f(r.get('mcr_pct'))} | {f(r.get('risk_share_pct'))} | "
                     f"{'over budget' if r.get('flag') else ''} |")
    lines += [f"- price history failed: {x}" for x in res["failed"]]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["report"])
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    from portfolio import Market, price_provider
    cfg = load_config()
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    res = report(state, Market(Fetcher(cfg), a.asof, cfg, price_provider(cfg)), cfg, a.asof)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{a.asof}.json").write_text(json.dumps(res, indent=1))
    (OUT / f"{a.asof}.md").write_text(report_md(res))
    print(f"OK reports/risk/{a.asof}.md sigma_p={res['sigma_p_pct']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
