"""Bulk core research loop (no fixed schedule; started by hand with bin/research-loop). Works through a ranked queue
(`<run>/loop-queue.json`, best first), 3 stocks at a time: the free pre-screen (scripts/prescreen.py) first, then
researcher -> macro-overlay -> evaluator, the decision log, and the portfolio-manager for any BUY (owner rule
2026-10-08: buys happen autonomously; the portfolio's rules still validate them, and the funding queue keeps a BUY
the cash reserve blocks). Entry-price and dip-radar hits go first. Every 6 finished stocks a batch report
(reports/research/<date>-batch-NN.md) is committed and pushed. It stops when the queue is done or `stop_after`
stocks in a row fail (usually the usage limit); a network outage is waited out, not counted (owner request
2026-10-09). It leaves the machine to the Friday weekly run. Run it again to continue where it stopped.

    bin/py scripts/research_loop.py rank runs/<name> [--cache-date YYYY-MM-DD]   build the queue: the global core
                                                       ranking (scripts/screen.py on that day's page cache)
    bin/research-loop runs/<name>                      start the loop detached (log: runs/<name>/run.log)
"""
import datetime as dt
import json
import socket
import subprocess
import time
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
import prescreen  # noqa: E402

stop_after = 3
run: Path = ROOT / "runs"  # the run folder, set by main()
lk = threading.Lock()
pm_lock = threading.Lock()  # one portfolio-manager session at a time: they share portfolio/state.json
state = {"fails_in_row": 0, "stop": False, "screened": 0}


def log(msg):
    with lk, (run / "run.log").open("a") as fh:
        fh.write(f"[{dt.datetime.now():%H:%M:%S}] {msg}\n")


NET_HOST, NET_POLL_S, NET_MAX_WAIT_S, NET_RETRIES = "api.anthropic.com", 60, 6 * 3600, 3
net_lock = threading.Lock()


def online() -> bool:
    try:
        socket.create_connection((NET_HOST, 443), timeout=10).close()
        return True
    except OSError:
        return False


def wait_online() -> bool:
    """Block until the API host is reachable (one waiter logs; the others share it). False if it never came
    back within NET_MAX_WAIT_S or the weekly run needs the machine."""
    with net_lock:
        if online():
            return True
        log(f"== network down ({NET_HOST} unreachable): waiting, checking every {NET_POLL_S}s")
        t0 = time.monotonic()
        while time.monotonic() - t0 < NET_MAX_WAIT_S:
            if weekly_run_near():
                return False
            time.sleep(NET_POLL_S)
            if online():
                log(f"== network back after {int(time.monotonic() - t0) // 60} min; retrying")
                return True
        log("!! network still down after the maximum wait")
        return False


def agent(name, prompt, log_):
    """wr.claude_agent, but a failure while the network is down waits for it and retries the same step."""
    for i in range(NET_RETRIES + 1):
        try:
            return wr.claude_agent(name, prompt, log_)
        except Exception:  # noqa: BLE001
            if i == NET_RETRIES or online() or not wait_online():
                raise


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
        sp = {r["ticker"] for r in csv.DictReader(fh)}
    stt = json.loads((ROOT / "portfolio" / "state.json").read_text())
    tt, res = totals(stt), current_reserve(cfg, dt.date.today().isoformat())
    head = (f"Research batch {n:02d}: {len(rows)} researched, {len(buys)} BUY"
            + (f" ({', '.join(buys)})" if buys else "") + f", {len(rows) - len(buys)} AVOID")
    md = "\n".join([f"# {head} — {dt.datetime.now():%Y-%m-%d %H:%M}", "",
                    "| Stock | Decision | Fair value (base) vs price | Entry price | Why |", "|---|---|---|---|---|", *rows, "",
                    f"Global universe researched: {len(decided & sp)} of {len(sp)} ({len([u for u in uni if u not in decided])} left in this queue); "
                    f"{state['screened']} skipped by the pre-screen this session (price above base fair value; "
                    f"reports/prescreen/). "
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
        subprocess.run([str(ROOT / "bin" / "py"), "scripts/dashboard.py"], cwd=ROOT, capture_output=True)  # keep GitHub current
        paths = [str(path.relative_to(ROOT)), "portfolio", "docs", "universe/ir_domains.txt", str(run.relative_to(ROOT)), "reports/prescreen"]
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
hits: list[str] = []
hit_rows: dict[str, dict] = {}


def build_queue() -> list[str]:
    """The ranked queue minus stocks already evaluated (or noted today), entry-price and dip-radar hits first."""
    global hits, hit_rows
    st = json.loads((ROOT / "portfolio" / "state.json").read_text())
    ranked = json.loads((run / "loop-queue.json").read_text())
    queue = [t for t in ranked if not (ROOT / "research" / Ticker(t).slug / f"{dt.date.today()}.md").exists()
             and not list((ROOT / "research" / Ticker(t).slug).glob("*-evaluation.md"))]
    hit_rows = {h["ticker"]: h for h in reversed((st.get("entry_hits") or []) + (st.get("dip_hits") or []))
                if h["ticker"] not in st.get("holdings", {})}  # entry-price and dip-radar hits (2026-10-19)
    hits = list(hit_rows)
    queue = hits + [t for t in queue if t not in hits]
    (run / "loop-queue.json").write_text(json.dumps([t for t in queue if t not in hits]))
    return queue


WEEKLY_LOCK = Path("/tmp/paper-portfolio-review.lock")


def weekly_run_near() -> bool:
    """Leave the machine to the Friday 22:00 weekly run: stop from 21:15 on Fridays, or while its lock exists
    over the weekend. On other days the lock is the weekday 21:30 fills job (about a minute): wait it out
    rather than stop (it stopped the loop every weekday night before 2026-10-12)."""
    now = dt.datetime.now()
    if (now.weekday() == 4 and (now.hour, now.minute) >= (21, 15)) or (WEEKLY_LOCK.exists() and now.weekday() >= 5):
        return True
    t0 = time.monotonic()
    while WEEKLY_LOCK.exists():
        if time.monotonic() - t0 > 30 * 60:
            return True  # held far longer than a fills run: something else owns the repo
        time.sleep(15)
    return False


def one(t):
    for _ in range(NET_RETRIES):
        t, r = attempt(t)
        if r != "NETWORK":
            return t, r
        if not wait_online():
            break
    with lk:  # gave up waiting for the network: count it like any other failure
        state["fails_in_row"] += 1
        if state["fails_in_row"] >= stop_after:
            state["stop"] = True
    return t, "FAILED"


def attempt(t):
    if state["stop"] or weekly_run_near():
        if not state["stop"]:
            state["stop"] = True
            log("== research loop pausing for the weekly run")
        return t, "not started"
    asof = dt.date.today().isoformat()
    if t not in hits:  # owner 2026-10-12: a free mechanical gate first; entry-price hits are never gated
        try:
            row = prescreen.check(t, asof, Fetcher(), cfg)
            prescreen.record(row)
        except Exception as e:  # noqa: BLE001  the gate can only skip work, never block it
            row = {"verdict": "PASS", "reason": f"pre-screen error ({str(e)[:120]}): researched"}
        if row["verdict"] == "SKIP":
            log(f"== screened out {t}: {row['reason']} (no AI research)")
            with lk:
                state["screened"] += 1
            return t, "SCREENED"
    try:
        log(f"== initiate {t}")
        why = (wr.entry_hit_reason(hit_rows[t]) if t in hit_rows else
               "New initiation from the global core screen. Decide BUY or AVOID.")
        ev = wr.research_and_evaluate(t, "CORE", asof, why, agent, log, run)
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
                    agent("portfolio-manager",
                                    f"Evaluation files: {ev.relative_to(ROOT)}. Date {asof}. Write the requests to "
                                    f"{run.relative_to(ROOT)}/requests-{Ticker(t).slug}.json and submit with --at-market "
                                    f"--save {run.relative_to(ROOT)}/submit-{Ticker(t).slug}.json (decided trades fill now at the live price where the market is open, else at the next open).", log)
            except Exception as e:  # noqa: BLE001  research stands; the order step is reported, not retried
                log(f"!! PORTFOLIO-MANAGER FAILED for {t} (research kept): {str(e)[:300]}")
        log(f"== done {t}")
        batch_add(t)
        return t, str(ev.relative_to(ROOT))
    except Exception as e:  # noqa: BLE001
        wr.discard_partial(t, asof)  # no half-finished docs
        if not online():  # an outage (e.g. a data fetch failed offline), not the stock: retried, not counted
            log(f"!! {t} interrupted by a network outage: {str(e)[:200]}")
            return t, "NETWORK"
        with lk:
            state["fails_in_row"] += 1
            if state["fails_in_row"] >= stop_after:
                state["stop"] = True
        log(f"!! FAILED {t}: {str(e)[:300]}")
        return t, "FAILED"


def rank(run_dir: Path, cache_date: str) -> None:
    """The global core ranking on that day's page cache; names with a core decision in the last 90 days excluded."""
    state_ = json.loads((ROOT / "portfolio" / "state.json").read_text())
    res = screen.run(Fetcher(today=cache_date), cfg, dt.date.today().isoformat(), state=state_)
    ranked = sorted((r for r in res["rows"] if r["core"] is not None), key=screen.core_rank_key, reverse=True)
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "loop-queue.json").write_text(json.dumps([r["ticker"] for r in ranked]))
    (run_dir / "ranking.json").write_text(json.dumps([{"ticker": r["ticker"], "name": res["names"].get(r["ticker"], ""),
                                                        "core": r["core"], "core_deep": r.get("core_deep")}
                                                       for r in ranked], indent=0))
    print("screened", res["screened"], "failed", len(res["failed"]), "ranked", len(ranked))


def main(argv=None) -> int:
    import argparse
    global run
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rank"])
    ap.add_argument("run_dir", help="runs/<name>")
    ap.add_argument("--cache-date", default=dt.date.today().isoformat(), help="rank: the page-cache day to screen")
    a = ap.parse_args(argv)
    run = (ROOT / a.run_dir).resolve()
    if a.cmd == "rank":
        rank(run, a.cache_date)
        return 0
    REPORTS.mkdir(parents=True, exist_ok=True)
    batch["n"] = len(list(REPORTS.glob(f"{dt.date.today()}-batch-*.md")))
    queue = build_queue()
    log(f"== research loop: {len(queue)} names queued, best first: {queue[:10]}")
    with ThreadPoolExecutor(max_workers=3) as pool:
        for t, r in pool.map(one, queue):
            if r != "not started":
                print(t, r, flush=True)
    batch_add(None, flush=True)  # report and upload whatever finished since the last group
    log(f"== pre-screen: {state['screened']} names skipped without AI research (reports/prescreen/)")
    log("== research loop stopped" + (" (repeated failures: usage limit?)" if state["stop"] else " (queue finished)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
