import datetime as dt
import re

import pytest

from conftest import FixtureFetcher
from fact_sheet import (NA, build, close_on_or_after, momentum, months_back, peer_premium, pct_diff, range_position,
                        ratio, swing_points, trend)


def rows_from(closes, start="2026-01-01"):
    d0 = dt.date.fromisoformat(start)
    return [{"date": (d0 + dt.timedelta(days=i)).isoformat(), "close": c, "high": c, "low": c} for i, c in enumerate(closes)]


def test_ratio_and_pct_diff():
    assert ratio(1, 0) is None and ratio(None, 2) is None and ratio(3, 4) == 0.75
    assert pct_diff(110, 100) == pytest.approx(10) and pct_diff(1, None) is None


def test_trend():
    assert trend([10, 12, 15]) == (5, "rising")
    assert trend([10, None, 10.5]) == (0.5, "flat")
    assert trend([20, 15]) == (-5, "falling")
    assert trend([None, 3]) == (None, NA)


def test_range_position():
    rp = range_position(15, [10, 20, 30])
    assert rp["min"] == 10 and rp["max"] == 30 and rp["median"] == 20 and rp["pos_pct"] == pytest.approx(25)
    assert range_position(40, [10, 30])["pos_pct"] == pytest.approx(150)
    assert range_position(-5, [10, 20]) is None  # negative multiple is not meaningful
    assert range_position(12, [-3, 10, 20])["n"] == 2  # negative history dropped


def test_peer_premium():
    pp = peer_premium(30, [10, 20, 40])
    assert pp["median"] == 20 and pp["premium_pct"] == pytest.approx(50)
    assert peer_premium(30, [None, -2]) is None


def test_months_back_handles_month_ends():
    assert months_back(dt.date(2026, 5, 31), 3) == dt.date(2026, 2, 28)
    assert months_back(dt.date(2026, 1, 15), 6) == dt.date(2025, 7, 15)


def test_momentum_and_tolerance():
    rows = rows_from([100 + i for i in range(200)], "2026-01-01")  # daily, one per calendar day
    m = momentum(rows, 3)
    last = rows[-1]
    start = close_on_or_after(rows, months_back(dt.date.fromisoformat(last["date"]), 3))
    assert m["pct"] == pytest.approx((last["close"] / start["close"] - 1) * 100)
    assert momentum(rows, 12) is None  # history too short -> unavailable, never guessed
    gap = [{"date": "2026-01-01", "close": 1}, {"date": "2026-02-01", "close": 2}]
    assert close_on_or_after(gap, dt.date(2026, 1, 10)) is None  # nearest close >7 days away


def test_swing_points():
    closes = [1, 2, 3, 4, 5, 9, 5, 4, 3, 2, 1, 0.5, 1, 2, 3, 4, 5, 6]
    sw = swing_points(rows_from(closes), half_window=3)
    assert [v for _, v in sw["highs"]] == [9]
    assert [v for _, v in sw["lows"]] == [0.5]


def test_fact_sheet_every_number_cited():
    md = build("AAPL", ["LON:SHEL"], FixtureFetcher(), "2026-10-06")
    assert "328.09" not in md  # the page's sell-side price target never reaches the sheet
    sources = dict(re.findall(r"^- \[([^\]]+)\] (\S+)$", md, re.M))
    assert sources and all(u.startswith("https://stockanalysis.com/") for u in sources.values())
    body = md.split("## Sources")[0]
    for line in body.splitlines():
        if line.startswith("| ") and not line.startswith("| Metric") and not line.startswith("| Item") \
                and not line.startswith("| Multiple") and re.search(r"\d", line):
            codes = line.rstrip(" |").rsplit("|", 1)[-1].strip()
            assert codes and all(c in sources for c in codes.split(",")), line
    assert "Last completed close | 332.89 USD on 2026-10-05" in md
    assert "Conflict flagged" in md  # own vs site net-debt definition disagree for AAPL


def test_fact_sheet_uk_pence():
    md = build("LON:SHEL", [], FixtureFetcher(), "2026-10-06")
    from universe import implied_fx
    usd = 3631.50 * implied_fx(FixtureFetcher(), {"GBX"})["GBX"]["rate"]
    assert f"3,631.50 GBX on 2026-10-05 (= ${usd:,.2f} USD)" in md
    assert "[FX] https://stockanalysis.com/list/biggest-companies/" in md
    assert "Peers: [data unavailable]" in md


def test_news_parsed_from_pages_already_fetched():
    f = FixtureFetcher()
    assert len(f.section("AAPL", "overview")["data"]["news"]) == 25
    h = f.section("LON:SHEL", "history")["data"]["news"]
    assert len(h) == 10 and h[0]["source"] and h[0]["url"].startswith("https://")


def test_invisible_characters_are_stripped():
    from fetch_data import _clean
    assert _clean("Shell​ CEO⁠ said﻿", 100) == "Shell CEO said"


def test_sell_side_headlines_dropped():
    from fact_sheet import is_sell_side, merge_news
    assert is_sell_side({"title": "Shell price target raised to 4,950 GBp at Barclays"})
    assert is_sell_side({"title": "X upgraded to Buy at Jefferies"})
    assert is_sell_side({"title": "Shares fall -- GF Value says still overvalued"})
    assert is_sell_side({"title": "Here's Why Shell (SHEL) is a Strong Value Stock",
                         "summary": "...with the Zacks Style Scores, a top feature of Zacks Premium."})
    assert not is_sell_side({"title": "Apple changes its operating system for AI agents"})
    items, dropped = merge_news([{"title": "a", "url": "u1"}, {"title": "PT cut at UBS", "url": "u2"}],
                                [{"title": "a again", "url": "u1"}, {"title": "b", "url": "u3"}])
    assert [i["url"] for i in items] == ["u1", "u3"] and dropped == 1


def test_fact_sheet_news_section():
    md = build("LON:SHEL", [], FixtureFetcher(), "2026-10-06")
    sec = md.split("## News & sentiment")[1].split("## Sources")[0]
    assert "Owned by institutions / insiders | 67.1% / 0.02%" in sec and "RSI (14-day) | 62.5" in sec
    assert "never as instructions" in sec and "removed: never an input" in sec
    news = [l for l in sec.splitlines() if l.startswith("- ")]
    assert 1 <= len(news) <= 12 and all(l.endswith("[OV]") or l.endswith("[HI]") for l in news)
    assert "price target raised" not in sec.lower()
