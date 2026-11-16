"""Historical replay and diagnostic harness for the PRICE-ONLY rules (owner request 2026-11-15, V2). No model calls.

What it replays, month by month over past prices, against SPY buy-and-hold:
  - momentum 6-1 (return from t-126 to t-21 sessions) picks the top K of the tickers given;
  - 60-session volatility sizes them (the [core] vol clamp), floor `min_size_pct` / ceiling `max_entry_pct`;
  - the S&P 500 50/200-day trend sets the cash reserve (5-35%, sliding over +/-2%, as regime.py's spy_50_200);
  - positions that don't fit within 100% - cash are dropped lowest-ranked first and the rest is NOT scaled up;
  - each rebalance pays `cost_bps` on the traded value (the repo's own costs are 0.10% spread + 0.15% FX).

What it is NOT: an out-of-sample test. Nothing is fitted, so this is a replay of fixed rules. Read it with these limits:
  - the tickers you pass are today's names (survivorship bias: past losers that left the list are missing);
  - fundamentals (quality, valuation, the scorecard) and the model's vetoes are NOT replayed (stockanalysis.com
    statements are not point-in-time); those are judged on the live paper record (portfolio/decisions.csv);
  - cash earns nothing here (the live portfolio earns [cash].interest_aer_pct), prices are Yahoo closes in each
    stock's own currency (no FX moves), and an exchange holiday repeats the last close.

Usage:
    python scripts/replay.py [--tickers A B C | --watchlist | --universe-top 100] [--years 5] [--k 10] [--cost-bps 10]
Writes reports/replay/<date>.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import math
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config, read_watchlist  # noqa: E402

OUT = ROOT / "reports" / "replay"
MOM_LONG, MOM_SKIP, VOL_DAYS, SMA_FAST, SMA_SLOW = 126, 21, 60, 50, 200


def slide(value: float, calm: float, stressed: float) -> float:
    return max(0.0, min(1.0, (value - calm) / (stressed - calm)))


def sma(xs: list[float], n: int) -> float:
    return sum(xs[-n:]) / n


def vol_pct(closes: list[float], n: int = VOL_DAYS) -> float | None:
    c = closes[-(n + 1):]
    r = [math.log(b / a) for a, b in zip(c, c[1:])]
    return st.stdev(r) * math.sqrt(252) * 100 if len(r) >= n // 2 else None


def momentum_6_1(closes: list[float]) -> float | None:
    if len(closes) < MOM_LONG + 1:
        return None
    return closes[-1 - MOM_SKIP] / closes[-1 - MOM_LONG] - 1


def cash_target(bench: list[float], cfg: dict) -> float:
    """Reserve fraction from the 50/200-day trend: reserve_min..reserve_max, sliding between the calm and stressed %."""
    cs, a = cfg["cash_strategy"], cfg["cash_strategy"]["indicators"]["spy_50_200"]
    trend = (sma(bench, SMA_FAST) / sma(bench, SMA_SLOW) - 1) * 100
    lo, hi = cs["reserve_min_pct"], cs["reserve_max_pct"]
    return (lo + (hi - lo) * slide(trend, a["calm"], a["stressed"])) / 100


def target_weights(hist: dict[str, list[float]], bench: list[float], cfg: dict, k: int) -> dict[str, float]:
    """Target weights from closes up to (and including) the last session before the rebalance."""
    c = cfg["core"]
    ranked = sorted(((momentum_6_1(v), t) for t, v in hist.items() if momentum_6_1(v) is not None), reverse=True)[:k]
    vols = {t: vol_pct(hist[t]) for _, t in ranked}
    known = [v for v in vols.values() if v]
    ref = st.median(known) if len(known) >= 5 else float(c.get("ref_vol_pct", 30))
    lo, hi = c.get("vol_scale_clamp", [0.6, 1.4])
    base, floor, cap = float(c["conviction_size_pct"]["4"]), float(c.get("min_size_pct", 0)), float(c.get("max_entry_pct", 15))
    room, out = 1 - cash_target(bench, cfg), {}
    for _, t in ranked:  # best momentum first; the first that no longer fits ends the list (never scaled back up)
        v = vols[t]
        w = max(floor, min(base * (min(max(ref / v, lo), hi) if v else 1.0), cap)) / 100
        if sum(out.values()) + w > room + 1e-12:
            break
        out[t] = w
    return out


def ffill(rows: list[tuple[str, float]], dates: list[str]) -> dict[str, float]:
    """Close on every benchmark date from the ticker's first close on; a date the exchange was shut repeats the last close."""
    have, out, last = dict(rows), {}, None
    for d in dates:
        last = have.get(d, last)
        if last is not None:
            out[d] = last
    return out


def replay(closes: dict[str, list[tuple[str, float]]], bench: list[tuple[str, float]], cfg: dict,
           k: int = 10, cost_bps: float = 10.0) -> dict:
    """closes: ticker -> [(date, close)] ascending. Monthly rebalance at the first session of each month, trading at
    that day's close from signals up to the day before. Returns NAV series for the replay and SPY, plus metrics."""
    dates = [d for d, _ in bench]
    px = {t: ffill(v, dates) for t, v in closes.items()}   # holiday gaps carry the last close, never drop a position
    bpx = [c for _, c in bench]
    start = SMA_SLOW + 1  # SPY needs 200 sessions for its trend; momentum needs 127
    held, cash, month = {}, 1.0, None      # held: ticker -> shares; the replay starts as 1.0 in cash
    nav, traded_total, rebalances = [], 0.0, 0
    for i in range(start, len(dates)):
        d = dates[i]
        value = cash + sum(sh * px[t][d] for t, sh in held.items() if d in px[t])
        if d[:7] != month:  # first session of a month: signals from closes before today, trade at today's close
            month = d[:7]
            hist = {t: [px[t][x] for x in dates[:i] if x in px[t]] for t in px}
            w = target_weights({t: v for t, v in hist.items() if v}, bpx[:i], cfg, k)
            cur = {t: sh * px[t][d] / value for t, sh in held.items() if d in px[t]}
            traded = sum(abs(w.get(t, 0) - cur.get(t, 0)) for t in set(w) | set(cur)) * value
            value -= traded * cost_bps / 1e4
            traded_total += traded / (value + traded * cost_bps / 1e4)
            held = {t: wt * value / px[t][d] for t, wt in w.items() if d in px[t]}
            cash = value - sum(sh * px[t][d] for t, sh in held.items())
            rebalances += 1
        nav.append(value)
    spy = [x / bpx[start] for x in bpx[start:]]
    return {"nav": nav, "spy": spy, "start": dates[start], "end": dates[-1], "rebalances": rebalances,
            "turnover_per_rebalance": traded_total / rebalances if rebalances else 0.0,
            "strategy": metrics(nav), "spy_metrics": metrics(spy)}


def metrics(nav: list[float]) -> dict:
    if len(nav) < 3:
        return {}
    r = [b / a - 1 for a, b in zip(nav, nav[1:])]
    years = len(r) / 252
    peak, dd = nav[0], 0.0
    for x in nav:
        peak = max(peak, x)
        dd = max(dd, 1 - x / peak)
    sd = st.stdev(r)
    return {"total_return_pct": round((nav[-1] / nav[0] - 1) * 100, 1),
            "cagr_pct": round(((nav[-1] / nav[0]) ** (1 / years) - 1) * 100, 1) if years > 0 else None,
            "vol_pct": round(sd * math.sqrt(252) * 100, 1),
            "sharpe": round(st.mean(r) / sd * math.sqrt(252), 2) if sd else None,
            "max_drawdown_pct": round(dd * 100, 1)}


def render(res: dict, tickers: list[str], k: int, cost_bps: float, asof: str) -> str:
    s, b = res["strategy"], res["spy_metrics"]
    rows = "\n".join(f"| {name} | {s.get(key)} | {b.get(key)} |" for name, key in (
        ("Total return %", "total_return_pct"), ("CAGR %", "cagr_pct"), ("Volatility %", "vol_pct"),
        ("Sharpe (rf 0)", "sharpe"), ("Max drawdown %", "max_drawdown_pct")))
    return (f"# Historical replay (diagnostic), {asof}\n\n"
            f"Price-only rules replayed over {res['start']} to {res['end']}: top {k} by 6-1 momentum of {len(tickers)} "
            f"tickers, 60-session volatility sizing, 50/200 trend cash reserve, monthly rebalance, {cost_bps:g} bps per "
            f"trade on the traded value ({res['rebalances']} rebalances, average turnover "
            f"{res['turnover_per_rebalance'] * 100:.0f}% of the portfolio).\n\n"
            f"| | Replay | SPY buy-and-hold |\n|---|---|---|\n{rows}\n\n"
            "**Read with care.** This is a replay of fixed rules, not an out-of-sample test. The tickers are today's "
            "names (survivorship bias); fundamentals and the model's vetoes are not replayed (the site's statements are "
            "not point-in-time; judge those on the live record in `portfolio/decisions.csv`); cash earns nothing and "
            "prices are in each stock's own currency (no FX moves).\n")


def load_yahoo(tickers: list[str], years: int) -> dict[str, list[tuple[str, float]]]:
    from prices import yahoo_symbol
    import yfinance as yf
    out = {}
    for t in tickers:
        sym = yahoo_symbol(t)
        if not sym:
            continue
        df = yf.Ticker(sym).history(period=f"{years}y", auto_adjust=True)
        if df is not None and len(df):
            out[t] = [(i.date().isoformat(), float(c)) for i, c in zip(df.index, df["Close"]) if c == c]
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="*")
    ap.add_argument("--watchlist", action="store_true", help="use universe/watchlist.txt")
    ap.add_argument("--universe-top", type=int, help="the N largest S&P 500 names by market cap (universe/universe.csv)")
    ap.add_argument("--years", type=int, default=5)
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--cost-bps", type=float, default=10.0)
    a = ap.parse_args(argv)
    tickers = a.tickers or (sorted(read_watchlist()) if a.watchlist else [])
    if a.universe_top:
        from universe import read_universe
        sp = [r for r in read_universe() if "SP500" in r["indexes"].split(";") and r.get("market_cap_usd")]
        tickers = [r["ticker"] for r in sorted(sp, key=lambda r: -float(r["market_cap_usd"]))[:a.universe_top]]
    if not tickers:
        ap.error("give --tickers, --watchlist or --universe-top")
    cfg = load_config()
    closes = load_yahoo(["SPY"] + [t for t in tickers if t != "SPY"], a.years)
    if "SPY" not in closes:
        raise DataError("yfinance", "SPY", "no benchmark history")
    bench = closes.pop("SPY")
    res = replay(closes, bench, cfg, a.k, a.cost_bps)
    asof = dt.date.today().isoformat()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{asof}.md").write_text(render(res, list(closes), a.k, a.cost_bps, asof))
    print(f"wrote {OUT / (asof + '.md')}: replay {res['strategy']} vs SPY {res['spy_metrics']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
