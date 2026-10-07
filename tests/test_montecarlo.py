import copy
import json
import math

import numpy as np
import pytest

from common import load_config
from montecarlo import McError, run

DATE = "2026-10-07"


class HistFetcher:
    """Synthetic stockanalysis.com-style history: 130 closes around 100 with ~`vol` annual volatility."""

    def __init__(self, vol=0.30, n=130):
        rng = np.random.default_rng(7)
        lr = rng.normal(0, vol / math.sqrt(252), n)
        closes = 100 * np.exp(np.cumsum(lr - lr.mean()))  # ends near 100
        self.rows = [{"date": f"2026-{4 + i // 22:02d}-{1 + i % 22:02d}", "close": float(c)} for i, c in enumerate(closes)]

    def section(self, ticker, page):
        return {"source_url": "https://stockanalysis.com/fake/history/",
                "data": {"rows": self.rows, "info": {"price_currency": "USD"}}}


def c(v, cite="research finding [FS]"):
    return {"value": v, "cite": cite}


def params(**over):
    p = {"ticker": "TEST", "date": DATE,
         "scenarios": {"bull": {"probability": c(0.25), "target_price_12m": c(140.0), "vol_multiplier": c(0.9)},
                       "base": {"probability": c(0.50), "target_price_12m": c(110.0), "vol_multiplier": c(1.0)},
                       "bear": {"probability": c(0.25), "target_price_12m": c(75.0), "vol_multiplier": c(1.3)}},
         "shocks": [{"name": "Q3 results", "annual_probability": c(0.9), "mean_impact": c(-0.03), "reason": "dated release"}],
         "technical_tilt": c(0.01)}
    p.update(over)
    return p


@pytest.fixture
def cfg():
    return load_config()


def write(tmp_path, p):
    f = tmp_path / f"{DATE}-mc-params.json"
    f.write_text(json.dumps(p))
    return f


def outputs(tmp_path):
    return sorted(x.name for x in tmp_path.glob(f"{DATE}-montecarlo.*"))


def test_full_output_for_three_horizons(tmp_path, cfg):
    doc = run(write(tmp_path, params()), HistFetcher(), cfg)
    assert outputs(tmp_path) == [f"{DATE}-montecarlo.json", f"{DATE}-montecarlo.md"]
    for h, d in (("3m", 63), ("6m", 126), ("12m", 252)):
        r = doc["results"][h]
        assert r["trading_days"] == d
        assert r["p5"] < r["p25"] < r["p50"] < r["p75"] < r["p95"] and r["p50"] == r["median"]
        assert 0 <= r["prob_loss"] <= 1 and abs(sum(r["scenario_share"].values()) - 1) < 1e-9
    assert doc["settings"]["paths"] == 10000
    share = doc["results"]["12m"]["scenario_share"]
    assert abs(share["base"] - 0.5) < 0.02 and abs(share["bull"] - 0.25) < 0.02  # sampled by probability
    md = (tmp_path / f"{DATE}-montecarlo.md").read_text()
    assert "| 3m |" in md and "| 12m |" in md and "not a signal" in md


def test_same_inputs_give_identical_numbers(tmp_path, cfg):
    a = run(write(tmp_path, params()), HistFetcher(), cfg)["results"]
    first = (tmp_path / f"{DATE}-montecarlo.json").read_bytes()
    b = run(write(tmp_path, params()), HistFetcher(), cfg)["results"]
    assert a == b and (tmp_path / f"{DATE}-montecarlo.json").read_bytes() == first


def test_scenario_median_matches_target_without_shocks(cfg):
    """With no shocks/tilt, each scenario's median 12m outcome is its researched target (drift = ln(target/close))."""
    from montecarlo import derive, market_inputs, read_params, simulate
    f = HistFetcher()
    one = params(shocks=[], technical_tilt=None)
    for k in ("bull", "base", "bear"):
        one["scenarios"][k]["target_price_12m"] = c(110.0)
    mc = cfg["montecarlo"]
    par = read_params(one, mc)
    sec = f.section("TEST", "history")
    mkt = market_inputs(sec["data"], sec["source_url"], DATE)
    res = simulate(par, mkt, derive(par, mkt, mc), mc)
    assert res["12m"]["median"] == pytest.approx(110.0 / mkt["last_close"] - 1, abs=0.01)  # within sampling noise


def bad(mutator):
    p = params()
    mutator(p)
    return p


@pytest.mark.parametrize("name,mutate,msg", [
    ("probabilities", lambda p: p["scenarios"]["bull"].update(probability=c(0.40)), "sum to"),
    ("missing input", lambda p: p["scenarios"]["base"].update(target_price_12m="[missing]"), "[missing]"),
    ("missing scenario", lambda p: p["scenarios"].pop("bear"), "scenarios.bear"),
    ("missing citation", lambda p: p["scenarios"]["bull"].update(vol_multiplier={"value": 0.9, "cite": ""}), "citation"),
    ("drift too high", lambda p: p["scenarios"]["bull"].update(target_price_12m=c(250.0)), "drift"),
    ("drift too low", lambda p: p["scenarios"]["bear"].update(target_price_12m=c(50.0)), "drift"),
    ("too many shocks", lambda p: p.update(shocks=[{"name": f"s{i}", "annual_probability": c(0.1),
                                                  "mean_impact": c(-0.05), "reason": "r"} for i in range(6)]), "max 5"),
    ("tilt too big", lambda p: p.update(technical_tilt=c(0.05)), "technical_tilt"),
    ("median outside range", lambda p: p.update(shocks=[{"name": "war", "annual_probability": c(1.0),
                                                       "mean_impact": c(-0.6), "reason": "r"}]), "12m median"),
])
def test_sanity_checks_reject_and_write_nothing(tmp_path, cfg, name, mutate, msg):
    with pytest.raises(McError) as e:
        run(write(tmp_path, bad(mutate)), HistFetcher(), cfg)
    assert any(msg in x for x in e.value.problems), e.value.problems
    assert outputs(tmp_path) == []


@pytest.mark.parametrize("vol", [0.01, 3.0])
def test_volatility_outside_range_rejected(tmp_path, cfg, vol):
    with pytest.raises(McError) as e:
        run(write(tmp_path, params()), HistFetcher(vol=vol), cfg)
    assert any("baseline volatility" in x for x in e.value.problems)
    assert outputs(tmp_path) == []


def test_short_history_is_missing_not_guessed(tmp_path, cfg):
    with pytest.raises(McError) as e:
        run(write(tmp_path, params()), HistFetcher(n=20), cfg)
    assert "[missing]" in e.value.problems[0] and outputs(tmp_path) == []


def test_config_bounds(cfg):
    mc = cfg["montecarlo"]
    assert mc["paths"] == 10000 and mc["drift_range"] == [-0.6, 0.8] and mc["vol_range"] == [0.05, 1.5]
    assert mc["horizons_days"] == {"3m": 63, "6m": 126, "12m": 252} and 4 <= mc["student_t_df"] <= 5
