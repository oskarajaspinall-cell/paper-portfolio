import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from portfolio import size_down_requests  # noqa: E402

CFG = {"core": {"min_buy_conviction": 4, "downgrade_trim_gap_pp": 1.0,
                "conviction_size_pct": {"1": 0, "2": 3, "3": 5, "4": 7, "5": 10}}}


class Sizer:
    def target(self, conv, t, s):
        return float(CFG["core"]["conviction_size_pct"][str(conv)]), ""


class Eng:
    sizer = Sizer()

    def pv(self, s):
        return 100_000.0

    def core_size(self, conv, t, s, for_trim=False):
        return self.sizer.target(conv, t, s)[0]


def state(**h):
    return {"cash_usd": 0, "holdings": {t: {"type": "CORE", "conviction": c, "market_value_usd": v}
                                        for t, (c, v) in h.items()}}


def test_downgraded_to_3_trims_to_5pct():
    r = size_down_requests(state(JKHY=(3, 7300)), Eng(), CFG)
    assert r == [r[0]] and r[0]["action"] == "TRIM" and r[0]["target_weight_pct"] == 5.0


def test_within_gap_and_high_conviction_untouched():
    assert size_down_requests(state(A=(3, 5800), B=(4, 12000), C=(5, 14000)), Eng(), CFG) == []


def test_conviction_1_sells_and_only_filter():
    s = state(X=(1, 4000), Y=(2, 6000))
    acts = {q["ticker"]: q["action"] for q in size_down_requests(s, Eng(), CFG)}
    assert acts == {"X": "SELL", "Y": "TRIM"}
    assert [q["ticker"] for q in size_down_requests(s, Eng(), CFG, only={"Y"})] == ["Y"]


def test_below_bar_never_scaled_up_and_trim_ignores_cash_room(cfg):
    from test_portfolio import engine, holding
    cfg["core"]["min_buy_conviction"] = 4
    eng = engine(cfg, {"AAPL": holding("AAPL", "CORE", 8, conv=3)}, cash=10000)
    s = eng.s
    eng.sizer.target = lambda c, t, st: (float(cfg["core"]["conviction_size_pct"][str(c)]) * 1.4, "")
    assert eng.core_size(3, "AAPL", s) == float(cfg["core"]["conviction_size_pct"]["3"])   # no scale-up below the bar
    four = float(cfg["core"]["conviction_size_pct"]["4"]) * 1.4
    assert eng.core_size(4, "AAPL", s, for_trim=True) == four                             # trim: no cash-room cap
    eng.sizer.target = lambda c, t, st: (float(cfg["core"]["conviction_size_pct"][str(c)]) * 0.8, "")
    assert eng.core_size(3, "AAPL", s) == float(cfg["core"]["conviction_size_pct"]["3"]) * 0.8  # scale-down kept
