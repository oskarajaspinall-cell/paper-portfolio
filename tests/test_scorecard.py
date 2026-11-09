import scorecard as S

CFG = {"scorecard": {}, "funding_queue": {"fair_value_weight": 0.5}}


def trends(roic=20.0, falling=(), nd=1.0, pe_pos=20.0):
    rec = {m: {"direction": "falling" if m in falling else "flat", "direction_3y": "flat"}
           for m in ("ROIC", "Operating margin", "FCF margin")}
    return {"quality": {"ROIC": {"ttm": roic}, "Net debt / EBITDA (debt − cash & ST inv.)": {"ttm": nd}},
            "recent": rec, "valuation": {"P/E": {"pos_pct": pe_pos}, "EV/EBITDA": {"pos_pct": pe_pos}}}


def decision(ev=140.0, price=100.0, moat="narrow", risk="low", cause="none", veto=None, dec="BUY", conv=None):
    d = {"decision": dec, "position_type": "CORE", "price_at_decision": price,
         "scenarios": {"base": {"probability": 1.0, "target_price_12m": ev}},
         "scorecard": {"decline_cause": cause, "decline_evidence": "guided reset" if cause != "none" else "",
                       "moat": moat, "key_risk": risk, "key_risk_text": "x", "veto": veto}}
    if conv is not None:
        d["conviction"] = conv
    return d


VAL = {"price": 100.0, "fair_value": {"base": 150.0}, "methods": [{"status": "ok", "values": {"base": 140.0}},
                                                                   {"status": "ok", "values": {"base": 160.0}}]}


def test_strong_cheap_business_scores_4_plus_and_veto_only_lowers():
    r = S.score(decision(), trends(), VAL, CFG)
    assert r["conviction"] >= 4 and not r["vetoed"]
    v = S.score(decision(veto={"code": "governance", "reason": "x"}), trends(), VAL, CFG)
    assert v["conviction"] == 3 and v["vetoed"]


def test_gates_block_a_4_without_quality_or_discount():
    assert S.score(decision(), trends(roic=5.0), VAL, CFG)["conviction"] <= 3          # quality 0
    assert S.score(decision(ev=101), trends(), dict(VAL, fair_value={"base": 102}), CFG)["conviction"] <= 3  # no discount


def test_python_decides_falling_and_temporary_only_adds_one_point():
    t = trends(falling=("Operating margin", "FCF margin"))
    s = S.score(decision(cause="structural"), t, VAL, CFG)
    tmp = S.score(decision(cause="temporary"), t, VAL, CFG)
    assert s["parts"]["quality_direction"] == 0 and tmp["parts"]["quality_direction"] == 1
    assert any("must be structural or temporary" in e for e in S.problems(decision(cause="none", conv=1), s))


def test_unreliable_fair_value_is_ignored():
    wild = dict(VAL, fair_value={"base": 400.0}, methods=[{"status": "ok", "values": {"base": 400.0}}])
    r = S.score(decision(ev=110), trends(), wild, CFG)
    assert round(r["upside_pct"]) == 10 and "unreliable" in " ".join(r["notes"])


def test_hold_band_and_add_needs_buy_threshold():
    hold = decision(dec="HOLD", risk="medium", ev=115.0)
    r = S.score(hold, trends(), dict(VAL, fair_value={"base": 112.0}), {**CFG, "scorecard": {"hold_4": 6}})
    assert r["conviction"] == 4 and not r["add_allowed"]
    add = dict(hold, decision="ADD", conviction=4)
    assert any("ADD needs the full buy threshold" in e for e in S.problems(add, r))


def test_conviction_must_match_and_fields_are_closed_sets():
    r = S.score(decision(), trends(), VAL, CFG)
    errs = S.problems(decision(conv=r["conviction"] + 1 if r["conviction"] < 5 else 3, moat="huge"), r)
    assert any("conviction must be" in e for e in errs) and any("moat" in e for e in errs)


def test_invented_owner_rule_fails_real_ones_pass():
    from check_docs import owner_rule_problems
    assert owner_rule_problems("Good but not compelling: conviction 3, so AVOID under the owner rule.") == []
    errs = owner_rule_problems("Cheap, but the owner rule buys quality on a stable or improving trend.")
    assert errs and "doesn't exist" in errs[0]


def test_consistency_needs_new_evidence(tmp_path):
    import json
    from check_docs import consistency_problems
    old = {"decision": "AVOID", "conviction": 3, "price_at_decision": 85.0}
    (tmp_path / "2026-11-08-evaluation.md").write_text("x\n```json\n" + json.dumps(old) + "\n```\n")
    p = tmp_path / "2026-11-09-evaluation.md"
    new = {"decision": "BUY", "conviction": 4, "price_at_decision": 85.2}
    assert any("verdict differs" in e for e in consistency_problems(p, new))
    assert any("needs more than 10%" in e for e in consistency_problems(p, dict(new, new_evidence={"type": "price_move", "text": "fell"})))
    assert consistency_problems(p, dict(new, price_at_decision=70.0, new_evidence={"type": "price_move", "text": "fell 18%"})) == []
    assert any("cite the dated source" in e for e in consistency_problems(p, dict(new, new_evidence={"type": "guidance", "text": "raised"})))
    assert consistency_problems(p, dict(old)) == []          # same verdict: nothing to explain
    assert consistency_problems(p, dict(old, conviction=2)) == []   # same side of the buy line: method change, fine


def test_calibration_shrinks_and_gates():
    import calibration as C
    assert C.shrunk([10.0] * 10, 30) == 2.5          # 10 decisions barely move it
    assert round(C.shrunk([10.0] * 90, 30), 2) == 7.5
    assert C.shrunk([], 30) is None


def test_calibration_offset_only_when_gate_met(tmp_path):
    import json
    p = tmp_path / "latest.json"
    p.write_text(json.dumps({"gate_met": False, "score_offset": -1}))
    assert S.calibration_offset(p) == 0.0
    p.write_text(json.dumps({"gate_met": True, "score_offset": -1}))
    assert S.calibration_offset(p) == -1.0


def test_method_change_only_for_pre_scorecard_verdicts(tmp_path):
    import json
    from check_docs import consistency_problems
    (tmp_path / "2026-11-08-evaluation.md").write_text("x\n```json\n" + json.dumps({"decision": "BUY", "conviction": 4}) + "\n```\n")
    new = {"decision": "AVOID", "conviction": 3, "new_evidence": {"type": "method_change", "text": "scorecard"}}
    assert consistency_problems(tmp_path / "2026-11-09-evaluation.md", new) == []
    (tmp_path / "2026-11-10-evaluation.md").write_text("x\n```json\n" + json.dumps({"decision": "BUY", "conviction": 4}) + "\n```\n")
    assert consistency_problems(tmp_path / "2026-11-11-evaluation.md", new)
