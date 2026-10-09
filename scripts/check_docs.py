"""Check research notes and evaluations against their templates. No model calls.

Usage:
    python scripts/check_docs.py note research/AAPL/2026-10-06.md
    python scripts/check_docs.py eval research/AAPL/2026-10-06-evaluation.md [--state portfolio/state.json]

Word counts exclude URLs, markdown link targets, confidence tags and the Sources section.
Exit 0 = pass (prints word counts), exit 1 = fail (prints every problem).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, allowed_domains, core_trigger_problem, load_config  # noqa: E402

TAGS = ("[Certain]", "[Likely]", "[Guessing]")
BANNED_PHRASES = ("price target", "analyst target", "consensus target", "target price", "no consensus",
                  "needs more research", "need more research", "further research")

CORE = {"total": 700, "sections": [
    ("1. Business", 80), ("2. Quality", 150), ("3. Valuation", 150), ("4. What would prove this wrong", None),
    ("5. Capital allocation and cash conversion", 100), ("6. Unusual items", None)]}
TACTICAL = {"total": 400, "sections": [
    ("1. Catalyst and why now", 120), ("2. What the price already assumes", 100), ("3. Price setup", 80),
    ("4. Proposed exit plan", None), ("5. Quality red flags", 50)]}

NEW_DECISIONS = {"BUY", "AVOID"}
HELD_DECISIONS = {"ADD", "HOLD", "TRIM", "SELL"}


def words(text: str) -> int:
    t = re.sub(r"\[([^\]]*)\]\((https?://[^)]+)\)", r"\1", text)
    t = re.sub(r"https?://\S+", "", t)
    for tag in TAGS:
        t = t.replace(tag, "")
    t = re.sub(r"[|*_`#>-]+", " ", t)
    return len(re.findall(r"[A-Za-z0-9£$€%][^\s]*", t))


def sections(md: str) -> list[tuple[str, str]]:
    parts = re.split(r"^## +(.+?)\s*$", md, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]


def allowed_hosts() -> set[str]:
    return allowed_domains()


def mixed_tags(md: str) -> list[str]:
    """Tags like [Certain/Likely] or [likely] are not allowed: one exact tag per claim."""
    return [m for m in re.findall(r"\[[^\]]*\b(?:certain|likely|guessing)\b[^\]]*\]", md, re.I) if m not in TAGS]


def bad_urls(md: str, extra: set[str] | None = None) -> list[str]:
    """URLs not on the allowlist. `extra` = exact URLs listed in the stock's fact sheet (its news headlines),
    which may be cited even though their sites are not fetched."""
    doms = allowed_hosts()
    out = []
    for u in re.findall(r"https?://[^\s)\]>|]+", md):
        if extra and u.rstrip(".,;") in extra:
            continue
        h = (urlparse(u).hostname or "").lower()
        if not any(h == d or h.endswith("." + d) for d in doms):
            out.append(u)
    return out


def check_note(md: str, sheet_urls: set[str] | None = None) -> tuple[list[str], dict]:
    errs, counts = [], {}
    title = md.splitlines()[0] if md.strip() else ""
    if "Core initiation" in title:
        tpl, kind = CORE, "CORE"
    elif "Tactical initiation" in title:
        tpl, kind = TACTICAL, "TACTICAL"
    else:
        return ["title line must contain 'Core initiation' or 'Tactical initiation'"], {}
    counts["type"] = kind
    secs = [(h, b) for h, b in sections(md) if h.lower() != "sources"]
    want = [h for h, _ in tpl["sections"]]
    got = [h for h, _ in secs]
    if got != want:
        errs.append(f"sections must be exactly {want} in order (got {got})")
    body = dict(secs)
    total = 0
    for h, limit in tpl["sections"]:
        b = body.get(h, "")
        n = words(b)
        total += n
        counts[h.split(".")[0]] = n
        if limit and n > limit:
            errs.append(f"'{h}' has {n} words (limit {limit})")
        if not b.strip():
            errs.append(f"'{h}' is empty")
    counts["total"] = total
    if total > tpl["total"]:
        errs.append(f"total {total} words (limit {tpl['total']})")
    if kind == "CORE":
        items = re.findall(r"^\s*(?:[-*]|\d+\.)\s+\S", body.get("4. What would prove this wrong", ""), re.M)
        if not 2 <= len(items) <= 4:
            errs.append(f"'4. What would prove this wrong' needs 2-4 list items (got {len(items)})")
    else:
        plan = body.get("4. Proposed exit plan", "").lower()
        for k in ("target", "stop", "time limit"):
            if k not in plan:
                errs.append(f"'4. Proposed exit plan' must state the {k}")
    if not any(t in md for t in TAGS):
        errs.append("no [Certain]/[Likely]/[Guessing] tags found")
    errs += [f"mixed/invalid confidence tag {m}: use exactly one of {', '.join(TAGS)}" for m in mixed_tags(md)]
    low = md.lower()
    errs += [f"banned phrase '{p}'" for p in BANNED_PHRASES if p in low]
    if not re.search(r"^## +Sources\s*$", md, re.M) or not re.search(r"https://stockanalysis\.com/", md):
        errs.append("needs a '## Sources' section citing the fact sheet's stockanalysis.com URLs")
    errs += [f"URL not on allowlist: {u}" for u in bad_urls(md, sheet_urls)]
    return errs, counts


def decision_block(md: str) -> tuple[dict | None, str | None]:
    m = re.search(r"```json\s*(\{.*?\})\s*```\s*$", md.strip(), re.S)
    if not m:
        return None, "evaluation must END with the Decision ```json block"
    try:
        return json.loads(m.group(1)), None
    except json.JSONDecodeError as e:
        return None, f"Decision block is not valid JSON: {e}"


def scenario_problems(sc) -> list[str]:
    """bull/base/bear with probabilities summing to 1, ordered positive targets and a cited basis."""
    if not isinstance(sc, dict):
        return ["decision block needs 'scenarios' (bull/base/bear with probability, target_price_12m, basis)"]
    errs = []
    for k in ("bull", "base", "bear"):
        v = sc.get(k)
        if not isinstance(v, dict):
            errs.append(f"scenarios.{k} missing")
            continue
        p, t = v.get("probability"), v.get("target_price_12m")
        if not isinstance(p, (int, float)) or not 0 < p < 1:
            errs.append(f"scenarios.{k}.probability must be a number between 0 and 1")
        if not isinstance(t, (int, float)) or t <= 0:
            errs.append(f"scenarios.{k}.target_price_12m must be a positive number")
        if not str(v.get("basis", "")).strip():
            errs.append(f"scenarios.{k}.basis (the research finding it rests on) is missing")
    if errs:
        return errs
    total = sum(sc[k]["probability"] for k in ("bull", "base", "bear"))
    if abs(total - 1) > 1e-6:
        errs.append(f"scenario probabilities sum to {total:g}, not 1")
    if not sc["bear"]["target_price_12m"] <= sc["base"]["target_price_12m"] <= sc["bull"]["target_price_12m"]:
        errs.append("scenario targets must be ordered bear <= base <= bull")
    return errs


def check_eval(md: str, state: dict, cfg: dict) -> tuple[list[str], dict]:
    errs, counts = [], {}
    heads = [h for h, _ in sections(md)]
    if heads != ["Bear case", "Bull case", "Decision"]:
        errs.append(f"sections must be exactly ['Bear case', 'Bull case', 'Decision'] in order (got {heads})")
    body = dict(sections(md))
    for h in ("Bear case", "Bull case"):
        n = words(body.get(h, ""))
        counts[h] = n
        if n > 150:
            errs.append(f"'{h}' has {n} words (limit 150)")
        if not any(t in body.get(h, "") for t in TAGS):
            errs.append(f"'{h}' has no confidence tags")
    errs += [f"mixed/invalid confidence tag {m}: use exactly one of {', '.join(TAGS)}" for m in mixed_tags(md)]
    low = md.lower()
    errs += [f"banned phrase '{p}'" for p in BANNED_PHRASES if p in low]
    d, err = decision_block(md)
    if err:
        return errs + [err], counts
    held = state.get("holdings", {})
    t = d.get("ticker")
    dec = d.get("decision")
    counts["decision"] = dec
    allowed = HELD_DECISIONS if t in held else NEW_DECISIONS
    if dec not in allowed:
        errs.append(f"decision must be one of {sorted(allowed)} for {'a holding' if t in held else 'a new name'} (got {dec!r})")
    ptype = d.get("position_type")
    if ptype not in ("CORE", "TACTICAL"):
        errs.append("position_type must be CORE or TACTICAL")
    c = d.get("conviction")
    if not isinstance(c, int) or not 1 <= c <= 5:
        errs.append("conviction must be an integer 1-5")
    elif dec in ("BUY", "ADD") and c < cfg["core"].get("min_buy_conviction", 2):
        errs.append(f"BUY/ADD needs conviction >= {cfg['core'].get('min_buy_conviction', 2)} "
                    "(only high-conviction positions): decide AVOID (new name) or HOLD (holding) instead")
    if t in held and ptype and held[t]["type"] != ptype and not d.get("core_initiation"):
        errs.append(f"{t} is held as {held[t]['type']}; the label is fixed")
    for k in ("price_at_decision", "price_date", "research_note", "rationale"):
        if d.get(k) in (None, ""):
            errs.append(f"decision block missing '{k}'")
    if ptype == "CORE" and dec != "SELL":
        trig = d.get("triggers") or []
        if not 2 <= len(trig) <= 4 or not all(isinstance(x, dict) and x.get("text") for x in trig):
            errs.append("CORE decision needs 2-4 invalidation triggers, each {\"text\": ...}")
        for x in trig:
            prob = isinstance(x, dict) and core_trigger_problem(x)
            if prob:
                errs.append(f"CORE triggers must be thesis-only, not price-based ({prob}): {x.get('text', '')[:60]}")
    if ptype == "TACTICAL" and dec != "SELL":
        ep = d.get("exit_plan") or {}
        for k in ("target", "stop", "time_limit"):
            if ep.get(k) in (None, ""):
                errs.append(f"TACTICAL decision needs exit_plan.{k}")
        px = d.get("price_at_decision")
        if dec in ("BUY", "ADD") and isinstance(px, (int, float)) and all(
                isinstance(ep.get(k), (int, float)) for k in ("target", "stop")):
            mrr = cfg["tactical"]["min_reward_risk"]
            if not ep["stop"] < px < ep["target"]:
                errs.append(f"TACTICAL exit_plan needs stop < price_at_decision ({px}) < target")
            elif (ep["target"] - px) / (px - ep["stop"]) < mrr - 1e-9:
                errs.append(f"TACTICAL BUY needs reward:risk >= {mrr} from price_at_decision "
                            f"(now {(ep['target'] - px) / (px - ep['stop']):.2f})")
    errs += scenario_problems(d.get("scenarios"))
    errs += override_problems(d.get("valuation_overrides"))
    if dec == "BUY" and len(held) >= cfg["portfolio"]["max_holdings"] and not (d.get("replaces") and d.get("replacement_reason")):
        errs.append("portfolio is at max holdings: BUY must name 'replaces' and 'replacement_reason'")
    if d.get("replaces") and d["replaces"] not in held:
        errs.append(f"replaces {d['replaces']!r} is not a current holding")
    return errs, counts


OVERRIDE_FIELDS = {"dcf": ("growth", "margin"), "dcf_norm": ("growth", "margin"), "fcfe": ("growth", "margin"),
                   "pe": ("multiple",), "ev_ebitda": ("multiple",), "ev_revenue": ("multiple",), "p_ffo": ("multiple",),
                   "pb_roe": ("roe",), "ddm": ("growth",)}


def override_problems(ovs) -> list[str]:
    """Optional evaluator overrides of fair-value assumptions: each must cite why (owner rule)."""
    if ovs in (None, []):
        return []
    if not isinstance(ovs, list):
        return ["valuation_overrides must be a list"]
    errs = []
    for o in ovs:
        if not isinstance(o, dict):
            errs.append("each valuation_override must be an object"); continue
        m, sc, fld = o.get("method"), o.get("scenario"), o.get("field")
        if m not in OVERRIDE_FIELDS:
            errs.append(f"valuation_override method {m!r} must be one of {sorted(OVERRIDE_FIELDS)}")
        elif fld not in OVERRIDE_FIELDS[m]:
            errs.append(f"valuation_override field {fld!r} not valid for {m} (use {OVERRIDE_FIELDS[m]})")
        if sc not in ("bear", "base", "bull"):
            errs.append(f"valuation_override scenario {sc!r} must be bear, base or bull")
        if not isinstance(o.get("value"), (int, float)):
            errs.append("valuation_override value must be a number (rates as fractions, e.g. 0.06)")
        reason = str(o.get("reason") or "")
        if not re.search(r"\[[A-Z]{2}[^\]]*\]|https?://|research/", reason):
            errs.append("valuation_override reason must cite a source (a fact-sheet code like [IS], a URL or a research file)")
    return errs


MACRO_WEIGHTS = ("none", "context", "secondary", "primary")


def check_macro(md: str, cfg: dict) -> tuple[list[str], dict]:
    errs = []
    heads = [h for h, _ in sections(md)]
    if heads != ["Assessment", "Overlay"]:
        errs.append(f"sections must be exactly ['Assessment', 'Overlay'] (got {heads})")
    d, err = decision_block(md)
    if err:
        return errs + [err.replace("Decision", "Overlay")], {}
    w = d.get("macro_weight")
    counts = {"macro_weight": w, "words": words(dict(sections(md)).get("Assessment", ""))}
    if w not in MACRO_WEIGHTS:
        return errs + [f"macro_weight must be one of {MACRO_WEIGHTS}"], counts
    if not str(d.get("macro_basis", "")).strip():
        errs.append("macro_basis is required")
    if w in ("secondary", "primary"):
        for k in ("dominant_chain", "market_pricing", "macro_bull", "macro_bear"):
            if not str(d.get(k, "")).strip():
                errs.append(f"{k} is required for macro_weight {w}")
        t = d.get("macro_tilt") or {}
        if t.get("direction") not in ("toward bull", "toward bear", "neutral") or t.get("size") not in ("small", "moderate", "large") \
                or not str(t.get("reason", "")).strip():
            errs.append("macro_tilt needs direction (toward bull|toward bear|neutral), size (small|moderate|large) and reason")
        trig = d.get("refresh_triggers") or []
        if not 2 <= len(trig) <= 4 or not all(isinstance(x, dict) and x.get("text") for x in trig):
            errs.append("2-4 refresh_triggers are required, each {\"text\": ...}")
        for x in trig:
            c = (x or {}).get("check")
            if c and not (c.get("source") == "fred" and c.get("series") and c.get("op") in ("<", ">")
                          and isinstance(c.get("value"), (int, float))):
                errs.append(f"trigger check must be {{source: fred, series, op: < or >, value}}: {x.get('text', '')[:50]}")
        if not d.get("sources"):
            errs.append("sources (URL + date for every figure) are required")
        if counts["words"] > 250:
            errs.append(f"Assessment has {counts['words']} words (limit 250)")
    elif counts["words"] > 80:
        errs.append(f"a {w} assessment should be ~2 sentences (got {counts['words']} words)")
    official = {d_.lower() for d_ in cfg.get("macro", {}).get("official_sources", [])}
    for u in re.findall(r"https?://[^\s)\]>|\"]+", md):
        h = (urlparse(u).hostname or "").lower()
        if not any(h == x or h.endswith("." + x) for x in official | allowed_hosts()):
            errs.append(f"URL not on the allowlist or official macro sources: {u}")
    errs += [f"banned phrase '{p_}'" for p_ in ("price target", "target price", "analyst target") if p_ in md.lower()]
    return errs, counts


def check_regime_view(md: str, score_doc: dict, cfg: dict) -> tuple[list[str], dict]:
    """The macro-strategist's view: valid regime, at most `notch_override` from the score, and any move
    backed by >= 2 reasons cited to official sources ([macro].official_sources)."""
    import regime as R
    errs = []
    try:
        v = R.view_from_md(md)
    except (ValueError, json.JSONDecodeError) as e:
        return [f"view: {e}"], {}
    fr = v.get("final_regime")
    if fr not in R.REGIMES:
        return [f"final_regime must be one of {R.REGIMES}"], {}
    i, j = R.REGIMES.index(score_doc["score_regime"]), R.REGIMES.index(fr)
    if abs(i - j) > cfg["cash_strategy"]["notch_override"]:
        errs.append(f"final_regime {fr} is {abs(i - j)} notches from the score's {score_doc['score_regime']} "
                    f"(max {cfg['cash_strategy']['notch_override']})")
    reasons = v.get("reasons") or []
    if not isinstance(reasons, list) or not all(isinstance(r, dict) and r.get("text") for r in reasons):
        errs.append("reasons must be a list of {text, source}")
        reasons = []
    if fr != score_doc["score_regime"]:
        official = {d.lower() for d in cfg.get("macro", {}).get("official_sources", [])}
        cited = [r for r in reasons if any(d in (r.get("source") or "").lower() for d in official)]
        if len(cited) < 2:
            errs.append(f"moving the regime needs >= 2 reasons cited to official sources ({', '.join(sorted(official))})")
    if bool(v.get("keep_score")) != (fr == score_doc["score_regime"]):
        errs.append("keep_score must be true exactly when final_regime equals the score's regime")
    words = len(re.sub(r"```json.*```", "", md, flags=re.S).split())
    if words > 220:
        errs.append(f"view text has {words} words (max ~150 + heading)")
    return errs, {"final_regime": fr, "score_regime": score_doc["score_regime"], "reasons": len(reasons)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["note", "eval", "macro", "regime"])
    ap.add_argument("path")
    ap.add_argument("--state", default=str(ROOT / "portfolio" / "state.json"))
    a = ap.parse_args(argv)
    md = Path(a.path).read_text()
    if a.kind == "note":
        path = Path(a.path)
        sheets = sorted(path.parent.glob("factsheet-*.md"))
        sheet_urls = set(re.findall(r"https?://[^\s)\]>|]+", sheets[-1].read_text())) if sheets else set()
        errs, counts = check_note(md, {u.rstrip(".,;") for u in sheet_urls})
    elif a.kind == "macro":
        errs, counts = check_macro(md, load_config())
    elif a.kind == "regime":  # reports/regime/<date>-view.md, checked against reports/regime/<date>.json
        p = Path(a.path)
        score = json.loads(p.with_name(p.name.replace("-view.md", ".json")).read_text())
        errs, counts = check_regime_view(md, score, load_config())
    else:
        errs, counts = check_eval(md, json.loads(Path(a.state).read_text()), load_config())
    if errs:
        print(f"FAIL {a.path}\n" + "\n".join(f"- {e}" for e in errs))
        return 1
    print(f"OK {a.path} " + " ".join(f"{k}={v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
