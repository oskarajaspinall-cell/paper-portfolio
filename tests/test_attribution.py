import pytest

from attribution import carino, daily_effects


def rows(*closes, start=1):
    return [{"date": f"2026-10-{start + i:02d}", "close": c} for i, c in enumerate(closes)]


def test_two_sector_two_day_hand_case_sums_to_excess():
    # $100 start; day 1 (close 10-01) buy $60 of A (Technology) at 10.00, 0 costs; hold cash 40.
    ledger = [{"date": "2026-10-01", "fill_close_date": "2026-10-01", "ticker": "A", "side": "BUY", "shares": "6",
               "gross_usd": "60", "cash_change_usd": "-60"}]
    hist = {"A": rows(10.0, 11.0, 11.0), "XLK": rows(100.0, 105.0, 105.0), "SPY": rows(100.0, 102.0, 101.0)}
    from attribution import SECTOR_ETF
    for s, e in SECTOR_ETF.items():
        hist.setdefault(e, rows(100.0, 100.0, 98.0))
    bench_w = {s: (0.5 if s == "Technology" else 0.5 / 10) for s in SECTOR_ETF}
    days = ["2026-10-01", "2026-10-02", "2026-10-03"]
    d = daily_effects(days, ledger, hist, {"A": "Technology"}, {}, 100.0, [], bench_w, 0.0)
    # day 1: portfolio = 60 x +10% = +6%; benchmark = 0.5 x 5% = +2.5%
    assert d[0]["rp"] == pytest.approx(0.06) and d[0]["rb"] == pytest.approx(0.025)
    tech = d[0]["sectors"]["Technology"]
    assert tech["allocation"] == pytest.approx((0.6 - 0.5) * (0.05 - 0.025))
    assert tech["selection"] == pytest.approx(0.5 * (0.10 - 0.05))
    assert tech["interaction"] == pytest.approx(0.1 * 0.05)
    cash = d[0]["sectors"]["Cash"]
    assert cash["wp"] == pytest.approx(0.4) and cash["allocation"] == pytest.approx(0.4 * (0 - 0.025))
    res = carino(d)
    assert res["portfolio"] == pytest.approx(1.06 * 1.0 - 1)
    assert res["allocation"] + res["selection"] + res["interaction"] == pytest.approx(res["excess"], abs=1e-12)
    assert res["residual"] == pytest.approx(0, abs=1e-12)


def test_trade_mid_period_and_unheld_sector_has_no_selection():
    ledger = [{"date": "2026-10-02", "fill_close_date": "2026-10-02", "ticker": "A", "side": "BUY", "shares": "5",
               "gross_usd": "50", "cash_change_usd": "-50.1"}]
    from attribution import SECTOR_ETF
    hist = {e: rows(100.0, 101.0, 102.0) for e in SECTOR_ETF.values()} | {"A": rows(10.0, 10.0, 10.5), "SPY": rows(1, 1, 1)}
    bench_w = {s: 1 / len(SECTOR_ETF) for s in SECTOR_ETF}
    d = daily_effects(["2026-10-01", "2026-10-02", "2026-10-03"], ledger, hist, {"A": "Energy"}, {}, 100.0, [], bench_w, 0.0)
    # the buy fills on day 1 (counted at the start): value 50 -> 50, costs 0.1 come out of cash
    assert d[0]["rp"] == pytest.approx(-0.001)
    assert d[0]["sectors"]["Utilities"]["selection"] == 0
    res = carino(d)
    assert sum(res[x] for x in ("allocation", "selection", "interaction")) == pytest.approx(res["excess"], abs=1e-12)
