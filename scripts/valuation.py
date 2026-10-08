"""Industry-appropriate fair value (owner rule 2026-10-08): inform-only; never a buy rule.

    python scripts/valuation.py TICKER [--asof D] [--eval research/<SLUG>/<D>-evaluation.md]
        -> research/<SLUG>/<D>-valuation.json and .md

Method per industry from valuation/industry_methods.csv (the owner's 145-industry table: best and 2nd-best
method). Company figures come ONLY from the stockanalysis.com pages the fact sheet already reads
(income statement, balance sheet, cash flow, ratios, statistics, overview); the risk-free rate is FRED's
10-year Treasury (macro exception). Analyst targets, forward estimates and stockanalysis.com's own
calculators are never used: the DCF and EPS x P/E maths are replicated here.

Assumptions are mechanical, from the stock's own history (bear / base / bull), and the evaluator may
override one with a cited reason (`valuation_overrides` in its Decision block). Models:
- dcf / dcf_norm: FCFF (FCF - stock-based pay + after-tax interest paid - after-tax interest earned)
  margin (financials: net income at the cost of equity, no net cash: their cash flow is distorted) x revenue path; growth starts at the scenario
  rate in year 1 and fades linearly to terminal growth by `explicit_years`; discounted at WACC (CAPM cost of equity,
  after-tax cost of debt); EV + net cash, per diluted share. dcf_norm (through-cycle) uses the 5y median
  margin as the base. Scenarios (growth mean-reverts): base = halfway between the 3y/5y average revenue
  CAGR and terminal growth, TTM margin (dcf) or 5y median (dcf_norm); bear = halfway between the weaker
  CAGR and terminal, minus `bear_growth_haircut`, lowest margin; bull = the stronger CAGR (capped),
  highest margin. Reverse DCF: the growth the price implies at the base margin.
- fcfe: the same path on levered FCF, discounted at the cost of equity, no net cash added.
- pe: TTM diluted EPS x own 5y min/median/max P/E (the stockanalysis Fair Value calculator's maths).
- pb_roe: BVPS x (ROE - g)/(ke - g) with ROE at the 5y min/median/max (capped).
- ev_ebitda, ev_revenue: TTM figure x own 5y min/median/max multiple, + net cash, per share.
- ddm: Gordon growth on the dividend per share.
- p_ffo: FFO proxy (net income + D&A, NOT AFFO) x own 5y P/FFO range (REITs).
- cash_ps: cash and investments per share (shells).
- nav, rnpv, sotp, pipeline: need inputs stockanalysis.com doesn't show -> [data unavailable].
Negative earnings/EBITDA/cash flow -> "n/m" (never forced). Per-share values convert from the financials'
currency to the quote currency with stockanalysis.com's implied FX.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import statistics as stats
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, Ticker, load_config  # noqa: E402

TABLE = ROOT / "valuation" / "industry_methods.csv"
SCEN = ("bear", "base", "bull")
UNAVAILABLE = {"nav": "reserve, mine or asset-level values", "rnpv": "pipeline success probabilities and peak sales",
               "sotp": "segment-level profits", "pipeline": "pipeline asset values"}
LABEL = {"dcf": "DCF", "dcf_norm": "through-cycle DCF", "fcfe": "FCFE DCF", "pe": "P/E", "pb_roe": "P/B + ROE",
         "ev_ebitda": "EV/EBITDA", "ev_revenue": "EV/Revenue", "ddm": "dividend discount", "p_ffo": "P/FFO (proxy)",
         "cash_ps": "cash per share", "nav": "NAV", "rnpv": "rNPV", "sotp": "sum of the parts", "pipeline": "pipeline value"}
# phrases in the owner's table -> model, longest first so "ev/ebitdax" wins over "ev/ebitda"
TOKENS = [(r"probability-adjusted dcf|rnpv", "rnpv"), (r"pipeline value", "pipeline"),
          (r"through-cycle dcf|normali[sz]ed dcf|commodity-cycle dcf", "dcf_norm"),
          (r"reserve nav|mine nav|liquidation value|asset value|\bnav\b", "nav"), (r"sotp", "sotp"),
          (r"p/affo", "p_ffo"), (r"p/b", "pb_roe"), (r"p/e|normali[sz]ed earnings", "pe"),
          (r"ev/ebitdax|ev/ebitda", "ev_ebitda"), (r"ev/revenue|ev/sales", "ev_revenue"),
          (r"dividend|ddm", "ddm"), (r"fcfe", "fcfe"), (r"cash \+ investments", "cash_ps"), (r"\bdcf\b", "dcf")]
_TOKEN_RE = re.compile("|".join(f"(?P<g{i}>{p})" for i, (p, _) in enumerate(TOKENS)), re.I)


def methods_in(cell: str) -> list[str]:
    """Models named in one cell of the owner's table, in order of appearance."""
    out = []
    for m in _TOKEN_RE.finditer(cell or ""):
        model = TOKENS[int(m.lastgroup[1:])][1]
        if model not in out:
            out.append(model)
    return out


def industry_methods(industry: str | None, path: Path = TABLE) -> dict:
    with path.open() as fh:
        rows = {r["industry"].strip().lower(): r for r in csv.DictReader(fh)}
    r = rows.get((industry or "").strip().lower())
    if not r:
        return {"industry": industry, "known": False, "best": "DCF", "second": "EV/EBITDA",
                "best_models": ["dcf"], "second_models": ["ev_ebitda"], "stockanalysis": ""}
    return {"industry": r["industry"], "known": True, "best": r["best"], "second": r["second"],
            "best_models": methods_in(r["best"]), "second_models": methods_in(r["second"]),
            "stockanalysis": r.get("stockanalysis", "")}


# --------------------------------------------------------------------------- inputs
def _series(sec: dict, key: str) -> tuple[float | None, list[float]]:
    """(TTM, fiscal years newest -> oldest) for one statement row; missing -> None / skipped."""
    per, vals = sec["periods"], sec["rows"].get(key) or []
    vals = list(vals) + [None] * (len(per) - len(vals))
    ttm = vals[per.index("TTM")] if "TTM" in per else None
    fy = [v for p, v in zip(per, vals) if p != "TTM"]
    return ttm, fy


def _num(v):
    return v if isinstance(v, (int, float)) else None


def inputs_from_sections(sec: dict, price: float, rf_pct: float, fx_fin_to_quote: float | None) -> dict:
    """Flatten the fact sheet's sections into valuation inputs (financials' currency unless noted)."""
    I, B, C, R, S = (sec[k]["data"] for k in ("income", "balance", "cashflow", "ratios", "statistics"))
    sv = lambda k: _num((S.get(k) or {}).get("value"))  # noqa: E731
    g = {}
    for name, (src, key) in {"revenue": (I, "revenue"), "fcf": (C, "fcf"), "netinc": (I, "netinc"),
                             "eps": (I, "epsdil"), "ebitda": (I, "ebitda"), "shares": (I, "sharesDiluted"),
                             "interest": (I, "interestExpense"), "int_income": (I, "interestIncome"),
                             "taxrate": (I, "taxrate"), "sbc": (C, "sbcomp"), "da": (C, "totalDepAmorCF"),
                             "netcash": (B, "netcash"), "debt": (B, "debt"), "bvps": (B, "bvps"),
                             "cash": (B, "totalcash"), "shares_out": (B, "sharesOutTotalCommon"),
                             "pe": (R, "pe"), "evebitda": (R, "evebitda"), "evrevenue": (R, "evrevenue"),
                             "roe": (R, "roe")}.items():
        g[name] = _series(src, key)
    return {"g": g, "price": price, "rf": rf_pct / 100, "beta": sv("beta"), "dps": sv("dps"),
            "financial": (sec.get("overview", {}).get("data", {}).get("sector") or "") == "Financials",
            "marketcap_quote": sv("marketcap"), "fx": fx_fin_to_quote,
            "fin_ccy": I.get("currency"), "sources": {k: sec[k]["source_url"] for k in
                                                     ("income", "balance", "cashflow", "ratios", "statistics")}}


# --------------------------------------------------------------------------- building blocks
def cagr(new, old, years):
    if not new or not old or new <= 0 or old <= 0:
        return None
    return (new / old) ** (1 / years) - 1


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def cost_of_equity(rf: float, beta: float | None, vc: dict) -> float:
    lo, hi = vc["beta_clamp"]
    return rf + clamp(beta if beta is not None else 1.0, lo, hi) * vc["erp"] / 100


def wacc(inp: dict, ke: float, vc: dict) -> float:
    g = inp["g"]
    debt = g["debt"][0] or 0.0
    fx = inp["fx"] or 1.0
    equity = (inp["marketcap_quote"] or 0.0) / fx  # market cap in the financials' currency
    tax = clamp(g["taxrate"][0] if g["taxrate"][0] is not None else 0.21, 0.0, 0.35)
    rf = inp["rf"]
    kd = clamp(abs(g["interest"][0] or 0.0) / debt, rf, rf + 0.06) if debt > 0 else rf
    w = equity / (equity + debt) if equity + debt > 0 else 1.0
    return max(w * ke + (1 - w) * kd * (1 - tax), vc["terminal_growth"] / 100 + 0.03)


def dcf_per_share(rev0: float, margin: float, growth: float, rate: float, vc: dict, net_cash: float,
                  shares: float) -> float:
    """Revenue grows at `growth` in year 1, fading linearly to terminal growth by explicit_years (growth
    mean-reverts; holding a strong past rate for years overstates value); cash flow = margin x revenue;
    Gordon terminal value; + net cash; per share."""
    n, gt = int(vc["explicit_years"]), vc["terminal_growth"] / 100
    rev, pv, cf = rev0, 0.0, 0.0
    for y in range(1, n + 1):
        gy = growth + (gt - growth) * (y - 1) / (n - 1)
        rev *= 1 + gy
        cf = rev * margin
        pv += cf / (1 + rate) ** y
    pv += cf * (1 + gt) / (rate - gt) / (1 + rate) ** n
    return (pv + net_cash) / shares


def implied_growth(target_ps: float, rev0, margin, rate, vc, net_cash, shares) -> float | None:
    """Reverse DCF: the year-1 growth (fading to terminal) that makes the DCF equal the price (bisection)."""
    lo, hi = -0.30, 0.80
    f = lambda gr: dcf_per_share(rev0, margin, gr, rate, vc, net_cash, shares) - target_ps  # noqa: E731
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2


def triple(values: list[float]) -> tuple[float, float, float] | None:
    vs = [v for v in values if v is not None and v > 0]
    return (min(vs), stats.median(vs), max(vs)) if len(vs) >= 2 else None


# --------------------------------------------------------------------------- models
def growth_scenarios(inp, vc, ov):
    g = inp["g"]
    rev = g["revenue"][1]
    c3 = cagr(rev[0], rev[3], 3) if len(rev) > 3 else None
    c5 = cagr(rev[0], rev[5], 5) if len(rev) > 5 else (cagr(rev[0], rev[-1], len(rev) - 1) if len(rev) > 2 else None)
    cs = [c for c in (c3, c5) if c is not None]
    if not cs:
        return None, {}
    lo, hi, avg = min(cs), max(cs), sum(cs) / len(cs)
    gt = vc["terminal_growth"] / 100
    base_lo, base_hi = vc["base_growth_cap"]
    # past growth barely predicts future growth (Chan, Karceski & Lakonishok 2003): the base case reverts
    # halfway to long-run growth; bull keeps the stronger history; bear is weaker still
    base = clamp((avg + gt) / 2, base_lo / 100, base_hi / 100)
    gs = {"bear": min(base, (lo + gt) / 2) - vc["bear_growth_haircut"] / 100, "base": base,
          "bull": max(base, clamp(hi, base_lo / 100, vc["bull_growth_cap"] / 100))}
    for s in SCEN:
        gs[s] = ov.get((s, "growth"), gs[s])
    return gs, {"cagr_3y": c3, "cagr_5y": c5}


def model_dcf(inp, vc, kind, ov):
    g = inp["g"]
    rev_t, shares, nc = g["revenue"][0], g["shares"][0], g["netcash"][0] or 0.0
    if not rev_t or not shares:
        return {"status": "n/m", "why": "no TTM revenue or share count"}
    gs, hist = growth_scenarios(inp, vc, ov)
    if gs is None:
        return {"status": "n/m", "why": "fewer than 3 years of revenue history"}
    tax = clamp(g["taxrate"][0] if g["taxrate"][0] is not None else 0.21, 0.0, 0.35)

    # financials: cash flow is distorted by balance-sheet flows (deposits, policyholder money, client
    # cash), so value the equity on net income at the cost of equity, with no net cash added
    equity_basis = kind == "fcfe" or inp.get("financial")

    def cf_margin(i_fcf, i_sbc, i_int, i_inc, i_ni, i_rev):
        """FCFF = FCF - stock-based pay + after-tax interest paid - after-tax interest earned on cash (the
        cash is added separately as net cash, so its income must not count twice). FCFE: levered FCF -
        stock-based pay. Financials: net income."""
        if not i_rev:
            return None
        if inp.get("financial"):
            return None if i_ni is None else i_ni / i_rev
        if i_fcf is None:
            return None
        adj = 0.0 if equity_basis else (abs(i_int or 0.0) - abs(i_inc or 0.0)) * (1 - tax)
        return (i_fcf - abs(i_sbc or 0.0) + adj) / i_rev
    margins = [cf_margin(g["fcf"][0], g["sbc"][0], g["interest"][0], g["int_income"][0], g["netinc"][0], rev_t)] + \
              [cf_margin(*x) for x in zip(g["fcf"][1], g["sbc"][1], g["interest"][1], g["int_income"][1],
                                          g["netinc"][1], g["revenue"][1])]
    ms = [m for m in margins if m is not None]
    if len(ms) < 3 or stats.median(ms) <= 0:
        return {"status": "n/m", "why": "free cash flow negative or too short a history"}
    ttm_m = margins[0] if margins[0] is not None else stats.median(ms)
    mg = {"bear": min(ms), "base": stats.median(ms) if kind == "dcf_norm" else ttm_m, "bull": max(ms)}
    for s in SCEN:
        mg[s] = ov.get((s, "margin"), mg[s])
    if mg["base"] <= 0:
        return {"status": "n/m", "why": "base cash-flow margin is negative"}
    ke = cost_of_equity(inp["rf"], inp["beta"], vc)
    rate = ke if equity_basis else wacc(inp, ke, vc)
    add_cash = 0.0 if equity_basis else nc
    vals = {s: dcf_per_share(rev_t, mg[s], gs[s], rate, vc, add_cash, shares) for s in SCEN}
    price_fin = inp["price"] / inp["fx"] if inp["fx"] else None
    imp = implied_growth(price_fin, rev_t, mg["base"], rate, vc, add_cash, shares) if price_fin else None
    basis = ("net income (financials: cash flow distorted by balance-sheet flows)" if inp.get("financial")
             else "levered FCF - stock-based pay" if kind == "fcfe" else "FCFF - stock-based pay")
    return {"status": "ok", "values": vals, "implied_growth": imp, "discount_rate": rate, "cost_of_equity": ke,
            "assumptions": {"cash_flow": basis, "growth": gs, "cash_flow_margin": mg, **hist,
                            "terminal_growth": vc["terminal_growth"] / 100}}


def model_multiple(inp, vc, metric, mult, per_share_ev, label, ov):
    g = inp["g"]
    x, shares = g[metric][0], g["shares"][0]
    if x is None or not shares or x <= 0:
        return {"status": "n/m", "why": f"TTM {label} is negative or missing"}
    t = triple(g[mult][1][:5])
    if t is None:
        return {"status": "n/m", "why": f"fewer than 2 positive years of {label} multiples"}
    ms = {s: ov.get((s, "multiple"), v) for s, v in zip(SCEN, t)}
    nc = g["netcash"][0] or 0.0
    vals = {s: ((x * ms[s] + nc) / shares if per_share_ev else x * ms[s]) for s in SCEN}
    return {"status": "ok", "values": vals, "assumptions": {"multiple": ms, f"ttm_{metric}": x}}


def model_pb_roe(inp, vc, ov):
    g = inp["g"]
    bvps = g["bvps"][0]
    if not bvps or bvps <= 0:
        return {"status": "n/m", "why": "book value per share negative or missing"}
    t = triple(g["roe"][1][:5])
    if t is None:
        return {"status": "n/m", "why": "fewer than 2 positive years of ROE"}
    ke, gt = cost_of_equity(inp["rf"], inp["beta"], vc), vc["terminal_growth"] / 100
    roes = {s: ov.get((s, "roe"), min(v, vc["roe_cap"] / 100)) for s, v in zip(SCEN, t)}
    pbs = {s: ((r - gt) / (ke - gt) if r > gt else r / ke) for s, r in roes.items()}
    return {"status": "ok", "values": {s: bvps * pbs[s] for s in SCEN}, "cost_of_equity": ke,
            "assumptions": {"roe": roes, "justified_pb": pbs, "bvps": bvps}}


def model_ddm(inp, vc, ov):
    dps = inp["dps"]  # statistics page: already in the QUOTE currency
    if not dps or dps <= 0:
        return {"status": "n/m", "why": "no dividend"}
    ke, gt = cost_of_equity(inp["rf"], inp["beta"], vc), vc["terminal_growth"] / 100
    gs = {"bear": gt - 0.01, "base": gt, "bull": min(gt + 0.01, ke - 0.01)}
    gs = {s: ov.get((s, "growth"), v) for s, v in gs.items()}
    return {"status": "ok", "quote_ccy": True, "values": {s: dps * (1 + gs[s]) / (ke - gs[s]) for s in SCEN},
            "cost_of_equity": ke, "assumptions": {"dividend_growth": gs, "dps": dps}}


def model_p_ffo(inp, vc, ov):
    g = inp["g"]
    ni, da, shares = g["netinc"][0], g["da"][0], g["shares"][0]
    if ni is None or da is None or not shares or ni + da <= 0:
        return {"status": "n/m", "why": "FFO proxy (net income + D&A) negative or missing"}
    hist = [pe * n / (n + d) for pe, n, d in zip(g["pe"][1][:5], g["netinc"][1][:5], g["da"][1][:5])
            if pe and n and d is not None and n > 0 and pe > 0]
    t = triple(hist)
    if t is None:
        return {"status": "n/m", "why": "fewer than 2 years of P/FFO history"}
    ffo_ps = (ni + da) / shares
    ms = {s: ov.get((s, "multiple"), v) for s, v in zip(SCEN, t)}
    return {"status": "ok", "values": {s: ffo_ps * ms[s] for s in SCEN},
            "assumptions": {"p_ffo": ms, "ffo_per_share": ffo_ps, "note": "FFO proxy = net income + D&A, not AFFO"}}


def model_cash_ps(inp, vc, ov):
    g = inp["g"]
    cash, shares = g["cash"][0], g["shares_out"][0] or g["shares"][0]
    if cash is None or not shares:
        return {"status": "n/m", "why": "cash or share count missing"}
    v = cash / shares
    return {"status": "ok", "values": {s: v for s in SCEN}, "assumptions": {"cash": cash}}


def run_model(model: str, inp: dict, vc: dict, ov: dict) -> dict:
    o = {k[1:]: v for k, v in ov.items() if k[0] == model}
    if model in UNAVAILABLE:
        return {"status": "unavailable", "why": f"[data unavailable — needs {UNAVAILABLE[model]}, not on stockanalysis.com]"}
    if model in ("dcf", "dcf_norm", "fcfe"):
        return model_dcf(inp, vc, model, o)
    if model == "pe":
        return model_multiple(inp, vc, "eps", "pe", False, "EPS", o)
    if model == "ev_ebitda":
        return model_multiple(inp, vc, "ebitda", "evebitda", True, "EBITDA", o)
    if model == "ev_revenue":
        return model_multiple(inp, vc, "revenue", "evrevenue", True, "revenue", o)
    if model == "pb_roe":
        return model_pb_roe(inp, vc, o)
    if model == "ddm":
        return model_ddm(inp, vc, o)
    if model == "p_ffo":
        return model_p_ffo(inp, vc, o)
    if model == "cash_ps":
        return model_cash_ps(inp, vc, o)
    raise ValueError(model)


# --------------------------------------------------------------------------- fair value
def overrides_from(decision: dict | None) -> dict:
    """{(model, scenario, field): value} from the evaluator's `valuation_overrides`."""
    out = {}
    for o in (decision or {}).get("valuation_overrides") or []:
        out[(o["method"], o["scenario"], o["field"])] = float(o["value"])
    return out


def fair_value(inp: dict, industry: str | None, vc: dict, decision: dict | None = None) -> dict:
    im = industry_methods(industry)
    ov = overrides_from(decision)
    order = [(m, "best") for m in im["best_models"]] + [(m, "second") for m in im["second_models"]]
    tried, used = [], []
    for m, slot in order:
        if any(t["model"] == m for t in tried):
            continue
        r = run_model(m, inp, vc, ov)
        if r["status"] == "ok":
            conv = 1.0 if r.get("quote_ccy") else inp["fx"]
            if conv is None:
                r = {"status": "unavailable", "why": f"[data unavailable — no FX rate for {inp['fin_ccy']}]"}
            else:
                r["values"] = {s: v * conv for s, v in r["values"].items()}
        tried.append({"model": m, "label": LABEL[m], "slot": slot, **r})
        if r["status"] == "ok" and len(used) < 2:
            used.append(tried[-1])
    out = {"industry": im, "methods": tried, "price": inp["price"], "risk_free": inp["rf"],
           "terminal_growth": vc["terminal_growth"] / 100,
           "overrides": [{"method": k[0], "scenario": k[1], "field": k[2], "value": v} for k, v in ov.items()]}
    if not used:
        out.update(fair_value=None, why="no method computable from stockanalysis.com data")
        return out
    w = [vc["blend_weights"][0], vc["blend_weights"][1]] if len(used) == 2 else [1.0]
    fv = {s: sum(wi * u["values"][s] for wi, u in zip(w, used)) / sum(w) for s in SCEN}
    out.update(fair_value=fv, used=[u["model"] for u in used], weights=w,
               upside={s: fv[s] / inp["price"] - 1 for s in SCEN} if inp["price"] else None,
               implied_growth=next((t.get("implied_growth") for t in tried if t.get("implied_growth") is not None), None))
    return out


def render_md(fv: dict, ccy: str, ticker: str, asof: str) -> str:
    im = fv["industry"]
    f = lambda x: "n/a" if x is None else f"{x:,.2f}"  # noqa: E731
    p = lambda x: "n/a" if x is None else f"{x * 100:+.1f}%"  # noqa: E731
    L = [f"# Fair value: {ticker} — {asof}",
         f"Industry: {im['industry'] or '[data unavailable]'} [OV]"
         + ("" if im["known"] else " (not in the owner's table: DCF / EV/EBITDA default)")
         + f" · best method: {im['best']} · 2nd: {im['second']} · risk-free {fv['risk_free'] * 100:.2f}% (FRED DGS10)",
         "Inform-only (owner rule): assumptions from the stock's own 5-year history; never an analyst target.", ""]
    if fv.get("fair_value"):
        w = fv["weights"]
        L += ["| | Bear | Base | Bull |", "|---|---|---|---|",
              f"| Fair value ({ccy}) | {f(fv['fair_value']['bear'])} | {f(fv['fair_value']['base'])} | {f(fv['fair_value']['bull'])} |",
              f"| vs last close {f(fv['price'])} | {p(fv['upside']['bear'])} | {p(fv['upside']['base'])} | {p(fv['upside']['bull'])} |",
              "", "Blend: " + " + ".join(f"{LABEL[m]} {wi / sum(w) * 100:.0f}%" for m, wi in zip(fv["used"], w))
              + (f" · reverse DCF: the price implies {fv['implied_growth'] * 100:.1f}% revenue growth in year 1, fading to "
                 f"{fv.get('terminal_growth', 0.025) * 100:.1f}% by year 10"
                 if fv.get("implied_growth") is not None else "")]
    else:
        L.append(f"Fair value: [data unavailable] — {fv.get('why')}")
    L += ["", "| Method | Slot | Status | Bear | Base | Bull | Key assumptions |", "|---|---|---|---|---|---|---|"]
    for m in fv["methods"]:
        v = m.get("values") or {}
        a = m.get("assumptions") or {}
        key = "; ".join(f"{k.replace('_', ' ')} " + fmt_assumption(k, d) for k, d in a.items() if d is not None)
        if m.get("discount_rate"):
            key += f"; discount rate {m['discount_rate'] * 100:.1f}%"
        L.append(f"| {m['label']} | {m['slot']} | {m['status'] if m['status'] == 'ok' else m['why']} | "
                 f"{f(v.get('bear'))} | {f(v.get('base'))} | {f(v.get('bull'))} | {key} |")
    if fv["overrides"]:
        L.append("\nEvaluator overrides: " + "; ".join(f"{o['method']} {o['scenario']} {o['field']} = {o['value']}"
                                                       for o in fv["overrides"]))
    return "\n".join(L) + "\n"


def fact_sheet_section(fv: dict, ccy: str) -> list[str]:
    """Compact "Fair value" section for the fact sheet: every table row ends with its source codes (the
    statement pages it is computed from). The full table is in research/<SLUG>/<date>-valuation.md."""
    im = fv["industry"]
    f = lambda x: "n/a" if x is None else f"{x:,.2f}"  # noqa: E731
    p = lambda x: "n/a" if x is None else f"{x * 100:+.1f}%"  # noqa: E731
    src = "IS,BS,CF,RA,ST"
    L = ["", "## Fair value (inform-only: own-history assumptions, never an analyst target)",
         f"Industry {im['industry'] or '[data unavailable]'} [OV]"
         + ("" if im["known"] else " (not in the owner's table: DCF / EV/EBITDA default)")
         + f"; owner's method table: best {im['best']}, 2nd {im['second']}. Risk-free {fv['risk_free'] * 100:.2f}% "
           "(FRED 10y Treasury, https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10).",
         "| Item | Bear | Base | Bull | Src |", "|---|---|---|---|---|"]
    if fv.get("fair_value"):
        L += [f"| Fair value ({ccy}) | {f(fv['fair_value']['bear'])} | {f(fv['fair_value']['base'])} | "
              f"{f(fv['fair_value']['bull'])} | {src},HI |",
              f"| vs last close {f(fv['price'])} | {p(fv['upside']['bear'])} | {p(fv['upside']['base'])} | "
              f"{p(fv['upside']['bull'])} | {src},HI |"]
    for m in fv["methods"]:
        v = m.get("values") or {}
        if m["status"] == "ok":
            L.append(f"| {m['label']} ({m['slot']}) | {f(v.get('bear'))} | {f(v.get('base'))} | {f(v.get('bull'))} | {src} |")
        else:
            L.append(f"| {m['label']} ({m['slot']}) | {m['why']} | | | {src} |")
    if fv.get("fair_value"):
        w = fv["weights"]
        L.append("Blend: " + " + ".join(f"{LABEL[m]} {wi / sum(w) * 100:.0f}%" for m, wi in zip(fv["used"], w))
                 + (f". Reverse DCF: the price implies {fv['implied_growth'] * 100:.1f}% revenue growth in year 1, "
                    "fading to terminal growth by year 10." if fv.get("implied_growth") is not None else ".")
                 + " Assumptions per method: research/<SLUG>/<date>-valuation.md.")
    else:
        L.append(f"Fair value: [data unavailable] — {fv.get('why')}")
    return L


PCT_KEYS = ("growth", "cash_flow_margin", "cagr_3y", "cagr_5y", "terminal_growth", "roe", "dividend_growth")


def fmt_assumption(k: str, d) -> str:
    """Rates as %, multiples as x, money as plain numbers; bear/base/bull dicts as a/b/c."""
    def one(x):
        if not isinstance(x, (int, float)):
            return str(x)
        if k in PCT_KEYS:
            return f"{x * 100:.1f}%"
        if k in ("multiple", "justified_pb", "p_ffo"):
            return f"{x:.2f}x"
        return f"{x:,.4g}"
    return "/".join(one(x) for x in d.values()) if isinstance(d, dict) else one(d)


def risk_free_pct(asof: str, cfg: dict) -> float:
    """FRED 10-year Treasury yield (%), from the day's macro snapshot or one cached FRED request."""
    snap = ROOT / "reports" / "macro" / f"{asof}.json"
    if snap.exists():
        for s in json.loads(snap.read_text())["series"]:
            if s["id"] == "DGS10" and isinstance(s.get("value"), (int, float)):
                return float(s["value"])
    from macro_data import FredFetcher, summarise
    got = FredFetcher(cfg).series("DGS10")
    s = summarise("DGS10", "US 10y", got["rows"], got["source_url"], asof)
    if not isinstance(s.get("value"), (int, float)):
        raise DataError(got["source_url"], "DGS10", "no observation")
    return float(s["value"])


def compute(ticker: str, asof: str, fetcher, cfg: dict, decision: dict | None = None) -> tuple[dict, str]:
    from portfolio import Market
    sec = {k: fetcher.section(ticker, k) for k in ("overview", "income", "balance", "cashflow", "ratios", "statistics", "history")}
    mkt = Market(fetcher, asof, cfg)
    q = mkt.quote(ticker)
    qccy = sec["history"]["data"]["info"]["price_currency"]
    fccy = sec["income"]["data"].get("currency") or qccy
    try:
        fx = 1.0 if fccy == qccy else mkt.fx(fccy)["rate"] / mkt.fx(qccy)["rate"]
    except (DataError, KeyError, TypeError):
        fx = None
    inp = inputs_from_sections(sec, q["close"], risk_free_pct(asof, cfg), fx)
    fv = fair_value(inp, sec["overview"]["data"].get("industry"), cfg["valuation"], decision)
    fv.update(ticker=ticker, asof=asof, quote_currency=qccy, financials_currency=fccy, fx_fin_to_quote=fx,
              price_date=q["date"], sources=inp["sources"])
    return fv, qccy


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--eval", help="evaluation file whose Decision block may carry valuation_overrides")
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    cfg = load_config()
    decision = None
    if a.eval:
        from decision_log import decision_from_eval
        decision = decision_from_eval(Path(a.eval).read_text())
    try:
        from fetch_data import CACHE_DIR
        day = a.asof if (CACHE_DIR / a.asof).exists() else None  # a past day's saved pages, when we have them
        fv, ccy = compute(a.ticker, a.asof, Fetcher(cfg, today=day), cfg, decision)
    except DataError as e:
        print(f"VALUATION FAILED — nothing written: {e}", file=sys.stderr)
        return 2
    out = ROOT / "research" / Ticker(a.ticker).slug / f"{a.asof}-valuation"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".json").write_text(json.dumps(fv, indent=1, default=str))
    out.with_suffix(".md").write_text(render_md(fv, ccy, a.ticker, a.asof))
    b = fv.get("fair_value") or {}
    print(json.dumps({"out": str(out.with_suffix(".md").relative_to(ROOT)), "used": fv.get("used"),
                      "fair_value": {k: round(v, 2) for k, v in b.items()}, "price": fv["price"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
