import json

import pytest

from allowlist_hook import is_allowed
from check_docs import check_eval, check_note, words

SRC = "## Sources\n- https://stockanalysis.com/stocks/aapl/\n- https://www.sec.gov/x\n"


def core_note(**over):
    secs = {"1. Business": "Sells phones and services. [Certain]",
            "2. Quality": "High returns on capital. [Likely]",
            "3. Valuation": "Price assumes steady growth. [Guessing]",
            "4. What would prove this wrong": "- Gross margin below 44%\n- ROIC below 50%",
            "5. Capital allocation and cash conversion": "Buybacks. [Certain]",
            "6. Unusual items": "None"}
    secs.update(over)
    body = "".join(f"## {h}\n{b}\n" for h, b in secs.items())
    return f"# Apple (AAPL) — Core initiation — 2026-10-06\n{body}{SRC}"


def tac_note(plan="Target 4,000p; stop 3,270p; time limit 2026-12-31."):
    secs = {"1. Catalyst and why now": "Q3 results 2026-10-29. [Certain]",
            "2. What the price already assumes": "Flat margins. [Likely]",
            "3. Price setup": "Above 200-day. [Certain]",
            "4. Proposed exit plan": plan, "5. Quality red flags": "None"}
    return "# Shell (LON:SHEL) — Tactical initiation — 2026-10-06\n" + \
        "".join(f"## {h}\n{b}\n" for h, b in secs.items()) + SRC


def test_word_count_excludes_urls_and_tags():
    assert words("Margins rose [Certain] (source: https://stockanalysis.com/x) to 48%") == 5


def test_good_notes_pass():
    errs, counts = check_note(core_note())
    assert errs == [] and counts["type"] == "CORE"
    errs, counts = check_note(tac_note())
    assert errs == [] and counts["type"] == "TACTICAL"


def test_note_word_limit():
    errs, _ = check_note(core_note(**{"1. Business": "word " * 81 + "[Certain]"}))
    assert any("'1. Business' has 81 words" in e for e in errs)


def test_note_total_limit():
    long = "word " * 140 + "[Likely]"
    errs, _ = check_note(core_note(**{"2. Quality": long, "3. Valuation": long, "1. Business": "w " * 80,
                                      "5. Capital allocation and cash conversion": "w " * 100,
                                      "6. Unusual items": "w " * 300}))
    assert any(e.startswith("total") for e in errs)


def test_note_section_order_and_triggers():
    md = core_note().replace("## 2. Quality", "## 2. Moat")
    assert any("sections must be exactly" in e for e in check_note(md)[0])
    errs, _ = check_note(core_note(**{"4. What would prove this wrong": "- only one"}))
    assert any("2-4 list items" in e for e in errs)


def test_tactical_exit_plan_complete():
    errs, _ = check_note(tac_note(plan="Target 4,000p."))
    assert any("stop" in e for e in errs) and any("time limit" in e for e in errs)


def test_note_rejects_targets_and_bad_urls():
    md = core_note(**{"3. Valuation": "The analyst price target is high. [Guessing]"})
    assert any("price target" in e for e in check_note(md)[0])
    md = core_note() + "- https://www.bloomberg.com/news\n"
    assert any("bloomberg" in e for e in check_note(md)[0])


STATE = {"holdings": {"MSFT": {"type": "CORE"}, "LON:SHEL": {"type": "TACTICAL"}}}


def evaluation(decision, bear="Too expensive. [Likely]", bull="Great business. [Certain]", order=None):
    secs = order or ["Bear case", "Bull case"]
    body = {"Bear case": bear, "Bull case": bull}
    d = {"ticker": "AAPL", "decision": "BUY", "position_type": "CORE", "conviction": 3, "thesis": "x",
         "rationale": "y", "price_at_decision": 332.89, "price_date": "2026-10-05",
         "research_note": "research/AAPL/2026-10-06.md", "triggers": [{"text": "a"}, {"text": "b"}]}
    d.update(decision)
    return "# Evaluation\n" + "".join(f"## {h}\n{body[h]}\n" for h in secs) + \
        "## Decision\n```json\n" + json.dumps(d) + "\n```\n"


@pytest.fixture
def cfgd(cfg):
    return cfg


def test_good_eval_passes(cfgd):
    errs, counts = check_eval(evaluation({}), STATE, cfgd)
    assert errs == [] and counts["decision"] == "BUY"


def test_bull_before_bear_fails(cfgd):
    errs, _ = check_eval(evaluation({}, order=["Bull case", "Bear case"]), STATE, cfgd)
    assert any("in order" in e for e in errs)


@pytest.mark.parametrize("dec,ticker,ok", [("BUY", "AAPL", True), ("AVOID", "AAPL", True), ("HOLD", "AAPL", False),
                                           ("NO CONSENSUS", "AAPL", False), ("HOLD", "MSFT", True),
                                           ("BUY", "MSFT", False), ("SELL", "MSFT", True)])
def test_allowed_decisions(cfgd, dec, ticker, ok):
    errs, _ = check_eval(evaluation({"decision": dec, "ticker": ticker}), STATE, cfgd)
    assert (errs == []) == ok, errs


def test_eval_requires_triggers_or_exit_plan(cfgd):
    assert any("triggers" in e for e in check_eval(evaluation({"triggers": [{"text": "a"}]}), STATE, cfgd)[0])
    tac = {"position_type": "TACTICAL", "triggers": None, "exit_plan": {"target": 4000, "stop": 3270}}
    assert any("time_limit" in e for e in check_eval(evaluation(tac), STATE, cfgd)[0])
    tac["exit_plan"]["time_limit"] = "2026-12-31"
    assert check_eval(evaluation(tac), STATE, cfgd)[0] == []


def test_eval_word_limit_and_end_block(cfgd):
    errs, _ = check_eval(evaluation({}, bear="w " * 151 + "[Likely]"), STATE, cfgd)
    assert any("'Bear case' has 151 words" in e for e in errs)
    errs, _ = check_eval(evaluation({}) + "\nTrailing text", STATE, cfgd)
    assert any("must END" in e for e in errs)


def test_replacement_named_when_full(cfgd):
    full = {"holdings": {f"X{i}": {"type": "CORE"} for i in range(15)}}
    assert any("replaces" in e for e in check_eval(evaluation({}), full, cfgd)[0])
    ok = evaluation({"replaces": "X3", "replacement_reason": "better ROIC, cheaper"})
    assert check_eval(ok, full, cfgd)[0] == []


@pytest.mark.parametrize("url,ok", [("https://www.sec.gov/cgi-bin/x", True), ("https://investor.apple.com/", True),
                                    ("https://stockanalysis.com/stocks/aapl/", True),
                                    ("https://www.bloomberg.com/", False), ("https://sec.gov.evil.com/", False),
                                    ("ftp://sec.gov/", False)])
def test_allowlist(url, ok):
    assert is_allowed(url, {"sec.gov", "stockanalysis.com", "investor.apple.com"}) == ok


def test_mixed_tags_rejected():
    md = core_note(**{"2. Quality": "High returns. [Certain/Likely]"})
    assert any("mixed/invalid confidence tag [Certain/Likely]" in e for e in check_note(md)[0])
    assert any("[likely]" in e for e in check_note(core_note(**{"2. Quality": "x [likely]"}))[0])


def test_avoid_still_needs_triggers_or_exit_plan(cfgd):
    assert any("triggers" in e for e in check_eval(evaluation({"decision": "AVOID", "triggers": None}), STATE, cfgd)[0])
    tac = {"decision": "AVOID", "position_type": "TACTICAL", "conviction": 1, "triggers": None}
    assert any("exit_plan" in e for e in check_eval(evaluation(tac), STATE, cfgd)[0])
    assert check_eval(evaluation({"decision": "SELL", "ticker": "MSFT", "triggers": None}), STATE, cfgd)[0] == []


def test_eval_rejects_price_triggers_on_core(cfgd):
    bad = {"triggers": [{"text": "ROIC below 50%"},
                        {"text": "x", "check": {"source": "price", "field": "close", "op": "<", "value": 289.75}}]}
    assert any("thesis-only" in e for e in check_eval(evaluation(bad), STATE, cfgd)[0])
