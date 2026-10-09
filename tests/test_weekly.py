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
        news = [{"title": f"{t} wins big contract", "source": "Reuters", "ago": "2 days ago", "url": f"https://x/{t}/1"},
                {"title": f"{t} price target raised at UBS", "source": "TheFly", "ago": "1 day ago", "url": f"https://x/{t}/2"}]
        return {"url": f"https://stockanalysis.com/fake/{t}/history/", "currency": "USD", "rows": self.hist[t], "news": news}


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
    mover = next(f for f in res["flagged"] if f["ticker"] == "MOVER")
    assert [h["title"] for h in mover["figures"]["recent_headlines"]] == ["MOVER wins big contract"]  # rating dropped
    assert all("recent_headlines" not in u for u in res["unflagged"])


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
    assert [a[0] for a in agents] == ["macro-strategist"]  # quiet week: only the weekly cash-strategy view
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
    assert seen == ["macro-strategist", "researcher", "macro-overlay", "evaluator", "mc-parameters", "portfolio-manager"]
    assert "full re-initiation of an existing CORE holding (scan: core or macro trigger fired)" in prompts[1]
    assert "Decide ADD, HOLD, TRIM or SELL" in prompts[3]


def test_failed_run_applies_no_trades_and_logs_error(fake_repo, monkeypatch):
    before = {p.name: p.read_bytes() for p in (fake_repo / "portfolio").iterdir()}
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, SCAN_QUIET, [], fail_on="decision_log.py update"))
    assert wr.run("2026-10-10", False, 0, agent=lambda *a: None) == 1
    after = {p.name: p.read_bytes() for p in (fake_repo / "portfolio").iterdir()}
    assert after == before  # the mechanical SELL that was "applied" mid-run is rolled back
    err = (fake_repo / "runs" / "2026-10-10" / "error.log").read_text()
    assert "FAILED at step: decision log" in err and "No trades from this run were applied" in err
    assert not (fake_repo / "runs" / "2026-10-10" / ".portfolio-backup").exists()


def test_paused_exits_without_changes(fake_repo, monkeypatch, tmp_path):
    monkeypatch.setattr(wr, "LOCK", tmp_path / "lock")
    (fake_repo / "PAUSED").write_text("")
    monkeypatch.setattr(wr, "sh", lambda *a: pytest.fail("no step may run while paused"))
    assert wr.main(["--asof", "2026-10-10"]) == 0
    assert not (fake_repo / "runs").exists()


def test_local_flag_runs_despite_paused(fake_repo, monkeypatch, tmp_path):
    monkeypatch.setattr(wr, "LOCK", tmp_path / "lock")
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
    (tmp_path / "portfolio" / "decisions.csv").write_text("date,ticker,type\n2026-10-01,LON:SHEL,CORE\n2026-10-02,AMD,TACTICAL\n")
    assert screen.recently_researched(90, "2026-10-07", "CORE") == {"LON-SHEL"}
    assert screen.recently_researched(90, "2026-10-07", "TACTICAL") == {"AMD"}


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


def test_second_concurrent_review_refuses(fake_repo, monkeypatch, tmp_path):
    lock = tmp_path / "review.lock"
    monkeypatch.setattr(wr, "LOCK", lock)
    lock.mkdir()
    monkeypatch.setattr(wr, "sh", lambda *a: pytest.fail("must not run while another review holds the lock"))
    assert wr.main(["--asof", "2026-10-10", "--local"]) == 1
    lock.rmdir()


def test_parallel_initiations_skip_failures_and_continue(fake_repo, monkeypatch):
    import threading
    import time as _t
    picks = [{"ticker": f"N{i}", "type": "CORE", "score": 90 - i} for i in range(6)]
    (fake_repo / "reports" / "screen" / "2026-10-10.json").write_text(json.dumps({"picks": picks}))
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, dict(SCAN_QUIET, exits=[], mechanical_requests=[]), []))
    live, peak, pm_prompt = [0], [0], []
    lock = threading.Lock()

    def agent(name, prompt, log):
        t = prompt.split()[1].rstrip(",") if name != "portfolio-manager" else None
        if name == "portfolio-manager":
            pm_prompt.append(prompt)
            (fake_repo / "runs" / "2026-10-10" / "submit.json").write_text("{}")
            return
        if name == "evaluator":
            t = prompt.split()[1]
        with lock:
            live[0] += 1
            peak[0] = max(peak[0], live[0])
        _t.sleep(0.05)
        with lock:
            live[0] -= 1
        if t == "N2":
            raise wr.StepFailed("simulated researcher crash")
        d = fake_repo / "research" / t
        d.mkdir(exist_ok=True)
        if name == "researcher":
            (d / "2026-10-10.md").write_text("note")
        else:
            (d / "2026-10-10-evaluation.md").write_text(EVAL.replace("AAA", t) % ("AVOID", 1))

    assert wr.run("2026-10-10", False, None, agent=agent) == 0           # one failure did not cancel the week
    assert 1 < peak[0] <= 3                                               # ran in parallel, never more than 3
    m = json.loads((fake_repo / "runs" / "2026-10-10" / "run.json").read_text())
    assert [x["ticker"] for x in m["skipped"]] == ["N2"]
    assert sorted(d["ticker"] for d in m["decisions"]) == ["N0", "N1", "N3", "N4", "N5"]
    assert "N2" not in pm_prompt[0] and "N5" in pm_prompt[0]
    assert not (fake_repo / "research" / "N2" / "2026-10-10.md").exists()  # no half-finished docs


def test_reinitiation_failure_still_cancels_the_week(fake_repo, monkeypatch):
    scan_ = dict(SCAN_QUIET, reinitiate=["TRIG"], exits=[], mechanical_requests=[])
    (fake_repo / "portfolio" / "state.json").write_text(json.dumps({"holdings": {"TRIG": {"type": "CORE"}}}))
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, scan_, []))

    def agent(name, prompt, log):
        raise wr.StepFailed("researcher crashed")
    assert wr.run("2026-10-10", False, 0, agent=agent) == 1
    assert "reinitiate TRIG" in (fake_repo / "runs" / "2026-10-10" / "error.log").read_text()


def test_run_builds_dashboard_but_its_failure_is_not_fatal(fake_repo, monkeypatch):
    calls = []
    base = make_sh(fake_repo, SCAN_QUIET, calls)

    def sh(args, log, timeout=None):
        if "dashboard.py" in " ".join(args):
            calls.append("dashboard")
            raise wr.StepFailed("disk full")
        return base(args, log)
    monkeypatch.setattr(wr, "sh", sh)
    assert wr.run("2026-10-10", False, 0, agent=lambda *a: None) == 0
    assert "dashboard" in calls and "dashboard not updated" in (fake_repo / "runs" / "2026-10-10" / "run.log").read_text()


def test_dashboard_series_and_safe_embedding():
    import dashboard
    vals = [{"date": "2026-10-09", "total_usd": "100000", "spy_close": "500", "baseline_usd": ""},
            {"date": "2026-10-09", "total_usd": "99990", "spy_close": "500", "baseline_usd": "99990"},
            {"date": "2026-10-16", "total_usd": "102000", "spy_close": "505", "baseline_usd": "101000"}]
    s = dashboard.series(vals, 100000)
    assert [p["date"] for p in s] == ["2026-10-09", "2026-10-16"]          # last row per date
    assert s[1]["portfolio"] == pytest.approx(102) and s[1]["spy"] == pytest.approx(101)
    assert s[1]["baseline"] == pytest.approx(101)
    html = dashboard.render({"x": "</script><script>alert(1)</script>"})
    assert "</script><script>alert(1)" not in html                          # data can't break out of its tag


def test_decision_log_relabels_low_conviction_buys(real_cfg, tmp_path, monkeypatch):
    monkeypatch.setattr(dl, "ROOT", tmp_path)
    (tmp_path / "e.md").write_text(EVAL % ("BUY", 3))
    m = DLMarket(real_cfg, {"AAA": {"2026-01-05": 100}, "SPY": {"2026-01-05": 500}})
    rows = dl.record([str(tmp_path / "e.md")], m, "2026-01-10", [])
    assert rows[0]["decision"] == "AVOID" and "below the minimum 4" in rows[0]["note"]
    out = tmp_path / "d.csv"
    dl.write(rows, out)
    assert dl.read(out)[0]["note"].startswith("relabelled BUY->AVOID")


def test_montecarlo_failure_is_reported_but_never_blocks(fake_repo, monkeypatch):
    import weekly_report
    picks = [{"ticker": "N0", "type": "CORE", "score": 90}]
    (fake_repo / "reports" / "screen" / "2026-10-10.json").write_text(json.dumps({"picks": picks}))
    monkeypatch.setattr(wr, "sh", make_sh(fake_repo, dict(SCAN_QUIET, exits=[], mechanical_requests=[]), []))
    pm = []

    def agent(name, prompt, log):
        d = fake_repo / "research" / "N0"
        d.mkdir(exist_ok=True)
        if name == "researcher":
            (d / "2026-10-10.md").write_text("note")
        elif name == "evaluator":
            (d / "2026-10-10-evaluation.md").write_text(EVAL.replace("AAA", "N0") % ("BUY", 4))
        elif name == "mc-parameters":
            raise wr.StepFailed("12m median outside the researched bear-to-bull range")
        elif name == "portfolio-manager":
            pm.append(prompt)
            (fake_repo / "runs" / "2026-10-10" / "submit.json").write_text("{}")

    assert wr.run("2026-10-10", False, None, agent=agent) == 0       # the week is not cancelled
    assert pm and "N0" in pm[0]                                         # the decision still goes to the PM
    log = (fake_repo / "runs" / "2026-10-10" / "montecarlo-failures.log").read_text()
    assert log.startswith("N0\t") and "bear-to-bull" in log
    (fake_repo / "runs" / "2026-10-10" / "submit-mechanical.json").unlink()  # fake-shell artefact, not real output
    monkeypatch.setattr(weekly_report, "ROOT", fake_repo)
    md = weekly_report.build(fake_repo / "runs" / "2026-10-10", "2026-10-10", fake_repo / "portfolio")
    assert "**N0** Monte Carlo FAILED (nothing written; decision unaffected)" in md


# ------------------------------------------------------------------ macro overlay
MACRO_OK = """# Macro overlay: X (X) — 2026-10-07
## Assessment
Real yields rose 0.7pp in 3 months [Certain] (https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10, 2026-10-05).
## Overlay
```json
%s
```
"""


def macro_md(**over):
    d = {"macro_weight": "secondary", "macro_basis": "long-duration growth multiple is sensitive to real yields",
         "dominant_chain": "real yields -> discount rate -> multiple", "market_pricing": "breakevens 2.36%",
         "macro_bull": "real yields fall -> multiple +", "macro_bear": "real yields rise -> multiple -",
         "macro_tilt": {"direction": "toward bear", "size": "small", "reason": "real yields rising"},
         "refresh_triggers": [{"text": "10y real yield above 3.2%", "check": {"source": "fred", "series": "DFII10", "op": ">", "value": 3.2}},
                              {"text": "PBoC cuts the RRR"}],
         "sources": ["https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10 (2026-10-05)"]}
    d.update(over)
    return MACRO_OK % json.dumps(d)


def test_check_macro_valid_and_invalid(real_cfg):
    from check_docs import check_macro
    assert check_macro(macro_md(), real_cfg)[0] == []
    assert check_macro(macro_md(macro_weight="context", dominant_chain=None, refresh_triggers=None), real_cfg)[0] == []
    assert any("macro_weight" in e for e in check_macro(macro_md(macro_weight="huge"), real_cfg)[0])
    assert any("refresh_triggers" in e for e in check_macro(macro_md(refresh_triggers=[{"text": "x"}]), real_cfg)[0])
    assert any("macro_tilt" in e for e in check_macro(macro_md(macro_tilt={"direction": "up"}), real_cfg)[0])
    bad = macro_md(refresh_triggers=[{"text": "a", "check": {"source": "bloomberg", "series": "X", "op": ">", "value": 1}}, {"text": "b"}])
    assert any("trigger check" in e for e in check_macro(bad, real_cfg)[0])
    bad_src = macro_md().replace("## Overlay", "See https://www.zerohedge.com/x [Guessing].\n## Overlay")
    assert any("not on the allowlist" in e for e in check_macro(bad_src, real_cfg)[0])


def test_fred_trigger_fires_only_in_window():
    from macro_data import fired, parse_csv
    rows = parse_csv("observation_date,DFII10\n2026-09-28,3.0\n2026-09-29,.\n2026-10-01,3.3\n2026-10-05,3.1\n", "u")
    assert [r["date"] for r in rows] == ["2026-09-28", "2026-10-01", "2026-10-05"]   # '.' = missing, skipped
    assert fired(rows, ">", 3.2, "2026-09-30", "2026-10-07") == {"date": "2026-10-01", "value": 3.3}
    assert fired(rows, ">", 3.2, "2026-10-02", "2026-10-07") is None
    assert fired(rows, "<", 3.05, None, "2026-10-07")["date"] == "2026-09-28"


def test_scan_macro_trigger_reinitiates_and_no_change_line(cfg, tmp_path, monkeypatch):
    import weekly_scan as ws
    monkeypatch.setattr("common.ROOT", tmp_path)
    for t in ("HOT", "CALM"):
        (tmp_path / "research" / t).mkdir(parents=True)
        (tmp_path / "research" / t / "2026-09-01-macro.md").write_text(macro_md())

    class Fred:
        def __init__(self, v): self.v = v
        def series(self, sid): return {"rows": [{"date": "2026-09-15", "value": self.v}]}

    hot = ws.macro_check("HOT", "2026-09-05", "2026-09-20", Fred(3.4))
    assert hot["fired"] and "DFII10 = 3.4" in hot["fired"][0] and hot["text_triggers"] == ["PBoC cuts the RRR"]
    calm = ws.macro_check("CALM", "2026-09-05", "2026-09-20", Fred(2.9))
    assert calm["fired"] == [] and "macro: no change" in calm["line"]
    assert ws.macro_check("NONE", None, "2026-09-20", Fred(9))["line"] is None   # no overlay: nothing to check


def test_macro_failure_never_blocks_research(fake_repo, monkeypatch):
    seen = []
    def agent(name, prompt, log):
        seen.append((name, prompt))
        d = fake_repo / "research" / "N0"
        d.mkdir(exist_ok=True)
        if name == "researcher":
            (d / "2026-10-10.md").write_text("note")
        elif name == "macro-overlay":
            raise wr.StepFailed("FRED unreachable")
        elif name == "evaluator":
            (d / "2026-10-10-evaluation.md").write_text(EVAL.replace("AAA", "N0") % ("AVOID", 1))
    (fake_repo / "runs" / "2026-10-10").mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(wr, "sh", lambda args, log, timeout=None: "")
    ev = wr.research_and_evaluate("N0", "CORE", "2026-10-10", "x", agent, lambda m: None, fake_repo / "runs" / "2026-10-10")
    assert ev.name == "2026-10-10-evaluation.md"
    evaluator_prompt = next(p for n, p in seen if n == "evaluator")
    assert "macro overlay" not in evaluator_prompt                      # evaluated without it, not blocked


def test_dashboard_week_tile_spans_seven_days():
    import dashboard
    ser = [{"date": d, "portfolio": p, "spy": 100.0} for d, p in
           (("2026-10-02", 100.0), ("2026-10-05", 101.0), ("2026-10-09", 102.0), ("2026-10-13", 104.0))]
    w = dashboard.week_change(ser)
    assert w["from"] == "2026-10-05" and w["portfolio"] == pytest.approx(104 / 101 - 1)
    assert dashboard.week_change(ser[:1]) is None


@pytest.mark.parametrize("decision,held,runs", [("AVOID", False, False), ("BUY", False, True), ("HOLD", True, True)])
def test_monte_carlo_only_for_buys_and_holdings(tmp_path, monkeypatch, decision, held, runs):
    (tmp_path / "research" / "XYZ").mkdir(parents=True)
    (tmp_path / "portfolio").mkdir()
    (tmp_path / "portfolio" / "state.json").write_text(json.dumps({"holdings": {"XYZ": {}} if held else {}}))
    monkeypatch.setattr(wr, "ROOT", tmp_path)
    monkeypatch.setattr(wr, "check_doc", lambda *a: None)
    monkeypatch.setattr(wr, "sh", lambda *a, **k: "")
    monkeypatch.setattr(wr, "run_macro", lambda *a: False)
    ran = []
    monkeypatch.setattr(wr, "run_montecarlo", lambda *a: ran.append(a[0]))

    def agent(name, prompt, log):
        d = tmp_path / "research" / "XYZ"
        if name == "researcher":
            (d / "2026-10-10.md").write_text("note")
        if name == "evaluator":
            (d / "2026-10-10-evaluation.md").write_text("# E\n```json\n" + json.dumps({"decision": decision}) + "\n```\n")
    logs = []
    wr.research_and_evaluate("XYZ", "CORE", "2026-10-10", "why", agent, logs.append, tmp_path)
    assert (ran == ["XYZ"]) == runs
    assert runs or any("Monte Carlo skipped" in m for m in logs)


def test_fair_value_reached_fires_once_per_crossing(cfg):
    from weekly_scan import fair_value_reached
    fv = {"base": 100.0}
    assert not fair_value_reached(99.0, fv, None, "2026-10-09", cfg)
    assert fair_value_reached(100.0, fv, None, "2026-10-09", cfg)
    assert not fair_value_reached(100.0, None, None, "2026-10-09", cfg)  # no valuation: never
    prior = {"date": "2026-10-09", "close": 101.0}
    assert not fair_value_reached(105.0, fv, prior, "2026-10-16", cfg)   # already reviewed this crossing
    assert fair_value_reached(111.2, fv, prior, "2026-10-16", cfg)       # a further 10% rise re-arms
    assert fair_value_reached(102.0, fv, prior, "2027-01-08", cfg)       # 90 days later re-arms


def test_scan_fair_value_reinitiates_and_records(cfg, monkeypatch, tmp_path):
    import weekly_scan as WS
    flat = rows([("2026-09-04", 100), ("2026-09-08", 101), ("2026-09-14", 102)])
    s = empty_state(cfg)
    s["last_scan"] = "2026-09-05"
    text = [{"text": "Bookings growth below 4% for two quarters"}]
    s["holdings"] = {"FV": holding("FV", "CORE", 50, triggers=text), "LOW": holding("LOW", "CORE", 50, triggers=text)}
    s["cash_usd"] = 60000
    vals = {"FV": {"base": 101.5, "currency": "USD", "file": "research/FV/v.json", "asof": "2026-09-01"},
            "LOW": {"base": 150.0, "currency": "USD", "file": "research/LOW/v.json", "asof": "2026-09-01"}}
    monkeypatch.setattr(WS, "latest_base_fair_value", lambda t: vals[t])
    f = ScanFetcher(events={"LOW": [{"date": "2026-09-10", "title": "Q3", "types": ["earnings_release"]}]}, stats={})
    res = scan(s, ScanMarket({"FV": flat, "LOW": flat}, cfg), f, cfg, "2026-09-20")
    assert res["reinitiate"] == ["FV"] and res["review"] == ["LOW"]
    fl = {x["ticker"]: x for x in res["flagged"]}
    assert any(r.startswith("FAIR VALUE:") and "not a sell signal" in r for r in fl["FV"]["reasons"])
    assert fl["LOW"]["figures"]["text_triggers"] == ["Bookings growth below 4% for two quarters"]
    WS.record_fv_reviews(res["fair_value_reached"], "2026-09-20")
    again = scan(s, ScanMarket({"FV": flat, "LOW": flat}, cfg), ScanFetcher(events={}, stats={}), cfg, "2026-09-27")
    assert again["reinitiate"] == []  # the crossing was reviewed
