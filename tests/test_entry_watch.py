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


def test_intraday_window(cfg):
    import datetime as dt
    assert EW.in_check_window(dt.datetime(2026, 10, 9, 10, 31), cfg)       # Friday 10:31 New York
    assert not EW.in_check_window(dt.datetime(2026, 10, 9, 9, 31), cfg)    # the UK-time run an hour early
    assert not EW.in_check_window(dt.datetime(2026, 10, 10, 10, 31), cfg)  # Saturday


def test_intraday_hits_us_only_and_today_only():
    from common import DataError
    rows = [{"ticker": "HIT", "entry_price": "50"}, {"ticker": "ABOVE", "entry_price": "50"},
            {"ticker": "STALE", "entry_price": "50"}, {"ticker": "NSE:TCS", "entry_price": "9999"},
            {"ticker": "GONE", "entry_price": "50"}, {"ticker": "OLD", "entry_price": "50", "expires": "2026-01-01"}]
    px = {"HIT": (49.5, "2026-10-09"), "ABOVE": (51.0, "2026-10-09"), "STALE": (10.0, "2026-10-08"),
          "OLD": (1.0, "2026-10-09")}

    def price(t):
        if t not in px:
            raise DataError("u", "f", "none")
        p, d = px[t]
        return {"price": p, "date": d, "time": f"{d}T10:31:00-04:00", "url": "u"}
    hits, notes = EW.intraday_hits(rows, price, "2026-10-09")
    assert [h["ticker"] for h in hits] == ["HIT"] and hits[0]["intraday"] and hits[0]["time"] == "10:31 ET"
    assert any("STALE" in n for n in notes) and any("GONE" in n for n in notes)  # TCS (not US) never fetched


def test_daily_check_keeps_unresearched_intraday_hits():
    old = [{"ticker": "A", "intraday": True}, {"ticker": "B", "intraday": True}]
    pending = {"A"}  # B's row was replaced by a re-research
    kept = EW.merge_hits([{"ticker": "C"}], [h for h in old if h["ticker"] in pending])
    assert [h["ticker"] for h in kept] == ["C", "A"]


def test_entry_research_todo(tmp_path):
    import entry_research as ER
    (tmp_path / "research" / "DONE").mkdir(parents=True)
    (tmp_path / "research" / "DONE" / "2026-10-09-evaluation.md").write_text("x")
    st = {"holdings": {"HELD": {}}, "entry_hits": [
        {"ticker": "A", "intraday": True}, {"ticker": "HELD", "intraday": True}, {"ticker": "DONE", "intraday": True},
        {"ticker": "CLOSE"}, {"ticker": "B", "intraday": True}, {"ticker": "C", "intraday": True}]}
    assert [h["ticker"] for h in ER.todo(st, "2026-10-09", 3, tmp_path)] == ["A", "B", "C"]
    (tmp_path / "runs" / "2026-10-09-entry").mkdir(parents=True)
    (tmp_path / "runs" / "2026-10-09-entry" / "done-X").write_text("")
    assert [h["ticker"] for h in ER.todo(st, "2026-10-09", 3, tmp_path)] == ["A", "B"]  # daily cap


def test_entry_hit_reason():
    import weekly_run as wr
    assert "traded at 49.5 at 10:31 ET" in wr.entry_hit_reason({"entry_price": 50, "close": 49.5, "intraday": True,
                                                                 "time": "10:31 ET", "hit_date": "2026-10-09"})
    assert "closed at 49.5 on 2026-10-09" in wr.entry_hit_reason({"entry_price": 50, "close": 49.5, "hit_date": "2026-10-09"})
