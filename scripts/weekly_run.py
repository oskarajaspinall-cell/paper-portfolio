"""The weekly run, in the required order. Agent steps are separate headless Claude Code sessions
(`claude -p --agent <name>`); everything else is a script. Each agent's output is checked by a
script before the next step.

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
TOOLS = {"researcher": "Read,Write,WebFetch,Bash(bin/py:*)", "evaluator": "Read,Write,Bash(bin/py:*)",
         "portfolio-manager": "Read,Write,Bash(bin/py:*)", "weekly-reviewer": "Read,Write,WebFetch"}


class StepFailed(Exception):
    pass


AGENT_TIMEOUT = 30 * 60  # seconds; a stuck session can't hang the night


def sh(args: list[str], log, timeout: int | None = None) -> str:
    log(f"$ {' '.join(args)}")
    try:
        p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        raise StepFailed(f"{args[0]} timed out after {timeout}s") from e
    log(p.stdout.strip()[-4000:])
    if p.returncode != 0:
        raise StepFailed(f"{' '.join(args)} exited {p.returncode}: {p.stderr.strip()[-2000:]}")
    return p.stdout


def claude_agent(name: str, prompt: str, log) -> str:
    """Run one subagent as its own headless session. Replaced in tests."""
    return sh(["claude", "-p", prompt, "--agent", name, "--allowedTools", TOOLS[name], "--output-format", "text"],
              log, timeout=AGENT_TIMEOUT)


def check_doc(kind: str, path: Path, log) -> None:
    sh(PY + ["scripts/check_docs.py", kind, str(path)], log)


def research_and_evaluate(ticker: str, ptype: str, asof: str, why: str, agent, log, run: Path) -> Path:
    slug = Ticker(ticker).slug
    note, ev = ROOT / "research" / slug / f"{asof}.md", ROOT / "research" / slug / f"{asof}-evaluation.md"
    agent("researcher", f"Ticker {ticker}, note type {ptype}, date {asof}. {why}", log)
    if not note.exists():
        raise StepFailed(f"researcher wrote no note at {note}")
    check_doc("note", note, log)
    agent("evaluator", f"Evaluate {ticker} for {asof}: fact sheet research/{slug}/factsheet-{asof}.md, "
                       f"note research/{slug}/{asof}.md, state portfolio/state.json. {why}", log)
    if not ev.exists():
        raise StepFailed(f"evaluator wrote no evaluation at {ev}")
    check_doc("eval", ev, log)
    return ev


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
        step("mark")
        sh(PY + ["scripts/portfolio.py", "mark", "--asof", asof], log)

        step("scan")
        sh(PY + ["scripts/weekly_scan.py", "--asof", asof, "--out", str(rundir)], log)
        scan = json.loads((rundir / "scan.json").read_text())
        state = json.loads((port / "state.json").read_text())

        reinit = list(scan["reinitiate"])
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
        for t in dict.fromkeys(reinit):
            step(f"reinitiate {t}")
            h = state["holdings"][t]
            why = (f"This is a full re-initiation of an existing {h['type']} holding "
                   f"(scan: {'core trigger hit' if t in scan['reinitiate'] else 'escalated by weekly review'}). "
                   f"Decide ADD, HOLD, TRIM or SELL.")
            evals.append(("reinitiation", research_and_evaluate(t, h["type"], asof, why, agent, log, rundir)))

        cap = cfg["agents"]["max_new_initiations_per_week"] if max_new is None else max_new
        from screen import recently_researched
        recent = recently_researched(cfg["screen"]["exclude_researched_days"], asof)
        picks = [p for p in screen_picks(asof) if p["ticker"] not in state["holdings"]
                 and Ticker(p["ticker"]).slug not in recent]
        manifest["skipped"] = []

        def initiate(p):
            """A failed NEW initiation skips that stock only (owner rule); it never cancels the week."""
            try:
                step(f"initiate {p['ticker']}")
                return research_and_evaluate(p["ticker"], p["type"], asof,
                                             "New initiation from this week's screen. Decide BUY or AVOID.",
                                             agent, log, rundir)
            except Exception as e:  # noqa: BLE001
                log(f"SKIPPED initiation {p['ticker']}: {e}")
                manifest["skipped"].append({"ticker": p["ticker"], "type": p["type"], "reason": str(e)[:300]})
                slug = Ticker(p["ticker"]).slug
                for f in (ROOT / "research" / slug).glob(f"{asof}*.md"):  # no half-finished docs left behind
                    f.unlink()
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
                  f"and submit with --save runs/{asof}/submit.json." + (" This is a DRY RUN." if dry_run else ""), log)
            if not (rundir / "submit.json").exists():
                raise StepFailed("portfolio-manager did not produce submit.json")
        else:
            (rundir / "submit.json").write_text(json.dumps({"applied": [], "rejected": [], "warnings": [],
                                                            "dry_run": dry_run}))

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
