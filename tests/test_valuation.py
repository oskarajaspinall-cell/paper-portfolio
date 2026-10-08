import csv

import pytest

import valuation as V
from check_docs import override_problems


@pytest.fixture
def vc(cfg):
    return cfg["valuation"]


def inputs(**over):
    """Synthetic stockanalysis.com-shaped inputs: (TTM, fiscal years newest -> oldest)."""
    g = {"revenue": (1000.0, [1000.0, 900.0, 800.0, 700.0, 650.0, 600.0]),
         "fcf": (150.0, [150.0, 130.0, 110.0, 100.0, 90.0, 80.0]), "sbc": (0.0, [0.0] * 6),
         "netinc": (120.0, [120.0] * 6), "eps": (1.2, [1.2] * 6), "ebitda": (200.0, [200.0] * 6),
         "shares": (100.0, [100.0] * 6), "interest": (0.0, [0.0] * 6), "int_income": (0.0, [0.0] * 6),
         "taxrate": (0.2, [0.2] * 6), "da": (30.0, [30.0] * 6), "netcash": (50.0, [50.0] * 6),
         "debt": (0.0, [0.0] * 6), "bvps": (5.0, [5.0] * 6), "cash": (80.0, [80.0] * 6),
         "shares_out": (100.0, [100.0] * 6), "pe": (15.0, [12.0, 15.0, 20.0, 18.0, 14.0]),
         "evebitda": (8.0, [6.0, 8.0, 10.0, 9.0, 7.0]), "evrevenue": (2.0, [1.5, 2.0, 2.5]),
         "roe": (0.15, [0.12, 0.15, 0.18, 0.14, 0.16])}
    g.update(over.pop("g", {}))
    base = {"g": g, "price": 20.0, "rf": 0.04, "beta": 1.0, "dps": None, "marketcap_quote": 2000.0, "fx": 1.0,
            "fin_ccy": "USD", "financial": False, "sources": {}}
    base.update(over)
    return base


def test_every_row_of_the_owners_table_maps_to_known_methods():
    with V.TABLE.open() as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 145
    for r in rows:
        for cell in (r["best"], r["second"]):
            ms = V.methods_in(cell)
            assert ms and all(m in V.LABEL for m in ms), (r["industry"], cell)
    assert V.methods_in("rNPV / probability-adjusted DCF") == ["rnpv"]
    assert V.methods_in("NAV / EV/EBITDAX") == ["nav", "ev_ebitda"]
    assert V.methods_in("Dividend / FCFE") == ["ddm", "fcfe"]
    assert V.industry_methods("Footwear & Accessories")["best_models"] == ["dcf"]
    unk = V.industry_methods("Something New")
    assert not unk["known"] and unk["best_models"] == ["dcf"] and unk["second_models"] == ["ev_ebitda"]


def test_dcf_at_terminal_growth_equals_gordon(vc):
    gt = vc["terminal_growth"] / 100
    v = V.dcf_per_share(1000.0, 0.1, gt, 0.09, vc, 50.0, 100.0)
    assert v == pytest.approx((1000 * 0.1 * (1 + gt) / (0.09 - gt) + 50) / 100, rel=1e-9)


def test_growth_fades_from_year_one(vc):
    hi = V.dcf_per_share(1000.0, 0.1, 0.20, 0.09, vc, 0.0, 100.0)
    lo = V.dcf_per_share(1000.0, 0.1, 0.05, 0.09, vc, 0.0, 100.0)
    assert hi > lo > V.dcf_per_share(1000.0, 0.1, vc["terminal_growth"] / 100, 0.09, vc, 0.0, 100.0)


def test_reverse_dcf_round_trip(vc):
    target = V.dcf_per_share(1000.0, 0.12, 0.07, 0.095, vc, 30.0, 100.0)
    assert V.implied_growth(target, 1000.0, 0.12, 0.095, vc, 30.0, 100.0) == pytest.approx(0.07, abs=1e-6)
    assert V.implied_growth(1e9, 1000.0, 0.12, 0.095, vc, 30.0, 100.0) is None  # outside any plausible growth


def test_dcf_scenarios_and_stock_based_pay(vc):
    r = V.run_model("dcf", inputs(), vc, {})
    assert r["status"] == "ok" and r["values"]["bear"] < r["values"]["base"] < r["values"]["bull"]
    g = r["assumptions"]["growth"]
    assert g["base"] == pytest.approx((sum(c for c in (r["assumptions"]["cagr_3y"], r["assumptions"]["cagr_5y"])) / 2
                                       + vc["terminal_growth"] / 100) / 2)
    with_sbc = V.run_model("dcf", inputs(g={"sbc": (-30.0, [-30.0] * 6)}), vc, {})
    assert with_sbc["values"]["base"] < r["values"]["base"]  # stock-based pay is a real cost


def test_financials_dcf_uses_net_income_and_no_cash(vc):
    r = V.run_model("dcf", inputs(financial=True), vc, {})
    assert "net income" in r["assumptions"]["cash_flow"] and r["discount_rate"] == pytest.approx(r["cost_of_equity"])


def test_multiples_pb_roe_ddm_and_nm(vc):
    pe = V.run_model("pe", inputs(), vc, {})
    assert pe["values"]["base"] == pytest.approx(1.2 * 15.0) and pe["values"]["bear"] == pytest.approx(1.2 * 12.0)
    ev = V.run_model("ev_ebitda", inputs(), vc, {})
    assert ev["values"]["base"] == pytest.approx((200 * 8.0 + 50) / 100)
    pb = V.run_model("pb_roe", inputs(), vc, {})
    ke, gt = 0.04 + 1.0 * vc["erp"] / 100, vc["terminal_growth"] / 100
    assert pb["values"]["base"] == pytest.approx(5.0 * (0.15 - gt) / (ke - gt))
    ddm = V.run_model("ddm", inputs(dps=0.5), vc, {})
    assert ddm["values"]["base"] == pytest.approx(0.5 * (1 + gt) / (ke - gt)) and ddm["quote_ccy"]
    assert V.run_model("pe", inputs(g={"eps": (-0.5, [-0.5] * 6)}), vc, {})["status"] == "n/m"
    assert V.run_model("ddm", inputs(), vc, {})["status"] == "n/m"
    assert V.run_model("nav", inputs(), vc, {})["status"] == "unavailable"


def test_fair_value_blend_fallback_overrides_and_fx(vc):
    fv = V.fair_value(inputs(), "Footwear & Accessories", vc)  # DCF 2/3 + P/E 1/3
    dcf, pe = (m["values"]["base"] for m in fv["methods"][:2])
    assert fv["used"] == ["dcf", "pe"] and fv["fair_value"]["base"] == pytest.approx((2 * dcf + pe) / 3)
    gold = V.fair_value(inputs(), "Gold", vc)  # mine NAV is not on stockanalysis.com -> EV/EBITDA
    assert gold["methods"][0]["status"] == "unavailable" and gold["used"] == ["ev_ebitda"]
    ov = V.fair_value(inputs(), "Insurance Brokers", vc,
                      {"valuation_overrides": [{"method": "pe", "scenario": "base", "field": "multiple", "value": 10,
                                                "reason": "x"}]})
    assert ov["methods"][0]["values"]["base"] == pytest.approx(1.2 * 10)
    hk = V.fair_value(inputs(fx=1.17), "Insurance Brokers", vc)  # financials in CNY, quote in HKD
    assert hk["methods"][0]["values"]["base"] == pytest.approx(1.2 * 15.0 * 1.17)
    nofx = V.fair_value(inputs(fx=None), "Insurance Brokers", vc)
    assert nofx["methods"][0]["status"] == "unavailable" and "FX" in nofx["methods"][0]["why"]


def test_override_checks():
    ok = {"method": "dcf", "scenario": "base", "field": "growth", "value": 0.05, "reason": "guidance cut [IS]"}
    assert override_problems([ok]) == [] and override_problems(None) == []
    assert any("cite" in e for e in override_problems([dict(ok, reason="feels right")]))
    assert any("field" in e for e in override_problems([dict(ok, field="multiple")]))
    assert any("scenario" in e for e in override_problems([dict(ok, scenario="best")]))


def test_country_risk_premium_by_reporting_currency(vc):
    assert V.country_risk("USD", vc) == 0.0
    assert V.country_risk("CNY", vc) == pytest.approx(vc["country_risk_premium"]["CNY"] / 100)
    assert V.country_risk("ZAR", vc) == pytest.approx(vc["country_risk_premium"]["default"] / 100)
    us = V.run_model("pb_roe", inputs(), vc, {})
    cn = V.run_model("pb_roe", inputs(fin_ccy="CNY"), vc, {})
    assert cn["cost_of_equity"] == pytest.approx(us["cost_of_equity"] + V.country_risk("CNY", vc))
    assert cn["values"]["base"] < us["values"]["base"]
    assert V.fair_value(inputs(fin_ccy="CNY"), "Banks - Regional", vc)["country_risk_premium"] > 0



def test_peak_earnings_guard(vc):
    spike = inputs(g={"eps": (5.0, [2.0, 1.8, 1.6, 1.5, 1.4])})  # TTM 5.0 vs 5y median 1.6
    r = V.run_model("pe", spike, vc, {})
    avg = sum([2.0, 1.8, 1.6, 1.5, 1.4]) / 5
    assert r["values"]["base"] == pytest.approx(avg * 15.0) and r["values"]["bull"] == pytest.approx(5.0 * 18.0)  # 2nd-highest P/E
    assert "peak_earnings" in r["assumptions"]
    assert "peak_earnings" not in V.run_model("pe", inputs(), vc, {})["assumptions"]



def test_one_bubble_year_does_not_set_the_bull_case():
    assert V.triple([2.0, 3.0, 2.5, 40.0, 2.2]) == (2.0, 2.5, 3.0)
    assert V.triple([2.0, 3.0, 40.0]) == (2.0, 3.0, 40.0)   # too short a history to drop one
    assert V.triple([5.0]) is None
