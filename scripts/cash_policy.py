"""Residual-cash policy (V2.3, owner request 2026-11-16: "Option A, bottom-up residual cash"). Pure functions, no I/O.

The macro stress score no longer sizes a cash reserve (scripts/regime.py stays as telemetry). Cash is whatever the
conviction-4+ pipeline and the caps leave over, above a 1.5% operational floor. This module holds the arithmetic:

- available_cash: deployable cash above the floor, as a fraction of the portfolio.
- min_trade: smallest step for a starter / top-up, min(2.5%, half the target) so a small target still starts.
- core_topup_reserve: cash held back from the tactical sleeve for core top-ups that could really execute
  (core first, tactical second). Starters are taken best-upside first and share their sector / cluster / country
  headroom, so two starters in one nearly-full sector reserve what the sector can absorb once, not twice.
- tactical_cap: what the tactical sleeve may still claim.

All weights are fractions of total portfolio value (0.025 = 2.5%).
"""
from __future__ import annotations

EPS = 1e-9
MIN_TRADE_CAP = 0.025


def residual_mode(cfg: dict) -> bool:
    return (cfg.get("cash_strategy") or {}).get("mode") == "residual"


def available_cash(cash_balance: float, total_value: float, floor: float = 0.015) -> float:
    """Deployable cash above the operational floor, as a fraction of the portfolio."""
    return max(0.0, cash_balance / total_value - floor) if total_value else 0.0


def min_trade(target_weight: float, cap: float = MIN_TRADE_CAP) -> float:
    return min(cap, 0.5 * target_weight)


def core_topup_reserve(starters: list[dict]) -> tuple[float, dict]:
    """(reserve, per-ticker executable top-up). A starter is {"ticker", "current", "target", "upside" (or None),
    "limits": {name: (room, members)}}: `room` is how much more this starter may add before that limit binds and
    `members` the tickers whose additions use the same room (itself included).

    Highest upside first (ticker breaks ties). A top-up is reserved only when it is at least min_trade, or when it
    exactly completes the gap to target; what it reserves is then deducted from the shared room of the starters
    after it. Otherwise it reserves 0 and leaves the room untouched."""
    added: dict[str, float] = {}
    out: dict[str, float] = {}
    for s in sorted(starters, key=lambda s: (s.get("upside") is None, -(s.get("upside") or 0.0), s["ticker"])):
        gap = s["target"] - s["current"]
        if gap <= EPS:
            continue
        rooms = [room - sum(added.get(m, 0.0) for m in members) for room, members in s.get("limits", {}).values()]
        ex = max(0.0, min([gap] + rooms))
        if ex >= min_trade(s["target"]) - EPS or (ex > EPS and abs(ex - gap) <= EPS):
            added[s["ticker"]] = out[s["ticker"]] = ex
        else:
            out[s["ticker"]] = 0.0
    return sum(added.values()), out


def tactical_cap(active_tactical_weight: float, available_cash_post_core: float, ceiling: float = 0.40) -> float:
    return max(0.0, min(ceiling - active_tactical_weight, available_cash_post_core))
