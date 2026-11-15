# Evaluation: Oscar Health, Inc. (OSCR) — 2026-11-15
## Bear case
TTM ROIC of 33.8% follows -27.6% in FY2025 and losses in four of five fiscal years: one good underwriting year, not a proven return stream [Certain]. ACA plans are price-driven and regulated; the 10-Q adds expired enhanced subsidies, 2027 income verification, new identity proofing and the Columbus II lawsuit, any of which could shrink the market and worsen morbidity [Certain]. The low P/E and P/FCF are on peak-like profit; the FCF yield of 42.98% is insurer working-capital timing, not cash returns [Likely]. Shares rose 28.25% YoY, heavy dilution [Certain]. The price is 27.1% above its 200-day average after a +105.6% year; with beta 2.49, any slip in 2027 pricing or medical costs risks a sharp de-rating [Likely]. P/B of 4.3x sits above its 5y max [Certain]. No mechanical fair value is computable, so the discount can't be checked [Certain].
## Bull case
Q3 2026 beat and management raised FY2026 operating earnings guidance to $850M-$950M [Likely]. Members grew about 27% YoY [company-reported] while the ACA market shrank, suggesting share gains from pricing and risk-adjustment discipline [Likely]. P/E 11.7x and EV/EBITDA 5.9x are well below peer medians of 23.3x and 13.7x [Certain]. Piotroski F is 7 [Certain]. Expansion into new Ohio and South Carolina counties for 2027 open enrollment widens the footprint [Likely]. The uptrend is intact: 6-month relative strength vs SPY +29.8pp, price above its 200-day average [Certain]. Midterm results were read as supportive for ACA operators [Guessing].
## Decision
```json
{
  "ticker": "OSCR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds nothing falling: TTM ROIC 33.8% vs -12.8% a year earlier [RA-T].", "moat": "none", "key_risk": "high", "key_risk_text": "ACA regulation (expired enhanced subsidies, 2027 income verification, identity proofing, Columbus II lawsuit) and medical-cost mean reversion could reverse a one-year profit recovery, with an extended price (beta 2.49) exposed to a de-rating.", "veto": null},
  "thesis": "A one-year ACA underwriting recovery with cheap multiples on peak-like profit, but no moat, heavy dilution and dominant regulatory risk.",
  "rationale": "Cheap versus peers and in an uptrend, but returns have been positive for only one year, the moat is thin, regulation can shrink the market, and no fair value is computable. Good but not compelling: AVOID; cash is acceptable.",
  "price_at_decision": 31.05,
  "price_date": "2026-11-13",
  "research_note": "research/OSCR/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (statistics page), showing the underwriting recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Share count growth YoY exceeds 30%, signalling continued heavy dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 30}},
    {"text": "Effectuated members fall YoY for two consecutive quarters (10-Q MD&A).", "check": null},
    {"text": "FY operating earnings guidance is cut at any quarterly update (earnings release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 38.5, "basis": "Raised FY2026 guidance holds into 2027 and the price retests its 52-week high of 38.50 [HI] as the multiple gap to peers narrows [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 31.05, "basis": "Earnings stay near guidance but the market keeps pricing mean reversion, so the multiple stays at today's level [ST]; no mechanical fair value is computable to anchor it [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 20.09, "basis": "Subsidy, verification or lawsuit effects in the 10-Q (https://www.sec.gov/Archives/edgar/data/1568651/000156865126000086/oscr-20260930.htm) lift medical costs and the price falls back to its 6-month low of 20.09 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the multiples are already low; the obstacles are an unproven one-year return record, no moat and unresolved ACA regulatory risk, so a lower price would not change the decision. No mechanical fair value is computable.",
  "replaces": null,
  "replacement_reason": null
}
```
