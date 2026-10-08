"""Tactical setups (owner rule 2026-10-08): post-earnings drift and pullback-in-uptrend, with
volatility-based stops. Pure functions over stockanalysis.com daily history rows (ascending, completed
sessions only) and statistics-page metrics. No model calls, no network.

- ATR(14): mean true range of the last 14 completed sessions (simple average, in the quoted currency).
- Post-earnings drift: within the last `drift_lookback_sessions` a session that closed >= `drift_min_jump_pct`
  above the prior close on volume >= `drift_min_volume_x` x its prior 50-session average, with the stock
  still holding >= `drift_min_hold_pct` of that jump. Stage 1 from the statistics page's earnings date:
  a date within the last `drift_recent_report_days` (the site keeps showing the date just reported until
  the next is confirmed) or >= `drift_min_days_to_next_earnings` ahead means results were just reported.
  Stop: the jump day's low minus 0.25 ATR (if the market undoes the reaction, the trade is wrong).
- Pullback: an established uptrend (above the 200-day average, strong 12-month trend) whose price has
  dipped back to around its 50-day average without being overbought, and no earnings for
  `pullback_min_days_to_earnings`. Stop: last close minus `stop_atr_multiple` x ATR.
- Every setup's minimum target is last close + `min_reward_risk` x (last close - stop).
"""
from __future__ import annotations

import datetime as dt


def atr(rows: list[dict], n: int = 14) -> float | None:
    """Average true range over the last n sessions (needs n + 1 rows with high/low/close)."""
    rs = [r for r in rows if r.get("high") is not None and r.get("low") is not None and r.get("close") is not None]
    if len(rs) < n + 1:
        return None
    trs = [max(b["high"] - b["low"], abs(b["high"] - a["close"]), abs(b["low"] - a["close"]))
           for a, b in zip(rs[-n - 1:-1], rs[-n:])]
    return sum(trs) / n


def drift_signal(rows: list[dict], tc: dict) -> dict | None:
    """The most recent qualifying earnings-reaction session in the lookback window, or None."""
    look, avg_n = int(tc["drift_lookback_sessions"]), 50
    if len(rows) < avg_n + 2:
        return None
    last = rows[-1]
    for i in range(len(rows) - 1, max(len(rows) - 1 - look, avg_n), -1):
        day, prev = rows[i], rows[i - 1]
        vols = [r.get("volume") for r in rows[i - avg_n:i] if r.get("volume")]
        if not vols or not day.get("volume") or not prev.get("close"):
            continue
        jump = day["close"] / prev["close"] - 1
        vol_x = day["volume"] / (sum(vols) / len(vols))
        if jump * 100 < tc["drift_min_jump_pct"] or vol_x < tc["drift_min_volume_x"]:
            continue
        held = (last["close"] - prev["close"]) / (day["close"] - prev["close"])
        if held * 100 < tc["drift_min_hold_pct"]:
            return None  # the most recent reaction has already faded
        return {"date": day["date"], "jump_pct": round(jump * 100, 2), "volume_x": round(vol_x, 2),
                "day_low": day["low"], "held_pct": round(held * 100, 1), "sessions_ago": len(rows) - 1 - i}
    return None


def days_to_earnings(ed: str | None, asof: str) -> int | None:
    """Days from asof to the statistics page's earnings date. After a report, stockanalysis.com keeps
    showing the date just reported until the company confirms the next one, so a PAST date means
    "just reported" (negative result)."""
    return None if not ed else (dt.date.fromisoformat(ed) - dt.date.fromisoformat(asof)).days


def pullback_candidate(d: dict, tc: dict, asof: str) -> bool:
    """Stage 1 (statistics page): uptrend intact, price back near the 50-day average, not overbought,
    and no earnings inside the window."""
    above200, vs50, rsi, ed = d.get("price_vs_sma200"), d.get("price_vs_sma50"), d.get("rsi"), d.get("earnings_date")
    lo50, hi50 = tc["pullback_sma50_band_pct"]
    rlo, rhi = tc["pullback_rsi_band"]
    n = days_to_earnings(ed, asof)
    if None in (above200, vs50, rsi, n):
        return False
    # a past date = results just out, the next report is roughly a quarter away
    far = n < 0 or n >= tc["pullback_min_days_to_earnings"]
    return above200 > 0 and lo50 <= vs50 <= hi50 and rlo <= rsi <= rhi and far


def drift_candidate(d: dict, tc: dict, asof: str) -> bool:
    """Stage 1 (statistics page): results just reported — the shown date is in the last few weeks (or the
    next date is already far away) — and trading above the 50-day average. Stage 2 confirms the reaction
    from daily history."""
    n, vs50 = days_to_earnings(d.get("earnings_date"), asof), d.get("price_vs_sma50")
    if n is None or vs50 is None:
        return False
    just_reported = -tc["drift_recent_report_days"] <= n <= 0 or n >= tc["drift_min_days_to_next_earnings"]
    return just_reported and vs50 > 0


def plan(setup: str, rows: list[dict], tc: dict, signal: dict | None = None) -> dict | None:
    """Volatility stop and minimum 2:1 target from the last completed close (quoted currency)."""
    a = atr(rows)
    if a is None or not rows:
        return None
    close = rows[-1]["close"]
    if setup == "drift":
        if not signal or signal.get("day_low") is None:
            return None
        stop = signal["day_low"] - 0.25 * a
    else:
        stop = close - tc["stop_atr_multiple"] * a
    if stop <= 0 or stop >= close:
        return None
    risk = close - stop
    return {"close": close, "close_date": rows[-1]["date"], "atr14": round(a, 4), "atr_pct": round(a / close * 100, 2),
            "stop": round(stop, 4), "stop_pct": round(-risk / close * 100, 2),
            "min_target": round(close + tc["min_reward_risk"] * risk, 4),
            "size_pct": round(min(tc["max_position_pct"], tc["risk_per_trade_pct"] / (risk / close)), 2)}


def describe(setup: str, p: dict, signal: dict | None = None) -> str:
    """One line for the researcher/evaluator prompt and the screen report."""
    base = (f"last close {p['close']:g} ({p['close_date']}), ATR(14) {p['atr14']:g} ({p['atr_pct']:.1f}%), "
            f"suggested stop {p['stop']:g} ({p['stop_pct']:+.1f}%), minimum 2:1 target {p['min_target']:g}, "
            f"risk-based size {p['size_pct']:.1f}%")
    if setup == "drift" and signal:
        return (f"post-earnings drift: {signal['date']} closed {signal['jump_pct']:+.1f}% on {signal['volume_x']:.1f}x "
                f"average volume, {signal['sessions_ago']} session(s) ago, still holding {signal['held_pct']:.0f}% of the "
                f"jump; stop below that day's low ({signal['day_low']:g}); " + base)
    return "pullback in uptrend: back near the 50-day average after a strong 12-month trend; " + base
