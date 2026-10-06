import pytest

from common import DataError, company_domain
from conftest import FIX
from fetch_data import PARSERS, page_nodes, parse_info, parse_statistics
from screen import percentile_ranks, pick, pillar_scores, score, stock_metrics
from universe import BIGGEST_URL, SP500_URL, build, dedupe_share_classes, fx_available, list_rows, to_ticker


@pytest.mark.parametrize("s,t", [("NVDA", "NVDA"), ("tyo/6857", "TYO:6857"), ("!lon/HSBA", "LON:HSBA"),
                                 ("$AAPL", "AAPL"), ("lon/BT.A", "LON:BT.A")])
def test_to_ticker(s, t):
    assert to_ticker(s) == t


def test_list_pages_parse():
    sp = list_rows((FIX / "list_sp500.html").read_text(), SP500_URL)
    assert len(sp) == 503 and sp[0]["s"] == "NVDA"
    big = list_rows((FIX / "list_biggest_p1.html").read_text(), BIGGEST_URL)
    assert len(big) == 100 and big[-1]["s"] == "tyo/6857" and big[-1]["priceCurrency"] == "JPY"


class ListFetcher:
    pages = {SP500_URL: "list_sp500.html", BIGGEST_URL: "list_biggest_p1.html",
             BIGGEST_URL + "?page=2": "list_biggest_p2.html"}

    def html(self, url):
        return (FIX / self.pages[url]).read_text()

    def section(self, ticker, page):
        if ticker == "LON:SHEL":
            url = "https://stockanalysis.com/quote/lon/SHEL/"
            return {"source_url": url, "data": PARSERS["overview"](page_nodes((FIX / "shel_overview.html").read_text(), url), url)}
        raise DataError(f"https://stockanalysis.com/quote/lon/{ticker}/", "infoTable.Sector", "fund page")


def test_build_universe(cfg, tmp_path):
    ftse = tmp_path / "ftse.txt"
    ftse.write_text("# c\nLON:HSBA # HSBC\nLON:SHEL # Shell\nLON:SMT screen=no # Scottish Mortgage\n")
    rows = {r["ticker"]: r for r in build(ListFetcher(), cfg, 150, ftse)}
    assert rows["NVDA"]["indexes"] == "ALLWORLD;SP500" and rows["NVDA"]["screen"] == "yes"
    assert rows["LON:HSBA"]["indexes"] == "ALLWORLD;FTSE100" and rows["LON:HSBA"]["currency"] == "GBX"
    assert rows["TPE:2330"]["screen"] == "yes" and rows["TPE:2330"]["currency"] == "TWD"  # site gives a USD rate
    assert rows["TYO:6857"]["screen"] == "yes"
    assert rows["LON:SMT"]["screen"] == "no" and "investment trust" in rows["LON:SMT"]["note"]
    assert rows["LON:SHEL"]["currency"] == "GBX"  # resolved from its own overview page
    assert sum("ALLWORLD" in r["indexes"] for r in rows.values()) == 150


def test_percentile_ranks():
    r = percentile_ranks({"a": 1, "b": 2, "c": 2, "d": 3, "e": None}, True)
    assert r == {"a": 0, "b": 50, "c": 50, "d": 100}
    assert percentile_ranks({"a": 1, "b": 3}, False) == {"a": 100, "b": 0}


def test_pillar_needs_min_metrics_and_ignores_negative_multiples():
    m = {"A": {"roic": 30, "pe": 10}, "B": {"roic": 10, "pe": -5}, "C": {"roic": 20, "pe": 20}}
    p = pillar_scores(m, ["roic", "-pe"], 2)
    assert p["B"] is None  # negative P/E is not "cheap": treated as missing -> too few metrics
    assert p["A"] > p["C"]


def test_score_and_pick(cfg):
    base = {"roic": 0, "roce": 0, "fcfMargin": 0, "operatingMargin": 0, "fScore": 0, "debtEbitda": 1,
            "fcfYield": 0, "earningsYield": 0, "evEbitda": 10, "pe": 10, "ch1y": 0, "price_vs_sma200": 0,
            "price_vs_sma50": 0, "earnings_date": None}
    good = dict(base, roic=50, roce=50, fcfMargin=30, operatingMargin=30, fScore=8, debtEbitda=0.5, fcfYield=8,
                earningsYield=8, evEbitda=6, pe=8)
    mom = dict(base, ch1y=80, price_vs_sma200=30, price_vs_sma50=10, earnings_date="2026-10-29")
    late = dict(mom, earnings_date="2027-03-01")  # outside the 42-day window
    rows = score({"GOOD": good, "MOM": mom, "LATE": late, "MID": base}, cfg, "2026-10-06")
    by = {r["ticker"]: r for r in rows}
    assert by["LATE"]["tactical"] is None and by["MOM"]["tactical"] is not None
    picks = pick(rows, cfg)
    assert picks == [{"ticker": "GOOD", "type": "CORE", "score": pytest.approx(by["GOOD"]["core"], abs=0.05)},
                     {"ticker": "MOM", "type": "TACTICAL", "score": pytest.approx(by["MOM"]["tactical"], abs=0.05)}]
    assert len(picks) <= cfg["agents"]["max_new_initiations_per_week"]


def test_stock_metrics_from_real_page():
    url = "https://stockanalysis.com/stocks/aapl/statistics/"
    nodes = page_nodes((FIX / "aapl_statistics.html").read_text(), url)
    m = stock_metrics(parse_statistics(nodes, url), parse_info(nodes, url))
    assert m["earnings_date"] == "2026-10-29" and m["roic"] == pytest.approx(101.57, abs=0.01)
    assert m["price_vs_sma200"] == pytest.approx((m["price"] / 289.757 - 1) * 100)


@pytest.mark.parametrize("w,d", [("https://www.apple.com", "apple.com"), ("https://www.shell.com/", "shell.com"),
                                 ("investors.example.co.uk", "investors.example.co.uk"), (None, None)])
def test_company_domain(w, d):
    assert company_domain(w) == d


def test_fx_available_only_for_currencies_with_a_site_rate():
    assert fx_available("USD", set()) and fx_available("TWD", {"TWD"}) and not fx_available("XYZ", {"TWD"})


def test_dedupe_share_classes():
    def row(name, idx, cap):
        return {"name": name, "indexes": set(idx), "market_cap_usd": cap, "note": []}
    uni = {"GOOGL": row("Alphabet Inc.", ["SP500", "ALLWORLD"], 4e12), "GOOG": row("Alphabet Inc.", ["SP500"], 4e12),
           "ASX:QUB": row("Qube Holdings Limited", ["ALLWORLD"], 5e9), "OTC:QUBHF": row("Qube Holdings Limited", ["ALLWORLD"], 6e9),
           "BRK.B": row("Berkshire Hathaway Inc.", ["SP500"], 1e12), "BRK.A": row("Berkshire Hathaway Inc.", ["ALLWORLD"], 1.1e12),
           "MSFT": row("Microsoft Corporation", ["SP500"], 3e12)}
    dedupe_share_classes(uni)
    assert set(uni) == {"GOOGL", "ASX:QUB", "BRK.B", "MSFT"}  # one line per company; never OTC over an exchange
    assert uni["BRK.B"]["indexes"] == {"SP500", "ALLWORLD"} and "BRK.A dropped" in uni["BRK.B"]["note"][0]


class CustomFetcher(ListFetcher):
    """Overview pages for custom tickers; records which list pages were read."""

    def __init__(self):
        self.read = []

    def html(self, url):
        self.read.append(url)
        return super().html(url)

    def section(self, ticker, page):
        name = {"AAPL": "aapl_overview", "MSFT": "aapl_overview", "LON:SHEL": "shel_overview"}.get(ticker)
        if not name:
            raise DataError(f"https://stockanalysis.com/x/{ticker}/", "http", "status 404")
        url = f"https://stockanalysis.com/x/{ticker}/"
        return {"source_url": url, "data": PARSERS["overview"](page_nodes((FIX / f"{name}.html").read_text(), url), url)}


def custom_cfg(cfg, size=0):
    import copy
    c = copy.deepcopy(cfg)
    c["universe"].update(sp500=False, ftse100=False, allworld_size=size)
    return c


def test_custom_only_universe_reads_no_list_pages(cfg, tmp_path):
    custom = tmp_path / "custom.txt"
    custom.write_text("# mine\nAAPL\nMSFT screen=no  # keep out of the screen\nNOPE\n")
    f = CustomFetcher()
    rows = {r["ticker"]: r for r in build(f, custom_cfg(cfg), custom_path=custom)}
    assert set(rows) == {"AAPL", "MSFT", "NOPE"} and all(r["indexes"] == "CUSTOM" for r in rows.values())
    assert rows["AAPL"]["screen"] == "yes" and rows["MSFT"]["screen"] == "no"
    assert rows["NOPE"]["screen"] == "no" and "no stock overview" in rows["NOPE"]["note"]
    assert f.read == []  # S&P list, FTSE file and global list all switched off; USD needs no FX page


def test_custom_non_usd_name_gets_fx_from_site(cfg, tmp_path):
    custom = tmp_path / "custom.txt"
    custom.write_text("LON:SHEL\n")
    f = CustomFetcher()
    rows = {r["ticker"]: r for r in build(f, custom_cfg(cfg), custom_path=custom)}
    assert rows["LON:SHEL"]["currency"] == "GBX" and rows["LON:SHEL"]["screen"] == "yes"
    assert f.read == [BIGGEST_URL]  # read just far enough to find a GBX rate
