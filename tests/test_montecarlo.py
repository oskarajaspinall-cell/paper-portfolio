import copy
import datetime as dt
import json
import math

import numpy as np
import pytest

from common import load_config
from mc_inputs import analogues, is_psd, regress, weekly_returns
from montecarlo import McError, build_spec, checks, read_params, run, simulate, summarise

DATE = "2026-10-07"


class HistFetcher:
    """Daily history whose last completed close is exactly 100."""

    def section(self, ticker, page):
        rows = [{"date": f"2026-09-{d:02d}", "close": 100.0 + (d % 3)} for d in range(1, 29)]
        rows.append({"date": "2026-09-30", "close": 100.0})
        return {"source_url": "https://stockanalysis.com/fake/history/", "data": {"rows": rows, "info": {"price_currency": "USD"}}}


def inputs(**over):
    d = {"regression": {"weeks": 156, "from": "2023-10-02", "to": "2026-09-28", "alpha_weekly": 0.0,
                        "betas": {"F1": 0.7, "F2": 0.3}, "r2": 0.4,
                        "residual_vol": {"52w": 0.24, "156w": 0.26, "blended": 0.25, "method": "blend", "why": "x"},
                        "stock_vol": 0.35, "factor_stats": {},
                        "correlation": {"factors": ["F1", "F2"], "matrix": [[1.0, 0.5], [0.5, 1.0]], "psd": True}},
         "analogues": {"all_weekly_moves": {"2024-01-01": -0.2, "2025-05-12": 0.16}, "largest_falls": [],
                       "largest_rises": [], "event_weeks": []}}
    d.update(over)
    return d


def c(v, cite="finding [FS]"):
    return {"value": v, "cite": cite}


def params(**over):
    p = {"ticker": "TEST", "date": DATE,
         "scenarios": {"bull": {"probability": c(0.3), "probability_evidence": "e1", "target_price_12m": c(125.0), "target_band": c(0.08)},
                       "base": {"probability": c(0.5), "probability_evidence": "e2", "target_price_12m": c(106.0), "target_band": c(0.05)},
                       "bear": {"probability": c(0.2), "probability_evidence": "e3", "target_price_12m": c(85.0), "target_band": c(0.08)}},
         "factors": {"F1": {"expected_12m_move": c(0.05), "uncertainty_12m": c(0.20)},
                     "F2": {"expected_12m_move": c(0.0), "uncertainty_12m": c(0.30)}},
         "jumps": [{"name": "regulation", "reason": "named in note", "cite": "note sec.6", "annual_probability": c(0.15),
                    "impact": c(-0.2), "analogue": {"week": "2024-01-01", "move": -0.2}}],
         "technical_tilt": c(0.01)}
    p.update(over)
    return p


@pytest.fixture
def cfg():
    return load_config()


def setup(tmp_path, p, inp=None):
    (tmp_path / f"{DATE}-mc-inputs.json").write_text(json.dumps(inp or inputs()))
    f = tmp_path / f"{DATE}-mc-params.json"
    f.write_text(json.dumps(p))
    return f


def outputs(tmp_path):
    return sorted(x.name for x in tmp_path.glob(f"{DATE}-montecarlo.*"))


# ------------------------------------------------------------------ output + reconciliation by construction
def test_full_output_reconciles(tmp_path, cfg):
    doc = run(setup(tmp_path, params()), HistFetcher(), cfg)
    assert outputs(tmp_path) == [f"{DATE}-montecarlo.json", f"{DATE}-montecarlo.md"]
    exp = 0.3 * 0.25 + 0.5 * 0.06 + 0.2 * -0.15
    assert doc["expected_12m"] == pytest.approx(exp)
    assert doc["results"]["12m"]["mean"] == pytest.approx(exp, abs=0.002)        # mean = Σp·target
    for h, d in (("3m", 63), ("6m", 126), ("12m", 252)):
        r = doc["results"][h]
        assert r["trading_days"] == d and r["p5"] < r["p25"] < r["p50"] < r["p75"] < r["p95"]
        a = r["attribution_mean_log_return"]
        assert set(a) == {"factor", "scenario", "jumps", "noise"}
    sh = doc["results"]["12m"]["scenario_share"]
    assert sh == {"bull": 0.3, "base": 0.5, "bear": 0.2}                          # exact allocation
    cases = [s["case"] for s in doc["sensitivity"]]
    assert cases == ["probabilities as researched", "bull +10pp / bear -10pp", "bull -10pp / bear +10pp",
                     "residual vol -25%", "residual vol +25%"]
    up = doc["sensitivity"][1]["mean_12m"] - doc["sensitivity"][0]["mean_12m"]
    assert up == pytest.approx(0.1 * (0.25 - -0.15), abs=0.005)                  # +10pp bull, -10pp bear
    md = (tmp_path / f"{DATE}-montecarlo.md").read_text()
    for s in ("Attribution", "Sensitivity", "| 3m |", "| 12m |", "week of 2024-01-01", "Reconciliation"):
        assert s in md


def test_each_scenario_mean_equals_its_target(cfg):
    par = read_params(params(), inputs(), cfg["montecarlo"])
    sim = simulate(build_spec(par, inputs(), 100.0), cfg["montecarlo"])
    r = sim["h"]["12m"]["ret"]
    for i, (k, t) in enumerate((("bull", 0.25), ("base", 0.06), ("bear", -0.15))):
        assert r[sim["idx"] == i].mean() == pytest.approx(t, abs=1e-9)


def test_attribution_sums_to_mean_log_return(cfg):
    par = read_params(params(), inputs(), cfg["montecarlo"])
    sim = simulate(build_spec(par, inputs(), 100.0), cfg["montecarlo"])
    res = summarise(sim)
    for h, v in sim["h"].items():
        assert sum(res[h]["attribution_mean_log_return"].values()) == pytest.approx(np.log1p(v["ret"]).mean())


def test_tilt_only_shapes_3m(cfg):
    mc = cfg["montecarlo"]
    a = read_params(params(technical_tilt=c(0.02)), inputs(), mc)
    b = read_params(params(technical_tilt=None), inputs(), mc)
    ra, rb = (summarise(simulate(build_spec(x, inputs(), 100.0), mc)) for x in (a, b))
    assert ra["12m"]["mean"] == pytest.approx(rb["12m"]["mean"], abs=1e-9)
    assert ra["3m"]["attribution_mean_log_return"]["scenario"] > rb["3m"]["attribution_mean_log_return"]["scenario"]


def test_same_inputs_identical_numbers(tmp_path, cfg):
    run(setup(tmp_path, params()), HistFetcher(), cfg)
    first = (tmp_path / f"{DATE}-montecarlo.json").read_bytes()
    run(setup(tmp_path, params()), HistFetcher(), cfg)
    assert (tmp_path / f"{DATE}-montecarlo.json").read_bytes() == first


# ------------------------------------------------------------------ reconciliation checks
def res_with(cfg, **over12):
    par = read_params(params(), inputs(), cfg["montecarlo"])
    res = summarise(simulate(build_spec(par, inputs(), 100.0), cfg["montecarlo"]))
    res["12m"].update(over12)
    return par, res


def test_check_mean_gap_over_1_5pp(cfg):
    par, res = res_with(cfg)
    mkt = {"last_close": 100.0}
    checks(par, inputs(), mkt, res, cfg["montecarlo"])                           # passes as simulated
    res["12m"]["mean"] += 0.016
    with pytest.raises(McError) as e:
        checks(par, inputs(), mkt, res, cfg["montecarlo"])
    assert "probability-weighted target" in e.value.problems[0]


def test_check_p5_vs_bear_needs_a_cited_jump(cfg):
    par, res = res_with(cfg, p5=-0.60)                                           # bear -15% -> floor -45%
    mkt = {"last_close": 100.0}
    checks(par, inputs(), mkt, res, cfg["montecarlo"])                           # cited -20% jump: floor -65%
    res["12m"]["p5"] = -0.70                                                     # beyond what the jump explains
    with pytest.raises(McError) as e:
        checks(par, inputs(), mkt, res, cfg["montecarlo"])
    assert any("beyond what the cited negative jumps" in x for x in e.value.problems)
    res["12m"]["p5"] = -0.50
    par["jumps"] = []
    with pytest.raises(McError) as e:
        checks(par, inputs(), mkt, res, cfg["montecarlo"])
    assert any("2x the bear drop" in x for x in e.value.problems)


def test_band_does_not_double_count_residual_vol(cfg):
    """With a band inside the residual-vol budget, total stock-specific 12m dispersion stays ~ resid vol."""
    mc = cfg["montecarlo"]
    def idio_sd(band):
        spec = {"scenarios": [("base", 1.0, 0.0, band)], "betas": [], "moves": [], "unc": [], "corr": [],
                "resid_vol": 0.30, "jumps": [], "tilt": 0.0}
        return float(np.log1p(simulate(spec, mc)["h"]["12m"]["ret"]).std())
    assert idio_sd(0.0) == pytest.approx(0.30, rel=0.05)
    assert idio_sd(0.20) == pytest.approx(0.30, rel=0.07)     # band carved out of the budget, not added


def test_check_correlation_not_psd(tmp_path, cfg):
    bad = inputs()
    bad["regression"]["betas"] = {"F1": 0.5, "F2": 0.3, "F3": 0.1}
    bad["regression"]["correlation"] = {"factors": ["F1", "F2", "F3"], "psd": False,
                                        "matrix": [[1, 0.99, -0.99], [0.99, 1, 0.99], [-0.99, 0.99, 1]]}
    assert not is_psd(np.array(bad["regression"]["correlation"]["matrix"], dtype=float))
    p = params()
    p["factors"]["F3"] = {"expected_12m_move": c(0.0), "uncertainty_12m": c(0.1)}
    with pytest.raises(McError) as e:
        run(setup(tmp_path, p, bad), HistFetcher(), cfg)
    assert any("positive semi-definite" in x for x in e.value.problems) and outputs(tmp_path) == []


# ------------------------------------------------------------------ probabilities, jumps, inputs
def test_symmetric_default_flagged_then_owner_override(tmp_path, cfg):
    p = params()
    for k, v in (("bull", 0.25), ("base", 0.5), ("bear", 0.25)):
        p["scenarios"][k]["probability"] = c(v)
    with pytest.raises(McError) as e:
        run(setup(tmp_path, p), HistFetcher(), cfg)
    assert "NEEDS REVIEW" in e.value.problems[0] and outputs(tmp_path) == []
    assert (tmp_path / f"{DATE}-mc-needs-review.md").exists()
    p["owner_review"] = {"approved": True, "note": "evidence reviewed"}
    run(setup(tmp_path, p), HistFetcher(), cfg)
    assert outputs(tmp_path) and not (tmp_path / f"{DATE}-mc-needs-review.md").exists()


@pytest.mark.parametrize("mutate,msg", [
    (lambda p: p.update(jumps=[]), "no_discrete_risks_reason"),
    (lambda p: p["jumps"][0]["analogue"].update(move=-0.30), "does not match the history"),
    (lambda p: p["jumps"][0]["analogue"].update(week="2020-01-06"), "not a completed week"),
    (lambda p: p["jumps"][0].update(impact=c(-0.10)), "must equal its analogue"),
    (lambda p: p["jumps"][0].update(analogue=None), "assumption"),
    (lambda p: p["jumps"][0].update(analogue=None, assumption="bounded guess", impact=c(-0.4)), "bound"),
    (lambda p: p["factors"].pop("F2"), "factors.F2"),
    (lambda p: p["scenarios"]["bull"].update(probability_evidence=""), "probability_evidence"),
    (lambda p: p["scenarios"]["bull"].update(probability=c(0.4)), "sum to"),
    (lambda p: p["scenarios"]["base"].update(target_price_12m="[missing]"), "[missing]"),
    (lambda p: p["scenarios"]["bull"].update(target_price_12m=c(250.0)), "drift"),
    (lambda p: p.update(jumps=[dict(p["jumps"][0], name=f"j{i}") for i in range(6)]), "max 5"),
    (lambda p: p.update(technical_tilt=c(0.05)), "technical_tilt"),
])
def test_bad_parameters_rejected_and_nothing_written(tmp_path, cfg, mutate, msg):
    p = params()
    mutate(p)
    with pytest.raises(McError) as e:
        run(setup(tmp_path, p), HistFetcher(), cfg)
    assert any(msg in x for x in e.value.problems), e.value.problems
    assert outputs(tmp_path) == []


def test_empty_jumps_allowed_with_logged_reason(tmp_path, cfg):
    doc = run(setup(tmp_path, params(jumps=[], no_discrete_risks_reason="research names no discrete risks")), HistFetcher(), cfg)
    assert "research names no discrete risks" in (tmp_path / f"{DATE}-montecarlo.md").read_text()
    assert doc["no_discrete_risks_reason"]


@pytest.mark.parametrize("rv", [0.01, 2.0])
def test_residual_vol_out_of_range(tmp_path, cfg, rv):
    inp = inputs()
    inp["regression"]["residual_vol"]["blended"] = rv
    with pytest.raises(McError) as e:
        run(setup(tmp_path, params(), inp), HistFetcher(), cfg)
    assert any("residual volatility" in x for x in e.value.problems) and outputs(tmp_path) == []


def test_missing_inputs_file(tmp_path, cfg):
    f = tmp_path / f"{DATE}-mc-params.json"
    f.write_text(json.dumps(params()))
    with pytest.raises(McError) as e:
        run(f, HistFetcher(), cfg)
    assert "[missing]" in e.value.problems[0]


# ------------------------------------------------------------------ mc_inputs maths
def weekly_rows(series, start="2021-01-04"):
    d0 = dt.date.fromisoformat(start)
    return [{"date": (d0 + dt.timedelta(weeks=i)).isoformat(), "adj_close": float(v)} for i, v in enumerate(series)]


def test_regression_recovers_known_betas():
    rng = np.random.default_rng(1)
    n = 200
    f1, f2 = rng.normal(0, 0.03, n), rng.normal(0, 0.02, n)
    y = 0.8 * f1 + 0.3 * f2 + rng.normal(0, 0.003, n)
    to_px = lambda r: np.exp(np.concatenate([[0], np.cumsum(r)])) * 100  # noqa: E731
    asof = "2030-01-01"
    rows = {k: weekly_rows(to_px(v)) for k, v in (("S", y), ("F1", f1), ("F2", f2))}
    reg = regress(weekly_returns(rows["S"], asof), {k: weekly_returns(rows[k], asof) for k in ("F1", "F2")}, 156, [52, 156])
    assert reg["weeks"] == 156 and reg["betas"]["F1"] == pytest.approx(0.8, abs=0.03) and reg["betas"]["F2"] == pytest.approx(0.3, abs=0.04)
    assert reg["r2"] > 0.8 and reg["correlation"]["psd"]
    assert reg["residual_vol"]["blended"] == pytest.approx(0.003 * math.sqrt(52), rel=0.2)


def test_weekly_returns_use_completed_weeks_only():
    rows = weekly_rows([100, 101, 102, 103], start="2026-09-14")             # last week starts 2026-10-05
    wr = weekly_returns(rows, "2026-10-07")
    assert "2026-10-05" not in wr and "2026-09-28" in wr


def test_analogue_event_weeks():
    rows = weekly_rows([100, 100, 80, 82], start="2023-12-04")
    a = analogues(rows, "2024-02-01", [{"date": "2023-12-22", "title": "draft rules", "types": ["press_release"]}])
    assert a["largest_falls"][0] == {"week": "2023-12-18", "move": -0.2}
    assert a["event_weeks"][0]["week"] == "2023-12-18" and a["event_weeks"][0]["move"] == -0.2
