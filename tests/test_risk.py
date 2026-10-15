import datetime as dt
import math
import random

import pytest

from conftest import FakeMarket
import risk
from risk import Sizer, contributions, covariance, daily_vol, weekly_returns


def series(vol_pct, n=130, seed=1, start=100.0):
    """Closes with roughly the given annualised volatility (alternating +/- daily moves)."""
    d = vol_pct / 100 / math.sqrt(252)
    rnd = random.Random(seed)
    out, c = [], start
    for i in range(n):
        c *= math.exp(d if rnd.random() < 0.5 else -d)
        out.append(c)
    return out


class VolMarket(FakeMarket):
    def __init__(self, vols, cfg):
        super().__init__({t: (100.0, "USD", "Technology") for t in vols}, cfg)
        day0 = dt.date(2026, 4, 1)
        self.rows = {t: [{"date": (day0 + dt.timedelta(days=i)).isoformat(), "close": c}
                         for i, c in enumerate(series(v, seed=k))] for k, (t, v) in enumerate(vols.items())}

    def history(self, t):
        return {"url": f"https://stockanalysis.com/fake/{t}/history/", "currency": "USD", "rows": self.rows[t]}


def test_daily_vol_matches_construction_and_needs_history():
    assert daily_vol(series(40), 126) == pytest.approx(40, rel=0.02)
    assert daily_vol(series(40, n=30), 126) is None


def test_high_vol_name_sized_down_low_vol_up_within_clamp(cfg):
    m = VolMarket({"HOT": 60, "MID": 30, "CALM": 20, "DEAD": 5}, cfg)
    s = {"holdings": {}, "cash_usd": 100000}
    z = Sizer(m, cfg)
    assert z.target(4, "HOT", s)[0] == pytest.approx(7 * 0.6, abs=0.05)       # 30/60 = 0.5 -> clamped at 0.6
    assert z.target(4, "MID", s)[0] == pytest.approx(7.0, abs=0.15)
    assert z.target(4, "CALM", s)[0] == pytest.approx(7 * 1.4, abs=0.4)       # 30/20 = 1.5 -> clamped at 1.4
    assert z.target(5, "DEAD", s)[0] == pytest.approx(14.0)                   # 10 x 1.4, under the 15% trim cap


def test_reference_is_median_of_core_holdings_once_there_are_five(cfg):
    vols = {f"H{i}": 50 for i in range(5)} | {"NEW": 50}
    m = VolMarket(vols, cfg)
    s = {"holdings": {f"H{i}": {"type": "CORE"} for i in range(5)}, "cash_usd": 0}
    assert Sizer(m, cfg).scale("NEW", s)[0] == pytest.approx(1.0, abs=0.03)


def test_scaling_off_or_no_history_leaves_conviction_size(cfg):
    m = FakeMarket({"X": (100.0, "USD", "Technology")}, cfg)
    assert Sizer(m, cfg).target(4, "X", {"holdings": {}})[0] == 7.0
    cfg["core"]["vol_scaling"] = False
    assert Sizer(VolMarket({"X": 80}, cfg), cfg).target(4, "X", {"holdings": {}})[0] == 7.0


def test_contributions_two_asset_hand_case():
    # sigma 20% and 40%, correlation 0.5, weights 50/50
    cov = [[0.04, 0.04], [0.04, 0.16]]
    c = contributions([0.5, 0.5], cov)
    var = 0.25 * 0.04 + 0.25 * 0.16 + 2 * 0.25 * 0.04
    assert c["sigma_p"] == pytest.approx(math.sqrt(var))
    assert c["mcr"][0] == pytest.approx((0.5 * 0.04 + 0.5 * 0.04) / math.sqrt(var))
    assert sum(c["rc"]) == pytest.approx(1.0)
    assert c["rc"][1] == pytest.approx(0.5 * (0.5 * 0.04 + 0.5 * 0.16) / var)


def test_weekly_returns_and_covariance_need_common_weeks():
    rows = [{"date": (dt.date(2026, 1, 5) + dt.timedelta(days=i)).isoformat(), "close": 100 + i} for i in range(70)]
    w = weekly_returns(rows)
    assert len(w) == 9 and all(x > 0 for x in w.values())
    names, cov = covariance({"A": w, "B": w})
    assert cov[0][1] == pytest.approx(cov[0][0])
    with pytest.raises(ValueError):
        covariance({"A": dict(list(w.items())[:5]), "B": w})


def test_core_buy_is_vol_sized_and_target_recorded(cfg):
    from portfolio import Engine, empty_state, mark
    from test_portfolio import core_buy
    m = VolMarket({"HOT": 60}, cfg)
    s = empty_state(cfg)
    s["cash_usd"] = 100000.0
    mark(s, m)
    e = Engine(s, m, cfg, {"HOT": None}, "2026-10-06")
    assert e.sizer.target(4, "HOT", s)[1].endswith("x0.60")
    e.process([core_buy("HOT")])
    h = e.s["holdings"]["HOT"]
    assert h["target_pct"] == pytest.approx(4.2, abs=0.05)
    assert h["market_value_usd"] / 100000 * 100 == pytest.approx(h["target_pct"], abs=0.2)
