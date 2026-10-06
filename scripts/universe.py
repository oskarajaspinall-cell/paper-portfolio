"""Build the investable universe: universe/universe.csv

Sources (switch each on/off in CLAUDE.md [universe]; all stockanalysis.com except the two text files):
- S&P 500: https://stockanalysis.com/list/sp-500-stocks/ (full list, one page)
- FTSE 100: universe/ftse100.txt (pasted by the owner; update at each quarterly review)
- FTSE All-World (approximation): the largest primary-listed stocks worldwide by USD market cap from
  https://stockanalysis.com/list/biggest-companies/?page=N . The official FTSE constituent list is not
  freely available; this proxy keeps every input on stockanalysis.com.

- Custom: your own tickers in universe/custom.txt (stockanalysis.com format, e.g. AAPL, LON:SHEL, TYO:7203).

A stock is screenable only if it is a primary-listed common stock, its quote currency has a USD rate
on stockanalysis.com (see implied_fx), and it is not tagged `screen=no`.

Usage:
    python scripts/universe.py build [--allworld-size 3800]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import BASE_URL, ROOT, DataError, load_config  # noqa: E402
from fetch_data import Fetcher, page_nodes  # noqa: E402

UNIVERSE = ROOT / "universe" / "universe.csv"
COLS = ["ticker", "name", "country", "currency", "market_cap_usd", "indexes", "screen", "note"]
SP500_URL = BASE_URL + "/list/sp-500-stocks/"
BIGGEST_URL = BASE_URL + "/list/biggest-companies/"


def to_ticker(s: str) -> str:
    """stockanalysis list symbol -> our ticker: 'NVDA' -> 'NVDA', 'tyo/6857' -> 'TYO:6857', '!lon/HSBA' -> 'LON:HSBA'."""
    s = s.lstrip("!$")
    if "/" in s:
        ex, sym = s.split("/", 1)
        return f"{ex.upper()}:{sym}"
    return s.upper()


def list_rows(html: str, url: str) -> list[dict]:
    page = page_nodes(html, url)[-1]
    rows = page.get("stockData")
    if not isinstance(rows, list) or not rows:
        raise DataError(url, "stockData", "list table missing")
    for r in rows:
        if not r.get("s"):
            raise DataError(url, "stockData.s", f"row without symbol: {r}")
    return rows


def read_ftse100(path: Path) -> dict[str, dict]:
    out = {}
    for line in path.read_text().splitlines():
        code, _, comment = line.partition("#")
        parts = code.split()
        if not parts:
            continue
        out[parts[0]] = {"name": comment.strip(), "screen": "screen=no" not in parts[1:]}
    return out


def implied_fx(fetcher, needed: set[str] | None = None, max_pages: int = 60, asof: str | None = None) -> dict:
    """USD per quoted unit for each currency, implied by stockanalysis.com's own conversion on the
    global list page (each row shows `price` in its quote currency and `priceUSD`). Quote units are kept
    as the site writes them, so GBX/ZAc rates are per penny/cent. Pages are read until every `needed`
    currency is found (or all pages up to max_pages when needed is None)."""
    import statistics as st
    found: dict[str, list[float]] = {}
    urls: dict[str, str] = {}
    for page in range(1, max_pages + 1):
        url = BIGGEST_URL + (f"?page={page}" if page > 1 else "")
        for r in list_rows(fetcher.html(url), url):
            if r.get("price") and r.get("priceUSD") and r.get("priceCurrency"):
                found.setdefault(r["priceCurrency"], []).append(r["priceUSD"] / r["price"])
                urls.setdefault(r["priceCurrency"], url)
        if needed is not None and needed <= set(found):
            break
    date = asof or dt.date.today().isoformat()
    return {c: {"rate": st.median(v), "date": date, "url": urls[c], "n": len(v)} for c, v in found.items()}


def fx_available(ccy: str, seen: set[str]) -> bool:
    return ccy == "USD" or ccy in seen


def build(fetcher, cfg: dict, allworld_size: int | None = None, ftse_path: Path | None = None,
          custom_path: Path | None = None) -> list[dict]:
    """Sources are switched on/off in CLAUDE.md [universe]; allworld_size overrides the config."""
    ucfg = cfg.get("universe", {})
    size = ucfg.get("allworld_size", 3800) if allworld_size is None else allworld_size
    ftse_path = ftse_path or ROOT / "universe" / "ftse100.txt"
    custom_path = custom_path or (ROOT / ucfg["custom_file"] if ucfg.get("custom_file") else None)
    uni: dict[str, dict] = {}

    def add(t, idx, **kw):
        row = uni.setdefault(t, {"ticker": t, "indexes": set(), "screen": True, "note": []})
        row["indexes"].add(idx)
        for k, v in kw.items():
            if v not in (None, "") and not row.get(k):
                row[k] = v
        return row

    if ucfg.get("sp500", True):
        for r in list_rows(fetcher.html(SP500_URL), SP500_URL):
            add(to_ticker(r["s"]), "SP500", name=r.get("n"), country="United States", currency="USD",
                market_cap_usd=r.get("marketCap"))

    page, kept, seen = 1, 0, set()
    while kept < size:
        url = BIGGEST_URL + (f"?page={page}" if page > 1 else "")
        rows = list_rows(fetcher.html(url), url)
        seen |= {r["priceCurrency"] for r in rows if r.get("price") and r.get("priceUSD") and r.get("priceCurrency")}
        for r in rows:
            if kept >= size:
                break
            if not r.get("isPrimaryListing") or r.get("subtype") != "stock":
                continue
            kept += 1
            add(to_ticker(r["s"]), "ALLWORLD", name=r.get("n"), country=r.get("country"),
                currency=r.get("priceCurrency"), market_cap_usd=r.get("marketCapUSD"))
        page += 1

    if ucfg.get("ftse100", True) and ftse_path.exists():
        for t, info in read_ftse100(ftse_path).items():
            row = add(t, "FTSE100", name=info["name"], country="United Kingdom")
            if not info["screen"]:
                row["screen"] = False
                row["note"].append("excluded from screen (investment trust/fund)")

    if custom_path and custom_path.exists():  # the user's own tickers (same file format as ftse100.txt)
        for t, info in read_ftse100(custom_path).items():
            row = add(t, "CUSTOM", name=info["name"])
            if not info["screen"]:
                row["screen"] = False
                row["note"].append("excluded from screen (screen=no)")

    for row in uni.values():
        if not row.get("currency"):  # names outside the global top list: confirm on the site
            try:
                sec = fetcher.section(row["ticker"], "overview")
                row["currency"] = sec["data"]["info"]["price_currency"]
                row["name"] = row.get("name") or sec["data"]["info"]["name"]
            except DataError as e:
                row["screen"] = False
                row["note"].append(f"no stock overview on stockanalysis.com ({e.field})")
                continue
        ccy = row.get("currency")
        if ccy != "USD" and ccy not in seen:  # not met on the pages read so far: look further
            try:
                seen |= set(implied_fx(fetcher, {ccy}))
            except DataError:
                pass
        if not fx_available(ccy, seen):
            row["screen"] = False
            row["note"].append(f"no FX rate for {ccy}")
    dedupe_share_classes(uni)
    out = []
    for t in sorted(uni, key=lambda k: -(uni[k].get("market_cap_usd") or 0)):
        r = uni[t]
        out.append({"ticker": t, "name": r.get("name", ""), "country": r.get("country", ""),
                    "currency": r.get("currency", ""), "market_cap_usd": r.get("market_cap_usd") or "",
                    "indexes": ";".join(sorted(r["indexes"])), "screen": "yes" if r["screen"] else "no",
                    "note": "; ".join(r["note"])})
    return out


def dedupe_share_classes(uni: dict[str, dict]) -> None:
    """Keep one line per company (same name): prefer an index member (SP500/FTSE100), then an exchange
    listing over OTC, then the larger market cap. The kept line inherits the dropped lines' indexes."""
    by_name: dict[str, list[str]] = {}
    for t, r in uni.items():
        if r.get("name"):
            by_name.setdefault(r["name"].strip().lower(), []).append(t)
    for tickers in by_name.values():
        if len(tickers) < 2:
            continue
        def rank(t):
            r = uni[t]
            return (bool(r["indexes"] & {"SP500", "FTSE100"}), not t.startswith("OTC:"), r.get("market_cap_usd") or 0)
        keep, *drop = sorted(tickers, key=rank, reverse=True)
        for t in drop:
            uni[keep]["indexes"] |= uni[t]["indexes"]
            uni[keep]["note"].append(f"other share class {t} dropped")
            del uni[t]


def read_universe(path: Path = UNIVERSE) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["build"])
    ap.add_argument("--allworld-size", type=int, help="override CLAUDE.md [universe] allworld_size")
    a = ap.parse_args(argv)
    cfg = load_config()
    try:
        rows = build(Fetcher(cfg), cfg, a.allworld_size)
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    with UNIVERSE.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    by = lambda k: sum(1 for r in rows if k in r["indexes"].split(";"))  # noqa: E731
    print(f"{UNIVERSE.relative_to(ROOT)}: {len(rows)} stocks (SP500 {by('SP500')}, FTSE100 {by('FTSE100')}, "
          f"ALLWORLD {by('ALLWORLD')}, CUSTOM {by('CUSTOM')}); screenable {sum(r['screen'] == 'yes' for r in rows)} "
          f"[built {dt.date.today().isoformat()}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
