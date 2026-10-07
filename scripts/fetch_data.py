"""Scrape stockanalysis.com pages into JSON (one `source_url` per section).

stockanalysis.com has no official API. Every page is server-rendered by SvelteKit and
embeds its full dataset as a JavaScript object literal inside the `kit.start(...)`
bootstrap script. We parse that literal (it is the same data the visible tables show)
instead of executing any JavaScript.

Rules enforced here: robots.txt respected, <=1 request per `request_interval_seconds`,
descriptive User-Agent, per-day cache in data/cache/, and any failed load or parse
raises DataError naming the URL and the field -- never a guessed value.

Usage:
    python scripts/fetch_data.py AAPL
    python scripts/fetch_data.py LON:SHEL --pages overview,history
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.robotparser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import BASE_URL, ROOT, DataError, Ticker, load_config, page_url  # noqa: E402

CACHE_DIR = ROOT / "data" / "cache"

PAGES = {
    "overview": "",
    "income": "financials/income-statement/",
    "balance": "financials/balance-sheet/",
    "cashflow": "financials/cash-flow-statement/",
    "ratios": "financials/ratios/",
    "statistics": "statistics/",
    "history": "history/",
    "filings": "filings/",
}

# Sell-side analyst outputs are never an input (house rule). Parsers drop these keys.
US_EXCHANGES = {"NASDAQ", "NYSE", "NYSEARCA", "NYSEAMERICAN", "BATS", "CBOE"}
BANNED_KEYS = {"target", "analysts", "priceTarget", "analystRating", "consensus", "fairValue"}


# --------------------------------------------------------------------------- JS literal parser
class JSLiteralParser:
    """Minimal parser for the JS object literals SvelteKit emits (unquoted keys,
    `void 0`, `.5` style numbers, `new Date(n)`). No code is executed."""

    _num = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")
    _ident = re.compile(r"[A-Za-z_$][\w$]*")

    def __init__(self, text: str, pos: int = 0):
        self.s, self.i = text, pos

    def _ws(self):
        while self.i < len(self.s) and self.s[self.i] in " \t\r\n":
            self.i += 1

    def parse(self):
        self._ws()
        c = self.s[self.i]
        if c == "{":
            return self._object()
        if c == "[":
            return self._array()
        if c in "\"'`":
            return self._string()
        if c == "-" or c == "." or c.isdigit():
            if self.s.startswith("-Infinity", self.i):
                self.i += 9
                return float("-inf")
            m = self._num.match(self.s, self.i)
            if not m:
                raise ValueError(f"bad number at {self.i}")
            self.i = m.end()
            v = float(m.group(0))
            return int(v) if re.fullmatch(r"-?\d+", m.group(0)) else v
        m = self._ident.match(self.s, self.i)
        if not m:
            raise ValueError(f"unexpected {c!r} at {self.i}")
        word = m.group(0)
        self.i = m.end()
        if word == "true":
            return True
        if word == "false":
            return False
        if word in ("null", "undefined"):
            return None
        if word == "NaN":
            return None
        if word == "Infinity":
            return float("inf")
        if word == "void":
            self._ws()
            self.parse()
            return None
        if word == "new":
            self._ws()
            ctor = self._ident.match(self.s, self.i)
            self.i = ctor.end()
            self._ws()
            self.i += 1  # (
            args = [] if self.s[self.i] == ")" else [self.parse()]
            self._ws()
            self.i += 1  # )
            return {"__new__": ctor.group(0), "args": args}
        raise ValueError(f"unsupported identifier {word!r} at {self.i}")

    def _string(self):
        q = self.s[self.i]
        self.i += 1
        out = []
        while True:
            c = self.s[self.i]
            if c == "\\":
                n = self.s[self.i + 1]
                if n == "u":
                    out.append(chr(int(self.s[self.i + 2:self.i + 6], 16)))
                    self.i += 6
                    continue
                out.append({"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f"}.get(n, n))
                self.i += 2
                continue
            if c == q:
                self.i += 1
                return "".join(out)
            out.append(c)
            self.i += 1

    def _array(self):
        self.i += 1
        out = []
        while True:
            self._ws()
            if self.s[self.i] == "]":
                self.i += 1
                return out
            if self.s[self.i] == ",":  # hole
                out.append(None)
                self.i += 1
                continue
            out.append(self.parse())
            self._ws()
            if self.s[self.i] == ",":
                self.i += 1

    def _object(self):
        self.i += 1
        out = {}
        while True:
            self._ws()
            if self.s[self.i] == "}":
                self.i += 1
                return out
            if self.s[self.i] in "\"'":
                key = self._string()
            else:
                m = re.compile(r"[\w$]+").match(self.s, self.i)
                key = m.group(0)
                self.i = m.end()
            self._ws()
            self.i += 1  # :
            out[key] = self.parse()
            self._ws()
            if self.s[self.i] == ",":
                self.i += 1


def page_nodes(html: str, url: str) -> list[dict]:
    """Return the `data` payload of every SvelteKit route node on the page."""
    k = html.find("kit.start(")
    if k < 0:
        raise DataError(url, "kit.start", "SvelteKit bootstrap script not found")
    m = re.compile(r"\bdata:\s*\[").search(html, k)
    if not m:
        raise DataError(url, "kit.start.data", "data array not found")
    try:
        nodes = JSLiteralParser(html, m.end() - 1).parse()
    except (ValueError, IndexError, AttributeError) as e:
        raise DataError(url, "kit.start.data", f"parse error: {e}") from e
    return [n.get("data") for n in nodes if isinstance(n, dict) and n.get("data")]


def _strip_banned(obj):
    if isinstance(obj, dict):
        return {k: _strip_banned(v) for k, v in obj.items() if k not in BANNED_KEYS}
    if isinstance(obj, list):
        return [_strip_banned(v) for v in obj]
    return obj


def parse_number(text) -> float | None:
    """'4,843,808,342,000' -> 4843808342000; '-2.125%' -> -2.125; 'n/a' -> None.
    Percent strings stay in percent units. Suffixes K/M/B/T are expanded."""
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return float(text)
    t = str(text).strip().replace(",", "").replace("$", "").replace("+", "")
    if t in ("", "n/a", "-", "N/A"):
        return None
    t = t.rstrip("%")
    mult = {"K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}.get(t[-1:], 1)
    if mult != 1:
        t = t[:-1]
    try:
        return float(t) * mult
    except ValueError:
        return None


# --------------------------------------------------------------------------- section parsers
def _info(nodes, url):
    for n in nodes:
        if "info" in n:
            return n["info"]
    raise DataError(url, "info", "ticker info node missing")


def parse_info(nodes, url) -> dict:
    info = _info(nodes, url)
    curr = info.get("curr") or {}
    q = info.get("quote") or {}
    if not curr.get("price") and info.get("exchange") in US_EXCHANGES:
        curr = {"price": "USD", "financial": "USD"}  # US-listed ETF pages omit `curr`
    if not curr.get("price"):
        raise DataError(url, "info.curr.price", "price currency missing")
    return {
        "ticker": info.get("ticker"),
        "name": info.get("nameFull") or info.get("name"),
        "exchange": info.get("exchange"),
        "type": info.get("type"),
        "price_currency": curr.get("price"),
        "financial_currency": curr.get("financial"),
        "quote": {"last": q.get("p"), "prev_close": q.get("cl"), "date": q.get("td"),
                  "market_state": q.get("ms"), "high_52w": q.get("h52"), "low_52w": q.get("l52")},
    }


def parse_overview(nodes, url) -> dict:
    page = _strip_banned(nodes[-1])
    out = {"info": parse_info(nodes, url)}
    table = {r.get("t"): r.get("v") for r in page.get("infoTable", []) or [] if isinstance(r, dict)}
    out["sector"] = table.get("Sector")
    out["industry"] = table.get("Industry")
    out["website"] = table.get("Website")
    out["earnings_date"] = page.get("earningsDate")
    out["earnings_date_label"] = page.get("earningsDateLabel")
    out["ch1y_pct"] = parse_number(page.get("ch1y"))  # ETFs show this on the overview
    if out["info"]["type"] != "etf" and not out["sector"]:
        raise DataError(url, "infoTable.Sector", "sector missing")
    return out


def parse_statement(nodes, url) -> dict:
    page = nodes[-1]
    fd = page.get("financialData")
    if not fd or not fd.get("datekey"):
        raise DataError(url, "financialData.datekey", "statement table missing")
    periods = fd["datekey"]
    rows = {k: v for k, v in fd.items()
            if k not in ("datekey", "fiscalYear", "fiscalQuarter") and isinstance(v, list)}
    for k, v in rows.items():
        if len(v) != len(periods):
            raise DataError(url, k, f"{len(v)} values for {len(periods)} periods")
    return {"statement": page.get("statement"), "period": page.get("period"),
            "periods": periods, "fiscal_years": fd.get("fiscalYear"),
            "currency": _info(nodes, url).get("curr", {}).get("financial"), "rows": rows}


def parse_statistics(nodes, url) -> dict:
    page = _strip_banned(nodes[-1])
    out = {}
    for group, body in page.items():
        if not isinstance(body, dict) or not isinstance(body.get("data"), list):
            continue
        for item in body["data"]:
            if not isinstance(item, dict) or "id" not in item or item["id"] in BANNED_KEYS:
                continue
            raw = item.get("hover", item.get("value"))
            out[item["id"]] = {"title": item.get("title"), "group": group,
                               "text": item.get("value"), "value": parse_number(raw)}
    if not out:
        raise DataError(url, "statistics", "no statistics groups found")
    return out


def parse_history(nodes, url) -> dict:
    page = nodes[-1]
    try:
        raw = page["data"]["data"]
    except (KeyError, TypeError) as e:
        raise DataError(url, "data.data", "price history array missing") from e
    rows = []
    for r in raw:
        if r.get("t") is None or r.get("c") is None:
            raise DataError(url, "history.close", f"row without date/close: {r}")
        rows.append({"date": r["t"], "open": r.get("o"), "high": r.get("h"), "low": r.get("l"),
                     "close": r["c"], "adj_close": r.get("a"), "volume": r.get("v")})
    if not rows:
        raise DataError(url, "history", "no rows")
    rows.sort(key=lambda r: r["date"])
    return {"info": parse_info(nodes, url), "rows": rows}


def parse_filings(nodes, url) -> dict:
    """Dated company events (earnings releases, reports, filings) from the filings page."""
    page = nodes[-1]
    events = page.get("events")
    if not isinstance(events, list):
        raise DataError(url, "events", "filings/events list missing")
    out = []
    for e in events:
        if not e.get("eventDate"):
            continue
        out.append({"date": e["eventDate"], "title": e.get("title"),
                    "types": sorted({f.get("type") for f in e.get("filings") or [] if f.get("type")})})
    out.sort(key=lambda e: e["date"])
    return {"events": out}


def completed_closes(history: dict, asof: str) -> list[dict]:
    """Rows strictly before `asof` (YYYY-MM-DD). The page includes today's live,
    not-yet-final row, so it is never treated as a close."""
    return [r for r in history["rows"] if r["date"] < asof]


PARSERS = {"overview": parse_overview, "income": parse_statement, "balance": parse_statement,
           "cashflow": parse_statement, "ratios": parse_statement,
           "statistics": parse_statistics, "history": parse_history, "filings": parse_filings}


# --------------------------------------------------------------------------- fetching
class Fetcher:
    def __init__(self, cfg: dict | None = None, cache_dir: Path = CACHE_DIR, today: str | None = None):
        cfg = cfg or load_config()
        self.ua = cfg["data"]["user_agent"]
        self.interval = float(cfg["data"]["request_interval_seconds"])
        self.today = today or dt.date.today().isoformat()
        self.cache_dir = cache_dir / self.today
        self.stamp = cache_dir / ".last_request"
        self._robots = None

    def _wait(self):
        try:
            last = float(self.stamp.read_text())
        except (OSError, ValueError):
            last = 0.0
        delay = last + self.interval - time.time()
        if delay > 0:
            time.sleep(delay)

    def _get(self, url: str) -> str:
        import requests

        import fcntl

        last_err = None
        self.stamp.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(3):  # network hiccups only; a bad page is never retried into a guess
            if attempt:
                time.sleep(self.interval * 5 * attempt)
            # One lock for every process on this machine (parallel researchers share one rate limit).
            with open(self.stamp.with_suffix(".lock"), "w") as lk:
                fcntl.flock(lk, fcntl.LOCK_EX)
                try:
                    self._wait()
                    try:
                        r = requests.get(url, headers={"User-Agent": self.ua}, timeout=30)
                        break
                    except requests.RequestException as e:
                        last_err = e
                finally:
                    self.stamp.write_text(str(time.time()))
                    fcntl.flock(lk, fcntl.LOCK_UN)
        else:
            raise DataError(url, "network", f"{type(last_err).__name__} after 3 attempts")
        if r.status_code != 200:
            raise DataError(url, "http", f"status {r.status_code}")
        r.encoding = "utf-8"  # pages are UTF-8 but the server doesn't say so (requests would guess Latin-1)
        return r.text

    def allowed(self, url: str) -> bool:
        if self._robots is None:
            cached = self.cache_dir / "robots.txt"
            if cached.exists():
                text = cached.read_text()
            else:
                text = self._get(BASE_URL + "/robots.txt")
                cached.parent.mkdir(parents=True, exist_ok=True)
                cached.write_text(text)
            self._robots = urllib.robotparser.RobotFileParser()
            self._robots.parse(text.splitlines())
        return self._robots.can_fetch(self.ua, url)

    def html(self, url: str) -> str:
        if not url.startswith(BASE_URL + "/"):
            raise DataError(url, "domain", "quantitative data must come from stockanalysis.com")
        cached = self.cache_dir / (url[len(BASE_URL) + 1:].strip("/").replace("/", "__") + ".html")
        if cached.exists():
            return cached.read_text()
        if not self.allowed(url):
            raise DataError(url, "robots.txt", "path disallowed by robots.txt -- STOP and tell the owner")
        text = self._get(url)
        cached.parent.mkdir(parents=True, exist_ok=True)
        cached.write_text(text)
        return text

    def section(self, ticker: str, page: str) -> dict:
        url = page_url(ticker, PAGES[page])
        data = PARSERS[page](page_nodes(self.html(url), url), url)
        return {"source_url": url, "data": data}

    def ticker(self, ticker: str, pages=tuple(p for p in PAGES if p != "filings")) -> dict:
        return {"ticker": ticker, "fetched": self.today,
                "sections": {p: self.section(ticker, p) for p in pages}}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--pages", default=",".join(p for p in PAGES if p != "filings"))
    args = ap.parse_args(argv)
    f = Fetcher()
    try:
        out = f.ticker(args.ticker, [p.strip() for p in args.pages.split(",")])
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    path = f.cache_dir / f"{Ticker(args.ticker).slug}.json"
    path.write_text(json.dumps(out, indent=1))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
