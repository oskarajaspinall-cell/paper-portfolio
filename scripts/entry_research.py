"""Re-research stocks whose price reached the entry price we set (owner rule 2026-10-09), straight away: the
intraday check (bin/entry-intraday) calls this for its hits. Full pipeline (researcher -> macro -> evaluator ->
fair value), decision log (which replaces the stock's entry-watch row), then the portfolio-manager for any BUY
(autonomous-buy rule; fills at the next open; the portfolio's rules still validate it). A hit is never a buy on
price alone: the re-initiation decides. At most [entry].intraday_max_research a day; holdings and stocks
already evaluated today are skipped.

    python scripts/entry_research.py [--asof D]     re-research the intraday hits in portfolio/state.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Ticker, load_config  # noqa: E402


def todo(state: dict, asof: str, cap: int, root: Path = ROOT) -> list[dict]:
    """Today's intraday hits still to research: not held, not evaluated today, at most `cap` (counting any
    already researched today from the intraday check)."""
    done_today = len(list((root / "runs" / f"{asof}-entry").glob("done-*")))
    out = []
    for h in state.get("entry_hits") or []:
        if not h.get("intraday") or h["ticker"] in state.get("holdings", {}):
            continue
        if (root / "research" / Ticker(h["ticker"]).slug / f"{asof}-evaluation.md").exists():
            continue
        out.append(h)
    return out[:max(0, cap - done_today)]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    cfg = load_config()
    import weekly_run as wr
    from decision_log import decision_from_eval
    state = json.loads((ROOT / "portfolio" / "state.json").read_text())
    hits = todo(state, a.asof, int(cfg["entry"].get("intraday_max_research", 3)))
    run = ROOT / "runs" / f"{a.asof}-entry"
    run.mkdir(parents=True, exist_ok=True)
    lk = threading.Lock()

    def log(msg):
        with lk, (run / "run.log").open("a") as fh:
            fh.write(f"[{dt.datetime.now():%H:%M:%S}] {msg}\n")

    def one(h):
        t = h["ticker"]
        try:
            log(f"== re-research {t} (entry price hit)")
            ev = wr.research_and_evaluate(t, "CORE", a.asof, wr.entry_hit_reason(h), wr.claude_agent, log, run)
            subprocess.run([str(ROOT / "bin" / "py"), "scripts/decision_log.py", "record", str(ev.relative_to(ROOT)),
                            "--asof", a.asof], cwd=ROOT, capture_output=True)
            (run / f"done-{Ticker(t).slug}").write_text(str(ev.relative_to(ROOT)))
            d = decision_from_eval(ev.read_text())
            log(f"== {t}: {d['decision']} {d['conviction']}")
            return t, d, ev
        except Exception as e:  # noqa: BLE001
            log(f"!! FAILED {t}: {str(e)[:300]}")
            return t, None, None

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(one, hits))
    buys = [ev for _, d, ev in results if d and d["decision"] == "BUY"]
    if buys:
        try:
            wr.claude_agent("portfolio-manager",
                            f"Evaluation files: {' '.join(str(e.relative_to(ROOT)) for e in buys)}. Date {a.asof}. "
                            f"Write the requests to runs/{a.asof}-entry/requests.json and submit with --at-next-open "
                            f"--save runs/{a.asof}-entry/submit.json (decided trades fill at the next open). "
                            f"Cash strategy: the latest reports/regime/*.md (new buys can't take cash below the reserve).", log)
        except Exception as e:  # noqa: BLE001
            log(f"!! PORTFOLIO-MANAGER FAILED (research kept): {str(e)[:300]}")
    # researched hits leave the list (their entry-watch rows were replaced by the new decisions)
    st = json.loads((ROOT / "portfolio" / "state.json").read_text())
    ok = {t for t, d, _ in results if d}
    st["entry_hits"] = [h for h in st.get("entry_hits") or [] if h["ticker"] not in ok]
    tmp = (ROOT / "portfolio" / "state.json").with_suffix(".tmp")
    tmp.write_text(json.dumps(st, indent=1, sort_keys=True))
    tmp.replace(ROOT / "portfolio" / "state.json")
    print(json.dumps({t: (f"{d['decision']} {d['conviction']}" if d else "FAILED") for t, d, _ in results}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
