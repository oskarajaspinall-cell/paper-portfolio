"""Read-only test: should the scorecard treat growth stocks differently? No model calls, no network, no portfolio writes.

    python scripts/growth_test.py [--asof D]     writes reports/growth-test/<D>.md

Uses the saved decisions (portfolio/decisions.csv, matured 1-month excess return vs SPY) and the saved research inputs.
Table A: excess return of growers (revenue CAGR >= 15%) vs the rest, by the model's fair-value gap.
Table B: re-score the latest evaluations with a growth-aware variant (fair value = midway to the bull case, capped at
+30% over price, and no strength penalty for a low fair value); the growers it lifts to conviction 4+ are compared with
the rest once their results mature, and the pre-registered rule gives the verdict. Everything is recomputed from the
saved research files, so there is nothing to log in between.
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


def diff_ci(a: list[float], b: list[float], rng: random.Random) -> tuple[float, float, float] | None:
    """Mean of a minus mean of b with a bootstrap 90% interval."""
    if not a or not b:
        return None
    d = sorted(st.mean(rng.choices(a, k=len(a))) - st.mean(rng.choices(b, k=len(b))) for _ in range(2000))
    return st.mean(a) - st.mean(b), d[100], d[1899]


def variant_conviction(eval_path: Path, cfg: dict, grower: bool) -> tuple[int | None, int | None]:
    """(today's scorecard conviction, growth-aware conviction) for a CORE evaluation from its saved inputs; (None, None)
    when it cannot be scored (not CORE, no fact-sheet sidecar)."""
    import scorecard as S
    from check_docs import decision_block
    d, err = decision_block(eval_path.read_text())
    if err or not d or d.get("position_type") != "CORE":
        return None, None
    trends, val = S.inputs_for(eval_path)
    if trends is None:
        return None, None
    if trends.get("fair_value"):
        val = trends["fair_value"]
    base = S.score(d, trends, val, cfg, S.calibration_offset())["conviction"]
    fv, price = (val or {}).get("fair_value") or {}, d.get("price_at_decision") or (val or {}).get("price")
    if not grower or not fv.get("base") or not price:
        return base, base
    v2 = json.loads(json.dumps(val))
    v2["fair_value"]["base"] = max(fv["base"], min((fv["base"] + (fv.get("bull") or fv["base"])) / 2, 1.3 * price))
    cfg2 = json.loads(json.dumps(cfg))
    cfg2.setdefault("scorecard", {})["max_strength_overvalue_pct"] = 1e9
    return base, S.score(d, trends, v2, cfg2, S.calibration_offset())["conviction"]


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


def scored(cfg: dict, log: Path | None = None) -> list[dict]:
    """Every stock's latest scorecard-era evaluation (it has a fact-sheet sidecar), re-scored under today's rules and the
    growth-aware variant, with its longest matured excess return vs SPY from the decision log (None until one matures)."""
    out_by_eval: dict[str, tuple[str, float]] = {}
    for r in csv.DictReader((log or ROOT / "portfolio" / "decisions.csv").open()):
        for h in ("12m", "6m", "3m", "1m"):
            if r.get(f"excess_{h}"):
                out_by_eval[r["evaluation"]] = (h, float(r[f"excess_{h}"]))
                break
    latest: dict[str, Path] = {}
    for ep in sorted(ROOT.glob("research/*/20??-??-??-evaluation.md")):
        if list(ep.parent.glob("factsheet-*.json")):
            latest[ep.parent.name] = ep
    out = []
    for slug, ep in latest.items():
        g = cagr(latest_valuation(ep))
        base, var = variant_conviction(ep, cfg, g is not None and g >= GROWER_CAGR)
        if base is not None:
            h, ex = out_by_eval.get(str(ep.relative_to(ROOT)), (None, None))
            out.append({"ticker": slug, "date": ep.name[:10], "base": base, "var": var, "cagr": g, "horizon": h, "excess": ex})
    return out


def promotions(cfg: dict) -> list[dict]:
    """Growers the growth-aware variant lifts to 4+."""
    return [r for r in scored(cfg) if r["base"] < 4 <= r["var"]]


def report(rows: list[dict], scored_rows: list[dict], asof: str, seed: int = 1) -> str:
    rng = random.Random(seed)
    f = lambda s: "n/a" if not s.get("n") else (f"{s['n']} | {s['mean']:+.1f} | {s['median']:+.1f} | {s['beat']:.0%} | "
                                               f"{s['lo']:+.1f} to {s['hi']:+.1f}")  # noqa: E731
    out = [f"# Growth-stock test, {asof}", "", RULE, "",
           "Caveats: one market regime; decision windows overlap; today's fundamentals and today's scorecard rules applied "
           "to past decisions; survivorship. Returns are excess vs SPY, in pp.", "",
           "## Table A: growers (revenue CAGR >= 15%) vs the rest, by fair-value gap (1-month)", "",
           "| group | fair-value gap | n | mean | median | beat SPY | 90% interval |", "|---|---|---|---|---|---|---|"]
    for label, flag in (("growers", True), ("others", False)):
        for name, lo, hi in BANDS:
            xs = [r["excess"] for r in rows if r["grower"] == flag and r["gap"] is not None and lo <= r["gap"] < hi]
            out.append(f"| {label} | {name} | {f(stats(xs, rng))} |")
    prom = [r for r in scored_rows if r["base"] < 4 <= r["var"]]
    p_ex = [r["excess"] for r in prom if r["excess"] is not None]
    r_ex = [r["excess"] for r in scored_rows if r not in prom and r["excess"] is not None]
    out += ["", "## Table B: growers a growth-aware scorecard would lift to conviction 4+", "",
            "| ticker | evaluated | conviction now | growth-aware | revenue CAGR | excess vs SPY |", "|---|---|---|---|---|---|"]
    out += [f"| {r['ticker']} | {r['date']} | {r['base']} | {r['var']} | {r['cagr']:.0%} | "
            + ("not matured" if r["excess"] is None else f"{r['excess']:+.1f} ({r['horizon']})") + " |"
            for r in sorted(prom, key=lambda r: r["ticker"])]
    d = diff_ci(p_ex, r_ex, rng)
    out += ["", f"{len(prom)} promoted of {len(scored_rows)} scored; with a matured result: {len(p_ex)} promoted, {len(r_ex)} others."]
    if d:
        out.append(f"Promoted minus others: {d[0]:+.1f}pp (90% interval {d[1]:+.1f} to {d[2]:+.1f}).")
    change = bool(d) and len(p_ex) >= 30 and d[0] >= 5 and d[1] > 0
    out += ["", "**Verdict by the rule: " + ("CHANGE**" if change else "DO NOT CHANGE**"
            + (" (fewer than 30 promoted names with a matured result)" if len(p_ex) < 30 else ""))]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    asof = argv[argv.index("--asof") + 1] if "--asof" in argv else dt.date.today().isoformat()
    cfg = load_config()
    text = report(collect(ROOT / "portfolio" / "decisions.csv"), scored(cfg), asof)
    p = ROOT / "reports" / "growth-test" / f"{asof}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
