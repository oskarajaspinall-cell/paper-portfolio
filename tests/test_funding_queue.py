import json

import pytest

import funding_queue as FQ
import portfolio as P
from portfolio import empty_state, place_orders, read_csv
from test_portfolio import WATCH, OpenMarket, core_buy, holding

TODAY = "2026-10-10"


@pytest.fixture
def reserve20(monkeypatch):
    monkeypatch.setattr(P, "current_reserve", lambda c, a: {"pct": 20.0, "regime": "neutral", "dip_multiplier": 1.0})


@pytest.fixture(autouse=True)
def fair_values(monkeypatch):
    """Base fair values in the quote currency (no research/ files read)."""
    fv = {"AAPL": 300.0, "NVDA": 180.0, "LON:ULVR": 4200.0, "MSFT": 380.0}
    monkeypatch.setattr(FQ, "latest_valuation", lambda t, d: ({"fair_value": {"base": fv[t]}}, f"research/{t}/v.json")
                        if t in fv else (None, None))


def state_file(tmp_path, cfg, holdings, cash):
    s = empty_state(cfg)
    s["holdings"] = holdings
    s["cash_usd"] = cash
    sp = tmp_path / "state.json"
    sp.write_text(json.dumps(s))
    return sp


def tight(tmp_path, cfg):
    """$100k: ULVR 78% core, cash 22%. A 7% BUY leaves 15% < the 20% reserve; 1.5% room is too little for a
    starter (half the target)."""
    return state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 78, conv=3)}, 22000)


def test_reserve_rejection_joins_the_queue(cfg, tmp_path, reserve20):
    sp = tight(tmp_path, cfg)
    out = place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    assert out["rejected"][0]["rule"] == "REPLACEMENT_REQUIRED" and not out["placed"]
    q = json.loads(sp.read_text())["funding_queue"]
    assert [(e["ticker"], e["decision_price"], e["added"], e["expires"]) for e in q] == [
        ("AAPL", 200.0, TODAY, "2026-11-09")]
    assert q[0]["fair_value_base"] == 300.0 and q[0]["request"]["conviction"] == 4
    assert [r["event"] for r in read_csv(tmp_path / "funding_queue.csv")] == ["ADDED"]
    # the same decision submitted again doesn't reset its date
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    assert json.loads(sp.read_text())["funding_queue"][0]["added"] == TODAY


def test_only_cash_breaches_and_high_conviction_queue(cfg, tmp_path, reserve20):
    cfg["core"]["min_buy_conviction"] = 4
    sp = tight(tmp_path, cfg)
    place_orders([core_buy("AAPL", conv=3)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    assert not json.loads(sp.read_text()).get("funding_queue")
    # a sector cap needs a sale, not cash: not queued
    hold = {"AAPL": holding("AAPL", "CORE", 10, conv=5), "MSFT": holding("MSFT", "CORE", 12, conv=5)}
    sp = state_file(tmp_path, cfg, hold, 78000)
    out = place_orders([core_buy("NVDA", conv=5)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    assert out["rejected"][0]["rule"] == "REPLACEMENT_REQUIRED"
    assert not json.loads(sp.read_text()).get("funding_queue")


def test_review_resubmits_when_room_appears(cfg, tmp_path, reserve20):
    sp = tight(tmp_path, cfg)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    # still no room: keeps waiting, nothing ordered
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    assert [w["ticker"] for w in out["waiting"]] == ["AAPL"] and not out["resubmitted"]
    s = json.loads(sp.read_text())
    assert not s.get("pending") and s["funding_queue"][0]["last_close"] == 200.0
    # cash arrives (e.g. a sale): the idea is queued for the next open and leaves the funding queue
    s["cash_usd"] += 10000
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-13", port_dir=tmp_path)
    assert [r["ticker"] for r in out["resubmitted"]] == ["AAPL"]
    s = json.loads(sp.read_text())
    assert [o["request"]["ticker"] for o in s["pending"]] == ["AAPL"] and s["funding_queue"] == []
    assert "funding queue: decided 2026-10-10" in s["pending"][0]["request"]["reason"]
    assert [r["event"] for r in read_csv(tmp_path / "funding_queue.csv")] == ["ADDED", "RESUBMITTED"]


def test_review_ranks_by_upside_and_fills_the_best_first(cfg, tmp_path, reserve20):
    sp = state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 75, conv=3)}, 25000)
    place_orders([core_buy("NVDA", conv=4), core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY,
                 port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["cash_usd"] += 4000  # room for exactly one 7% position above the 20% reserve
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    assert [r["ticker"] for r in out["resubmitted"]] == ["NVDA"]  # +80% upside beats AAPL's +50%
    assert [w["ticker"] for w in out["waiting"]] == ["AAPL"]


def test_review_drops_stale_ideas(cfg, tmp_path, reserve20):
    sp = tight(tmp_path, cfg)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["funding_queue"][0]["decision_price"] = 180.0  # the close (200) is now +11% above it
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    assert out["dropped"][0]["ticker"] == "AAPL" and "too stale" in out["dropped"][0]["reason"]
    assert json.loads(sp.read_text())["funding_queue"] == []
    sp = tight(tmp_path, cfg)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-11-10", port_dir=tmp_path)
    assert "waited 30 days" in out["dropped"][0]["reason"]


def test_dry_run_review_changes_nothing(cfg, tmp_path, reserve20):
    sp = tight(tmp_path, cfg)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["cash_usd"] += 10000
    sp.write_text(json.dumps(s))
    before = sp.read_text()
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", dry_run=True, port_dir=tmp_path)
    assert [r["ticker"] for r in out["resubmitted"]] == ["AAPL"] and sp.read_text() == before


def test_swap_brief_and_answer(cfg, tmp_path, reserve20):
    hold = {"LON:ULVR": holding("LON:ULVR", "CORE", 40, conv=3), "LON:SHEL": holding("LON:SHEL", "CORE", 35, conv=4)}
    sp = state_file(tmp_path, cfg, hold, 25000)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    s = json.loads(sp.read_text())
    mkt = OpenMarket(cfg)
    P.mark(s, mkt)
    md, allowed = FQ.brief(s, mkt, cfg, TODAY)
    assert allowed == {"buy": "AAPL", "candidates": ["LON:ULVR", "LON:SHEL"]}  # conviction 3 first
    assert "| AAPL | 4 |" in md and "| 50.0% |" in md
    ok = '```json\n{"swap": true, "buy": "AAPL", "replaces": "LON:ULVR", "replacement_reason": "higher ROIC, cheaper"}\n```'
    sw = FQ.parse_swap(ok, allowed)
    assert sw["replaces"] == "LON:ULVR"
    assert FQ.parse_swap('```json\n{"swap": false}\n```', allowed) is None
    with pytest.raises(ValueError):
        FQ.parse_swap(ok.replace("LON:ULVR", "NVDA"), allowed)
    req = FQ.swap_request(s, sw)
    out = place_orders([req], sp, mkt, cfg, WATCH, TODAY, port_dir=tmp_path)
    assert [p["ticker"] for p in out["placed"]] == ["AAPL"] and out["placed"][0]["replaces"] == "LON:ULVR"
    assert json.loads(sp.read_text())["funding_queue"] == []


def test_starter_position_then_top_up(cfg, tmp_path, reserve20):
    from portfolio import fill_pending
    sp = state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 75, conv=3)}, 25000)  # 4.5% room
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    st = out["started"][0]
    assert st["ticker"] == "AAPL" and 4.0 <= st["starter_pct"] <= 4.5 and st["target_pct"] == 7
    s = json.loads(sp.read_text())
    assert [o["request"]["funding_stage"] for o in s["pending"]] == ["starter"]
    assert s["funding_queue"][0]["stage"] == "topup"  # the rest waits
    # while the starter order waits for its open, nothing else happens
    assert FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)["waiting"][0]["reason"].startswith("starter")
    fill_pending(sp, OpenMarket(cfg, opens={"AAPL": [("2026-10-13", 200.0)]}, asof="2026-10-14"), cfg, WATCH,
                 port_dir=tmp_path)
    s = json.loads(sp.read_text())
    h = s["holdings"]["AAPL"]
    assert h["target_pct"] == 7 and 4.0 <= h["market_value_usd"] / 1000 <= 4.6  # ~4.3% of ~$100k, target kept
    # 1.5% of new room: a top-up step, still not complete
    s["cash_usd"] += 1500
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg, asof="2026-10-14"), cfg, WATCH, "2026-10-14", port_dir=tmp_path)
    tu = out["topped_up"][0]
    assert tu["ticker"] == "AAPL" and not tu["complete"] and tu["to_pct"] < 7
    s = json.loads(sp.read_text())
    assert s["pending"][-1]["request"]["action"] == "ADD" and s["funding_queue"][0]["stage"] == "topup"
    events = [r["event"] for r in read_csv(tmp_path / "funding_queue.csv")]
    assert events == ["ADDED", "STARTER", "TOPUP_STEP"]


def test_top_up_completes_and_leaves_the_queue(cfg, tmp_path, reserve20):
    from portfolio import fill_pending
    sp = state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 75, conv=3)}, 25000)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    fill_pending(sp, OpenMarket(cfg, opens={"AAPL": [("2026-10-13", 200.0)]}, asof="2026-10-14"), cfg, WATCH,
                 port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["cash_usd"] += 10000
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg, asof="2026-10-14"), cfg, WATCH, "2026-10-14", port_dir=tmp_path)
    assert out["topped_up"][0]["complete"] and json.loads(sp.read_text())["funding_queue"] == []


def test_top_up_is_dropped_when_the_price_runs_away(cfg, tmp_path, reserve20):
    sp = state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 75, conv=3)}, 25000)
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["funding_queue"][0]["decision_price"] = 170.0  # close 200 = +17.6%
    s["pending"] = []
    s["holdings"]["AAPL"] = holding("AAPL", "CORE", 4.5)
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-13", port_dir=tmp_path)
    assert "stays at its starter size" in out["dropped"][0]["reason"]


def test_one_starter_at_a_time(cfg, tmp_path, reserve20):
    sp = state_file(tmp_path, cfg, {"LON:ULVR": holding("LON:ULVR", "CORE", 70, conv=3)}, 30000)  # 9.5% room
    s = json.loads(sp.read_text())
    s["cash_usd"] = 22000  # enqueue both while there's no room...
    sp.write_text(json.dumps(s))
    place_orders([core_buy("NVDA", conv=4), core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, TODAY,
                 port_dir=tmp_path)
    s = json.loads(sp.read_text())
    s["cash_usd"] = 25000  # ...then 4.5% of room: one starter, not two
    sp.write_text(json.dumps(s))
    out = FQ.review(sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", dry_run=True, port_dir=tmp_path)
    assert [x["ticker"] for x in out["started"]] == ["NVDA"]
