import pytest

import portfolio as P
import regime as R


def snap(hy=3.1, hy3=0.4, vix=15.0, t10=5.3, t2=4.8, ry3=0.2):
    s = lambda sid, v, c3=None: {"id": sid, "value": v, "date": "2026-10-07", "chg_3m": c3}  # noqa: E731
    return {"series": [s("BAMLH0A0HYM2", hy, hy3), s("VIXCLS", vix), s("DGS10", t10), s("DGS2", t2),
                       s("DFII10", 2.9, ry3)]}


SPY_UP = {"close": 780.0, "date": "2026-10-05", "avg_40w": 730.0, "high_52w": 782.0, "drawdown_pct": 0.3, "source": "x"}


def test_calm_market_is_risk_on(cfg):
    d = R.build(snap(), SPY_UP, cfg, "2026-10-09")
    assert d["points"] == 0 and d["final_regime"] == "risk_on" and d["reserve_pct"] == 10


def test_each_indicator_scores(cfg):
    cs = cfg["cash_strategy"]
    pts = lambda **k: {i["name"]: i["points"] for i in R.score_indicators(snap(**k), SPY_UP, cs)}  # noqa: E731
    assert pts(hy=5.5)["High-yield credit spread, %"] == 1 and pts(hy=5.5, hy3=1.5)["High-yield credit spread, %"] == 2
    assert pts(vix=28)["VIX"] == 1 and pts(vix=40)["VIX"] == 2
    assert pts(t10=4.0, t2=4.5)["Yield curve, 10y - 2y, pp"] == 1
    assert pts(ry3=0.7)["Real 10y yield, 3m change, pp"] == 1
    below = dict(SPY_UP, close=700.0)
    assert {i["name"]: i["points"] for i in R.score_indicators(snap(), below, cs)}[
        "S&P 500 vs its 40-week (~200-day) average, %"] == 1


def test_regime_boundaries_and_missing_data(cfg):
    cs = cfg["cash_strategy"]
    assert [R.regime_for(p, cs) for p in (0, 1, 2, 3, 4, 6)] == ["risk_on", "risk_on", "neutral", "neutral",
                                                                 "defensive", "defensive"]
    d = R.build({"series": []}, None, cfg, "2026-10-09")  # nothing available: never guessed, scores 0
    assert d["points"] == 0 and all(i["value"] == "[data unavailable]" for i in d["indicators"])


def test_stressed_market_is_defensive(cfg):
    d = R.build(snap(hy=5.6, hy3=1.4, vix=31, t10=4.0, t2=4.4), dict(SPY_UP, close=700.0), cfg, "2026-10-09")
    assert d["final_regime"] == "defensive" and d["reserve_pct"] == 35


@pytest.mark.parametrize("dd,mult", [(None, 1.0), (9.9, 1.0), (10.0, 0.5), (19.0, 0.5), (20.0, 0.0), (35.0, 0.0)])
def test_dip_steps(cfg, dd, mult):
    assert R.dip_multiplier(dd, cfg["cash_strategy"]) == mult


def test_dip_releases_the_reserve(cfg):
    d = R.build(snap(vix=28, t10=4.0, t2=4.5), dict(SPY_UP, drawdown_pct=12.0), cfg, "2026-10-09")
    assert d["final_regime"] == "neutral" and d["reserve_pct"] == 10  # 20% x 0.5


def test_view_may_move_one_notch_only(cfg):
    d = R.build(snap(), SPY_UP, cfg, "2026-10-09")
    v = {"final_regime": "neutral", "reasons": [{"text": "a", "source": "x"}, {"text": "b", "source": "y"}]}
    assert R.apply_view(dict(d), v, cfg)["reserve_pct"] == 20
    with pytest.raises(ValueError, match="notches"):
        R.apply_view(dict(d), dict(v, final_regime="defensive"), cfg)


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
