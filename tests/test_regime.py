import pytest

import json

import portfolio as P
import regime as R

REAL_RESERVE = P.current_reserve  # conftest patches it to 0% for the rule tests


def snap(hy=3.1, hy3=0.4, vix=15.0, t10=5.3, t2=4.8, ry3=0.2, cpi=300.0, cpi3=1.5, ff3=0.0):
    s = lambda sid, v, c3=None: {"id": sid, "value": v, "date": "2026-10-07", "chg_3m": c3}  # noqa: E731
    return {"series": [s("BAMLH0A0HYM2", hy, hy3), s("VIXCLS", vix), s("DGS10", t10), s("DGS2", t2),
                       s("DFII10", 2.9, ry3), s("CPILFESL", cpi, cpi3), s("DFF", 3.6, ff3)]}


SPY_UP = {"close": 780.0, "date": "2026-10-05", "avg_40w": 730.0, "high_52w": 782.0, "drawdown_pct": 0.3, "source": "x"}


def scores(doc):
    return {i["key"]: i["score"] for i in doc["indicators"]}


def test_calm_market_has_a_low_reserve(cfg):
    d = R.build(snap(), SPY_UP, cfg, "2026-10-09")
    assert d["stress"] < 15 and d["final_regime"] == "risk_on" and 5 <= d["reserve_pct"] <= 10


def test_indicators_slide_between_calm_and_stressed(cfg):
    sc = scores(R.build(snap(hy=5.0, hy3=1.0, vix=24.5, t10=4.5, t2=4.5, ry3=0.5, ff3=0.5), dict(SPY_UP, close=711.75),
                        cfg, "2026-10-09"))
    assert sc["hy_spread"] == 0.5 and sc["hy_widening_3m"] == 0.5 and sc["vix"] == 0.5
    assert sc["curve_10y_2y"] == pytest.approx(0.667, abs=1e-3)  # flat curve: 2/3 of the way to -0.5
    assert sc["real_yield_3m"] == 0.5 and sc["fed_funds_3m"] == 0.5
    assert sc["spy_vs_40w"] == pytest.approx(0.5, abs=0.01)  # 711.75 / 730 = -2.5%, halfway from +5 to -10
    assert sc["core_cpi_3m_ann"] == pytest.approx(0.0, abs=1e-9)  # 1.5 on 298.5 = ~2.0% annualised: calm
    assert R.slide(50, 3, 7) == 1.0 and R.slide(-1, 3, 7) == 0.0  # clamped


def test_stress_maps_linearly_to_the_reserve(cfg):
    cs = cfg["cash_strategy"]
    assert [R.reserve_for(x, cs) for x in (0, 50, 100)] == [5.0, 20.0, 35.0]
    assert [R.regime_for(x, cs) for x in (0, 32.9, 33, 59.9, 60)] == ["risk_on", "risk_on", "neutral", "neutral",
                                                                       "defensive"]


def test_missing_data_is_never_guessed(cfg):
    d = R.build({"series": []}, None, cfg, "2026-10-09")
    assert d["stress"] is None and all(i["value"] == "[data unavailable]" for i in d["indicators"])
    assert d["reserve_pct"] == cfg["cash_strategy"]["fallback_reserve_pct"] and "too few" in d["note"]
    d = R.build({"series": []}, None, cfg, "2026-10-16", prev={"score_reserve_pct": 12.0})
    assert d["reserve_pct"] == 12.0  # last week's reserve stands
    part = R.build({"series": snap()["series"][:2]}, SPY_UP, cfg, "2026-10-09")  # HY only + SPY: 3 of 8
    assert part["stress"] is None


def test_stressed_market_is_defensive(cfg):
    d = R.build(snap(hy=7.5, hy3=2.5, vix=36, t10=4.0, t2=4.6, ry3=1.2, cpi3=4.0, ff3=1.0), dict(SPY_UP, close=600.0),
                cfg, "2026-10-09")
    assert d["stress"] > 95 and d["final_regime"] == "defensive" and d["reserve_pct"] >= 34


def test_weekly_move_is_capped(cfg):
    calm, hot = snap(), snap(hy=7.5, hy3=2.5, vix=36, t10=4.0, t2=4.6, ry3=1.2, cpi3=4.0, ff3=1.0)
    d = R.build(hot, dict(SPY_UP, close=600.0), cfg, "2026-10-16", prev={"score_reserve_pct": 10.0})
    assert d["unsmoothed_reserve_pct"] >= 34 and d["score_reserve_pct"] == 15.0
    d = R.build(calm, SPY_UP, cfg, "2026-10-16", prev={"base_reserve_pct": 20.0})  # an old-format file
    assert d["score_reserve_pct"] == 15.0
@pytest.mark.parametrize("dd,mult", [(None, 1.0), (9.9, 1.0), (10.0, 0.5), (19.0, 0.5), (20.0, 0.0), (35.0, 0.0)])
def test_dip_steps(cfg, dd, mult):
    assert R.dip_multiplier(dd, cfg["cash_strategy"]) == mult


def test_dip_releases_the_reserve(cfg):
    d = R.build(snap(), dict(SPY_UP, drawdown_pct=12.0), cfg, "2026-10-09")
    assert d["reserve_pct"] == d["score_reserve_pct"] * 0.5


def test_view_moves_the_reserve_one_notch_of_5pp(cfg):
    d = R.build(snap(), SPY_UP, cfg, "2026-10-09")
    assert d["score_regime"] == "risk_on"
    v = {"final_regime": "neutral", "reasons": [{"text": "a", "source": "x"}, {"text": "b", "source": "y"}]}
    got = R.apply_view(dict(d), v, cfg)
    assert got["view_adjust_pp"] == 5 and got["reserve_pct"] == d["score_reserve_pct"] + 5
    with pytest.raises(ValueError, match="notches"):
        R.apply_view(dict(d), dict(v, final_regime="defensive"), cfg)
    low = R.apply_view(dict(d, score_regime="neutral"), dict(v, final_regime="risk_on"), cfg)
    assert low["base_reserve_pct"] >= cfg["cash_strategy"]["reserve_min_pct"]  # never below the minimum


def test_buy_below_the_reserve_needs_a_replacement(cfg, monkeypatch):
    from test_portfolio import PRICES, WATCH, core_buy, holding
    from conftest import FakeMarket
    monkeypatch.setattr(P, "current_reserve", lambda c, a: {"pct": 20.0, "regime": "neutral", "dip_multiplier": 1.0})
    s = P.empty_state(cfg)
    s["holdings"]["LON:SHEL"] = holding("LON:SHEL", "CORE", 40, conv=5)
    s["holdings"]["LON:ULVR"] = holding("LON:ULVR", "CORE", 35, conv=5)
    s["cash_usd"] = 100000 * 0.25  # 25% cash of $100k: a 7% buy would leave ~18%, below the 20% reserve
    e = P.Engine(s, FakeMarket(PRICES, cfg), cfg, WATCH, "2026-10-06")
    e.process([core_buy("AAPL", conv=4)])
    assert e.rejections and e.rejections[0]["rule"] == "REPLACEMENT_REQUIRED" and "reserve" in e.rejections[0]["detail"]
    e = P.Engine(s, FakeMarket(PRICES, cfg), cfg, WATCH, "2026-10-06")
    e.process([core_buy("AAPL", conv=4, replaces="LON:ULVR", replacement_reason="better value")])
    assert e.applied and "LON:ULVR" not in e.s["holdings"]


def test_dip_candidates_only_while_the_reserve_is_released(cfg):
    from weekly_scan import dip_candidates
    work = {"holdings": {"A": {"type": "CORE", "conviction": 4, "market_value_usd": 4500.0},   # 4.5% vs 7%
                         "B": {"type": "CORE", "conviction": 4, "market_value_usd": 6500.0},   # 6.5%: close enough
                         "T": {"type": "TACTICAL", "conviction": 4, "market_value_usd": 1000.0}}}
    calm = {"pct": 10.0, "regime": "risk_on", "dip_multiplier": 1.0}
    dip = {"pct": 5.0, "regime": "risk_on", "dip_multiplier": 0.5}
    assert dip_candidates(work, 100000.0, cfg, calm, set()) == []
    got = dip_candidates(work, 100000.0, cfg, dip, set())
    assert [d["ticker"] for d in got] == ["A"] and "ADD eligible" in got[0]["why"]


def test_regime_view_check(cfg):
    from check_docs import check_regime_view
    score = {"score_regime": "risk_on"}
    view = lambda **v: "# Macro view\nKeep.\n```json\n" + __import__("json").dumps(v) + "\n```\n"  # noqa: E731
    ok, _ = check_regime_view(view(final_regime="risk_on", keep_score=True, reasons=[]), score, cfg)
    assert ok == []
    errs, _ = check_regime_view(view(final_regime="neutral", keep_score=False,
                                     reasons=[{"text": "a", "source": "a blog"}]), score, cfg)
    assert any("official sources" in e for e in errs)
    errs, _ = check_regime_view(view(final_regime="defensive", keep_score=False, reasons=[]), score, cfg)
    assert any("notches" in e for e in errs)
    cited = [{"text": "FOMC hiked", "source": "https://www.federalreserve.gov/x (2026-10-08)"},
             {"text": "HY spread jumped", "source": "https://fred.stlouisfed.org/x (2026-10-08)"}]
    ok, _ = check_regime_view(view(final_regime="neutral", keep_score=False, reasons=cited), score, cfg)
    assert ok == []


def test_new_orders_are_checked_after_the_pending_ones(cfg, tmp_path, monkeypatch):
    from test_portfolio import PRICES, WATCH, core_buy
    from conftest import FakeMarket
    monkeypatch.setattr(P, "current_reserve", lambda c, a: {"pct": 88.0, "regime": "defensive", "dip_multiplier": 1.0})
    sp = tmp_path / "state.json"
    mkt = FakeMarket(PRICES, cfg)
    out = P.place_orders([core_buy("AAPL", conv=4)], sp, mkt, cfg, WATCH, "2026-10-06", port_dir=tmp_path)
    assert out["placed"]  # 100% cash -> ~93% after a 7% buy: above the 88% reserve
    out = P.place_orders([core_buy("MSFT", conv=4)], sp, mkt, cfg, WATCH, "2026-10-06", port_dir=tmp_path)
    assert not out["placed"] and out["rejected"][0]["rule"] == "REPLACEMENT_REQUIRED"  # ~86% once AAPL's order counts


# ------------------------------------------------------------------ daily dip check (2026-10-19)
def test_daily_dip_check_overrides_the_weekly_dip_until_the_next_weekly_file(cfg, tmp_path, monkeypatch):
    weekly = {"asof": "2026-10-17", "final_regime": "neutral", "base_reserve_pct": 20, "reserve_pct": 20,
              "dip": {"drawdown_pct": 2.0, "multiplier": 1.0}}
    spy = {"close": 680.0, "date": "2026-10-20", "high_52w": 780.0, "drawdown_pct": 12.82, "source": "x"}
    (tmp_path / "dip-2026-10-21.json").write_text(json.dumps(R.dip_doc(spy, cfg, "2026-10-21")))
    (tmp_path / "dip-2026-10-17.json").write_text(json.dumps(R.dip_doc(dict(spy, drawdown_pct=25.0), cfg, "2026-10-17")))
    assert R.latest_dip("2026-10-20", "2026-10-17", tmp_path) is None  # not in force before its date
    assert R.latest_dip("2026-10-21", "2026-10-17", tmp_path)["multiplier"] == 0.5
    assert R.latest_dip("2026-10-21", "2026-10-21", tmp_path) is None  # a newer weekly file supersedes it
    monkeypatch.setattr(R, "latest", lambda asof: weekly)
    monkeypatch.setattr(R, "latest_dip", lambda asof, after: R.dip_doc(spy, cfg, "2026-10-21"))
    res = REAL_RESERVE(cfg, "2026-10-21")
    assert (res["pct"], res["regime"], res["dip_multiplier"], res["dip_asof"]) == (10.0, "neutral", 0.5, "2026-10-21")
    monkeypatch.setattr(R, "latest_dip", lambda asof, after: None)
    assert REAL_RESERVE(cfg, "2026-10-21")["pct"] == 20


def test_spy_dip_daily_uses_closes_before_asof(cfg):
    rows = [{"date": f"2026-{1 + i // 28:02d}-{1 + i % 28:02d}", "close": 700.0 + i} for i in range(260)]

    class F:
        def long_history(self, t, etf=False, range_="1Y", period="Daily"):
            assert (t, etf, period) == ("SPY", True, "Daily")
            return {"rows": rows + [{"date": "2026-12-31", "close": 1.0}], "source_url": "u"}
    d = R.spy_dip_daily(F(), "2026-12-30")
    assert d["close"] == 959.0 and d["high_52w"] == 959.0 and d["drawdown_pct"] == 0.0
