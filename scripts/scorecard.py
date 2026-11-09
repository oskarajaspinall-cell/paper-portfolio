"""Conviction scorecard (owner-approved 2026-11-09). Python sets a CORE evaluation's conviction; the evaluator
only fills judgement fields. No model calls.

Why: the evaluator's conviction drifted with prompt wording (OKE: AVOID 3 on 2026-11-08, BUY 4 on 2026-11-09 from
the same fact sheet; 0 of ~70 at 4+ one day, 4 of 11 the next). Now:
- Python scores what can be measured, from the fact sheet's trends sidecar (research/<SLUG>/factsheet-<date>.json)
  and the fair-value file (research/<SLUG>/<date>-valuation.json):
    quality level      0-2  ROIC TTM (ROE for financials) vs [scorecard].quality_hi / quality_lo
    quality direction  0-2  ROIC/ROE, operating margin, FCF margin falling over the last 1 or 3 years (rolling 12m)
    balance sheet      0-2  net debt / EBITDA (financials: 1, neutral)
    valuation          0-4  upside to the value blend (reliable base fair value x fair_value_weight + the
                            evaluation's own expected 12-month value) + 1 if cheap against its own 5y P/E, EV/EBITDA
- The evaluator fills ONLY (Decision block "scorecard"):
    decline_cause  "structural" | "temporary" | "none"  (+1 direction point when temporary, with evidence;
                   required when Python finds a decline)
    decline_evidence  the cited reason
    moat           "none" | "narrow" | "wide"           0 / 1 / 2
    key_risk       "low" | "medium" | "high"            0 / -1 / -2
    key_risk_text  what it is
    veto           null or {"code": fraud_flag|binary_event|governance|data_conflict, "reason": "..."}: DOWNWARD only,
                   conviction becomes at most 3. There is no upward override.
- Total -> conviction by [scorecard].thresholds; plus a calibration offset from reports/calibration/latest.json
  only when its gate is met (scripts/calibration.py).

Usage: python scripts/scorecard.py research/<SLUG>/<date>-evaluation.md   -> the breakdown as JSON
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, load_config  # noqa: E402

CAUSES = ("structural", "temporary", "none")
MOATS = {"none": 0, "narrow": 1, "wide": 2}
RISKS = {"low": 0, "medium": -1, "high": -2}
VETO_CODES = ("fraud_flag", "binary_event", "governance", "data_conflict")
FINANCIAL_SECTORS = ("Financials",)
DIRECTION_METRICS = ("ROIC", "Operating margin", "FCF margin")


def settings(cfg: dict) -> dict:
    c = cfg.get("scorecard", {})
    return {"quality_hi": float(c.get("quality_hi", 15)), "quality_lo": float(c.get("quality_lo", 10)),
            "balance_good": float(c.get("balance_good", 1.5)), "balance_ok": float(c.get("balance_ok", 3.0)),
            "upside_bands": [float(x) for x in c.get("upside_bands", [30, 15, 5])],
            "cheap_history_pos": float(c.get("cheap_history_pos", 33)),
            "thresholds": {int(k): float(v) for k, v in (c.get("thresholds") or {"5": 11, "4": 9, "3": 5, "2": 3}).items()},
            "hold_4": float(c.get("hold_4", 8)),
            "fv_weight": float((cfg.get("funding_queue") or {}).get("fair_value_weight", 0.5))}


def expected_value(decision: dict) -> float | None:
    sc = decision.get("scenarios") or {}
    pts = [(float(v["probability"]), float(v["target_price_12m"])) for v in sc.values()
           if isinstance(v, dict) and v.get("probability") is not None and v.get("target_price_12m")]
    w = sum(p for p, _ in pts)
    return sum(p * t for p, t in pts) / w if pts and w > 0 else None


def calibration_offset(path: Path | None = None) -> float:
    """Applied only when scripts/calibration.py marked the gate met (enough resolved decisions)."""
    p = path or ROOT / "reports" / "calibration" / "latest.json"
    try:
        doc = json.loads(p.read_text())
    except (OSError, ValueError):
        return 0.0
    return float(doc.get("score_offset", 0.0)) if doc.get("gate_met") else 0.0


def score(decision: dict, trends: dict, valuation: dict | None, cfg: dict, offset: float = 0.0) -> dict:
    s = settings(cfg)
    j = decision.get("scorecard") or {}
    q, rec = trends.get("quality", {}), trends.get("recent", {})
    # banks and insurers have no ROIC / EBITDA on the site: ROE and a neutral balance sheet instead. A non-bank
    # "financial" with a ROIC (Edenred: negative equity, so no ROE) is scored like any other company.
    fin = (q.get("ROIC") or {}).get("ttm") is None
    parts, notes = {}, []

    # quality level
    key = "ROE" if fin else "ROIC"
    lvl = (q.get(key) or {}).get("ttm")
    parts["quality_level"] = 0 if lvl is None else (2 if lvl >= s["quality_hi"] else 1 if lvl >= s["quality_lo"] else 0)
    notes.append(f"{key} TTM {'n/a' if lvl is None else f'{lvl:.1f}%'}")

    # quality direction (Python decides what is falling; the evaluator only explains why)
    falling = []
    for m in (("ROE",) if fin else ("ROIC",)) + DIRECTION_METRICS[1:]:
        r = rec.get(m) or {}
        if r.get("direction") == "falling" or r.get("direction_3y") == "falling":
            falling.append(m)
    d = 2 if not falling else 1 if len(falling) == 1 else 0
    if falling and j.get("decline_cause") == "temporary" and str(j.get("decline_evidence", "")).strip():
        d = min(2, d + 1)
    parts["quality_direction"] = d
    notes.append("falling (1y or 3y): " + (", ".join(falling) if falling else "none"))

    # balance sheet
    nd = (q.get("Net debt / EBITDA (debt − cash & ST inv.)") or {}).get("ttm")
    if nd is None:
        parts["balance_sheet"] = 1
    else:
        parts["balance_sheet"] = 2 if nd <= s["balance_good"] else 1 if nd <= s["balance_ok"] else 0
    notes.append("net debt/EBITDA " + ("n/a" if nd is None else f"{nd:.2f}x"))

    # valuation: value blend vs the decision price, plus cheapness against the stock's own history
    price = decision.get("price_at_decision")
    ev = expected_value(decision)
    fv = None
    if valuation and (valuation.get("fair_value") or {}).get("base"):
        import valuation as V
        fv = valuation["fair_value"]["base"] if V.is_reliable(valuation) else None
        if fv is None:
            notes.append("base fair value unreliable: ignored")
    vals = [x for x in ((fv, s["fv_weight"]), (ev, 1 - s["fv_weight"])) if x[0]]
    blend = sum(v * w for v, w in vals) / sum(w for _, w in vals) if vals else None
    up = (blend / price - 1) * 100 if blend and price else None
    b30, b15, b5 = s["upside_bands"]
    v = 0 if up is None else (3 if up >= b30 else 2 if up >= b15 else 1 if up >= b5 else 0)
    pos = [x.get("pos_pct") for k, x in (trends.get("valuation") or {}).items()
           if k in ("P/E", "EV/EBITDA") and x.get("pos_pct") is not None]
    cheap_hist = bool(pos) and sorted(pos)[len(pos) // 2] <= s["cheap_history_pos"]
    parts["valuation"] = v + (1 if cheap_hist else 0)
    notes.append(f"value blend upside {'n/a' if up is None else f'{up:+.0f}%'}; own-history position "
                 + ("n/a" if not pos else "/".join(f"{x:.0f}%" for x in pos)))

    parts["moat"] = MOATS.get(j.get("moat"), 0)
    parts["key_risk"] = RISKS.get(j.get("key_risk"), -1)
    total = sum(parts.values()) + offset
    conv = 1
    for c in sorted(s["thresholds"], reverse=True):
        if total >= s["thresholds"][c]:
            conv = c
            break
    # a 4+ needs the mandate's basics: a decent business (quality >= 1), moving the right way or explained
    # (direction >= 1) and a real discount (valuation >= 2)
    gated = conv >= 4 and not (parts["quality_level"] >= 1 and parts["quality_direction"] >= 1 and parts["valuation"] >= 2)
    if gated:
        conv = 3
    # hold band (2026-11-09): an existing holding keeps conviction 4 from hold_4 points (no needless turnover), but
    # an ADD, like a new BUY, needs the full buy threshold
    held = decision.get("decision") in ("HOLD", "ADD", "TRIM")
    add_ok = conv >= 4
    if held and conv == 3 and not gated and total >= s["hold_4"]:
        conv = 4
    final = min(conv, 3) if isinstance(j.get("veto"), dict) and j["veto"].get("code") in VETO_CODES else conv
    return {"parts": parts, "offset": offset, "total": total, "conviction_score": conv, "conviction": final,
            "falling": falling, "upside_pct": up, "notes": notes, "vetoed": final < conv, "gated": gated,
            "add_allowed": add_ok and final >= 4}


def problems(decision: dict, result: dict) -> list[str]:
    """Judgement fields valid, and the Decision block's conviction equals the scorecard's."""
    j = decision.get("scorecard")
    if not isinstance(j, dict):
        return ["Decision block needs \"scorecard\": {decline_cause, decline_evidence, moat, key_risk, key_risk_text, "
                "veto} (judgement only; Python sets the conviction)"]
    errs = []
    if j.get("decline_cause") not in CAUSES:
        errs.append(f"scorecard.decline_cause must be one of {CAUSES}")
    if result["falling"] and j.get("decline_cause") == "none":
        errs.append("Python finds " + ", ".join(result["falling"]) + " falling: decline_cause must be structural or "
                    "temporary, with decline_evidence")
    if j.get("decline_cause") in ("structural", "temporary") and not str(j.get("decline_evidence", "")).strip():
        errs.append("scorecard.decline_evidence is required for a structural/temporary decline")
    if j.get("moat") not in MOATS:
        errs.append(f"scorecard.moat must be one of {tuple(MOATS)}")
    if j.get("key_risk") not in RISKS or not str(j.get("key_risk_text", "")).strip():
        errs.append(f"scorecard.key_risk must be one of {tuple(RISKS)} with key_risk_text")
    v = j.get("veto")
    if v is not None and not (isinstance(v, dict) and v.get("code") in VETO_CODES and str(v.get("reason", "")).strip()):
        errs.append(f"scorecard.veto must be null or {{code: one of {VETO_CODES}, reason}} (downward only)")
    if decision.get("decision") == "ADD" and not result["add_allowed"]:
        errs.append("ADD needs the full buy threshold (a holding inside the hold band keeps conviction 4 but is not "
                    "added to): decide HOLD")
    if decision.get("conviction") != result["conviction"]:
        errs.append(f"conviction must be {result['conviction']} (scorecard total {result['total']:g}: "
                    + ", ".join(f"{k} {v:g}" for k, v in result["parts"].items())
                    + (f", calibration offset {result['offset']:+g}" if result["offset"] else "")
                    + (", vetoed" if result["vetoed"] else "") + "). Python sets conviction; you may not override it. "
                    "BUY/ADD only at 4+.")
    return errs


def _latest(d: Path, pattern: str, on_or_before: str) -> Path | None:
    files = sorted(p for p in d.glob(pattern) if re.search(r"\d{4}-\d{2}-\d{2}", p.name)
                   and re.search(r"\d{4}-\d{2}-\d{2}", p.name).group(0) <= on_or_before)
    return files[-1] if files else None


def inputs_for(eval_path: Path) -> tuple[dict | None, dict | None]:
    """(trends, valuation) for an evaluation: the latest fact-sheet sidecar and valuation file on/before its date."""
    date = eval_path.name[:10]
    t = _latest(eval_path.parent, "factsheet-*.json", date)
    v = _latest(eval_path.parent, "20??-??-??-valuation.json", date)
    return (json.loads(t.read_text()) if t else None), (json.loads(v.read_text()) if v else None)


def evaluate_file(eval_path: Path, cfg: dict | None = None) -> tuple[dict | None, list[str]]:
    from check_docs import decision_block
    cfg = cfg or load_config()
    d, err = decision_block(eval_path.read_text())
    if err or not d:
        return None, [err or "no Decision block"]
    if d.get("position_type") != "CORE" or d.get("decision") == "SELL":
        return None, []
    trends, val = inputs_for(eval_path)
    if trends is None:
        return None, ["no fact-sheet trends file (factsheet-<date>.json): rebuild the fact sheet with "
                      "scripts/fact_sheet.py before evaluating"]
    res = score(d, trends, val, cfg, calibration_offset())
    return res, problems(d, res)


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print(__doc__)
        return 2
    res, errs = evaluate_file(Path(argv[0]))
    print(json.dumps({"result": res, "problems": errs}, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
