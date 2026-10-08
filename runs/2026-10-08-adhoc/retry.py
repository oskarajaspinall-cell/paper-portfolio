import datetime as dt, subprocess, sys
from pathlib import Path
ROOT = Path.home() / "paper-portfolio"
sys.path.insert(0, str(ROOT / "scripts"))
import weekly_run as wr
from decision_log import decision_from_eval
asof = dt.date.today().isoformat(); run = ROOT / "runs" / f"{asof}-adhoc"
def log(m):
    with (run / "run.log").open("a") as fh: fh.write(f"[{dt.datetime.now():%H:%M:%S}] {m}\n")
for t in ("ONDS", "GRAB"):
    log(f"== Monte Carlo retry {t}"); wr.run_montecarlo(t, t, asof, wr.claude_agent, log, run)
log("== retry initiate HIMS")
try:
    ev = wr.research_and_evaluate("HIMS", "CORE", asof, "Owner-requested initiation. Decide BUY or AVOID.", wr.claude_agent, log, run)
    subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", str(ev.relative_to(ROOT)), "--asof", asof], cwd=ROOT)
    d = decision_from_eval(ev.read_text())
    if d["decision"] == "BUY":
        wr.claude_agent("portfolio-manager", f"Evaluation files: {ev.relative_to(ROOT)}. Date {asof}. Write the requests to "
                        f"runs/{asof}-adhoc/requests-hims.json and submit with --at-next-open --save runs/{asof}-adhoc/submit-hims.json "
                        "(decided trades fill at the next open).", log)
    print("HIMS", d["decision"], d["conviction"], "|", d.get("rationale", ""))
except Exception as e:
    log(f"!! FAILED HIMS: {e}"); print("HIMS FAILED", str(e)[:300])
