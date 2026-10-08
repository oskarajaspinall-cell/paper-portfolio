"""Trial of the new tactical setups (owner rule 2026-10-08): full initiation of the best drift and best
pullback candidate from the S&P 500 screen, then the portfolio-manager for any BUY. Usage: tactical_trial.py"""
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
from decision_log import decision_from_eval  # noqa: E402
from fetch_data import Fetcher  # noqa: E402

run = ROOT / "runs" / "2026-10-07-sp500"
lk = threading.Lock()


def log(msg):
    with lk, (run / "tactical-trial.log").open("a") as fh:
        fh.write(f"[{dt.datetime.now():%H:%M:%S}] {msg}\n")


cfg = load_config()
asof = dt.date.today().isoformat()
state = json.loads((ROOT / "portfolio" / "state.json").read_text())
res = screen.run(Fetcher(cfg), cfg, asof, state=state, index="SP500")  # today's pages (cached after the first run)
picks = []
for k in ("drift", "pullback"):
    best = sorted((r for r in res["rows"] if r["setup"] == k), key=lambda r: -r["tactical"])
    if best:
        picks.append((best[0]["ticker"], best[0]["setup_detail"]))
log(f"== tactical trial picks: {picks}")


def one(p):
    t, detail = p
    try:
        ev = wr.research_and_evaluate(t, "TACTICAL", asof, "New tactical initiation from the S&P 500 screen. Decide BUY "
                                      f"or AVOID. Screen setup: {detail}.", wr.claude_agent, log, run)
        subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", str(ev.relative_to(ROOT)),
                        "--asof", asof], cwd=ROOT, capture_output=True)
        d = decision_from_eval(ev.read_text())
        log(f"== {t}: {d['decision']} {d['conviction']} | exit_plan {d.get('exit_plan')}")
        return t, d, ev
    except Exception as e:  # noqa: BLE001
        log(f"!! FAILED {t}: {str(e)[:300]}")
        return t, None, None


with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(one, picks))
buys = [ev for t, d, ev in results if d and d["decision"] == "BUY"]
if buys:
    wr.claude_agent("portfolio-manager", f"Evaluation files: {' '.join(str(e.relative_to(ROOT)) for e in buys)}. Date {asof}. "
                    "Write the requests to runs/2026-10-07-sp500/requests-tactical-trial.json and submit with --at-next-open "
                    "--save runs/2026-10-07-sp500/submit-tactical-trial.json (decided trades fill at the next open).", log)
log("== tactical trial finished")
print(json.dumps([(t, d and {k: d.get(k) for k in ("decision", "conviction", "exit_plan", "rationale")}) for t, d, _ in results], indent=1))
