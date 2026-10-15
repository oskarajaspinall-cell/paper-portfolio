"""Dividends and stock splits (owner request 2026-10-16)."""
import csv
import math

import pytest

from conftest import FIX
from common import DataError
from corporate_actions import check, parse_split_stats, shares_before
from decision_log import split_factor
from entry_watch import adjust_splits
from fetch_data import page_nodes, parse_amount, parse_dividends
from portfolio import VAL_COLS, append_csv, empty_state, invested_series, read_csv, totals

CFG = {"corporate_actions": {"withholding_pct": {"USD": 15, "default": 0}},
       "portfolio": {"starting_cash_usd": 100000}}


# ------------------------------------------------------------------ parsing
@pytest.mark.parametrize("name,ccy,empty", [("ci", "USD", False), ("deck", None, True), ("hk9999", "HKD", False),
                                            ("spy", "USD", False)])
def test_parse_dividend_pages(name, ccy, empty):
    path = FIX / f"{name}_dividend.html"
    if not path.exists():
        pytest.skip("saved page not present (fixtures stay local)")
    url = f"https://stockanalysis.com/x/{name}/dividend/"
    rows = parse_dividends(page_nodes(path.read_text(), url), url)["rows"]
    assert (rows == []) == empty
    if rows:
        r = rows[0]
        assert r["currency"] == ccy and r["amount"] > 0 and r["ex_date"][:2] == "20"
        assert r["pay_date"] is None or r["pay_date"] >= r["ex_date"]


def test_parse_amount():
    assert parse_amount("$1.560", "u") == (1.56, "USD")
    assert parse_amount("0.75272 HKD", "u") == (0.75272, "HKD")
    assert parse_amount("1,200.5 JPY", "u") == (1200.5, "JPY")
    for bad in ("1.5", "n/a", "", None):
        with pytest.raises(DataError):
            parse_amount(bad, "u")


def test_parse_dividends_format_change_is_an_error():
    with pytest.raises(DataError):
        parse_dividends([{"somethingElse": []}], "u")


def test_parse_split_stats():
    st = {"lastSplitDate": {"text": "Jun 10, 2024"}, "splitRatio": {"text": "10:1"}}
    assert parse_split_stats(st) == ("2024-06-10", 10.0)
    assert parse_split_stats({"lastSplitDate": {"text": "Jan 2, 2026"}, "splitRatio": {"text": "1:10"}})[1] == 0.1
    assert parse_split_stats({}) is None


# ------------------------------------------------------------------ helpers
class FakeMkt:
    def __init__(self, rows=None, source="yfinance", px=50.0):
        self.rows, self.source, self.px = rows or {}, source, px

    def history(self, t):
        r = self.rows.get(t, [{"date": "2026-10-01", "close": 100.0}])
        return {"url": f"https://finance.yahoo.com/quote/{t}/history", "rows": r, "all_rows": r, "source": self.source}

    def quote(self, t, on_or_before=None):
        return {"price_usd": self.px, "close": self.px, "date": on_or_before}

    def fx(self, ccy):
        return {"rate": 0.128}


def holding(t, shares, typ="CORE", **kw):
    return {t: {"type": typ, "shares": shares, "entry_date": "2026-10-08", "entry_close_date": "2026-10-08",
                "entry_price": 100.0, "last_close": 100.0, "market_value_usd": shares * 100.0,
                "cost_basis_usd": shares * 100.0, "sector": "X", **kw}}


def buy(t, day, shares, typ="CORE"):
    return {"date": day, "ticker": t, "type": typ, "side": "BUY", "shares": str(shares), "fill_close_date": day,
            "cash_change_usd": str(-shares * 100.0)}


def state_with(h):
    s = empty_state(CFG)
    s["holdings"] = h
    s["cash_usd"] = 1000.0
    return s


def divs(rows, url="https://stockanalysis.com/stocks/x/dividend/"):
    return lambda t: {"url": url, "rows": rows.get(t, [])}


def no_stats(t):
    raise AssertionError("statistics page should not be needed")


# ------------------------------------------------------------------ dividends
def test_bought_on_ex_date_gets_nothing():
    s = state_with(holding("INTU", 23))
    out = check(s, [buy("INTU", "2026-10-08", 23)], [], FakeMkt(), CFG, "2026-10-17",
                divs({"INTU": [{"ex_date": "2026-10-08", "amount": 1.38, "currency": "USD", "pay_date": "2026-10-16"}]}),
                no_stats)
    assert out["ca"] == [] and s.get("receivables") == [] and s["cash_usd"] == 1000.0


def test_dividend_receivable_then_paid_net_of_withholding():
    s = state_with(holding("ZTS", 98))
    ledger = [buy("ZTS", "2026-10-08", 98)]
    d = divs({"ZTS": [{"ex_date": "2026-10-30", "amount": 0.53, "currency": "USD", "pay_date": "2026-12-01"}]})
    # before the ex-date: listed as upcoming only
    out = check(s, ledger, [], FakeMkt(), CFG, "2026-10-29", d, no_stats)
    assert out["ca"] == [] and out["upcoming"][0]["ticker"] == "ZTS"
    # ex-date passed: a receivable that counts in the value, not yet cash
    before = totals(s)["total"]
    out = check(s, ledger, [], FakeMkt(), CFG, "2026-10-31", d, no_stats)
    net = round(98 * 0.53 * 0.85, 2)
    assert [r["kind"] for r in out["ca"]] == ["DIVIDEND"] and s["receivables"][0]["net_usd"] == net == 44.15
    assert s["cash_usd"] == 1000.0 and totals(s)["total"] == pytest.approx(before + net)
    assert s["flows"]["CORE"]["income"] == net
    # a re-run on the same day changes nothing, even if the log row was lost (the receivable itself is the guard)
    ca = out["ca"]
    assert check(s, ledger, ca, FakeMkt(), CFG, "2026-10-31", d, no_stats)["ca"] == []
    assert check(s, ledger, [], FakeMkt(), CFG, "2026-10-31", d, no_stats)["ca"] == [] and len(s["receivables"]) == 1
    # pay date passed: receivable -> cash, a DIVIDEND ledger row dated the pay date
    out = check(s, ledger, ca, FakeMkt(), CFG, "2026-12-02", d, no_stats)
    assert s["receivables"] == [] and s["cash_usd"] == pytest.approx(1000.0 + net)
    row = out["ledger"][0]
    assert row["side"] == "DIVIDEND" and row["fill_close_date"] == "2026-12-01" and row["cash_change_usd"] == net
    assert totals(s)["total"] == pytest.approx(before + net)


def test_missed_days_catch_up_in_one_run():
    s = state_with(holding("HKG:9999", 295))
    out = check(s, [buy("HKG:9999", "2026-10-06", 295)], [], FakeMkt(), CFG, "2026-12-20",
                divs({"HKG:9999": [{"ex_date": "2026-11-02", "amount": 0.75, "currency": "HKD", "pay_date": "2026-11-15"}]}),
                no_stats)
    net = round(295 * 0.75 * 0.128, 2)  # HKD: no withholding by default, converted at the stockanalysis.com rate
    assert [r["kind"] for r in out["ca"]] == ["DIVIDEND", "DIVIDEND_PAID"] and s["cash_usd"] == pytest.approx(1000 + net)


def test_unreadable_dividend_page_is_skipped_not_fatal():
    s = state_with(holding("CI", 25))

    def bad(t):
        raise DataError("https://stockanalysis.com/stocks/ci/dividend/", "network", "down")
    out = check(s, [buy("CI", "2026-10-09", 25)], [], FakeMkt(), CFG, "2026-10-17", bad, no_stats)
    assert out["ca"] == [] and "CI" in out["notes"][0]


def test_shares_before_counts_trades_and_splits():
    led = [buy("A", "2026-10-01", 10), {"ticker": "A", "side": "TRIM", "shares": "4", "fill_close_date": "2026-10-05",
                                         "date": "2026-10-05"},
           {"ticker": "A", "side": "SPLIT", "shares": "6", "fill_close_date": "2026-10-10", "date": "2026-10-10"}]
    assert shares_before(led, "A", "2026-10-01") == 0
    assert shares_before(led, "A", "2026-10-06") == 6
    assert shares_before(led, "A", "2026-10-11") == 12


# ------------------------------------------------------------------ splits
def test_two_for_one_split_adjusts_shares_and_prices_value_unchanged():
    plan = {"stop": 90.0, "target": 130.0, "time_limit": "2026-12-01"}
    s = state_with(holding("T", 10, "TACTICAL", exit_plan=plan))
    s["baseline"] = {"start": "2026-10-07", "frozen_from": "2026-10-14", "cash_usd": 0.0, "holdings": {"T": {"shares": 10}}}
    mkt = FakeMkt({"T": [{"date": "2026-10-20", "close": 50.0, "split": 2.0}]}, px=50.0)
    stats = {"lastSplitDate": {"text": "Oct 20, 2026"}, "splitRatio": {"text": "2:1"}}
    out = check(s, [buy("T", "2026-10-08", 10, "TACTICAL")], [], mkt, CFG, "2026-10-21", divs({}), lambda t: stats)
    h = s["holdings"]["T"]
    assert h["shares"] == 20 and h["entry_price"] == 50.0 and h["exit_plan"]["stop"] == 45.0
    assert h["exit_plan"]["target"] == 65.0 and h["cost_basis_usd"] == 1000.0
    assert h["shares"] * 50.0 == 10 * 100.0  # same value at the post-split close
    assert s["baseline"]["holdings"]["T"]["shares"] == 20 and s["cash_usd"] == 1000.0
    assert out["ledger"][0]["side"] == "SPLIT" and out["ledger"][0]["shares"] == 10
    # applied once
    assert check(s, [], out["ca"], mkt, CFG, "2026-10-22", divs({}), lambda t: stats)["ca"] == []


def test_reverse_split_pays_the_fraction_in_cash():
    s = state_with(holding("R", 25))
    mkt = FakeMkt({"R": [{"date": "2026-10-20", "close": 40.0, "split": 0.1}]}, px=40.0)
    stats = {"lastSplitDate": {"text": "Oct 20, 2026"}, "splitRatio": {"text": "1:10"}}
    check(s, [buy("R", "2026-10-08", 25)], [], mkt, CFG, "2026-10-21", divs({}), lambda t: stats)
    assert s["holdings"]["R"]["shares"] == 2 and s["cash_usd"] == pytest.approx(1000 + 0.5 * 40.0)


def test_split_sources_disagree_stops_the_run():
    s = state_with(holding("T", 10))
    mkt = FakeMkt({"T": [{"date": "2026-10-20", "close": 50.0, "split": 2.0}]})
    with pytest.raises(DataError):
        check(s, [], [], mkt, CFG, "2026-10-21", divs({}), lambda t: {})
    assert s["holdings"]["T"]["shares"] == 10


def test_split_before_purchase_is_ignored():
    s = state_with(holding("T", 10))
    mkt = FakeMkt({"T": [{"date": "2026-06-10", "close": 50.0, "split": 10.0}]})
    assert check(s, [], [], mkt, CFG, "2026-10-21", divs({}), no_stats)["ca"] == []


def test_watchlist_entry_price_split_adjusted_once():
    rows = [{"ticker": "W", "entry_price": "80", "set_date": "2026-10-10"}]
    hist = lambda t: {"rows": [{"date": "2026-10-20", "close": 45.0, "split": 2.0}]}  # noqa: E731
    assert len(adjust_splits(rows, hist, "2026-10-21")) == 1 and rows[0]["entry_price"] == 40.0
    assert adjust_splits(rows, hist, "2026-10-22") == [] and rows[0]["entry_price"] == 40.0


def test_decision_scoring_split_factor():
    class M:
        def history(self, t):
            return {"rows": [{"date": "2026-10-20", "split": 2.0}, {"date": "2026-10-21", "close": 1}]}
    assert split_factor(M(), "T", "2026-10-10", "2026-11-10") == 2.0
    assert split_factor(M(), "T", "2026-10-20", "2026-11-10") == 1.0
    assert split_factor(object(), "T", "2026-10-10", "2026-11-10") == 1.0


# ------------------------------------------------------------------ returns and storage
def v(date, core, cin, income=0, spy=100, div=""):
    return {"date": date, "core_usd": core, "core_in": cin, "core_out": 0, "tactical_usd": 0, "tactical_in": 0,
            "tactical_out": 0, "core_income": income, "tactical_income": 0, "spy_close": spy, "spy_div_cum": div}


def test_invested_return_counts_dividends_and_spy_dividends():
    vals = [v("2026-10-06", 10000, 10000, spy=100, div=0), v("2026-10-31", 10000, 10000, income=50, spy=100, div=1.0)]
    last = invested_series(vals)[-1]
    assert last["dividends"] == 50 and last["pct"] == pytest.approx(0.005)
    assert last["spy_pct"] == pytest.approx(100 * 1.0 / 10000)  # 100 SPY units x $1 dividend


def test_old_valuation_rows_without_the_new_columns_still_work():
    old = {"date": "2026-10-06", "core_usd": "10000", "core_in": "10000", "core_out": "0", "tactical_usd": "0",
           "tactical_in": "0", "tactical_out": "0", "spy_close": "100"}
    assert invested_series([old])[-1]["pct"] == 0


def test_append_csv_migrates_a_file_to_new_columns(tmp_path):
    p = tmp_path / "valuations.csv"
    old_cols = VAL_COLS[:12]
    append_csv(p, old_cols, [{c: "1" for c in old_cols}])
    append_csv(p, VAL_COLS, [{c: "2" for c in VAL_COLS}])
    rows = read_csv(p)
    with p.open() as fh:
        assert next(csv.reader(fh)) == VAL_COLS
    assert rows[0]["spy_div_cum"] == "" and rows[0]["total_usd"] == "1" and rows[1]["spy_div_cum"] == "2"
    assert math.isclose(float(rows[1]["core_income"]), 2)
