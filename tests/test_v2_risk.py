"""V2 risk changes (owner request 2026-11-15): size floor and entry cap, trim drift band (trigger 20 -> back to 12),
sector cap 35, 60-session volatility window. The shared `cfg` fixture pins the pre-V2 numbers; these tests use the
real config values."""
import datetime as dt

import pytest

from conftest import FakeMarket
from risk import Sizer
from weekly_scan import scan
from test_weekly import ScanFetcher, ScanMarket, holding, rows, empty_state
from test_risk import series


class StubMarket(FakeMarket):
    def __init__(self, vols, cfg):
        super().__init__({t: (100.0, "USD", "Technology") for t in vols}, cfg)
        day0 = dt.date(2026, 4, 1)
        self.rows = {t: [{"date": (day0 + dt.timedelta(days=i)).isoformat(), "close": c}
                         for i, c in enumerate(series(v, seed=k))] for k, (t, v) in enumerate(vols.items())}

    def history(self, t):
        return {"url": "https://stockanalysis.com/fake/", "currency": "USD", "rows": self.rows[t]}


def test_v2_config_values(real_cfg):
    c, p = real_cfg["core"], real_cfg["portfolio"]
    assert p["max_sector_pct"] == 35
    assert (c["trim_above_pct"], c["trim_to_pct"], c["max_entry_pct"], c["min_size_pct"]) == (20, 12, 15, 7)
    assert c["vol_lookback_sessions"] == 60
    assert c["min_size_pct"] <= c["trim_to_pct"] < c["max_entry_pct"] < c["trim_above_pct"]  # coherent band


def test_buy_bar_size_has_a_floor_and_entry_cap(real_cfg):
    vols = {"HOT": 90, "CALM": 8, "M1": 30, "M2": 30, "M3": 30, "M4": 30, "M5": 30}
    z = Sizer(StubMarket(vols, real_cfg), real_cfg)
    s = {"holdings": {t: {"type": "CORE"} for t in ("M1", "M2", "M3", "M4", "M5")}}
    assert z.target(4, "HOT", s)[0] == 7.0     # vol-scaled to 4.2 -> lifted to the 7% floor
    assert z.target(5, "CALM", s)[0] <= 15.0   # 10 x 1.4 = 14, never past the entry cap
    assert z.target(5, "CALM", s)[0] >= 10.0   # the plain conviction size is still the floor of a scale-up


def test_below_buy_bar_gets_no_floor(real_cfg):
    z = Sizer(StubMarket({"HOT": 90}, real_cfg), real_cfg)
    assert z.target(3, "HOT", {"holdings": {}})[0] <= 5.0  # a downgrade always means smaller


def test_trim_only_above_the_drift_band_and_back_to_12(cfg):
    cfg["core"].update(trim_above_pct=20, trim_to_pct=12)
    flat = rows([("2026-09-04", 100), ("2026-09-08", 101), ("2026-09-14", 102)])

    def run(big_shares):
        s = empty_state(cfg)
        s["last_scan"] = "2026-09-05"
        s["holdings"] = {"BIG": holding("BIG", "CORE", big_shares), "OTHER": holding("OTHER", "CORE", 50)}
        s["cash_usd"] = 60000
        res = scan(s, ScanMarket({"BIG": flat, "OTHER": flat}, cfg), ScanFetcher(), cfg, "2026-09-20")
        return {r["ticker"]: r for r in res["mechanical_requests"]}

    drifted = run(120)   # ~17-18%: above the old 15% cap, inside the new band -> left alone
    assert "BIG" not in drifted
    big = run(200)       # ~21-22%: past the trigger
    assert big["BIG"]["action"] == "TRIM" and big["BIG"]["target_weight_pct"] == 12


# ------------------------------------------------------------------ correlation cluster cap
import random

from portfolio import Engine, empty_state, mark, totals
from test_portfolio import PRICES, TODAY, WATCH, core_buy, tac_buy
from test_portfolio import holding as pf_holding  # (test_weekly's `holding` is a different helper)


class HistMarket(FakeMarket):
    """Daily history for every ticker: the 'together' names share one return stream plus a little noise."""

    def __init__(self, prices, cfg, together, days=120):
        super().__init__(prices, cfg)
        rnd = random.Random(7)
        base = [rnd.gauss(0, 0.02) for _ in range(days)]
        day0 = dt.date(2026, 6, 1)
        self.rows = {}
        for t in prices:
            close, out = 100.0, []
            for i in range(days):
                r = base[i] + rnd.gauss(0, 0.002) if t in together else rnd.gauss(0, 0.02)
                close *= 1 + r
                out.append({"date": (day0 + dt.timedelta(days=i)).isoformat(), "close": close})
            k = prices[t][0] / out[-1]["close"]  # end at the stated price so weights match the fixtures
            self.rows[t] = [{**o, "close": o["close"] * k} for o in out]

    def history(self, t):
        return {"url": "https://stockanalysis.com/fake/", "currency": "USD", "rows": self.rows[t]}


def cluster_engine(cfg, cap, together=("AAPL", "MSFT", "NVDA")):
    cfg["portfolio"].update(max_sector_pct=100, cluster_cap_pct=cap, cluster_corr=0.85, cluster_days=90)
    if cap is None:
        cfg["portfolio"].pop("cluster_cap_pct")
    s = empty_state(cfg)
    mkt = HistMarket({t: PRICES[t] for t in ("AAPL", "MSFT", "NVDA", "LON:ULVR")}, cfg, together)
    s["holdings"] = {"AAPL": pf_holding("AAPL", "CORE", 20, conv=5), "MSFT": pf_holding("MSFT", "CORE", 12, conv=5)}
    s["cash_usd"] = 100000 - sum(h["market_value_usd"] for h in s["holdings"].values())
    mark(s, mkt)
    return Engine(s, mkt, cfg, WATCH, TODAY)


def cluster_weight(e, names):
    pv = totals(e.s)["total"]
    return sum(e.s["holdings"][t]["market_value_usd"] for t in names if t in e.s["holdings"]) / pv * 100


def test_cluster_cap_sizes_a_buy_down_to_the_room(cfg):
    cfg["core"]["min_size_pct"] = 7
    e = cluster_engine(cfg, 40)
    e.process([core_buy("NVDA", conv=5)])  # wants 10%; AAPL 20 + MSFT 12 leave 8% of room
    assert [r["ticker"] for r in e.applied] == ["NVDA"] and not e.rejections
    nvda = cluster_weight(e, ["NVDA"])
    assert 7.0 <= nvda <= 8.0                                  # sized down, not rejected
    assert cluster_weight(e, ["AAPL", "MSFT", "NVDA"]) <= 40.0
    assert e.s["holdings"]["NVDA"]["target_pct"] > 9.0         # the full (vol-scaled) size stays the target


def test_cluster_cap_skips_a_buy_whose_room_is_under_the_floor(cfg):
    cfg["core"]["min_size_pct"] = 7
    e = cluster_engine(cfg, 33)  # room 1%: far below the 7% minimum position
    e.process([core_buy("NVDA", conv=5)])
    assert not e.applied and e.rejections[0]["rule"] == "CLUSTER_MAX"
    assert "minimum position" in e.rejections[0]["detail"] and "AAPL" in e.rejections[0]["detail"]


def test_cluster_cap_stops_an_add_at_the_room(cfg):
    e = cluster_engine(cfg, 40)
    e.s["holdings"]["NVDA"] = pf_holding("NVDA", "CORE", 3, conv=5)
    e.s["cash_usd"] -= e.s["holdings"]["NVDA"]["market_value_usd"]
    e.process([{"ticker": "NVDA", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert [r["ticker"] for r in e.applied] == ["NVDA"]
    assert cluster_weight(e, ["NVDA"]) > 3.5 and cluster_weight(e, ["AAPL", "MSFT", "NVDA"]) <= 40.0
    e2 = cluster_engine(cfg, 32)  # the cluster is already full
    e2.s["holdings"]["NVDA"] = pf_holding("NVDA", "CORE", 3, conv=5)
    e2.s["cash_usd"] -= e2.s["holdings"]["NVDA"]["market_value_usd"]
    e2.process([{"ticker": "NVDA", "action": "ADD", "position_type": "CORE", "conviction": 5, "reason": "x"}])
    assert not e2.applied and e2.rejections[0]["rule"] == "CLUSTER_MAX"


def test_cluster_cap_allows_it_when_it_fits_or_is_unrelated_or_off(cfg):
    e = cluster_engine(cfg, 45)
    e.process([core_buy("NVDA", conv=5)])  # 42% <= 45%
    assert [r["ticker"] for r in e.applied] == ["NVDA"]
    e = cluster_engine(cfg, 40, together=("AAPL", "MSFT"))
    e.process([core_buy("NVDA", conv=5)])  # NVDA does not move with them: no cluster
    assert [r["ticker"] for r in e.applied] == ["NVDA"]
    e = cluster_engine(cfg, None)
    e.process([core_buy("NVDA", conv=5)])  # check off
    assert [r["ticker"] for r in e.applied] == ["NVDA"]


# ------------------------------------------------------------------ re-entry cooldown
def test_a_fully_sold_name_cannot_be_rebought_for_30_days(cfg):
    cfg["portfolio"].update(max_sector_pct=100, reentry_cooldown_days=30)
    s = empty_state(cfg)
    mkt = FakeMarket({t: PRICES[t] for t in ("AAPL", "MSFT")}, cfg)
    s["holdings"] = {"AAPL": pf_holding("AAPL", "CORE", 10)}
    s["cash_usd"] = 90000.0
    mark(s, mkt)
    e = Engine(s, mkt, cfg, WATCH, TODAY)
    e.process([{"ticker": "AAPL", "action": "SELL", "position_type": "CORE", "reason": "thesis broken"}])
    assert e.applied and s["last_sold"] == {"AAPL": TODAY}
    e.process([core_buy("AAPL")])
    assert e.rejections[-1]["rule"] == "COOLDOWN" and "2026-11-05" in e.rejections[-1]["detail"]
    e2 = Engine(s, mkt, cfg, WATCH, "2026-11-05")   # day 30: free again
    e2.process([core_buy("AAPL")])
    assert [r["ticker"] for r in e2.applied] == ["AAPL"]
    s["last_sold"] = {}                               # an old state without the key behaves as before
    del s["last_sold"]
    e3 = Engine(s, mkt, cfg, WATCH, TODAY)
    e3.process([core_buy("MSFT")])
    assert [r["ticker"] for r in e3.applied] == ["MSFT"]


# ------------------------------------------------------------------ smoke alarm (lag AND below the 200-day average)
from weekly_scan import relative_return_pp, smoke_alarm

N = 260


def series_from(vals, d0="2025-12-01"):
    d = dt.date.fromisoformat(d0)
    return [{"date": (d + dt.timedelta(days=i)).isoformat(), "close": float(v)} for i, v in enumerate(vals)]


def line(a, b, n=N):
    return series_from([a + (b - a) * i / (n - 1) for i in range(n)])


def rises_then_stalls(top=150.0, stall_at=197, n=N):  # up 50%, flat for the last 63 sessions: above its 200-day
    return series_from([100 + (top - 100) * min(i, stall_at) / stall_at for i in range(n)])


def test_relative_return_is_over_sessions_and_needs_history(cfg):
    spy, lag = line(100, 130), line(100, 100)
    pp = relative_return_pp(lag, spy, 63)
    assert pp is not None and -7 < pp < -5.5                      # SPY gains ~6.2% over the last 63 sessions, the stock 0
    assert relative_return_pp(line(100, 100, 40), line(100, 110, 40), 63) is None   # not 63 sessions old yet
    assert relative_return_pp(lag, [], 63) is None


def test_smoke_alarm_needs_both_the_lag_and_a_close_below_the_200_day(cfg):
    asof = "2026-08-20"
    cfg["core"].update(smoke_alarm_pp=15, smoke_alarm_sessions=63, smoke_alarm_rearm_days=30)
    spy = line(100, 230)                                          # SPY +16% over the last 63 sessions
    h = {"last_decision": {"date": "2026-01-01"}}
    broken = line(150, 100)                                       # falling, well below its 200-day, lags by > 15pp
    assert smoke_alarm(h, broken, spy, cfg, asof) < -15
    healthy_lagger = rises_then_stalls()                          # lags SPY by ~16pp but sits ABOVE its 200-day
    assert relative_return_pp(healthy_lagger, spy, 63) < -15 and smoke_alarm(h, healthy_lagger, spy, cfg, asof) is None
    assert smoke_alarm(h, line(100, 215), spy, cfg, asof) is None                      # keeping up
    assert smoke_alarm(h, line(150, 100, 150), spy, cfg, asof) is None                 # < 200 closes: can't test, no alarm
    assert smoke_alarm({"last_decision": {"date": "2026-08-10"}}, broken, spy, cfg, asof) is None  # looked at 10 days ago
    assert smoke_alarm(h, broken, None, cfg, asof) is None
    cfg["core"]["smoke_alarm_pp"] = 0
    assert smoke_alarm(h, broken, spy, cfg, asof) is None                                # switched off


def test_scan_sends_only_a_broken_laggard_to_reinitiation(cfg):
    cfg["core"].update(smoke_alarm_pp=15, smoke_alarm_sessions=63, smoke_alarm_rearm_days=30)
    spy = line(100, 230)
    s = empty_state(cfg)
    s["last_scan"] = "2026-08-10"
    s["holdings"] = {"BROKEN": holding("BROKEN", "CORE", 50), "STEADY": holding("STEADY", "CORE", 50)}
    s["cash_usd"] = 60000
    mkt = ScanMarket({"BROKEN": line(150, 100), "STEADY": rises_then_stalls(), "SPY": spy}, cfg)
    res = scan(s, mkt, ScanFetcher(), cfg, "2026-08-20")
    assert res["reinitiate"] == ["BROKEN"] and [a["ticker"] for a in res["smoke_alarm"]] == ["BROKEN"]
    broken = next(f for f in res["flagged"] if f["ticker"] == "BROKEN")
    assert any("SMOKE ALARM" in r and "200-day" in r and "not a sell signal" in r for r in broken["reasons"])
    assert not any(m["action"] == "SELL" for m in res["mechanical_requests"])   # a prompt, never an automatic sale


# ------------------------------------------------------------------ momentum tilt (2026-11-15)
from screen import core_mix


def test_tactical_caps_and_core_weights_in_config(real_cfg):
    assert real_cfg["tactical"]["max_sleeve_pct"] == 40 and real_cfg["tactical"]["max_position_pct"] == 8
    assert real_cfg["screen"]["core_weights"] == {"quality": 0.40, "valuation": 0.30, "momentum": 0.30}
    assert real_cfg["screen"]["momentum"] == ["ch1y", "price_vs_sma200"]


def test_core_mix_weights_and_a_missing_momentum_renormalises(real_cfg):
    assert core_mix(real_cfg, 100, 0, 0) == pytest.approx(40) and core_mix(real_cfg, 0, 100, 0) == pytest.approx(30)
    assert core_mix(real_cfg, 0, 0, 100) == pytest.approx(30)
    assert core_mix(real_cfg, 80, 50, None) == pytest.approx((80 * 0.4 + 50 * 0.3) / 0.7)   # momentum drops out
    assert core_mix(real_cfg, None, 50, 50) is None and core_mix(real_cfg, 50, None, 50) is None   # q and v required
    # a market leader (top momentum, middling value) now outranks a cheap business that is not working
    assert core_mix(real_cfg, 80, 40, 95) > core_mix(real_cfg, 80, 70, 10)


def test_cluster_cap_sizes_a_tactical_buy_down_too(cfg):
    cfg["tactical"].update(max_sleeve_pct=40, max_position_pct=8)
    e = cluster_engine(cfg, 40)
    e.process([tac_buy("NVDA", 150.0, conviction=4, target_weight_pct=8.0, exit_plan={"target": 150.0, "stop": 90.0})])
    assert [r["ticker"] for r in e.applied] == ["NVDA"] and not e.rejections
    assert cluster_weight(e, ["NVDA"]) <= 8.0 and cluster_weight(e, ["AAPL", "MSFT", "NVDA"]) <= 40.0
    e2 = cluster_engine(cfg, 32.5)   # room 0.5%: under a tactical position's 1% minimum
    e2.process([tac_buy("NVDA", 150.0, conviction=4, target_weight_pct=8.0, exit_plan={"target": 150.0, "stop": 90.0})])
    assert not e2.applied and e2.rejections[0]["rule"] == "CLUSTER_MAX"
