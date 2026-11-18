"""Build docs/index.html: a self-contained portfolio dashboard (no external libraries, no model calls).

Reads portfolio/state.json, valuations.csv, ledger.csv, decisions.csv, universe/universe.csv (names,
optional) and the latest reports/screen/, reports/risk/ and reports/attribution/ <date>.json. Open the file in any browser, or publish it with
GitHub Pages (Settings -> Pages -> Deploy from branch: main, /docs).

    python scripts/dashboard.py [--out docs/index.html]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Ticker, load_config  # noqa: E402
import entry_watch  # noqa: E402
import portfolio  # noqa: E402

OUT = ROOT / "docs" / "index.html"


def _csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def repo_url() -> str | None:
    try:
        u = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return None
    if u.startswith("git@github.com:"):
        u = "https://github.com/" + u.split(":", 1)[1]
    return u[:-4] if u.endswith(".git") else (u or None)


def series(vals: list[dict], start_cash: float) -> list[dict]:
    """One point per valuation date (the last row of each date), indexed to 100 at inception."""
    by_date: dict[str, dict] = {}
    for v in vals:
        by_date[v["date"]] = v
    pts = [by_date[d] for d in sorted(by_date)]
    if not pts:
        return []
    spy0 = _f(pts[0]["spy_close"])
    inv = {p["date"]: p for p in portfolio.invested_series(vals)}
    out, tw, prev = [], None, None
    for v in pts:
        tw, prev = invested_tw(v, prev, tw), v
        tot, spy, base, i = _f(v["total_usd"]), _f(v["spy_close"]), _f(v.get("baseline_usd")), inv.get(v["date"])
        out.append({"date": v["date"], "value": tot,
                    "portfolio": None if tot is None else tot / start_cash * 100,
                    "spy": None if not (spy and spy0) else spy / spy0 * 100,
                    "baseline": None if base is None else base / start_cash * 100,
                    "invested": None if not i else 100 + i["pct"] * 100,
                    "spy_same": None if not i or i["spy_pct"] is None else 100 + i["spy_pct"] * 100,
                    "invested_tw": tw})
    return out


def invested_tw(v: dict, prev: dict | None, idx: float | None) -> float | None:
    """Time-weighted index of the money in stocks (2026-11-17). The money-weighted "invested" line is (holdings +
    proceeds + income) / everything ever invested, so its change over a few days is not that period's return: the
    proceeds already taken out don't move, and a day's buys and sells change the divisor (on 17 Nov it showed the S&P
    500 at -0.5% on a -1.0% day). Here each day chains (value + income) / (yesterday's value + today's net buys at the
    open). The chart uses it, with SPY's own price, for every range but All."""
    f = lambda r, k: _f(r.get(k)) or 0.0  # noqa: E731
    val = lambda r: f(r, "core_usd") + f(r, "tactical_usd")  # noqa: E731
    cum = lambda r, side: f(r, f"core_{side}") + f(r, f"tactical_{side}")  # noqa: E731
    if prev is None:
        return None
    base = val(prev) + (cum(v, "in") - cum(prev, "in")) - (cum(v, "out") - cum(prev, "out"))
    inc = (f(v, "core_income") + f(v, "tactical_income")) - (f(prev, "core_income") + f(prev, "tactical_income"))
    if base <= 0:
        return idx
    return (idx or 100.0) * (val(v) + inc) / base


def week_change(ser: list[dict]) -> dict | None:
    """Latest point vs the latest one at least 7 days earlier (daily points exist), else the first."""
    if len(ser) < 2 or not ser[-1]["portfolio"]:
        return None
    last = ser[-1]
    cut = (dt.date.fromisoformat(last["date"]) - dt.timedelta(days=7)).isoformat()
    prev = ([p for p in ser[:-1] if p["date"] <= cut] or ser[:1])[-1]
    if not prev["portfolio"]:
        return None
    return {"from": prev["date"], "portfolio": last["portfolio"] / prev["portfolio"] - 1,
            "spy": (last["spy"] / prev["spy"] - 1) if last["spy"] and prev["spy"] else None}


def live_snapshot(tickers: list[str], fetch=None) -> dict:
    """Live prices at build time (owner request 2026-10-09: show how current every price is). Yahoo 1-minute
    bars via prices.live_price; a stock with no price is left out. Display only: the portfolio's official
    value stays on closing prices."""
    from concurrent.futures import ThreadPoolExecutor
    from zoneinfo import ZoneInfo
    if fetch is None:
        from prices import live_price as fetch

    def one(t):
        try:
            q = fetch(t)
        except Exception:  # noqa: BLE001
            return t, None
        uk = dt.datetime.fromisoformat(q["time"]).astimezone(ZoneInfo("Europe/London"))
        return t, {"price": round(q["price"], 4), "date": q["date"], "uk": uk.strftime("%a %H:%M") + " UK"}
    with ThreadPoolExecutor(8) as pool:
        return {t: q for t, q in pool.map(one, dict.fromkeys(tickers)) if q}


def expected_fill(order: dict, cfg: dict) -> str:
    """When a pending order should fill: the first weekday on/after its first eligible open, at that exchange's
    opening time (exchange holidays aren't known here, so it can be a session later)."""
    t = order["request"]["ticker"]
    d = dt.date.fromisoformat(portfolio.first_eligible_open(order, t, cfg))
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    ex = portfolio.Ticker(t).exchange or "US"
    spec = cfg.get("fills", {}).get("open_times", {}).get(ex)
    return f"{d:%a %d %b} open" + (f" ({spec.split()[1]} {ex} time)" if spec else "")


def est_usd(est: dict, ledger: list[dict]) -> float | None:
    """An order's estimated USD value: recorded by portfolio.py, else shares x price x the latest ledger FX rate."""
    if est.get("usd") is not None:
        return float(est["usd"])
    if not est.get("shares") or est.get("price") is None:
        return None
    if est.get("currency") == "USD":
        return est["shares"] * est["price"]
    fx = next((_f(r.get("fx_usd_per_unit")) for r in reversed(ledger)
               if r.get("currency") == est.get("currency") and _f(r.get("fx_usd_per_unit"))), None)
    return est["shares"] * est["price"] * fx if fx else None


CCY_COUNTRY = {"CNY": "China", "HKD": "Hong Kong", "GBP": "United Kingdom", "JPY": "Japan", "KRW": "South Korea",
               "TWD": "Taiwan", "INR": "India", "CAD": "Canada", "CHF": "Switzerland", "AUD": "Australia",
               "BRL": "Brazil", "SGD": "Singapore", "SEK": "Sweden", "DKK": "Denmark", "NOK": "Norway",
               "ZAR": "South Africa", "MXN": "Mexico", "IDR": "Indonesia", "THB": "Thailand", "PLN": "Poland"}
EUR_EXCHANGE = {"AMS": "Netherlands", "BME": "Spain", "EPA": "France", "ETR": "Germany", "BIT": "Italy",
                "EBR": "Belgium", "ELI": "Portugal", "HEL": "Finland", "ISE": "Ireland", "VIE": "Austria"}


def country_of(ticker: str, reporting_ccy: str | None, listed: str) -> str:
    """Where the business is (2026-10-20): the reporting currency's country (NetEase reports in yuan: China, though
    incorporated in the Cayman Islands); euro reporters by their exchange; USD and others by the listed country."""
    if reporting_ccy in CCY_COUNTRY:
        return CCY_COUNTRY[reporting_ccy]
    ex = Ticker(ticker).exchange
    if reporting_ccy == "EUR" and ex in EUR_EXCHANGE:
        return EUR_EXCHANGE[ex]
    return listed or ("United States" if not ex else ex)


def max_drawdown(values: list) -> float:
    """Largest peak-to-trough fall of a value series, in % (0 or negative)."""
    peak, dd = None, 0.0
    for v in values:
        if v is None:
            continue
        peak = v if peak is None else max(peak, v)
        dd = min(dd, v / peak - 1)
    return dd * 100


def add_world(ser: list[dict], closes: dict | None) -> None:
    """Index the global benchmark to 100 at the first valuation date, on each point as `world` (None when unknown)."""
    def on(day):
        ds = [d for d in closes if d <= day]
        return closes[max(ds)] if ds else None
    base = on(ser[0]["date"]) if ser and closes else None
    for p in ser:
        c = on(p["date"]) if base else None
        p["world"] = c / base * 100 if c else None


def funnel(decisions: list[dict], ledger: list[dict], today: str) -> dict:
    """Stocks researched -> rated conviction 4+ -> bought, over the last 7 and 30 days (new-name verdicts only)."""
    out = {}
    for days in (7, 30):
        cut = (dt.date.fromisoformat(today) - dt.timedelta(days=days)).isoformat()
        d = [r for r in decisions if r["date"] > cut and r.get("decision") in ("BUY", "AVOID")]
        out[str(days)] = {"researched": len({r["ticker"] for r in d}),
                          "conv4": len({r["ticker"] for r in d if int(r.get("conviction") or 0) >= 4}),
                          "bought": len({r["ticker"] for r in ledger if r["date"] > cut and r.get("side") == "BUY"})}
    return out


def attention(pending: list[dict], holdings: list[dict], entry_hits: list[dict], watch: list[dict], queue: list,
              min_buy: int) -> list[dict]:
    """The short list of things worth a look today, each with the tab that shows it."""
    out = []
    for o in pending:
        if o["action"] != "HOLD":
            out.append({"page": "pipeline", "text": f"Order pending: {o['action']} {o['ticker']} ({o.get('fills') or 'next open'})"})
    for h in holdings:
        lc = h.get("latest_conviction")
        if lc is not None and lc < min_buy and lc < (h.get("conviction") or 0):
            out.append({"page": "holdings", "text": f"{h['ticker']}: research of {h.get('latest_eval_date')} rates it conviction {lc} "
                                                    f"(held as {h['conviction']}); not applied to the position yet"})
    if entry_hits:
        out.append({"page": "pipeline", "text": "Entry price hit, waiting for re-research: " + ", ".join(h["ticker"] for h in entry_hits)})
    skipped = [r["ticker"] for r in watch if r.get("skipped_hit_date")]
    if skipped:
        out.append({"page": "pipeline", "text": "Hit skipped (too far from a 4 at any price): " + ", ".join(skipped)})
    near = [r["ticker"] for r in watch if not r.get("hit_date") and not r.get("skipped_hit_date")
            and (_f(r.get("pct_to_entry")) is not None and _f(r.get("pct_to_entry")) >= -2)]
    if near:
        out.append({"page": "pipeline", "text": f"Within 2% of entry price: {', '.join(near[:8])}" + (f" and {len(near) - 8} more" if len(near) > 8 else "")})
    if queue:
        out.append({"page": "pipeline", "text": f"{len(queue)} conviction-4 buy(s) waiting for cash in the funding queue"})
    return out


JOBS = (("Daily prices and fills (21:30)", "fills-"), ("Weekly run (Saturday)", "weekly-local-"),
        ("Intraday entry check", "entry-intraday-"), ("Live dashboard", "live-dashboard-"))


def health(logs: Path, today: str) -> dict:
    """When each scheduled job last ran, and the problem lines (`!!`) its logs wrote in the last 7 days."""
    cut = (dt.date.fromisoformat(today) - dt.timedelta(days=7)).isoformat()
    jobs, problems = [], []
    for label, prefix in JOBS:
        files = sorted(f for f in logs.glob(prefix + "20??-??-??.log"))
        jobs.append({"job": label, "last": files[-1].stem[-10:] if files else None,
                     "ok": bool(files) and "!!" not in files[-1].read_text(errors="replace")})
        for f in files:
            if f.stem[-10:] >= cut:
                problems += [{"date": f.stem[-10:], "job": label, "line": ln.strip()[:200]}
                             for ln in f.read_text(errors="replace").splitlines() if "!!" in ln]
    return {"jobs": jobs, "problems": problems[-20:][::-1]}


def regime_now() -> dict | None:
    """The weekly regime with the daily dip check applied (2026-10-20: the tile showed the weekly file's dip only).
    Dated for the next session, as the 21:30 run writes its dip check."""
    import regime as R
    asof = (dt.date.today() + dt.timedelta(days=1)).isoformat()
    doc = R.latest(asof)
    if not doc:
        return None
    dip = R.latest_dip(asof, doc["asof"])
    if dip:
        doc = dict(doc, reserve_pct=round(doc["base_reserve_pct"] * dip["multiplier"], 2),
                   dip={"drawdown_pct": dip["drawdown_pct"], "multiplier": dip["multiplier"], "asof": dip["asof"]})
    return doc


def build_data(live: bool = True) -> dict:
    cfg = load_config()
    port = ROOT / "portfolio"
    near_pct = float(cfg["entry"].get("near_pct", 10))
    state = json.loads((port / "state.json").read_text()) if (port / "state.json").exists() else {"holdings": {}, "cash_usd": 0}
    start = float(cfg["portfolio"]["starting_cash_usd"])
    uni = _csv(ROOT / "universe" / "universe.csv")
    names = {r["ticker"]: r["name"] for r in uni}
    listed = {r["ticker"]: r.get("country", "") for r in uni}
    hold = []
    recv = sum(r["net_usd"] for r in state.get("receivables", []))  # dividends past the ex-date, not yet paid
    total = state.get("cash_usd", 0.0) + recv + sum(h.get("market_value_usd", 0.0) for h in state["holdings"].values())
    for t, h in sorted(state["holdings"].items(), key=lambda kv: -kv[1].get("market_value_usd", 0)):
        mv, cb = h.get("market_value_usd", 0.0), h.get("cost_basis_usd", 0.0)
        ep, lp = _f(h.get("entry_price")), _f(h.get("last_close"))
        plan = ""
        if h["type"] == "TACTICAL" and h.get("exit_plan"):
            ep_ = h["exit_plan"]
            plan = f"target {ep_['target']} · stop {ep_['stop']} · until {ep_['time_limit']}"
        elif h.get("triggers"):
            plan = f"{len(h['triggers'])} thesis triggers"
        hold.append({"ticker": t, "name": names.get(t, ""), "type": h["type"], "conviction": h.get("conviction"),
                     "sector": h.get("sector") or "", "entry_date": h.get("entry_date", ""), "currency": h.get("currency", ""),
                     "entry_price": ep, "last_price": lp, "last_date": h.get("last_close_date", ""),
                     "change_pct": (lp / ep - 1) * 100 if ep and lp else None,
                     "value": mv, "weight": mv / total * 100 if total else 0, "pl": mv - cb if cb else None,
                     "plan": plan, "thesis": h.get("thesis", ""),
                     "prev_close": _f(h.get("prev_close")), "prev_date": h.get("prev_close_date", "")})
    all_watch = _csv(port / "entry_watch.csv")
    watch_rows = sorted(all_watch, key=lambda r: -(_f(r.get("pct_to_entry")) or -999))[:40]
    snap = live_snapshot([h["ticker"] for h in hold] + [r["ticker"] for r in watch_rows] + ["SPY"]) if live else {}
    if live:  # holdings re-priced before prev_close was recorded (2026-10-20): read it from the daily history once
        from fetch_data import Fetcher
        mkt = portfolio.Market(Fetcher(cfg), dt.date.today().isoformat(), cfg, portfolio.price_provider(cfg))
        for h in hold:  # the portfolio's own price chain: Yahoo, else stockanalysis.com
            if h["prev_close"] is None and h["last_date"]:
                try:
                    rows = [r for r in mkt.history(h["ticker"])["all_rows"] if r["date"] < h["last_date"] and r.get("close")]
                    if rows:
                        h["prev_close"], h["prev_date"] = rows[-1]["close"], rows[-1]["date"]
                except Exception:  # noqa: BLE001  display only
                    pass
    for h in hold:  # the latest session's change (close vs the close before; bought that day: vs the fill)
        lp, pc = h["last_price"], h["prev_close"]
        if h["entry_date"] and h["entry_date"] == h["last_date"] and h["entry_price"]:
            pc, h["prev_date"] = h["entry_price"], "bought at the open"
        h["day_pct"] = (lp / pc - 1) * 100 if lp and pc else None
        h["day_usd"] = h["value"] * (1 - pc / lp) if lp and pc else None
    live_total = state.get("cash_usd", 0.0) + recv
    for h in hold:
        q, lc = snap.get(h["ticker"]), h["last_price"]
        h["live"] = q
        if q and lc:
            h["live_change_pct"] = (q["price"] / h["entry_price"] - 1) * 100 if h["entry_price"] else None
            h["live_value"] = h["value"] * q["price"] / lc
            if q["date"] > (h["last_date"] or ""):  # a session after the last close is trading: today's move
                h["live_day_pct"] = (q["price"] / lc - 1) * 100
                h["live_day_usd"] = h["live_value"] - h["value"]
        live_total += h.get("live_value", h["value"])
    sectors: dict[str, float] = {}
    for h in hold:
        sectors[h["sector"] or "Unknown"] = sectors.get(h["sector"] or "Unknown", 0) + h["weight"]
    countries: dict[str, float] = {}  # where the business is: the reporting currency's country, else the listing
    for h in hold:
        c = country_of(h["ticker"], state["holdings"][h["ticker"]].get("reporting_currency"), listed.get(h["ticker"], ""))
        h["country"] = c
        countries[c] = countries.get(c, 0) + h["weight"]
    vals = _csv(port / "valuations.csv")
    ser = series(vals, start)
    wc = None
    if live:  # the global benchmark (VT): reporting only
        import weekly_report
        wc = weekly_report.world_closes()
    add_world(ser, wc)
    all_ledger = _csv(port / "ledger.csv")
    ledger = all_ledger[-25:][::-1]
    decisions = _csv(port / "decisions.csv")
    today = dt.date.today().isoformat()
    last_dec = {d["ticker"]: d for d in decisions}
    for h in hold:  # the latest research next to what is held
        d = last_dec.get(h["ticker"])
        h["latest_conviction"] = int(d["conviction"]) if d and d.get("conviction") else None
        h["latest_eval_date"], h["latest_decision"] = (d["date"], d["decision"]) if d else (None, None)
        h["days_held"] = (dt.date.today() - dt.date.fromisoformat(h["entry_date"])).days if h["entry_date"] else None
        vfiles = sorted((ROOT / "research" / Ticker(h["ticker"]).slug).glob("20??-??-??-valuation.json"))
        v = json.loads(vfiles[-1].read_text()) if vfiles else {}
        base = (v.get("fair_value") or {}).get("base")
        h["fv_upside"] = (base / h["last_price"] - 1) * 100 if base and h["last_price"] and v.get("quote_currency") == h["currency"] else None
        # the scorecard ignores a fair value whose methods disagree widely; the page must not show it as a plain number
        h["fv_unreliable"] = bool(base) and not __import__("valuation").is_reliable(v)
    cal = ROOT / "reports" / "calibration" / "latest.json"
    cal = json.loads(cal.read_text()) if cal.exists() else {}
    screens = sorted((ROOT / "reports" / "screen").glob("20??-??-??.json"))
    screen = json.loads(screens[-1].read_text()) if screens else {}

    def latest(kind):
        files = sorted((ROOT / "reports" / kind).glob("20??-??-??.json"))
        return json.loads(files[-1].read_text()) if files else None
    risk, attr = latest("risk"), latest("attribution")
    dip = latest("dip-radar")
    fq = []
    for e in state.get("funding_queue") or []:  # 2026-10-19: conviction-4 ideas waiting for room
        c = e.get("last_close") or e.get("decision_price")
        fv = e.get("fair_value_base")
        h = state["holdings"].get(e["ticker"]) or {}
        fq.append({"ticker": e["ticker"], "name": names.get(e["ticker"], ""), "stage": e.get("stage", "full"),
                   "conviction": e["request"].get("conviction"), "added": e["added"], "expires": e["expires"],
                   "decision_price": e["decision_price"], "close": c, "ccy": e.get("currency", ""),
                   "upside": (lambda v: (v / c - 1) * 100 if v and c else None)(
                       __import__("funding_queue").value_and_basis(e["ticker"], None, fv)[0]),
                   "weight": h.get("market_value_usd", 0) / total * 100 if h and total else None,
                   "target": h.get("target_pct"), "ordered": e["ticker"] in {o["request"]["ticker"] for o in state.get("pending", [])},
                   "evaluation": next((str(p_.relative_to(ROOT)) for p_ in sorted((ROOT / "research" / Ticker(e["ticker"]).slug).glob("20??-??-??-evaluation.md"))[-1:]), "")})
    fq.sort(key=lambda x: (x["stage"] != "topup", -(x["upside"] or -999)))
    from decision_log import HORIZONS
    hits = {}
    for h in HORIZONS:
        done = [d for d in decisions if d.get(f"hit_{h}m") not in ("", None)]
        hits[f"{h}m"] = {"n": len(done), "hits": sum(int(d[f"hit_{h}m"]) for d in done)}
        for side, own in (("buy", True), ("avoid", False)):  # one blended rate is mostly AVOIDs in a rising market
            part = [d for d in done if (d["decision"] in ("BUY", "ADD", "HOLD")) == own]
            hits[f"{h}m"][side] = {"n": len(part), "hits": sum(int(d[f"hit_{h}m"]) for d in part)}
    exits = _csv(port / "exits.csv")[::-1]  # scripts/exit_log.py: how sold and trimmed stocks did afterwards
    newest = decisions[::-1]
    matured = {id(d) for d in [d for d in newest if d.get("excess_1m") not in ("", None)][:300]}
    shown = [d for i, d in enumerate(newest) if i < 60 or d["decision"] != "AVOID" or id(d) in matured]
    last = ser[-1] if ser else None
    week = week_change(ser)
    live_pt = None  # the chart's live point (1D range): whole portfolio and SPY at live prices
    spy_live = snap.get("SPY")
    if snap and last and last["portfolio"] is not None and vals:
        lsc = _f(vals[-1].get("spy_close"))
        live_pt = {"date": dt.datetime.now().isoformat(timespec="minutes"), "live": True, "value": live_total,
                   "portfolio": live_total / start * 100,
                   "spy": last["spy"] * spy_live["price"] / lsc if spy_live and lsc and last["spy"] else None,
                   "baseline": None, "invested": None, "spy_same": None}
    return {
        "generated": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "repo": repo_url(),
        "total": total, "cash": state.get("cash_usd", 0.0), "start": start, "receivable": recv,
        "close_date": max((h["last_date"] for h in hold), default=""),
        "live_total": live_total if snap else None, "live_at": dt.datetime.now().strftime("%a %H:%M") + " UK" if snap else None,
        "inception": state.get("inception_date"),
        "since": None if not last or last["portfolio"] is None else last["portfolio"] / 100 - 1,
        "since_spy": None if not last or last["spy"] is None else last["spy"] / 100 - 1,
        "invested": portfolio.invested_return(vals),
        "since_world": None if not last or last.get("world") is None else last["world"] / 100 - 1,
        "max_drawdown": max_drawdown([p.get("value") for p in ser]),
        "min_buy": int(cfg["core"].get("min_buy_conviction", 4)),
        "attention": attention([{"action": o["request"]["action"], "ticker": o["request"]["ticker"], "fills": expected_fill(o, cfg)}
                                for o in state.get("pending", [])], hold,
                               [h for h in state.get("entry_hits") or []  # still unresearched: its watch row keeps the hit date
                                if h["ticker"] in {r["ticker"] for r in all_watch if r.get("hit_date")}], all_watch,
                               state.get("funding_queue") or [], int(cfg["core"].get("min_buy_conviction", 4))),
        "funnel": funnel(decisions, all_ledger, today),
        "scoreboard": {"asof": cal.get("asof"), "by_conviction": cal.get("by_conviction") or {}, "by_points": cal.get("by_points") or {}},
        "health": health(ROOT / "logs", today),
        "trades": [{"date": r["date"], "side": r["side"], "ticker": r["ticker"]} for r in all_ledger],
        "n_watch": len(all_watch),
        "week": week, "series": ser, "live_point": live_pt, "holdings": hold, "interest": state.get("cash_interest"),
        "regime": regime_now(),
        "cash_mode": cfg.get("cash_strategy", {}).get("mode", "regime"),
        "cash_floor_pct": float(cfg["portfolio"]["min_cash_pct"]),
        "sectors": sorted(([k, v] for k, v in sectors.items()), key=lambda kv: -kv[1]),
        "countries": sorted(([k, v] for k, v in countries.items()), key=lambda kv: -kv[1]),
        "ledger": [{k: r.get(k, "") for k in ("date", "ticker", "type", "side", "shares", "fill_price", "currency",
                                              "fill_close_date", "gross_usd", "costs_usd", "reason")} for r in ledger],
        "decisions": [{k: d.get(k, "") for k in ("date", "ticker", "type", "decision", "conviction", "price", "currency",
                                                 "excess_1m", "excess_3m", "evaluation", "price_date")}
                      | {"live": "price: live" in (d.get("note") or "")} for d in shown],
        "hits": hits, "n_decisions": len(decisions),
        "exits": [{k: e.get(k, "") for k in ("date", "ticker", "decision", "shares", "kind", "replaced_by", "usd", "since_date",
                                             "since_ret", "since_excess", "kept_usd", "vs_replacement_since",
                                             "excess_1m", "hit_1m", "excess_3m")} for e in exits],
        "watch": sorted(({"ticker": r["ticker"], "close": r.get("last_close"), "entry": r["entry_price"],
                          "close_date": r.get("last_close_date", ""), "live": snap.get(r["ticker"]),
                          "ccy": r.get("currency", ""), "to_entry": _f(r.get("pct_to_entry")), "source": r["source"],
                          "conviction": r.get("conviction"), "hit": r.get("hit_date", ""),
                          "near_since": r.get("near_since", ""), "evaluation": r.get("evaluation", ""),
                          "blocked": entry_watch.blocked(r, cfg["entry"].get("skip_hit_points_short")),
                          "skipped": r.get("skipped_hit_date", ""),
                          "why": entry_watch.why_not_yet(r) if entry_watch.is_near(r, near_pct) else ""}
                         for r in all_watch),  # every name; only the 40 closest carry a live price
                        key=lambda r: -(r["to_entry"] if r["to_entry"] is not None else -999)),
        "near_pct": near_pct,
        "pending": [{"id": o["id"], "placed": o["placed"], "action": o["request"]["action"],
                     "ticker": o["request"]["ticker"], "type": o["request"]["position_type"],
                     "conviction": o["request"].get("conviction"), "est": o.get("estimate", {}),
                     "fills": expected_fill(o, cfg), "replaces": o["request"].get("replaces"),
                     "est_usd": est_usd(o.get("estimate", {}), all_ledger)}
                    for o in state.get("pending", [])],
        "screen": {"asof": screen.get("asof"), "screened": screen.get("screened"), "picks": screen.get("picks", []),
                   "illiquid": len(screen.get("illiquid") or [])},
        "risk": risk and {"asof": risk["asof"], "sigma_p": risk.get("sigma_p_pct"),
                          "corr_flag": risk.get("corr_flag"), "corr_pairs": risk.get("corr_pairs"),
                          "rows": sorted(({k: r.get(k) for k in ("ticker", "weight_pct", "target_pct", "vol_pct",
                                                                  "mcr_pct", "risk_share_pct", "flag")}
                                          for r in risk["rows"]), key=lambda r: -(r["risk_share_pct"] or 0))},
        "attribution": attr if attr and not attr.get("note") else None,
        "funding_queue": fq,
        "dip": dip and {"asof": dip["asof"], "watched": len(dip["assessed"]), "hits": [h["ticker"] for h in dip["hits"]],
                        "no_data": len(dip.get("failed") or []),
                        "rows": sorted(({k: a.get(k) for k in ("ticker", "kind", "z", "ret_pct", "spy_pct", "specific_pct",
                                                                 "sessions", "last_research", "vs_base_pct", "signal", "why_not",
                                                                 "close", "close_date", "currency")}
                                        for a in dip["assessed"] if a.get("signal") or (a.get("z") is not None and a["z"] <= -1.0)),
                                       key=lambda a: (not a["signal"], a["z"] if a["z"] is not None else 0))[:15]},
    }


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Paper Portfolio</title>
<style>
:root{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;
--axis:#c3c2b7;--ring:rgba(11,11,11,.10);--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--up:#006300;--down:#d03b3b;--wash:rgba(42,120,214,.10)}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])){color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#fff;
--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);--s1:#3987e5;--s2:#d95926;--s3:#199e70;--up:#0ca30c;--down:#e66767;--wash:rgba(57,135,229,.12)}}
:root[data-theme="dark"]{color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;
--ring:rgba(255,255,255,.10);--s1:#3987e5;--s2:#d95926;--s3:#199e70;--up:#0ca30c;--down:#e66767;--wash:rgba(57,135,229,.12)}
*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--ink);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1120px;margin:0 auto;padding:0 16px 48px}
h1{font-size:20px;margin:0}h2{font-size:16px;margin:0 0 4px}.sub{color:var(--ink2);font-size:13px}.muted{color:var(--muted)}
.card{background:var(--surface);border:1px solid var(--ring);border-radius:12px;padding:16px;margin-top:16px}
.hero{font-size:48px;font-weight:600;line-height:1.1;margin:8px 0 2px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-top:12px}
.tile .l{color:var(--ink2);font-size:13px}.tile .v{font-size:22px;font-weight:600}.tile .d{font-size:13px}
.up{color:var(--up)}.down{color:var(--down)}
.grid2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}@media (max-width:760px){.grid2{grid-template-columns:minmax(0,1fr)}}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--ink2);margin:6px 0}
.key{display:inline-block;width:14px;height:2px;vertical-align:middle;margin-right:6px;border-radius:1px}
.sw{display:inline-block;width:10px;height:10px;border-radius:2px;vertical-align:-1px;margin-right:6px}
svg{display:block;width:100%;height:auto;overflow:visible}svg text{fill:var(--muted);font-size:12px;font-family:inherit}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--grid);white-space:nowrap}
th{color:var(--ink2);font-weight:600}td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}td.w{white-space:normal;min-width:220px;color:var(--ink2)}
.tip{position:fixed;pointer-events:none;background:var(--surface);border:1px solid var(--ring);border-radius:8px;padding:8px 10px;font-size:13px;
box-shadow:0 4px 16px rgba(0,0,0,.12);display:none;z-index:10}.tip b{font-weight:600}.tip .r{display:flex;align-items:center;gap:6px}
.empty{color:var(--ink2);padding:24px 0;text-align:center}details summary{cursor:pointer;color:var(--ink2);font-size:13px;margin-top:8px}
a{color:var(--s1)}.pill{display:inline-block;padding:1px 8px;border-radius:999px;border:1px solid var(--ring);font-size:12px;color:var(--ink2)}
.tabs{display:flex;gap:4px;margin:8px 0;border-bottom:1px solid var(--grid)}
.tab2{background:none;border:0;border-bottom:2px solid transparent;color:var(--ink2);padding:6px 10px;margin-bottom:-1px;cursor:pointer;font:inherit;font-size:14px}
.tab2[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--s1)}
.tab{background:none;border:0;border-bottom:2px solid transparent;color:var(--ink2);padding:6px 10px;margin-bottom:-1px;cursor:pointer;font:inherit;font-size:14px}
.tab[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--s1);font-weight:600}
.ranges{display:flex;gap:4px;flex-wrap:wrap;margin:4px 0 8px}
.rng{background:none;border:1px solid var(--ring);border-radius:999px;color:var(--ink2);padding:3px 12px;cursor:pointer;font:inherit;font-size:13px}
.rng[aria-pressed="true"]{background:var(--ink);color:var(--page);border-color:var(--ink)}
.chg{display:inline-block;min-width:76px;text-align:right;padding:2px 8px;border-radius:6px;font-weight:600;font-variant-numeric:tabular-nums}
.chg.up{color:var(--up);background:color-mix(in srgb,var(--up) 13%,transparent)}.chg.down{color:var(--down);background:color-mix(in srgb,var(--down) 13%,transparent)}
.chg.flat{color:var(--ink2);background:color-mix(in srgb,var(--ink2) 10%,transparent)}.chg small{font-weight:400;opacity:.8;margin-left:4px}
.mandate p{margin:6px 0 0;max-width:80ch}
.steps{list-style:none;margin:12px 0 8px;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}
.steps li{border:1px solid var(--ring);border-radius:8px;padding:8px 10px;font-size:13px;color:var(--ink2);background:var(--page)}
.steps li b{display:block;color:var(--ink);font-size:14px;margin-bottom:2px}
@media (max-width:900px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:520px){.steps{grid-template-columns:1fr}}
.toggle{background:none;border:1px solid var(--ring);border-radius:8px;color:var(--ink2);padding:4px 10px;cursor:pointer;font:inherit;font-size:13px}
.top{padding:16px 0 0}
.pages{display:flex;gap:2px;overflow-x:auto;margin-top:8px;position:sticky;top:0;z-index:5;background:var(--page);border-bottom:1px solid var(--grid)}
.pg{background:none;border:0;border-bottom:2px solid transparent;color:var(--ink2);padding:8px 14px;cursor:pointer;font:inherit;font-size:14px;white-space:nowrap}
.pg[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--ink);font-weight:600}.pg .ct{margin-left:6px;font-size:12px;color:var(--muted);font-weight:400}
.page{display:none}.page.on{display:block}
td.w{white-space:nowrap;max-width:360px;min-width:0;overflow:hidden;text-overflow:ellipsis}tr.open td.w{white-space:normal}
tr.x{cursor:pointer}tr.x:hover td{background:color-mix(in srgb,var(--ink) 3%,transparent)}
.more{margin-top:10px}th.so{cursor:pointer;user-select:none}th.so:hover{color:var(--ink)}
th[aria-sort="ascending"]::after{content:" ▲";font-size:10px}th[aria-sort="descending"]::after{content:" ▼";font-size:10px}
.chip{background:none;border:1px solid var(--ring);border-radius:999px;color:var(--ink2);padding:3px 12px;cursor:pointer;font:inherit;font-size:13px}
.chip[aria-pressed="true"]{background:var(--ink);color:var(--page);border-color:var(--ink)}
.filter{width:100%;max-width:320px;margin:8px 0;padding:6px 10px;border:1px solid var(--ring);border-radius:8px;background:var(--page);color:var(--ink);font:inherit;font-size:13px}
.att{list-style:none;margin:8px 0 0;padding:0}.att li{padding:7px 0;border-bottom:1px solid var(--grid);font-size:14px;cursor:pointer;display:flex;gap:10px;align-items:baseline}
.att li:last-child{border-bottom:0}.att li:hover{color:var(--s1)}.att .go{margin-left:auto;color:var(--muted);font-size:12px;white-space:nowrap}
.lg{background:none;border:0;color:var(--ink2);font:inherit;font-size:13px;cursor:pointer;padding:0}.lg[aria-pressed="false"]{opacity:.45;text-decoration:line-through}
.flag{display:inline-block;padding:0 6px;border-radius:6px;font-size:12px;font-weight:600;color:var(--down);background:color-mix(in srgb,var(--down) 13%,transparent)}
.okd{color:var(--up)}.bad{color:var(--down)}
.daily p{margin:8px 0 0;font-size:14px;max-width:90ch}.daily ul{margin:4px 0 0;padding-left:18px;font-size:14px}
.daily summary{cursor:pointer;color:var(--muted);font-size:13px;margin-top:10px}
td.nm{max-width:180px;overflow:hidden;text-overflow:ellipsis}
</style></head><body><main>
<header class="top"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap"><div><h1>Paper Portfolio</h1><div class="sub">Paper trading only, not investment advice · updated <span id="gen"></span> · <span id="counts"></span></div></div>
<button class="toggle" id="theme" type="button">Toggle dark mode</button></div>
</header><nav class="pages" role="tablist" aria-label="Sections" id="pages"></nav>
<div class="page" data-page="overview">
__INTRO__
<section class="card" aria-label="Summary"><div class="sub">Portfolio value</div><div class="hero" id="hero"></div><div class="sub" id="heroSub"></div>
<div class="tiles" id="tiles"></div></section>
<section class="card" id="attCard"><h2>Needs attention</h2><ul class="att" id="att"></ul></section>
__DAILY__
<section class="card"><h2>Return vs the S&amp;P 500</h2>
<div class="tabs" role="tablist"><button type="button" role="tab" class="tab" data-tab="invested">Invested money</button><button type="button" role="tab" class="tab" data-tab="whole">Whole portfolio</button></div>
<div class="ranges" role="group" aria-label="Chart period" id="ranges"></div>
<div class="sub" id="lineSub"></div>
<div class="legend" id="lineLegend"></div><div id="line"></div>
<details><summary>Show as a table</summary><div class="tw"><table id="lineTable"></table></div></details></section>
<div class="grid2"><section class="card"><h2>Holdings by weight</h2><div class="legend"><span><span class="sw" style="background:var(--s1)"></span>Core</span>
<span><span class="sw" style="background:var(--s2)"></span>Tactical</span></div><div id="bars"></div></section>
<section class="card"><h2>Sectors &amp; countries</h2><div class="tabs" role="tablist"><button type="button" role="tab" class="tab2" data-mix="sectors">Sectors</button><button type="button" role="tab" class="tab2" data-mix="countries">Countries</button></div>
<div class="sub" id="mixSub"></div><div id="sectors"></div></section></div>
</div>
<div class="page" data-page="holdings">
<section class="card"><h2>Holdings</h2><div class="sub">Latest research = the conviction of the most recent evaluation; when it is below the held conviction the position is resized at the next open. A “?” after a fair-value figure means the valuation methods disagree widely, so the scorecard ignores it. Click a row for its plan.</div><div class="tw"><table id="holdings"></table></div></section>
<div class="grid2"><section class="card"><h2>Risk</h2><div class="sub" id="riskSub"></div>
<div class="legend"><span><span class="sw" style="background:var(--s1)"></span>Share of portfolio risk</span><span><span class="sw" style="background:var(--axis)"></span>Share of invested money</span></div>
<div id="risk"></div><div class="sub" id="corrPairs"></div><details><summary>Show as a table</summary><div class="tw"><table id="riskTable"></table></div></details></section>
<section class="card"><h2>Where the excess return came from</h2><div class="sub" id="attrSub"></div><div class="tiles" id="attrTiles"></div>
<div class="tw" style="margin-top:12px"><table id="attrTable"></table></div></section></div>
</div>
<div class="page" data-page="pipeline">
<section class="card"><h2>Pending orders</h2><div class="sub">Decided trades fill at the next opening price of their own market; every rule is checked again at that price. The 21:30 UK job records the fills.</div><div class="tw"><table id="pending"></table></div></section>
<section class="card"><h2>Funding queue</h2><div class="sub">Conviction-4 buys waiting for cash, best first. The portfolio runs up to 98.5% invested, so a buy waits only when it doesn't fit. A position that started small (a starter) is topped up first, once a week; the others are bought when cash frees up (a trim, a sale or a swap), or swapped in for a weaker holding by the weekly review. Each drops out after 30 days or if the price runs 10% above where we decided.</div><div class="tw"><table id="fqueue"></table></div></section>
<section class="card"><h2>Watchlist: entry prices</h2><div class="sub" id="watchSub"></div><div class="tw"><table id="watch"></table></div></section>
<section class="card"><h2>Dip radar</h2><div class="sub" id="dipSub"></div><div class="tw"><table id="dips"></table></div></section>
<section class="card"><h2>Latest screen</h2><div class="sub" id="screenSub"></div><div id="picks" style="margin-top:8px"></div></section>
</div>
<div class="page" data-page="activity">
<section class="card"><h2>Research funnel</h2><div class="sub">How many stocks were researched, how many reached the buy bar, and how many were bought.</div><div class="tiles" id="funnel"></div></section>
<section class="card"><h2>Recent trades</h2><div class="tw"><table id="trades"></table></div></section>
<section class="card"><h2>Decisions &amp; hit rates</h2><div class="sub">A decision is a hit when it was right about direction against the S&amp;P 500: a buy or hold that beat it, an avoid or trim that lagged it. Avoids are counted apart because there are far more of them. The table lists the latest decisions and those with a result; click a column to sort.</div>
<div class="tiles" id="hits"></div><div class="tw" style="margin-top:12px"><table id="decisions"></table></div></section>
<section class="card"><h2>After we sold</h2><div class="sub">Every trim and sale, followed from its fill price. A trim or sale was right when the stock then lagged the S&amp;P 500. "Selling saved" is what the sold shares have lost since (+) or gained (−); for a swap, the last column is the stock bought minus the one sold.</div>
<div class="tiles" id="exitTiles"></div><div class="tw" style="margin-top:12px"><table id="exits"></table></div></section>
<section class="card"><h2>Conviction scoreboard</h2><div class="sub" id="scoreSub"></div><div class="tw"><table id="score"></table></div>
<div class="sub" style="margin-top:12px" id="pointsSub"></div><div class="tw"><table id="points"></table></div></section>
</div>
<div class="page" data-page="process">
__MANDATE__
<section class="card"><h2>System health</h2><div class="sub">When each scheduled job last ran, and any problem lines its logs wrote in the last 7 days.</div>
<div class="tw"><table id="jobs"></table></div><div class="tw" style="margin-top:12px"><table id="problems"></table></div></section>
</div>
<p class="sub muted">All prices and financials from stockanalysis.com. Generated by scripts/dashboard.py. <span id="repo"></span></p>
</main><div class="tip" id="tip" role="tooltip"></div>
<script type="application/json" id="data">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const $=id=>document.getElementById(id),el=(t,a={},...k)=>{const e=document.createElement(t);for(const[x,y]of Object.entries(a))x==='class'?e.className=y:e.setAttribute(x,y);k.forEach(c=>e.append(c));return e;};
const NS='http://www.w3.org/2000/svg',sv=(t,a={})=>{const e=document.createElementNS(NS,t);for(const[x,y]of Object.entries(a))e.setAttribute(x,y);return e;};
const usd=(x,d=0)=>x==null||isNaN(x)?'n/a':(x<0?'-':'')+'$'+Math.abs(x).toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const pct=(x,d=2)=>x==null?'n/a':(x>=0?'+':'')+x.toFixed(d)+'%';
const cls=x=>x==null?'':x>=0?'up':'down';
const px=x=>x==null||x===''||isNaN(+x)?'':(+x).toLocaleString('en-US',{maximumFractionDigits:Math.abs(+x)<10?4:2});  // share prices
try{const t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}catch(e){}
$('theme').onclick=()=>{const dark=matchMedia('(prefers-color-scheme: dark)').matches;const cur=document.documentElement.dataset.theme||(dark?'dark':'light');
const n=cur==='dark'?'light':'dark';document.documentElement.dataset.theme=n;try{localStorage.setItem('theme',n)}catch(e){}};
$('gen').textContent=D.generated;
$('counts').textContent=`${D.holdings.length} holdings · ${D.n_decisions} decisions logged`;
const PAGES=[['overview','Overview'],['holdings','Holdings',D.holdings.length],['pipeline','Pipeline',(D.pending||[]).length+(D.funding_queue||[]).length||''],['activity','Activity'],['process','Process']];
let PAGE='overview',drawn=false;
function setPage(n,push){PAGE=PAGES.some(([k])=>k===n)?n:'overview';
 document.querySelectorAll('.page').forEach(d=>d.classList.toggle('on',d.dataset.page===PAGE));
 document.querySelectorAll('.pg').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.p===PAGE)));
 if(push){try{history.replaceState(null,'','#'+PAGE)}catch(e){}scrollTo(0,0);}
 if(drawn)drawAll();}
PAGES.forEach(([k,l,c])=>{const b=el('button',{type:'button',role:'tab',class:'pg','data-p':k},l);if(c)b.append(el('span',{class:'ct'},String(c)));b.onclick=()=>setPage(k,true);$('pages').append(b);});
addEventListener('hashchange',()=>setPage(location.hash.slice(1)));
$('hero').textContent=usd(D.total);
const I=D.invested;
$('heroSub').textContent=(D.inception?`At the ${D.close_date} close`:'No trades yet: the portfolio is all cash')
 +(D.live_total!=null&&D.holdings.some(h=>h.live_day_pct!=null)?` · live estimate ${usd(D.live_total)} (${pct((D.live_total/D.total-1)*100,2)} since the close) at ${D.live_at}`:'');
const tile=(l,v,d,c)=>el('div',{class:'tile'},el('div',{class:'l'},l),el('div',{class:'v'},v),d?el('div',{class:'d '+(c||'')},d):'');
$('tiles').append(
 I?tile('Return on invested money',pct(I.pct*100),`${usd(I.gain)} on ${usd(I.invested)} invested`+(I.spy_pct==null?'':` · S&P 500 from day one ${pct(I.spy_pct*100)}`),cls(I.spy_pct==null?null:I.pct-I.spy_pct))
  :tile('Return on invested money','–','starts with the first trade'),
 D.inception?tile('Whole portfolio (incl. cash)',D.since==null?'n/a':pct(D.since*100),(D.since_spy==null?'':'S&P 500 '+pct(D.since_spy*100))+(D.since_world==null?'':' · global (VT) '+pct(D.since_world*100)),cls(D.since==null||D.since_spy==null?null:D.since-D.since_spy))
  :tile('Whole portfolio (incl. cash)','–','starts with the first trade'),
 (()=>{const s=D.series,a=s.length>1?s[s.length-2]:null,b=s.length?s[s.length-1]:null;
  if(D.live_total!=null&&D.total&&D.holdings.some(h=>h.live_day_pct!=null))return tile('Last 24h',pct((D.live_total/D.total-1)*100),`live ${D.live_at} · ${(D.live_total>=D.total?'+':'−')+usd(Math.abs(D.live_total-D.total))} vs the ${D.close_date} close`,cls(D.live_total-D.total));
  if(a&&b&&a.value&&b.value)return tile('Last 24h',pct((b.value/a.value-1)*100),`${b.date} vs ${a.date} · ${(b.value>=a.value?'+':'−')+usd(Math.abs(b.value-a.value))}`,cls(b.value-a.value));
  return tile('Latest day','n/a','');})(),
 tile('This week',D.week?pct(D.week.portfolio*100):'n/a',D.week&&D.week.spy!=null?'S&P 500 '+pct(D.week.spy*100):'',D.week&&D.week.spy!=null?cls(D.week.portfolio-D.week.spy):''),
 tile('Cash',usd(D.cash),(D.total?(D.cash/D.total*100).toFixed(1)+'% of portfolio':'')+(D.cash_mode==='residual'?` · ${D.cash_floor_pct}% floor, otherwise fully invested`:(D.regime?` · reserve ${D.regime.reserve_pct}%`:''))+(D.receivable?` · ${usd(D.receivable,2)} dividends due`:'')),
 tile('Largest fall from a peak',D.max_drawdown==null?'n/a':D.max_drawdown.toFixed(1)+'%','whole portfolio, daily closes since inception')
);
{const A=D.attention||[],names=Object.fromEntries(PAGES.map(([k,l])=>[k,l]));
 if(!A.length)$('att').append(el('li',{style:'cursor:default'},el('span',{class:'muted'},'Nothing waiting: no pending orders, hits or downgrades.')));
 A.forEach(a=>{const li=el('li',{tabindex:0,role:'link'},el('span',{},a.text),el('span',{class:'go'},names[a.page]+' →'));li.onclick=()=>setPage(a.page,true);li.onkeydown=e=>{if(e.key==='Enter')setPage(a.page,true);};$('att').append(li);});}
const tip=$('tip');function showTip(ev,nodes){tip.replaceChildren(...nodes);tip.style.display='block';const x=Math.min(ev.clientX+14,innerWidth-tip.offsetWidth-8);
tip.style.left=x+'px';tip.style.top=Math.max(8,ev.clientY-tip.offsetHeight-12)+'px';}function hideTip(){tip.style.display='none'}
// ---- line chart
const S=D.series.filter(p=>p.portfolio!=null).map(p=>({...p,...Object.fromEntries(['invested','spy_same','portfolio','spy','baseline','world','invested_tw'].map(k=>[k,p[k]==null?null:p[k]-100]))}));  // % return since inception
const TABS={invested:{sub:'Gain on the money put into stocks, cash excluded, vs the S&P 500 bought with all the money on day one (%, US dollars).',
  defs:[['invested','Invested money','--s1','Invested'],['spy_same','S&P 500 from day one','--s2','S&P 500']]},
 whole:{sub:'All $100k, cash and its interest included, vs the S&P 500 since inception (%, US dollars). Baseline = the first week\'s picks held unchanged.',
  defs:[['portfolio','Whole portfolio (incl. cash)','--s1','Portfolio'],['spy','S&P 500 (SPY)','--s2','S&P 500'],['world','Global shares (VT)','--s3','Global'],['baseline','Baseline (first picks held)','--muted','Baseline']]}};
const HID=new Set(['baseline']);try{const h=localStorage.getItem('chartHidden');if(h!=null){HID.clear();h.split(',').filter(Boolean).forEach(k=>HID.add(k));}}catch(e){}
const TRD={};(D.trades||[]).forEach(t=>{(TRD[t.date]=TRD[t.date]||[]).push(t);});
function nice(lo,hi){const raw=(hi-lo)/5||1,p=Math.pow(10,Math.floor(Math.log10(raw))),m=raw/p,st=(m<1.5?1:m<3?2:m<7?5:10)*p;return {lo:Math.floor(lo/st)*st,hi:Math.ceil(hi/st)*st,st};}
let defs=[],RANGE='All';
const RANGES=[['1D','24h'],['1W','1 week'],['3M','3 months'],['6M','6 months'],['YTD','Year to date'],['All','All']];
const LP=D.live_point?{...D.live_point,...Object.fromEntries(['invested','spy_same','portfolio','spy','baseline','world'].map(k=>[k,D.live_point[k]==null?null:D.live_point[k]-100]))}:null;
function rangeSeries(){if(!S.length)return {pts:[],base:null};const last=S[S.length-1],ld=new Date(last.date+'T00:00:00');let cut=null;
 if(RANGE==='1W'){cut=new Date(ld);cut.setDate(cut.getDate()-7);}
 else if(RANGE==='3M'||RANGE==='6M'){cut=new Date(ld);cut.setMonth(cut.getMonth()-(RANGE==='3M'?3:6));}
 else if(RANGE==='YTD'){cut=new Date(ld.getFullYear(),0,1);cut.setDate(0);}
 if(RANGE==='All')return {pts:S,base:S[0]};  // since inception, exactly as the headline figures
 let i0=0;if(RANGE==='1D')i0=Math.max(0,S.length-2);
 else if(cut){const c=`${cut.getFullYear()}-${String(cut.getMonth()+1).padStart(2,'0')}-${String(cut.getDate()).padStart(2,'0')}`;S.forEach((p,i)=>{if(p.date<=c)i0=i;});}
 // a part of the history: the invested tab compares time-weighted returns (money in stocks vs SPY's price), since the
 // money-weighted lines only add up over the whole period (see invested_tw in dashboard.py)
 const win=S.slice(i0).concat(RANGE==='1D'&&LP?[LP]:[]).map(p=>CUR==='invested'?{...p,invested:p.invested_tw}:p);const keys=['invested','spy_same','portfolio','spy','baseline','world'];
 const base={};keys.forEach(k=>{const b=win.find(p=>p[k]!=null);base[k]=b?b[k]:null;});
 return {pts:win.map(p=>({...p,...Object.fromEntries(keys.map(k=>[k,p[k]==null||base[k]==null?null:((100+p[k])/(100+base[k])-1)*100]))})),base:win[0]};}
function setRange(r){RANGE=r;document.querySelectorAll('.rng').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.r===r)));
 try{localStorage.setItem('chartRange',r)}catch(e){}drawLine();}
RANGES.forEach(([r,l])=>{const b=el('button',{type:'button',class:'rng','data-r':r,title:l,'aria-pressed':'false'},r);b.onclick=()=>setRange(r);$('ranges').append(b);});
let CUR='invested';
function setTab(name){const t=TABS[name]||TABS.invested;CUR=TABS[name]?name:'invested';defs=t.defs.filter(([k])=>S.some(p=>p[k]!=null));
 document.querySelectorAll('.tab').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.tab===name)));
 $('lineSub').textContent=t.sub;$('lineLegend').replaceChildren(...defs.map(([k,n,c])=>{const b=el('button',{type:'button',class:'lg','aria-pressed':String(!HID.has(k)),title:'Show or hide this line'},el('span',{class:'key',style:`background:var(${c})`}),n);
  b.onclick=()=>{if(HID.has(k))HID.delete(k);else if(defs.filter(([x])=>!HID.has(x)).length>1)HID.add(k);try{localStorage.setItem('chartHidden',[...HID].join(','))}catch(e){}setTab(CUR);};return b;}));
 $('lineTable').replaceChildren(el('tr',{},el('th',{},'Date'),...defs.map(([,n])=>el('th',{class:'n'},n)),el('th',{class:'n'},'Value')),
  ...S.map(p=>el('tr',{},el('td',{},p.date),...defs.map(([k])=>el('td',{class:'n'},p[k]==null?'n/a':pct(p[k]))),el('td',{class:'n'},usd(p.value)))));
 try{localStorage.setItem('chartTab',name)}catch(e){}drawLine();}
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>setTab(b.dataset.tab));
function drawLine(){const box=$('line');box.replaceChildren();const RS=rangeSeries(),S=RS.pts,vis=defs.filter(([k])=>!HID.has(k));
 const rl=(RANGES.find(([r])=>r===RANGE)||[])[1]||RANGE,[A,B2]=defs,lastP=S[S.length-1];
 const gapNow=A&&B2&&lastP&&lastP[A[0]]!=null&&lastP[B2[0]]!=null?lastP[A[0]]-lastP[B2[0]]:null;
 $('lineSub').textContent=(TABS[CUR]||TABS.invested).sub+(RS.base?` Showing ${rl.toLowerCase()}: change since the ${RS.base.date} close`+(RANGE==='1D'&&LP?', to live prices now':'')+(CUR==='invested'&&RANGE!=='All'?', as a daily-chained return of the money in stocks':'')+'.':'')
  +(gapNow==null?'':` ${gapNow>=0?'Ahead of':'Behind'} the S&P 500 by ${Math.abs(gapNow).toFixed(1)} percentage points.`);
 if(S.length<2){box.append(el('div',{class:'empty'},'Not enough data for this period yet.'));return;}
 const W=Math.max(300,Math.round(box.getBoundingClientRect().width)),L=44,R=W<560?92:124,T=12,B=30,H=W<560?230:320;
 // equal spacing per trading day (weekends and holidays take no room)
 const XI=new Map(S.map((p,i)=>[p.date,i])),XD=p=>L+XI.get(p.date)/((S.length-1)||1)*(W-L-R);
 const all=S.flatMap(p=>vis.map(([k])=>p[k]).filter(v=>v!=null));const N=nice(Math.min(0,...all),Math.max(0,...all)+1e-9),lo=N.lo,hi=N.hi;
 const Y=v=>T+(hi-v)/(hi-lo)*(H-T-B);const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Return of the portfolio against the S&P 500 (%); the same figures are in the table below'});
 for(let v=lo;v<=hi+N.st/2;v+=N.st){const z=Math.abs(v)<N.st/1e6;svg.append(sv('line',{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:z?'var(--axis)':'var(--grid)','stroke-width':1}));
  const t=sv('text',{x:L-6,y:Y(v)+4,'text-anchor':'end'});t.textContent=(z?0:v).toFixed(N.st<1?1:0)+'%';svg.append(t);}
 const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
 const dl=p=>p.live?'live':(+p.date.slice(8))+' '+MON[+p.date.slice(5,7)-1];
 {let lastX=1e9;for(let i=S.length-1;i>=0;i--){const x=XD(S[i]);if(lastX-x>=64||i===S.length-1){svg.append(sv('line',{x1:x,x2:x,y1:H-B,y2:H-B+4,stroke:'var(--axis)','stroke-width':1}));
   const t=sv('text',{x,y:H-B+18,'text-anchor':i===S.length-1?'end':'middle'});t.textContent=dl(S[i]);svg.append(t);lastX=x;}}}
 // the gap to the S&P 500, shaded: this is the excess return
 if(A&&B2&&!HID.has(A[0])&&!HID.has(B2[0]))for(let i=0;i<S.length-1;i++){const p=S[i],q=S[i+1],a=A[0],b=B2[0];if([p[a],p[b],q[a],q[b]].some(v=>v==null))continue;
  svg.append(sv('path',{d:`M${XD(p)},${Y(p[a])}L${XD(q)},${Y(q[a])}L${XD(q)},${Y(q[b])}L${XD(p)},${Y(p[b])}Z`,fill:(p[a]-p[b]+q[a]-q[b])>=0?'var(--up)':'var(--down)','fill-opacity':.1}));}
 const ends=[];vis.forEach(([k,n,c,short])=>{const P=S.filter(p=>p[k]!=null);if(P.length<2)return;
  svg.append(sv('path',{d:P.map((p,i)=>(i?'L':'M')+XD(p).toFixed(1)+','+Y(p[k]).toFixed(1)).join(''),fill:'none',stroke:`var(${c})`,'stroke-width':2,'stroke-linejoin':'round','stroke-linecap':'round',...(k==='baseline'?{'stroke-dasharray':'4 4'}:{})}));
  const e=P[P.length-1];ends.push({y:Y(e[k]),x:XD(e),c,label:(short||n)+' '+pct(e[k],1)});});
 // trades: a small mark on the date axis (what was traded is in the tooltip)
 S.forEach(p=>{if(TRD[p.date])svg.append(sv('circle',{cx:XD(p),cy:H-B,r:3.5,fill:'var(--ink2)',stroke:'var(--surface)','stroke-width':1.5}));});
 ends.sort((a,b)=>a.y-b.y);let prev=-1e9;ends.forEach(e=>{e.ly=Math.max(e.y,prev+16);prev=e.ly;});
 ends.forEach(e=>{svg.append(sv('circle',{cx:e.x,cy:e.y,r:4,fill:`var(${e.c})`,stroke:'var(--surface)','stroke-width':2}));
  if(Math.abs(e.ly-e.y)>2)svg.append(sv('line',{x1:e.x+6,y1:e.y,x2:e.x+12,y2:e.ly,stroke:'var(--axis)','stroke-width':1}));
  const t=sv('text',{x:e.x+14,y:e.ly+4});t.style.fill='var(--ink2)';t.textContent=e.label;svg.append(t);});
 const cross=sv('line',{y1:T,y2:H-B,stroke:'var(--axis)','stroke-width':1,visibility:'hidden'});svg.append(cross);
 const hit=sv('rect',{x:L,y:T,width:W-L-R,height:H-T-B+8,fill:'transparent'});svg.append(hit);
 hit.addEventListener('pointermove',ev=>{const r=svg.getBoundingClientRect(),px=(ev.clientX-r.left)/r.width*W;let best=S[0];
  S.forEach(p=>{if(Math.abs(XD(p)-px)<Math.abs(XD(best)-px))best=p;});const cx=XD(best);
  cross.setAttribute('x1',cx);cross.setAttribute('x2',cx);cross.setAttribute('visibility','visible');
  const rows=[el('div',{},el('span',{class:'muted'},(best.live?'Live '+(D.live_at||''):best.date+' close')+' · '+usd(best.value)))];
  vis.forEach(([k,n,c])=>{if(best[k]!=null)rows.push(el('div',{class:'r'},el('span',{class:'key',style:`background:var(${c})`}),el('b',{},pct(best[k])),el('span',{class:'muted'},n)));});
  if(A&&B2&&best[A[0]]!=null&&best[B2[0]]!=null){const g=best[A[0]]-best[B2[0]];rows.push(el('div',{class:'muted'},`${g>=0?'ahead of':'behind'} the S&P 500 by ${Math.abs(g).toFixed(1)} pp`));}
  (TRD[best.date]||[]).forEach(t=>rows.push(el('div',{},el('b',{},({BUY:'Bought',ADD:'Added to',SELL:'Sold',TRIM:'Trimmed'})[t.side]||t.side),' '+t.ticker)));showTip(ev,rows);});
 hit.addEventListener('pointerleave',()=>{cross.setAttribute('visibility','hidden');hideTip();});box.append(svg);}
// ---- horizontal bars
function hbars(box,items,emptyMsg){box.replaceChildren();if(!items.length){box.append(el('div',{class:'empty'},emptyMsg));return;}
 const rowH=28,W=Math.max(280,Math.round(box.getBoundingClientRect().width)),R=56,
  L=Math.min(Math.round(W*.45),Math.max(...items.map(i=>i.label.length))*7+12),H=items.length*rowH+8,max=Math.max(...items.map(i=>i.v));const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img'});
 items.forEach((it,i)=>{const y=4+i*rowH,w=Math.max(2,(it.v/max)*(W-L-R)),h=16,r=4;
  const lab=sv('text',{x:L-8,y:y+h/2+4,'text-anchor':'end'});lab.style.fill='var(--ink2)';const maxCh=Math.floor((L-12)/7);lab.textContent=it.label.length>maxCh?it.label.slice(0,maxCh-1)+'…':it.label;svg.append(lab);
  const d=`M${L},${y}H${L+w-r}Q${L+w},${y} ${L+w},${y+r}V${y+h-r}Q${L+w},${y+h} ${L+w-r},${y+h}H${L}Z`;
  const bar=sv('path',{d,fill:`var(${it.c||'--s1'})`});svg.append(bar);
  const val=sv('text',{x:L+w+6,y:y+h/2+4});val.textContent=it.v.toFixed(1)+'%';svg.append(val);
  const hit=sv('rect',{x:0,y:y-4,width:W,height:rowH,fill:'transparent',tabindex:0});
  const tipN=()=>[el('div',{},el('b',{},it.v.toFixed(2)+'%'),' ',el('span',{class:'muted'},it.tip||it.label))];
  hit.addEventListener('pointermove',ev=>{bar.style.opacity=.8;showTip(ev,tipN());});hit.addEventListener('pointerleave',()=>{bar.style.opacity=1;hideTip();});
  svg.append(hit);});box.append(svg);}
function drawAll(){if(PAGE==='holdings')riskBars();if(PAGE!=='overview')return;drawLine();
 hbars($('bars'),D.holdings.map(h=>({label:h.ticker,v:h.weight,c:h.type==='CORE'?'--s1':'--s2',tip:`${h.ticker} ${h.name} · ${h.type.toLowerCase()} · ${usd(h.value)}`})),'No holdings yet.');
 drawMix();}
let MIX='sectors';try{MIX=localStorage.getItem('mixTab')||MIX}catch(e){}if(!['sectors','countries'].includes(MIX))MIX='sectors';
function drawMix(){document.querySelectorAll('.tab2').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.mix===MIX)));
 $('mixSub').textContent=MIX==='sectors'?'% of the portfolio (cash not shown)':"% of the portfolio (cash not shown), by where the business is: the country of the currency a company reports in (NetEase reports in yuan: China, not its Cayman Islands incorporation), else where it's listed.";
 hbars($('sectors'),(D[MIX]||[]).map(([s,v])=>({label:s,v,tip:s+' · '+D.holdings.filter(h=>(MIX==='sectors'?h.sector:h.country)===s).map(h=>h.ticker).join(', ')})),'No holdings yet.');}
document.querySelectorAll('.tab2').forEach(b=>b.onclick=()=>{MIX=b.dataset.mix;try{localStorage.setItem('mixTab',MIX)}catch(e){}drawMix();});
// ---- risk: paired bars (risk share vs share of invested money)
function riskBars(){const box=$('risk');box.replaceChildren();const R=D.risk;
 if(!R||!R.rows.some(r=>r.risk_share_pct!=null)){box.append(el('div',{class:'empty'},'Appears after the first weekly risk report.'));return;}
 const inv=R.rows.reduce((a,r)=>a+(r.weight_pct||0),0),rows=R.rows.filter(r=>r.risk_share_pct!=null);
 const rowH=34,W=Math.max(280,Math.round(box.getBoundingClientRect().width)),L=78,Rm=52,H=rows.length*rowH+4,max=Math.max(...rows.flatMap(r=>[r.risk_share_pct,r.weight_pct/inv*100]));
 const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Each holding: share of portfolio risk vs share of invested money'});
 rows.forEach((r,i)=>{const y=2+i*rowH,ws=r.weight_pct/inv*100,sc=x=>Math.max(2,x/max*(W-L-Rm));
  const lab=sv('text',{x:L-8,y:y+13,'text-anchor':'end'});lab.style.fill='var(--ink2)';lab.textContent=r.ticker;svg.append(lab);
  const b1=sv('rect',{x:L,y:y+2,width:sc(r.risk_share_pct),height:12,rx:3,fill:r.flag?'var(--down)':'var(--s1)'});svg.append(b1);
  const b2=sv('rect',{x:L,y:y+17,width:sc(ws),height:8,rx:2,fill:'var(--axis)'});svg.append(b2);
  const v=sv('text',{x:L+sc(r.risk_share_pct)+6,y:y+12});v.textContent=r.risk_share_pct.toFixed(1)+'%';svg.append(v);
  const hit=sv('rect',{x:0,y,width:W,height:rowH,fill:'transparent'});
  hit.addEventListener('pointermove',ev=>showTip(ev,[el('div',{},el('b',{},r.ticker),el('span',{class:'muted'},` · vol ${r.vol_pct==null?'n/a':r.vol_pct.toFixed(0)+'%'}`)),
   el('div',{},`${r.risk_share_pct.toFixed(1)}% of risk on ${ws.toFixed(1)}% of invested money`),r.flag?el('div',{class:'down'},'over its risk budget (more than 2x)'):'']));
  hit.addEventListener('pointerleave',hideTip);svg.append(hit);});box.append(svg);}
{const R=D.risk,P=R&&R.corr_pairs;$('corrPairs').textContent=!P?'':P.length?`Moving closely together (weekly-return correlation above ${R.corr_flag}): `+P.map(p=>`${p.a} & ${p.b} ${p.rho.toFixed(2)}`).join(', ')+'. Overlapping exposure, informational only.':`No two holdings move closely together (correlation above ${R.corr_flag}).`;}
{const R=D.risk;$('riskSub').textContent=R?`${R.asof}: portfolio volatility ${R.sigma_p==null?'n/a':R.sigma_p.toFixed(1)+'%'} a year (cash included). How much of the portfolio's ups and downs each holding drives, next to how much money it holds. Red = more than twice its share. Informational; never trades.`:'No risk report yet.';
 table('riskTable',[{h:'Ticker',f:r=>r.ticker},{h:'Weight',n:1,f:r=>r.weight_pct==null?'':r.weight_pct.toFixed(1)+'%'},{h:'Target',n:1,f:r=>r.target_pct==null?'':r.target_pct.toFixed(1)+'%'},
  {h:'Volatility',n:1,f:r=>r.vol_pct==null?'n/a':r.vol_pct.toFixed(0)+'%'},{h:'MCR',n:1,f:r=>r.mcr_pct==null?'n/a':r.mcr_pct.toFixed(1)+'%'},
  {h:'Risk share',n:1,f:r=>r.risk_share_pct==null?'n/a':r.risk_share_pct.toFixed(1)+'%',c:r=>r.flag?'down':''}],R?R.rows:[],'No risk report yet.');}
{const A=D.attribution,p2=x=>x==null?'n/a':pct(x*100,2);
 if(!A){$('attrSub').textContent='Appears after the first weekly attribution report.';}
 else{$('attrSub').textContent=`${A.start} to ${A.end} (${A.days} trading days) vs a sector-weighted S&P 500. Informational: not meaningful until about 6 months of history. Cash is its own sector, so the reserve's cost or benefit shows in allocation.`;
  $('attrTiles').append(tile('Excess return',p2(A.excess),`portfolio ${p2(A.portfolio)} · index ${p2(A.benchmark)}`,cls(A.excess)),
   tile('Sector bets (allocation)',p2(A.allocation),'which sectors, and cash, we held',cls(A.allocation)),
   tile('Stock picking (selection)',p2(A.selection),'our stocks vs their sector',cls(A.selection)),
   tile('Interaction',p2(A.interaction),'overweight where we also picked well (or not)',cls(A.interaction)));
  const rows=Object.entries(A.sectors).map(([s,e])=>({s,...e,t:e.allocation+e.selection+e.interaction})).filter(r=>r.wp_avg>0||Math.abs(r.t)>5e-5).sort((a,b)=>Math.abs(b.t)-Math.abs(a.t));
  table('attrTable',[{h:'Sector',f:r=>r.s},{h:'Our weight',n:1,f:r=>(r.wp_avg*100).toFixed(1)+'%'},{h:'Index',n:1,f:r=>(r.wb*100).toFixed(1)+'%'},
   {h:'Allocation',n:1,f:r=>p2(r.allocation),c:r=>cls(r.allocation)},{h:'Selection',n:1,f:r=>p2(r.selection),c:r=>cls(r.selection)},
   {h:'Interaction',n:1,f:r=>p2(r.interaction),c:r=>cls(r.interaction)},{h:'Total',n:1,f:r=>p2(r.t),c:r=>cls(r.t)}],rows,'');}}
{let r0='All';try{r0=localStorage.getItem('chartRange')||r0}catch(e){}RANGE=RANGES.some(([r])=>r===r0)?r0:'All';
 document.querySelectorAll('.rng').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.r===RANGE)));}
{let t0='invested';try{t0=localStorage.getItem('chartTab')||t0}catch(e){}setTab(TABS[t0]?t0:'invested');}
setPage(location.hash.slice(1));drawn=true;drawAll();let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(drawAll,150);});
// ---- tables
function table(id,cols,rows,empty,opt={}){const t=$(id),lim=opt.limit??15;
 const ths=cols.map(c=>el('th',{class:(c.n?'n ':'')+'so',tabindex:0,title:'Click to sort'},c.h));t.append(el('tr',{},...ths));
 if(!rows.length){t.append(el('tr',{},el('td',{colspan:cols.length,class:'muted'},empty)));return;}
 const wide=cols.some(c=>c.w);
 const trs=rows.map(r=>{const tr=el('tr',{},...cols.map(c=>{const v=c.f(r);const td=el('td',{class:(c.n?'n ':'')+(c.w?'w ':'')+(c.c?c.c(r):'')});
  if(v instanceof Node)td.append(v);else td.textContent=v;return td;}));
  if(wide){tr.classList.add('x');tr.title='Click to show the full text';tr.onclick=e=>{if(!e.target.closest('a'))tr.classList.toggle('open');};}t.append(tr);return tr;});
 const wrap=t.closest('.tw');let all=false,q='',chip=opt.chips?opt.chips[0][1]:null,ord=trs.map((_,i)=>i),sc=-1,dir=1;
 const more=el('button',{type:'button',class:'toggle more'});
 const apply=()=>{let n=0,m=0;ord.forEach(i=>{const tr=trs[i],ok=(!q||tr.textContent.toLowerCase().includes(q))&&(!chip||chip(rows[i])),show=ok&&(all||q||n<lim);if(ok)m++;if(show)n++;tr.hidden=!show;});
  more.hidden=m<=lim||!!q;more.textContent=all?`Show the first ${lim}`:`Show all ${m}`;};
 more.onclick=()=>{all=!all;apply();};wrap.after(more);
 // sort on the cell text: numbers for numeric columns, blanks always last
 const key=(ci,i)=>{const x=trs[i].children[ci].textContent.trim();if(!cols[ci].n)return x.toLowerCase()||null;const v=parseFloat(x.replace(/[$,+▲▼\s]/g,'').replace('−','-'));return isNaN(v)?null:v;};
 ths.forEach((th,ci)=>{const go=()=>{dir=sc===ci?-dir:(cols[ci].n?-1:1);sc=ci;const k=trs.map((_,i)=>key(ci,i));
   ord.sort((a,b)=>k[a]==null?(k[b]==null?0:1):k[b]==null?-1:(k[a]<k[b]?-1:k[a]>k[b]?1:0)*dir);ord.forEach(i=>t.append(trs[i]));
   ths.forEach(x=>x.removeAttribute('aria-sort'));th.setAttribute('aria-sort',dir>0?'ascending':'descending');apply();};
  th.onclick=go;th.onkeydown=e=>{if(e.key==='Enter')go();};});
 if(opt.filter){const inp=el('input',{type:'search',class:'filter',placeholder:opt.filter,'aria-label':opt.filter});inp.oninput=()=>{q=inp.value.trim().toLowerCase();apply();};wrap.before(inp);}
 if(opt.chips){const box=el('div',{class:'ranges',role:'group'});opt.chips.forEach(([l,f],i)=>{const b=el('button',{type:'button',class:'chip','aria-pressed':String(i===0)},l);
   b.onclick=()=>{chip=f;all=false;box.querySelectorAll('.chip').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));apply();};box.append(b);});wrap.before(box);}
 apply();}
const link=(path,txt)=>D.repo&&path?el('a',{href:`${D.repo}/blob/main/${path}`,target:'_blank',rel:'noopener'},txt):txt;
const dayOf=r=>r.live_day_pct!=null?{p:r.live_day_pct,u:r.live_day_usd,t:'last 24h: live price vs the '+r.last_date+' close'}:
 (r.day_pct!=null?{p:r.day_pct,u:r.day_usd,t:r.prev_date==='bought at the open'?`last session: ${r.last_date} close vs our fill at the open`:`last session: ${r.last_date} close vs the ${r.prev_date} close`}:null);
const chg=d=>{if(!d)return '–';const c=d.p>0.005?'up':d.p<-0.005?'down':'flat';
 const b=el('span',{class:'chg '+c,title:d.t},(c==='up'?'▲ ':c==='down'?'▼ ':'')+pct(d.p,2));
 if(d.u!=null)b.append(el('small',{},(d.u>=0?'+':'−')+usd(Math.abs(d.u))));return b;};
table('holdings',[{h:'Ticker',f:r=>r.ticker},{h:'Name',f:r=>el('span',{title:r.name},r.name),c:()=>'nm'},{h:'Held conv.',n:1,f:r=>r.conviction??''},
 {h:'Latest research',f:r=>{if(r.latest_conviction==null)return '';const t=`${r.latest_conviction} (${r.latest_eval_date})`;return r.latest_conviction<D.min_buy&&r.latest_conviction<(r.conviction||0)?el('span',{class:'flag',title:'Below the buy bar: the position is resized at the next open'},t+' ▼'):t;}},
 {h:'Weight',n:1,f:r=>r.weight.toFixed(1)+'%'},{h:'Value',n:1,f:r=>usd(r.value)},
 {h:'Since entry',n:1,f:r=>pct(r.live_change_pct!=null&&r.live_day_pct!=null?r.live_change_pct:r.change_pct,1),c:r=>cls(r.live_day_pct!=null?r.live_change_pct:r.change_pct)},
 {h:'P/L',n:1,f:r=>r.pl==null?'':usd(r.pl),c:r=>cls(r.pl)},{h:'24h change',n:1,f:r=>chg(dayOf(r))},
 {h:'To fair value',n:1,f:r=>r.fv_upside==null?'–':r.fv_unreliable?el('span',{class:'muted',title:'Unreliable: the valuation methods disagree by more than 2x, so the scorecard ignores this fair value'},pct(r.fv_upside,0)+' ?'):pct(r.fv_upside,0),c:r=>r.fv_unreliable?'':cls(r.fv_upside)},
 {h:'Days held',n:1,f:r=>r.days_held??''},{h:'Entry',n:1,f:r=>r.entry_price==null?'':`${px(r.entry_price)} ${r.currency} (${r.entry_date})`},
 {h:'Close',n:1,f:r=>r.last_price==null?'':`${px(r.last_price)} ${r.currency} (${r.last_date})`},{h:'Live',n:1,f:r=>r.live?`${r.live.price.toFixed(2)} (${r.live.uk})`:'–'},
 {h:'Sector',f:r=>r.sector},{h:'Plan and thesis',w:1,f:r=>[r.plan,r.thesis].filter(Boolean).join(' · ')}],D.holdings,'No holdings yet: the portfolio is all cash.',{limit:30});
const isHold=r=>r.action==='HOLD';
table('pending',[{h:'Placed',f:r=>r.placed},{h:'Action',f:r=>r.action},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},
 {h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Est. shares',n:1,f:r=>isHold(r)?'–':(r.est.shares??'')},
 {h:'Latest close',n:1,f:r=>isHold(r)||r.est.price==null?'–':`${px(r.est.price)} ${r.est.currency} (${r.est.close_date})`},
 {h:'Est. value',n:1,f:r=>isHold(r)||r.est_usd==null?'–':usd(r.est_usd)},
 {h:'Fills',f:r=>r.fills||''},
 {h:'Note',w:1,f:r=>isHold(r)?'No trade: records the refreshed thesis and conviction from the re-research.':(r.replaces?`Replaces ${r.replaces}.`:'Rules re-checked at the opening price before it fills.')}],
 D.pending,'No pending orders.');
table('fqueue',[{h:'Ticker',f:r=>r.ticker},{h:'Name',f:r=>r.name},{h:'Stage',f:r=>r.stage==='topup'?(r.ordered?'starter ordered':'top-up'):'waiting'},
 {h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Decided',f:r=>`${r.added} at ${px(r.decision_price)} ${r.ccy}`},
 {h:'Latest close',n:1,f:r=>r.close==null?'':`${px(r.close)} ${r.ccy}`},{h:'Base FV upside',n:1,f:r=>r.upside==null?'–':pct(r.upside,0),c:r=>cls(r.upside)},
 {h:'Weight / target',n:1,f:r=>r.stage==='topup'&&r.weight!=null&&r.target!=null?`${r.weight.toFixed(1)}% of ${(+r.target).toFixed(1)}%`:'–'},
 {h:'Expires',f:r=>r.expires},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],D.funding_queue||[],'Nothing waiting: every conviction-4 buy fitted.');
{const P=D.dip;$('dipSub').textContent=P?`${P.asof}: ${P.watched} stocks watched (holdings and recent conviction-3+ AVOIDs). A signal is an unusual fall since our last research, beyond what the market explains (z = standard deviations of the stock's own moves; −2 or lower), with the price at or below base fair value. Signals are re-researched the next day; a fall is never a buy on its own. ${P.hits.length?'Queued: '+P.hits.join(', ')+'.':'Nothing queued.'}`:'The dip radar has not run yet.';
table('dips',[{h:'Ticker',f:r=>r.ticker},{h:'Kind',f:r=>r.kind==='holding'?'holding':'avoid'},{h:'Signal',f:r=>r.signal?'YES':''},
 {h:'z',n:1,f:r=>r.z==null?'–':r.z.toFixed(2),c:r=>r.z!=null&&r.z<=-2?'down':''},
 {h:'Since research',f:r=>r.last_research?`${r.last_research} (${r.sessions} sessions)`:''},
 {h:'Return',n:1,f:r=>r.ret_pct==null?'–':pct(r.ret_pct,1),c:r=>cls(r.ret_pct)},{h:'S&P',n:1,f:r=>r.spy_pct==null?'–':pct(r.spy_pct,1)},
 {h:'Stock-specific',n:1,f:r=>r.specific_pct==null?'–':pct(r.specific_pct,1),c:r=>cls(r.specific_pct)},
 {h:'vs base FV',n:1,f:r=>r.vs_base_pct==null?'–':pct(r.vs_base_pct,0)},{h:'Why not a signal',w:1,f:r=>r.signal?'':(r.why_not||'')}],
 P?P.rows:[],'No unusual falls since our last research (nothing at z −1 or lower).');}
{const np=D.near_pct??10,W=D.watch||[],nearRow=r=>r.hit||(r.to_entry!=null&&r.to_entry>=-np),lte=r=>r.live?(r.entry/r.live.price-1)*100:null;
table('watch',[{h:'Ticker',f:r=>r.ticker},{h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Close',n:1,f:r=>r.close==null||r.close===''?'':`${(+r.close).toFixed(2)} ${r.ccy} (${r.close_date})`},
 {h:'Live',n:1,f:r=>r.live?`${r.live.price.toFixed(2)} (${r.live.uk})`:'–'},
 {h:'Entry price',n:1,f:r=>`${(+r.entry).toFixed(2)} ${r.ccy}`},{h:'To entry (close)',n:1,f:r=>r.to_entry==null?'':pct(r.to_entry,1),c:r=>r.to_entry!=null&&r.to_entry>=0?'up':''},
 {h:'To entry (live)',n:1,f:r=>{const x=lte(r);return x==null?'–':pct(x,1);},c:r=>lte(r)>=0?'up':''},
 {h:'Status',f:r=>r.hit?'HIT '+r.hit+': re-research next run':r.skipped?'hit skipped '+r.skipped:r.blocked?'too far from a 4: a hit is skipped':r.near_since?'close since '+r.near_since:''},
 {h:'Why not a buy yet',w:1,f:r=>r.why||''},{h:'Set by',f:r=>r.source},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],W,'No entry prices yet.',
 {filter:'Filter by ticker or text',chips:[[`Within ${np}% of entry (${W.filter(nearRow).length})`,nearRow],[`All ${W.length}`,null]]});
$('watchSub').textContent=`${W.length} conviction-3 names, closest first, with the price at which we'd look again. Live prices cover the 40 closest. A close at or below it triggers a full re-research (never an automatic buy), unless the scorecard is 2 or more points short of a 4 at any price.`;}
table('trades',[{h:'Date',f:r=>r.date},{h:'Side',f:r=>r.side},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Shares',n:1,f:r=>r.shares},
 {h:'Fill',n:1,f:r=>`${px(r.fill_price)} ${r.currency} (${r.fill_close_date})`},{h:'Gross',n:1,f:r=>usd(+r.gross_usd,2)},{h:'Costs',n:1,f:r=>usd(+r.costs_usd,2)},
 {h:'Reason',w:1,f:r=>r.reason||''}],D.ledger,'No trades yet.');
{const hs=['1m','3m','6m','12m'].filter(h=>D.hits[h].n),rate=(l,x)=>tile(l,x.n?Math.round(x.hits/x.n*100)+'%':'–',x.n?`${x.hits} of ${x.n} decisions right`:'none matured yet');
 if(!hs.length)$('hits').append(tile('Hit rate','–','no decision is a month old yet'));
 hs.forEach(h=>$('hits').append(rate(`Buys and holds, ${h}`,D.hits[h].buy),rate(`Avoids and trims, ${h}`,D.hits[h].avoid)));}
table('decisions',[{h:'Date',f:r=>r.date},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Decision',f:r=>r.decision},
 {h:'Conv.',n:1,f:r=>r.conviction},{h:'Price',n:1,f:r=>`${(+r.price).toFixed(2)} ${r.currency} (${r.live?'live, ':'close '}${r.price_date})`},{h:'1m vs SPY',n:1,f:r=>r.excess_1m===''?'–':pct(+r.excess_1m,1),c:r=>r.excess_1m===''?'':cls(+r.excess_1m)},
 {h:'3m vs SPY',n:1,f:r=>r.excess_3m===''?'–':pct(+r.excess_3m,1),c:r=>r.excess_3m===''?'':cls(+r.excess_3m)},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],D.decisions,'No decisions yet.',{filter:'Filter by ticker or decision',chips:[['With a result',r=>r.excess_1m!==''],['Buys',r=>r.decision==='BUY'||r.decision==='ADD'],
  ['Holds and trims',r=>!['BUY','ADD','AVOID'].includes(r.decision)],['Avoids',r=>r.decision==='AVOID'],['All',null]]});
{const E=D.exits||[],sv=x=>x===''?'–':(+x>=0?'+':'−')+usd(Math.abs(+x),0),lag=E.filter(r=>r.since_excess!==''),m1=E.filter(r=>r.hit_1m!=='');
 $('exitTiles').append(tile('Since the exit: lagged the S&P 500',lag.length?`${lag.filter(r=>+r.since_excess<0).length} of ${lag.length}`:'–','sold or trimmed stocks that did worse than the index since'),
  tile('Selling saved so far',lag.length?sv(-lag.reduce((a,r)=>a+(+r.kept_usd||0),0)):'–','what the sold shares lost since (+) or gained (−)'),
  tile('Trims and sells right, 1m',m1.length?Math.round(m1.filter(r=>+r.hit_1m).length/m1.length*100)+'%':'–',m1.length?`${m1.filter(r=>+r.hit_1m).length} of ${m1.length}`:'none a month old yet'));
 const why=r=>r.kind==='swap'?`swapped for ${r.replaced_by}`:r.kind==='sizing'?'cut to conviction-3 size':'research';
 table('exits',[{h:'Date',f:r=>r.date},{h:'Ticker',f:r=>r.ticker},{h:'Exit',f:r=>r.decision.toLowerCase()},{h:'Why',f:why},{h:'Sold',n:1,f:r=>usd(+r.usd,0)},
  {h:'Since, vs S&P',n:1,f:r=>r.since_excess===''?'–':pct(+r.since_excess,1),c:r=>r.since_excess===''?'':cls(-r.since_excess)},
  {h:'Selling saved',n:1,f:r=>sv(-r.kept_usd),c:r=>r.kept_usd===''?'':cls(-r.kept_usd)},
  {h:'Bought vs sold',n:1,f:r=>r.vs_replacement_since===''?'–':pct(+r.vs_replacement_since,1),c:r=>r.vs_replacement_since===''?'':cls(+r.vs_replacement_since)},
  {h:'1m vs SPY',n:1,f:r=>r.excess_1m===''?'–':pct(+r.excess_1m,1),c:r=>r.excess_1m===''?'':cls(-r.excess_1m)},
  {h:'3m vs SPY',n:1,f:r=>r.excess_3m===''?'–':pct(+r.excess_3m,1),c:r=>r.excess_3m===''?'':cls(-r.excess_3m)}],E,'No trims or sales yet.');}
{const F=D.funnel||{};['7','30'].forEach(d=>{const x=F[d];if(!x)return;$('funnel').append(tile(`Last ${d} days: researched`,String(x.researched),'stocks given a verdict'),
  tile('reached conviction 4+',String(x.conv4),x.researched?(x.conv4/x.researched*100).toFixed(1)+'% of those researched':''),tile('bought',String(x.bought),'filled buy orders'));});}
{const SC=D.scoreboard||{},rows=Object.entries(SC.by_conviction||{}).flatMap(([g,hs])=>Object.entries(hs).map(([h,c])=>({g,h,...c}))).sort((a,b)=>b.g.localeCompare(a.g)||a.h.localeCompare(b.h));
 $('scoreSub').textContent=SC.asof?`${SC.asof}: how stocks did after the decision, by conviction, against the S&P 500 and against their own sector (average, percentage points). A scorecard that works shows higher convictions doing better. Most convictions here are AVOIDs, so a positive number for conviction 3 means names we passed on went up.`:'Appears after the first weekly calibration report.';
 const f1=x=>x==null?'n/a':(x>=0?'+':'')+x.toFixed(1);
 table('score',[{h:'Conviction',f:r=>r.g},{h:'Horizon',f:r=>r.h},{h:'Decisions',n:1,f:r=>r.n},{h:'vs S&P 500',n:1,f:r=>f1(r.mean_vs_spy),c:r=>cls(r.mean_vs_spy)},{h:'vs sector',n:1,f:r=>f1(r.mean_vs_sector),c:r=>cls(r.mean_vs_sector)}],rows,'No matured decisions yet.');
 const pr=Object.entries(SC.by_points||{}).map(([k,c])=>({k,...c}));
 $('pointsSub').textContent='By scorecard points under today\'s rules (the buy bar is 9). Fills in from December, when the first scorecard-era decisions are a month old.';
 table('points',[{h:'Points',f:r=>r.k},{h:'Decisions',n:1,f:r=>r.n},{h:'vs S&P 500',n:1,f:r=>f1(r.mean_vs_spy),c:r=>cls(r.mean_vs_spy)}],pr,'No scorecard-era decision has matured yet.');}
{const Hh=D.health||{jobs:[],problems:[]};
 table('jobs',[{h:'Job',f:r=>r.job},{h:'Last ran',f:r=>r.last||'never'},{h:'Last run',f:r=>r.last?(r.ok?'no problems logged':'problems logged'):'',c:r=>r.last?(r.ok?'okd':'bad'):''}],Hh.jobs,'No logs found.');
 table('problems',[{h:'Date',f:r=>r.date},{h:'Job',f:r=>r.job},{h:'Log line',w:1,f:r=>r.line}],Hh.problems,'No problem lines in the last 7 days.');}
$('screenSub').textContent=D.screen.asof?`${D.screen.asof}: ${D.screen.screened} stocks scored${D.screen.illiquid?` (${D.screen.illiquid} too thinly traded to rank were left out first)`:''}. The picks below were sent to research. The score ranks how well a stock fits the screen (core: quality and value; tactical: the strength of its setup). It is not a rating: research decides, and most picks come back AVOID.`:'No screen yet.';
D.screen.picks.forEach(p=>$('picks').append(el('span',{class:'pill',style:'margin:0 6px 6px 0'},`${p.ticker} · ${p.type.toLowerCase()} · ${p.score}`)));
if(D.repo)$('repo').append('Source and research notes: ',el('a',{href:D.repo},D.repo.replace('https://','')));
</script></body></html>
"""


def mandate_html(cfg: dict, short: bool = False) -> str:
    """The mandate / investment-process card at the top of the dashboard (owner request 2026-11-06: make the
    process visible to outside viewers). Built from the live config so its numbers never go stale."""
    from html import escape as e
    p, core, cs = cfg["portfolio"], cfg["core"], cfg.get("cash_strategy", {})
    sz = core["conviction_size_pct"]
    lo, hi = core.get("vol_scale_clamp", [0.6, 1.4])
    caps = "; ".join(f"{g['name']} {g['max_pct']:g}%" for g in p.get("country_group_caps", []))
    uni = cfg.get("universe", {}).get("allworld_size")
    roll = int(core.get("rolling_reviews_per_week", 0))
    steps = [
        ("Screen", f"Every week {f'the ~{uni:,} largest listed companies worldwide' if uni else 'the universe'} "
                   "are ranked on quality and valuation; cyclicals on peak profits are marked down."),
        ("Research", "An AI analyst writes a note from stockanalysis.com figures and primary sources (filings, "
                     "company releases), citing every number."),
        ("Decide", "The bear case is argued before the bull case, ending in BUY or AVOID with conviction 1-5. "
                   f"Only conviction {core.get('min_buy_conviction', 4)}+ is bought."),
        ("Size", f"{sz['4']:g}% (conviction 4) or {sz['5']:g}% (5), scaled {lo:g}-{hi:g}x by volatility. "
                 f"Caps: {p['max_sector_pct']:g}% per sector" + (f"; {caps}" if caps else "")
                 + f"; at most {p['max_holdings']} holdings."),
        ("Monitor", "Daily re-pricing and thesis triggers, a dip radar for unusual falls"
                    + (f", and a full re-check of {roll} holdings a week" if roll else "")
                    + (f". Cash is whatever the caps and conviction bar leave, above a {p['min_cash_pct']:g}% floor; "
                       "the macro stress score is shown, never used to size cash." if cs.get("mode") == "residual" else
                       f". A cash reserve of {cs['reserve_min_pct']:g}-{cs['reserve_max_pct']:g}% follows a "
                       "macro stress score." if "reserve_min_pct" in cs else ".")),
    ]
    intro = (f"Objective: beat the S&P 500 over rolling 12-month periods with a concentrated portfolio of "
             f"{p['min_holdings']}-{p['max_holdings']} high-quality businesses bought at attractive valuations, "
             f"held for their fundamentals (about a 12-month horizon). Paper trading only: "
             f"${p['starting_cash_usd']:,.0f} simulated, in US dollars, no broker.")
    rule = ("Core positions have no price stops: they are sold when the business case breaks, not when the price "
            "falls. Sell-side price targets are never used. Every decision is logged and scored against the "
            "S&P 500 at 1, 3, 6 and 12 months.")
    if short:  # top of Overview: say what this is first (owner request 2026-11-17); the full card stays on Process
        return (f'<section class="card mandate" aria-label="What this is"><h2>What this is</h2><p>{e(intro)}</p>'
                f'<p class="sub">{e(" → ".join(t for t, _ in steps))} · '
                '<a href="#process" onclick="setPage(\'process\',true);return false">How it works</a></p></section>')
    lis = "".join(f'<li><b>{i}. {e(t)}</b><span>{e(d)}</span></li>' for i, (t, d) in enumerate(steps, 1))
    return (f'<section class="card mandate" aria-label="Mandate"><h2>Mandate &amp; investment process</h2>'
            f'<p>{e(intro)}</p><ol class="steps">{lis}</ol><p class="sub">{e(rule)}</p></section>')


DAILY_TOP = ("**Portfolio", "**Trades", "**Moves", "**Problems")


def daily_html(folder: Path) -> str:
    """The latest reports/daily/<date>.md as a card: what the 21:30 run did (owner request 2026-11-17). Value,
    trades, moves and problems show; the rest folds under "Full report"."""
    import re
    from html import escape
    files = sorted(folder.glob("*.md"))
    if not files:
        return ""

    def block(b: str) -> str:
        lines = [re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(ln)) for ln in b.strip().splitlines()]
        items = "".join(f"<li>{ln[2:]}</li>" for ln in lines if ln.startswith("- "))
        return "".join(f"<p>{ln}</p>" for ln in lines if not ln.startswith("- ")) + (f"<ul>{items}</ul>" if items else "")

    blocks = [b.strip() for b in files[-1].read_text().split("\n\n") if b.strip() and not b.startswith("#")]
    top = "".join(block(b) for b in blocks if b.startswith(DAILY_TOP))
    rest = "".join(block(b) for b in blocks if not b.startswith(DAILY_TOP))
    more = f"<details><summary>Full report</summary>{rest}</details>" if rest else ""
    return f'<section class="card daily"><h2>Last daily run · {escape(files[-1].stem)}</h2>{top}{more}</section>'


def render(data: dict) -> str:
    blob = json.dumps(data).replace("</", "<\\/")  # never let data close the script tag
    return (PAGE.replace("__DATA__", blob).replace("__MANDATE__", mandate_html(load_config()))
            .replace("__INTRO__", mandate_html(load_config(), short=True))
            .replace("__DAILY__", daily_html(ROOT / "reports" / "daily")))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--no-live", action="store_true", help="skip the live-price snapshot (offline / tests)")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(build_data(live=not a.no_live)))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
