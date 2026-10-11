"""Make-up for the 2026-10-11 weekly run: its 15 screen initiations were skipped when the usage limit hit
(23:25). Same steps as weekly_run.run: research_and_evaluate with the screen's instructions, decision log,
one portfolio-manager pass (--at-market: markets closed -> next open), then the macro view that also missed.
Resumable: evaluations already written today are kept, not redone. MOEX:MTSS is left out (the researcher
could not produce a note for it on the first attempt).

    bin/py runs/2026-10-11/makeup.py
"""
import datetime as dt
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path.home() / "paper-portfolio"
sys.path.insert(0, str(ROOT / "scripts"))
import weekly_run as wr  # noqa: E402
from common import Ticker  # noqa: E402

asof = "2026-10-11"
run = ROOT / "runs" / asof


def log(m):
    with (run / "run.log").open("a") as fh:
        fh.write(f"[{dt.datetime.now():%H:%M:%S}] {m}\n")


def evaluation(t):
    return ROOT / "research" / Ticker(t).slug / f"{asof}-evaluation.md"


skipped = {s["ticker"] for s in json.loads((run / "run.json").read_text())["skipped"]}
picks = [p for p in wr.screen_picks(asof) if p["ticker"] in skipped and p["ticker"] != "MOEX:MTSS"]
done = [evaluation(p["ticker"]) for p in picks if evaluation(p["ticker"]).exists()]
todo = [p for p in picks if not evaluation(p["ticker"]).exists()]
log(f"== MAKE-UP resumed: {len(done)} already evaluated, {len(todo)} to go {[p['ticker'] for p in todo]}")


def one(p):
    try:
        return wr.research_and_evaluate(
            p["ticker"], p["type"], asof, "New initiation from this week's screen. Decide BUY or AVOID."
            + (f" Screen setup: {p['setup_detail']}." if p.get("setup_detail") else ""), wr.claude_agent, log, run)
    except Exception as e:  # noqa: BLE001
        log(f"SKIPPED initiation {p['ticker']} (make-up): {str(e)[:300]}")
        for f in (ROOT / "research" / Ticker(p["ticker"]).slug).glob(f"{asof}*.md"):
            f.unlink()
        return None


with ThreadPoolExecutor(3) as pool:
    evals = done + [e for e in pool.map(one, todo) if e]
if evals:
    rel = [str(e.relative_to(ROOT)) for e in evals]
    subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", *rel, "--asof", asof], cwd=ROOT)
    try:
        wr.claude_agent("portfolio-manager", f"Evaluation files: {' '.join(rel)}. Date {asof}. Write the requests to "
                        f"runs/{asof}/requests-makeup.json and submit with --at-market --save runs/{asof}/submit-makeup.json "
                        "(decided trades fill now at the live price where the market is open, else at the next open). "
                        f"Cash strategy: reports/regime/{asof}.md (new buys can't take cash below the reserve; if one would, "
                        "it must name the holding it replaces and why).", log)
    except Exception as e:  # noqa: BLE001
        log(f"!! PORTFOLIO-MANAGER FAILED (make-up; research kept): {str(e)[:300]}")
wr.run_cash_strategy(asof, wr.claude_agent, log)  # the macro view that also missed the limit
log(f"== MAKE-UP finished: {len(evals)} of {len(picks)} evaluated")
