"""SEC filing delta: what changed in Risk Factors and MD&A since the comparable filing. No model calls.

Design by Claude 2026-10-16. For a US SEC filer, the latest 10-K or 10-Q is compared with its comparable:
    10-K -> the previous 10-K                       (Item 1A Risk Factors, Item 7 MD&A)
    10-Q -> the same fiscal quarter a year earlier  (Part II Item 1A Risk Factors, Part I Item 2 MD&A)
(a 10-Q's risk factors are usually "no material change from the 10-K", and quarter-on-quarter MD&A mostly
differs by season). The sections are split into paragraphs and diffed (difflib); paragraphs that differ only
in their numbers or dates (routine figure updates), whitespace or position are dropped. What is left -- added,
removed and reworded paragraphs, Risk Factors first -- goes to research/<SLUG>/sec-delta-<date>.md, capped at
[sec].max_words, each block citing its filing URL. The researcher reads it before any web fetch.
Numbers inside filings are context, never data (the stockanalysis.com-only rule is unchanged).

sec.gov asks automated clients to name a contact in the User-Agent (its fair-access policy). The step is
OFF until the owner sets [sec].contact in CLAUDE.md. Requests: sec.gov's robots.txt, >= [data]
request_interval_seconds apart, cached per day in data/cache/<date>/sec/.

Usage:
    python scripts/sec_delta.py TICKER [--asof YYYY-MM-DD]
Exit 0 with the output path, or 0 with "SKIP <reason>" (not a US filer, step off, no comparable filing).
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import sys
import time
import urllib.request
import urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

CACHE = ROOT / "data" / "cache"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SECTIONS = {
    "10-K": [("Risk Factors", r"item\s*1a\.?\W*risk\s+factors"), ("MD&A", r"item\s*7\.?\W*management.s\s+discussion")],
    "10-Q": [("Risk Factors", r"item\s*1a\.?\W*risk\s+factors"), ("MD&A", r"item\s*2\.?\W*management.s\s+discussion")],
}
ITEM = r"(part\s+[iv]+\W*)?item\s*\d+[a-z]?\b"  # any item heading ends a section
MAX_HEADING_CHARS = 150
MIN_PARA_CHARS = 60


# --------------------------------------------------------------------------- fetching
class SecFetcher:
    def __init__(self, cfg: dict, today: str | None = None):
        contact = (cfg.get("sec") or {}).get("contact", "").strip()
        if not contact:
            raise DataError("https://www.sec.gov/", "contact", "[sec].contact is not set")
        self.ua = f"{cfg['data']['user_agent']} contact: {contact}"
        self.interval = float(cfg["data"]["request_interval_seconds"])
        self.dir = CACHE / (today or dt.date.today().isoformat()) / "sec"
        self._robots, self._last = None, 0.0

    def _get(self, url: str) -> str:
        wait = self.interval - (time.time() - self._last)
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers={"User-Agent": self.ua, "Accept-Encoding": "identity"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                text = r.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001 - any network failure is a DataError naming the URL
            raise DataError(url, "fetch", str(e)) from e
        finally:
            self._last = time.time()
        return text

    def get(self, url: str) -> str:
        cached = self.dir / re.sub(r"[^\w.-]+", "_", url.split("://", 1)[1])
        if cached.exists():
            return cached.read_text()
        if self._robots is None:
            self._robots = urllib.robotparser.RobotFileParser()
            self._robots.parse(self._get("https://www.sec.gov/robots.txt").splitlines())
        if not self._robots.can_fetch(self.ua, url):
            raise DataError(url, "robots.txt", "path disallowed by sec.gov robots.txt")
        text = self._get(url)
        cached.parent.mkdir(parents=True, exist_ok=True)
        cached.write_text(text)
        return text


def cik_for(fetcher, ticker: str) -> int | None:
    sym = Ticker(ticker).symbol.upper().replace(".", "-")
    for row in json.loads(fetcher.get(TICKERS_URL)).values():
        if str(row.get("ticker", "")).upper() == sym:
            return int(row["cik_str"])
    return None


def pick_filings(recent: dict) -> tuple[dict, dict] | None:
    """(latest, comparable) from a submissions JSON's filings.recent columns."""
    rows = [dict(zip(recent, vals)) for vals in zip(*recent.values())]
    rows = sorted((r for r in rows if r.get("form") in SECTIONS and r.get("reportDate")),
                  key=lambda r: r["filingDate"], reverse=True)
    if not rows:
        return None
    latest = rows[0]
    same = [r for r in rows[1:] if r["form"] == latest["form"]]
    if latest["form"] == "10-K":
        return (latest, same[0]) if same else None
    want = dt.date.fromisoformat(latest["reportDate"]) - dt.timedelta(days=365)
    near = [r for r in same if abs((dt.date.fromisoformat(r["reportDate"]) - want).days) <= 45]
    return (latest, near[0]) if near else None


def doc_url(cik: int, f: dict) -> str:
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accessionNumber'].replace('-', '')}/{f['primaryDocument']}"


# --------------------------------------------------------------------------- text
class _Text(HTMLParser):
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def lines(doc: str) -> list[str]:
    p = _Text()
    p.feed(doc)
    text = "".join(p.parts).replace("\xa0", " ")
    out: list[str] = []
    for ln in (re.sub(r"\s+", " ", x).strip() for x in text.split("\n")):
        if not ln:
            continue
        if out and re.fullmatch(ITEM + r"\.?", out[-1], re.I):  # "ITEM 1A." with its title on the next line
            out[-1] += " " + ln
        else:
            out.append(ln)
    return out


def _heading(ln: str, pattern: str) -> bool:
    return len(ln) <= MAX_HEADING_CHARS and bool(re.match(pattern, ln, re.I))


def section(ls: list[str], start: str) -> list[str]:
    """The longest run from a heading matching `start` to the next item heading (the table of contents
    lists the same headings, but its runs are empty)."""
    best: list[str] = []
    for i, ln in enumerate(ls):
        if _heading(ln, start):
            j = next((k for k in range(i + 1, len(ls)) if _heading(ls[k], ITEM)), len(ls))
            if sum(map(len, ls[i + 1:j])) > sum(map(len, best)):
                best = ls[i + 1:j]
    return [x for x in best if len(x) >= MIN_PARA_CHARS]


def _norm(p: str) -> str:
    return re.sub(r"\s+", " ", p.lower()).strip()


def _masked(p: str) -> str:
    """Paragraph with numbers, dates and years masked: equal masks = only figures changed."""
    t = re.sub(r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\b", "#", _norm(p))
    return re.sub(r"[$€£]?\d[\d,.]*%?", "#", t)


def diff(old: list[str], new: list[str]) -> dict[str, list]:
    """Added / removed / changed paragraphs, ignoring figure-only edits and moved paragraphs."""
    a, b = [_masked(x) for x in old], [_masked(x) for x in new]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    added, removed, changed = [], [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        olds, news = list(range(i1, i2)), list(range(j1, j2))
        if op == "replace":  # pair up rewordings of the same paragraph
            for i in list(olds):
                best = max(news, key=lambda j: difflib.SequenceMatcher(a=a[i], b=b[j]).ratio(), default=None)
                if best is not None and difflib.SequenceMatcher(a=a[i], b=b[best]).ratio() >= 0.6:
                    changed.append((old[i], new[best]))
                    olds.remove(i)
                    news.remove(best)
        removed += [old[i] for i in olds]
        added += [new[j] for j in news]
    moved = {_masked(x) for x in added} & {_masked(x) for x in removed}
    return {"added": [x for x in added if _masked(x) not in moved],
            "removed": [x for x in removed if _masked(x) not in moved], "changed": changed}


# --------------------------------------------------------------------------- output
def _clip(text: str, n: int) -> str:
    w = text.split()
    return " ".join(w[:n]) + (" ..." if len(w) > n else "")


def render(ticker: str, asof: str, latest: dict, comp: dict, urls: tuple[str, str], deltas: list[tuple[str, dict]],
           max_words: int) -> str:
    out = [f"# SEC filing delta: {ticker} — {asof}", "",
           f"{latest['form']} filed {latest['filingDate']} (period {latest['reportDate']}): {urls[0]}",
           f"compared with {comp['form']} filed {comp['filingDate']} (period {comp['reportDate']}): {urls[1]}", "",
           "Only added, removed and reworded paragraphs; paragraphs whose only change is a number or date are left "
           "out. Filing text is qualitative context: never take a number from it (fact sheet only).", ""]
    budget, left = max_words, 0
    for name, d in deltas:
        out.append(f"## {name}")
        n = sum(len(v) for v in d.values())
        if not n:
            out += ["No substantive change.", ""]
            continue
        for label, key in (("Added", "added"), ("Removed", "removed"), ("Reworded", "changed")):
            for item in d[key]:
                text = (f"NOW: {_clip(item[1], 120)}\n  WAS: {_clip(item[0], 80)}" if key == "changed"
                        else _clip(item, 120))
                cost = len(text.split())
                if cost > budget:
                    left += 1
                    continue
                budget -= cost
                out.append(f"- **{label}**: {text}")
        out.append("")
    if left:
        out.append(f"{left} more changed paragraph(s) not shown (word cap {max_words}); see the filing: {urls[0]}")
    return "\n".join(out).rstrip() + "\n"


def run(ticker: str, asof: str, cfg: dict, fetcher=None) -> tuple[str, Path | None]:
    sc = cfg.get("sec") or {}
    if not sc.get("contact", "").strip():
        return "SKIP sec step off: set [sec].contact in CLAUDE.md", None
    if Ticker(ticker).exchange:
        return f"SKIP {ticker}: not a US listing (SEC filers only)", None
    f = fetcher or SecFetcher(cfg, asof)
    cik = cik_for(f, ticker)
    if cik is None:
        return f"SKIP {ticker}: not an SEC filer", None
    sub = json.loads(f.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    pair = pick_filings(sub["filings"]["recent"])
    if not pair:
        return f"SKIP {ticker}: no 10-K/10-Q with a comparable earlier filing", None
    latest, comp = pair
    urls = (doc_url(cik, latest), doc_url(cik, comp))
    new_ls, old_ls = lines(f.get(urls[0])), lines(f.get(urls[1]))
    spec = SECTIONS[latest["form"]]
    new_secs = [section(new_ls, s) for _, s in spec]
    if not any(new_secs):
        raise DataError(urls[0], "sections", "Risk Factors / MD&A headings not found")
    deltas = [(name, diff(section(old_ls, s), new)) for (name, s), new in zip(spec, new_secs)]
    path = ROOT / "research" / Ticker(ticker).slug / f"sec-delta-{asof}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(ticker, asof, latest, comp, urls, deltas, int(sc.get("max_words", 2000))))
    return f"OK {path.relative_to(ROOT)}", path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    try:
        msg, _ = run(a.ticker, a.asof, load_config())
    except DataError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
