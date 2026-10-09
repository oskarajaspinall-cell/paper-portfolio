"""Ad-hoc owner-requested initiations: full research (researcher -> macro -> evaluator -> fair value -> Monte
Carlo), decision log, then the portfolio-manager for any BUY (owner rule: buys happen autonomously; the
portfolio's rules still validate them). Usage: research.py TYPE TICKER [TICKER ...]   (TYPE = CORE|TACTICAL)"""
import datetime as dt
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path.home() / "paper-portfolio"
sys.path.insert(0, str(ROOT / "scripts"))
import weekly_run as wr  # noqa: E402
from decision_log import decision_from_eval  # noqa: E402

asof = dt.date.today().isoformat()
run = ROOT / "runs" / f"{asof}-adhoc"
run.mkdir(parents=True, exist_ok=True)
ptype, tickers = sys.argv[1], sys.argv[2:]
lk = threading.Lock()


def log(msg):
    with lk, (run / "run.log").open("a") as fh:
        fh.write(f"[{dt.datetime.now():%H:%M:%S}] {msg}\n")


def one(t):
    try:
        log(f"== initiate {t} ({ptype})")
        ev = wr.research_and_evaluate(t, ptype, asof, "Owner-requested initiation. Decide BUY or AVOID.",
                                      wr.claude_agent, log, run)
        subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", str(ev.relative_to(ROOT)),
                        "--asof", asof], cwd=ROOT, capture_output=True)
        d = decision_from_eval(ev.read_text())
        log(f"== {t}: {d['decision']} {d['conviction']}")
        return t, d, ev
    except Exception as e:  # noqa: BLE001
        log(f"!! FAILED {t}: {str(e)[:300]}")
        return t, None, None


with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(one, tickers))
buys = [ev for _, d, ev in results if d and d["decision"] == "BUY"]
if buys:
    wr.claude_agent("portfolio-manager", f"Evaluation files: {' '.join(str(e.relative_to(ROOT)) for e in buys)}. Date {asof}. "
                    f"Write the requests to runs/{asof}-adhoc/requests.json and submit with --at-market "
                    f"--save runs/{asof}-adhoc/submit.json (decided trades fill now at the live price where the market is open, else at the next open).", log)
log("== finished")
for t, d, _ in results:
    print(t, "FAILED" if not d else f"{d['decision']} {d['conviction']} | {d.get('rationale', '')}", flush=True)
