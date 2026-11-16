"""Read-only: for growers, which fair-value assumption keeps them 'overvalued'? Uses the saved valuation files only.

    python scripts/growth_assumptions.py [--asof D]     writes reports/growth-test/assumptions-<D>.md

Per grower (revenue CAGR >= 15%, latest valuation on/after 2026-11-08): is the price below the BULL fair value (the stronger
history, no reversion), and is the growth the price implies (reverse DCF) at or below the historical CAGR?
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from growth_test import GROWER_CAGR, cagr  # noqa: E402


def rows(since: str = "2026-11-08") -> list[dict]:
    latest: dict[str, Path] = {}
    for p in sorted(ROOT.glob("research/*/20??-??-??-valuation.json")):
        if p.name[:10] >= since:
            latest[p.parent.name] = p
    out = []
    for slug, p in latest.items():
        v = json.loads(p.read_text())
        g, imp, fv = cagr(v), v.get("implied_growth"), v.get("fair_value") or {}
        if g is None or g < GROWER_CAGR or not v.get("price") or not fv.get("base"):
            continue
        out.append({"t": slug, "price": v["price"], "base": fv["base"], "bull": fv.get("bull"), "cagr": g, "imp": imp})
    return out


def report(rs: list[dict], asof: str) -> str:
    over = [r for r in rs if r["base"] < r["price"]]
    bull_ok = [r for r in over if r["bull"] and r["bull"] >= r["price"]]
    hist_ok = [r for r in over if r["imp"] is not None and r["imp"] <= r["cagr"]]
    out = [f"# Growers and fair-value assumptions, {asof}", "",
           f"{len(rs)} growers (revenue CAGR >= 15%). {len(over)} have base fair value below price.", "",
           f"- of those, price is below the BULL fair value (no reversion, stronger history): {len(bull_ok)}",
           f"- of those, the growth the price implies is at or below the historical CAGR: {len(hist_ok)}", "",
           "A name in the last list is priced for growth it has already delivered; the base case's halfway reversion to 2.5% "
           "is what makes it look expensive. That reversion is the assumption to test with outcomes, not the scorecard.", "",
           "| ticker | price | base FV | bull FV | implied growth | historical CAGR |", "|---|---|---|---|---|---|"]
    out += [f"| {r['t']} | {r['price']:.2f} | {r['base']:.2f} | {r['bull'] or 0:.2f} | "
            f"{'n/a' if r['imp'] is None else f'{r['imp']:.0%}'} | {r['cagr']:.0%} |"
            for r in sorted(over, key=lambda r: r["t"])]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    asof = argv[argv.index("--asof") + 1] if "--asof" in argv else dt.date.today().isoformat()
    text = report(rows(), asof)
    p = ROOT / "reports" / "growth-test" / f"assumptions-{asof}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print("\n".join(text.splitlines()[:9]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
