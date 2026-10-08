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
- Structure checks (owner-approved 2026-10-08, so research isn't spent on trades that can't pass):
  room to resistance (the highest high of the last `resistance_lookback_sessions`, i.e. the peak the
  stock came from, must be at least `min_reward_risk` x the stop distance above the close; at new highs
  or within one ATR of it = clear; minor wiggles inside a pullback are not resistance) and, for pullbacks, an intact uptrend
  (the close is still above the most recent swing low; swing points are the fact sheet's).
- Pullback trend-quality checks (owner-approved 2026-10-08, after 6/6 pullbacks were rejected as
  stocks rolling over rather than dipping): 12-month change > `pullback_min_ch1y_pct`; 50-day average
  >= `pullback_min_sma50_over_sma200_pct` above the 200-day; beating SPY over ~6 months by
  >= `pullback_min_rs_6m_pp`; no series of lower highs (the last three swing highs falling); no new
  20-session low in the last 5 sessions; the 50/200-day position measured from the last COMPLETED close
  (the statistics page's price can be live); room to the 3-month peak >= `resistance_min_room_x`.
"""
from __future__ import annotations

import datetime as dt


def swing_points(rows: list[dict], half_window: int = 5, keep: int | None = 3) -> dict:
    """Pivot highs/lows: a bar whose high (low) is the extreme of +/-half_window bars."""
    highs, lows = [], []
    for i in range(half_window, len(rows) - half_window):
        win = rows[i - half_window:i + half_window + 1]
        if rows[i]["high"] is not None and rows[i]["high"] == max(r["high"] or 0 for r in win):
            highs.append((rows[i]["date"], rows[i]["high"]))
        if rows[i]["low"] is not None and rows[i]["low"] == min(r["low"] or float("inf") for r in win):
            lows.append((rows[i]["date"], rows[i]["low"]))
    return {"highs": highs[-keep:] if keep else highs, "lows": lows[-keep:] if keep else lows}


def pct_change(rows: list[dict], sessions: int) -> float | None:
    if len(rows) <= sessions or not rows[-1 - sessions].get("close"):
        return None
    return (rows[-1]["close"] / rows[-1 - sessions]["close"] - 1) * 100


def structure_problem(setup: str, rows: list[dict], p: dict, tc: dict, sma: dict | None = None,
                      spy_rows: list[dict] | None = None) -> str | None:
    """Why this setup can't make a valid trade, or None. Records the 3-month peak on `p`. `sma` (the
    statistics page's 50/200-day averages) and `spy_rows` (SPY daily history) feed the pullback checks."""
    sw = swing_points(rows, keep=None)
    close, risk = p["close"], p["close"] - p["stop"]
    recent = [r for r in rows[-int(tc["resistance_lookback_sessions"]):] if r.get("high") is not None]
    peak = max(recent, key=lambda r: r["high"]) if recent else None
    # within one ATR of the peak = effectively at the high (the latest bars' own highs are not resistance)
    above = [(peak["high"], peak["date"])] if peak and peak["high"] - close > p["atr14"] else []
    p["resistance"] = {"price": above[0][0], "date": above[0][1],
                       "room_x": round((above[0][0] - close) / risk, 2)} if above else None
    if setup == "pullback":
        if sw["lows"] and close <= sw["lows"][-1][1]:
            return f"broke its most recent swing low {sw['lows'][-1][1]:g} ({sw['lows'][-1][0]}): uptrend not intact"
        h3 = sw["highs"][-3:]  # one lower high is a normal bounce inside a pullback; a series is a downtrend
        if len(h3) == 3 and h3[0][1] > h3[1][1] > h3[2][1]:
            return ("a series of lower highs (" + ", ".join(f"{v:g} on {d}" for d, v in h3)
                    + "): rolling over, not pulling back")
        lows = [r["low"] for r in rows[-20:] if r.get("low") is not None]
        if len(lows) == 20 and min(lows[-5:]) < min(lows[:-5]):  # equal lows = a base, not a breakdown
            return "made a new 20-session low in the last 5 sessions: fresh breakdown"
        if sma and sma.get("sma50") and sma.get("sma200"):
            vs50, vs200 = (close / sma["sma50"] - 1) * 100, (close / sma["sma200"] - 1) * 100
            lo50, hi50 = tc["pullback_sma50_band_pct"]
            if vs200 <= 0 or not lo50 <= vs50 <= hi50:
                return (f"at the last completed close {close:g}: {vs50:+.1f}% vs the 50-day, {vs200:+.1f}% vs the "
                        f"200-day (needs {lo50:g}% to {hi50:+g}% and above the 200-day)")
        if spy_rows:
            n = int(tc["rs_sessions"])
            a, b = pct_change(rows, n), pct_change(spy_rows, n)
            if a is not None and b is not None and a - b < tc["pullback_min_rs_6m_pp"]:
                return f"weaker than SPY over {n} sessions ({a:+.1f}% vs {b:+.1f}%)"
    need = tc["resistance_min_room_x"]
    if above and above[0][0] - close < need * risk:
        return (f"3-month peak {above[0][0]:g} ({above[0][1]}) is only {p['resistance']['room_x']:.1f}x the "
                f"stop distance away (needs {need:g}x)")
    return None


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
    """Stage 1 (statistics page): a real uptrend (positive 12 months, 50-day well above the 200-day),
    price back near the 50-day average, not overbought, and no earnings inside the window."""
    above200, vs50, rsi, ed = d.get("price_vs_sma200"), d.get("price_vs_sma50"), d.get("rsi"), d.get("earnings_date")
    ch1y, s50, s200 = d.get("ch1y"), d.get("sma50"), d.get("sma200")
    if ch1y is None or ch1y <= tc["pullback_min_ch1y_pct"] or not s50 or not s200 \
            or (s50 / s200 - 1) * 100 < tc["pullback_min_sma50_over_sma200_pct"]:
        return False
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
            f"risk-based size {p['size_pct']:.1f}%; "
            + (f"3-month peak (resistance) {p['resistance']['price']:g} ({p['resistance']['date']}), "
               f"{p['resistance']['room_x']:.1f}x the stop distance" if p.get("resistance")
               else "at its 3-month high (clear overhead)"))
    if setup == "drift" and signal:
        return (f"post-earnings drift: {signal['date']} closed {signal['jump_pct']:+.1f}% on {signal['volume_x']:.1f}x "
                f"average volume, {signal['sessions_ago']} session(s) ago, still holding {signal['held_pct']:.0f}% of the "
                f"jump; stop below that day's low ({signal['day_low']:g}); " + base)
    return "pullback in uptrend: back near the 50-day average after a strong 12-month trend; " + base
