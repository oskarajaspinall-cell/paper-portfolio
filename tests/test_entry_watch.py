import pytest

import entry_watch as EW


def dec(**k):
    d = {"ticker": "ABC", "decision": "AVOID", "conviction": 3, "price_at_decision": 100.0}
    d.update(k)
    return d


def test_rows_from_decisions(cfg):
    val = {"fair_value": {"base": 110.0}}
    r = EW.row_from_decision(dec(entry_price=82.5, entry_basis="P/FCF 5y low [RA]"), "e.md", "2026-10-09", cfg, val, "USD")
    assert (r["entry_price"], r["source"], r["expires"]) == (82.5, "evaluator", "2027-01-07")
    m = EW.row_from_decision(dec(), "e.md", "2026-10-09", cfg, val, "USD")  # no evaluator price: anchor
    assert m["source"] == "mechanical" and m["entry_price"] == pytest.approx(110.0 * 0.8)
    assert EW.row_from_decision(dec(entry_price=None, entry_basis="quality falling"), "e", "2026-10-09", cfg, val) is None
    assert EW.row_from_decision(dec(conviction=2), "e", "2026-10-09", cfg, val) is None
    assert EW.row_from_decision(dec(decision="BUY", conviction=4), "e", "2026-10-09", cfg, val) is None
    assert EW.row_from_decision(dec(), "e", "2026-10-09", cfg, {"fair_value": {"base": 120.0}})["entry_price"] == 96.0
    assert EW.row_from_decision(dec(), "e", "2026-10-09", cfg, {"fair_value": {"base": 130.0}}) is None  # 104 above price


def test_upsert_replaces_and_removes():
    rows = [{"ticker": "ABC", "entry_price": 80}, {"ticker": "XYZ", "entry_price": 10}]
    assert EW.upsert(rows, {"ticker": "ABC", "entry_price": 75}, "ABC") == [{"ticker": "XYZ", "entry_price": 10},
                                                                         {"ticker": "ABC", "entry_price": 75}]
    assert EW.upsert(rows, None, "ABC") == [{"ticker": "XYZ", "entry_price": 10}]


def test_daily_check_hits_and_expiry():
    rows = [{"ticker": "HIT", "entry_price": "80", "expires": "2027-01-01"},
            {"ticker": "FAR", "entry_price": "50", "expires": "2027-01-01"},
            {"ticker": "OLD", "entry_price": "999", "expires": "2026-10-01"}]
    closes = {"HIT": 79.5, "FAR": 100.0, "OLD": 1.0}
    live, hits = EW.check(rows, lambda t: {"close": closes[t], "date": "2026-10-09"}, "2026-10-10")
    assert [r["ticker"] for r in live] == ["HIT", "FAR"] and [h["ticker"] for h in hits] == ["HIT"]
    assert hits[0]["hit_date"] == "2026-10-09" and live[1]["pct_to_entry"] == pytest.approx(-50.0)
