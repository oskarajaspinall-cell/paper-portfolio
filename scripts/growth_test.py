"""Read-only test: should the scorecard treat growth stocks differently? No model calls, no network, no portfolio writes.

    python scripts/growth_test.py [--asof D]     writes reports/growth-test/<D>.md

Uses the saved decisions (portfolio/decisions.csv, matured 1-month excess return vs SPY) and the saved research inputs.
Table A: excess return of growers (revenue CAGR >= 15%) vs the rest, by the model's fair-value gap.
Table B: re-score the latest evaluations with a growth-aware variant (fair value = midway to the bull case, capped at
+30% over price, and no strength penalty for a low fair value) and list the growers it lifts to conviction 4+.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import random
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, load_config  # noqa: E402

GROWER_CAGR = 0.15
BANDS = [("fair value >20% below price", -9, -0.20), ("20% below to price", -0.20, 0.0), ("at or above price", 0.0, 9)]
RULE = ("RULE (fixed before looking): change the live scorecard only if the promoted names beat the rest by >= 5pp "
        "mean excess return with a 90% interval that excludes zero, on >= 30 promoted names. Otherwise leave it and "
        "re-test when 3-month results exist.")


def cagr(val: dict | None) -> float | None:
    vals = [a.get(k) for m in (val or {}).get("methods", []) for a in [m.get("assumptions") or {}]
            for k in ("cagr_3y", "cagr_5y") if isinstance(a.get(k), (int, float))]
    return max(vals) if vals else None


def stats(xs: list[float], rng: random.Random) -> dict:
    if not xs:
        return {"n": 0}
    boots = sorted(st.mean(rng.choices(xs, k=len(xs))) for _ in range(2000))
    return {"n": len(xs), "mean": st.mean(xs), "median": st.median(xs), "beat": sum(x > 0 for x in xs) / len(xs),
            "lo": boots[100], "hi": boots[1899]}


def variant_conviction(eval_path: Path, cfg: dict, grower: bool) -> tuple[int | None, int | None]:
    """(baseline, growth-aware) conviction for a CORE evaluation from its saved inputs."""
    return variant_detail(eval_path, cfg, grower)[:2]


def variant_detail(eval_path: Path, cfg: dict, grower: bool) -> tuple:
    """(baseline conviction, growth-aware conviction, price, base fair value, growth-aware fair value)."""
    import scorecard as S
    from check_docs import decision_block
    d, err = decision_block(eval_path.read_text())
    none = (None,) * 5
    if err or not d or d.get("position_type") != "CORE":
        return none
    trends, val = S.inputs_for(eval_path)
    if trends is None:
        return none
    if trends.get("fair_value"):
        val = trends["fair_value"]
    base = S.score(d, trends, val, cfg)["conviction"]
    if not grower or not val or not (val.get("fair_value") or {}).get("base"):
        return base, base, d.get("price_at_decision"), None, None
    fv, price = val["fair_value"], d.get("price_at_decision") or val.get("price")
    mid = (fv["base"] + (fv.get("bull") or fv["base"])) / 2
    new = max(fv["base"], min(mid, 1.3 * price)) if price else fv["base"]
    v2 = json.loads(json.dumps(val))
    v2["fair_value"]["base"] = new
    cfg2 = json.loads(json.dumps(cfg))
    cfg2.setdefault("scorecard", {})["max_strength_overvalue_pct"] = 1e9
    return base, S.score(d, trends, v2, cfg2)["conviction"], price, fv["base"], new


def latest_valuation(ep: Path) -> dict | None:
    vals = [v for v in sorted(ep.parent.glob("20??-??-??-valuation.json")) if v.name[:10] <= ep.name[:10]]
    return json.loads(vals[-1].read_text()) if vals else None


def collect(log: Path) -> list[dict]:
    """Latest matured 1-month decision per ticker, labelled grower / not (no re-scoring: October decisions predate the
    fact-sheet sidecars the scorecard needs)."""
    latest: dict[str, dict] = {}
    for r in csv.DictReader(log.open()):
        if r["excess_1m"] and r["evaluation"] and (r["ticker"] not in latest or r["date"] >= latest[r["ticker"]]["date"]):
            latest[r["ticker"]] = r
    rows = []
    for r in latest.values():
        ep = ROOT / r["evaluation"]
        val = latest_valuation(ep) if ep.exists() else None
        g = cagr(val)
        if g is not None:
            rows.append({"ticker": r["ticker"], "excess": float(r["excess_1m"]), "grower": g >= GROWER_CAGR,
                         "gap": (val.get("upside") or {}).get("base")})
    return rows


def promotions(cfg: dict) -> list[dict]:
    """Growers whose latest scorecard-era evaluation (it has a fact-sheet sidecar) the growth-aware variant lifts to 4+."""
    latest: dict[str, Path] = {}
    for ep in sorted(ROOT.glob("research/*/20??-??-??-evaluation.md")):
        if list(ep.parent.glob("factsheet-*.json")):
            latest[ep.parent.name] = ep
    out = []
    for slug, ep in latest.items():
        g = cagr(latest_valuation(ep))
        if g is None or g < GROWER_CAGR:
            continue
        base, var = variant_conviction(ep, cfg, True)
        if base is not None and base < 4 <= var:
            out.append({"ticker": slug, "date": ep.name[:10], "base": base, "var": var, "cagr": g})
    return out


SHADOW_COLS = ["date", "ticker", "price", "conviction", "growth_aware_conviction", "fair_value_base", "fair_value_growth_aware"]


def log_shadow(asof: str, cfg: dict, path: Path | None = None) -> int:
    """Append each grower's live vs growth-aware conviction (one row per ticker and day) so 3-month outcomes can be
    compared later. Observational only: nothing reads this file when trading."""
    path = path or ROOT / "portfolio" / "growth_shadow.csv"
    seen = {(r["date"], r["ticker"]) for r in csv.DictReader(path.open())} if path.exists() else set()
    latest: dict[str, Path] = {}
    for ep in sorted(ROOT.glob("research/*/20??-??-??-evaluation.md")):
        if ep.name[:10] <= asof and list(ep.parent.glob("factsheet-*.json")):
            latest[ep.parent.name] = ep
    rows = []
    for slug, ep in latest.items():
        g = cagr(latest_valuation(ep))
        if g is None or g < GROWER_CAGR or (ep.name[:10], slug) in seen:
            continue
        base, var, price, fv, fv2 = variant_detail(ep, cfg, True)
        if base is not None:
            rows.append([ep.name[:10], slug, price, base, var, fv, fv2])
    if not rows:
        return 0
    new = not path.exists()
    with path.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(SHADOW_COLS)
        w.writerows(rows)
    return len(rows)


def report(rows: list[dict], promoted: list[dict], asof: str, seed: int = 1) -> str:
    rng = random.Random(seed)
    f = lambda s: "n/a" if not s.get("n") else (f"{s['n']} | {s['mean']:+.1f} | {s['median']:+.1f} | {s['beat']:.0%} | "
                                               f"{s['lo']:+.1f} to {s['hi']:+.1f}")  # noqa: E731
    out = [f"# Growth-stock test, {asof}", "", RULE, "",
           "Caveats: one market regime; decisions from a few days in early October, so the 1-month windows overlap; "
           "today's fundamentals applied to past decisions; survivorship. Returns are 1-month excess vs SPY, in pp.", "",
           "## Table A: growers (revenue CAGR >= 15%) vs the rest, by fair-value gap", "",
           "| group | fair-value gap | n | mean | median | beat SPY | 90% interval |", "|---|---|---|---|---|---|---|"]
    for label, flag in (("growers", True), ("others", False)):
        for name, lo, hi in BANDS:
            xs = [r["excess"] for r in rows if r["grower"] == flag and r["gap"] is not None and lo <= r["gap"] < hi]
            out.append(f"| {label} | {name} | {f(stats(xs, rng))} |")
    out += ["", "## Table B: growers a growth-aware scorecard would lift to conviction 4+", "",
            "| ticker | evaluated | conviction now | growth-aware | revenue CAGR |", "|---|---|---|---|---|"]
    out += [f"| {r['ticker']} | {r['date']} | {r['base']} | {r['var']} | {r['cagr']:.0%} |" for r in sorted(promoted, key=lambda r: r["ticker"])]
    out += ["", f"{len(promoted)} names. Their returns cannot be tested yet: the scorecard only exists from 2026-11-08, so none has a "
            "matured 1-month result. The rule needs >= 30 promoted names with matured results, so:", "",
            "**Verdict by the rule: DO NOT CHANGE (not testable yet). Re-run in early January when 3-month results exist.**"]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    asof = argv[argv.index("--asof") + 1] if "--asof" in argv else dt.date.today().isoformat()
    cfg = load_config()
    text = report(collect(ROOT / "portfolio" / "decisions.csv"), promotions(cfg), asof)
    p = ROOT / "reports" / "growth-test" / f"{asof}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
