import pytest

import dashboard as D


def test_max_drawdown():
    assert D.max_drawdown([100, 110, 99, 120, None, 114]) == pytest.approx(-10.0) and D.max_drawdown([]) == 0.0


def test_add_world_indexes_to_the_first_date():
    ser = [{"date": "2026-10-06"}, {"date": "2026-10-07"}]
    D.add_world(ser, {"2026-10-05": 50.0, "2026-10-07": 55.0})
    assert [p["world"] for p in ser] == pytest.approx([100.0, 110.0])
    D.add_world(ser, None)
    assert ser[0]["world"] is None


def test_funnel_counts_stocks_not_rows():
    dec = [{"date": "2026-11-15", "ticker": "A", "decision": "AVOID", "conviction": "3"},
           {"date": "2026-11-16", "ticker": "A", "decision": "BUY", "conviction": "4"},
           {"date": "2026-11-16", "ticker": "H", "decision": "HOLD", "conviction": "4"},   # a holding: not a new-name verdict
           {"date": "2026-10-25", "ticker": "B", "decision": "AVOID", "conviction": "2"}]
    led = [{"date": "2026-11-16", "ticker": "A", "side": "BUY"}, {"date": "2026-11-16", "ticker": "Z", "side": "TRIM"}]
    f = D.funnel(dec, led, "2026-11-17")
    assert f["7"] == {"researched": 1, "conv4": 1, "bought": 1} and f["30"]["researched"] == 2


def test_attention_lists_what_is_waiting():
    hold = [{"ticker": "CI", "conviction": 4, "latest_conviction": 3, "latest_eval_date": "2026-11-16"},
            {"ticker": "OTIS", "conviction": 3, "latest_conviction": 3, "latest_eval_date": "2026-11-16"}]  # already resized
    watch = [{"ticker": "N", "pct_to_entry": "-1.0"}, {"ticker": "F", "pct_to_entry": "-9"},
             {"ticker": "S", "pct_to_entry": "2", "skipped_hit_date": "2026-11-17"}]
    a = D.attention([{"action": "BUY", "ticker": "T", "fills": "next open"}, {"action": "HOLD", "ticker": "Q"}], hold,
                    [{"ticker": "X"}], watch, [1], 4)
    text = " | ".join(i["text"] for i in a)
    assert "BUY T" in text and "CI:" in text and "OTIS" not in text and "re-research: X" in text
    assert "skipped" in text and "S" in text and "Within 2% of entry price: N" in text and "1 conviction-4" in text
    assert D.attention([], [], [], [], [], 4) == []


def test_health_reads_the_last_run_and_problem_lines(tmp_path):
    (tmp_path / "fills-2026-11-16.log").write_text("== start\n!! upload failed\n")
    (tmp_path / "fills-2026-10-01.log").write_text("!! old problem\n")
    h = D.health(tmp_path, "2026-11-17")
    daily = h["jobs"][0]
    assert daily["last"] == "2026-11-16" and daily["ok"] is False and h["jobs"][1]["last"] is None
    assert [p["line"] for p in h["problems"]] == ["!! upload failed"]


def test_page_renders_with_the_new_sections():
    data = D.build_data(live=False)
    h1 = data["hits"]["1m"]  # buys and avoids are scored apart and add up to the blended figure
    assert h1["buy"]["n"] + h1["avoid"]["n"] == h1["n"] and h1["buy"]["hits"] + h1["avoid"]["hits"] == h1["hits"]
    html = D.render(data)
    assert 'id="near"' not in html and html.index('id="risk"') > html.index('data-page="holdings"')
    for needle in ('data-page="overview"', 'id="att"', 'id="funnel"', 'id="score"', 'id="jobs"', "function setPage"):
        assert needle in html


def test_daily_html_shows_the_latest_run_and_folds_the_rest(tmp_path):
    assert D.daily_html(tmp_path) == ""
    (tmp_path / "2026-11-13.md").write_text("# old\n\n**Trades**\n- None.\n")
    (tmp_path / "2026-11-16.md").write_text("# Daily\n\n**Trades**\n- BUY A <b>\n\n**Watchlist**: quiet\n\n**Problems**: none.\n")
    h = D.daily_html(tmp_path)
    assert "2026-11-16" in h and "<li>BUY A &lt;b&gt;</li>" in h and "old" not in h
    top, rest = h.split("<details>")
    assert "Problems" in top and "Watchlist" in rest


def test_invested_tw_is_the_period_return_not_the_money_weighted_change():
    row = lambda val, inn, out, inc=0: {"core_usd": val, "tactical_usd": 0, "core_in": inn, "tactical_in": 0,  # noqa: E731
                                        "core_out": out, "tactical_out": 0, "core_income": inc, "tactical_income": 0}
    a, b = row(1000, 1000, 0), row(1100, 1000, 0)               # +10%, no flows
    assert D.invested_tw(b, a, 100.0) == pytest.approx(110.0)
    c = row(600, 1000, 500)                                     # sold 500 at the open, the rest fell 0%: 600 of 600
    assert D.invested_tw(c, b, 110.0) == pytest.approx(110.0)
    d = row(1200, 1600, 500)                                    # bought 600 at the open, all flat
    assert D.invested_tw(d, c, 110.0) == pytest.approx(110.0)
    assert D.invested_tw(a, None, None) is None
