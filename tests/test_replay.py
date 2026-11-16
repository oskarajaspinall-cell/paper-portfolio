import datetime as dt
import math
import random

import pytest

import replay
from replay import cash_target, metrics, momentum_6_1, replay as run_replay, target_weights, vol_pct


def days(n, d0="2024-01-01"):
    d, out = dt.date.fromisoformat(d0), []
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d += dt.timedelta(days=1)
    return out


def walk(n, drift, vol, seed, start=100.0):
    rnd, c, out = random.Random(seed), start, []
    for _ in range(n):
        c *= math.exp(drift + rnd.gauss(0, vol))
        out.append(c)
    return out


def test_momentum_skips_the_last_month_and_needs_history():
    flat_then_spike = [100.0] * 150 + [150.0] * 10          # the spike is inside the skipped month
    assert momentum_6_1([100.0] * 100) is None
    assert momentum_6_1(flat_then_spike) == pytest.approx(0.0)   # t-21 and t-126 are both still flat
    spike_only_last_week = [100.0] * 160 + [200.0] * 5
    assert momentum_6_1(spike_only_last_week) == pytest.approx(0.0)  # t-21 .. t-126 both flat


def test_cash_target_follows_the_50_200_trend(real_cfg):
    up = [100 + i * 0.2 for i in range(260)]
    down = [152 - i * 0.2 for i in range(260)]
    assert cash_target(up, real_cfg) == pytest.approx(0.05)       # fast average well above slow: reserve minimum
    assert cash_target(down, real_cfg) == pytest.approx(0.35)     # fast well below slow: reserve maximum
    assert 0.05 < cash_target([100.0] * 260, real_cfg) < 0.35     # inside the band: in between


def test_weights_are_floored_capped_and_never_scaled_up(real_cfg):
    hist = {f"T{i}": walk(260, 0.001 + i * 0.0002, 0.005 + i * 0.002, i) for i in range(12)}
    bench = [100 + i * 0.2 for i in range(260)]                    # bull: 5% reserve
    w = target_weights(hist, bench, real_cfg, k=12)
    assert w and all(0.07 - 1e-9 <= x <= 0.15 + 1e-9 for x in w.values())
    assert sum(w.values()) <= 0.95 + 1e-9                          # fits 100% - reserve, remainder stays cash
    assert len(w) < 12                                             # 12 x >=7% = 84%+, some drop or all fit but never scaled
    bear = [152 - i * 0.2 for i in range(260)]                     # bear: 35% reserve -> fewer names
    assert sum(target_weights(hist, bear, real_cfg, k=12).values()) <= 0.65 + 1e-9


def test_replay_runs_costs_bite_and_metrics_are_sane(real_cfg):
    n = 700
    ds = days(n)
    bench = list(zip(ds, [100 * math.exp(0.0004 * i) for i in range(n)]))
    closes = {f"T{i}": list(zip(ds, walk(n, 0.0006 + i * 0.0001, 0.012, i))) for i in range(10)}
    free = run_replay(closes, bench, real_cfg, k=5, cost_bps=0)
    paid = run_replay(closes, bench, real_cfg, k=5, cost_bps=50)
    assert free["rebalances"] > 12 and free["start"] == ds[201]
    assert paid["strategy"]["total_return_pct"] < free["strategy"]["total_return_pct"]
    assert 0 < free["strategy"]["max_drawdown_pct"] < 100 and free["spy_metrics"]["total_return_pct"] > 0
    text = replay.render(free, list(closes), 5, 0, "2026-11-15")
    assert "not an out-of-sample test" in text and "survivorship" in text


def test_metrics_edge_cases():
    assert metrics([1.0, 1.0]) == {}
    m = metrics([1.0, 1.1, 0.99, 1.2, 1.3])
    assert m["max_drawdown_pct"] == pytest.approx(10.0)
