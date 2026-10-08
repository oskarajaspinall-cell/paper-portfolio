import copy
import json
from pathlib import Path

import pytest

from conftest import FakeMarket, FixtureFetcher
from common import DataError
from portfolio import (Engine, Market, chain, empty_state, interval_return, mark, read_csv, returns_table, run_submit,
                       totals, trade_costs)

TODAY = "2026-10-06"
PRICES = {  # close, currency, sector.  FakeMarket fixes USD per GBP at 1.25
    "AAPL": (200.0, "USD", "Technology"),     # $200.00
    "MSFT": (400.0, "USD", "Technology"),
    "NVDA": (100.0, "USD", "Technology"),
    "LON:SHEL": (3000.0, "GBX", "Energy"),    # 3000p = £30.00 = $37.50
    "LON:BP": (500.0, "GBX", "Energy"),       # $6.25
    "LON:ULVR": (4000.0, "GBX", "Consumer Staples"),
    "BIG": (800000.0, "USD", "Financials"),   # $800,000 per share
    "SPY": (500.0, "USD", None),
}
WATCH = {t: None for t in PRICES}


def core_buy(t, conv=4, **kw):
    r = {"ticker": t, "action": "BUY", "position_type": "CORE", "conviction": conv, "reason": "test",
         "thesis": "good business, cheap", "research_note": f"research/{t}/x.md",
         "triggers": [{"text": "ROIC < 15%"}, {"text": "gross margin < 40%"}]}
    r.update(kw)
    return r


def tac_buy(t, target, conviction=3, **kw):
    r = {"ticker": t, "action": "BUY", "position_type": "TACTICAL", "conviction": conviction, "reason": "catalyst",
         "thesis": "Q3 results 2026-10-29", "exit_plan": {"target": target}}
    r.update(kw)
    return r


def holding(t, ptype, weight_pct, pv=100000.0, conv=4):
    c, ccy, sector = PRICES[t]
    usd = c / 100 * 1.25 if ccy == "GBX" else c
    shares = round(weight_pct / 100 * pv / usd)
    return {"type": ptype, "shares": shares, "currency": ccy, "sector": sector, "cost_basis_usd": shares * usd,
            "conviction": conv, "thesis": "x", "triggers": [{"text": "a"}, {"text": "b"}] if ptype == "CORE" else None,
            "exit_plan": {"target": c * 1.2, "stop": c * 0.9, "time_limit": "2026-12-01"} if ptype == "TACTICAL" else None,
            "entry_date": "2026-09-01", "entry_price": c, "market_value_usd": shares * usd}


def engine(cfg, holdings=None, cash=None, prices=None, watch=None):
    s = empty_state(cfg)
    mkt = FakeMarket({**PRICES, **(prices or {})}, cfg)
    for t, h in (holdings or {}).items():
        s["holdings"][t] = h
    # default: cash balances the portfolio to exactly $100,000
    s["cash_usd"] = cash if cash is not None else 100000 - sum(h["market_value_usd"] for h in s["holdings"].values())
    mark(s, mkt)
    return Engine(s, mkt, cfg, watch or WATCH, TODAY)


def only_rule(e):
    assert not e.applied, e.ledger
    assert len(e.rejections) == 1, e.rejections
    return e.rejections[0]["rule"]


# ------------------------------------------------------------------ costs
def test_costs_us_buy(cfg):
    c = trade_costs(7000.00, "USD", cfg)
    assert c == {"spread_usd": 7.00, "fx_fee_usd": 0.0, "costs_usd": 7.00}  # USD share: no FX fee


def test_costs_uk_share_has_fx_fee_no_stamp(cfg):
    c = trade_costs(4987.50, "GBX", cfg)
    assert c == {"spread_usd": 4.99, "fx_fee_usd": 7.48, "costs_usd": 12.47}
    assert "stamp_usd" not in c


def test_core_buy_sizing_and_cash(cfg):
    e = engine(cfg)
    e.process([core_buy("AAPL", conv=4)])  # 7% of $100,000 = $7,000 / $200 = 35 shares
    row = e.ledger[0]
    assert (row["shares"], row["gross_usd"], row["costs_usd"]) == (35, 7000.00, 7.00)
    assert e.s["cash_usd"] == pytest.approx(100000 - 7000 - 7.00)
    h = e.s["holdings"]["AAPL"]
    assert h["type"] == "CORE" and h["cost_basis_usd"] == pytest.approx(7007.00) and h["sector"] == "Technology"
    assert row["fill_close_date"] == "2026-10-05" and row["source_url"].startswith("https://stockanalysis.com/")


def test_uk_buy_and_sell(cfg):
    e = engine(cfg)
    e.process([core_buy("LON:SHEL", conv=3)])  # 5% = $5,000 / $37.50 = 133 shares
    assert e.ledger[0]["shares"] == 133 and e.ledger[0]["gross_usd"] == 4987.50 and e.ledger[0]["costs_usd"] == 12.47
    assert e.ledger[0]["fx_usd_per_unit"] == 0.0125  # USD per penny (= $1.25 per GBP)
    cash = e.s["cash_usd"]
    e.process([{"ticker": "LON:SHEL", "action": "SELL", "position_type": "CORE", "reason": "trigger"}])
    assert e.ledger[-1]["cash_change_usd"] == pytest.approx(4987.50 - 12.47)
    assert e.s["cash_usd"] == pytest.approx(cash + 4975.03) and "LON:SHEL" not in e.s["holdings"]


def test_trim_core_to_conviction_size(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "CORE", 10, conv=5)})
    e.process([{"ticker": "AAPL", "action": "TRIM", "position_type": "CORE", "conviction": 3, "reason": "less sure"}])
    tt = totals(e.s)
    assert e.s["holdings"]["AAPL"]["market_value_usd"] / tt["total"] * 100 == pytest.approx(5, abs=0.2)


# ------------------------------------------------------------------ every validation rule
@pytest.mark.parametrize("req", [
    {"ticker": "AAPL", "action": "BUY", "position_type": "CORE", "conviction": 3},             # no reason
    {"ticker": "AAPL", "action": "HODL", "position_type": "CORE", "conviction": 3, "reason": "x"},
    {"ticker": "AAPL", "action": "BUY", "position_type": "SWING", "conviction": 3, "reason": "x"},
    {"ticker": "AAPL", "action": "BUY", "position_type": "CORE", "conviction": 7, "reason": "x"},
])
def test_rule_schema(cfg, req):
    e = engine(cfg)
    e.process([req])
    assert only_rule(e) == "SCHEMA"


def test_rule_watchlist(cfg):
    e = engine(cfg, watch={"MSFT": None})
    e.process([core_buy("AAPL")])
    assert only_rule(e) == "WATCHLIST"


def test_rule_already_held(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "CORE", 5)})
    e.process([core_buy("AAPL")])
    assert only_rule(e) == "ALREADY_HELD"


def test_rule_not_held(cfg):
    e = engine(cfg)
    e.process([{"ticker": "AAPL", "action": "SELL", "position_type": "CORE", "reason": "x"}])
    assert only_rule(e) == "NOT_HELD"


def test_rule_label_fixed_on_add(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "TACTICAL", 3)})
    e.process([{"ticker": "AAPL", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert only_rule(e) == "LABEL_FIXED"


def test_rule_label_fixed_no_relabel_without_core_initiation(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "TACTICAL", 3)})
    e.process([core_buy("AAPL")])
    assert only_rule(e) == "LABEL_FIXED"


def test_tactical_becomes_core_only_via_core_initiation(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "TACTICAL", 3)})
    e.process([core_buy("AAPL", conv=4, core_initiation=True)])
    h = e.s["holdings"]["AAPL"]
    assert h["type"] == "CORE" and h["entry_date"] == TODAY and h["exit_plan"] is None
    assert [r["side"] for r in e.ledger] == ["CONVERT", "ADD"]
    assert h["market_value_usd"] / totals(e.s)["total"] * 100 == pytest.approx(7, abs=0.2)


def test_rule_conviction_one_is_no_position(cfg):
    e = engine(cfg)
    e.process([core_buy("AAPL", conv=1)])
    assert only_rule(e) == "CONVICTION_NO_POSITION"


@pytest.mark.parametrize("n", [1, 5])
def test_rule_core_triggers(cfg, n):
    e = engine(cfg)
    e.process([core_buy("AAPL", triggers=[{"text": f"t{i}"} for i in range(n)])])
    assert only_rule(e) == "CORE_TRIGGERS"


def test_rule_core_size_add_must_increase(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "CORE", 7)})
    e.process([{"ticker": "AAPL", "action": "ADD", "position_type": "CORE", "conviction": 3, "reason": "x"}])
    assert only_rule(e) == "CORE_SIZE"


def test_rule_core_position_max(cfg):
    cfg = copy.deepcopy(cfg)
    cfg["core"]["conviction_size_pct"]["5"] = 20
    e = engine(cfg, {"AAPL": holding("AAPL", "CORE", 7)})
    e.process([{"ticker": "AAPL", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert only_rule(e) == "CORE_POSITION_MAX"


def test_tactical_defaults_filled(cfg):
    e = engine(cfg)
    e.process([tac_buy("NVDA", target=120)])
    ep = e.s["holdings"]["NVDA"]["exit_plan"]
    assert ep["stop"] == pytest.approx(90.0) and ep["time_limit"] == "2027-01-06" and ep["target"] == 120
    w = e.s["holdings"]["NVDA"]["market_value_usd"] / totals(e.s)["total"] * 100
    assert 4.9 < w <= 5.0  # full-size tactical lands at/below the cap after its own costs


@pytest.mark.parametrize("plan", [
    {},                                                         # no target
    {"target": 120, "stop": 105},                               # stop above close
    {"target": 95},                                             # target below close
    {"target": 120, "time_limit": "2027-03-01"},                # beyond 3 months
    {"target": 120, "time_limit": "2026-10-01"},                # in the past
])
def test_rule_tactical_exit_plan(cfg, plan):
    e = engine(cfg)
    e.process([tac_buy("NVDA", target=None, exit_plan=plan)])
    assert only_rule(e) == "TACTICAL_EXIT_PLAN"


def test_rule_tactical_position_max(cfg):
    e = engine(cfg)
    e.process([tac_buy("NVDA", target=120, target_weight_pct=6)])
    assert only_rule(e) == "TACTICAL_POSITION_MAX"


def four_tactical():
    return {"LON:BP": holding("LON:BP", "TACTICAL", 5), "LON:ULVR": holding("LON:ULVR", "TACTICAL", 5),
            "MSFT": holding("MSFT", "TACTICAL", 4.8), "LON:SHEL": holding("LON:SHEL", "TACTICAL", 5)}


def test_rule_tactical_sleeve_max_needs_replacement(cfg):
    e = engine(cfg, four_tactical() | {"AAPL": holding("AAPL", "TACTICAL", 4.5)})  # sleeve ~24.3%
    e.process([tac_buy("NVDA", target=120, target_weight_pct=4.5)])
    assert only_rule(e) == "REPLACEMENT_REQUIRED"
    e = engine(cfg, four_tactical() | {"AAPL": holding("AAPL", "TACTICAL", 4.5)})
    e.process([tac_buy("NVDA", target=120, target_weight_pct=4.5, replaces="AAPL",
                       replacement_reason="dated catalyst vs none")])
    assert e.applied and "AAPL" not in e.s["holdings"]


def test_rule_tactical_sleeve_max_after_replacement(cfg):
    hold = four_tactical() | {"AAPL": holding("AAPL", "CORE", 3)}  # sleeve ~19.8%
    e = engine(cfg, hold)
    e.process([tac_buy("NVDA", target=120, target_weight_pct=4.5, replaces="AAPL", replacement_reason="x")])
    assert e.applied  # ~24.3% <= 25%
    cfg2 = copy.deepcopy(cfg)
    cfg2["tactical"]["max_sleeve_pct"] = 22
    e = engine(cfg2, hold)
    e.process([tac_buy("NVDA", target=120, target_weight_pct=4.5, replaces="AAPL", replacement_reason="x")])
    assert only_rule(e) == "TACTICAL_SLEEVE_MAX"  # replacing a CORE name frees no tactical room


def test_rule_sector_max_add_and_buy(cfg):
    hold = {"AAPL": holding("AAPL", "CORE", 10, conv=5), "MSFT": holding("MSFT", "CORE", 12, conv=5),
            "NVDA": holding("NVDA", "CORE", 7, conv=4)}  # Technology ~29%
    e = engine(cfg, hold)
    e.process([{"ticker": "NVDA", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert only_rule(e) == "SECTOR_MAX"
    e = engine(cfg, {"AAPL": hold["AAPL"], "MSFT": hold["MSFT"]},
               prices={"ORCL": (100.0, "USD", "Technology")}, watch=dict(WATCH, ORCL=None))
    e.process([core_buy("ORCL", conv=5)])  # 22% + 10% > 30%
    assert only_rule(e) == "REPLACEMENT_REQUIRED"


def test_rule_cash_min(cfg):
    hold = {"AAPL": holding("AAPL", "CORE", 3, conv=2), "LON:ULVR": holding("LON:ULVR", "CORE", 96.5)}
    e = engine(cfg, hold)  # cash ~0.5%
    e.process([{"ticker": "AAPL", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert only_rule(e) == "CASH_MIN"
    e = engine(cfg, hold)
    e.process([core_buy("LON:SHEL", conv=3)])
    assert only_rule(e) == "REPLACEMENT_REQUIRED"


def fifteen(cfg):
    extra = {f"X{i}": (100.0, "GBP", f"S{i}") for i in range(15)}
    hold = {}
    for t, (c, ccy, sec) in extra.items():
        hold[t] = {"type": "CORE", "shares": 60, "currency": ccy, "sector": sec, "cost_basis_usd": 6000,
                   "conviction": 3, "thesis": "", "triggers": [], "exit_plan": None, "market_value_usd": 6000}
    return engine(cfg, hold, cash=10000, prices=extra)


def test_rule_max_holdings_requires_replacement(cfg):
    e = fifteen(cfg)
    e.process([core_buy("LON:SHEL", conv=3)])
    assert only_rule(e) == "REPLACEMENT_REQUIRED"


def test_replacement_sold_in_same_run(cfg):
    e = fifteen(cfg)
    e.process([core_buy("LON:SHEL", conv=3, replaces="X3", replacement_reason="higher ROIC at a lower multiple")])
    assert [(r["side"], r["ticker"]) for r in e.ledger] == [("SELL", "X3"), ("BUY", "LON:SHEL")]
    assert "X3" not in e.s["holdings"] and len(e.s["holdings"]) == 15


@pytest.mark.parametrize("kw", [{"replaces": "NOPE", "replacement_reason": "x"}, {"replaces": "X3"}])
def test_rule_replacement_invalid(cfg, kw):
    e = fifteen(cfg)
    e.process([core_buy("LON:SHEL", conv=3, **kw)])
    assert only_rule(e) == "REPLACEMENT_INVALID"
    assert "X3" in e.s["holdings"]  # replacement never sold when the pair is rejected


def test_rule_min_shares(cfg):
    e = engine(cfg)
    e.process([core_buy("BIG", conv=2)])
    assert only_rule(e) == "MIN_SHARES"


# ------------------------------------------------------------------ files: applied vs rejected
def test_rejected_trade_leaves_state_unchanged_and_is_logged(cfg, tmp_path):
    mkt = FakeMarket(PRICES, cfg)
    sp = tmp_path / "state.json"
    run_submit([core_buy("AAPL")], sp, mkt, cfg, WATCH, TODAY, port_dir=tmp_path)
    before = sp.read_bytes()
    ledger_before = (tmp_path / "ledger.csv").read_bytes()
    out = run_submit([core_buy("AAPL", conv=1), tac_buy("NVDA", target=50)], sp, mkt, cfg, WATCH, TODAY, port_dir=tmp_path)
    assert out["applied"] == []
    assert {r["rule"] for r in out["rejected"]} == {"ALREADY_HELD", "TACTICAL_EXIT_PLAN"}
    assert sp.read_bytes() == before  # byte-for-byte unchanged
    assert (tmp_path / "ledger.csv").read_bytes() == ledger_before
    assert len(read_csv(tmp_path / "rejections.csv")) == 2


def test_buy_writes_state_and_ledger(cfg, tmp_path):
    mkt = FakeMarket(PRICES, cfg)
    sp = tmp_path / "state.json"
    out = run_submit([core_buy("AAPL")], sp, mkt, cfg, WATCH, TODAY, port_dir=tmp_path)
    assert out["cash_before_usd"] == 100000 and out["cash_after_usd"] == pytest.approx(92993.00)
    led = read_csv(tmp_path / "ledger.csv")
    assert led[0]["ticker"] == "AAPL" and led[0]["costs_usd"] == "7.0"
    assert json.loads(sp.read_text())["baseline"]["holdings"] == {"AAPL": {"shares": 35}}


# ------------------------------------------------------------------ baseline
def test_baseline_frozen_after_first_week(cfg):
    e = engine(cfg)
    e.process([core_buy("AAPL")])
    e.update_baseline()
    assert e.s["baseline"]["holdings"] == {"AAPL": {"shares": 35}} and e.s["inception_date"] == TODAY
    e.today = "2026-10-20"
    e.ledger = []
    e.process([core_buy("MSFT")])
    e.update_baseline()
    assert e.s["baseline"]["holdings"] == {"AAPL": {"shares": 35}}


# ------------------------------------------------------------------ returns maths
def test_interval_return():
    assert interval_return(100, 110, 0, 0) == pytest.approx(0.10)
    assert interval_return(0, 1000, 1002, 0) == pytest.approx(-2 / 1002)  # costs only
    assert interval_return(100, 0, 0, 99.8) == pytest.approx(-0.002)       # full sale at end
    assert interval_return(0, 0, 0, 0) is None


def val(date, phase, total, core=0, cin=0, cout=0, tac=0, tin=0, tout=0, base="", spy=100):
    return {"date": date, "phase": phase, "total_usd": total, "core_usd": core, "core_in": cin, "core_out": cout,
            "tactical_usd": tac, "tactical_in": tin, "tactical_out": tout, "baseline_usd": base, "spy_close": spy}


def test_returns_table_chain_links():
    vals = [val("2026-09-25", "inception", 100000, spy=100),
            val("2026-09-25", "post", 99990, core=10000, cin=10010, base=99990, spy=100),
            val("2026-10-02", "pre", 100990, core=11000, cin=10010, base=100990, spy=102),
            val("2026-10-02", "post", 100990, core=11000, cin=10010, base=100990, spy=102),
            val("2026-10-09", "pre", 101540, core=11550, cin=10010, base=101540, spy=101)]
    rt = returns_table(vals, "2026-10-10")
    assert rt["inception"]["total"] == pytest.approx(0.0154)
    assert rt["inception"]["core"] == pytest.approx(10000 / 10010 * 1.10 * 1.05 - 1)
    assert rt["week"]["core"] == pytest.approx(0.05) and rt["week"]["spy"] == pytest.approx(101 / 102 - 1)
    assert rt["mtd"]["from"] == "2026-09-25" and rt["mtd"]["total"] == pytest.approx(101540 / 99990 - 1)
    assert rt["inception"]["baseline"] == pytest.approx(101540 / 99990 - 1)
    assert rt["inception"]["tactical"] is None


def test_chain_level():
    assert chain([{"x": "100"}, {"x": "110"}], key_level="x") == pytest.approx(0.1)


# ------------------------------------------------------------------ FX + fills from real fixtures
def test_fx_and_fill_from_real_pages(cfg):
    mkt = Market(FixtureFetcher(), TODAY, cfg)
    gbx = mkt.fx("GBX")
    assert gbx["rate"] * 100 == pytest.approx(1.3278, abs=0.002)  # USD per GBP implied by the site
    assert gbx["url"] == "https://stockanalysis.com/list/biggest-companies/" and gbx["date"] == TODAY
    q = mkt.quote("AAPL")
    assert q["date"] == "2026-10-05" and q["price_usd"] == 332.89 and q["fx"] is None  # USD: no conversion
    shel = mkt.quote("LON:SHEL")
    assert shel["price_usd"] == pytest.approx(3631.5 * gbx["rate"]) and shel["fx"]["rate"] == gbx["rate"]

def test_core_fundamental_triggers_accepted(cfg):
    e = engine(cfg)
    e.process([core_buy("AAPL", triggers=[
        {"text": "Gross margin below 44%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 44}},
        {"text": "Pricing power erodes: services revenue growth turns negative"}])])
    assert e.applied


def test_fx_for_other_currencies(cfg):
    mkt = FakeMarket({"ETR:SAP": (200.0, "EUR", "Technology"), "JSE:NPN": (300000.0, "ZAc", "Technology"),
                      "XXX": (10.0, "XYZ", "Technology")}, cfg)
    assert mkt.quote("ETR:SAP")["price_usd"] == pytest.approx(220.0)
    assert mkt.quote("JSE:NPN")["price_usd"] == pytest.approx(180.0)  # cents x USD-per-cent
    with pytest.raises(DataError):  # no rate on the site -> unavailable, never guessed
        mkt.quote("XXX")

def test_implied_fx_one_rate_per_currency():
    from universe import implied_fx
    fx = implied_fx(FixtureFetcher(), None, max_pages=2)
    assert {"EUR", "JPY", "GBX", "TWD", "HKD"} <= set(fx)
    assert fx["JPY"]["rate"] == pytest.approx(0.0063241, rel=1e-4) and fx["EUR"]["n"] > 1

@pytest.mark.skipif(not (Path(__file__).resolve().parent.parent / "universe" / "universe.csv").exists(),
                    reason="universe.csv is built locally by scripts/universe.py (not distributed)")
def test_investable_includes_universe_and_watchlist():
    from portfolio import investable
    names = investable()
    assert {"AAPL", "LON:SHEL", "NVDA", "LON:HSBA"} <= set(names)


def test_sell_fills_at_given_close_date(cfg):
    mkt = Market(FixtureFetcher(), TODAY, cfg)
    s = empty_state(cfg)
    s["holdings"]["AAPL"] = {"type": "TACTICAL", "shares": 10, "currency": "USD", "sector": "Technology",
                             "cost_basis_usd": 3000.0, "conviction": 3, "market_value_usd": 0.0}
    mark(s, mkt)
    e = Engine(s, mkt, cfg, WATCH, TODAY)
    e.process([{"ticker": "AAPL", "action": "SELL", "position_type": "TACTICAL", "reason": "stop", "fill_date": "2026-09-29"}])
    assert e.ledger[0]["fill_close_date"] == "2026-09-29" and e.ledger[0]["fill_price"] == 329.4
    e.process([{"ticker": "MSFT", "action": "SELL", "position_type": "CORE", "reason": "x", "fill_date": "2026-09-27"}])
    assert e.rejections[-1]["rule"] == "NOT_HELD"


def test_hold_refreshes_core_decision_without_trading(cfg):
    e = engine(cfg, {"AAPL": holding("AAPL", "CORE", 5, conv=3)})
    new = [{"text": "Gross margin below 40%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
           {"text": "ROIC below 30%"}]
    e.process([{"ticker": "AAPL", "action": "HOLD", "position_type": "CORE", "conviction": 4, "reason": "re-init",
                "thesis": "new thesis", "triggers": new, "research_note": "research/AAPL/x.md"}])
    h = e.s["holdings"]["AAPL"]
    assert e.ledger == [] and len(e.applied) == 1
    assert h["triggers"] == new and h["thesis"] == "new thesis" and h["conviction"] == 4
    e.process([{"ticker": "AAPL", "action": "HOLD", "position_type": "CORE", "conviction": 4, "reason": "x",
                "triggers": [{"text": "a"}, {"text": "Share price closes below 200"}]}])
    assert e.rejections[-1]["rule"] == "CORE_TRIGGERS"


def test_tactical_hold_never_changes_exit_plan(cfg):
    e = engine(cfg, {"NVDA": holding("NVDA", "TACTICAL", 4)})
    plan = dict(e.s["holdings"]["NVDA"]["exit_plan"])
    e.process([{"ticker": "NVDA", "action": "HOLD", "position_type": "TACTICAL", "conviction": 3, "reason": "x",
                "thesis": "still on", "exit_plan": {"target": 999, "stop": 1, "time_limit": "2027-06-01"}}])
    assert e.s["holdings"]["NVDA"]["exit_plan"] == plan


def test_trim_rounds_to_nearest_share(cfg):
    e = engine(cfg, {"NVDA": holding("NVDA", "CORE", 6.3, conv=3)})  # $100 shares
    e.process([{"ticker": "NVDA", "action": "TRIM", "position_type": "CORE", "conviction": 2, "reason": "x"}])
    w = e.s["holdings"]["NVDA"]["market_value_usd"] / totals(e.s)["total"] * 100
    assert abs(w - 3) < 0.1


@pytest.mark.parametrize("conv,ok", [(2, False), (3, False), (4, True), (5, True)])
def test_rule_min_buy_conviction_core(real_cfg, conv, ok):
    assert real_cfg["core"]["min_buy_conviction"] == 4
    e = engine(real_cfg)
    e.process([core_buy("AAPL", conv=conv)])
    if ok:
        assert e.applied
    else:
        assert only_rule(e) == "CONVICTION_TOO_LOW"


def test_rule_min_buy_conviction_tactical_and_add(real_cfg):
    e = engine(real_cfg)
    e.process([tac_buy("NVDA", target=120)])  # tac_buy uses conviction 3
    assert only_rule(e) == "CONVICTION_TOO_LOW"
    e = engine(real_cfg, {"AAPL": holding("AAPL", "CORE", 3, conv=2)})
    e.process([{"ticker": "AAPL", "action": "ADD", "position_type": "CORE", "conviction": 3, "reason": "x"}])
    assert only_rule(e) == "CONVICTION_TOO_LOW"


# ------------------------------------------------------------------ next-open orders (owner rule)
class OpenMarket(FakeMarket):
    """Completed closes up to 2026-10-09 (Fri); `opens` gives later sessions' opening prices."""

    def __init__(self, cfg, opens=None, asof="2026-10-10"):
        super().__init__(PRICES, cfg, asof=asof, close_date="2026-10-09")
        self.opens = opens or {}

    def history(self, t):
        h = super().history(t)
        extra = [{"date": d, "open": o, "close": o, "high": o, "low": o} for d, o in self.opens.get(t, [])]
        return {**h, "all_rows": [dict(h["rows"][0], open=h["rows"][0]["close"])] + extra}


def test_place_orders_changes_nothing_but_the_queue(cfg, tmp_path):
    from portfolio import place_orders
    sp = tmp_path / "state.json"
    out = place_orders([core_buy("AAPL", conv=4), core_buy("MSFT", conv=1)], sp, OpenMarket(cfg), cfg, WATCH,
                       "2026-10-10", port_dir=tmp_path)
    s = json.loads(sp.read_text())
    assert s["cash_usd"] == 100000 and s["holdings"] == {}
    assert [o["request"]["ticker"] for o in s["pending"]] == ["AAPL"] and s["pending"][0]["placed"] == "2026-10-10"
    assert out["placed"][0]["est_shares"] == 35 and out["rejected"][0]["rule"] == "CONVICTION_NO_POSITION"
    assert not (tmp_path / "ledger.csv").exists()


def test_fill_waits_for_the_open_then_fills_at_it(cfg, tmp_path):
    from portfolio import fill_pending, place_orders
    sp = tmp_path / "state.json"
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, "2026-10-10", port_dir=tmp_path)
    out = fill_pending(sp, OpenMarket(cfg, asof="2026-10-11"), cfg, WATCH, port_dir=tmp_path)  # Sunday: no open yet
    assert out["still_pending"] and json.loads(sp.read_text())["holdings"] == {}
    mkt = OpenMarket(cfg, opens={"AAPL": [("2026-10-12", 210.0)]}, asof="2026-10-13")
    out = fill_pending(sp, mkt, cfg, WATCH, port_dir=tmp_path)
    row = out["applied"][0]
    assert (row["fill_price"], row["fill_close_date"]) == (210.0, "2026-10-12")      # Monday's OPEN, not a close
    assert "filled at the open of 2026-10-12" in row["reason"]
    s = json.loads(sp.read_text())
    assert s["pending"] == [] and s["holdings"]["AAPL"]["entry_price"] == 210.0
    assert s["cash_usd"] == pytest.approx(100000 - row["gross_usd"] - row["costs_usd"])


def test_tactical_order_cancelled_if_it_opens_beyond_target(cfg, tmp_path):
    from portfolio import fill_pending, place_orders
    sp = tmp_path / "state.json"
    place_orders([tac_buy("NVDA", target=110, conviction=4)], sp, OpenMarket(cfg), cfg, WATCH, "2026-10-10",
                 port_dir=tmp_path)
    out = fill_pending(sp, OpenMarket(cfg, opens={"NVDA": [("2026-10-12", 115.0)]}, asof="2026-10-13"), cfg, WATCH,
                       port_dir=tmp_path)
    assert out["applied"] == [] and out["rejected"][0]["rule"] == "TACTICAL_EXIT_PLAN"
    assert "at the open of 2026-10-12" in out["rejected"][0]["detail"]
    assert json.loads(sp.read_text())["pending"] == []


def test_order_expires_without_an_open(cfg, tmp_path):
    from portfolio import fill_pending, place_orders
    sp = tmp_path / "state.json"
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, "2026-10-10", port_dir=tmp_path)
    out = fill_pending(sp, OpenMarket(cfg, asof="2026-10-30"), cfg, WATCH, port_dir=tmp_path)
    assert out["expired"] and out["rejected"][0]["rule"] == "ORDER_EXPIRED"
    assert json.loads(sp.read_text())["pending"] == []


def test_replacement_pair_fills_both_sides_at_their_opens(cfg, tmp_path):
    from portfolio import fill_pending, place_orders
    sp = tmp_path / "state.json"
    s = empty_state(cfg)
    s["holdings"]["MSFT"] = holding("MSFT", "CORE", 5)
    s["cash_usd"] = 95000
    sp.write_text(json.dumps(s))
    place_orders([core_buy("AAPL", conv=4, replaces="MSFT", replacement_reason="better value")], sp, OpenMarket(cfg),
                 cfg, WATCH, "2026-10-10", port_dir=tmp_path)
    mkt = OpenMarket(cfg, opens={"AAPL": [("2026-10-12", 205.0)], "MSFT": [("2026-10-12", 390.0)]}, asof="2026-10-13")
    out = fill_pending(sp, mkt, cfg, WATCH, port_dir=tmp_path)
    assert [(a["side"], a["ticker"], a["fill_price"]) for a in out["applied"]] == [("SELL", "MSFT", 390.0), ("BUY", "AAPL", 205.0)]


# ------------------------------------------------------------------ daily re-pricing
def test_daily_valuation_rows(tmp_path):
    from portfolio import VAL_COLS, record_valuation
    path = tmp_path / "valuations.csv"
    base = {k: "" for k in VAL_COLS}
    assert record_valuation(path, {**base, "date": "2026-10-09", "phase": "post", "total_usd": 100}) == "appended"
    # the weekly run already valued that close: no duplicate daily row
    assert record_valuation(path, {**base, "date": "2026-10-09", "phase": "daily", "total_usd": 100}) == "skipped"
    assert record_valuation(path, {**base, "date": "2026-10-12", "phase": "daily", "total_usd": 101}) == "appended"
    # same-day re-run replaces the daily row
    assert record_valuation(path, {**base, "date": "2026-10-12", "phase": "daily", "total_usd": 102}) == "replaced"
    rows = read_csv(path)
    assert [(r["date"], r["phase"], r["total_usd"]) for r in rows] == [
        ("2026-10-09", "post", "100"), ("2026-10-12", "daily", "102")]


def test_week_return_spans_seven_days_with_daily_rows():
    vals = [val("2026-10-02", "post", 100000, spy=100),
            val("2026-10-05", "daily", 100500, spy=101),
            val("2026-10-08", "daily", 101000, spy=102),
            val("2026-10-09", "pre", 102000, spy=103),
            val("2026-10-12", "daily", 103000, spy=104),
            val("2026-10-13", "daily", 104000, spy=105)]
    rt = returns_table(vals, "2026-10-14")
    # latest valuation at least 7 days before 2026-10-13 is 2026-10-05 (not yesterday)
    assert rt["week"]["from"] == "2026-10-05"
    assert rt["week"]["total"] == pytest.approx(104000 / 100500 - 1)
    assert rt["week"]["spy"] == pytest.approx(105 / 101 - 1)


def test_order_never_fills_at_the_open_of_its_own_decision_day(cfg, tmp_path):
    from portfolio import fill_pending, place_orders
    sp = tmp_path / "state.json"
    place_orders([core_buy("AAPL", conv=4)], sp, OpenMarket(cfg), cfg, WATCH, "2026-10-12", port_dir=tmp_path)
    # decided on Monday after the open: Monday's open is look-ahead; Tuesday's open is the fill
    mkt = OpenMarket(cfg, opens={"AAPL": [("2026-10-12", 200.0), ("2026-10-13", 205.0)]}, asof="2026-10-14")
    row = fill_pending(sp, mkt, cfg, WATCH, port_dir=tmp_path)["applied"][0]
    assert (row["fill_price"], row["fill_close_date"]) == (205.0, "2026-10-13")
