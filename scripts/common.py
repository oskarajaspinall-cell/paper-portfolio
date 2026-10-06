"""Shared helpers: config loading, ticker <-> URL mapping, watchlist parsing."""
from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://stockanalysis.com"


class DataError(Exception):
    """A page failed to load or parse. Always names the URL and the field."""

    def __init__(self, url: str, field: str, detail: str = ""):
        self.url, self.field = url, field
        super().__init__(f"{url} :: field '{field}'" + (f" :: {detail}" if detail else ""))


def load_config(claude_md: Path | None = None) -> dict:
    text = (claude_md or ROOT / "CLAUDE.md").read_text()
    m = re.search(r"<!-- CONFIG:START -->\s*```toml\n(.*?)```\s*<!-- CONFIG:END -->", text, re.S)
    if not m:
        raise SystemExit("CLAUDE.md: config block (CONFIG:START/END) not found")
    return tomllib.loads(m.group(1))


@dataclass(frozen=True)
class Ticker:
    raw: str  # e.g. "AAPL", "LON:SHEL", "SPY"

    @property
    def exchange(self) -> str | None:
        return self.raw.split(":")[0].upper() if ":" in self.raw else None

    @property
    def symbol(self) -> str:
        return self.raw.split(":")[-1]

    @property
    def is_uk(self) -> bool:
        return self.exchange == "LON"

    @property
    def slug(self) -> str:
        return self.raw.replace(":", "-")

    def base_path(self, etf: bool = False) -> str:
        if self.exchange:
            return f"/quote/{self.exchange.lower()}/{self.symbol}/"
        return f"/{'etf' if etf else 'stocks'}/{self.symbol.lower()}/"

    def url(self, page: str = "", etf: bool = False) -> str:
        return BASE_URL + self.base_path(etf) + page


ETF_TICKERS = {"SPY"}


def page_url(ticker: str, page: str = "") -> str:
    t = Ticker(ticker)
    return t.url(page, etf=t.raw.upper() in ETF_TICKERS)


def read_watchlist(path: Path | None = None) -> dict[str, str | None]:
    """Returns {ticker: ir_domain_or_None}. Lines: 'AAPL ir=investor.apple.com'."""
    out: dict[str, str | None] = {}
    for line in (path or ROOT / "universe" / "watchlist.txt").read_text().splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        ir = next((p[3:] for p in parts[1:] if p.startswith("ir=")), None)
        out[parts[0]] = ir
    return out


# Core triggers are thesis-only (owner rule): no price levels and no price-driven multiples.
PRICE_DRIVEN_FIELDS = {"close", "price", "sma50", "sma200", "ch1y", "pe", "peForward", "ps", "pb", "pfcf", "pocf",
                       "evEbitda", "evSales", "evEbit", "evFcf", "evEarnings", "fcfYield", "earningsYield",
                       "dividendYield", "marketcap", "enterpriseValue", "rsi", "beta"}
_PRICE_WORDS = re.compile(r"\b(share price|stock price|price (?:falls|drops|closes|level)|closes? (?:below|above)|"
                          r"moving average|\d+-day|drawdown|stop[- ]loss|P/E|EV/EBITDA|multiple)\b", re.I)


def core_trigger_problem(trigger: dict) -> str | None:
    """Reason a CORE trigger is not thesis-only, or None if acceptable."""
    chk = trigger.get("check") or {}
    if chk.get("source") == "price" or chk.get("field") in PRICE_DRIVEN_FIELDS:
        return f"price-based check {chk.get('source')}.{chk.get('field')}"
    m = _PRICE_WORDS.search(trigger.get("text", ""))
    if m:
        return f"price-based wording '{m.group(0)}'"
    return None


IR_DOMAINS = ROOT / "universe" / "ir_domains.txt"


def company_domain(website: str | None) -> str | None:
    """'https://www.apple.com/' -> 'apple.com' (the company's own site, from its stockanalysis.com overview)."""
    if not website:
        return None
    from urllib.parse import urlparse
    host = (urlparse(website if "://" in website else "https://" + website).hostname or "").lower()
    return host[4:] if host.startswith("www.") else (host or None)


def record_ir_domain(ticker: str, domain: str | None) -> None:
    """Remember a company's own domain so researchers may fetch its IR pages."""
    if not domain:
        return
    lines = IR_DOMAINS.read_text().splitlines() if IR_DOMAINS.exists() else []
    if any(l.split()[:1] == [ticker] for l in lines):
        return
    lines.append(f"{ticker} {domain}")
    IR_DOMAINS.write_text("\n".join(sorted(lines)) + "\n")


def allowed_domains(cfg: dict | None = None) -> set[str]:
    """Qualitative allowlist: config allowlist + watchlist ir= domains + recorded company domains."""
    doms = {d.lower() for d in (cfg or load_config())["data"]["allowlist"]}
    doms |= {ir.lower() for ir in read_watchlist().values() if ir}
    if IR_DOMAINS.exists():
        doms |= {l.split()[1].lower() for l in IR_DOMAINS.read_text().splitlines() if len(l.split()) == 2}
    return doms
