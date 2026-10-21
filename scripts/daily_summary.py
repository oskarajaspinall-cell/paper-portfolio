"""Plain-English summary of the weekday 21:30 run (owner request 2026-10-21: "always give me a summary of the 21:30
run"). No AI and no network: it reads what the run already wrote. Writes reports/daily/<date>.md and prints the
one-line headline (bin/fill-pending shows it as a Mac notification).

    python scripts/daily_summary.py --asof YYYY-MM-DD [--log logs/fills-<date>.log]
    (--asof = the run's ASOF, the next session; the summary is dated the session it covers)
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, load_config  # noqa: E402

OUT = ROOT / "reports" / "daily"


def _csv(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open() as fh:
        return list(csv.DictReader(fh))


def _json(p: Path):
    return json.loads(p.read_text()) if p.exists() else None


def usd(x: float, sign: bool = False) -> str:
    s = f"${abs(x):,.0f}"
    return (("+" if x >= 0 else "−") + s) if sign else s


def build(asof: str, log_text: str = "") -> tuple[str, str]:
    """(headline, markdown) for the run whose ASOF is `asof`."""
    from portfolio import current_reserve, totals
    cfg = load_config()
    port = ROOT / "portfolio"
    state = json.loads((port / "state.json").read_text())
    session = (dt.date.fromisoformat(asof) - dt.timedelta(days=1)).isoformat()
    tt = totals(state)
    by_date: dict[str, dict] = {}
    for v in _csv(port / "valuations.csv"):
        by_date[v["date"]] = v
    dates = sorted(by_date)
    prev = by_date[dates[-2]] if len(dates) > 1 else None
    day = tt["total"] - float(prev["total_usd"]) if prev else None
    L = [f"# Daily update — {session} (21:30 run)", ""]

    # value
    cash_pct = tt["cash"] / tt["total"] * 100
    L.append(f"**Portfolio {usd(tt['total'])}**" + (f" ({usd(day, True)}, {day / float(prev['total_usd']) * 100:+.2f}% "
                                                     f"since {prev['date']})" if prev else "")
             + f" · cash {usd(tt['cash'])} ({cash_pct:.1f}%) · {tt['n']} holdings.")
    # trades
    fills = [r for r in _csv(port / "ledger.csv") if r["date"] == session and r["side"] in ("BUY", "ADD", "SELL", "TRIM")]
    L += ["", "**Trades**"]
    L += [f"- {r['side']} {r['ticker']}: {int(float(r['shares'])):,} shares at {float(r['fill_price']):g} {r['currency']} "
          f"({usd(abs(float(r['cash_change_usd'])))})" for r in fills] or ["- None."]
    pend = state.get("pending", [])
    if pend:
        L.append("- Pending for the next open: " + ", ".join(f"{o['request']['action']} {o['request']['ticker']}"
                                                            for o in pend) + ".")
    divs = [r for r in _csv(port / "ledger.csv") if r["date"] == session and r["side"] in ("DIVIDEND", "SPLIT")]
    L += [f"- {r['side'].title()} {r['ticker']}: {usd(float(r['cash_change_usd']))}" for r in divs]
    # movers (the latest session per holding)
    mv = []
    for t, h in state["holdings"].items():
        lc, pc = h.get("last_close"), h.get("prev_close")
        if lc and pc and h.get("last_close_date") == session:
            mv.append(((lc / pc - 1) * 100, t, h["market_value_usd"] * (1 - pc / lc)))
    if mv:
        mv.sort()
        best, worst = mv[-1], mv[0]
        L += ["", f"**Moves** (today's close vs the previous): best {best[1]} {best[0]:+.1f}% ({usd(best[2], True)}), "
                  f"worst {worst[1]} {worst[0]:+.1f}% ({usd(worst[2], True)}); "
                  f"{sum(1 for m in mv if m[0] > 0)} up, {sum(1 for m in mv if m[0] < 0)} down."]
    # cash strategy
    res = current_reserve(cfg, asof)
    dip = None
    import regime as R
    wk = R.latest(asof)
    if wk:
        dip = R.latest_dip(asof, wk["asof"])
    dd = (dip or {}).get("drawdown_pct", (wk or {}).get("dip", {}).get("drawdown_pct"))
    room = cash_pct - res["pct"]
    L += ["", f"**Cash strategy**: reserve {res['pct']:g}% ({res['regime']}"
              + (f", stress {wk['stress']:g}/100" if wk and wk.get("stress") is not None else "") + ")"
              + (f"; S&P 500 {dd:.1f}% below its 52-week high" if dd is not None else "")
              + (" — **dip release active**" if res.get("dip_multiplier", 1) < 1 else "")
              + f". Room above the reserve: {room:.1f}% of the portfolio."]
    # funding queue
    fq = state.get("funding_queue") or []
    ev = [r for r in _csv(port / "funding_queue.csv") if r["date"] == session or r["date"] == asof]
    L += ["", "**Funding queue**: " + (", ".join(f"{e['ticker']}{' (top-up)' if e.get('stage') == 'topup' else ''}"
                                                 for e in fq) or "empty") + "."]
    L += [f"- {r['event'].replace('_', ' ').lower()}: {r['ticker']} — {r['detail'][:140]}" for r in ev]
    # entry prices and dips
    hits = state.get("entry_hits") or []
    dips = _json(ROOT / "reports" / "dip-radar" / f"{asof}.json") or {}
    L += ["", "**Watchlist**: "
          + (f"entry price reached: {', '.join(h['ticker'] for h in hits)} (re-researched next)" if hits
             else "no entry prices reached")
          + "; dip radar: " + (", ".join(h["ticker"] for h in dips.get("hits", [])) + " queued for re-research"
                                if dips.get("hits") else f"no signals ({len(dips.get('assessed', []))} watched)") + "."]
    # attribution / risk
    at = _json(ROOT / "reports" / "attribution" / f"{asof}.json")
    rk = _json(ROOT / "reports" / "risk" / f"{asof}.json")
    bits = []
    if at:
        bits.append(f"excess return vs a sector-weighted S&P 500 since {at.get('start')}: {at['excess'] * 100:+.2f}%")
    if rk and rk.get("sigma_p_pct"):
        bits.append(f"portfolio volatility {rk['sigma_p_pct']:.1f}% a year")
    if bits:
        L += ["", "**Scorecard**: " + "; ".join(bits) + "."]
    # problems
    errs = [l.strip() for l in log_text.splitlines() if l.startswith("!!")]
    L += ["", "**Problems**: " + ("; ".join(errs[:5]) if errs else "none.")]
    head = (f"{usd(tt['total'])}" + (f" ({day / float(prev['total_usd']) * 100:+.2f}%)" if prev else "")
            + f" · {len(fills)} trade(s) · cash {cash_pct:.0f}% vs {res['pct']:g}% reserve"
            + (f" · entry hit {', '.join(h['ticker'] for h in hits)}" if hits else "")
            + (f" · dip {', '.join(h['ticker'] for h in dips.get('hits', []))}" if dips.get("hits") else "")
            + (f" · {len(errs)} problem(s)" if errs else ""))
    return head, "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=(dt.date.today() + dt.timedelta(days=1)).isoformat())
    ap.add_argument("--log")
    a = ap.parse_args(argv)
    log_text = Path(a.log).read_text() if a.log and Path(a.log).exists() else ""
    head, md = build(a.asof, log_text)
    session = (dt.date.fromisoformat(a.asof) - dt.timedelta(days=1)).isoformat()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{session}.md").write_text(md)
    print(head)
    return 0


if __name__ == "__main__":
    sys.exit(main())
