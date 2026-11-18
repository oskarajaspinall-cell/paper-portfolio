import json

import pandas as pd
import pytest

import shadow_shorts as SS
import short_screen as SC

SHEET = """# Fact sheet
Sector: Technology [OV] · Industry: Computer Hardware [OV] · Price ccy: USD · Market cap: 235.7bn USD [ST]
| ROIC | 12.0% | -10.1% | -3.7% | 4.7% | 104.4% | 102.2% | rising (+92.4pp) | RA |
| Operating margin | 10.0% | -20.0% | 5.0% | 12.0% | 60.0% | 61.6% | rising | IS |
| ROIC | 239.9% (2026-09-30) | 157.5% (2025-09-30) | +82.3pp | +155.9pp (rising) | 284.8% (x) | rising | RA-T |
| vs 200-day MA (1,174.82) | +37.0% | ST,HI |
| 12-month (52-week) change | +1,230.7% | ST |
| Short interest (% float) | 3.89% | ST |
| Next earnings date | Nov 20, 2026 (Earnings Date) | ST,OV |
"""


@pytest.fixture
def scfg(cfg):
    from common import load_config
    cfg["short"] = load_config()["short"]
    return cfg


def test_fact_sheet_signals_reads_the_annual_table_only():
    s = SC.fact_sheet_signals(SHEET)
    assert s["industry"] == "Computer Hardware" and s["ROIC"]["ttm"] == 102.2
    assert s["ROIC"]["peak_pp"] == pytest.approx(102.2 - 4.7)          # not the rolling table's 239.9
    assert (s["vs_200d"], s["change_12m"], s["short_interest"], s["next_results"]) == (37.0, 1230.7, 3.89, "2026-11-20")


def test_peak_cycle_needs_a_profit_and_confidence_adds_up(scfg):
    s = SC.fact_sheet_signals(SHEET)
    assert SC.peak_cycle(s, scfg) and SC.confidence(s, 2, scfg) == 6   # ROIC 2 + margin 2 + stretched 1 + parabolic 1
    assert SC.confidence(s, 1, scfg) == 7
    loss = {"ROIC": {"peak_pp": None}, "Operating margin": {"ttm": -40.0, "peak_pp": 300.0}}
    assert not SC.peak_cycle(loss, scfg)                                 # shrinking losses are not a peak (ASTS)


def test_trend_turned():
    falling = [100 - i * 0.5 for i in range(60)]
    rising = [100 + i * 0.5 for i in range(60)]
    assert SC.trend_turned(falling) and not SC.trend_turned(rising) and not SC.trend_turned(falling[:40])


def test_guards(scfg):
    s = dict(SC.fact_sheet_signals(SHEET), short_interest=24.5)
    g = SC.guards(s, "A definitive all-cash takeover by Thrive", 1.0, "2026-11-18", False, True, scfg)
    assert any("crowded" in x for x in g) and any("small" in x for x in g) and any("takeover" in x for x in g)
    assert any("results due 2026-11-20" in x for x in g) and "on the buy watchlist" in g
    assert SC.guards(SC.fact_sheet_signals(SHEET), "", 200.0, "2026-12-01", False, False, scfg) == []


def test_put_choice_and_thin_chain(scfg):
    assert SS.pick_expiry(["2026-11-20", "2027-01-15", "2027-03-19", "2027-06-18"], "2026-11-18") == "2027-03-19"
    chain = pd.DataFrame([{"contractSymbol": "X270319P00100000", "strike": 100.0, "bid": 9.0, "ask": 11.0,
                           "openInterest": 900, "impliedVolatility": 0.2},
                          {"contractSymbol": "X270319P00120000", "strike": 120.0, "bid": 25.0, "ask": 27.0,
                           "openInterest": 900, "impliedVolatility": 0.2}])
    closes = [100 * (1.02 if i % 2 else 0.98) for i in range(260)]   # realised vol far above 20%: IV is cheap
    put = SS.price_put("AAPL", 101.0, "2026-11-18", closes, scfg, loader=lambda s: (["2027-03-19"], lambda e: chain))
    assert (put["strike"], put["mid"]) == (100.0, 10.0)
    thin = chain.assign(openInterest=10)
    assert SS.price_put("AAPL", 101.0, "2026-11-18", closes, scfg, loader=lambda s: (["2027-03-19"], lambda e: thin)) is None
    assert SS.price_put("KRX:000660", 1.0, "2026-11-18", closes, scfg) is None   # no listed US chain


def test_exits_and_marks(scfg):
    row = {"entry_close": "100", "etf_entry": "50", "put_entry_mid": "10", "contracts": "2", "put_expiry": "2027-03-19",
           "opened": "2026-11-18"}
    assert SS.exit_reason(row, 116, "2026-12-01", [], scfg).startswith("stop")
    assert SS.exit_reason(row, 95, "2026-12-01", ["gross margin rose"], scfg).startswith("falsifier")
    assert SS.exit_reason(row, 95, "2027-02-20", [], scfg).startswith("time")
    assert SS.exit_reason(row, 50, "2026-12-01", [], scfg) == ""   # no fair-value target: a big fall keeps it open
    SS.mark(row, 80, 51, "2026-12-01", 22.0)
    assert (row["stock_vs_etf_pct"], row["put_pnl_usd"]) == (-22.0, 2400.0)   # -20% vs +2%; (22-10) x 100 x 2


def test_short_evaluation_check(scfg):
    import check_docs
    blk = {"ticker": "SNDK", "decision": "SHORT", "conviction": 4,
           "parts": {"overvaluation": 2, "peak_cycle": 2, "deterioration": 1, "capital_need": 1, "catalyst": 2,
                     "momentum": 0, "takeover_appeal": 0, "crowding": 0, "insider_support": -1},
           "thesis": "t", "catalyst": {"text": "Q4", "date": "2027-01-28"}, "bull_case": "b",
           "falsifiers": [{"text": "a"}, {"text": "b"}, {"text": "c", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 75}}]}
    md = "## Bear thesis\nx\n## Bull case against the short\ny\n## Decision\n```json\n" + json.dumps(blk) + "\n```\n"
    errs, counts = check_docs.check_short(md, scfg)
    assert errs == [] and counts["short"] == "7->4"
    blk["conviction"] = 5
    assert any("gives 4" in e for e in check_docs.check_short(md.replace('"conviction": 4', '"conviction": 5'), scfg)[0])
    weak = md.replace('"catalyst": 2', '"catalyst": 0').replace('"conviction": 4', '"conviction": 3')
    assert any("needs conviction 4" in e for e in check_docs.check_short(weak, scfg)[0])


def test_foreign_shorts_restricted_markets_adr_and_borrowing(scfg):
    sig = SC.fact_sheet_signals(SHEET)
    g = SC.guards(sig, "", 200.0, "2026-12-01", False, False, scfg, "KRX:000660", None)
    assert g == ["shorting restricted in KRX and no US-listed share"]
    assert SC.guards(sig, "", 200.0, "2026-12-01", False, False, scfg, "TPE:2330", "TSM") == []   # its US share is shortable
    assert SC.guards(sig, "", 200.0, "2026-12-01", False, False, scfg, "TYO:6857", None) == []    # Japan is not restricted
    assert SC.adr_map().get("TPE:2330") == "TSM"

    chain = pd.DataFrame([{"contractSymbol": "TSM270319P00200000", "strike": 200.0, "bid": 9.0, "ask": 11.0,
                           "openInterest": 900, "impliedVolatility": 0.2}])
    closes = [100 * (1.02 if i % 2 else 0.98) for i in range(260)]
    put = SS.price_put("TPE:2330", 201.0, "2026-11-18", closes, scfg, loader=lambda s: (["2027-03-19"], lambda e: chain),
                       adr="TSM")
    assert put["underlying"] == "TSM" and put["strike"] == 200.0          # foreign stock, put on its US share

    row = {"entry_close": "100", "etf_entry": "50", "opened": "2026-11-18", "borrow_fee_pct": "6"}
    SS.mark(row, 80, 51, "2027-05-18", None)                              # 181 days: 6% x 181/365 = 2.98%
    assert row["borrow_cost_pct"] == pytest.approx(2.98, abs=0.01)
    assert row["short_net_pct"] == pytest.approx(22.0 - 2.98, abs=0.01)  # stock -20% vs fund +2%, less the fee


def test_alt_exit_rules_followed_side_by_side(scfg):
    days = [f"2026-{m:02d}-{d:02d}" for m in (8, 9, 10, 11) for d in range(1, 29)]
    px = [100.0] * 60 + [100 - 2 * i for i in range(1, 21)] + [60 + 3 * i for i in range(1, 33)]  # flat, falls 40%, rebounds
    rows = [{"date": d, "close": c, "high": c * 1.01, "low": c * 0.99} for d, c in zip(days, px)]
    etf = {d: 50.0 for d in days}
    alt = SS.alt_exits(rows, etf, days[60], days[-1], scfg)
    assert set(alt) == set(SS.ALT_RULES) - {"value"}   # no valuation anchor given
    assert alt["take15"]["fired"] and alt["take15"]["result"] >= 15 and alt["take25"]["result"] >= 25
    assert alt["trail_atr"]["fired"] and alt["trail_atr"]["date"] < alt["hold"]["date"]   # the rebound trips it
    assert not alt["hold"]["fired"] and alt["hold"]["result"] == pytest.approx(-((px[-1] / px[60]) - 1) * 100, abs=0.01)
    book = [{"sector": "Technology", "alt_exits": json.dumps(alt)}, {"sector": "Energy", "alt_exits": json.dumps(alt)}]
    summ = SS.alt_summary(book)
    assert summ["All"]["take15"]["n"] == 2 and set(summ) == {"All", "Technology", "Energy"}


def test_valuation_and_technical_exit_rules(scfg):
    sheet = ("| P/E | 6.4x | [data unavailable] | x |\n| EV/Sales | 3.7x | 1.0x / 6.8x / 12.6x | 23% |\n"
             "| P/B | 9.9x | 0.7x / 8.6x / 16.4x | 36% |\n")
    vt = SS.valuation_target(sheet, 1255.0)
    assert vt["multiple"] == "P/B" and vt["target"] == pytest.approx(1255 * 8.6 / 9.9, abs=0.01)
    assert SS.valuation_target(sheet.replace("9.9x", "6.3x"), 797.0) is None   # both multiples already below median
    assert SS.valuation_target("| P/B | 6.3x | 0.7x / 8.6x / 16.4x |", 797.0) is None   # already below its median
    assert SS.rsi([float(x) for x in range(1, 40)]) == 100.0 and SS.rsi([40.0 - x for x in range(39)]) == 0.0
    days = [f"2026-{m:02d}-{d:02d}" for m in (8, 9, 10, 11) for d in range(1, 29)]
    px = [100.0] * 60 + [100 - 2 * i for i in range(1, 21)] + [60 + 3 * i for i in range(1, 33)]
    rows = [{"date": d, "close": c, "high": c * 1.01, "low": c * 0.99} for d, c in zip(days, px)]
    alt = SS.alt_exits(rows, {d: 50.0 for d in days}, days[60], days[-1], scfg, {"target": 80.0})
    assert alt["value"]["fired"] and alt["value"]["result"] == pytest.approx(-(80 / 98 - 1) * 100, abs=0.01)
    assert alt["rsi30"]["fired"] and alt["stretch25"]["fired"]
    assert "value" not in SS.alt_exits(rows, {d: 50.0 for d in days}, days[60], days[-1], scfg)
