import csv

import pytest

import prescreen
from common import DataError


@pytest.fixture(autouse=True)
def no_trend(monkeypatch):  # these tests cover the fair-value gate; trend strength and the points gate are tested below
    monkeypatch.setattr(prescreen, "trend_strong", lambda *a: None)
    monkeypatch.setattr(prescreen, "scorecard_points", lambda *a: None)


def fake_compute(price, base):
    def compute(ticker, asof, fetcher, cfg):
        if base is None:
            return {"price": price, "fair_value": None, "upside": None}, "USD"
        return {"price": price, "fair_value": {"base": base}, "upside": {"base": base / price - 1}}, "USD"
    return compute


@pytest.mark.parametrize("price,base,verdict", [(44.05, 92.38, "PASS"), (100, 100, "PASS"),
                                                (235.23, 218.53, "SKIP"), (229.28, 85.79, "SKIP")])
def test_gate_on_base_upside(cfg, monkeypatch, price, base, verdict):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(price, base))
    row = prescreen.check("X", "2026-10-12", None, cfg)
    assert row["verdict"] == verdict and row["base_upside_pct"] == round((base / price - 1) * 100, 1)


def test_floor_comes_from_config(cfg, monkeypatch):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(100, 95))
    cfg = {**cfg, "screen": {**cfg["screen"], "prescreen_min_base_upside_pct": -10}}
    assert prescreen.check("X", "2026-10-12", None, cfg)["verdict"] == "PASS"


def test_no_fair_value_passes_to_full_research(cfg, monkeypatch):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(100, None))
    assert prescreen.check("X", "2026-10-12", None, cfg)["verdict"] == "PASS"

    def boom(*a):
        raise DataError("https://stockanalysis.com/stocks/x/financials/", "revenue", "missing")
    monkeypatch.setattr(prescreen.valuation, "compute", boom)
    row = prescreen.check("X", "2026-10-12", None, cfg)
    assert row["verdict"] == "PASS" and "unavailable" in row["reason"]


def test_record_appends_csv(tmp_path, monkeypatch):
    monkeypatch.setattr(prescreen, "ROOT", tmp_path)
    for t in ("A", "B"):
        prescreen.record({"ticker": t, "asof": "2026-10-12", "price": 1, "base_fair_value": 2,
                          "base_upside_pct": 100.0, "verdict": "PASS", "reason": "r"})
    rows = list(csv.DictReader((tmp_path / "reports" / "prescreen" / "2026-10-12.csv").open()))
    assert [r["ticker"] for r in rows] == ["A", "B"]


def test_unreliable_model_still_skips_when_every_method_is_below_price(cfg, monkeypatch):
    def compute(ticker, asof, fetcher, cfg):
        m = [{"status": "ok", "values": {"base": 40.0}}, {"status": "ok", "values": {"base": 90.0}}]
        return {"price": 100.0, "fair_value": {"base": 65.0}, "upside": {"base": -0.35}, "methods": m}, "USD"
    monkeypatch.setattr(prescreen.valuation, "compute", compute)
    assert prescreen.check("X", "2026-11-09", None, cfg)["verdict"] == "SKIP"

    def compute2(ticker, asof, fetcher, cfg):
        m = [{"status": "ok", "values": {"base": 40.0}}, {"status": "ok", "values": {"base": 130.0}}]
        return {"price": 100.0, "fair_value": {"base": 85.0}, "upside": {"base": -0.15}, "methods": m}, "USD"
    monkeypatch.setattr(prescreen.valuation, "compute", compute2)
    assert prescreen.check("X", "2026-11-09", None, cfg)["verdict"] == "PASS"   # one method sees value: research it


def test_trend_strength_rescues_a_skip(cfg, monkeypatch):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(235.23, 218.53))
    monkeypatch.setattr(prescreen, "trend_strong", lambda *a: "price +20% vs 200-day, FCF yield 3.0%")
    row = prescreen.check("X", "2026-11-15", None, cfg)
    assert row["verdict"] == "PASS" and "trend strength" in row["reason"]


def points(total, quality=2):
    return {"total": total, "parts": {"quality_level": quality}, "notes": ["ROIC TTM 4.0%"]}


@pytest.mark.parametrize("got,verdict", [((points(4), True), "SKIP"),       # below the floor with a reliable fair value
                                         ((points(5), True), "PASS"),       # at the floor: researched
                                         ((points(2), False), "PASS"),      # no reliable fair value: the estimate isn't trusted
                                         ((points(8, quality=0), False), "SKIP"),  # the quality gate blocks a 4 regardless
                                         (None, "PASS")])
def test_points_gate_skips_what_cannot_reach_conviction_4(cfg, monkeypatch, got, verdict):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(100, 140))
    monkeypatch.setattr(prescreen, "scorecard_points", lambda *a: got)
    cfg = {**cfg, "screen": {**cfg["screen"], "prescreen_min_points": 5}}
    assert prescreen.check("X", "2026-11-17", None, cfg)["verdict"] == verdict


def test_points_gate_off_or_unscoreable_passes(cfg, monkeypatch):
    monkeypatch.setattr(prescreen.valuation, "compute", fake_compute(100, 140))
    monkeypatch.setattr(prescreen, "scorecard_points", lambda *a: (points(1), True))
    off = {**cfg, "screen": {**cfg["screen"], "prescreen_min_points": 0}}
    assert prescreen.check("X", "2026-11-17", None, off)["verdict"] == "PASS"

    def boom(*a):
        raise DataError("no statements")
    monkeypatch.setattr(prescreen, "scorecard_points", boom)
    on = {**cfg, "screen": {**cfg["screen"], "prescreen_min_points": 5}}
    assert prescreen.check("X", "2026-11-17", None, on)["verdict"] == "PASS"
