"""Funding queue (design by Claude 2026-10-18, owner-approved): a conviction-4+ CORE BUY rejected only because
it would take cash below the regime reserve (or the cash floor) waits here instead of being lost. No AI.

- Added automatically by `portfolio.place_orders` / `fill_pending` when such a rejection happens; it keeps the
  full trade request, the close it was decided at and the evaluation's base fair value.
- `review` (weekdays, bin/fill-pending; and at the start of the weekly swap step): drops an idea that is now
  held or ordered, older than `[funding_queue].max_days`, or whose close rose more than `max_rise_pct` above the
  decision price (the research is then too stale to act on); then resubmits the waiting ideas best base-fair-value
  upside first. An idea that now fits is queued for the next open with every rule checked again; one that still
  breaches only the cash reserve keeps waiting; any other rejection drops it.
- `brief` writes the weekly swap brief (the best waiting idea vs the weakest CORE holdings) for the
  swap-reviewer agent; a swap is an ordinary BUY with `replaces`, validated by portfolio.py like any other.
The reserve is never relaxed: a queued idea only buys with room above it, or by replacing a holding.
Events are logged in portfolio/funding_queue.csv.

    python scripts/funding_queue.py list
    python scripts/funding_queue.py review [--asof YYYY-MM-DD] [--dry-run]
    python scripts/funding_queue.py add <requests.json> [--asof YYYY-MM-DD]   (backfill a rejected BUY)
    python scripts/funding_queue.py brief --out runs/<date>/funding-queue.md [--asof YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

PORT = ROOT / "portfolio"
EVENT_COLS = ["date", "ticker", "event", "detail"]
QUEUEABLE = {"CASH_RESERVE", "CASH_MIN"}  # breaches that more cash fixes; sector / holdings caps need a sale


def settings(cfg: dict) -> dict:
    fq = cfg.get("funding_queue") or {}
    return {"max_days": int(fq.get("max_days", 30)), "max_rise_pct": float(fq.get("max_rise_pct", 10)),
            "swap_candidates": int(fq.get("swap_candidates", 3)),
            "starter_min_fraction": float(fq.get("starter_min_fraction", 0.5)),
            "min_step_pct": float(fq.get("min_step_pct", 1.0))}


def queueable(rej: dict, req: dict | None, cfg: dict) -> bool:
    return (rej.get("rule") == "REPLACEMENT_REQUIRED" and rej.get("action") == "BUY" and rej.get("type") == "CORE"
            and bool(rej.get("breaches")) and set(rej["breaches"]) <= QUEUEABLE and req is not None
            and not req.get("replaces")
            and int(req.get("conviction") or 0) >= int(cfg["core"].get("min_buy_conviction", 4)))


def latest_valuation(ticker: str, on_or_before: str) -> tuple[dict, str] | tuple[None, None]:
    """The newest research/<slug>/<date>-valuation.json on/before the date (fair values in the quote currency)."""
    d = ROOT / "research" / Ticker(ticker).slug
    files = sorted(p for p in d.glob("20??-??-??-valuation.json") if p.name[:10] <= on_or_before)
    if not files:
        return None, None
    return json.loads(files[-1].read_text()), str(files[-1].relative_to(ROOT))


def log_events(rows: list[dict], port_dir: Path = PORT) -> None:
    from portfolio import append_csv
    append_csv(port_dir / "funding_queue.csv", EVENT_COLS, rows)


def enqueue(state: dict, rejections: list[dict], requests: list[dict], quote, cfg: dict, today: str,
            port_dir: Path = PORT) -> bool:
    """Add queueable rejections to state["funding_queue"] (in place). `quote(ticker)` gives the close used.
    Re-adding the same decision (same research note) keeps its original date and price. True if changed."""
    st, q, events = settings(cfg), state.setdefault("funding_queue", []), []
    by_ticker = {r.get("ticker"): r for r in requests}
    for rej in rejections:
        req = by_ticker.get(rej.get("ticker"))
        if not queueable(rej, req, cfg):
            continue
        t = req["ticker"]
        old = next((e for e in q if e["ticker"] == t), None)
        if old and old["request"].get("research_note") == req.get("research_note"):
            continue  # the same decision is already waiting
        try:
            qt = quote(t)
        except DataError:
            continue
        val, vpath = latest_valuation(t, today)
        fv = ((val or {}).get("fair_value") or {}).get("base")
        entry = {"ticker": t, "added": today,
                 "expires": (dt.date.fromisoformat(today) + dt.timedelta(days=st["max_days"])).isoformat(),
                 "decision_price": qt["close"], "currency": qt["currency"], "price_date": qt.get("date"),
                 "fair_value_base": fv, "valuation": vpath, "request": copy.deepcopy(req)}
        if old:
            q.remove(old)
        q.append(entry)
        events.append({"date": today, "ticker": t, "event": "ADDED",
                       "detail": f"conviction {req.get('conviction')}; {rej['detail']}"[:300]})
    if events:
        log_events(events, port_dir)
    return bool(events)


def drop_ordered(state: dict, tickers: set[str], today: str, port_dir: Path = PORT) -> bool:
    """A queued idea that got an order by any route (research loop, swap, resubmission) leaves the queue."""
    q = state.get("funding_queue") or []
    gone = [e for e in q if e["ticker"] in tickers and e.get("stage") != "topup"]
    if not gone:
        return False
    state["funding_queue"] = [e for e in q if e not in gone]
    log_events([{"date": today, "ticker": e["ticker"], "event": "ORDERED", "detail": "order placed"} for e in gone],
               port_dir)
    return True


def _upside(e: dict) -> float | None:
    fv, c = e.get("fair_value_base"), e.get("last_close") or e.get("decision_price")
    return (fv / c - 1) * 100 if fv and c else None


def _rank(q: list[dict]) -> list[dict]:
    """Top-ups of positions already started come first (finish what we started), then the best upside."""
    return sorted(q, key=lambda e: (e.get("stage") != "topup", _upside(e) is None, -(_upside(e) or 0)))


def room(state_path: Path, mkt, cfg: dict, watch: dict, today: str) -> dict:
    """Cash above the reserve once the pending orders fill, as % of the portfolio (0.5% margin for costs)."""
    from portfolio import Engine, load_state, mark, totals
    state = load_state(state_path, cfg)
    mark(state, mkt)
    work = copy.deepcopy(state)
    eng = Engine(work, mkt, cfg, watch, today)
    eng.process([copy.deepcopy(o["request"]) for o in state.get("pending", [])])
    tt = totals(work)
    return {"pct": tt["cash"] / tt["total"] * 100 - eng.reserve["pct"] - 0.5, "engine": eng, "state": work}


def _request(e: dict, today: str) -> dict:
    req = copy.deepcopy(e["request"])
    stage = e.get("stage", "full")
    if stage == "topup":
        req["action"] = "ADD"
        req.pop("replaces", None)
        req.pop("replacement_reason", None)
    req["funding_stage"] = stage
    req["reason"] = (f"{req.get('reason', '')} [funding queue: decided {e['added']} at {e['decision_price']:g}; "
                     + ("top-up of the starter position" if stage == "topup" else "resubmitted")
                     + f" {today} with room above the cash reserve]").strip()
    return req


def review(state_path: Path, mkt, cfg: dict, watch: dict, today: str, now: dt.datetime | None = None,
           dry_run: bool = False, port_dir: Path = PORT) -> dict:
    """Drop stale ideas, then, best first (top-ups before new names): a full-size order when it fits; otherwise
    a starter position when the room above the reserve is at least starter_min_fraction of its target (the rest
    stays queued as a top-up); a top-up in steps of at least min_step_pct whenever room appears."""
    from portfolio import atomic_write, load_state, place_orders
    st = settings(cfg)
    state = load_state(state_path, cfg)
    out = {"resubmitted": [], "started": [], "topped_up": [], "dropped": [], "waiting": []}
    q = state.get("funding_queue") or []
    if not q:
        return out
    held = set(state["holdings"])
    ordered = {o["request"]["ticker"] for o in state.get("pending", [])}
    keep, events = [], []

    def drop(e, why):
        out["dropped"].append({"ticker": e["ticker"], "reason": why})
        events.append({"date": today, "ticker": e["ticker"], "event": "DROPPED", "detail": why})

    for e in q:
        t, topup = e["ticker"], e.get("stage") == "topup"
        if not topup and (t in held or t in ordered):
            drop(e, "now held or ordered")
            continue
        if topup and t not in held and t not in ordered:
            drop(e, "the starter position is no longer held: top-up cancelled")
            continue
        if today > e["expires"]:
            drop(e, f"waited {st['max_days']} days" + (" (the position stays at its starter size)" if topup else
                                                        f" without room (decided {e['added']})"))
            continue
        try:
            c = mkt.quote(t)["close"]
        except DataError as x:
            keep.append(e)  # no price today: keep waiting, nothing is resubmitted blind
            e["note"] = f"no price {today}: {str(x)[:120]}"
            continue
        rise = (c / e["decision_price"] - 1) * 100
        if rise > st["max_rise_pct"]:
            drop(e, f"close {c:g} is {rise:+.1f}% above the decision price {e['decision_price']:g} "
                    f"(> {st['max_rise_pct']:g}%): the research is too stale to act on"
                    + ("; the position stays at its starter size" if topup else ""))
            continue
        e["last_close"] = c
        e.pop("note", None)
        keep.append(e)
    state["funding_queue"] = _rank(keep)
    if not dry_run:
        atomic_write(state_path, json.dumps(state, indent=1, sort_keys=True))
        log_events(events, port_dir)

    def save_entry(t, update=None):
        """Remove (update None) or update a queue entry in the saved state."""
        if dry_run:
            return
        s2 = load_state(state_path, cfg)
        qq = s2.get("funding_queue", [])
        if update is None:
            s2["funding_queue"] = [x for x in qq if x["ticker"] != t]
        else:
            for x in qq:
                if x["ticker"] == t:
                    x.update(update)
        atomic_write(state_path, json.dumps(s2, indent=1, sort_keys=True))

    def place(req):
        trial = place_orders([req], state_path, mkt, cfg, watch, today, dry_run=True, port_dir=port_dir, now=now)
        if trial["placed"] and not dry_run:
            real = place_orders([req], state_path, mkt, cfg, watch, today, port_dir=port_dir, now=now)
            if not real["placed"]:
                return None, real["rejected"]
        return trial["placed"], trial["rejected"]

    # one starter at a time: none while another starter's order is still waiting for its open (2026-10-19)
    starter_busy = any(x.get("stage") == "topup" and x["ticker"] in ordered for x in state["funding_queue"])
    for e in list(state["funding_queue"]):
        t = e["ticker"]
        if e.get("note"):
            out["waiting"].append({"ticker": t, "reason": e["note"]})
            continue
        if t in ordered:  # the starter order hasn't filled yet
            out["waiting"].append({"ticker": t, "reason": "starter order waiting for its open"})
            continue
        req = _request(e, today)
        if e.get("stage") == "topup":
            r = room(state_path, mkt, cfg, watch, today)
            h = r["state"]["holdings"].get(t)
            if not h:
                out["waiting"].append({"ticker": t, "reason": "starter not filled yet"})
                continue
            from portfolio import totals
            pv = totals(r["state"])["total"]
            now_pct = h["market_value_usd"] / pv * 100
            target = r["engine"].core_size(int(req["conviction"]), t, r["state"])
            if target - now_pct < st["min_step_pct"]:
                save_entry(t)
                events.append({"date": today, "ticker": t, "event": "COMPLETE", "detail": f"at {now_pct:.2f}% of {target:.2f}%"})
                out["topped_up"].append({"ticker": t, "complete": True})
                if not dry_run:
                    log_events([events[-1]], port_dir)
                continue
            step = min(target, now_pct + max(0.0, r["pct"]))
            if step - now_pct < st["min_step_pct"]:
                out["waiting"].append({"ticker": t, "reason": f"top-up: {now_pct:.2f}% of {target:.2f}%, "
                                                              f"room {max(0.0, r['pct']):.2f}%"})
                continue
            req["cap_pct"] = round(step, 2)
            placed, rej = place(req)
            if placed:
                done = step >= target - 1e-6
                save_entry(t) if done else None
                ev = {"date": today, "ticker": t, "event": "TOPPED_UP" if done else "TOPUP_STEP",
                      "detail": f"to {step:.2f}% of {target:.2f}%"}
                if not dry_run:
                    log_events([ev], port_dir)
                out["topped_up"].append({"ticker": t, "to_pct": round(step, 2), "target_pct": round(target, 2),
                                         "complete": done})
            else:
                out["waiting"].append({"ticker": t, "reason": "; ".join(x["rule"] for x in rej or [])})
            continue
        placed, rej = place(req)
        if placed:
            p = placed[0]
            out["resubmitted"].append({"ticker": t, "est_shares": p.get("est_shares"), "est_price": p.get("est_price"),
                                       "upside_pct": _upside(e)})
            save_entry(t)
            if not dry_run:
                log_events([{"date": today, "ticker": t, "event": "RESUBMITTED", "detail": "full size, next open"}],
                           port_dir)
            continue
        first = (rej or [{}])[0]
        if not queueable(first, e["request"], cfg):
            save_entry(t)
            drop(e, f"{first.get('rule')}: {first.get('detail', '')}"[:300])
            if not dry_run:
                log_events([events[-1]], port_dir)
            continue
        # no room for the full size: a starter position when the room is at least half the target (2026-10-19)
        r = room(state_path, mkt, cfg, watch, today)
        target = r["engine"].sizer.target(int(req["conviction"]), t, r["state"])[0]
        if not starter_busy and r["pct"] >= st["starter_min_fraction"] * target:
            req["cap_pct"] = round(r["pct"], 2)
            req["funding_stage"] = "starter"
            placed, rej2 = place(req)
            if placed:
                save_entry(t, {"stage": "topup"})
                ev = {"date": today, "ticker": t, "event": "STARTER",
                      "detail": f"{req['cap_pct']:.2f}% now of a {target:.2f}% target; the rest waits as a top-up"}
                if not dry_run:
                    log_events([ev], port_dir)
                out["started"].append({"ticker": t, "starter_pct": req["cap_pct"], "target_pct": round(target, 2),
                                       "est_shares": placed[0].get("est_shares"), "est_price": placed[0].get("est_price")})
                ordered.add(t)
                starter_busy = True
                continue
            first = (rej2 or [first])[0]
        out["waiting"].append({"ticker": t, "reason": first.get("detail", "")[:200], "upside_pct": _upside(e)})
    return out


# ------------------------------------------------------------------ weekly swap brief
def swap_candidates(state: dict, mkt, cfg: dict, today: str) -> list[dict]:
    """CORE holdings, weakest first: lowest conviction, then least base-fair-value upside at the latest close."""
    from portfolio import totals
    pv = totals(state)["total"]
    rows = []
    for t, h in state["holdings"].items():
        if h["type"] != "CORE":
            continue
        try:
            c = mkt.quote(t)["close"]
        except DataError:
            continue
        val, vpath = latest_valuation(t, today)
        fv = ((val or {}).get("fair_value") or {}).get("base")
        d = ROOT / "research" / Ticker(t).slug
        evs = sorted(p for p in d.glob("20??-??-??-evaluation.md") if p.name[:10] <= today)
        rows.append({"ticker": t, "conviction": h.get("conviction"), "weight_pct": h["market_value_usd"] / pv * 100,
                     "close": c, "currency": h["currency"], "entry_date": h.get("entry_date"),
                     "entry_price": h.get("entry_price"),
                     "return_pct": (c / h["entry_price"] - 1) * 100 if h.get("entry_price") else None,
                     "fair_value_base": fv, "upside_pct": (fv / c - 1) * 100 if fv else None,
                     "evaluation": str(evs[-1].relative_to(ROOT)) if evs else None, "valuation": vpath})
    return sorted(rows, key=lambda r: (int(r["conviction"] or 0), r["upside_pct"] if r["upside_pct"] is not None
                                       else float("inf")))


def brief(state: dict, mkt, cfg: dict, today: str) -> tuple[str, dict] | tuple[None, None]:
    """Markdown brief + {"buy", "candidates"} for the weekly swap-reviewer, or (None, None) when nothing waits."""
    q = _rank([e for e in state.get("funding_queue") or [] if e.get("stage") != "topup"])
    if not q:
        return None, None
    best = q[0]
    cands = swap_candidates(state, mkt, cfg, today)[:settings(cfg)["swap_candidates"]]
    if not cands:
        return None, None
    d = ROOT / "research" / Ticker(best["ticker"]).slug
    evs = sorted(p for p in d.glob("20??-??-??-evaluation.md") if p.name[:10] <= today)
    f = lambda x, n=1: "n/a" if x is None else f"{x:,.{n}f}"  # noqa: E731
    L = [f"# Funding-queue swap brief — {today}", "",
         "The best idea waiting for cash (conviction-4+ CORE BUY rejected only by the cash reserve) against the "
         "weakest CORE holdings. All figures are computed by scripts/funding_queue.py.", "",
         "## Waiting idea", "",
         "| Ticker | Conviction | Decided | Decision price | Latest close | Base fair value | Upside | Evaluation |",
         "|---|---|---|---|---|---|---|---|",
         f"| {best['ticker']} | {best['request'].get('conviction')} | {best['added']} | {f(best['decision_price'], 2)} "
         f"{best['currency']} | {f(best.get('last_close') or best['decision_price'], 2)} | {f(best.get('fair_value_base'), 2)} | "
         f"{f(_upside(best))}% | {str(evs[-1].relative_to(ROOT)) if evs else 'n/a'} |", "",
         f"Thesis: {best['request'].get('thesis', '')}", "",
         "## Weakest CORE holdings (lowest conviction, then least upside)", "",
         "| Ticker | Conviction | Weight | Entry | Return since entry | Latest close | Base fair value | Upside | Latest evaluation |",
         "|---|---|---|---|---|---|---|---|---|"]
    for c in cands:
        L.append(f"| {c['ticker']} | {c['conviction']} | {f(c['weight_pct'])}% | {c['entry_date']} at {f(c['entry_price'], 2)} | "
                 f"{f(c['return_pct'])}% | {f(c['close'], 2)} {c['currency']} | {f(c['fair_value_base'], 2)} | "
                 f"{f(c['upside_pct'])}% | {c['evaluation'] or 'n/a'} |")
    others = [e["ticker"] for e in q[1:]]
    if others:
        L += ["", f"Also waiting (not in this week's comparison): {', '.join(others)}."]
    return "\n".join(L) + "\n", {"buy": best["ticker"], "candidates": [c["ticker"] for c in cands]}


def parse_swap(text: str, allowed: dict) -> dict | None:
    """The swap-reviewer's final ```json block -> a validated {"buy", "replaces", "replacement_reason"} or None
    (no swap). Raises ValueError on a malformed or out-of-brief answer."""
    if "```json" not in text:
        raise ValueError("no ```json block")
    d = json.loads(text.rsplit("```json", 1)[1].split("```", 1)[0])
    if d.get("swap") is not True:
        if d.get("swap") is not False:
            raise ValueError('"swap" must be true or false')
        return None
    if d.get("buy") != allowed["buy"]:
        raise ValueError(f"buy {d.get('buy')} is not the brief's waiting idea {allowed['buy']}")
    if d.get("replaces") not in allowed["candidates"]:
        raise ValueError(f"replaces {d.get('replaces')} is not one of the brief's candidates")
    if not str(d.get("replacement_reason") or "").strip():
        raise ValueError("replacement_reason missing")
    return {"buy": d["buy"], "replaces": d["replaces"], "replacement_reason": d["replacement_reason"].strip()}


def swap_request(state: dict, swap: dict) -> dict:
    e = next(x for x in state["funding_queue"] if x["ticker"] == swap["buy"])
    req = copy.deepcopy(e["request"])
    req.update(replaces=swap["replaces"], replacement_reason=swap["replacement_reason"])
    req["reason"] = f"{req.get('reason', '')} [funding queue: decided {e['added']}; weekly swap review]".strip()
    return req


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "review", "add", "brief"])
    ap.add_argument("requests", nargs="?")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--out")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    cfg = load_config()
    from portfolio import Market, atomic_write, investable, load_state, mark, place_orders, price_provider
    from fetch_data import Fetcher
    sp = PORT / "state.json"
    state = load_state(sp, cfg)
    if a.cmd == "list":
        for e in _rank(state.get("funding_queue") or []):
            u = _upside(e)
            print(f"{e['ticker']}\tconviction {e['request'].get('conviction')}\tdecided {e['added']} at "
                  f"{e['decision_price']:g} {e['currency']}\texpires {e['expires']}\tupside "
                  + ("n/a" if u is None else f"{u:+.0f}%"))
        return 0
    mkt = Market(Fetcher(cfg, refresh=a.cmd == "review"), a.asof, cfg, price_provider(cfg))
    try:
        if a.cmd == "review":
            # --asof bounds the prices (bin/fill-pending passes tomorrow to include today's close); orders and
            # the queue's dates use the real date
            today = min(a.asof, dt.date.today().isoformat())
            out = review(sp, mkt, cfg, investable(), today, now=dt.datetime.now(dt.timezone.utc), dry_run=a.dry_run)
            print(json.dumps(out, indent=1))
        elif a.cmd == "add":  # backfill: validate now; queued only if the cash reserve is the sole obstacle
            reqs = json.loads(Path(a.requests).read_text())
            trial = place_orders(reqs, sp, mkt, cfg, investable(), a.asof, dry_run=True)
            mark(state, mkt)
            if enqueue(state, trial["rejected"], reqs, mkt.quote, cfg, a.asof):
                atomic_write(sp, json.dumps(state, indent=1, sort_keys=True))
            print(json.dumps({"placeable_now": [p["ticker"] for p in trial["placed"]],
                              "queue": [e["ticker"] for e in state.get("funding_queue", [])],
                              "rejected": trial["rejected"]}, indent=1, default=str))
        elif a.cmd == "brief":
            mark(state, mkt)
            md, allowed = brief(state, mkt, cfg, a.asof)
            if md is None:
                print("nothing waiting")
                return 0
            Path(a.out).parent.mkdir(parents=True, exist_ok=True)
            Path(a.out).write_text(md)
            Path(a.out).with_suffix(".json").write_text(json.dumps(allowed))
            print(f"OK {a.out}")
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
