"""Parsers against real saved stockanalysis.com HTML (fetched 2026-10-06)."""
import json
import re

import requests

import pytest

from common import DataError, Ticker, page_url
from conftest import FIX
from fetch_data import (Fetcher, JSLiteralParser, completed_closes, page_nodes, parse_history, parse_number,
                        parse_overview, parse_statement, parse_statistics)


def load(name, parser):
    url = f"https://stockanalysis.com/fixture/{name}"
    return parser(page_nodes((FIX / f"{name}.html").read_text(), url), url)


# ---- JS literal parser
@pytest.mark.parametrize("src,expected", [
    ('{a:1,b:"x"}', {"a": 1, "b": "x"}),
    ("{a:void 0,b:null,c:true,d:false}", {"a": None, "b": None, "c": True, "d": False}),
    ("[.5,-.3,1e3,-2.5e-2]", [0.5, -0.3, 1000.0, -0.025]),
    (r'{"q k":"a\"b\\cé"}', {"q k": 'a"b\\cé'}),
    ("{d:new Date(5)}", {"d": {"__new__": "Date", "args": [5]}}),
    ("{x:[{y:[1,2]},{}],z:NaN}", {"x": [{"y": [1, 2]}, {}], "z": None}),
])
def test_js_literal(src, expected):
    assert JSLiteralParser(src).parse() == expected


@pytest.mark.parametrize("text,val", [("4,843,808,342,000", 4843808342000), ("-2.125%", -2.125), ("+29.15%", 29.15),
                                      ("n/a", None), ("4.84T", 4.84e12), ("$1.08", 1.08), (None, None)])
def test_parse_number(text, val):
    assert parse_number(text) == val


# ---- overview
def test_overview_us():
    d = load("aapl_overview", parse_overview)
    assert d["sector"] == "Technology" and d["industry"] == "Consumer Electronics"
    assert d["info"]["price_currency"] == "USD" and d["earnings_date"] == "Oct 29, 2026"


def test_overview_uk_and_etf():
    d = load("shel_overview", parse_overview)
    assert d["sector"] == "Energy" and d["info"]["price_currency"] == "GBX" and d["info"]["financial_currency"] == "USD"
    spy = load("spy_overview", parse_overview)
    assert spy["info"]["price_currency"] == "USD" and spy["ch1y_pct"] == 16.59


def test_sell_side_targets_are_dropped():
    raw = (FIX / "aapl_overview.html").read_text()
    assert 'target:"' in raw  # the page does show an analyst target...
    for name, parser in [("aapl_overview", parse_overview), ("aapl_statistics", parse_statistics)]:
        blob = json.dumps(load(name, parser))
        assert '"target"' not in blob and '"analysts"' not in blob  # ...but we never keep it


# ---- statements
def test_income_statement():
    d = load("aapl_income", parse_statement)
    assert d["periods"][0] == "TTM" and d["periods"][1] == "2025-09-27"
    assert d["rows"]["revenue"][1] == 416161000000 and d["rows"]["netinc"][1] == 112010000000
    assert d["rows"]["ebitda"][0] is not None and d["currency"] == "USD"


def test_balance_cashflow_ratios():
    b = load("aapl_balance", parse_statement)
    assert b["rows"]["totalcash"][1] == 54697000000 and "debt" in b["rows"]
    c = load("aapl_cashflow", parse_statement)
    assert "fcf" in c["rows"] and len(c["rows"]["fcf"]) == len(c["periods"])
    r = load("aapl_ratios", parse_statement)
    assert r["rows"]["pe"][0] == pytest.approx(38.18827) and r["rows"]["roic"][1] == pytest.approx(0.92698)


def test_uk_statement_in_usd():
    d = load("shel_income", parse_statement)
    assert d["periods"][1] == "2025-12-31" and d["currency"] == "USD"


# ---- statistics
def test_statistics():
    d = load("aapl_statistics", parse_statistics)
    assert d["sma200"]["value"] == pytest.approx(289.757)
    assert d["sma50"]["value"] == pytest.approx(322.34, abs=0.01)
    assert d["ch1y"]["value"] == pytest.approx(29.15)
    assert d["earningsdate"]["text"] == "Oct 29, 2026"
    assert d["marketcap"]["value"] == 4843808342000


# ---- history
def test_history_and_completed_closes():
    d = load("aapl_history", parse_history)
    rows = d["rows"]
    assert len(rows) == 127 and rows[0]["date"] < rows[-1]["date"]
    done = completed_closes(d, "2026-10-06")
    assert done[-1] == {**done[-1], "date": "2026-10-05", "close": 332.89}
    assert all(r["date"] < "2026-10-06" for r in done)


def test_history_matches_rendered_table():
    """The embedded data and the server-rendered HTML table agree (data is in static HTML)."""
    html = (FIX / "aapl_history.html").read_text()
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", html, flags=re.S))
    assert re.search(r"Oct 5, 2026\s+332\.82\s+336\.21\s+331\.65\s+332\.89", re.sub(r"\s+", " ", text))


def test_history_uk_pence_and_etf():
    d = load("shel_history", parse_history)
    assert d["info"]["price_currency"] == "GBX"
    assert completed_closes(d, "2026-10-06")[-1]["close"] == 3631.5
    assert load("spy_history", parse_history)["info"]["price_currency"] == "USD"


# ---- failure modes: always name URL + field, never guess
def test_parse_failure_names_url_and_field():
    with pytest.raises(DataError) as e:
        page_nodes("<html>no data</html>", "https://stockanalysis.com/x/")
    assert e.value.url == "https://stockanalysis.com/x/" and e.value.field == "kit.start"


def test_missing_statement_table():
    html = '<script>kit.start(app, el, {data: [{type:"data",data:{info:{curr:{price:"USD"}}}},{type:"data",data:{statement:"x"}}]})</script>'
    with pytest.raises(DataError) as e:
        parse_statement(page_nodes(html, "u"), "u")
    assert e.value.field == "financialData.datekey"


# ---- URL mapping
def test_ticker_urls():
    assert page_url("AAPL", "history/") == "https://stockanalysis.com/stocks/aapl/history/"
    assert page_url("LON:SHEL", "statistics/") == "https://stockanalysis.com/quote/lon/SHEL/statistics/"
    assert page_url("SPY", "history/") == "https://stockanalysis.com/etf/spy/history/"
    assert Ticker("LON:SHEL").slug == "LON-SHEL" and Ticker("LON:SHEL").is_uk


# ---- fetcher behaviour (network mocked)
class FakeResp:
    def __init__(self, text, code=200):
        self.text, self.status_code, self.encoding = text, code, None


@pytest.fixture
def fetcher(tmp_path, cfg, monkeypatch):
    calls = []

    def fake_get(url, headers, timeout):
        calls.append((url, headers["User-Agent"]))
        if url.endswith("robots.txt"):
            return FakeResp("User-agent: *\nDisallow: /e/\nDisallow: /p/\n")
        if "/flaky/" in url:
            raise requests.ConnectionError("timed out")
        if "/missing/" in url:
            return FakeResp("", 404)
        return FakeResp((FIX / "aapl_history.html").read_text())

    monkeypatch.setattr(requests, "get", fake_get)
    sleeps = []
    monkeypatch.setattr("fetch_data.time.sleep", lambda s: sleeps.append(s))
    f = Fetcher(cfg, cache_dir=tmp_path, today="2026-10-06")
    f.calls, f.sleeps = calls, sleeps
    return f


def test_fetch_respects_robots(fetcher):
    with pytest.raises(DataError) as e:
        fetcher.html("https://stockanalysis.com/e/something/")
    assert e.value.field == "robots.txt"


def test_fetch_only_stockanalysis(fetcher):
    with pytest.raises(DataError):
        fetcher.html("https://example.com/stocks/aapl/")


def test_fetch_caches_per_day_and_rate_limits(fetcher, cfg):
    fetcher.section("AAPL", "history")
    fetcher.section("AAPL", "history")  # served from cache
    urls = [u for u, _ in fetcher.calls]
    assert urls.count("https://stockanalysis.com/stocks/aapl/history/") == 1
    assert all(ua == cfg["data"]["user_agent"] for _, ua in fetcher.calls)
    assert fetcher.sleeps and max(fetcher.sleeps) <= 3  # waited between robots.txt and the page


def test_fetch_http_error_names_url(fetcher):
    with pytest.raises(DataError) as e:
        fetcher.html("https://stockanalysis.com/missing/")
    assert e.value.field == "http" and "missing" in e.value.url


def test_fetch_network_failure_names_url(fetcher):
    with pytest.raises(DataError) as e:
        fetcher.html("https://stockanalysis.com/flaky/")
    assert e.value.field == "network" and "flaky" in e.value.url
    assert sum("flaky" in u for u, _ in fetcher.calls) == 3


def test_fetch_decodes_pages_as_utf8(fetcher):
    import requests as rq
    raw = "Petróleo Brasileiro".encode("utf-8")
    resp = rq.models.Response()
    resp.status_code, resp._content = 200, raw
    resp.headers["Content-Type"] = "text/html"  # no charset, as the site sends
    import fetch_data
    orig = rq.get
    rq.get = lambda *a, **k: resp
    try:
        assert fetcher._get("https://stockanalysis.com/x/") == "Petróleo Brasileiro"
    finally:
        rq.get = orig


def test_rate_limit_is_shared_between_parallel_fetchers(tmp_path, cfg, monkeypatch):
    import copy
    import threading
    import time as _t
    c = copy.deepcopy(cfg)
    c["data"]["request_interval_seconds"] = 0.3
    stamps = []

    def fake_get(url, headers, timeout):
        stamps.append(_t.time())
        return FakeResp("ok")

    monkeypatch.setattr(requests, "get", fake_get)
    fetchers = [Fetcher(c, cache_dir=tmp_path, today="2026-10-07") for _ in range(3)]  # like 3 researchers
    threads = [threading.Thread(target=f._get, args=(f"https://stockanalysis.com/p{i}/",)) for i, f in enumerate(fetchers)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    stamps.sort()
    assert len(stamps) == 3 and all(b - a >= 0.29 for a, b in zip(stamps, stamps[1:]))



def test_fetcher_refresh_refetches_pages_cached_earlier(tmp_path, monkeypatch, cfg):
    import time
    from fetch_data import BASE_URL, Fetcher
    calls = []
    monkeypatch.setattr(Fetcher, "allowed", lambda self, url: True)
    monkeypatch.setattr(Fetcher, "_get", lambda self, url: calls.append(url) or f"page {len(calls)}")
    url = BASE_URL + "/stocks/deck/history/"
    assert Fetcher(cfg, cache_dir=tmp_path, today="2026-10-08").html(url) == "page 1"   # saved before the open
    assert Fetcher(cfg, cache_dir=tmp_path, today="2026-10-08").html(url) == "page 1"   # normal: cached
    time.sleep(0.01)
    fresh = Fetcher(cfg, cache_dir=tmp_path, today="2026-10-08", refresh=True)
    assert fresh.html(url) == "page 2" and fresh.html(url) == "page 2"                 # re-fetched once
    assert len(calls) == 2
