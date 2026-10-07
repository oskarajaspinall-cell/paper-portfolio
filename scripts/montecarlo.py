"""Monte Carlo return distributions from research. numpy does all the maths; no model calls.

Input: research/<SLUG>/<date>-mc-params.json, written by the mc-parameters agent (every value cited).
Python adds what is arithmetic (last close, realised volatility, scenario drifts) from stockanalysis.com,
runs the sanity checks, simulates, and only then writes:
    research/<SLUG>/<date>-montecarlo.json  and  research/<SLUG>/<date>-montecarlo.md
If any check fails it prints every problem, exits 2 and writes nothing.

Model (per path): pick a scenario by its probability; daily log return over 252 trading days =
    drift_s/252 + vol*mult_s/sqrt(252) * t  (Student-t, unit variance)  + sum of shock jumps
    (+ technical tilt/252 on days 1-63 only).
drift_s = ln(target_12m / last close), so with no shocks each scenario's median 12m price is its target.
A shock jumps on any day with probability 1-(1-p_annual)^(1/252), by ln(1 + mean_impact).

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


class McError(Exception):
    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__("; ".join(problems))


# --------------------------------------------------------------------------- parameters
def _cited(node, path: str, problems: list[str], number=True):
    """A parameter is {"value": ..., "cite": "..."}; returns the value or None (recording problems)."""
    if node == MISSING or (isinstance(node, dict) and node.get("value") == MISSING):
        problems.append(f"{path}: {MISSING} (required research input not found)")
        return None
    if not isinstance(node, dict) or "value" not in node:
        problems.append(f"{path}: missing (expected {{value, cite}})")
        return None
    if not str(node.get("cite", "")).strip() or node.get("cite") == MISSING:
        problems.append(f"{path}: no citation to a research finding")
    v = node["value"]
    if number and not isinstance(v, (int, float)):
        problems.append(f"{path}: value must be a number")
        return None
    return v


def read_params(p: dict, mc: dict) -> dict:
    """Validate the LLM-written parameters. Raises McError listing every problem."""
    probs = []
    out = {"scenarios": {}, "shocks": [], "tilt": 0.0}
    for k in SCEN:
        s = (p.get("scenarios") or {}).get(k)
        if s in (None, MISSING):
            probs.append(f"scenarios.{k}: {MISSING}")
            continue
        out["scenarios"][k] = {f: _cited(s.get(f, MISSING), f"scenarios.{k}.{f}", probs)
                               for f in ("probability", "target_price_12m", "vol_multiplier")}
    shocks = p.get("shocks", [])
    if not isinstance(shocks, list):
        probs.append("shocks must be a list")
        shocks = []
    if len(shocks) > mc["max_shocks"]:
        probs.append(f"{len(shocks)} shocks (max {mc['max_shocks']})")
    for i, sh in enumerate(shocks):
        name = sh.get("name") or f"shock {i + 1}"
        if not str(sh.get("reason", "")).strip():
            probs.append(f"shocks[{name}].reason missing")
        pa = _cited(sh.get("annual_probability", MISSING), f"shocks[{name}].annual_probability", probs)
        im = _cited(sh.get("mean_impact", MISSING), f"shocks[{name}].mean_impact", probs)
        if pa is not None and not 0 < pa <= 1:
            probs.append(f"shocks[{name}].annual_probability must be in (0, 1]")
        if im is not None and not -0.95 < im <= 1:
            probs.append(f"shocks[{name}].mean_impact must be in (-0.95, 1]")
        out["shocks"].append({"name": name, "p": pa, "impact": im})
    tilt = p.get("technical_tilt")
    if tilt not in (None, {}):
        t = _cited(tilt, "technical_tilt", probs)
        if t is not None and abs(t) > mc["max_technical_tilt"]:
            probs.append(f"technical_tilt {t:+.3f} exceeds ±{mc['max_technical_tilt']} annualised")
        out["tilt"] = t or 0.0
    if probs:
        raise McError(probs)
    for k, s in out["scenarios"].items():
        if not 0 < s["probability"] < 1:
            probs.append(f"scenarios.{k}.probability must be between 0 and 1")
        if s["target_price_12m"] <= 0:
            probs.append(f"scenarios.{k}.target_price_12m must be positive")
        if not 0 < s["vol_multiplier"] <= 5:
            probs.append(f"scenarios.{k}.vol_multiplier must be in (0, 5]")
    total = sum(s["probability"] for s in out["scenarios"].values())
    if abs(total - 1) > 1e-6:
        probs.append(f"scenario probabilities sum to {total:.6g}, not 1")
    if probs:
        raise McError(probs)
    return out


def market_inputs(history: dict, url: str, asof: str) -> dict:
    """Last completed close and realised volatility from the stockanalysis.com history page."""
    rows = [r for r in history["rows"] if r["date"] < asof and r.get("close")]
    if len(rows) < 40:
        raise McError([f"price history: only {len(rows)} completed closes at {url} (need >= 40) {MISSING}"])
    closes = np.array([r["close"] for r in rows], dtype=float)
    lr = np.diff(np.log(closes))
    vol = float(lr.std(ddof=1) * math.sqrt(252))
    return {"last_close": float(closes[-1]), "close_date": rows[-1]["date"], "currency": history["info"]["price_currency"],
            "baseline_vol": vol, "lookback": f"{len(lr)} daily log returns, {rows[0]['date']} to {rows[-1]['date']}",
            "source_url": url}


def derive(par: dict, mkt: dict, mc: dict) -> dict:
    """Arithmetic the LLM never does: annualised drifts. Raises McError on out-of-range inputs."""
    probs = []
    lo, hi = mc["vol_range"]
    if not lo <= mkt["baseline_vol"] <= hi:
        probs.append(f"baseline volatility {mkt['baseline_vol']:.1%} outside {lo:.0%}-{hi:.0%}")
    drifts = {}
    for k, s in par["scenarios"].items():
        d = math.log(s["target_price_12m"] / mkt["last_close"])
        drifts[k] = d
        if not mc["drift_range"][0] <= d <= mc["drift_range"][1]:
            probs.append(f"{k} drift {d:+.1%} outside {mc['drift_range'][0]:+.0%} to {mc['drift_range'][1]:+.0%} "
                         f"(target {s['target_price_12m']} vs last close {mkt['last_close']})")
    if probs:
        raise McError(probs)
    return drifts


# --------------------------------------------------------------------------- simulation
def simulate(par: dict, mkt: dict, drifts: dict, mc: dict) -> dict:
    rng = np.random.default_rng(mc["seed"])
    n, days, df = int(mc["paths"]), max(mc["horizons_days"].values()), float(mc["student_t_df"])
    probs = np.array([par["scenarios"][k]["probability"] for k in SCEN])
    idx = rng.choice(len(SCEN), size=n, p=probs / probs.sum())
    mu = np.array([drifts[k] for k in SCEN])[idx]
    sig = mkt["baseline_vol"] * np.array([par["scenarios"][k]["vol_multiplier"] for k in SCEN])[idx]
    eps = rng.standard_t(df, size=(n, days)) * math.sqrt((df - 2) / df)  # unit variance, fat tails
    steps = mu[:, None] / 252 + sig[:, None] / math.sqrt(252) * eps
    tilt_days = mc["horizons_days"]["3m"]
    steps[:, :tilt_days] += par["tilt"] / 252
    for sh in par["shocks"]:
        p_day = 1 - (1 - sh["p"]) ** (1 / 252)
        steps += (rng.random((n, days)) < p_day) * math.log(1 + sh["impact"])
    cum = np.cumsum(steps, axis=1)
    out = {}
    for h, d in mc["horizons_days"].items():
        r = np.exp(cum[:, d - 1]) - 1
        pct = np.percentile(r, [5, 25, 50, 75, 95])
        out[h] = {"trading_days": d, "mean": float(r.mean()), "median": float(np.median(r)),
                  "p5": float(pct[0]), "p25": float(pct[1]), "p50": float(pct[2]), "p75": float(pct[3]),
                  "p95": float(pct[4]), "prob_loss": float((r < 0).mean()),
                  "scenario_share": {k: float((idx == i).mean()) for i, k in enumerate(SCEN)}}
    return out


def check_result(res: dict, par: dict, mkt: dict) -> None:
    lo = par["scenarios"]["bear"]["target_price_12m"] / mkt["last_close"] - 1
    hi = par["scenarios"]["bull"]["target_price_12m"] / mkt["last_close"] - 1
    med = res["12m"]["median"]
    if not lo <= med <= hi:
        raise McError([f"12m median {med:+.1%} outside the researched bear-to-bull range {lo:+.1%} to {hi:+.1%}"])


# --------------------------------------------------------------------------- output
def render_md(doc: dict) -> str:
    m, ps = doc["market"], doc["parameters"]
    lines = [f"## Monte Carlo — {doc['ticker']} ({doc['date']})",
             f"{doc['settings']['paths']:,} scenario-weighted paths, seed {doc['settings']['seed']}, jump-diffusion with "
             f"Student-t (df {doc['settings']['student_t_df']}) innovations. Start: {m['last_close']} {m['currency']} "
             f"(close {m['close_date']}). Baseline volatility {m['baseline_vol']:.1%} ({m['lookback']}; {m['source_url']}).",
             "", "| Scenario | Probability | 12m target | Drift (annualised) | Vol multiplier |", "|---|---|---|---|---|"]
    for k in SCEN:
        s = ps["scenarios"][k]
        lines.append(f"| {k} | {s['probability']:.0%} | {s['target_price_12m']} | {doc['drifts'][k]:+.1%} | {s['vol_multiplier']} |")
    if ps["shocks"]:
        lines.append("\nShocks: " + "; ".join(f"{x['name']} ({x['p']:.0%}/yr, {x['impact']:+.0%})" for x in ps["shocks"]))
    if ps["tilt"]:
        lines.append(f"Technical tilt (3m only): {ps['tilt']:+.1%} annualised.")
    lines += ["", "| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) | Paths bull / base / bear |",
              "|---|---|---|---|---|---|---|---|---|"]
    for h, r in doc["results"].items():
        sh = r["scenario_share"]
        lines.append(f"| {h} | {r['mean']:+.1%} | {r['median']:+.1%} | {r['p5']:+.1%} | {r['p25']:+.1%} | {r['p75']:+.1%} | "
                     f"{r['p95']:+.1%} | {r['prob_loss']:.0%} | {sh['bull']:.0%} / {sh['base']:.0%} / {sh['bear']:.0%} |")
    lines.append("\nEvery input is cited in the parameters file. This is a distribution of outcomes, not a signal.")
    return "\n".join(lines) + "\n"


def run(params_path: Path, fetcher, cfg: dict) -> dict:
    """Validate, simulate, check, and only then write. Raises McError (nothing written) on any failure."""
    mc = cfg["montecarlo"]
    raw = json.loads(params_path.read_text())
    for k in ("ticker", "date"):
        if not raw.get(k) or raw.get(k) == MISSING:
            raise McError([f"{k}: {MISSING}"])
    par = read_params(raw, mc)
    try:
        sec = fetcher.section(raw["ticker"], "history")
    except DataError as e:
        raise McError([f"price history unavailable: {e} {MISSING}"]) from e
    mkt = market_inputs(sec["data"], sec["source_url"], raw["date"])
    drifts = derive(par, mkt, mc)
    res = simulate(par, mkt, drifts, mc)
    check_result(res, par, mkt)
    doc = {"ticker": raw["ticker"], "date": raw["date"], "params_file": str(params_path.name),
           "settings": {k: mc[k] for k in ("paths", "seed", "student_t_df", "horizons_days")},
           "market": mkt, "drifts": drifts,
           "drift_method": "ln(target_price_12m / last close), annualised log drift (12-month targets)",
           "parameters": par, "results": res}
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
