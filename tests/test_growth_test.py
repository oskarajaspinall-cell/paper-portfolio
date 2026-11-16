import random

import growth_test as G


def test_cagr_takes_the_larger_of_3y_and_5y():
    v = {"methods": [{"assumptions": {"cagr_3y": 0.1, "cagr_5y": 0.3}}, {"assumptions": {}}]}
    assert G.cagr(v) == 0.3 and G.cagr({"methods": []}) is None


def test_report_bands_growers_and_lists_promotions():
    rows = [{"ticker": "G", "excess": 5.0, "grower": True, "gap": -0.5}, {"ticker": "O", "excess": 1.0, "grower": False, "gap": 0.1}]
    out = G.report(rows, [{"ticker": "PLTR", "date": "2026-11-16", "base": 3, "var": 4, "cagr": 0.3}], "2026-11-16")
    assert "| growers | fair value >20% below price | 1 | +5.0" in out and "| PLTR | 2026-11-16 | 3 | 4 | 30% |" in out
    assert "DO NOT CHANGE" in out


def test_stats_interval_brackets_the_mean():
    s = G.stats([1.0, 2.0, 3.0, 4.0, 5.0], random.Random(1))
    assert s["lo"] <= s["mean"] <= s["hi"] and s["beat"] == 1.0


def test_shadow_log_is_idempotent_and_skips_when_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(G, "ROOT", tmp_path)  # no research files: nothing to log
    p = tmp_path / "g.csv"
    assert G.log_shadow("2026-11-16", {}, p) == 0 and G.log_shadow("2026-11-16", {}, p) == 0
    assert not p.exists()  # nothing to log: no file


def test_assumption_report_counts():
    import growth_assumptions as A
    rs = [{"t": "X", "price": 100, "base": 50, "bull": 120, "cagr": .3, "imp": .25},
          {"t": "Y", "price": 100, "base": 50, "bull": 80, "cagr": .2, "imp": .4},
          {"t": "Z", "price": 100, "base": 150, "bull": 200, "cagr": .2, "imp": None}]
    out = A.report(rs, "2026-11-16")
    assert "2 have base fair value below price" in out and "BULL fair value (no reversion, stronger history): 1" in out
