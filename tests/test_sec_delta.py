import json

import pytest

import sec_delta as S

RISK_OLD = ["Competition in our markets is intense and could reduce our revenue and margins over time.",
            "We depend on a small number of suppliers for key components, and a disruption could hurt production.",
            "Revenue grew 12% to $4.1 billion in fiscal 2025, driven by subscription growth across all regions."]
RISK_NEW = ["Competition in our markets is intense and could reduce our revenue and margins over time.",
            "We depend on a single supplier for key components, and any disruption could halt production entirely.",
            "Revenue grew 9% to $4.5 billion in fiscal 2026, driven by subscription growth across all regions.",
            "We are subject to a new antitrust investigation by the European Commission into our bundling practices."]


def doc(risk, mdna):
    toc = "<p>Item 1A. Risk Factors</p><p>Item 1B. Unresolved Staff Comments</p><p>Item 7. Management's Discussion</p>"
    body = ("<p>Item 1A. Risk Factors</p>" + "".join(f"<p>{x}</p>" for x in risk)
            + "<p>Item 1B. Unresolved Staff Comments</p><p>None.</p>"
            + "<p>Item 7. Management&#8217;s Discussion and Analysis</p>" + "".join(f"<div>{x}</div>" for x in mdna)
            + "<p>Item 8. Financial Statements</p>")
    return f"<html><body>{toc}{body}</body></html>"


def test_section_skips_table_of_contents():
    ls = S.lines(doc(RISK_OLD, ["Our margins benefited from lower freight costs and a favourable product mix this year."]))
    assert S.section(ls, S.SECTIONS["10-K"][0][1]) == RISK_OLD
    assert len(S.section(ls, S.SECTIONS["10-K"][1][1])) == 1


def test_diff_drops_figure_only_edits_and_keeps_real_changes():
    d = S.diff(RISK_OLD, RISK_NEW)
    assert d["added"] == [RISK_NEW[3]]
    assert d["removed"] == []
    assert d["changed"] == [(RISK_OLD[1], RISK_NEW[1])]     # the revenue paragraph changed only its numbers


def test_moved_paragraph_is_not_a_change():
    d = S.diff(RISK_OLD, [RISK_OLD[1], RISK_OLD[0], RISK_OLD[2]])
    assert d == {"added": [], "removed": [], "changed": []}


def test_pick_filings_10k_vs_previous_10k_and_10q_vs_year_ago_quarter():
    def recent(*rows):
        keys = ["form", "filingDate", "reportDate", "accessionNumber", "primaryDocument"]
        return {k: [r[i] for r in rows] for i, k in enumerate(keys)}
    k = recent(("10-K", "2026-02-01", "2025-12-31", "a", "x.htm"), ("10-Q", "2025-11-01", "2025-09-30", "b", "x.htm"),
               ("10-K", "2025-02-01", "2024-12-31", "c", "x.htm"))
    assert [f["accessionNumber"] for f in S.pick_filings(k)] == ["a", "c"]
    q = recent(("10-Q", "2026-08-01", "2026-06-30", "a", "x"), ("10-Q", "2026-05-01", "2026-03-31", "b", "x"),
               ("10-K", "2026-02-01", "2025-12-31", "c", "x"), ("10-Q", "2025-08-01", "2025-06-30", "d", "x"))
    assert [f["accessionNumber"] for f in S.pick_filings(q)] == ["a", "d"]
    assert S.pick_filings(recent(("10-Q", "2026-08-01", "2026-06-30", "a", "x"))) is None


def test_off_without_contact_and_non_us_skipped(cfg):
    assert S.run("AAPL", "2026-10-16", cfg, who="")[0].startswith("SKIP sec step off")
    assert "not a US listing" in S.run("LON:SHEL", "2026-10-16", cfg, fetcher=object(), who="owner@example.com")[0]


def test_contact_from_environment_or_env_file(tmp_path, monkeypatch):
    f = tmp_path / ".env"
    f.write_text("OTHER=1\nSEC_CONTACT='owner@example.com'\n")
    monkeypatch.delenv("SEC_CONTACT", raising=False)
    assert S.contact(f) == "owner@example.com"
    monkeypatch.setenv("SEC_CONTACT", "env@example.com")
    assert S.contact(f) == "env@example.com"


def test_run_writes_delta_with_urls_and_word_cap(cfg, tmp_path, monkeypatch):
    cfg["sec"] = {"max_words": 2000}
    sub = {"filings": {"recent": {"form": ["10-K", "10-K"], "filingDate": ["2026-02-01", "2025-02-01"],
                                  "reportDate": ["2025-12-31", "2024-12-31"], "accessionNumber": ["0001-26-1", "0001-25-1"],
                                  "primaryDocument": ["new.htm", "old.htm"]}}}
    mdna = ["Gross margin improved on lower freight costs and a richer mix of subscription revenue this year."]
    pages = {S.TICKERS_URL: json.dumps({"0": {"cik_str": 320193, "ticker": "AAPL"}}),
             "https://data.sec.gov/submissions/CIK0000320193.json": json.dumps(sub),
             "https://www.sec.gov/Archives/edgar/data/320193/0001261/new.htm": doc(RISK_NEW, mdna),
             "https://www.sec.gov/Archives/edgar/data/320193/0001251/old.htm": doc(RISK_OLD, mdna)}

    class F:
        def get(self, url):
            return pages[url]
    monkeypatch.setattr(S, "ROOT", tmp_path)
    msg, path = S.run("AAPL", "2026-10-16", cfg, F(), who="owner@example.com")
    md = path.read_text()
    assert msg.startswith("OK") and "European Commission" in md and "WAS:" in md
    assert "new.htm" in md and "old.htm" in md and "## MD&A\nNo substantive change." in md
    assert "fiscal 2026" not in md                      # figure-only edit left out
    cfg["sec"]["max_words"] = 20
    md = S.run("AAPL", "2026-10-16", cfg, F(), who="owner@example.com")[1].read_text()
    assert "not shown (word cap 20)" in md


def test_fetcher_refuses_without_contact(cfg):
    with pytest.raises(S.DataError):
        S.SecFetcher(cfg, who=" ")


def test_item_label_and_title_on_separate_lines():
    ls = S.lines("<p>ITEM 1A.</p><p>RISK FACTORS</p>" + "".join(f"<p>{r}</p>" for r in RISK_OLD) + "<p>ITEM 1B.</p><p>X</p>")
    assert S.section(ls, S.SECTIONS["10-K"][0][1]) == RISK_OLD


def test_table_rows_are_not_paragraphs():
    ls = S.lines("<p>Item 7. Management's Discussion and Analysis</p>"
                 "<p>Research and development$11,729 $8,866 32%$34,035 $25,684 33%</p>"
                 f"<p>{RISK_OLD[0]}</p><p>Item 8. Financial Statements</p>")
    assert S.section(ls, S.SECTIONS["10-K"][1][1]) == [RISK_OLD[0]]
