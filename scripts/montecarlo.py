"""Monte Carlo return distributions from research (v2). numpy does all the maths; no model calls.

Inputs (same folder, research/<SLUG>/):
    <date>-mc-inputs.json   scripts/mc_inputs.py: factor betas, R², residual vol, factor correlation,
                            jump-analogue table (all from stockanalysis.com history)
    <date>-mc-params.json   the mc-parameters agent: scenarios (+ uncertainty bands and probability
                            evidence), factor scenarios, jumps (with analogues), optional tilt; all cited
Outputs (only if every check passes): <date>-montecarlo.json and <date>-montecarlo.md.
A symmetric default probability set writes <date>-mc-needs-review.md instead and stops.

Model, per path (10,000, fixed seed; scenario mix allocated exactly n·p):
    daily log return = drift_path/252 + Σβ·factor_day + jumps_day + noise_day (+ tilt on days 1-63, netted
    out over days 64-252 so it only shapes the 3m horizon)
  factor_day  ~ MVN(ln(1+E[move])/252, D·R·D/252): correlated, historical correlation R, cited moves/uncertainty
  noise_day   = Student-t (df, unit variance) × noise_vol / √252, where noise_vol = sqrt(resid_vol² − band²)
               (floored at noise_floor_share × resid_vol): the measured residual vol is the total stock-specific
               budget, split between the researched target band and day-to-day noise (no double count)
  jumps_day   = Bernoulli(1-(1-p_annual)^(1/252)) × ln(1+impact) for each cited jump
  drift_path  = ln(1+T_path) + κ_s, with T_path drawn from target_s ± band_s and κ_s set on the seeded draws
               so each scenario's simulated MEAN simple return equals its researched target exactly.
No double count: the researched targets are TOTAL expected returns. κ_s removes the expected factor and jump
contributions from the scenario drift, so the idiosyncratic (scenario) part = target − factor − jumps; the
factor and jump terms shape dispersion and correlation, and the attribution reports each part.

    python scripts/montecarlo.py research/HKG-9999/2026-10-07-mc-params.json
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DataError, load_config  # noqa: E402

SCEN = ("bull", "base", "bear")
MISSING = "[missing]"
PSD_TOL = -1e-10


class McError(Exception):
    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__("; ".join(problems))


# --------------------------------------------------------------------------- parameter reading
def _cited(node, path, probs, number=True):
    if node == MISSING or (isinstance(node, dict) and node.get("value") == MISSING):
        probs.append(f"{path}: {MISSING} (required research input not found)")
        return None
    if not isinstance(node, dict) or "value" not in node:
        probs.append(f"{path}: missing (expected {{value, cite}})")
        return None
    if not str(node.get("cite", "")).strip() or node.get("cite") == MISSING:
        probs.append(f"{path}: no citation to a research finding")
    v = node["value"]
    if number and not isinstance(v, (int, float)):
        probs.append(f"{path}: value must be a number")
        return None
    return v


def is_symmetric_default(p: dict) -> bool:
    return abs(p["bull"] - p["bear"]) < 1e-9


def read_params(raw: dict, inputs: dict, mc: dict) -> dict:
    probs: list[str] = []
    par = {"scenarios": {}, "factors": [], "jumps": [], "tilt": 0.0}
    for k in SCEN:
        s = (raw.get("scenarios") or {}).get(k)
        if s in (None, MISSING):
            probs.append(f"scenarios.{k}: {MISSING}")
            continue
        sc = {f: _cited(s.get(f, MISSING), f"scenarios.{k}.{f}", probs)
              for f in ("probability", "target_price_12m", "target_band")}
        if not str(s.get("probability_evidence", "")).strip() or s.get("probability_evidence") == MISSING:
            probs.append(f"scenarios.{k}.probability_evidence: the evidence behind the probability is missing")
        par["scenarios"][k] = sc
    # factor scenarios must cover exactly the factors in the regression
    reg = inputs["regression"]
    fp = raw.get("factors") or {}
    for t in reg["betas"]:
        f = fp.get(t)
        if f in (None, MISSING):
            probs.append(f"factors.{t}: {MISSING} (expected 12m move and uncertainty)")
            continue
        m = _cited(f.get("expected_12m_move", MISSING), f"factors.{t}.expected_12m_move", probs)
        u = _cited(f.get("uncertainty_12m", MISSING), f"factors.{t}.uncertainty_12m", probs)
        if m is not None and not -0.6 < m < 1.0:
            probs.append(f"factors.{t}.expected_12m_move {m:+.2f} outside -60%..+100%")
        if u is not None and not 0 < u <= 1.5:
            probs.append(f"factors.{t}.uncertainty_12m must be in (0, 1.5]")
        par["factors"].append({"ticker": t, "beta": reg["betas"][t], "move": m, "unc": u})
    # jumps: mandatory unless the research names no discrete risks
    jumps = raw.get("jumps")
    if jumps is None:
        jumps = []
    if not isinstance(jumps, list):
        probs.append("jumps must be a list")
        jumps = []
    if not jumps and not str(raw.get("no_discrete_risks_reason", "")).strip():
        probs.append("jumps is empty but no_discrete_risks_reason explains why the research names no discrete risks")
    if len(jumps) > mc["max_shocks"]:
        probs.append(f"{len(jumps)} jumps (max {mc['max_shocks']})")
    moves = inputs["analogues"]["all_weekly_moves"]
    for i, j in enumerate(jumps):
        name = j.get("name") or f"jump {i + 1}"
        if not str(j.get("reason", "")).strip() or not str(j.get("cite", "")).strip():
            probs.append(f"jumps[{name}]: reason and cite (the research finding naming this risk) are required")
        pa = _cited(j.get("annual_probability", MISSING), f"jumps[{name}].annual_probability", probs)
        im = _cited(j.get("impact", MISSING), f"jumps[{name}].impact", probs)
        if pa is not None and not 0 < pa <= 1:
            probs.append(f"jumps[{name}].annual_probability must be in (0, 1]")
        an = j.get("analogue")
        if an:
            w, mv = an.get("week"), an.get("move")
            if w not in moves:
                probs.append(f"jumps[{name}].analogue week {w} is not a completed week in the stock's history")
            elif not isinstance(mv, (int, float)) or abs(moves[w] - mv) > 0.005:
                probs.append(f"jumps[{name}].analogue move {mv} does not match the history ({moves[w]:+.4f} in week {w})")
            elif im is not None and abs(im - mv) > 0.01:
                probs.append(f"jumps[{name}].impact {im:+.3f} must equal its analogue's observed move {mv:+.3f}")
        else:
            if not str(j.get("assumption", "")).strip():
                probs.append(f"jumps[{name}]: no analogue, so a stated 'assumption' is required")
            if im is not None and abs(im) > mc["max_jump_impact_assumed"]:
                probs.append(f"jumps[{name}].impact {im:+.2f} exceeds the ±{mc['max_jump_impact_assumed']:.0%} bound for an assumption")
        if im is not None and not -0.95 < im <= 1:
            probs.append(f"jumps[{name}].impact must be in (-0.95, 1]")
        par["jumps"].append({"name": name, "p": pa, "impact": im, "analogue": an, "cited": bool(j.get("cite"))})
    tilt = raw.get("technical_tilt")
    if tilt not in (None, {}):
        t = _cited(tilt, "technical_tilt", probs)
        if t is not None and abs(t) > mc["max_technical_tilt"]:
            probs.append(f"technical_tilt {t:+.3f} exceeds ±{mc['max_technical_tilt']} annualised")
        par["tilt"] = t or 0.0
    if probs:
        raise McError(probs)
    for k, s in par["scenarios"].items():
        if not 0 < s["probability"] < 1:
            probs.append(f"scenarios.{k}.probability must be between 0 and 1")
        if s["target_price_12m"] <= 0:
            probs.append(f"scenarios.{k}.target_price_12m must be positive")
        if not 0 <= s["target_band"] <= 0.5:
            probs.append(f"scenarios.{k}.target_band must be a fraction in [0, 0.5]")
    total = sum(s["probability"] for s in par["scenarios"].values())
    if abs(total - 1) > 1e-6:
        probs.append(f"scenario probabilities sum to {total:.6g}, not 1")
    if probs:
        raise McError(probs)
    return par


# --------------------------------------------------------------------------- simulation core
def allocate(n: int, p: np.ndarray) -> np.ndarray:
    """Largest-remainder counts so the scenario mix is exactly n·p (no sampling error)."""
    raw = n * p
    c = np.floor(raw).astype(int)
    for i in np.argsort(-(raw - c))[: n - c.sum()]:
        c[i] += 1
    return c


def sqrt_psd(m: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh((m + m.T) / 2)
    if np.any(w < PSD_TOL):
        raise McError(["factor correlation matrix is not positive semi-definite"])
    return v * np.sqrt(np.clip(w, 0, None))


def simulate(spec: dict, mc: dict) -> dict:
    """spec: scenarios [(name, p, target_ret, band)], betas, factor moves/uncertainty, corr, resid_vol,
    jumps [(p, impact)], tilt. Returns per-horizon arrays and components (all seeded)."""
    rng = np.random.default_rng(mc["seed"])
    n, days, df = int(mc["paths"]), 252, float(mc["student_t_df"])
    names = [s[0] for s in spec["scenarios"]]
    p = np.array([s[1] for s in spec["scenarios"]], dtype=float)
    idx = rng.permutation(np.repeat(np.arange(len(names)), allocate(n, p / p.sum())))
    tr = np.array([s[2] for s in spec["scenarios"]])[idx]
    band = np.array([s[3] for s in spec["scenarios"]])[idx]
    T = np.clip((1 + tr) * (1 + band * rng.standard_normal(n)) - 1, -0.95, None)

    k = len(spec["betas"])
    if k:
        corr = np.array(spec["corr"], dtype=float)
        L = sqrt_psd(corr)
        sd = np.array(spec["unc"], dtype=float) / math.sqrt(days)
        mean = np.log1p(np.array(spec["moves"], dtype=float)) / days
        z = rng.standard_normal((n, days, k)) @ L.T
        fac = (mean + z * sd) @ np.array(spec["betas"], dtype=float)
    else:
        fac = np.zeros((n, days))
    # Variance budget: measured residual vol is the TOTAL stock-specific 12m uncertainty. The researched target
    # band takes its share; daily noise gets the remainder (floored so short horizons keep realistic noise).
    rv = spec["resid_vol"]
    noise_vol = np.sqrt(np.maximum(rv ** 2 - band ** 2, (mc.get("noise_floor_share", 0.5) * rv) ** 2))
    noise = (rng.standard_t(df, size=(n, days)) * math.sqrt((df - 2) / df)) * (noise_vol / math.sqrt(days))[:, None]
    jmp = np.zeros((n, days))
    for jp, ji in spec["jumps"]:
        jmp += (rng.random((n, days)) < 1 - (1 - jp) ** (1 / days)) * math.log1p(ji)
    tilt = np.zeros(days)
    tilt[:63] = spec["tilt"] / days
    tilt[63:] = -spec["tilt"] * 63 / days / (days - 63)

    y12 = fac.sum(1) + noise.sum(1) + jmp.sum(1)
    targets = [s[2] for s in spec["scenarios"]]
    drift = np.empty(n)
    for i in range(len(names)):
        m = idx == i
        # calibrate to the researched target itself, so the scenario's simulated mean equals it exactly
        kappa = math.log1p(targets[i]) - math.log(((1 + T[m]) * np.exp(y12[m])).mean())
        drift[m] = np.log1p(T[m]) + kappa
    out = {"idx": idx, "names": names, "h": {}}
    for h, d in mc["horizons_days"].items():
        comp = {"factor": fac[:, :d].sum(1), "jumps": jmp[:, :d].sum(1), "noise": noise[:, :d].sum(1),
                "scenario": drift * d / days + tilt[:d].sum()}
        out["h"][h] = {"days": d, "ret": np.expm1(sum(comp.values())), "comp": comp}
    return out


def summarise(sim: dict) -> dict:
    res = {}
    for h, v in sim["h"].items():
        r = v["ret"]
        pct = np.percentile(r, [5, 25, 50, 75, 95])
        res[h] = {"trading_days": v["days"], "mean": float(r.mean()), "median": float(np.median(r)),
                  "p5": float(pct[0]), "p25": float(pct[1]), "p50": float(pct[2]), "p75": float(pct[3]), "p95": float(pct[4]),
                  "prob_loss": float((r < 0).mean()),
                  "scenario_share": {n: float((sim["idx"] == i).mean()) for i, n in enumerate(sim["names"])},
                  "attribution_mean_log_return": {c: float(x.mean()) for c, x in v["comp"].items()}}
    return res


# --------------------------------------------------------------------------- the run
def last_close(fetcher, ticker: str, asof: str) -> dict:
    try:
        sec = fetcher.section(ticker, "history")
    except DataError as e:
        raise McError([f"price history unavailable: {e} {MISSING}"]) from e
    rows = [r for r in sec["data"]["rows"] if r["date"] < asof and r.get("close")]
    if not rows:
        raise McError([f"no completed close before {asof} at {sec['source_url']} {MISSING}"])
    return {"last_close": float(rows[-1]["close"]), "close_date": rows[-1]["date"],
            "currency": sec["data"]["info"]["price_currency"], "source_url": sec["source_url"]}


def build_spec(par: dict, inputs: dict, close: float, resid_scale: float = 1.0, probs=None) -> dict:
    reg = inputs["regression"]
    order = reg["correlation"]["factors"]
    fac = {f["ticker"]: f for f in par["factors"]}
    pr = probs or {k: par["scenarios"][k]["probability"] for k in SCEN}
    return {"scenarios": [(k, pr[k], par["scenarios"][k]["target_price_12m"] / close - 1, par["scenarios"][k]["target_band"])
                          for k in SCEN],
            "betas": [fac[t]["beta"] for t in order], "moves": [fac[t]["move"] for t in order],
            "unc": [fac[t]["unc"] for t in order], "corr": reg["correlation"]["matrix"],
            "resid_vol": reg["residual_vol"]["blended"] * resid_scale,
            "jumps": [(j["p"], j["impact"]) for j in par["jumps"]], "tilt": par["tilt"]}


def checks(par: dict, inputs: dict, mkt: dict, res: dict, mc: dict) -> None:
    probs = []
    lo, hi = mc["vol_range"]
    rv = inputs["regression"]["residual_vol"]["blended"]
    if not lo <= rv <= hi:
        probs.append(f"residual volatility {rv:.1%} outside {lo:.0%}-{hi:.0%}")
    if not inputs["regression"]["correlation"].get("psd", False):
        probs.append("factor correlation matrix is not positive semi-definite")
    tr = {k: par["scenarios"][k]["target_price_12m"] / mkt["last_close"] - 1 for k in SCEN}
    for k, r in tr.items():
        d = math.log1p(r)
        if not mc["drift_range"][0] <= d <= mc["drift_range"][1]:
            probs.append(f"{k} drift {d:+.1%} outside {mc['drift_range'][0]:+.0%} to {mc['drift_range'][1]:+.0%}")
    expected = sum(par["scenarios"][k]["probability"] * tr[k] for k in SCEN)
    gap = (res["12m"]["mean"] - expected) * 100
    if abs(gap) > mc["reconcile_mean_pp"]:
        probs.append(f"12m mean {res['12m']['mean']:+.2%} differs from the probability-weighted target {expected:+.2%} "
                     f"by {gap:+.2f}pp (limit {mc['reconcile_mean_pp']}pp)")
    bear = tr["bear"]
    if bear < 0:
        jump_drop = sum(j["impact"] for j in par["jumps"] if j["impact"] < 0 and j["cited"])
        floor = bear - 2 * abs(bear) + jump_drop
        if res["12m"]["p5"] < floor:
            probs.append(f"12m P5 {res['12m']['p5']:+.1%} is below the bear target {bear:+.1%} by more than 2x the bear "
                         f"drop, beyond what the cited negative jumps ({jump_drop:+.1%} combined) explain (floor {floor:+.1%})")
    if not tr["bear"] <= res["12m"]["median"] <= tr["bull"]:
        probs.append(f"12m median {res['12m']['median']:+.1%} outside the researched bear-to-bull range "
                     f"{tr['bear']:+.1%} to {tr['bull']:+.1%}")
    if probs:
        raise McError(probs)


def sensitivity(par: dict, inputs: dict, close: float, mc: dict) -> list[dict]:
    base = {k: par["scenarios"][k]["probability"] for k in SCEN}
    cases = [("probabilities as researched", base, 1.0)]
    for label, d in (("bull +10pp / bear -10pp", +0.10), ("bull -10pp / bear +10pp", -0.10)):
        pr = {"bull": base["bull"] + d, "base": base["base"], "bear": base["bear"] - d}
        if min(pr.values()) > 0:
            cases.append((label, pr, 1.0))
    cases += [("residual vol -25%", base, 0.75), ("residual vol +25%", base, 1.25)]
    out = []
    for label, pr, scale in cases:
        r = summarise(simulate(build_spec(par, inputs, close, scale, pr), mc))["12m"]
        out.append({"case": label, "probabilities": pr, "resid_vol_scale": scale,
                    "mean_12m": r["mean"], "prob_loss_12m": r["prob_loss"]})
    return out


def needs_review_md(raw: dict, par: dict) -> str:
    lines = [f"## Monte Carlo NEEDS REVIEW — {raw['ticker']} ({raw['date']})",
             "The scenario probabilities are a symmetric default (bull = bear). Per the owner's rule they are not "
             "accepted automatically. Evidence currently cited:"]
    for k in SCEN:
        s = (raw.get("scenarios") or {}).get(k, {})
        lines.append(f"- {k}: {par['scenarios'][k]['probability']:.0%} — {s.get('probability_evidence', MISSING)}")
    lines.append("\nTo accept them, add to the parameters file: "
                 '`"owner_review": {"approved": true, "note": "<why these probabilities are right>"}` and re-run.')
    return "\n".join(lines) + "\n"


def render_md(doc: dict) -> str:
    m, reg, ps = doc["market"], doc["inputs"], doc["parameters"]
    L = [f"## Monte Carlo — {doc['ticker']} ({doc['date']})",
         f"{doc['settings']['paths']:,} paths (scenario mix allocated exactly), seed {doc['settings']['seed']}, Student-t "
         f"(df {doc['settings']['student_t_df']}) residual noise, correlated factor paths and event jumps. Start "
         f"{m['last_close']} {m['currency']} (close {m['close_date']}).",
         f"Factor regression ({reg['weeks']} weekly returns, {reg['from']} to {reg['to']}): R² {reg['r2']:.2f}; residual "
         f"vol {reg['residual_vol']['blended']:.1%} ({reg['residual_vol']['method']}).", "",
         "| Factor | Beta | Expected 12m move | Uncertainty |", "|---|---|---|---|"]
    L += [f"| {f['ticker']} | {f['beta']:+.2f} | {f['move']:+.1%} | {f['unc']:.1%} |" for f in ps["factors"]]
    L += ["", "| Scenario | Probability | 12m target | Target return | Band |", "|---|---|---|---|---|"]
    L += [f"| {k} | {s['probability']:.0%} | {s['target_price_12m']} | {doc['target_returns'][k]:+.1%} | ±{s['target_band']:.0%} |"
          for k, s in ps["scenarios"].items()]
    if ps["jumps"]:
        L += ["", "| Jump | Annual probability | Impact | Analogue |", "|---|---|---|---|"]
        for jp in ps["jumps"]:
            an = jp["analogue"]
            src = f"week of {an['week']} ({an['move']:+.1%})" if an else "none (stated assumption)"
            L.append(f"| {jp['name']} | {jp['p']:.0%} | {jp['impact']:+.1%} | {src} |")
    else:
        L.append(f"\nNo jumps: {doc['no_discrete_risks_reason']}")
    L += ["", "| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |", "|---|---|---|---|---|---|---|---|"]
    for h, r in doc["results"].items():
        L.append(f"| {h} | {r['mean']:+.1%} | {r['median']:+.1%} | {r['p5']:+.1%} | {r['p25']:+.1%} | {r['p75']:+.1%} | "
                 f"{r['p95']:+.1%} | {r['prob_loss']:.0%} |")
    L += ["", "Attribution of the mean log return:", "", "| Horizon | Factor | Scenario | Jumps | Noise |", "|---|---|---|---|---|"]
    for h, r in doc["results"].items():
        a = r["attribution_mean_log_return"]
        L.append(f"| {h} | {a['factor']:+.1%} | {a['scenario']:+.1%} | {a['jumps']:+.1%} | {a['noise']:+.1%} |")
    L += ["", "Sensitivity (12m):", "", "| Case | Mean | P(loss) |", "|---|---|---|"]
    L += [f"| {s['case']} | {s['mean_12m']:+.1%} | {s['prob_loss_12m']:.0%} |" for s in doc["sensitivity"]]
    L.append(f"\nReconciliation: 12m mean {doc['results']['12m']['mean']:+.2%} vs probability-weighted target "
             f"{doc['expected_12m']:+.2%}. Every input is cited in the parameters file. A distribution, not a signal.")
    return "\n".join(L) + "\n"


def run(params_path: Path, fetcher, cfg: dict) -> dict:
    mc = cfg["montecarlo"]
    raw = json.loads(params_path.read_text())
    for k in ("ticker", "date"):
        if not raw.get(k) or raw.get(k) == MISSING:
            raise McError([f"{k}: {MISSING}"])
    inp_path = params_path.parent / f"{raw['date']}-mc-inputs.json"
    if not inp_path.exists():
        raise McError([f"{inp_path.name}: {MISSING} (run scripts/mc_inputs.py first)"])
    inputs = json.loads(inp_path.read_text())
    par = read_params(raw, inputs, mc)
    review = params_path.parent / f"{raw['date']}-mc-needs-review.md"
    pr = {k: par["scenarios"][k]["probability"] for k in SCEN}
    if is_symmetric_default(pr) and not (raw.get("owner_review") or {}).get("approved"):
        review.write_text(needs_review_md(raw, par))
        raise McError([f"NEEDS REVIEW: symmetric default probabilities {pr} (see {review.name})"])
    mkt = last_close(fetcher, raw["ticker"], raw["date"])
    res = summarise(simulate(build_spec(par, inputs, mkt["last_close"]), mc))
    checks(par, inputs, mkt, res, mc)
    tr = {k: par["scenarios"][k]["target_price_12m"] / mkt["last_close"] - 1 for k in SCEN}
    reg = inputs["regression"]
    doc = {"ticker": raw["ticker"], "date": raw["date"], "params_file": params_path.name, "inputs_file": inp_path.name,
           "settings": {k: mc[k] for k in ("paths", "seed", "student_t_df", "horizons_days")},
           "market": mkt, "target_returns": tr,
           "expected_12m": sum(pr[k] * tr[k] for k in SCEN),
           "inputs": {k: reg[k] for k in ("weeks", "from", "to", "betas", "r2", "residual_vol")},
           "parameters": par, "no_discrete_risks_reason": raw.get("no_discrete_risks_reason"),
           "owner_review": raw.get("owner_review"),
           "separation": "targets are total expected returns; per-scenario calibration removes the expected factor "
                         "and jump terms from the scenario drift, so factor + scenario + jumps = target (no double count)",
           "results": res, "sensitivity": sensitivity(par, inputs, mkt["last_close"], mc)}
    if review.exists():
        review.unlink()
    stem = params_path.name.replace("-mc-params.json", "")
    (params_path.parent / f"{stem}-montecarlo.json").write_text(json.dumps(doc, indent=1))
    (params_path.parent / f"{stem}-montecarlo.md").write_text(render_md(doc))
    return doc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("params")
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    cfg = load_config()
    try:
        doc = run(Path(a.params), Fetcher(cfg), cfg)
    except McError as e:
        print("MONTE CARLO FAILED — nothing written:\n" + "\n".join(f"- {x}" for x in e.problems), file=sys.stderr)
        return 2
    r = doc["results"]
    print(json.dumps({h: {k: round(v, 4) for k, v in r[h].items() if isinstance(v, float)} for h in r}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
