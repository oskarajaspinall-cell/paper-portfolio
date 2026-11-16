import pytest

from cash_policy import available_cash, core_topup_reserve, min_trade, tactical_cap


def starter(t, cur, tgt, up, **limits):
    return {"ticker": t, "current": cur, "target": tgt, "upside": up, "limits": limits}


def test_available_cash_is_above_the_floor():
    assert available_cash(5_000, 100_000) == pytest.approx(0.035)
    assert available_cash(1_000, 100_000) == 0.0  # below the 1.5% floor


def test_min_trade_reconciles_with_the_starter_threshold():
    assert min_trade(0.04) == pytest.approx(0.02)   # a 4% target starts with 2%
    assert min_trade(0.12) == pytest.approx(0.025)  # a 12% target never dribbles below 2.5%


def test_shared_sector_headroom_is_reserved_once():
    # 4% sector headroom, two 3% starters: #1 reserves 3%, #2 sees 1% < min_trade (2.5%) and reserves 0
    sec = (0.04, {"A", "B"})
    total, per = core_topup_reserve([starter("A", 0.04, 0.07, 30, sector=sec), starter("B", 0.04, 0.07, 10, sector=sec)])
    assert total == pytest.approx(0.03) and per == {"A": pytest.approx(0.03), "B": 0.0}


def test_tied_upside_breaks_on_ticker():
    sec = (0.03, {"A", "B"})
    _, per = core_topup_reserve([starter("B", 0.04, 0.07, 20, sector=sec), starter("A", 0.04, 0.07, 20, sector=sec)])
    assert per["A"] == pytest.approx(0.03) and per["B"] == 0.0


def test_tiny_final_gap_reserves_only_when_it_completes_the_target():
    total, per = core_topup_reserve([starter("A", 0.068, 0.07, 5)])  # 0.2% gap < min_trade but completes it
    assert total == pytest.approx(0.002)
    # the same small amount capped by a limit (does NOT complete the gap) reserves nothing
    total, per = core_topup_reserve([starter("A", 0.04, 0.07, 5, sector=(0.002, {"A"}))])
    assert total == 0.0 and per["A"] == 0.0


def test_cap_blocked_starter_reserves_nothing_and_leaves_headroom():
    sec = (0.05, {"A", "B"})
    total, per = core_topup_reserve([starter("A", 0.04, 0.07, 30, sector=sec, country=(0.0, {"A"})),
                                     starter("B", 0.04, 0.07, 10, sector=sec)])
    assert per["A"] == 0.0 and per["B"] == pytest.approx(0.03) and total == pytest.approx(0.03)


def test_unset_upside_goes_last_and_full_positions_are_ignored():
    sec = (0.03, {"A", "B"})
    _, per = core_topup_reserve([starter("A", 0.04, 0.07, None, sector=sec), starter("B", 0.04, 0.07, -5, sector=sec),
                                 starter("C", 0.07, 0.07, 50)])
    assert per["B"] == pytest.approx(0.03) and per["A"] == 0.0 and "C" not in per


def test_tactical_cap():
    assert tactical_cap(0.30, 0.20) == pytest.approx(0.10)
    assert tactical_cap(0.30, 0.05) == pytest.approx(0.05)
    assert tactical_cap(0.45, 0.20) == 0.0


# ---- integration: the residual-cash mode in portfolio.py / funding_queue.py
import json

import portfolio as P
from portfolio import empty_state, place_orders
from test_portfolio import WATCH, OpenMarket, holding, tac_buy

TODAY = "2026-10-10"
REAL_RESERVE = P.current_reserve  # conftest's autouse fixture replaces it with a zero reserve; these tests want the real one


def residual_cfg(cfg):
    cfg["cash_strategy"]["mode"] = "residual"
    cfg["portfolio"]["min_cash_pct"] = 1.5
    return cfg


def starter_state(tmp_path, cfg, with_queue=True):
    s = empty_state(cfg)
    h = holding("AAPL", "CORE", 3, conv=4)
    h["target_pct"] = 7
    s["holdings"] = {"AAPL": h, "LON:ULVR": holding("LON:ULVR", "CORE", 87, conv=4)}
    s["cash_usd"] = 10000
    if with_queue:  # AAPL is a 3%-of-7% starter waiting for a top-up
        s["funding_queue"] = [{"ticker": "AAPL", "stage": "topup", "target_pct": 7, "added": TODAY, "expires": "2026-11-09",
                               "decision_price": 200.0, "currency": "USD", "fair_value_base": 300.0,
                               "request": {"ticker": "AAPL", "conviction": 4}}]
    sp = tmp_path / "state.json"
    sp.write_text(json.dumps(s))
    return sp


def test_residual_mode_reserve_is_just_the_floor(cfg):
    assert REAL_RESERVE(residual_cfg(cfg), TODAY)["pct"] == 1.5


def test_open_core_topup_holds_cash_back_from_a_tactical_buy(cfg, tmp_path, monkeypatch):
    monkeypatch.setattr(P, "current_reserve", REAL_RESERVE)
    residual_cfg(cfg)
    # cash 10%: a 5% tactical buy would leave 5% -- above the 1.5% floor, but AAPL's 4% top-up has first claim
    out = place_orders([tac_buy("NVDA", 130.0)], starter_state(tmp_path, cfg), OpenMarket(cfg), cfg, WATCH, TODAY,
                       dry_run=True, port_dir=tmp_path)
    assert not out["placed"] and "below the 5.4" in out["rejected"][0]["detail"]  # 1.5% floor + AAPL's 4% top-up
    # no waiting top-up: the same tactical buy goes through
    out = place_orders([tac_buy("NVDA", 130.0)], starter_state(tmp_path, cfg, with_queue=False), OpenMarket(cfg), cfg,
                       WATCH, TODAY, dry_run=True, port_dir=tmp_path)
    assert [p["ticker"] for p in out["placed"]] == ["NVDA"]


def test_telemetry_row_shows_the_reserve_and_blocked_starters(cfg, tmp_path, monkeypatch):
    import funding_queue as FQ
    monkeypatch.setattr(P, "current_reserve", REAL_RESERVE)
    residual_cfg(cfg)
    row = FQ.log_telemetry(starter_state(tmp_path, cfg), OpenMarket(cfg), cfg, WATCH, TODAY, port_dir=tmp_path)
    assert row["open_core_topup_reserve_pct"] == 4.0 and row["starters_waiting"] == 1 and row["starters_blocked_by_cap"] == 0
    assert row["available_cash_pct"] == pytest.approx(8.5, abs=0.1)   # 10% cash - 1.5% floor
    assert row["available_tactical_cap_pct"] == pytest.approx(4.5, abs=0.1)  # what is left after the core top-up
    assert (tmp_path / "cash_telemetry.csv").exists()
    assert FQ.log_telemetry(starter_state(tmp_path, cfg), OpenMarket(cfg), cfg | {"cash_strategy": {"mode": "regime"}},
                            WATCH, TODAY, port_dir=tmp_path) is None
