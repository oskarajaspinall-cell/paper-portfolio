"""The weekly run, in the required order. Agent steps are separate headless Claude Code sessions
(`claude -p --agent <name>`); everything else is a script. Each agent's output is checked by a
script before the next step.

  0. fill pending orders from earlier runs at their next open
  1. mark to market (pre-trade valuation)
  2. weekly_scan.py: flags, mechanical tactical exits and trims (no model calls)
  3. weekly-reviewer on flagged holdings (skipped if none)
  4. core re-initiations (researcher + evaluator) for fired triggers and escalations
  5. up to `max_new_initiations_per_week` new initiations from this week's screen picks, researched
     `parallel_research` at a time; a failed NEW initiation skips that stock (listed in the report)
  6. mechanical exits/trims submitted by script (no model call); then portfolio-manager turns the
     evaluators' decisions into requests -> portfolio.py submit (skipped if there are none)
  7. decision log: record this run's decisions, update matured outcomes
  8. stamp the scan date; 9. weekly report; 10. dashboard (docs/index.html)

Test switch: env PAPER_SIMULATE_FAILURE=<step name prefix, e.g. "decision log"> forces a failure there.

Apart from skipped new initiations, if ANY step fails: portfolio/ is restored to its state at the start of the run (no trades applied),
runs/<date>/error.log is written, and the exit code is 1.

    python scripts/weekly_run.py [--asof YYYY-MM-DD] [--dry-run] [--max-new N] [--local]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Ticker, load_config  # noqa: E402

PY = [str(ROOT / "bin" / "py")]
# Least privilege (security review 2026-10-15): agents read untrusted web pages, so each may run only the
# scripts it needs (never bare `bin/py`, which would allow `bin/py -c ...`) and write only to its output
# folders (Edit path rules also cover Write; a bare "Write" would allow any path), so it can't replace a
# script and then run it.
_CHECK = "Bash(bin/py scripts/check_docs.py:*)"
_OUT = "Edit(research/**),Edit(reports/**),Edit(runs/**)"
TOOLS = {"researcher": f"Read,Glob,Grep,WebFetch,Bash(bin/py scripts/fact_sheet.py:*),{_CHECK},{_OUT}",
         "evaluator": f"Read,Glob,Grep,{_CHECK},{_OUT}",
         "portfolio-manager": f"Read,Glob,Grep,Bash(bin/py scripts/portfolio.py:*),{_CHECK},Edit(runs/**),"
                              "Edit(portfolio/requests-*.json),Edit(logs/dry-run-requests-*.json)",
         "weekly-reviewer": f"Read,Glob,Grep,WebFetch,{_OUT}",
         "macro-overlay": f"Read,Glob,Grep,WebFetch,{_CHECK},{_OUT}",
         "macro-strategist": f"Read,Glob,Grep,WebFetch,{_CHECK},{_OUT}",
         "swap-reviewer": f"Read,Glob,Grep,{_OUT}"}


class StepFailed(Exception):
    pass


AGENT_TIMEOUT = 30 * 60  # seconds; a stuck session can't hang the night


def sh(args: list[str], log, timeout: int | None = None) -> str:
    log(f"$ {' '.join(args)}".replace(f"{ROOT}/", ""))  # no absolute home paths in the public logs
    try:
        p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        raise StepFailed(f"{args[0]} timed out after {timeout}s") from e
    log(p.stdout.strip()[-4000:].replace(f"{ROOT}/", ""))
    if p.returncode != 0:
        raise StepFailed(f"{' '.join(args)} exited {p.returncode}: {p.stderr.strip()[-2000:]}")
    return p.stdout


def claude_agent(name: str, prompt: str, log) -> str:
    """Run one subagent as its own headless session. Replaced in tests."""
    return sh(["claude", "-p", prompt, "--agent", name, "--permission-mode", "dontAsk", "--allowedTools", TOOLS[name],
               "--output-format", "text"],
              log, timeout=AGENT_TIMEOUT)


def check_doc(kind: str, path: Path, log) -> None:
    sh(PY + ["scripts/check_docs.py", kind, str(path)], log)


def entry_hit_reason(h: dict) -> str:
    """The re-research instruction for a stock that reached its entry price (daily close or intraday check), or
    for a dip-radar signal (scripts/dip_radar.py writes its own)."""
    if h.get("kind") == "dip":
        return h["reason"]
    how = f"traded at {h['close']} at {h['time']}" if h.get("intraday") else f"closed at {h['close']} on {h['hit_date']}"
    return (f"Re-research: the price reached the entry price we set ({h['entry_price']}; it {how}). "
            "Find out why it fell; decide BUY or AVOID.")


def discard_partial(ticker: str, asof: str) -> None:
    """A failed research step leaves no half-finished docs: today's note, macro, evaluation, valuation, fact sheet
    and SEC delta for that stock."""
    d = ROOT / "research" / Ticker(ticker).slug
    for f in list(d.glob(f"{asof}*")) + list(d.glob(f"factsheet-{asof}.md")) + list(d.glob(f"sec-delta-{asof}.md")):
        f.unlink()


def research_and_evaluate(ticker: str, ptype: str, asof: str, why: str, agent, log, run: Path) -> Path:
    slug = Ticker(ticker).slug
    note, ev = ROOT / "research" / slug / f"{asof}.md", ROOT / "research" / slug / f"{asof}-evaluation.md"
    if note.exists() and ev.exists():  # a re-run (2026-10-24: the usage limit stopped the first): today's research
        try:                            # is reused when both documents still pass their checks
            check_doc("note", note, log)
            check_doc("eval", ev, log)
            log(f"== {ticker}: reusing today's research ({ev.relative_to(ROOT)})")
            return ev
        except StepFailed as e:
            log(f"{ticker}: today's research doesn't pass its checks, redoing it: {str(e)[:200]}")
    delta = ""
    if ptype == "CORE":  # SEC filing delta (scripts/sec_delta.py): context only, a failure never blocks research
        try:
            out = sh(PY + ["scripts/sec_delta.py", ticker, "--asof", asof], log, timeout=300)
            if out.strip().startswith("OK "):
                delta = (f" SEC filing delta: research/{slug}/sec-delta-{asof}.md (read it before any web fetch; "
                         "it does not count toward the fetch cap).")
        except StepFailed as e:
            log(f"sec delta skipped for {ticker}: {e}")
    agent("researcher", f"Ticker {ticker}, note type {ptype}, date {asof}. {why}{delta}", log)
    if not note.exists():
        raise StepFailed(f"researcher wrote no note at {note}")
    check_doc("note", note, log)
    macro = run_macro(ticker, slug, asof, agent, log)
    agent("evaluator", f"Evaluate {ticker} for {asof}: fact sheet research/{slug}/factsheet-{asof}.md, "
                       f"note research/{slug}/{asof}.md, state portfolio/state.json"
                       + (f", macro overlay research/{slug}/{asof}-macro.md" if macro else "") + f". {why}", log)
    if not ev.exists():
        raise StepFailed(f"evaluator wrote no evaluation at {ev}")
    check_doc("eval", ev, log)
    try:  # final fair value with any evaluator overrides (inform-only: a failure never blocks the decision)
        sh(PY + ["scripts/valuation.py", ticker, "--asof", asof, "--eval", str(ev)], log)
    except StepFailed as e:
        log(f"!! FAIR VALUE NOT UPDATED for {ticker}: {e}")
    return ev


def run_macro(ticker: str, slug: str, asof: str, agent, log) -> bool:
    """Macro overlay (skill: macro-overlay). Non-blocking: on failure the stock is researched without it."""
    out = ROOT / "research" / slug / f"{asof}-macro.md"
    try:
        if not (ROOT / "reports" / "macro" / f"{asof}.json").exists():
            sh(PY + ["scripts/macro_data.py", "--asof", asof], log)  # official FRED snapshot, once per run
        agent("macro-overlay", f"Ticker {ticker}, date {asof}. Research: research/{slug}/factsheet-{asof}.md, "
                               f"research/{slug}/{asof}.md. Macro snapshot: reports/macro/{asof}.md. "
                               f"Write research/{slug}/{asof}-macro.md.", log)
        if not out.exists():
            raise StepFailed("macro-overlay wrote no file")
        check_doc("macro", out, log)
        return True
    except StepFailed as e:
        log(f"!! MACRO OVERLAY UNAVAILABLE for {ticker}: {e}")
        return False


def run_cash_strategy(asof: str, agent, log) -> None:
    """Score the regime (no LLM), then the macro-strategist may move it one notch with cited reasons. If the
    view step fails, the mechanical score stands (logged); if scoring itself fails the run continues and the
    rules use the latest earlier regime file (or the neutral reserve)."""
    try:
        if not (ROOT / "reports" / "macro" / f"{asof}.json").exists():
            sh(PY + ["scripts/macro_data.py", "--asof", asof], log)
        sh(PY + ["scripts/regime.py", "--asof", asof], log)
    except StepFailed as e:
        log(f"!! CASH STRATEGY SCORE FAILED (earlier regime / neutral reserve applies): {e}")
        return
    view = ROOT / "reports" / "regime" / f"{asof}-view.md"
    try:
        agent("macro-strategist", f"Date {asof}. Regime score: reports/regime/{asof}.md. Macro snapshot: "
                                  f"reports/macro/{asof}.md. Write reports/regime/{asof}-view.md.", log)
        if not view.exists():
            raise StepFailed("macro-strategist wrote no view")
        sh(PY + ["scripts/check_docs.py", "regime", str(view)], log)
        sh(PY + ["scripts/regime.py", "--apply-view", "--asof", asof], log)
    except Exception as e:  # noqa: BLE001  the view is optional: never cancels the week
        log(f"!! MACRO VIEW UNAVAILABLE (the mechanical score stands): {e}")


def run_funding_queue(asof: str, dry_run: bool, agent, log, rundir: Path) -> None:
    """Funding queue (2026-10-18): resubmit waiting conviction-4 BUYs that now fit above the cash reserve, then
    the swap-reviewer weighs the best one still waiting against the weakest CORE holdings. A swap is a BUY with
    `replaces`, validated by portfolio.py like any other trade."""
    dry = ["--dry-run"] if dry_run else []
    sh(PY + ["scripts/funding_queue.py", "review", "--asof", asof] + dry, log)
    brief = rundir / "funding-queue.md"
    if not sh(PY + ["scripts/funding_queue.py", "brief", "--asof", asof, "--out", str(brief)], log).strip().startswith("OK "):
        return  # nothing waiting
    review = rundir / "swap-review.md"
    agent("swap-reviewer", f"Brief runs/{asof}/funding-queue.md, date {asof}. Write runs/{asof}/swap-review.md.", log)
    if not review.exists():
        raise StepFailed("swap-reviewer wrote no swap-review.md")
    import funding_queue
    swap = funding_queue.parse_swap(review.read_text(), json.loads(brief.with_suffix(".json").read_text()))
    if swap is None:
        log("swap review: no swap this week")
        return
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    req = rundir / "requests-swap.json"
    req.write_text(json.dumps([funding_queue.swap_request(state, swap)], indent=1))
    sh(PY + ["scripts/portfolio.py", "submit", str(req), "--asof", asof, "--at-market",
             "--save", str(rundir / "submit-swap.json")] + dry, log)


def screen_picks(asof: str, max_age_days: int = 7) -> list[dict]:
    d = ROOT / "reports" / "screen"
    files = sorted(p for p in d.glob("20??-??-??.json")
                   if (dt.date.fromisoformat(asof) - dt.date.fromisoformat(p.stem)).days in range(0, max_age_days + 1))
    return json.loads(files[-1].read_text())["picks"] if files else []


def run(asof: str, dry_run: bool, max_new: int | None, agent=claude_agent, local: bool = False) -> int:
    cfg = load_config()
    rundir = ROOT / "runs" / asof
    rundir.mkdir(parents=True, exist_ok=True)
    logf = (rundir / "run.log").open("a")

    log_lock = threading.Lock()

    def log(msg):
        with log_lock:  # parallel researchers share this log
            logf.write(msg + "\n")
            logf.flush()

    port, backup = ROOT / "portfolio", rundir / ".portfolio-backup"
    if backup.exists():
        shutil.rmtree(backup)
    shutil.copytree(port, backup)
    manifest = {"asof": asof, "dry_run": dry_run, "decisions": [], "steps": []}

    def step(name):
        manifest["steps"].append(name)
        if os.environ.get("PAPER_SIMULATE_FAILURE") and name.startswith(os.environ["PAPER_SIMULATE_FAILURE"]):
            raise StepFailed(f"simulated failure at step '{name}' (PAPER_SIMULATE_FAILURE test switch)")
    try:
        if (ROOT / "PAUSED").exists() and not local:
            raise StepFailed("PAUSED file present (the workflow should have exited before this)")
        step("fill pending")  # orders from earlier runs fill at their next open (owner rule)
        sh(PY + ["scripts/portfolio.py", "fill-pending", "--asof", asof, "--save", str(rundir / "fills.json")]
           + (["--dry-run"] if dry_run else []), log)
        step("mark")
        sh(PY + ["scripts/corporate_actions.py", "check", "--asof", asof], log)  # dividends/splits first (2026-10-16)
        sh(PY + ["scripts/portfolio.py", "mark", "--asof", asof], log)

        step("cash strategy")  # cash is a holding (owner rule 2026-10-09): macro regime -> cash reserve
        run_cash_strategy(asof, agent, log)

        step("scan")
        sh(PY + ["scripts/weekly_scan.py", "--asof", asof, "--out", str(rundir)], log)
        scan = json.loads((rundir / "scan.json").read_text())
        state = json.loads((port / "state.json").read_text())

        reinit = list(scan["reinitiate"])
        dip_holdings = {h["ticker"]: h for h in state.get("dip_hits") or [] if h["ticker"] in state["holdings"]}
        if scan["review"]:
            step("review")
            agent("weekly-reviewer", f"Scan file runs/{asof}/scan.json, date {asof}. "
                                     f"Write runs/{asof}/reviews.md.", log)
            rv = rundir / "reviews.md"
            if not rv.exists():
                raise StepFailed("weekly-reviewer wrote no reviews.md")
            text = rv.read_text()
            for t in scan["review"]:
                sec = text.split(f"### {t}", 1)[1].split("\n### ", 1)[0] if f"### {t}" in text else ""
                if "Action:" not in sec:
                    raise StepFailed(f"reviews.md has no Action line for {t}")
                if "ESCALATE" in sec.split("Action:", 1)[1]:
                    reinit.append(t)

        evals = []
        fvr = {f["ticker"]: f for f in scan.get("fair_value_reached", [])}
        for t in dict.fromkeys(reinit + list(dip_holdings)):
            step(f"reinitiate {t}")
            h = state["holdings"][t]
            src = ("the price reached its base fair value" if t in fvr and t in scan["reinitiate"] else
                   "core or macro trigger fired" if t in scan["reinitiate"] else
                   "escalated by weekly review" if t in reinit else "dip radar")
            why = (f"This is a full re-initiation of an existing {h['type']} holding (scan: {src}). "
                   f"Decide ADD, HOLD, TRIM or SELL.")
            if t in dip_holdings and t not in reinit:
                why = dip_holdings[t]["reason"]
            if t in fvr:
                f = fvr[t]
                why += (f" The close {f['close']} reached the base fair value {f['base']:.2f} from {f['file']}. "
                        "Owner rule: fair value is ONE model estimate, not a sell signal and not the thesis. Re-examine "
                        "whether the original thesis has played out or still has room: has the business improved so the "
                        "old fair value is stale, does the evidence (quality trend, cash returns, peers, own history) "
                        "still support holding, and is there a better use of the capital? SELL or TRIM only if the "
                        "whole evidence says the opportunity is spent; HOLD is right when the thesis is still running.")
            evals.append(("reinitiation", research_and_evaluate(t, h["type"], asof, why, agent, log, rundir)))
        if fvr and not dry_run:
            from weekly_scan import record_fv_reviews
            record_fv_reviews([f for t, f in fvr.items() if t in reinit], asof, port / "fv_reviews.json")

        cap = cfg["agents"]["max_new_initiations_per_week"] if max_new is None else max_new
        from screen import recently_researched
        days = cfg["screen"]["exclude_researched_days"]
        recent = {k: recently_researched(days, asof, k) for k in ("CORE", "TACTICAL")}  # same kind only
        picks = [p for p in screen_picks(asof) if p["ticker"] not in state["holdings"]
                 and Ticker(p["ticker"]).slug not in recent.get(p["type"], set())]
        # entry-price hits (owner rule 2026-10-09) go first and bypass the 90-day rule: the price reached the
        # level we set, so re-research whether it's now a BUY (it fell for a reason; nothing is bought blindly)
        hits = [{"ticker": h["ticker"], "type": "CORE", "entry_hit": h}
                for h in (state.get("entry_hits") or []) + (state.get("dip_hits") or [])
                if h["ticker"] not in state["holdings"]]
        hits = list({h["ticker"]: h for h in reversed(hits)}.values())[::-1]  # one per stock, first kept
        picks = hits + [p for p in picks if p["ticker"] not in {h["ticker"] for h in hits}]
        manifest["skipped"] = []

        def initiate(p):
            """A failed NEW initiation skips that stock only (owner rule); it never cancels the week."""
            try:
                step(f"initiate {p['ticker']}")
                return research_and_evaluate(p["ticker"], p["type"], asof,
                                             (entry_hit_reason(p["entry_hit"]) if p.get("entry_hit") else "New initiation from this week's screen. Decide BUY or AVOID.")
                                             + (f" Screen setup: {p['setup_detail']}." if p.get("setup_detail") else ""),
                                             agent, log, rundir)
            except Exception as e:  # noqa: BLE001
                log(f"SKIPPED initiation {p['ticker']}: {e}")
                manifest["skipped"].append({"ticker": p["ticker"], "type": p["type"], "reason": str(e)[:300]})
                discard_partial(p["ticker"], asof)  # no half-finished docs left behind
                return None

        workers = max(1, int(cfg["agents"].get("parallel_research", 1)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for p, ev in zip(picks[:cap], pool.map(initiate, picks[:cap])):
                if ev is not None:
                    evals.append(("new", ev))

        mech = rundir / "requests-mechanical.json"
        step("mechanical submit")
        sh(PY + ["scripts/portfolio.py", "submit", str(mech), "--asof", asof, "--save", str(rundir / "submit-mechanical.json")]
           + (["--dry-run"] if dry_run else []), log)  # scripted exits/trims: no model call
        if evals:
            step("portfolio-manager")
            files = " ".join(str(e.relative_to(ROOT)) for _, e in evals)
            agent("portfolio-manager",
                  f"Evaluation files: {files}. Date {asof}. Write the requests to runs/{asof}/requests-decisions.json "
                  f"and submit with --at-market --save runs/{asof}/submit.json (decided trades fill now at the live price where the market is open, else at the next open). "
                  f"Cash strategy: reports/regime/{asof}.md (new buys can't take cash below the reserve; if one would, "
                  "it must name the holding it replaces and why)." + (" This is a DRY RUN." if dry_run else ""), log)
            if not (rundir / "submit.json").exists():
                raise StepFailed("portfolio-manager did not produce submit.json")
        else:
            (rundir / "submit.json").write_text(json.dumps({"applied": [], "rejected": [], "warnings": [],
                                                            "dry_run": dry_run}))

        step("funding queue")
        try:  # 2026-10-18: a problem here trades nothing and never cancels the week
            run_funding_queue(asof, dry_run, agent, log, rundir)
        except Exception as e:  # noqa: BLE001
            log(f"!! FUNDING QUEUE STEP FAILED (no swap this week): {str(e)[:300]}")

        from decision_log import decision_from_eval
        for kind, e in evals:
            d = decision_from_eval(e.read_text())
            manifest["decisions"].append({"kind": kind, "ticker": d["ticker"], "decision": d["decision"],
                                          "conviction": d["conviction"], "rationale": d.get("rationale", ""),
                                          "evaluation": str(e.relative_to(ROOT))})
        if not dry_run:
            step("decision log")
            if evals:
                sh(PY + ["scripts/decision_log.py", "record", *[str(e.relative_to(ROOT)) for _, e in evals],
                         "--asof", asof], log)
            sh(PY + ["scripts/decision_log.py", "update", "--asof", asof], log)
            sh(PY + ["scripts/portfolio.py", "stamp", "--asof", asof], log)
        (rundir / "run.json").write_text(json.dumps(manifest, indent=1))
        step("risk")
        try:  # informational (scripts/risk.py): a problem is logged, never cancels the week
            sh(PY + ["scripts/risk.py", "report", "--asof", asof], log)
        except StepFailed as e:
            log(f"risk report not written: {e}")
        try:  # informational (scripts/attribution.py)
            sh(PY + ["scripts/attribution.py", "report", "--asof", asof], log)
        except StepFailed as e:
            log(f"attribution not written: {e}")
        step("report")
        sh(PY + ["scripts/weekly_report.py", "--asof", asof, "--run", str(rundir)], log)
        if not dry_run:
            try:  # cosmetic: a dashboard problem is logged, never cancels the week
                sh(PY + ["scripts/dashboard.py"], log)
            except StepFailed as e:
                log(f"dashboard not updated: {e}")
        if dry_run:  # a dry run never changes the portfolio
            shutil.rmtree(port)
            shutil.copytree(backup, port)
    except Exception as e:  # noqa: BLE001 - any failure aborts the whole run
        shutil.rmtree(port)
        shutil.copytree(backup, port)
        (rundir / "error.log").write_text(
            f"Weekly run {asof} FAILED at step: {manifest['steps'][-1] if manifest['steps'] else 'start'}\n"
            f"{e}\n\n{traceback.format_exc()}\nNo trades from this run were applied; portfolio/ restored.\n")
        log(f"FAILED: {e}")
        print(f"FAILED: {e} (see runs/{asof}/error.log)", file=sys.stderr)
        return 1
    finally:
        shutil.rmtree(backup, ignore_errors=True)
        logf.close()
    print(f"OK reports/weekly/{asof}.md")
    return 0


LOCK = Path("/tmp/paper-portfolio-review.lock")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-new", type=int)
    ap.add_argument("--local", action="store_true",
                    help="run on this computer even if PAUSED exists (PAUSED then only pauses GitHub)")
    a = ap.parse_args(argv)
    if (ROOT / "PAUSED").exists() and not a.local:
        print("PAUSED: exiting without changes (on your own computer, add --local to run anyway)")
        return 0
    try:
        LOCK.mkdir()  # one review at a time on this machine
    except FileExistsError:
        print(f"Another weekly review is already running (lock {LOCK}). Exiting without changes.")
        return 1
    try:
        return run(a.asof, a.dry_run, a.max_new, local=a.local)
    finally:
        LOCK.rmdir()


if __name__ == "__main__":
    sys.exit(main())
