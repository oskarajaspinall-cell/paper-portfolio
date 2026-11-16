import pytest
import random

import growth_test as G


def test_cagr_takes_the_larger_of_3y_and_5y():
    v = {"methods": [{"assumptions": {"cagr_3y": 0.1, "cagr_5y": 0.3}}, {"assumptions": {}}]}
    assert G.cagr(v) == 0.3 and G.cagr({"methods": []}) is None


def test_report_bands_growers_and_applies_the_rule():
    rows = [{"ticker": "G", "excess": 5.0, "grower": True, "gap": -0.5}, {"ticker": "O", "excess": 1.0, "grower": False, "gap": 0.1}]
    sc = lambda t, base, var, ex: {"ticker": t, "date": "2026-11-16", "base": base, "var": var, "cagr": 0.3, "horizon": "3m", "excess": ex}  # noqa: E731
    few = [sc("PLTR", 3, 4, None), sc("X", 3, 3, 1.0)]
    out = G.report(rows, few, "2026-11-16")
    assert "| growers | fair value >20% below price | 1 | +5.0" in out and "| PLTR | 2026-11-16 | 3 | 4 | 30% | not matured |" in out
    assert "DO NOT CHANGE** (fewer than 30" in out
    many = [sc(f"P{i}", 3, 4, 20.0 + i % 3) for i in range(30)] + [sc(f"R{i}", 3, 3, -2.0 + i % 3) for i in range(40)]
    assert "**Verdict by the rule: CHANGE**" in G.report(rows, many, "2026-11-16")
    assert "DO NOT CHANGE" in G.report(rows, many[:10] + many[30:], "2026-11-16")  # only 10 promoted


def test_stats_interval_brackets_the_mean():
    s = G.stats([1.0, 2.0, 3.0, 4.0, 5.0], random.Random(1))
    assert s["lo"] <= s["mean"] <= s["hi"] and s["beat"] == 1.0


def test_points_table_groups_by_whole_points():
    import calibration as C
    t = C.points_table([(9.0, 10.0), (9.0, 20.0), (8.0, -4.0)])
    assert list(t) == ["9", "8"] and t["9"] == {"n": 2, "mean_vs_spy": 15.0} and t["8"]["n"] == 1


def test_world_returns_use_the_portfolio_dates():
    import weekly_report as W
    vals = [{"date": "2026-10-06"}, {"date": "2026-11-09"}, {"date": "2026-11-16"}]
    r = W.world_returns(vals, {"2026-10-05": 100.0, "2026-11-09": 110.0, "2026-11-14": 121.0})
    assert r["inception"] == pytest.approx(0.21) and r["week"] == pytest.approx(0.10)
    assert W.world_returns(vals, {"2026-11-01": 100.0}) is None  # inception not covered
