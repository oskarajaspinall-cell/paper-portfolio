import csv

import pytest

import prescreen
from common import DataError


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
