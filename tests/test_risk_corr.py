import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from risk import Correlator, correlated_pairs, correlation  # noqa: E402

CFG = {"core": {"corr_flag": 0.7, "corr_weeks": 52}}


def series(seed, base=None, noise=1.0):
    rnd = random.Random(seed)
    return {f"2026-W{i:02d}" if i < 53 else f"2027-W{i-52:02d}":
            (base[k] if base else 0) + rnd.gauss(0, 0.02) * noise
            for i, k in zip(range(1, 61), (sorted(base) if base else [None] * 60))}


def test_correlated_pair_flagged_unrelated_not():
    a = series(1)
    b = {k: v + random.Random(k).gauss(0, 0.004) for k, v in a.items()}   # near copy
    c = series(2)                                                       # independent
    assert correlation(a, b) > 0.9
    assert abs(correlation(a, c)) < 0.5
    pairs = correlated_pairs({"A": a, "B": b, "C": c}, CFG)
    assert [(p["a"], p["b"]) for p in pairs] == [("A", "B")]


def test_too_few_weeks_gives_none():
    a = {f"2026-W{i:02d}": i * 0.01 for i in range(1, 10)}
    assert correlation(a, a) is None


def test_buy_warning_names_overlapping_holding():
    a = series(3)
    b = {k: v * 1.1 + random.Random(k).gauss(0, 0.003) for k, v in a.items()}
    c = series(4)

    class M:
        def history(self, t):
            raise KeyError(t)

    corr = Correlator(M(), CFG)
    corr._s = {"NEW": a, "HELD": b, "OTHER": c}
    w = corr.warning("NEW", {"holdings": {"HELD": {}, "OTHER": {}}})
    assert w and "HELD" in w and "OTHER" not in w
    assert corr.warning("OTHER", {"holdings": {"HELD": {}}}) is None
