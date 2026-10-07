"""Paper portfolio engine. ALL portfolio arithmetic lives here, never in agent prose.

Paper only: no broker, no broker API, no real orders.

Commands:
    python scripts/portfolio.py submit requests.json [--asof YYYY-MM-DD] [--dry-run]
    python scripts/portfolio.py mark [--asof YYYY-MM-DD]
    python scripts/portfolio.py returns [--asof YYYY-MM-DD]
    python scripts/portfolio.py status [--asof YYYY-MM-DD]
    python scripts/portfolio.py stamp --asof YYYY-MM-DD      (weekly run: record the scan date)

A trade-request file is a JSON list. Each request:
    {"ticker": "AAPL", "action": "BUY|ADD|TRIM|SELL", "position_type": "CORE|TACTICAL",
     "conviction": 1-5, "reason": "...", "research_note": "research/AAPL/2026-10-06.md",
     "thesis": "...",                                   # BUY
     "triggers": [{"text": "...", "check": {...}}],     # CORE BUY (2-4)
     "exit_plan": {"target": 250.0, "stop": 200.0, "time_limit": "2027-01-06"},  # TACTICAL BUY
     "target_weight_pct": 4.0,                          # TACTICAL BUY/ADD, optional TRIM
     "replaces": "XYZ", "replacement_reason": "...",    # when the replacement rule applies
     "core_initiation": true,                           # BUY CORE on a held TACTICAL (re-initiation)
     "fill_date": "YYYY-MM-DD"}                         # SELL/TRIM only: fill at that day's close
                                                        # (mechanical tactical exits at the first crossing close)
The portfolio is kept entirely in USD. Tactical exit-plan levels are in the share's quoted
currency (GBX for LSE) because they are compared with that share's own daily closes.
"""
from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import json
import math
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, core_trigger_problem, load_config, read_watchlist  # noqa: E402

PORT = ROOT / "portfolio"
LEDGER_COLS = ["date", "ticker", "type", "side", "shares", "fill_price", "currency", "fill_close_date",
               "fx_usd_per_unit", "gross_usd", "spread_usd", "fx_fee_usd", "costs_usd",
               "cash_change_usd", "source_url", "fx_source_url", "reason"]
REJECT_COLS = ["date", "ticker", "action", "type", "rule", "detail"]
VAL_COLS = ["date", "phase", "total_usd", "cash_usd", "core_usd", "tactical_usd",
            "core_in", "core_out", "tactical_in", "tactical_out", "baseline_usd", "spy_close"]
ACTIONS = {"BUY", "ADD", "TRIM", "SELL", "HOLD"}
TYPES = {"CORE", "TACTICAL"}
BASE_CCY = "USD"
# quoted minor units -> (major currency, divisor); used for display only (FX rates are per quoted unit)
MINOR_UNITS = {"GBX": ("GBP", 100), "GBp": ("GBP", 100), "ZAC": ("ZAR", 100), "ZAc": ("ZAR", 100), "ILA": ("ILS", 100)}


# --------------------------------------------------------------------------- market data
class Market:
    """Closes, sectors and USD rates, all from stockanalysis.com (via a Fetcher-like object).
    Fills use the most recent COMPLETED daily close (date < asof)."""

    def __init__(self, fetcher, asof: str, cfg: dict):
        self.f, self.asof, self.cfg = fetcher, asof, cfg
        self._hist, self._sector, self._fx = {}, {}, {}

    def history(self, ticker: str) -> dict:
        if ticker not in self._hist:
            s = self.f.section(ticker, "history")
            rows = [r for r in s["data"]["rows"] if r["date"] < self.asof]
            if not rows:
                raise DataError(s["source_url"], "history.close", f"no completed close before {self.asof}")
            self._hist[ticker] = {"url": s["source_url"], "rows": rows,
                                  "currency": s["data"]["info"]["price_currency"], "news": s["data"].get("news", [])}
        return self._hist[ticker]

    def sector(self, ticker: str) -> str:
        if ticker not in self._sector:
            self._sector[ticker] = self.f.section(ticker, "overview")["data"]["sector"]
        return self._sector[ticker]

    def fx(self, ccy: str) -> dict:
        """USD per quoted unit (e.g. per penny for GBX), implied by stockanalysis.com's own USD prices."""
        if ccy not in self._fx:
            from universe import implied_fx
            self._fx.update(implied_fx(self.f, {ccy}, asof=self.asof))
            if ccy not in self._fx:
                raise DataError("https://stockanalysis.com/list/biggest-companies/", "fx",
                                f"[data unavailable] no USD rate for {ccy} on stockanalysis.com")
        return self._fx[ccy]

    def quote(self, ticker: str, on_or_before: str | None = None) -> dict:
        h = self.history(ticker)
        rows = [r for r in h["rows"] if on_or_before is None or r["date"] <= on_or_before]
        if not rows:
            raise DataError(h["url"], "history.close", f"no close on/before {on_or_before}")
        last = rows[-1]
        return self.price(ticker, last["close"], last["date"], h["currency"], h["url"])

    def price(self, ticker, close, date, ccy, url) -> dict:
        fx = None
        if ccy == "USD":
            usd = close
        else:
            fx = self.fx(ccy)
            usd = close * fx["rate"]
        return {"ticker": ticker, "close": close, "date": date, "currency": ccy, "url": url,
                "price_usd": usd, "fx": fx}


# --------------------------------------------------------------------------- costs
def trade_costs(gross_usd: float, currency: str, cfg: dict) -> dict:
    """Spread on every trade; FX fee on every trade in a non-USD share. No stamp duty."""
    c = cfg["costs"]
    spread = round(gross_usd * c["spread_pct"] / 100, 2)
    fx = round(gross_usd * c["fx_fee_pct"] / 100, 2) if currency != BASE_CCY else 0.0
    return {"spread_usd": spread, "fx_fee_usd": fx, "costs_usd": round(spread + fx, 2)}


# --------------------------------------------------------------------------- state io
def empty_state(cfg: dict) -> dict:
    return {"base_currency": BASE_CCY, "inception_date": None, "cash_usd": float(cfg["portfolio"]["starting_cash_usd"]),
            "holdings": {}, "flows": {"CORE": {"in": 0.0, "out": 0.0}, "TACTICAL": {"in": 0.0, "out": 0.0}},
            "baseline": None, "last_marked": None}


def load_state(path: Path, cfg: dict) -> dict:
    return json.loads(path.read_text()) if path.exists() else empty_state(cfg)


def atomic_write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    os.replace(tmp, path)


def append_csv(path: Path, cols: list[str], rows: list[dict]):
    if not rows:
        return
    new = not path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


# --------------------------------------------------------------------------- valuation
def mark(state: dict, mkt: Market) -> dict:
    """Mark holdings (and baseline) to the latest completed close. Mutates state."""
    for t, h in state["holdings"].items():
        q = mkt.quote(t)
        h.update(last_close=q["close"], last_close_date=q["date"], last_price_usd=round(q["price_usd"], 6),
                 market_value_usd=round(h["shares"] * q["price_usd"], 2))
    state["last_marked"] = mkt.asof
    return totals(state)


def totals(state: dict) -> dict:
    core = sum(h["market_value_usd"] for h in state["holdings"].values() if h["type"] == "CORE")
    tac = sum(h["market_value_usd"] for h in state["holdings"].values() if h["type"] == "TACTICAL")
    total = state["cash_usd"] + core + tac
    sectors: dict[str, float] = {}
    for h in state["holdings"].values():
        sectors[h["sector"]] = sectors.get(h["sector"], 0.0) + h["market_value_usd"]
    return {"total": total, "cash": state["cash_usd"], "core": core, "tactical": tac, "sectors": sectors,
            "n": len(state["holdings"])}


def baseline_value(state: dict, mkt: Market) -> float | None:
    b = state.get("baseline")
    if not b:
        return None
    return b["cash_usd"] + sum(v["shares"] * mkt.quote(t)["price_usd"] for t, v in b["holdings"].items())


def valuation_row(state: dict, mkt: Market, phase: str) -> dict:
    tt = totals(state)
    spy = mkt.quote(mkt.cfg["portfolio"]["benchmark"])
    fl = state["flows"]
    bv = baseline_value(state, mkt)
    return {"date": spy["date"], "phase": phase, "total_usd": round(tt["total"], 2), "cash_usd": round(tt["cash"], 2),
            "core_usd": round(tt["core"], 2), "tactical_usd": round(tt["tactical"], 2),
            "core_in": round(fl["CORE"]["in"], 2), "core_out": round(fl["CORE"]["out"], 2),
            "tactical_in": round(fl["TACTICAL"]["in"], 2), "tactical_out": round(fl["TACTICAL"]["out"], 2),
            "baseline_usd": "" if bv is None else round(bv, 2), "spy_close": spy["close"]}


# --------------------------------------------------------------------------- returns
def interval_return(mv0, mv1, fin, fout) -> float | None:
    """Modified Dietz for one interval: buys (fin, incl. costs) weighted at the start,
    sale proceeds (fout) at the end. None when nothing was invested."""
    denom = mv0 + fin
    if denom <= 0:
        return None
    return (mv1 - mv0 - fin + fout) / denom


def chain(rows: list[dict], key_mv: str | None = None, key_in: str | None = None, key_out: str | None = None,
          key_level: str | None = None) -> float | None:
    """Chain-link returns across consecutive valuation rows. With key_level, a simple
    level ratio (no flows) is used: last/first - 1."""
    if len(rows) < 2:
        return None
    if key_level:
        a, b = rows[0][key_level], rows[-1][key_level]
        if a in ("", None) or b in ("", None) or float(a) == 0:
            return None
        return float(b) / float(a) - 1
    growth, seen = 1.0, False
    for r0, r1 in zip(rows, rows[1:]):
        fin = float(r1[key_in]) - float(r0[key_in])
        fout = float(r1[key_out]) - float(r0[key_out])
        r = interval_return(float(r0[key_mv]), float(r1[key_mv]), fin, fout)
        if r is not None:
            growth *= 1 + r
            seen = True
    return growth - 1 if seen else None


def returns_table(vals: list[dict], asof: str) -> dict:
    """Week (since previous run), month-to-date and since-inception returns for
    total, core, tactical, baseline and SPY (all USD)."""
    if not vals:
        return {}
    run_dates = sorted({v["date"] for v in vals})
    last_date = run_dates[-1]
    prev_date = run_dates[-2] if len(run_dates) > 1 else run_dates[0]
    month_start = last_date[:8] + "01"
    before_month = [d for d in run_dates if d < month_start]
    mtd_from = before_month[-1] if before_month else run_dates[0]

    def window(start_date):
        rows = [v for v in vals if v["date"] >= start_date]
        first_idx = max(i for i, v in enumerate(rows) if v["date"] == start_date)  # last row of start date
        return rows[first_idx:]

    out = {}
    for label, start in (("week", prev_date), ("mtd", mtd_from), ("inception", run_dates[0])):
        w = window(start) if label != "inception" else vals
        bl = [v for v in w if v["baseline_usd"] not in ("", None)]
        out[label] = {
            "from": w[0]["date"], "to": w[-1]["date"],
            "total": chain(w, key_level="total_usd"),
            "core": chain(w, "core_usd", "core_in", "core_out"),
            "tactical": chain(w, "tactical_usd", "tactical_in", "tactical_out"),
            "baseline": chain(bl, key_level="baseline_usd") if len(bl) > 1 else None,
            "spy": chain(w, key_level="spy_close"),
        }
    return out


def format_returns(rt: dict) -> str:
    def p(x):
        return "n/a" if x is None else f"{x * 100:+.2f}%"

    def rel(x, s):
        return "n/a" if x is None or s is None else f"{(x - s) * 100:+.2f}pp"

    lines = ["| Period | Total | Core | Tactical | Baseline | SPY | Total vs SPY | Core vs SPY | Tactical vs SPY | Baseline vs SPY |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for k, name in (("week", "Week"), ("mtd", "Month-to-date"), ("inception", "Since inception")):
        r = rt.get(k)
        if not r:
            continue
        lines.append(f"| {name} ({r['from']}→{r['to']}) | {p(r['total'])} | {p(r['core'])} | {p(r['tactical'])} | "
                     f"{p(r['baseline'])} | {p(r['spy'])} | {rel(r['total'], r['spy'])} | {rel(r['core'], r['spy'])} | "
                     f"{rel(r['tactical'], r['spy'])} | {rel(r['baseline'], r['spy'])} |")
    return "\n".join(lines)


# --------------------------------------------------------------------------- validation + application
class Reject(Exception):
    def __init__(self, rule: str, detail: str):
        self.rule, self.detail = rule, detail
        super().__init__(f"{rule}: {detail}")


class Engine:
    def __init__(self, state: dict, mkt: Market, cfg: dict, watchlist: dict, today: str):
        self.s, self.mkt, self.cfg, self.watch, self.today = state, mkt, cfg, watchlist, today
        self.ledger: list[dict] = []
        self.rejections: list[dict] = []
        self.applied: list[dict] = []

    # ---- helpers
    def pv(self, s=None) -> float:
        return totals(s or self.s)["total"]

    def weight(self, s, ticker) -> float:
        h = s["holdings"].get(ticker)
        return 0.0 if not h else h["market_value_usd"] / self.pv(s) * 100

    def cost_rate(self, currency: str) -> float:
        c = self.cfg["costs"]
        return (c["spread_pct"] + (c["fx_fee_pct"] if currency != BASE_CCY else 0)) / 100

    def capped_shares(self, target_pct, pv, current_mv, q) -> int:
        """Shares to reach target_pct without exceeding it once this trade's own costs
        have reduced the portfolio: n*p + cur <= t*(pv - n*p*c)."""
        t = target_pct / 100
        return math.floor((t * pv - current_mv) / (q["price_usd"] * (1 + t * self.cost_rate(q["currency"]))))

    def core_size(self, conviction: int) -> float:
        return float(self.cfg["core"]["conviction_size_pct"][str(conviction)])

    # ---- the trade primitive (no rule checks; callers validate)
    def _execute(self, s, ticker, ptype, side, shares, q, reason):
        gross = round(shares * q["price_usd"], 2)
        cost = trade_costs(gross, q["currency"], self.cfg)
        if side in ("BUY", "ADD"):
            cash_change = -(gross + cost["costs_usd"])
            s["flows"][ptype]["in"] += -cash_change
        else:
            cash_change = gross - cost["costs_usd"]
            s["flows"][ptype]["out"] += cash_change
        s["cash_usd"] = round(s["cash_usd"] + cash_change, 2)
        h = s["holdings"].get(ticker)
        if side in ("BUY", "ADD"):
            h["shares"] += shares
            h["cost_basis_usd"] = round(h.get("cost_basis_usd", 0.0) + gross + cost["costs_usd"], 2)
        else:
            h["cost_basis_usd"] = round(h["cost_basis_usd"] * (1 - shares / h["shares"]), 2)
            h["shares"] -= shares
        h["market_value_usd"] = round(h["shares"] * q["price_usd"], 2)
        if h["shares"] == 0:
            del s["holdings"][ticker]
        return {"date": self.today, "ticker": ticker, "type": ptype, "side": side, "shares": shares,
                "fill_price": q["close"], "currency": q["currency"], "fill_close_date": q["date"],
                "fx_usd_per_unit": round(q["fx"]["rate"], 8) if q["fx"] else "", "gross_usd": gross, **cost,
                "cash_change_usd": round(cash_change, 2), "source_url": q["url"],
                "fx_source_url": q["fx"]["url"] if q["fx"] else "", "reason": reason}

    # ---- schema
    def _schema(self, r):
        for k in ("ticker", "action", "position_type", "reason"):
            if not r.get(k):
                raise Reject("SCHEMA", f"missing '{k}'")
        if r["action"] not in ACTIONS:
            raise Reject("SCHEMA", f"action must be one of {sorted(ACTIONS)}")
        if r["position_type"] not in TYPES:
            raise Reject("SCHEMA", "position_type must be CORE or TACTICAL")
        if r["action"] != "SELL":
            c = r.get("conviction")
            if not isinstance(c, int) or not 1 <= c <= 5:
                raise Reject("SCHEMA", "conviction must be an integer 1-5")

    # ---- per-action validation + application on working state `s`; returns ledger rows
    def _apply(self, s, r) -> list[dict]:
        t, act, ptype = r["ticker"], r["action"], r["position_type"]
        held = s["holdings"].get(t)
        rows = []
        if act == "BUY":
            conversion = bool(held and held["type"] == "TACTICAL" and ptype == "CORE" and r.get("core_initiation"))
            if held and not conversion:
                if held["type"] != ptype:
                    raise Reject("LABEL_FIXED", f"{t} is held as {held['type']}; a tactical position can only become "
                                                "core via a full core initiation (core_initiation=true + research_note)")
                raise Reject("ALREADY_HELD", f"{t} already held; use ADD")
            if conversion and not r.get("research_note"):
                raise Reject("LABEL_FIXED", "core re-initiation of a tactical holding needs research_note")
            if t not in self.watch and not held:
                raise Reject("WATCHLIST", f"{t} is not in universe/universe.csv or universe/watchlist.txt")
            if r["conviction"] == 1:
                raise Reject("CONVICTION_NO_POSITION", "conviction 1 means no position")
            q = self.mkt.quote(t)
            pv = self.pv(s)
            if ptype == "CORE":
                self._core_entry_fields(r)
                target_pct = self.core_size(r["conviction"])
            else:
                target_pct = self._tactical_entry_fields(r, q)
            if conversion:
                rows.append(self._convert(s, t, r, q))
                held = s["holdings"][t]
                delta = math.floor((target_pct / 100 * pv - held["market_value_usd"]) / q["price_usd"])
                if delta > 0:
                    rows.append(self._execute(s, t, "CORE", "ADD", delta, q, r["reason"]))
                elif delta < 0:
                    rows.append(self._execute(s, t, "CORE", "TRIM", -delta, q, r["reason"]))
            else:
                shares = math.floor(target_pct / 100 * pv / q["price_usd"]) if ptype == "CORE" \
                    else self.capped_shares(target_pct, pv, 0.0, q)
                if shares < 1:
                    raise Reject("MIN_SHARES", f"{target_pct}% of ${pv:,.0f} buys <1 share at ${q['price_usd']:,.2f}")
                s["holdings"][t] = self._new_holding(t, ptype, r, q)
                rows.append(self._execute(s, t, ptype, "BUY", shares, q, r["reason"]))
        elif act == "HOLD":  # re-initiation outcome: no trade, but a new decision record for the holding
            if not held:
                raise Reject("NOT_HELD", f"{t} is not held")
            if held["type"] != ptype:
                raise Reject("LABEL_FIXED", f"{t} is held as {held['type']}, request says {ptype}")
            self._refresh_decision(held, r)
        elif act in ("ADD", "TRIM", "SELL"):
            if not held:
                raise Reject("NOT_HELD", f"{t} is not held")
            if held["type"] != ptype:
                raise Reject("LABEL_FIXED", f"{t} is held as {held['type']}, request says {ptype}")
            q = self.mkt.quote(t, r.get("fill_date"))
            if r.get("fill_date") and q["date"] != r["fill_date"]:
                raise Reject("SCHEMA", f"no daily close for {t} on fill_date {r['fill_date']}")
            pv = self.pv(s)
            cur = held["market_value_usd"]
            if act == "SELL":
                rows.append(self._execute(s, t, ptype, "SELL", held["shares"], q, r["reason"]))
            else:
                if r["conviction"] == 1 and act == "ADD":
                    raise Reject("CONVICTION_NO_POSITION", "conviction 1 means no position; use SELL")
                if ptype == "CORE":
                    target_pct = r.get("target_weight_pct") if act == "TRIM" and r.get("target_weight_pct") is not None \
                        else self.core_size(r["conviction"])
                else:
                    target_pct = r.get("target_weight_pct")
                    if target_pct is None:
                        raise Reject("SCHEMA", "tactical ADD/TRIM needs target_weight_pct")
                delta = (target_pct / 100 * pv - cur) / q["price_usd"]
                if act == "ADD":
                    n = math.floor(delta) if ptype == "CORE" else self.capped_shares(target_pct, pv, cur, q)
                    if n < 1:
                        raise Reject("CORE_SIZE" if ptype == "CORE" else "TACTICAL_SIZE",
                                     f"ADD to {target_pct}% does not increase the position (now {cur / pv * 100:.2f}%)")
                    rows.append(self._execute(s, t, ptype, "ADD", n, q, r["reason"]))
                    held = s["holdings"][t]
                    held["conviction"] = r["conviction"]
                else:
                    n = round(-delta)  # nearest share to the target weight
                    if n < 1:
                        raise Reject("CORE_SIZE" if ptype == "CORE" else "TACTICAL_SIZE",
                                     f"TRIM to {target_pct}% does not reduce the position (now {cur / pv * 100:.2f}%)")
                    if n >= held["shares"]:
                        raise Reject("SCHEMA", "TRIM would close the position; use SELL")
                    rows.append(self._execute(s, t, ptype, "TRIM", n, q, r["reason"]))
                    s["holdings"][t]["conviction"] = r["conviction"]
                if t in s["holdings"]:
                    self._refresh_decision(s["holdings"][t], r)
        return rows

    def _refresh_decision(self, h: dict, r: dict):
        """A re-initiation (HOLD/ADD/TRIM) replaces a CORE holding's thesis, triggers and conviction, so a
        fired trigger is not re-evaluated every week. Tactical exit plans are never changed."""
        if not r.get("triggers") and not r.get("thesis"):
            return
        if h["type"] == "CORE":
            if r.get("triggers") is not None:
                self._core_entry_fields(r)
                h["triggers"] = r["triggers"]
            if r.get("thesis"):
                h["thesis"] = r["thesis"]
        h["conviction"] = r.get("conviction", h["conviction"])
        if r.get("research_note"):
            h["research_note"] = r["research_note"]
        h["last_decision"] = {"date": self.today, "action": r["action"], "conviction": h["conviction"]}

    def _core_entry_fields(self, r):
        trig = r.get("triggers") or []
        if not 2 <= len(trig) <= 4:
            raise Reject("CORE_TRIGGERS", "a CORE entry needs 2-4 measurable invalidation triggers")
        for x in trig:
            prob = core_trigger_problem(x if isinstance(x, dict) else {"text": str(x)})
            if prob:
                raise Reject("CORE_TRIGGERS", f"core triggers must be thesis-only ({prob})")
        if not r.get("thesis"):
            raise Reject("SCHEMA", "missing 'thesis'")

    def _tactical_entry_fields(self, r, q) -> float:
        tc = self.cfg["tactical"]
        ep = dict(r.get("exit_plan") or {})
        if ep.get("target") is None:
            raise Reject("TACTICAL_EXIT_PLAN", "tactical entry needs exit_plan.target")
        if ep.get("stop") is None:
            ep["stop"] = round(q["close"] * (1 + tc["default_stop_pct"] / 100), 4)
        if not ep.get("time_limit"):
            ep["time_limit"] = _add_months(self.today, tc["default_time_limit_months"])
        max_limit = _add_months(self.today, tc["default_time_limit_months"])
        if not ep["stop"] < q["close"] < ep["target"]:
            raise Reject("TACTICAL_EXIT_PLAN",
                         f"need stop < last close < target (stop {ep['stop']}, close {q['close']}, target {ep['target']})")
        if not self.today < ep["time_limit"] <= max_limit:
            raise Reject("TACTICAL_EXIT_PLAN", f"time_limit must be after today and on/before {max_limit}")
        if not r.get("thesis"):
            raise Reject("SCHEMA", "missing 'thesis' (catalyst)")
        r["exit_plan"] = ep
        w = r.get("target_weight_pct", tc["max_position_pct"])
        if not 0 < w <= tc["max_position_pct"]:
            raise Reject("TACTICAL_POSITION_MAX", f"tactical size {w}% exceeds {tc['max_position_pct']}%")
        return float(w)

    def _new_holding(self, t, ptype, r, q) -> dict:
        return {"type": ptype, "shares": 0, "currency": q["currency"], "sector": self.mkt.sector(t),
                "cost_basis_usd": 0.0, "conviction": r["conviction"], "thesis": r.get("thesis", ""),
                "triggers": r.get("triggers") if ptype == "CORE" else None,
                "exit_plan": r.get("exit_plan") if ptype == "TACTICAL" else None,
                "entry_date": self.today, "entry_price": q["close"], "entry_close_date": q["date"],
                "entry_url": q["url"], "research_note": r.get("research_note", ""),
                "last_close": q["close"], "last_close_date": q["date"], "last_price_usd": q["price_usd"],
                "market_value_usd": 0.0}

    def _convert(self, s, t, r, q) -> dict:
        """Tactical -> core via full core initiation: a NEW entry decision. No costs."""
        h = s["holdings"][t]
        mv = h["market_value_usd"]
        s["flows"]["TACTICAL"]["out"] += mv
        s["flows"]["CORE"]["in"] += mv
        h.update(type="CORE", conviction=r["conviction"], thesis=r["thesis"], triggers=r["triggers"], exit_plan=None,
                 entry_date=self.today, entry_price=q["close"], entry_close_date=q["date"], entry_url=q["url"],
                 research_note=r["research_note"], converted_from="TACTICAL")
        return {"date": self.today, "ticker": t, "type": "CORE", "side": "CONVERT", "shares": h["shares"],
                "fill_price": q["close"], "currency": q["currency"], "fill_close_date": q["date"], "gross_usd": mv,
                "spread_usd": 0, "fx_fee_usd": 0, "costs_usd": 0, "cash_change_usd": 0,
                "source_url": q["url"], "reason": "core re-initiation of tactical holding: " + r["reason"]}

    # ---- portfolio-level limits checked AFTER a trade on the working state
    def limit_breaches(self, s, r) -> list[tuple[str, str]]:
        p, tc, cc = self.cfg["portfolio"], self.cfg["tactical"], self.cfg["core"]
        tt = totals(s)
        pv = tt["total"]
        out = []
        if tt["cash"] / pv * 100 < p["min_cash_pct"] - 1e-9:
            out.append(("CASH_MIN", f"cash would be {tt['cash'] / pv * 100:.2f}% (< {p['min_cash_pct']}%)"))
        if tt["n"] > p["max_holdings"]:
            out.append(("MAX_HOLDINGS", f"{tt['n']} holdings (> {p['max_holdings']})"))
        if tt["tactical"] / pv * 100 > tc["max_sleeve_pct"] + 1e-9:
            out.append(("TACTICAL_SLEEVE_MAX", f"tactical sleeve {tt['tactical'] / pv * 100:.2f}% (> {tc['max_sleeve_pct']}%)"))
        h = s["holdings"].get(r["ticker"])
        if h and r["action"] in ("BUY", "ADD"):
            sec = tt["sectors"][h["sector"]] / pv * 100
            if sec > p["max_sector_pct"] + 1e-9:
                out.append(("SECTOR_MAX", f"{h['sector']} would be {sec:.2f}% (> {p['max_sector_pct']}%)"))
            w = h["market_value_usd"] / pv * 100
            if h["type"] == "TACTICAL" and w > tc["max_position_pct"] + 1e-9:
                out.append(("TACTICAL_POSITION_MAX", f"{w:.2f}% (> {tc['max_position_pct']}%)"))
            if h["type"] == "CORE" and w > cc["trim_above_pct"] + 1e-9:
                out.append(("CORE_POSITION_MAX", f"{w:.2f}% (> {cc['trim_above_pct']}%)"))
        return out

    def _reject(self, r, rule, detail):
        self.rejections.append({"date": self.today, "ticker": r.get("ticker", ""), "action": r.get("action", ""),
                                "type": r.get("position_type", ""), "rule": rule, "detail": detail})

    def process(self, requests: list[dict]):
        order = {"SELL": 0, "TRIM": 1, "ADD": 2, "BUY": 3}
        for r in sorted(requests, key=lambda r: order.get(r.get("action"), 9)):
            r = copy.deepcopy(r)
            try:
                self._schema(r)
                work = copy.deepcopy(self.s)
                rows = []
                if r["action"] == "BUY" and r.get("replaces"):
                    rep = r["replaces"]
                    if rep not in work["holdings"] or rep == r["ticker"]:
                        raise Reject("REPLACEMENT_INVALID", f"replaced holding {rep} is not held")
                    if not r.get("replacement_reason"):
                        raise Reject("REPLACEMENT_INVALID", "replacement_reason missing (why the new idea is better)")
                    rh = work["holdings"][rep]
                    rows.append(self._execute(work, rep, rh["type"], "SELL", rh["shares"], self.mkt.quote(rep),
                                              f"replaced by {r['ticker']}: {r['replacement_reason']}"))
                rows += self._apply(work, r)
                breaches = self.limit_breaches(work, r)
                if breaches:
                    if r["action"] == "BUY" and not r.get("replaces") and any(
                            b[0] in ("CASH_MIN", "MAX_HOLDINGS", "TACTICAL_SLEEVE_MAX", "SECTOR_MAX") for b in breaches):
                        raise Reject("REPLACEMENT_REQUIRED", "BUY would breach " + "; ".join(d for _, d in breaches)
                                     + " -- name the holding it replaces and why the new idea is better")
                    raise Reject(breaches[0][0], "; ".join(d for _, d in breaches))
            except Reject as e:
                self._reject(r, e.rule, e.detail)
                continue
            self.s.clear()
            self.s.update(work)
            self.ledger += rows
            self.applied.append(r)

    def update_baseline(self):
        """Baseline = the first week's picks held unchanged. Trades in the first 7 days
        after inception are mirrored into it, then it is frozen."""
        if not self.applied and self.s.get("baseline") is None:
            return
        if self.s.get("inception_date") is None:
            self.s["inception_date"] = self.today
        b = self.s.get("baseline")
        freeze_after = _add_days(self.s["inception_date"], 7)
        if b is None or (self.today < freeze_after and self.ledger):
            self.s["baseline"] = {"start": self.s["inception_date"], "frozen_from": freeze_after,
                                  "cash_usd": self.s["cash_usd"],
                                  "holdings": {t: {"shares": h["shares"]} for t, h in self.s["holdings"].items()}}


def _add_months(iso: str, months: int) -> str:
    d = dt.date.fromisoformat(iso)
    y, m = divmod(d.month - 1 + months, 12)
    for day in (d.day, 30, 29, 28):
        try:
            return dt.date(d.year + y, m + 1, day).isoformat()
        except ValueError:
            continue
    raise ValueError(iso)


def _add_days(iso: str, days: int) -> str:
    return (dt.date.fromisoformat(iso) + dt.timedelta(days=days)).isoformat()


# --------------------------------------------------------------------------- CLI
def target_warnings(state: dict, cfg: dict) -> list[str]:
    """Targets that are reported, not enforced by rejection (they can't hold while building up)."""
    p, tt = cfg["portfolio"], totals(state)
    out = []
    if tt["n"] < p["min_holdings"]:
        out.append(f"holdings {tt['n']} below target minimum {p['min_holdings']}")
    if tt["total"] and tt["cash"] / tt["total"] * 100 > p["max_cash_pct"]:
        out.append(f"cash {tt['cash'] / tt['total'] * 100:.1f}% above target maximum {p['max_cash_pct']}%")
    for t, h in state["holdings"].items():
        w = h["market_value_usd"] / tt["total"] * 100
        if h["type"] == "CORE" and w > cfg["core"]["trim_above_pct"]:
            out.append(f"{t} core weight {w:.1f}% above {cfg['core']['trim_above_pct']}% -> TRIM due")
    return out


def investable() -> dict:
    """Tickers a BUY may target: the universe (S&P 500, FTSE 100, All-World proxy) plus the watchlist."""
    names = dict(read_watchlist())
    uni = ROOT / "universe" / "universe.csv"
    if uni.exists():
        names.update({r["ticker"]: None for r in read_csv(uni)})
    return names


def run_submit(requests, state_path, mkt, cfg, watch, today, dry_run=False, port_dir=PORT) -> dict:
    state = load_state(state_path, cfg)
    if not read_csv(port_dir / "valuations.csv") and not dry_run:
        append_csv(port_dir / "valuations.csv", VAL_COLS, [valuation_row(state, mkt, "inception")])
    mark(state, mkt)
    cash_before = state["cash_usd"]
    eng = Engine(state, mkt, cfg, watch, today)
    eng.process(requests)
    eng.update_baseline()
    summary = {"cash_before_usd": cash_before, "cash_after_usd": state["cash_usd"],
               "applied": [{k: r.get(k, "") for k in ("side", "ticker", "type", "shares", "fill_price", "currency",
                                                     "fill_close_date", "gross_usd", "costs_usd", "cash_change_usd",
                                                     "reason")}
                           for r in eng.ledger],
               "rejected": eng.rejections, "warnings": target_warnings(state, cfg)}
    if not dry_run:
        append_csv(port_dir / "rejections.csv", REJECT_COLS, eng.rejections)
        if eng.applied:  # nothing applied -> state.json, ledger and valuations are left byte-for-byte untouched
            atomic_write(state_path, json.dumps(state, indent=1, sort_keys=True))
            append_csv(port_dir / "ledger.csv", LEDGER_COLS, eng.ledger)
            append_csv(port_dir / "valuations.csv", VAL_COLS, [valuation_row(state, mkt, "post")])
    return summary


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["submit", "mark", "returns", "status", "stamp"])
    ap.add_argument("--save", help="submit: also write the JSON summary to this path")
    ap.add_argument("requests", nargs="?")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    cfg = load_config()
    from fetch_data import Fetcher

    mkt = Market(Fetcher(cfg), args.asof, cfg)
    state_path = PORT / "state.json"
    try:
        if args.cmd == "submit":
            reqs = json.loads(Path(args.requests).read_text())
            out = run_submit(reqs, state_path, mkt, cfg, investable(), args.asof, args.dry_run)
            out["dry_run"] = args.dry_run
            if args.save:
                Path(args.save).parent.mkdir(parents=True, exist_ok=True)
                Path(args.save).write_text(json.dumps(out, indent=1))
            print(json.dumps(out, indent=1))
        elif args.cmd == "stamp":  # record the weekly scan date (end of a successful weekly run)
            state = load_state(state_path, cfg)
            state["last_scan"] = args.asof
            atomic_write(state_path, json.dumps(state, indent=1, sort_keys=True))
            print(f"last_scan = {args.asof}")
        elif args.cmd == "mark":
            state = load_state(state_path, cfg)
            if not read_csv(PORT / "valuations.csv"):
                append_csv(PORT / "valuations.csv", VAL_COLS, [valuation_row(state, mkt, "inception")])
            mark(state, mkt)
            atomic_write(state_path, json.dumps(state, indent=1, sort_keys=True))
            append_csv(PORT / "valuations.csv", VAL_COLS, [valuation_row(state, mkt, "pre")])
            print(json.dumps({k: round(v, 2) if isinstance(v, float) else v for k, v in totals(state).items()}))
        elif args.cmd == "returns":
            print(format_returns(returns_table(read_csv(PORT / "valuations.csv"), args.asof)))
        elif args.cmd == "status":
            state = load_state(state_path, cfg)
            tt = totals(state)
            print(json.dumps({"total_usd": round(tt["total"], 2), "cash_pct": round(tt["cash"] / tt["total"] * 100, 2),
                              "holdings": {t: {"type": h["type"], "weight_pct": round(h["market_value_usd"] / tt["total"] * 100, 2),
                                               "sector": h["sector"]} for t, h in state["holdings"].items()},
                              "warnings": target_warnings(state, cfg)}, indent=1))
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
