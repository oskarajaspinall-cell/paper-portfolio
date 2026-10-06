import json
import shutil

import pytest

import decision_log as dl
import weekly_run as wr
from common import DataError
from conftest import FakeMarket
from portfolio import empty_state, mark
from weekly_scan import events_in_window, price_move, reference_close, scan, tactical_exit, trigger_hits, window


def rows(pairs):
    return [{"date": d, "close": c, "high": c, "low": c} for d, c in pairs]


H = rows([("2026-09-03", 100), ("2026-09-04", 100), ("2026-09-08", 104), ("2026-09-09", 93), ("2026-09-10", 88),
          ("2026-09-11", 112), ("2026-09-14", 96)])


# ------------------------------------------------------------------ reference close + window
def test_reference_close_last_close_before_previous_run():
    ref = reference_close(H, "2026-09-05", "2026-08-01")
    assert ref["date"] == "2026-09-04" and [r["date"] for r in window(H, ref)][0] == "2026-09-08"


def test_reference_close_uses_entry_if_opened_after_last_run():
    assert reference_close(H, "2026-09-05", "2026-09-09")["date"] == "2026-09-09"
    assert reference_close(H, None, "2026-09-03")["date"] == "2026-09-03"


# ------------------------------------------------------------------ flag rule 1: price move beyond +/-8%
@pytest.mark.parametrize("closes,flag", [([104, 107.9], False), ([104, 108.1], True), ([96, 91.9], True),
                                         ([92, 100], False), ([120, 101], True)])
def test_price_move_flag(closes, flag):
    ref = {"date": "2026-09-04", "close": 100}
    win = rows([(f"2026-09-0{5 + i}", c) for i, c in enumerate(closes)])
    assert price_move(ref, win, 8)["flag"] is flag


# ------------------------------------------------------------------ flag rule 2: earnings / filing in window
def test_events_in_window():
    ev = [{"date": "2026-09-04"}, {"date": "2026-09-08"}, {"date": "2026-09-14"}, {"date": "2026-10-06"}]
    assert [e["date"] for e in events_in_window(ev, "2026-09-04", "2026-10-06")] == ["2026-09-08", "2026-09-14"]


# ------------------------------------------------------------------ flag rule 3: core trigger hit
def test_trigger_hits():
    stats = {"grossMargin": {"value": 43.0}, "roic": {"value": 60.0}}
    trig = [{"text": "GM < 44", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 44}},
            {"text": "ROIC > 100", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 100}},
            {"text": "Debt rises", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3}},
            {"text": "Services growth stalls"}]
    hits, unchecked = trigger_hits(trig, stats)
    assert [h["field"] for h in hits] == ["grossMargin"]
    assert len(unchecked) == 2 and "data unavailable: debtEbitda" in unchecked[0]


# ------------------------------------------------------------------ mechanical tactical exits at the FIRST crossing close
PLAN = {"target": 110, "stop": 90, "time_limit": "2026-12-01"}


def test_stop_fills_at_first_crossing_close_even_on_gap():
    ex = tactical_exit(window(H, H[1]), PLAN, "2026-09-20")
    assert ex["fill_date"] == "2026-09-10" and ex["close"] == 88 and "stop" in ex["why"]  # gapped below 90: fill 88


def test_target_fills_at_first_crossing_close():
    ex = tactical_exit(window(H, H[1]), dict(PLAN, stop=80), "2026-09-20")
    assert ex["fill_date"] == "2026-09-11" and ex["close"] == 112 and "target" in ex["why"]


def test_first_crossing_wins_when_both_levels_crossed():
    ex = tactical_exit(window(H, H[1]), dict(PLAN, stop=94, target=111), "2026-09-20")
    assert ex["fill_date"] == "2026-09-09" and ex["close"] == 93  # stop crossed before the later target


def test_time_limit_exit_at_last_close_and_ignores_later_crossings():
    ex = tactical_exit(window(H, H[1]), dict(PLAN, stop=80, target=200, time_limit="2026-09-09"), "2026-09-20")
    assert ex["fill_date"] == "2026-09-14" and ex["close"] == 96 and "time limit" in ex["why"]
    assert tactical_exit(window(H, H[1]), dict(PLAN, stop=80, target=200), "2026-09-20") is None


# ------------------------------------------------------------------ full scan with fake market
class ScanMarket(FakeMarket):
    def __init__(self, hist, cfg):
        super().__init__({t: (r[-1]["close"], "USD", "Technology") for t, r in hist.items()}, cfg, asof="2026-09-20",
                         close_date="2026-09-14")
        self.hist = hist

    def history(self, t):
        return {"url": f"https://stockanalysis.com/fake/{t}/history/", "currency": "USD", "rows": self.hist[t]}


class ScanFetcher:
    def __init__(self, events=None, stats=None):
        self.events, self.stats, self.calls = events or {}, stats or {}, []

    def section(self, t, page):
        self.calls.append((t, page))
        if page == "filings":
            return {"source_url": f"https://stockanalysis.com/fake/{t}/filings/", "data": {"events": self.events.get(t, [])}}
        return {"source_url": f"https://stockanalysis.com/fake/{t}/statistics/", "data": self.stats.get(t, {})}


def holding(t, ptype, shares, **kw):
    h = {"type": ptype, "shares": shares, "currency": "USD", "sector": "S-" + t, "conviction": 3, "cost_basis_usd": 0,
         "entry_close_date": "2026-09-01", "market_value_usd": 0.0, "triggers": None, "exit_plan": None}
    h.update(kw)
    return h


def test_scan_end_to_end(cfg):
    flat = rows([("2026-09-04", 100), ("2026-09-08", 101), ("2026-09-14", 102)])
    hist = {"QUIET": flat, "MOVER": rows([("2026-09-04", 100), ("2026-09-10", 115), ("2026-09-14", 106)]),
            "TRIG": flat, "EARN": flat, "TAC": H, "BIG": flat}
    trig = [{"text": "GM < 44", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 44}},
            {"text": "ROIC < 10", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}}]
    s = empty_state(cfg)
    s["last_scan"] = "2026-09-05"
    s["holdings"] = {"QUIET": holding("QUIET", "CORE", 50, triggers=trig), "MOVER": holding("MOVER", "CORE", 50),
                     "TRIG": holding("TRIG", "CORE", 50, triggers=trig), "EARN": holding("EARN", "CORE", 50),
                     "TAC": holding("TAC", "TACTICAL", 30, exit_plan=PLAN), "BIG": holding("BIG", "CORE", 200)}
    s["cash_usd"] = 60000
    mkt = ScanMarket(hist, cfg)
    f = ScanFetcher(events={"EARN": [{"date": "2026-09-10", "title": "Q3", "types": ["earnings_release"]}]},
                    stats={"QUIET": {"grossMargin": {"value": 50}, "roic": {"value": 30}},
                           "TRIG": {"grossMargin": {"value": 40}, "roic": {"value": 30}}})
    res = scan(s, mkt, f, cfg, "2026-09-20")
    assert res["reinitiate"] == ["TRIG"]
    assert sorted(res["review"]) == ["EARN", "MOVER"]
    assert [u["ticker"] for u in res["unflagged"]] == ["QUIET"] and "no material change" in res["unflagged"][0]["line"]
    assert res["exits"][0]["ticker"] == "TAC" and res["exits"][0]["fill_date"] == "2026-09-10"
    assert ("TAC", "filings") not in f.calls  # exited mechanically: nothing else looked up
    req = {r["ticker"]: r for r in res["mechanical_requests"]}
    assert req["TAC"] == {"ticker": "TAC", "action": "SELL", "position_type": "TACTICAL", "fill_date": "2026-09-10",
                          "reason": req["TAC"]["reason"]}
    assert req["BIG"]["action"] == "TRIM" and req["BIG"]["target_weight_pct"] == 15  # 20.4k of ~95k > 15%


# ------------------------------------------------------------------ decision log
EVAL = """# Evaluation
## Bear case
x [Likely]
## Bull case
y [Likely]
## Decision
```json
{"ticker": "AAA", "decision": "%s", "position_type": "CORE", "conviction": %d, "price_at_decision": 100,
 "price_date": "2026-01-05", "research_note": "n", "rationale": "r", "thesis": "t"}
```
"""


class DLMarket:
    """quote(ticker, on_or_before) from a hand-made price table."""

    def __init__(self, cfg, table):
        self.cfg, self.table = cfg, table

    def quote(self, t, d):
        pts = [(k, v) for k, v in sorted(self.table[t].items()) if k <= d]
        if not pts:
            raise DataError("https://stockanalysis.com/x/", "history.close", "too old")
        return {"close": pts[-1][1], "price_usd": pts[-1][1], "currency": "USD", "date": pts[-1][0]}


def test_decision_log_record_update_and_hits(cfg, tmp_path, monkeypatch):
    monkeypatch.setattr(dl, "ROOT", tmp_path)
    (tmp_path / "e1.md").write_text(EVAL % ("BUY", 4))
    (tmp_path / "e2.md").write_text(EVAL % ("AVOID", 2))
    table = {"AAA": {"2026-01-05": 100, "2026-02-05": 110, "2026-04-03": 95},
             "SPY": {"2026-01-05": 500, "2026-02-05": 510, "2026-04-03": 520}}
    m = DLMarket(cfg, table)
    rows_ = dl.record([str(tmp_path / "e1.md"), str(tmp_path / "e2.md")], m, "2026-01-10", [])
    rows_ = dl.record([str(tmp_path / "e1.md")], m, "2026-01-10", rows_)  # idempotent
    assert len(rows_) == 2 and rows_[0]["spy_close"] == 500
    dl.update(rows_, m, "2026-04-10")
    buy, avoid = rows_
    assert buy["ret_1m"] == 10.0 and buy["spy_1m"] == 2.0 and buy["excess_1m"] == 8.0 and buy["hit_1m"] == 1
    assert avoid["hit_1m"] == 0                               # AVOID was wrong: stock beat SPY
    assert buy["hit_3m"] == 0 and avoid["hit_3m"] == 1        # -5% vs +4%: BUY wrong, AVOID right
    assert buy.get("ret_6m", "") == ""                        # not matured yet
    t = dl.hit_table(rows_)
    assert "| All decisions | 2 | 1/2 (50%) | 1/2 (50%) | – | – |" in t
    assert "| Conviction 4 | 1 | 1/1 (100%) | 0/1 (0%) | – | – |" in t
    assert "| TACTICAL | 0 |" in t


def test_decision_log_old_horizon_is_unavailable_not_guessed(cfg):
    r = [{"ticker": "AAA", "decision": "BUY", "price_date": "2026-01-05", "price_usd": 100, "spy_close": 500}]
    notes = dl.update(r, DLMarket(cfg, {"AAA": {"2027-01-01": 1}, "SPY": {"2027-01-01": 1}}), "2027-06-01")
    assert r[0]["ret_1m"] == "n/a" and "data unavailable" in notes[0]


# ------------------------------------------------------------------ weekly run: failure applies nothing
@pytest.fixture
def fake_repo(tmp_path, monkeypatch):
    port = tmp_path / "portfolio"
    port.mkdir()
    (port / "state.json").write_text(json.dumps({"holdings": {}, "cash_usd": 100000.0}))
    (port / "ledger.csv").write_text("date\n")
    (tmp_path / "reports" / "screen").mkdir(parents=True)
    (tmp_path / "research").mkdir()
    monkeypatch.setattr(wr, "ROOT", tmp_path)
    return tmp_path


def make_sh(root, scan, calls, fail_on=None):
    def sh(args, log):
        cmd = " ".join(args)
        calls.append(cmd)
        if fail_on and fail_on in cmd:
            raise wr.StepFailed(f"simulated failure in {fail_on}")
        run = root / "runs" / "2026-10-10"
        if "weekly_scan.py" in cmd:
            (run / "scan.json").write_text(json.dumps(scan))
            (run / "requests-mechanical.json").write_text(json.dumps(scan["mechanical_requests"]))
        if "portfolio.py submit" in cmd:  # pretend a trade was applied
            (root / "portfolio" / "ledger.csv").write_text("date\n2026-10-10,TAC,SELL\n")
            (root / "portfolio" / "state.json").write_text(json.dumps({"holdings": {}, "cash_usd": 1.0}))
            (run / "submit-mechanical.json").write_text(json.dumps({"applied": [{"ticker": "TAC"}], "rejected": []}))
        return ""
    return sh


SCAN_QUIET = {"reinitiate": [], "review": [], "unflagged": [{"ticker": "Q", "line": "Q: no material change"}],
              "exits": [{"ticker": "TAC"}], "mechanical_requests": [{"ticker": "TAC", "action": "SELL"}]}


def test_run_makes_no_model_calls_for_unflagged_or_exits(fake_repo, monkeypatch):
    calls, agents = [], []
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, SCAN_QUIET, calls))
    assert wr.run("2026-10-10", False, 0, agent=lambda *a: agents.append(a)) == 0
    assert agents == []  # unflagged holding + mechanical exit: zero agent sessions
    assert any("portfolio.py submit" in c and "requests-mechanical.json" in c for c in calls)


def test_run_reinitiates_fired_core_trigger(fake_repo, monkeypatch):
    scan_ = dict(SCAN_QUIET, reinitiate=["TRIG"], exits=[], mechanical_requests=[])
    (fake_repo / "portfolio" / "state.json").write_text(json.dumps({"holdings": {"TRIG": {"type": "CORE"}}}))
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, scan_, []))
    seen, prompts = [], []

    def agent(name, prompt, log):
        seen.append(name)
        prompts.append(prompt)
        d = fake_repo / "research" / "TRIG"
        d.mkdir(exist_ok=True)
        if name == "researcher":
            (d / "2026-10-10.md").write_text("note")
        if name == "evaluator":
            (d / "2026-10-10-evaluation.md").write_text(EVAL.replace("AAA", "TRIG") % ("HOLD", 3))
        if name == "portfolio-manager":
            (fake_repo / "runs" / "2026-10-10" / "submit.json").write_text("{}")

    assert wr.run("2026-10-10", False, 0, agent=agent) == 0
    assert seen == ["researcher", "evaluator", "portfolio-manager"]
    assert "full re-initiation of an existing CORE holding (scan: core trigger hit)" in prompts[0]
    assert "Decide ADD, HOLD, TRIM or SELL" in prompts[1]


def test_failed_run_applies_no_trades_and_logs_error(fake_repo, monkeypatch):
    before = {p.name: p.read_bytes() for p in (fake_repo / "portfolio").iterdir()}
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, SCAN_QUIET, [], fail_on="decision_log.py update"))
    assert wr.run("2026-10-10", False, 0, agent=lambda *a: None) == 1
    after = {p.name: p.read_bytes() for p in (fake_repo / "portfolio").iterdir()}
    assert after == before  # the mechanical SELL that was "applied" mid-run is rolled back
    err = (fake_repo / "runs" / "2026-10-10" / "error.log").read_text()
    assert "FAILED at step: decision log" in err and "No trades from this run were applied" in err
    assert not (fake_repo / "runs" / "2026-10-10" / ".portfolio-backup").exists()


def test_paused_exits_without_changes(fake_repo, monkeypatch):
    (fake_repo / "PAUSED").write_text("")
    monkeypatch.setattr(wr, "sh", lambda *a: pytest.fail("no step may run while paused"))
    assert wr.main(["--asof", "2026-10-10"]) == 0
    assert not (fake_repo / "runs").exists()


def test_local_flag_runs_despite_paused(fake_repo, monkeypatch):
    (fake_repo / "PAUSED").write_text("")
    calls = []
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, SCAN_QUIET, calls))
    monkeypatch.setattr(wr, "claude_agent", lambda *a: None)
    assert wr.main(["--asof", "2026-10-10", "--local", "--max-new", "0"]) == 0
    assert any("weekly_scan.py" in c for c in calls)  # it ran


def test_recently_researched_counts_only_logged_decisions(tmp_path, monkeypatch):
    import screen
    monkeypatch.setattr(screen, "ROOT", tmp_path)
    (tmp_path / "research" / "AAPL").mkdir(parents=True)
    (tmp_path / "research" / "AAPL" / "2026-10-01.md").write_text("dry-run note")
    assert screen.recently_researched(90, "2026-10-07") == set()  # a note alone doesn't block
    (tmp_path / "portfolio").mkdir()
    (tmp_path / "portfolio" / "decisions.csv").write_text("date,ticker\n2026-10-01,LON:SHEL\n2026-01-01,MSFT\n")
    assert screen.recently_researched(90, "2026-10-07") == {"LON-SHEL"}


def test_report_lists_new_initiation_reasons(tmp_path):
    import weekly_report
    run = tmp_path / "run"
    run.mkdir()
    (run / "run.json").write_text(json.dumps({"decisions": [{"kind": "new", "ticker": "AMD", "decision": "AVOID",
        "conviction": 1, "rationale": "gap risk through the stop", "evaluation": "research/AMD/x.md"}]}))
    (tmp_path / "port").mkdir()
    md = weekly_report.build(run, "2026-10-07", tmp_path / "port")
    sec4 = md.split("## 4. Review notes")[1].split("## 5.")[0]
    assert "**AMD** new initiation → AVOID (conviction 1): gap risk through the stop" in sec4
