"""Full global core ranking (owner 2026-10-12: move the loop from the low end of the S&P 500 to the top of the
global universe). Re-runs scripts/screen.py on Friday's page cache (2026-10-10, prices as of the 2026-10-09
close); names with a core decision in the last 90 days are excluded. Writes loop-queue.json, best first."""
import json
import sys
from pathlib import Path

ROOT = Path.home() / "paper-portfolio"
sys.path.insert(0, str(ROOT / "scripts"))
import screen  # noqa: E402
from common import load_config  # noqa: E402
from fetch_data import Fetcher  # noqa: E402

cfg = load_config()
state = json.loads((ROOT / "portfolio" / "state.json").read_text())
res = screen.run(Fetcher(today="2026-10-10"), cfg, "2026-10-12", state=state)
ranked = sorted((r for r in res["rows"] if r["core"] is not None), key=screen.core_rank_key, reverse=True)
run = ROOT / "runs" / "2026-10-12-global"
(run / "loop-queue.json").write_text(json.dumps([r["ticker"] for r in ranked]))
(run / "ranking.json").write_text(json.dumps([{"ticker": r["ticker"], "name": res["names"].get(r["ticker"], ""),
                                               "core": r["core"], "core_deep": r.get("core_deep")} for r in ranked], indent=0))
print("screened", res["screened"], "failed", len(res["failed"]), "ranked", len(ranked), "deep", res["deep_dived"])
print([r["ticker"] for r in ranked[:30]])
