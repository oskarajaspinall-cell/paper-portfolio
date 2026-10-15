"""Dividends and stock splits (owner request 2026-10-16). No model calls.

    python scripts/corporate_actions.py check [--asof YYYY-MM-DD] [--dry-run]

Runs before the daily re-pricing (bin/fill-pending) and the weekly run's mark. `asof` is the day after the last
completed session, as for `portfolio.py mark`: only ex-dates, pay dates and split dates BEFORE asof are acted on.

DIVIDENDS (stockanalysis.com dividend page of each stock held now or sold in the last 90 days):
- due only on shares held at the close BEFORE the ex-date (ledger fills dated before that day): a stock bought
  on its ex-date gets nothing,
- on the ex-date the net amount (after [corporate_actions].withholding_pct for the dividend's currency) becomes
  a receivable: it counts in the portfolio's value (the share price drops by about the dividend that day) and in
  the sleeve's income, converted to USD at the stockanalysis.com rate on the day it is recorded,
- on the pay date the receivable moves into cash (a DIVIDEND ledger row, so the interest rebuild stays exact),
- the baseline earns the same dividends on its own shares (credited to its cash on the ex-date).
A dividend page that can't be read is skipped and named in the output; the next run catches it up.

SPLITS (the split column of Yahoo's daily history, the owner-approved price source, confirmed against the
stockanalysis.com statistics page; the run STOPS if the two disagree, so nothing is re-priced on a wrong count):
- shares x ratio, cost basis unchanged; a fraction left by a reverse split is paid out in cash at that close,
- every stored per-share price / ratio: entry price, last close, tactical stop and target,
- the baseline's shares likewise.
Watchlist entry prices are split-adjusted by entry_watch.py check; decision scoring by decision_log.py.

Every action is keyed by ticker + date in portfolio/corporate_actions.csv, so a re-run or a catch-up after a
missed day never applies it twice.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DataError, load_config  # noqa: E402

CA_COLS = ["key", "date", "ticker", "kind", "ex_date", "pay_date", "ratio", "amount", "currency", "fx_usd_per_unit",
           "shares", "gross_usd", "withholding_usd", "net_usd", "source_url", "note"]
SOLD_LOOKBACK_DAYS = 90
TRADE_SIGN = {"BUY": 1, "ADD": 1, "SELL": -1, "TRIM": -1}


def shares_before(ledger: list[dict], ticker: str, day: str) -> float:
    """Shares of `ticker` held at the close before `day`, rebuilt from the ledger (splits included)."""
    n = 0.0
    for r in ledger:
        if r["ticker"] != ticker or (r.get("fill_close_date") or r["date"]) >= day:
            continue
        if r["side"] in TRADE_SIGN:
            n += TRADE_SIGN[r["side"]] * float(r["shares"])
        elif r["side"] == "SPLIT":
            n += float(r["shares"])  # the change in shares
    return n


def withholding_pct(cfg: dict, ccy: str) -> float:
    w = (cfg.get("corporate_actions") or {}).get("withholding_pct") or {}
    return float(w.get(ccy, w.get("default", 0.0)))


def parse_split_stats(stats: dict) -> tuple[str, float] | None:
    """stockanalysis.com statistics page -> (last split date ISO, new shares per old share), or None."""
    d, r = (stats.get("lastSplitDate") or {}).get("text"), (stats.get("splitRatio") or {}).get("text")
    if not d or not r or d == "n/a":
        return None
    new, old = (float(x) for x in str(r).split(":"))
    return dt.datetime.strptime(d, "%b %d, %Y").date().isoformat(), new / old


def _ptype(state: dict, ledger: list[dict], ticker: str) -> str:
    h = state["holdings"].get(ticker)
    if h:
        return h["type"]
    return next((r["type"] for r in reversed(ledger) if r["ticker"] == ticker and r["type"] in ("CORE", "TACTICAL")),
                "CORE")


def candidates(state: dict, ledger: list[dict], asof: str) -> list[str]:
    """Held now, or sold in the last 90 days (a sale after an ex-date still earns that dividend)."""
    cut = (dt.date.fromisoformat(asof) - dt.timedelta(days=SOLD_LOOKBACK_DAYS)).isoformat()
    out = list(state["holdings"])
    for r in ledger:
        if r["side"] in ("SELL", "TRIM") and r["date"] >= cut and r["ticker"] not in out:
            out.append(r["ticker"])
    return out


def dividends(state: dict, ledger: list[dict], done: set, mkt, cfg: dict, asof: str, rows_fn) -> dict:
    """Record new ex-dates as receivables, then pay those whose pay date has passed. Mutates state."""
    new_ledger, ca, notes, upcoming = [], [], [], []
    recv = state.setdefault("receivables", [])
    for t in candidates(state, ledger, asof):
        try:
            page = rows_fn(t)
        except DataError as e:
            notes.append(f"{t}: dividend page not read, retried next run ({str(e)[:120]})")
            continue
        for d in page["rows"]:
            key = f"DIV:{t}:{d['ex_date']}"
            if d["ex_date"] >= asof:
                if t in state["holdings"]:
                    upcoming.append({"ticker": t, "ex_date": d["ex_date"], "pay_date": d["pay_date"],
                                     "amount": d["amount"], "currency": d["currency"]})
                continue
            if key in done:
                continue
            sh = shares_before(ledger, t, d["ex_date"])
            if sh <= 0:
                continue
            fx = 1.0 if d["currency"] == "USD" else mkt.fx(d["currency"])["rate"]
            gross = sh * d["amount"] * fx
            wht = gross * withholding_pct(cfg, d["currency"]) / 100
            net = round(gross - wht, 2)
            ptype = _ptype(state, ledger, t)
            recv.append({"key": key, "ticker": t, "type": ptype, "ex_date": d["ex_date"], "pay_date": d["pay_date"],
                         "shares": sh, "amount": d["amount"], "currency": d["currency"], "fx_usd_per_unit": fx,
                         "gross_usd": round(gross, 2), "withholding_usd": round(wht, 2), "net_usd": net,
                         "source_url": page.get("url", "")})
            fl = state["flows"][ptype]
            fl["income"] = round(fl.get("income", 0.0) + net, 2)
            b = state.get("baseline")
            if b and t in b["holdings"]:  # mirrored until frozen_from, its own shares after
                bsh = b["holdings"][t]["shares"] if d["ex_date"] >= b.get("frozen_from", "") else sh
                b["cash_usd"] += bsh * d["amount"] * fx * (1 - withholding_pct(cfg, d["currency"]) / 100)
            done.add(key)
            ca.append({"key": key, "date": d["ex_date"], "ticker": t, "kind": "DIVIDEND", "ex_date": d["ex_date"],
                       "pay_date": d["pay_date"] or "", "amount": d["amount"], "currency": d["currency"],
                       "fx_usd_per_unit": round(fx, 8), "shares": sh, "gross_usd": round(gross, 2),
                       "withholding_usd": round(wht, 2), "net_usd": net, "source_url": page.get("url", ""),
                       "note": "receivable from the ex-date"})
    for r in list(recv):
        pay = r["pay_date"] or r["ex_date"]  # no pay date shown: paid on the ex-date
        if pay >= asof:
            continue
        state["cash_usd"] = round(state["cash_usd"] + r["net_usd"], 2)
        recv.remove(r)
        new_ledger.append({"date": pay, "ticker": r["ticker"], "type": r["type"], "side": "DIVIDEND",
                           "shares": r["shares"], "fill_price": r["amount"], "currency": r["currency"],
                           "fill_close_date": pay, "fx_usd_per_unit": round(r["fx_usd_per_unit"], 8),
                           "gross_usd": r["gross_usd"], "costs_usd": r["withholding_usd"],
                           "cash_change_usd": r["net_usd"], "source_url": r["source_url"],
                           "reason": f"dividend {r['amount']} {r['currency']}/share, ex-date {r['ex_date']}, "
                                     f"withholding tax ${r['withholding_usd']:.2f}"})
        ca.append({"key": r["key"] + ":PAID", "date": pay, "ticker": r["ticker"], "kind": "DIVIDEND_PAID",
                   "ex_date": r["ex_date"], "pay_date": pay, "amount": r["amount"], "currency": r["currency"],
                   "net_usd": r["net_usd"], "note": "moved from receivable to cash"})
    return {"ledger": new_ledger, "ca": ca, "notes": notes, "upcoming": upcoming}


def _scale_prices(h: dict, ratio: float):
    for k in ("entry_price", "last_close"):
        if h.get(k) not in ("", None):
            h[k] = round(float(h[k]) / ratio, 6)
    plan = h.get("exit_plan")
    if plan:
        for k in ("stop", "target"):
            if plan.get(k) not in ("", None):
                plan[k] = round(float(plan[k]) / ratio, 4)


def splits(state: dict, done: set, mkt, asof: str, stats_fn) -> dict:
    """Apply splits of held (and baseline) stocks dated after their entry and before asof. Mutates state.
    Raises DataError when Yahoo and stockanalysis.com disagree, so the re-pricing never runs on a wrong count."""
    new_ledger, ca = [], []
    b = state.get("baseline") or {"holdings": {}}
    for t in list(dict.fromkeys(list(state["holdings"]) + list(b["holdings"]))):
        h = state["holdings"].get(t)
        after = (h.get("entry_close_date") or h.get("entry_date")) if h else b.get("start", "")
        hist = mkt.history(t)
        rows = hist.get("all_rows", hist["rows"])
        found = [(r["date"], r["split"]) for r in rows
                 if r.get("split") and after < r["date"] < asof and f"SPLIT:{t}:{r['date']}" not in done]
        if hist.get("source") == "yfinance" and not found:
            continue
        st = parse_split_stats(stats_fn(t))  # confirm Yahoo's split, or detect one when Yahoo wasn't the source
        if hist.get("source") == "yfinance":
            for day, ratio in found:
                if not st or st[0] != day or abs(st[1] - ratio) > 1e-6:
                    raise DataError(hist["url"], "split",
                                    f"{t}: Yahoo shows a {ratio:g}-for-1 split on {day}, stockanalysis.com shows "
                                    f"{'none' if not st else f'{st[1]:g}-for-1 on {st[0]}'} -- STOP, check by hand")
        else:
            found = [st] if st and after < st[0] < asof and f"SPLIT:{t}:{st[0]}" not in done else []
        for day, ratio in found:
            key = f"SPLIT:{t}:{day}"
            px = mkt.quote(t, day)["price_usd"]  # the first post-split close (history is split-adjusted)
            if h:
                old = h["shares"]
                whole = math.floor(old * ratio + 1e-9)
                frac_cash = round((old * ratio - whole) * px, 2)
                h["shares"] = whole
                _scale_prices(h, ratio)
                if frac_cash:
                    state["cash_usd"] = round(state["cash_usd"] + frac_cash, 2)
                    state["flows"][h["type"]]["out"] += frac_cash
                new_ledger.append({"date": day, "ticker": t, "type": h["type"], "side": "SPLIT",
                                   "shares": whole - old, "fill_price": round(px, 4), "currency": "USD",
                                   "fill_close_date": day, "gross_usd": 0, "costs_usd": 0,
                                   "cash_change_usd": frac_cash, "source_url": hist["url"],
                                   "reason": f"{ratio:g}-for-1 split: {old} -> {whole} shares"
                                             + (f", fraction paid in cash ${frac_cash:.2f}" if frac_cash else "")})
            if t in b["holdings"]:
                bo = b["holdings"][t]["shares"]
                bw = math.floor(bo * ratio + 1e-9)
                b["holdings"][t]["shares"] = bw
                b["cash_usd"] += (bo * ratio - bw) * px
            done.add(key)
            ca.append({"key": key, "date": day, "ticker": t, "kind": "SPLIT", "ratio": ratio,
                       "shares": (h["shares"] if h else ""), "source_url": hist["url"],
                       "note": "confirmed on the stockanalysis.com statistics page"})
    return {"ledger": new_ledger, "ca": ca}


def check(state: dict, ledger: list[dict], ca_rows: list[dict], mkt, cfg: dict, asof: str,
          dividend_fn, stats_fn) -> dict:
    """Splits first (so dividend entitlement sees the new share count), then dividends. Mutates state."""
    done = {r["key"] for r in ca_rows} | {r["key"] for r in state.get("receivables", [])}  # never twice
    sp = splits(state, done, mkt, asof, stats_fn)
    dv = dividends(state, ledger + sp["ledger"], done, mkt, cfg, asof, dividend_fn)
    return {"ledger": sp["ledger"] + dv["ledger"], "ca": sp["ca"] + dv["ca"], "notes": dv["notes"],
            "upcoming": dv["upcoming"]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check"])
    ap.add_argument("--asof", default=(dt.date.today() + dt.timedelta(days=1)).isoformat())
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    cfg = load_config()
    from fetch_data import Fetcher
    from portfolio import LEDGER_COLS, PORT, Market, append_csv, atomic_write, load_state, price_provider, read_csv
    mkt = Market(Fetcher(cfg, refresh=True), a.asof, cfg, price_provider(cfg))
    state = load_state(PORT / "state.json", cfg)
    ledger = read_csv(PORT / "ledger.csv")

    def dividend_fn(t):
        s = mkt.f.section(t, "dividend")
        return {"url": s["source_url"], "rows": s["data"]["rows"]}

    try:
        out = check(state, ledger, read_csv(PORT / "corporate_actions.csv"), mkt, cfg, a.asof, dividend_fn,
                    lambda t: mkt.f.section(t, "statistics")["data"])
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    if not a.dry_run:
        if out["ca"]:
            atomic_write(PORT / "state.json", json.dumps(state, indent=1, sort_keys=True))
            append_csv(PORT / "ledger.csv", LEDGER_COLS, out["ledger"])
            append_csv(PORT / "corporate_actions.csv", CA_COLS, out["ca"])
    print(json.dumps({"dry_run": a.dry_run, "applied": [{k: r.get(k) for k in ("kind", "ticker", "date", "ratio", "net_usd")
                                                          if r.get(k) not in ("", None)} for r in out["ca"]],
                      "receivables": [{k: r[k] for k in ("ticker", "ex_date", "pay_date", "net_usd")}
                                      for r in state.get("receivables", [])],
                      "upcoming": out["upcoming"], "notes": out["notes"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
