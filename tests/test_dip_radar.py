import datetime as dt
import random

import dip_radar as D


def series(n=200, start="2026-01-01", drift=0.0, beta=1.0, mkt=None, shock_from=None, shock=0.0, seed=1):
    """Daily closes: stock = beta x market + noise; from index `shock_from` an extra daily fall `shock`."""
    rnd = random.Random(seed)
    d0 = dt.date.fromisoformat(start)
    rows, c = [], 100.0
    for i in range(n):
        m = mkt[i] if mkt else 0.0
        r = beta * m + rnd.gauss(drift, 0.01) + (shock if shock_from is not None and i >= shock_from else 0.0)
        c *= 1 + r
        rows.append({"date": (d0 + dt.timedelta(days=i)).isoformat(), "close": c})
    return rows


def spy_and_moves(n=200, crash_from=None, crash=0.0):
    rnd = random.Random(7)
    moves = [rnd.gauss(0, 0.008) + (crash if crash_from is not None and i >= crash_from else 0.0) for i in range(n)]
    c, rows, d0 = 100.0, [], dt.date(2026, 1, 1)
    for i, m in enumerate(moves):
        c *= 1 + m
        rows.append({"date": (d0 + dt.timedelta(days=i)).isoformat(), "close": c})
    return rows, moves


def test_stock_specific_fall_is_unusual_but_a_market_fall_is_not():
    spy, mv = spy_and_moves()
    calm = D.move_stats(series(mkt=mv, beta=1.2), spy, 20, 120)
    assert abs(calm["z"]) < 2 and abs(calm["beta"] - 1.2) < 0.25
    hit = D.move_stats(series(mkt=mv, beta=1.2, shock_from=190, shock=-0.02), spy, 20, 120)
    assert hit["z"] < -2 and hit["specific_pct"] < -10
    spy2, mv2 = spy_and_moves(crash_from=190, crash=-0.02)  # the whole market falls: beta explains it
    mk = D.move_stats(series(mkt=mv2, beta=1.0), spy2, 20, 120)
    assert mk["ret_pct"] < -10 and abs(mk["z"]) < 2


def test_window_starts_at_our_last_research():
    spy, mv = spy_and_moves()
    rows = series(mkt=mv, shock_from=185, shock=-0.02)
    seen = D.move_stats(rows, spy, 20, 120, since=rows[196]["date"])  # researched after most of the fall
    assert seen["sessions"] == 3 and seen["z"] is None
    fresh = D.move_stats(rows, spy, 20, 120, since=rows[183]["date"])
    assert fresh["sessions"] == 16 and fresh["z"] < -2


def watch_row(**k):
    return {"ticker": "X", "kind": "avoid", "decision": "AVOID", "conviction": 3, "price": 100.0, "currency": "USD",
            "date": "2026-10-01", **k}


def stats(z=-2.5, close=80.0):
    return {"beta": 1.0, "ret_pct": -20.0, "spy_pct": 0.0, "market_part_pct": 0.0, "specific_pct": -20.0, "z": z,
            "off_3m_high_pct": -20.0, "close": close, "close_date": "2026-10-16", "sessions": 10}


def test_signal_needs_an_unusual_fall_and_value_support(real_cfg):
    st = D.settings(real_cfg)
    ok = D.assess(watch_row(), stats(), {"base": 90.0, "bear": 70.0}, st, False, "2026-10-19")
    assert ok["signal"] and ok["cause"] == "stock-specific" and ok["vs_base_pct"] < 0
    assert not D.assess(watch_row(), stats(z=-1.0), {"base": 90.0}, st, False, "2026-10-19")["signal"]
    pricey = D.assess(watch_row(), stats(), {"base": 60.0}, st, False, "2026-10-19")
    assert not pricey["signal"] and "above base fair value" in pricey["why_not"]
    # no fair value: needs a 15% fall since our decision
    assert D.assess(watch_row(), stats(close=84.0), {}, st, False, "2026-10-19")["signal"]
    assert not D.assess(watch_row(), stats(close=90.0), {}, st, False, "2026-10-19")["signal"]
    # a market dip releasing the reserve: a 10% fall since the decision is enough, even if beta explains it
    mkt = D.assess(watch_row(), stats(z=-0.5, close=88.0), {"base": 95.0}, st, True, "2026-10-19")
    assert mkt["signal"] and mkt["cause"] == "market dip"


def test_watch_list_holdings_and_recent_conviction3_avoids(real_cfg):
    st = D.settings(real_cfg)
    state = {"holdings": {"H": {"type": "CORE", "conviction": 4, "entry_price": 50.0, "currency": "USD",
                                "entry_date": "2026-10-07"}, "T": {"type": "TACTICAL"}},
             "funding_queue": [{"ticker": "Q"}]}
    dec = [{"ticker": t, "decision": d, "conviction": c, "date": day, "price": "10", "currency": "USD", "type": "CORE"}
           for t, d, c, day in [("A", "AVOID", "3", "2026-10-10"), ("B", "AVOID", "2", "2026-10-10"),
                                ("C", "AVOID", "4", "2026-04-01"), ("Q", "BUY", "4", "2026-10-18"),
                                ("H", "BUY", "4", "2026-10-07")]]
    w = D.watch_list(state, dec, "2026-10-19", st)
    assert [(x["ticker"], x["kind"]) for x in w] == [("H", "holding"), ("A", "avoid")]


def test_hit_reason_asks_the_right_question():
    a = {**watch_row(), **stats(), "fair_value_base": 90.0, "from_decision_pct": -20.0, "last_research": "2026-10-01"}
    assert "Decide BUY or AVOID" in D.hit_reason(a) and "a falling price alone is not a reason" in D.hit_reason(a)
    h = dict(a, kind="holding")
    assert "ADD is the question" in D.hit_reason(h) and "Decide ADD, HOLD, TRIM or SELL" in D.hit_reason(h)


def test_entry_research_takes_dip_hits_including_holdings(tmp_path):
    from entry_research import todo
    state = {"holdings": {"H": {}}, "entry_hits": [{"ticker": "E", "intraday": True}],
             "dip_hits": [{"ticker": "H", "kind": "dip"}, {"ticker": "A", "kind": "dip"}, {"ticker": "E", "kind": "dip"}]}
    assert [h["ticker"] for h in todo(state, "2026-10-20", 3, root=tmp_path)] == ["E", "H", "A"]
    assert [h["ticker"] for h in todo(state, "2026-10-20", 2, root=tmp_path)] == ["E", "H"]


def test_weekly_reason_for_a_dip_hit():
    import weekly_run as wr
    assert wr.entry_hit_reason({"kind": "dip", "reason": "Dip radar: x"}) == "Dip radar: x"
