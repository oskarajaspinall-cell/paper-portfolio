"""Dip radar (design by Claude, owner request 2026-10-19: "identify when it's a good opportunity to buy stocks when
they dip"). Daily, no AI. Finds stocks we already know that have fallen in a way worth a fresh look, and queues the
best few for re-research. A dip is never a buy on its own: the re-research decides, and every rule still applies.

Watched: CORE holdings (an ADD question) and every stock whose latest decision was AVOID at conviction >=
[dip].min_conviction within [dip].watch_days (including the ones whose evaluator said "price is not the obstacle",
which have no entry price and so are invisible to scripts/entry_watch.py).

For each, from daily closes (the portfolio's price source, as entry_watch): the stock's beta to the S&P 500 (SPY),
its return since our last research (at most `lookback_sessions`) split into the market's part (beta x SPY) and the stock-specific part, and that
stock-specific move in standard deviations of its own daily residuals (z). A signal needs
  - an unusual stock-specific fall: z <= z_threshold, or, while a market dip releases the cash reserve, a fall of
    at least market_dip_from_decision_pct since our decision (a market-driven dip in a name we liked), AND
  - value support: the close at or below the latest base fair value (no fair value: down >= no_fv_drop_pct since
    the decision), AND
  - the fall happened AFTER our last research (the window starts there, at most lookback_sessions, at least
    min_sessions): a fall the last evaluation already saw is not news.
Signals are ranked (biggest stock-specific fall in z first, then discount to the bear fair value) and the top
max_hits_per_day go to state["dip_hits"]; the next intraday window re-researches them (scripts/entry_research.py),
as do the research loop and the weekly run. Everything is listed in reports/dip-radar/<date>.md.

    python scripts/dip_radar.py [--asof YYYY-MM-DD] [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

OUT = ROOT / "reports" / "dip-radar"


def settings(cfg: dict) -> dict:
    d = cfg.get("dip") or {}
    return {"z_threshold": float(d.get("z_threshold", -2.0)), "lookback": int(d.get("lookback_sessions", 20)),
            "watch_days": int(d.get("watch_days", 120)), "min_conviction": int(d.get("min_conviction", 3)),
            "market_dip_pct": float(d.get("market_dip_from_decision_pct", -10)),
            "no_fv_drop_pct": float(d.get("no_fv_drop_pct", -15)),
            "max_hits": int(d.get("max_hits_per_day", 3)), "beta_sessions": int(d.get("beta_sessions", 120)),
            "min_sessions": int(d.get("min_sessions", 5))}


def watch_list(state: dict, decisions: list[dict], asof: str, st: dict) -> list[dict]:
    """[{ticker, kind: holding|avoid, decision, conviction, price, currency, date, evaluation}]"""
    out = []
    for t, h in state.get("holdings", {}).items():
        if h["type"] == "CORE":
            out.append({"ticker": t, "kind": "holding", "decision": "HOLD", "conviction": h.get("conviction"),
                        "price": h.get("entry_price"), "currency": h.get("currency"), "date": h.get("entry_date")})
    latest: dict[str, dict] = {}
    for r in decisions:
        latest[r["ticker"]] = r
    since = (dt.date.fromisoformat(asof) - dt.timedelta(days=st["watch_days"])).isoformat()
    queued = {e["ticker"] for e in state.get("funding_queue") or []}
    for t, r in latest.items():
        if t in state.get("holdings", {}) or t in queued or r["decision"] != "AVOID" or r["date"] < since:
            continue
        try:
            conv = int(float(r["conviction"]))
        except (TypeError, ValueError):
            continue
        if conv < st["min_conviction"] or r.get("type", "CORE") != "CORE":
            continue
        out.append({"ticker": t, "kind": "avoid", "decision": "AVOID", "conviction": conv,
                    "price": float(r["price"]) if r.get("price") else None, "currency": r.get("currency"),
                    "date": r["date"], "evaluation": r.get("evaluation")})
    return out


def _returns(rows: list[dict]) -> dict[str, float]:
    out = {}
    for a, b in zip(rows, rows[1:]):
        if a.get("close") and b.get("close"):
            out[b["date"]] = b["close"] / a["close"] - 1
    return out


def move_stats(rows: list[dict], spy_rows: list[dict], lookback: int, beta_sessions: int, since: str | None = None,
               min_sessions: int = 5) -> dict | None:
    """Beta, the return since `since` (our last research; at most `lookback` sessions) split into market and
    stock-specific parts, and z of the stock-specific part. A fall our last research already saw doesn't count;
    fewer than `min_sessions` since then -> z None."""
    rows = [r for r in rows if r.get("close")]
    if len(rows) < lookback + 40:
        return None
    rs, rm = _returns(rows), _returns(spy_rows)
    days = [d for d in rs if d in rm]
    est = days[-(beta_sessions + lookback):-lookback] if len(days) > beta_sessions + lookback else days[:-lookback]
    if len(est) < 40:
        return None
    x, y = [rm[d] for d in est], [rs[d] for d in est]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    vx = sum((a - mx) ** 2 for a in x)
    beta = sum((a - mx) * (b - my) for a, b in zip(x, y)) / vx if vx else 1.0
    resid = [b - beta * a for a, b in zip(x, y)]
    mr = sum(resid) / len(resid)
    sd = math.sqrt(sum((e - mr) ** 2 for e in resid) / (len(resid) - 1))
    win = [d for d in days if since is None or d > since][-lookback:]
    if len(win) < min_sessions:
        return {"beta": round(beta, 2), "z": None, "sessions": len(win), "close": rows[-1]["close"],
                "close_date": rows[-1]["date"], "ret_pct": None, "spy_pct": None, "market_part_pct": None,
                "specific_pct": None, "off_3m_high_pct": None}
    r_stock = math.prod(1 + rs[d] for d in win) - 1
    r_mkt = math.prod(1 + rm[d] for d in win) - 1
    idio = r_stock - beta * r_mkt
    hi = max(r["close"] for r in rows[-63:])
    return {"beta": round(beta, 2), "ret_pct": round(r_stock * 100, 2), "spy_pct": round(r_mkt * 100, 2),
            "market_part_pct": round(beta * r_mkt * 100, 2), "specific_pct": round(idio * 100, 2),
            "z": round(idio / (sd * math.sqrt(len(win))), 2) if sd else None, "sessions": len(win),
            "from_date": win[0],
            "off_3m_high_pct": round((rows[-1]["close"] / hi - 1) * 100, 2),
            "close": rows[-1]["close"], "close_date": rows[-1]["date"]}


def latest_valuation(ticker: str, on_or_before: str) -> dict:
    d = ROOT / "research" / Ticker(ticker).slug
    files = sorted(p for p in d.glob("20??-??-??-valuation.json") if p.name[:10] <= on_or_before)
    return json.loads(files[-1].read_text()) if files else {}


def last_research(ticker: str) -> str | None:
    d = ROOT / "research" / Ticker(ticker).slug
    evs = sorted(p.name[:10] for p in d.glob("20??-??-??-evaluation.md"))
    return evs[-1] if evs else None


def assess(w: dict, m: dict, fv: dict, st: dict, dip_released: bool, asof: str) -> dict:
    """The watch row + stats + verdict: signal (bool) and why / why not."""
    c = m["close"]
    base, bear = fv.get("base"), fv.get("bear")
    from_dec = (c / w["price"] - 1) * 100 if w.get("price") else None
    out = {**w, **m, "fair_value_base": base, "fair_value_bear": bear,
           "from_decision_pct": None if from_dec is None else round(from_dec, 2),
           "vs_base_pct": None if not base else round((c / base - 1) * 100, 2),
           "vs_bear_pct": None if not bear else round((c / bear - 1) * 100, 2)}
    unusual = m["z"] is not None and m["z"] <= st["z_threshold"]
    market = dip_released and from_dec is not None and from_dec <= st["market_dip_pct"]
    if base:
        value = c <= base
    else:
        value = from_dec is not None and from_dec <= st["no_fv_drop_pct"]
    why = []
    if m["z"] is None:
        why.append(f"only {m['sessions']} session(s) since our last research")
    elif not (unusual or market):
        why.append(f"no unusual fall since our last research (z {m['z']})")
    if not value:
        why.append("above base fair value" if base else "not down enough with no fair value")
    out.update(signal=not why, cause=("stock-specific" if unusual else "market dip" if market else ""),
               why_not="; ".join(why))
    return out


def rank_key(a: dict):
    return (a["z"] if a["z"] is not None else 0, a["vs_bear_pct"] if a["vs_bear_pct"] is not None else 0)


def hit_reason(a: dict) -> str:
    """The re-research instruction for a dip-radar signal (used by entry_research / weekly run / research loop)."""
    fv = (f"; base fair value {a['fair_value_base']:.2f}" if a.get("fair_value_base") else "; no mechanical fair value")
    head = (f"Dip radar: the close {a['close']:g} ({a['close_date']}) is {a['ret_pct']:+.1f}% over the "
            f"{a['sessions']} sessions since our last research ({a.get('last_research') or 'n/a'}) vs the S&P 500 "
            f"{a['spy_pct']:+.1f}% (beta {a['beta']}); the stock-specific "
            f"part is {a['specific_pct']:+.1f}% ({a['z']} standard deviations)"
            + (f"; {a['from_decision_pct']:+.1f}% since our {a['decision']} at conviction {a['conviction']} on {a['date']}"
               if a.get("from_decision_pct") is not None else "") + fv + ". ")
    if a["kind"] == "holding":
        return head + ("This is a full re-initiation of an existing CORE holding. Find out why it fell (results, "
                       "guidance, filings, news): if the thesis is intact and the fall is an overreaction, ADD is the "
                       "question; if the fall reveals a thesis problem, say so. Decide ADD, HOLD, TRIM or SELL.")
    return head + ("Find out why it fell (results, guidance, filings, news). Decide BUY or AVOID: BUY only if the fall "
                   "is an overreaction to something that doesn't break the business case, or it removed the "
                   "obstacle that made it an AVOID; a falling price alone is not a reason.")


def render(asof: str, assessed: list[dict], hits: list[dict], dip_released: bool, failed: list[str]) -> str:
    sig = [a for a in assessed if a["signal"]]
    f = lambda x, s="": "" if x is None else f"{x:+.1f}{s}"  # noqa: E731
    L = [f"# Dip radar — {asof}", "",
         f"{len(assessed)} stocks watched (CORE holdings + conviction-3+ AVOIDs from the last 120 days); "
         f"{len(sig)} signal(s); {len(hits)} queued for re-research"
         + (" (market dip: the cash reserve is being released)" if dip_released else "") + ".",
         "A signal = an unusual stock-specific fall (or a market dip in a name we liked) with the price at or below "
         "base fair value. Never a buy on its own: the re-research decides.", ""]
    if sig:
        L += ["| Stock | Kind | Queued | Return since research | S&P part | Stock-specific | z | Since decision | vs base FV | vs bear FV |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        q = {h["ticker"] for h in hits}
        for a in sig:
            L.append(f"| {a['ticker']} | {a['kind']} | {'yes' if a['ticker'] in q else 'next days'} | {f(a['ret_pct'], '%')} | "
                     f"{f(a['market_part_pct'], '%')} | {f(a['specific_pct'], '%')} | {a['z']} | {f(a['from_decision_pct'], '%')} | "
                     f"{f(a['vs_base_pct'], '%')} | {f(a['vs_bear_pct'], '%')} |")
    near = sorted((a for a in assessed if not a["signal"] and a["z"] is not None and a["z"] <= -1.5), key=rank_key)[:10]
    if near:
        L += ["", "Close to a signal (z <= -1.5):", ""] + [f"- {a['ticker']}: z {a['z']}, {a['why_not']}" for a in near]
    if failed:
        L += ["", f"No price data for {len(failed)}: " + ", ".join(failed[:30])]
    return "\n".join(L) + "\n"


def pending_hits(state: dict) -> list[dict]:
    """Dip hits not yet re-researched (any route: intraday job, weekly run, research loop) since they were found."""
    return [h for h in state.get("dip_hits") or [] if (last_research(h["ticker"]) or "") < h["hit_date"]]


def run(state: dict, decisions: list[dict], mkt, cfg: dict, asof: str, dip_released: bool) -> tuple[list, list, list]:
    st = settings(cfg)
    spy = mkt.history("SPY")["all_rows"]
    spy = [r for r in spy if r["date"] < asof]
    assessed, failed = [], []
    for w in watch_list(state, decisions, asof, st):
        try:
            rows = [r for r in mkt.history(w["ticker"])["all_rows"] if r["date"] < asof]
        except DataError:
            failed.append(w["ticker"])
            continue
        last = last_research(w["ticker"])
        m = move_stats(rows, spy, st["lookback"], st["beta_sessions"], last, st["min_sessions"])
        if not m:
            failed.append(w["ticker"])
            continue
        fv = (latest_valuation(w["ticker"], asof).get("fair_value") or {})
        a = assess(w, m, fv, st, dip_released, asof)
        a["last_research"] = last
        assessed.append(a)
    sig = sorted((a for a in assessed if a["signal"]), key=rank_key)
    already = {h["ticker"] for h in pending_hits(state)}
    hits = [{"ticker": a["ticker"], "kind": "dip", "holding": a["kind"] == "holding", "hit_date": asof,
             "close": a["close"], "z": a["z"], "reason": hit_reason(a)}
            for a in sig if a["ticker"] not in already][:st["max_hits"]]
    return assessed, hits, failed


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    cfg = load_config()
    from fetch_data import Fetcher
    from portfolio import Market, current_reserve, price_provider
    from prices import YahooPrices
    pp = price_provider(cfg)
    if isinstance(pp, YahooPrices):
        pp = YahooPrices(period="1y")  # beta needs ~140 sessions before the lookback window
    mkt = Market(Fetcher(cfg), a.asof, cfg, pp)
    sp = ROOT / "portfolio" / "state.json"
    state = json.loads(sp.read_text())
    with (ROOT / "portfolio" / "decisions.csv").open() as fh:
        decisions = list(csv.DictReader(fh))
    released = current_reserve(cfg, a.asof).get("dip_multiplier", 1.0) < 1
    try:
        assessed, hits, failed = run(state, decisions, mkt, cfg, a.asof, released)
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    md = render(a.asof, assessed, hits, released, failed)
    if not a.dry_run:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{a.asof}.md").write_text(md)
        (OUT / f"{a.asof}.json").write_text(json.dumps({"asof": a.asof, "assessed": assessed, "hits": hits,
                                                         "failed": failed}, indent=1, default=str))
        state = json.loads(sp.read_text())
        kept = pending_hits(state)
        if hits or len(kept) != len(state.get("dip_hits") or []):
            state["dip_hits"] = kept + hits
            tmp = sp.with_suffix(".tmp")
            tmp.write_text(json.dumps(state, indent=1, sort_keys=True))
            tmp.replace(sp)
    print(json.dumps({"asof": a.asof, "watched": len(assessed), "signals": sum(x["signal"] for x in assessed),
                      "queued": [h["ticker"] for h in hits], "no_data": len(failed)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
