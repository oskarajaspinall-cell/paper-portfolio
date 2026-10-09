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


BATCH_SIZE = 6
batch_lock = threading.Lock()
batch = {"done": [], "n": 0}
REPORTS = ROOT / "reports" / "research"


def batch_report(tickers: list[str], n: int) -> tuple[str, str]:
    """Plain-Python findings for a group of finished initiations (no model call). Returns (headline, markdown)."""
    import csv
    from decision_log import decision_from_eval
    from portfolio import current_reserve, totals
    rows, buys = [], []
    for t in tickers:
        slug = Ticker(t).slug
        evs = sorted((ROOT / "research" / slug).glob("*-evaluation.md"))
        if not evs:
            continue
        d = decision_from_eval(evs[-1].read_text())
        fvp = evs[-1].with_name(evs[-1].name.replace("-evaluation.md", "-valuation.json"))
        fv = json.loads(fvp.read_text()) if fvp.exists() else {}
        base, price = (fv.get("fair_value") or {}).get("base"), fv.get("price")
        fv_txt = f"{base:,.2f} vs {price:,.2f} ({(base / price - 1) * 100:+.0f}%)" if base and price else "n/m"
        order = ""
        if d["decision"] == "BUY":
            sub = run / f"submit-{slug}.json"
            if sub.exists():
                so = json.loads(sub.read_text())
                order = ("order placed: " + ", ".join(f"{p['est_shares']} sh ~{p['est_price']:.2f}" for p in so.get("placed", []))
                         or "rejected: " + "; ".join(r["rule"] for r in so.get("rejected", [])))
            else:
                order = "order NOT placed (portfolio-manager failed; retry needed)"
            buys.append(t)
        why = (d.get("rationale") or "").replace("|", "/").replace("\n", " ")
        import entry_watch
        ew = next((r for r in entry_watch.read() if r["ticker"] == t), None)
        entry = (f"{float(ew['entry_price']):,.2f} ({ew['source']})" if ew else
                 ("n/a: " + str(d.get("entry_basis"))[:80] if d.get("decision") not in ("BUY", "ADD") and "entry_price" in d else ""))
        rows.append(f"| {t} | {d['decision']} {d['conviction']} | {fv_txt} | {entry} | {why} {('**' + order + '**') if order else ''} |")
    with (ROOT / "portfolio" / "decisions.csv").open() as fh:
        decided = {r["ticker"] for r in csv.DictReader(fh)}
    uni = json.loads((run / "loop-queue.json").read_text())
    with (ROOT / "universe" / "universe.csv").open() as fh:
        sp = {r["ticker"] for r in csv.DictReader(fh) if "SP500" in r["indexes"].split(";")}
    stt = json.loads((ROOT / "portfolio" / "state.json").read_text())
    tt, res = totals(stt), current_reserve(cfg, dt.date.today().isoformat())
    head = (f"Research batch {n:02d}: {len(rows)} researched, {len(buys)} BUY"
            + (f" ({', '.join(buys)})" if buys else "") + f", {len(rows) - len(buys)} AVOID")
    md = "\n".join([f"# {head} — {dt.datetime.now():%Y-%m-%d %H:%M}", "",
                    "| Stock | Decision | Fair value (base) vs price | Entry price | Why |", "|---|---|---|---|---|", *rows, "",
                    f"S&P 500 researched: {len(decided & sp)} of {len(sp)} ({len(uni)} left in the queue). "
                    f"Portfolio ${tt['total']:,.0f}, cash {tt['cash'] / tt['total'] * 100:.1f}% vs a {res['pct']:g}% "
                    f"reserve ({res['regime']}); {tt['n']} holdings, {len(stt.get('pending', []))} order(s) pending."]) + "\n"
    return head, md


def publish(tickers: list[str], n: int) -> None:
    """Write the batch report, commit + push (updates the Mac folder and GitHub), and show a Mac banner.
    Failures are logged and never stop the research; an unpushed commit goes up with the next batch."""
    try:
        head, md = batch_report(tickers, n)
        REPORTS.mkdir(parents=True, exist_ok=True)
        path = REPORTS / f"{dt.date.today()}-batch-{n:02d}.md"
        path.write_text(md)
        paths = [str(path.relative_to(ROOT)), "portfolio", "universe/ir_domains.txt", "runs/2026-10-07-sp500"]
        paths += [str((ROOT / "research" / Ticker(t).slug).relative_to(ROOT)) for t in tickers]
        git = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)  # noqa: E731
        git("add", "--", *paths)
        c = git("commit", "-q", "-m", head + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
        p = git("pull", "-q", "--rebase", "--autostash")
        u = git("push", "-q")
        ok = u.returncode == 0 and p.returncode == 0
        log(f"== {head} -> {path.relative_to(ROOT)}; " + ("uploaded to GitHub" if ok else f"!! upload failed: {(p.stderr + u.stderr)[-200:]}"))
        subprocess.run(["osascript", "-e", f'display notification "{head.replace(chr(34), "")}" with title "Paper portfolio" '
                        f'subtitle "{"uploaded to GitHub" if ok else "saved locally; upload failed"}"'], capture_output=True)
    except Exception as e:  # noqa: BLE001
        log(f"!! batch report/upload failed: {str(e)[:300]}")


def batch_add(t: str | None, flush: bool = False) -> None:
    with batch_lock:
        if t:
            batch["done"].append(t)
        if batch["done"] and (flush or len(batch["done"]) >= BATCH_SIZE):
            batch["n"] += 1
            done, batch["done"] = batch["done"], []
            publish(done, batch["n"])


cfg = load_config()
REPORTS.mkdir(parents=True, exist_ok=True)
batch["n"] = len(list(REPORTS.glob(f"{dt.date.today()}-batch-*.md")))
st = json.loads((ROOT / "portfolio" / "state.json").read_text())
ranked = json.loads((run / "loop-queue.json").read_text())  # yesterday's S&P 500 core ranking, best first
queue = [t for t in ranked if t not in SKIP and not (ROOT / "research" / Ticker(t).slug / f"{dt.date.today()}.md").exists()
         and not list((ROOT / "research" / Ticker(t).slug).glob("*-evaluation.md"))] + sorted(SKIP)
hits = [h["ticker"] for h in st.get("entry_hits", []) if h["ticker"] not in st.get("holdings", {})]
queue = hits + [t for t in queue if t not in hits]  # entry-price hits first (owner rule 2026-10-09)
(run / "loop-queue.json").write_text(json.dumps([t for t in queue if t not in hits]))
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
        batch_add(t)
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
batch_add(None, flush=True)  # report and upload whatever finished since the last group
log("== research loop stopped" + (" (repeated failures: usage limit?)" if state["stop"] else " (queue finished)"))
