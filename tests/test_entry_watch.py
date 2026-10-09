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
    live, hits, _ = EW.check(rows, lambda t: {"close": closes[t], "date": "2026-10-09"}, "2026-10-10")
    assert [r["ticker"] for r in live] == ["HIT", "FAR"] and [h["ticker"] for h in hits] == ["HIT"]
    assert hits[0]["hit_date"] == "2026-10-09" and live[1]["pct_to_entry"] == pytest.approx(-50.0)


def test_close_to_entry_band():
    rows = [{"ticker": "NEAR", "entry_price": "95", "expires": "2027-01-01"},
            {"ticker": "HIT", "entry_price": "80", "expires": "2027-01-01", "near_since": "2026-10-01"},
            {"ticker": "LEFT", "entry_price": "50", "expires": "2027-01-01", "near_since": "2026-10-01"},
            {"ticker": "EDGE", "entry_price": "90", "expires": "2027-01-01"}]
    closes = {"NEAR": 100.0, "HIT": 79.0, "LEFT": 100.0, "EDGE": 100.0}
    live, hits, entered = EW.check(rows, lambda t: {"close": closes[t], "date": "2026-10-09"}, "2026-10-09", 10)
    by = {r["ticker"]: r for r in live}
    assert [r["ticker"] for r in entered] == ["NEAR", "EDGE"]  # HIT was already in the band: no second alert
    assert by["NEAR"]["near_since"] == "2026-10-09" and by["HIT"]["near_since"] == "2026-10-01"
    assert by["LEFT"]["near_since"] == ""  # left the band
    assert [r["ticker"] for r in EW.near(live, 10)] == ["HIT", "NEAR", "EDGE"]  # -10.0% is inside
    _, _, again = EW.check(live, lambda t: {"close": closes[t], "date": "2026-10-10"}, "2026-10-10", 10)
    assert again == []


def test_why_not_yet_reads_rationale(tmp_path, monkeypatch):
    ev = tmp_path / "e.md"
    ev.write_text('x\n```json\n{"rationale": "' + "Leverage is rising. " * 20 + '"}\n```\n')
    monkeypatch.setattr(EW, "ROOT", tmp_path)
    w = EW.why_not_yet({"evaluation": "e.md"}, 60)
    assert w.startswith("Leverage is rising.") and w.endswith("…") and len(w) <= 60
    assert EW.why_not_yet({"evaluation": "missing.md"}) == ""
