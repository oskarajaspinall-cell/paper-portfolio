"""Claude Code PreToolUse hook for WebFetch: enforce the qualitative-source allowlist.

Allowed: the `allowlist` in CLAUDE.md's config block, each `ir=` domain in universe/watchlist.txt,
and company domains recorded in universe/ir_domains.txt, including their subdomains. Anything else is blocked (exit 2,
reason sent back to the agent) and the skipped URL is logged to logs/skipped-urls.log.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, allowed_domains  # noqa: E402

LOG = ROOT / "logs" / "skipped-urls.log"


def is_allowed(url: str, domains: set[str]) -> bool:
    p = urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        return False
    host = p.hostname.lower()
    return any(host == d or host.endswith("." + d) for d in domains)


def main() -> int:
    event = json.load(sys.stdin)
    url = (event.get("tool_input") or {}).get("url", "")
    if is_allowed(url, allowed_domains()):
        return 0
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as fh:
        fh.write(f"{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}\tSKIPPED\t{url}\n")
    print(f"Blocked: {url} is not on the allowlist (CLAUDE.md config + watchlist IR domains). "
          "Skip this source and continue; it has been logged.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
