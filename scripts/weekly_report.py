"""Assemble reports/weekly/<date>.md from a run's files. No model calls.

Sections, in order: 1. Summary (3 lines)  2. Trades executed and rejected  3. Returns
4. Review notes  5. Hit-rate table.

    python scripts/weekly_report.py --asof YYYY-MM-DD [--run runs/<date>]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from decision_log import hit_table, read as read_decisions  # noqa: E402
from portfolio import format_returns, read_csv, returns_table  # noqa: E402


def _load(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def pct(x):
    return "n/a" if x is None else f"{x * 100:+.2f}%"


def build(run: Path, asof: str, port: Path = ROOT / "portfolio") -> str:
    scan = _load(run / "scan.json", {})
    empty = {"applied": [], "rejected": [], "warnings": []}
    mech_sub, sub = _load(run / "submit-mechanical.json", empty), _load(run / "submit.json", empty)
    fills = _load(run / "fills.json", empty)
    placed = sub.get("placed", [])
    sub = {"applied": fills.get("applied", []) + mech_sub.get("applied", []) + sub.get("applied", []),
           "rejected": fills.get("rejected", []) + mech_sub.get("rejected", []) + sub.get("rejected", []),
           "dry_run": mech_sub.get("dry_run") or sub.get("dry_run")}
    manifest = _load(run / "run.json", {})
    vals = read_csv(port / "valuations.csv")
    rt = returns_table(vals, asof) if vals else {}
    total = float(vals[-1]["total_usd"]) if vals else None
    state = _load(port / "state.json", {})
    cash = state.get("cash_usd")
    wk, inc = rt.get("week", {}), rt.get("inception", {})
    applied, rejected = sub.get("applied", []), sub.get("rejected", [])
    mech = sum(1 for a in applied if str(a.get("reason", "")).startswith("mechanical"))
    decisions = manifest.get("decisions", [])
    dry = " (DRY RUN: nothing written to the portfolio)" if sub.get("dry_run") else ""

    out = [f"# Weekly report — {asof}{dry}", "", "## 1. Summary"]
    out.append(f"- Portfolio ${total:,.0f}; week {pct(wk.get('total'))} vs SPY {pct(wk.get('spy'))}; since inception "
               f"{pct(inc.get('total'))} vs SPY {pct(inc.get('spy'))}." if total is not None else "- No valuations yet.")
    out.append(f"- Trades: {len(applied)} executed ({mech} mechanical), {len(placed)} order(s) placed for the next open, "
               f"{len(rejected)} rejected; "
               f"{len(state.get('holdings', {}))} holdings, cash "
               f"{(cash / total * 100) if cash is not None and total else 0:.1f}%.")
    out.append(f"- Scan: {len(scan.get('review', []))} reviewed, {len(scan.get('reinitiate', []))} core re-initiation(s), "
               f"{len(scan.get('unflagged', []))} unchanged; new initiations: "
               + (", ".join(f"{d['ticker']} {d['decision']}" for d in decisions if d.get("kind") == "new") or "none")
               + (f"; {len(manifest.get('skipped', []))} skipped" if manifest.get("skipped") else "") + ".")

    out += ["", "## 2. Trades executed and rejected", "", "**Executed**", ""]
    if applied:
        out += ["| Side | Ticker | Type | Shares | Fill (close date) | Gross $ | Costs $ | Reason |", "|---|---|---|---|---|---|---|---|"]
        out += [f"| {a['side']} | {a['ticker']} | {a['type']} | {a['shares']} | {a['fill_price']} {a['currency']} ({a['fill_close_date']}) | "
                f"{a['gross_usd']:,.2f} | {a['costs_usd']:,.2f} | {str(a.get('reason', ''))[:120]} |" for a in applied]
    else:
        out.append("None.")
    out += ["", "**Orders placed (fill at the next market open)**", ""]
    if placed:
        out += ["| Action | Ticker | Type | Est. shares | Latest close | Replaces |", "|---|---|---|---|---|---|"]
        out += [f"| {p['action']} | {p['ticker']} | {p['type']} | {p.get('est_shares', '')} | "
                f"{p.get('est_price', '')} {p.get('est_currency', '')} ({p.get('est_close_date', '')}) | {p.get('replaces') or ''} |"
                for p in placed]
    else:
        out.append("None.")
    out += ["", "**Rejected**", ""]
    if rejected:
        out += ["| Ticker | Action | Rule | Detail |", "|---|---|---|---|"]
        out += [f"| {r['ticker']} | {r['action']} | {r['rule']} | {r['detail']} |" for r in rejected]
    else:
        out.append("None.")

    out += ["", "## 3. Returns", "", "All USD. Baseline = first-week picks held unchanged. SPY priced from "
            "https://stockanalysis.com/etf/spy/history/.", "", format_returns(rt) if rt else "No valuations yet."]

    out += ["", "## 4. Review notes", ""]
    for e in scan.get("exits", []):
        out.append(f"- **{e['ticker']}**: mechanical exit, {e['why']} — filled at close {e['close']} on {e['fill_date']} "
                   f"(no model call; {e['source_url']}).")
    for t in scan.get("trims", []):
        out.append(f"- **{t['ticker']}**: mechanical trim, core weight {t['weight_pct']}% above cap (no model call).")
    for f in scan.get("flagged", []):
        out.append(f"- **{f['ticker']}** flagged: " + " | ".join(f["reasons"]))
    for d in decisions:
        what = "core re-initiation" if d.get("kind") == "reinitiation" else "new initiation"
        out.append(f"- **{d['ticker']}** {what} → {d['decision']} (conviction {d['conviction']}): "
                   f"{d.get('rationale', '')} [{d['evaluation']}]")
    reviews = run / "reviews.md"
    if reviews.exists():
        body = "\n".join(l for l in reviews.read_text().strip().splitlines() if not l.startswith("# "))
        out += ["", "**Weekly reviewer notes**", "", body.strip(), ""]
    for sk in manifest.get("skipped", []):
        out.append(f"- **{sk['ticker']}** new initiation SKIPPED (research failed; no decision, no trade): {sk['reason']}")
    for u in scan.get("unflagged", []):
        out.append(f"- {u['line']}")
    for n in scan.get("notes", []):
        out.append(f"- Note: {n}")

    out += ["", "## 5. Hit rates", "", "Decision direction vs SPY (USD) at each horizon; a horizon counts once it has matured.",
            "", hit_table(read_decisions(port / "decisions.csv"))]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--run")
    a = ap.parse_args(argv)
    run = Path(a.run) if a.run else ROOT / "runs" / a.asof
    path = ROOT / "reports" / "weekly" / f"{a.asof}.md"
    path.write_text(build(run, a.asof))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
