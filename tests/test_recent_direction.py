import fact_sheet as FS


def test_recent_direction_compares_a_year_back_and_finds_the_high(monkeypatch):
    dates = ["2024-12-31", "2025-03-31", "2025-06-30", "2025-09-30", "2025-12-31", "2026-03-31", "2026-06-30"]
    roic = [0.15, 0.17, 0.19, 0.203, 0.19, 0.188, 0.185]
    pages = {
        "ratios": {"roic": roic, "roce": [0.2] * 7},
        "income": {"opinc": [34] * 6 + [29.6], "revenue": [100] * 7},
        "cash-flow": {"fcf": [30] * 7},
    }

    class F:
        def html(self, url):
            return url

    def parse(nodes, url):
        key = next(k for k in pages if k in url)
        return {"periods": ["TTM"] + dates[::-1], "rows": {k: [v[-1]] + v[::-1] for k, v in pages[key].items()}}

    monkeypatch.setattr("fetch_data.page_nodes", lambda html, url: [])
    monkeypatch.setattr("fetch_data.parse_statement", parse)
    rows, src = FS.recent_direction(F(), "EPA:EDEN")
    r = {x["label"]: x for x in rows}
    assert round(r["ROIC"]["prior"], 1) == 19.0 and r["ROIC"]["prior_date"] == "2025-06-30"
    assert r["ROIC"]["high_date"] == "2025-09-30" and r["ROIC"]["direction"] == "flat"
    assert r["Operating margin"]["direction"] == "falling" and round(r["Operating margin"]["change"], 1) == -4.4
    assert set(src) == {"RA-T", "IS-T", "CF-T"} and all(u.endswith("?p=trailing") for u in src.values())
