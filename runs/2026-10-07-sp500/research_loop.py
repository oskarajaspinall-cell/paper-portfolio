"""Keep researching the S&P 500 screen's core ranking (best first), 3 at a time, until the usage limit
(or anything else) makes `stop_after` initiations in a row fail. The portfolio-manager runs only for BUYs (owner rule 2026-10-08: buys happen autonomously; the portfolio's rules still validate
them). Each finished evaluation is recorded in the decision log. Usage: research_loop.py"""
import datetime as dt
import json
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path.home() / "paper-portfolio"
sys.path.insert(0, str(ROOT / "scripts"))
import screen  # noqa: E402
import weekly_run as wr  # noqa: E402
from common import Ticker, load_config  # noqa: E402
from fetch_data import Fetcher  # noqa: E402

SKIP = {"APA", "UHS", "LDOS"}  # failed when the usage limit hit; retried at the end of the queue
stop_after = 3
run = ROOT / "runs" / "2026-10-07-sp500"
lk = threading.Lock()
pm_lock = threading.Lock()  # one portfolio-manager session at a time: they share portfolio/state.json
state = {"fails_in_row": 0, "stop": False}


def log(msg):
    with lk, (run / "run.log").open("a") as fh:
        fh.write(f"[{dt.datetime.now():%H:%M:%S}] {msg}\n")


cfg = load_config()
st = json.loads((ROOT / "portfolio" / "state.json").read_text())
ranked = json.loads((run / "loop-queue.json").read_text())  # yesterday's S&P 500 core ranking, best first
queue = [t for t in ranked if t not in SKIP and not (ROOT / "research" / Ticker(t).slug / f"{dt.date.today()}.md").exists()
         and not list((ROOT / "research" / Ticker(t).slug).glob("*-evaluation.md"))] + sorted(SKIP)
(run / "loop-queue.json").write_text(json.dumps(queue))
log(f"== research loop: {len(queue)} names queued, best first: {queue[:10]}")


WEEKLY_LOCK = Path("/tmp/paper-portfolio-review.lock")


def weekly_run_near() -> bool:
    """Leave the machine to the Friday 22:00 weekly run: stop from 21:15 on Fridays or while its lock exists."""
    now = dt.datetime.now()
    return WEEKLY_LOCK.exists() or (now.weekday() == 4 and (now.hour, now.minute) >= (21, 15))


def one(t):
    if state["stop"] or weekly_run_near():
        if not state["stop"]:
            state["stop"] = True
            log("== research loop pausing for the weekly run")
        return t, "not started"
    asof = dt.date.today().isoformat()
    try:
        log(f"== initiate {t}")
        ev = wr.research_and_evaluate(t, "CORE", asof, "New initiation from the S&P 500 screen. Decide BUY or AVOID.",
                                      wr.claude_agent, log, run)
        subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", str(ev.relative_to(ROOT)),
                        "--asof", asof], cwd=ROOT, capture_output=True)
        with lk:
            state["fails_in_row"] = 0
        from decision_log import decision_from_eval
        d = decision_from_eval(ev.read_text())
        if d["decision"] == "BUY":
            try:
                with pm_lock:
                    log(f"== portfolio-manager {t} (BUY {d['conviction']})")
                    wr.claude_agent("portfolio-manager",
                                    f"Evaluation files: {ev.relative_to(ROOT)}. Date {asof}. Write the requests to "
                                    f"runs/2026-10-07-sp500/requests-{Ticker(t).slug}.json and submit with --at-next-open "
                                    f"--save runs/2026-10-07-sp500/submit-{Ticker(t).slug}.json (decided trades fill at the next open).", log)
            except Exception as e:  # noqa: BLE001  research stands; the order step is reported, not retried
                log(f"!! PORTFOLIO-MANAGER FAILED for {t} (research kept): {str(e)[:300]}")
        log(f"== done {t}")
        return t, str(ev.relative_to(ROOT))
    except Exception as e:  # noqa: BLE001
        for f in (ROOT / "research" / Ticker(t).slug).glob(f"{asof}*"):  # no half-finished docs
            f.unlink()
        with lk:
            state["fails_in_row"] += 1
            if state["fails_in_row"] >= stop_after:
                state["stop"] = True
        log(f"!! FAILED {t}: {str(e)[:300]}")
        return t, "FAILED"


def mc_retry(t):  # evaluations that finished but whose Monte Carlo stalled (Mac slept overnight)
    slug = Ticker(t).slug
    for ev in sorted((ROOT / "research" / slug).glob("*-evaluation.md")):
        asof = ev.name[:10]
        if not (ROOT / "research" / slug / f"{asof}-montecarlo.json").exists() and \
                not (ROOT / "research" / slug / f"{asof}-mc-needs-review.md").exists():
            log(f"== Monte Carlo retry {t} {asof}")
            wr.run_montecarlo(t, slug, asof, wr.claude_agent, log, run)


with ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(mc_retry, ["TPR", "EOG", "PNR"]))

with ThreadPoolExecutor(max_workers=3) as pool:
    for t, r in pool.map(one, queue):
        if r != "not started":
            print(t, r, flush=True)
log("== research loop stopped" + (" (repeated failures: usage limit?)" if state["stop"] else " (queue finished)"))
