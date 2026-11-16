# Evaluation: Commerce Bancshares, Inc. (CBSH) — 2026-11-16
## Bear case
The fall to 55.74 has no stock-specific cause behind it: Q3 EPS was $1.08, flat with consensus, and guidance was unchanged [Certain]. That makes it a de-rating driven by rates, not a mispricing. The macro overlay shows the 10y-2y slope at only 0.24pp, with the 2y up 0.71pp in three months, so deposit costs and securities marks squeeze margin [Likely]. ROE has slipped from 17.8% (FY2023) to 15.1% TTM and net margin from 33.1% to 31.4% [Certain]. Growth comes from acquisitions: nine-month EPS rose only 3.6% against net income +7.2% [company-reported], and shares are up 2.07% [Certain]. FineMark purchase accretion flatters NII [Likely]. The Direction-change line (FCF margin up to 67.3%) is bank cash-flow timing, not earnings power [Likely]. The fair value is flagged unreliable, and P/B is still 32% above peers [Certain].
## Bull case
This is a high-quality, low-beta (0.60) regional bank still earning ROE of 15.1%, well above its peers [Certain]. P/E of 13.4x sits near its 5y minimum of 13.0x, against a 15.9x median, and P/B of 1.9x is at its 5y low [Certain]. A sticky, low-cost commercial and wealth deposit franchise is a narrow moat [Likely]. The ROE drift is a normalisation from the FY2023 rate peak plus acquisition goodwill in equity, not lost share [Likely]. The buyback reauthorized on 2026-11-03 and the stock and cash dividends return capital [Certain]. Fee bolt-ons (FineMark, Nolan) diversify away from spread income [Likely]. P/B + ROE gives 64.07 and FCFE gives 67.44, both above the price [Certain]. The macro tilt is only small, because the multiple already discounts a lot [Guessing].
## Decision
```json
{
  "ticker": "CBSH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "The scorecard finds no 1y or 3y decline in its tracked metrics; ROE has drifted from the FY2023 rate-cycle peak of 17.8% to 15.1% TTM [RA], consistent with margin normalisation and FineMark acquisition equity (https://www.sec.gov/Archives/edgar/data/22356/000002235626000213/cbsh-20260930.htm), not lost share.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A flat or inverting curve (10y-2y 0.24pp, macro overlay) squeezes net interest margin through deposit repricing while purchase accretion fades, keeping EPS growth low and the multiple compressed.", "veto": null},
  "thesis": "A high-ROE, low-beta regional bank trading at the bottom of its own P/E and P/B range, but with drifting returns, acquisition-led growth and a rate headwind that leave the discount moderate rather than compelling.",
  "rationale": "The fall is rate-driven de-rating with no thesis break, so it is not an overreaction to buy into; quality is good but returns are drifting, growth is acquired and the fair value is flagged unreliable. The scorecard gives conviction 3, below the buy bar. Cash is acceptable.",
  "price_at_decision": 55.74,
  "price_date": "2026-11-13",
  "research_note": "research/CBSH/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROE falls below 12% (15.1% now), showing returns have broken below a normal rate-cycle range.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM net margin falls below 28% (31.4% now), showing deposit costs or credit are compressing profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Shares outstanding growth exceeds 4% year on year (2.07% now) without a further acquisition, showing dilution outruns buybacks.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 4}},
    {"text": "Efficiency ratio in the 10-Q MD&A rises above 62% (58.34% for nine months of 2026 [company-reported])."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 70.27, "basis": "Curve steepens and NIM holds, P/B re-rates off its 5y low of 1.9x toward the mechanical bull fair value 70.27 [RA, fact sheet]; probability trimmed for the macro overlay's small bear tilt (research/CBSH/2026-11-16-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 62.0, "basis": "ROE holds near 15.1% and P/E drifts partway back from 13.4x toward its 15.9x median, a little below the P/B + ROE value of 64.07 [RA, fact sheet] because returns are still drifting and the fair value is flagged unreliable."},
    "bear": {"probability": 0.3, "target_price_12m": 50.0, "basis": "Curve inverts and spreads widen (macro overlay bear, small bear tilt raises this weight; research/CBSH/2026-11-16-macro.md), EPS growth stays near the 3.6% nine-month rate [company-reported] and P/E slips below its 13.0x 5y min [RA]."}
  },
  "entry_price": 55.41,
  "entry_basis": "valuation file: base 65.19 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```
