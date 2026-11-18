"""Shadow short book (owner 2026-11-18). SHADOW ONLY: positions are recorded and marked, never traded; nothing
here touches portfolio/state.json, cash or the ledger.

    python scripts/shadow_shorts.py run [--asof D] [--no-agent]

Each night: (1) the short screen (scripts/short_screen.py); (2) open positions are marked and closed on an exit
rule; (3) a qualifying candidate gets a fresh fact sheet and the short-evaluator agent while a slot is free
([short].max_open, one per industry, not re-evaluated within 30 days); a SHORT verdict at conviction
[short].min_short_conviction+ opens a position. A position is a bought put (90-180 days out, strike nearest the money,
premium [short].premium_pct of the portfolio) where a listed, liquid chain exists, and always the same-money short of
the stock against its US sector ETF, so the stock call is judged apart from the option's cost.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

BOOK = ROOT / "portfolio" / "shadow_shorts.csv"
COLS = ["id", "ticker", "status", "opened", "evaluation", "confidence", "short_conviction", "industry", "currency",
        "entry_close", "sector_etf", "etf_entry", "borrow_fee_pct", "put_underlying", "put_contract", "put_expiry", "put_strike", "contracts", "put_entry_mid",
        "put_bid", "put_ask", "put_iv", "premium_usd", "notional_usd", "last_date", "last_close", "etf_last",
        "put_last_mid", "sector", "alt_exits", "stock_ret_pct", "etf_ret_pct", "stock_vs_etf_pct", "borrow_cost_pct", "short_net_pct", "put_pnl_usd", "closed", "close_reason"]
SECTOR_ETF = {"Technology": "XLK", "Financials": "XLF", "Healthcare": "XLV", "Energy": "XLE", "Industrials": "XLI",
              "Consumer Discretionary": "XLY", "Consumer Staples": "XLP", "Utilities": "XLU", "Real Estate": "XLRE",
              "Materials": "XLB", "Basic Materials": "XLB", "Communication Services": "XLC"}


def read(path: Path = BOOK) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


def write(rows: list[dict], path: Path = BOOK) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in COLS})
    tmp.replace(path)


# ------------------------------------------------------------------ options (yfinance; US-listed chains only)
def pick_expiry(expiries: list[str], asof: str) -> str | None:
    """The first expiry 90-180 days out, else the nearest beyond 90 days."""
    d0 = dt.date.fromisoformat(asof)
    days = [(e, (dt.date.fromisoformat(e) - d0).days) for e in expiries]
    inside = [e for e, n in days if 90 <= n <= 180]
    beyond = [e for e, n in days if n > 90]
    return (inside or beyond or [None])[0]


def iv_rank(iv: float, closes: list[float]) -> float | None:
    """Where today's implied vol sits among the stock's 30-day realised vols over the last year (0-100).
    shortcut: realised vol stands in for the option's own IV history, which Yahoo does not keep; switch if a source does."""
    rets = [math.log(b / a) for a, b in zip(closes[-253:-1], closes[-252:]) if a > 0 and b > 0]
    vols = [(sum(x * x for x in rets[i - 30:i]) / 30) ** 0.5 * math.sqrt(252) for i in range(30, len(rets) + 1)]
    return None if not vols else 100 * sum(v < iv for v in vols) / len(vols)


def price_put(ticker: str, close: float, asof: str, closes: list[float], cfg: dict, loader=None,
              adr: str | None = None) -> dict | None:
    """The put to record, or None (no listed chain, too thin, or implied vol too high: the stock record stays).
    A foreign stock uses its US-listed share's chain (`adr`, with that share's own price and history)."""
    s = cfg["short"]
    from prices import yahoo_symbol
    sym = adr or (yahoo_symbol(ticker) if not Ticker(ticker).exchange else None)  # listed US chains only
    if not sym:
        return None
    try:
        if loader:
            expiries, chain_for = loader(sym)
        else:
            import yfinance as yf
            t = yf.Ticker(sym)
            expiries, chain_for = list(t.options), (lambda e: t.option_chain(e).puts)
        exp = pick_expiry(expiries, asof)
        if not exp:
            return None
        puts = chain_for(exp)
        row = min(puts.to_dict("records"), key=lambda r: abs(r["strike"] - close))
    except Exception:  # noqa: BLE001  no chain: the stock-vs-ETF record still opens
        return None
    bid, ask, oi, iv = row.get("bid") or 0, row.get("ask") or 0, row.get("openInterest") or 0, row.get("impliedVolatility")
    if bid <= 0 or ask <= 0 or oi < s["min_open_interest"]:
        return None
    rank = iv_rank(iv, closes) if iv else None
    if rank is not None and rank > s["max_iv_pct_rank"]:
        return None
    return {"underlying": sym, "contract": row.get("contractSymbol", ""), "expiry": exp, "strike": row["strike"], "bid": bid, "ask": ask,
            "mid": (bid + ask) / 2, "iv": iv}


def put_mark(underlying: str, contract: str, expiry: str, strike: float, close: float, asof: str, loader=None) -> float:
    """Today's mid for the recorded contract; its intrinsic value once expired or no longer quoted."""
    if asof < expiry:
        try:
            if loader:
                return loader(contract)
            import yfinance as yf
            puts = yf.Ticker(underlying).option_chain(expiry).puts
            r = puts[puts["contractSymbol"] == contract].iloc[0]
            if r["bid"] > 0 and r["ask"] > 0:
                return float((r["bid"] + r["ask"]) / 2)
        except Exception:  # noqa: BLE001
            pass
    return max(0.0, strike - close)


# ------------------------------------------------------------------ positions
def exit_reason(row: dict, close: float, asof: str, falsifier_hits: list[str], cfg: dict) -> str:
    """The position's own exit: a falsifier, the stop or the time limit. (2026-11-18: no fair-value target: a DCF on
    peak earnings puts fair value ABOVE a peaking cyclical's price, so it fired on the day a short opened.)"""
    s = cfg["short"]
    if falsifier_hits:
        return "falsifier: " + falsifier_hits[0][:80]
    if close >= float(row["entry_close"]) * (1 + s["stop_pct"] / 100):
        return f"stop: {s['stop_pct']:g}% above entry"
    if row.get("put_expiry") and (dt.date.fromisoformat(row["put_expiry"]) - dt.date.fromisoformat(asof)).days <= s["min_days_to_expiry"]:
        return "time: put near expiry"
    if not row.get("put_expiry") and (dt.date.fromisoformat(asof) - dt.date.fromisoformat(row["opened"])).days >= 180:
        return "time: 180 days"
    return ""


ALT_RULES = {"trend": "back above a rising 50-day average", "trail_atr": "trailing stop: lowest close + 2.5 x ATR",
             "take15": "profit-take at +15 points vs the sector", "take25": "profit-take at +25 points vs the sector",
             "hold": "hold to the time limit"}


def horizon_end(row: dict, cfg: dict) -> str:
    """The time limit every rule is judged to: the put's expiry less min_days_to_expiry, else 180 days."""
    if row.get("put_expiry"):
        return (dt.date.fromisoformat(row["put_expiry"]) - dt.timedelta(days=cfg["short"]["min_days_to_expiry"])).isoformat()
    return (dt.date.fromisoformat(row["opened"]) + dt.timedelta(days=180)).isoformat()


def alt_exits(rows: list[dict], etf: dict[str, float], opened: str, end: str, cfg: dict) -> dict:
    """What each candidate exit rule would have made on this position (owner 2026-11-18: compare exit rules, and by
    sector, before choosing one). Result = the short's gain vs the sector ETF in points (+ = the short won), at the
    rule's first trigger, else at the latest close up to `end` (still held). Judged independently of the real exit."""
    from setups import atr
    rows = [r for r in rows if r.get("close") and r["date"] <= end]
    i0 = next((i for i, r in enumerate(rows) if r["date"] >= opened), None)
    if i0 is None or not etf:
        return {}
    e_on = lambda d: etf.get(d) or etf[max([k for k in etf if k <= d] or [min(etf)])]  # noqa: E731
    p0, e0 = rows[i0]["close"], e_on(rows[i0]["date"])
    res = lambda i: round(-((rows[i]["close"] / p0 - 1) - (e_on(rows[i]["date"]) / e0 - 1)) * 100, 2)  # noqa: E731
    a = atr(rows[:i0 + 1]) or 0
    k, out, low = cfg["short"].get("trail_atr_multiple", 2.5), {}, p0
    closes = [r["close"] for r in rows]
    for i in range(i0 + 1, len(rows)):
        c, r, d = closes[i], res(i), rows[i]["date"]
        low = min(low, c)
        sma, sma5 = (sum(closes[i - 49:i + 1]) / 50, sum(closes[i - 54:i - 4]) / 50) if i >= 54 else (None, None)
        hits = {"trend": sma is not None and c > sma > sma5, "trail_atr": a > 0 and c >= low + k * a,
                "take15": r >= 15, "take25": r >= 25}
        for rule, hit in hits.items():
            if hit and rule not in out:
                out[rule] = {"date": d, "result": r, "fired": True}
    last = len(rows) - 1
    for rule in ALT_RULES:
        out.setdefault(rule, {"date": rows[last]["date"], "result": res(last), "fired": False})
    return out


def alt_summary(book: list[dict]) -> dict:
    """Median result per exit rule, overall and by sector, across every position (fired or still held)."""
    import statistics as st
    by: dict = {}
    for r in book:
        alt = json.loads(r.get("alt_exits") or "{}")
        for rule, v in alt.items():
            for grp in ("All", r.get("sector") or "Unknown"):
                by.setdefault(grp, {}).setdefault(rule, []).append(v["result"])
    return {g: {rule: {"n": len(v), "median": round(st.median(v), 2)} for rule, v in rules.items()} for g, rules in by.items()}


def mark(row: dict, close: float, etf: float, asof: str, put_mid: float | None) -> None:
    sr = close / float(row["entry_close"]) - 1
    er = etf / float(row["etf_entry"]) - 1
    days = (dt.date.fromisoformat(asof) - dt.date.fromisoformat(row["opened"])).days
    borrow = float(row.get("borrow_fee_pct") or 0) * days / 365
    # short_net_pct: what shorting the stock against its sector fund made, after the borrowing fee (+ = the short won)
    row.update(last_date=asof, last_close=round(close, 4), etf_last=round(etf, 4), stock_ret_pct=round(sr * 100, 2),
               etf_ret_pct=round(er * 100, 2), stock_vs_etf_pct=round((sr - er) * 100, 2),
               borrow_cost_pct=round(borrow, 2), short_net_pct=round(-(sr - er) * 100 - borrow, 2))
    if put_mid is not None and row.get("contracts"):
        row.update(put_last_mid=round(put_mid, 4),
                   put_pnl_usd=round((put_mid - float(row["put_entry_mid"])) * 100 * int(row["contracts"]), 2))


def new_position(cand: dict, decision: dict, eval_rel: str, close_q: dict, etf_sym: str, etf_close: float,
                 put: dict | None, portfolio_usd: float, asof: str, cfg: dict) -> dict:
    budget = cfg["short"]["premium_pct"] / 100 * portfolio_usd
    row = {"id": f"{asof}-{cand['ticker']}", "ticker": cand["ticker"], "status": "open", "opened": asof,
           "evaluation": eval_rel, "confidence": cand["confidence"], "short_conviction": decision["conviction"],
           "industry": cand.get("industry", ""), "currency": close_q["currency"], "entry_close": close_q["close"],
           "sector_etf": etf_sym, "etf_entry": etf_close, "notional_usd": round(budget, 2),
           "borrow_fee_pct": cfg["short"]["borrow_fee_hard_pct"] if (cand.get("short_interest") or 0) >= 10
           else cfg["short"]["borrow_fee_pct"]}
    if put:
        n = max(1, int(budget // (put["mid"] * 100)))
        row.update(put_underlying=put["underlying"], put_contract=put["contract"], put_expiry=put["expiry"], put_strike=put["strike"], contracts=n,
                   put_entry_mid=round(put["mid"], 4), put_bid=put["bid"], put_ask=put["ask"],
                   put_iv=round(put["iv"] or 0, 4), premium_usd=round(n * put["mid"] * 100, 2))
    return row


def evaluate(cand: dict, asof: str, log) -> tuple[dict | None, str]:
    """A fresh fact sheet, then the short-evaluator agent; returns (decision block, evaluation path)."""
    slug = Ticker(cand["ticker"]).slug
    subprocess.run([str(ROOT / "bin" / "py"), "scripts/fact_sheet.py", cand["ticker"], "--asof", asof], cwd=ROOT,
                   capture_output=True, timeout=900)
    ev = ROOT / cand["evaluation"]
    out = f"research/{slug}/{asof}-short-evaluation.md"
    prompt = (f"Ticker {cand['ticker']}. Date {asof}. Fact sheet: research/{slug}/factsheet-{asof}.md. Latest research: "
              f"{ev.parent.relative_to(ROOT)}/{ev.name[:10]}.md and {cand['evaluation']}. Write {out}.")
    from weekly_run import claude_agent
    claude_agent("short-evaluator", prompt, log)
    chk = subprocess.run([str(ROOT / "bin" / "py"), "scripts/check_docs.py", "short", out], cwd=ROOT,
                         capture_output=True, text=True)
    if chk.returncode != 0:
        log(f"!! short evaluation for {cand['ticker']} failed its check: {chk.stdout[-300:]}")
        return None, out
    from decision_log import decision_from_eval
    return decision_from_eval((ROOT / out).read_text()), out


def run(asof: str, cfg: dict, mkt, agent: bool, log=print) -> dict:
    import short_screen
    from weekly_scan import trigger_hits
    s = cfg["short"]
    cands = short_screen.screen(asof, cfg, mkt)
    short_screen.OUT.mkdir(parents=True, exist_ok=True)
    (short_screen.OUT / f"{asof}.json").write_text(json.dumps({"asof": asof, "candidates": cands}, indent=1))
    (short_screen.OUT / f"{asof}.md").write_text(short_screen.render_md(asof, cands, cfg))
    rows, opened, closed = read(), [], []
    for r in rows:  # every exit rule is followed to the time limit, also after the position's own exit
        if asof <= horizon_end(r, cfg) or not r.get("alt_exits"):
            try:
                hist = mkt.history(r["ticker"])["rows"]
                etf = {x["date"]: x["close"] for x in mkt.history(r["sector_etf"])["rows"] if x.get("close")}
                r["alt_exits"] = json.dumps(alt_exits(hist, etf, r["opened"], min(asof, horizon_end(r, cfg)), cfg))
            except DataError:
                pass
    for r in rows:  # mark and close
        if r["status"] != "open":
            continue
        try:
            q, e = mkt.quote(r["ticker"], asof), mkt.quote(r["sector_etf"], asof)
        except DataError:
            continue
        pm = put_mark(r.get("put_underlying") or r["ticker"], r["put_contract"], r["put_expiry"], float(r["put_strike"]), q["close"], asof) if r.get("put_contract") else None
        mark(r, q["close"], e["close"], asof, pm)
        hits = []
        ev = ROOT / r["evaluation"]
        if ev.exists():
            from decision_log import decision_from_eval
            try:
                stats = mkt.f.section(r["ticker"], "statistics")["data"]
                hits = [h["text"] for h in trigger_hits(decision_from_eval(ev.read_text()).get("falsifiers"), stats)[0]]
            except (DataError, KeyError, ValueError):
                pass
        why = exit_reason(r, q["close"], asof, hits, cfg)
        if why:
            r.update(status="closed", closed=asof, close_reason=why)
            closed.append(r["ticker"])
    open_rows = [r for r in rows if r["status"] == "open"]
    recent = {r["ticker"] for r in rows if r["opened"] >= (dt.date.fromisoformat(asof) - dt.timedelta(days=30)).isoformat()}
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    from portfolio import totals
    pv = totals(state)["total"]
    for c in [c for c in cands if c["qualifies"]]:
        if len(open_rows) >= s["max_open"] or c["ticker"] in recent or c["industry"] in {r["industry"] for r in open_rows}:
            continue
        slug = Ticker(c["ticker"]).slug
        done = sorted((ROOT / "research" / slug).glob("*-short-evaluation.md"))
        if done and done[-1].name[:10] >= (dt.date.fromisoformat(asof) - dt.timedelta(days=30)).isoformat():
            continue  # evaluated within 30 days: not again
        if not agent:
            log(f"would evaluate {c['ticker']} (confidence {c['confidence']})")
            continue
        d, path = evaluate(c, asof, log)
        if not d or d.get("decision") != "SHORT" or int(d.get("conviction") or 0) < s["min_short_conviction"]:
            log(f"{c['ticker']}: no shadow short ({'evaluation failed' if not d else d.get('decision')} {d and d.get('conviction')})")
            continue
        q = mkt.quote(c["ticker"], asof)
        from calibration import sector_of
        sector = sector_of(c["ticker"]) or ""
        etf = SECTOR_ETF.get(sector, "SPY")  # shortcut: a US sector ETF even for foreign stocks
        und = c.get("adr")
        hq = mkt.quote(und, asof) if und else q  # a foreign stock's put sits on its US share, at that share's price
        closes = [x["close"] for x in mkt.history(und or c["ticker"])["rows"] if x.get("close")]
        put = price_put(c["ticker"], hq["close"], asof, closes, cfg, adr=und)
        row = new_position(c, d, path, q, etf, mkt.quote(etf, asof)["close"], put, pv, asof, cfg)
        row["sector"] = sector
        rows.append(row)
        open_rows.append(row)
        opened.append(c["ticker"])
    write(rows)
    return {"candidates": len(cands), "qualify": [c["ticker"] for c in cands if c["qualifies"]], "opened": opened,
            "closed": closed, "open": [r["ticker"] for r in rows if r["status"] == "open"]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run"])
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--no-agent", action="store_true", help="screen and mark only; no short evaluation (no model call)")
    a = ap.parse_args(argv)
    cfg = load_config()
    from fetch_data import Fetcher
    from portfolio import Market, price_provider
    mkt = Market(Fetcher(cfg), a.asof, cfg, price_provider(cfg))
    print(json.dumps(run(a.asof, cfg, mkt, not a.no_agent)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
