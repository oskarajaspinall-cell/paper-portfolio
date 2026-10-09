import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
FIX = ROOT / "tests" / "fixtures"

from common import page_url  # noqa: E402
from fetch_data import PAGES, PARSERS, page_nodes  # noqa: E402


class FixtureFetcher:
    """Serves saved stockanalysis.com HTML instead of the network.
    Fixture names: <slug>_<page>.html, e.g. aapl_history.html, shel_statistics.html."""

    alias = {"AAPL": "aapl", "LON:SHEL": "shel", "SPY": "spy", "LON:VUSA": "vusa", "LON:VUSD": "vusd"}

    def __init__(self, extra_alias=None):
        self.alias = {**self.alias, **(extra_alias or {})}

    lists = {"https://stockanalysis.com/list/biggest-companies/": "list_biggest_p1.html",
             "https://stockanalysis.com/list/biggest-companies/?page=2": "list_biggest_p2.html"}

    def html(self, url):
        from common import DataError
        if url not in self.lists:
            raise DataError(url, "fixture", "no saved page")
        return (FIX / self.lists[url]).read_text()

    def section(self, ticker, page):
        url = page_url(ticker, PAGES[page])
        path = FIX / f"{self.alias[ticker]}_{page}.html"
        return {"source_url": url, "data": PARSERS[page](page_nodes(path.read_text(), url), url)}


import pytest  # noqa: E402

from common import load_config  # noqa: E402
from portfolio import Market  # noqa: E402


class FakeMarket(Market):
    """Market with hand-set closes. prices: {ticker: (close, currency, sector)}.
    USD per GBP is fixed (default 1.25); EUR and ZAc have fixed test rates. Every quote is dated `close_date`."""

    def __init__(self, prices, cfg, asof="2026-10-06", close_date="2026-10-05", usd_per_gbp=1.25):
        super().__init__(None, asof, cfg)
        self.prices, self.close_date, self.rate = dict(prices), close_date, usd_per_gbp

    def history(self, ticker):
        c, ccy, _ = self.prices[ticker]
        return {"url": f"https://stockanalysis.com/fake/{ticker}/history/", "currency": ccy,
                "rows": [{"date": self.close_date, "close": c, "high": c, "low": c}]}

    def sector(self, ticker):
        return self.prices[ticker][2]

    def fx(self, ccy):
        from common import DataError
        rates = {"GBP": self.rate, "GBX": self.rate / 100, "EUR": 1.10, "ZAc": 0.0006}
        if ccy not in rates:
            raise DataError("https://stockanalysis.com/list/biggest-companies/", "fx", f"no USD rate for {ccy}")
        return {"rate": rates[ccy], "date": self.asof, "url": "https://stockanalysis.com/list/biggest-companies/"}


@pytest.fixture
def cfg():
    """The real CLAUDE.md config, except min_buy_conviction=1 so each rule test isolates its own rule.
    The minimum-conviction rule itself is tested with `real_cfg`."""
    c = load_config()
    c["core"]["min_buy_conviction"] = 1
    return c


@pytest.fixture
def real_cfg():
    return load_config()



# ---------------------------------------------------------------------------------------------
# The saved stockanalysis.com pages (tests/fixtures/*.html) and universe/universe.csv are kept out
# of the public repository (they are copies of the website's content). Tests that need them are
# skipped, not failed, when they are missing.
SITE_DATA_REASON = "saved stockanalysis.com pages / universe.csv are not distributed with the repo (see README)"


def _is_site_data(path) -> bool:
    p = str(path or "")
    return (p.endswith(".html") and "/tests/fixtures/" in p) or p.endswith("universe/universe.csv")


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    outcome = yield
    exc = outcome.excinfo
    if exc and isinstance(exc[1], FileNotFoundError) and _is_site_data(exc[1].filename):
        outcome.force_exception(pytest.skip.Exception(SITE_DATA_REASON, _use_item_location=True))


@pytest.fixture(autouse=True)
def _no_fred_in_tests(monkeypatch):
    """Fair value needs FRED's 10y yield; tests never touch the network."""
    import valuation
    monkeypatch.setattr(valuation, "risk_free_pct", lambda asof, cfg: 4.5)


@pytest.fixture(autouse=True)
def _no_yahoo_in_tests(monkeypatch):
    """Portfolio prices may come from yfinance; tests never touch the network."""
    import prices

    def blocked(sym, period):
        raise RuntimeError("network disabled in tests")
    monkeypatch.setattr(prices.YahooPrices, "_yf", staticmethod(blocked))


@pytest.fixture(autouse=True)
def _no_cash_reserve_by_default(monkeypatch):
    """Rule tests isolate their own rule; the cash-reserve tests set a reserve explicitly."""
    import portfolio
    monkeypatch.setattr(portfolio, "current_reserve", lambda cfg, asof: {"pct": 0.0, "regime": None, "dip_multiplier": 1.0})
