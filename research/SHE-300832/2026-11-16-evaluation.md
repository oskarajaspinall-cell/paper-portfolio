# Evaluation: Shenzhen New Industries Biomedical Engineering (SHE:300832) — 2026-11-16
## Bear case
Returns have halved on the fiscal view: ROIC fell from 50.1% (FY2021) to 26.6% (FY2025) and operating margin from 41.5% to 38.7% [Certain]; the 12-month rebound to 29.4% and 42.6% is still below the 2-year highs of 33.3% and 44.7%, and its cause is unexplained in the research [Certain]. Chinese diagnostics procurement and reimbursement policy can cap reagent prices permanently, which would make the FY2025 dip structural; no official source was read to rule this out [Guessing]. The mechanical DCF base of 28.96 sits far below the 60.55 close and the reverse DCF needs 30.7% year-1 revenue growth [Certain]. The stock trades 21.3% above its 200-day average after a +22.0% 3-month run: an extended price risks a de-rating if growth slows [Likely]. EV/Sales and P/B are far above peers [Certain]. Overseas mix is [data unavailable].
## Bull case
A net-cash (net debt/EBITDA -1.21x) razor/razorblade franchise with 71.2% gross margin, 42.6% operating margin and 29.4% ROIC [Certain]. The last 12 months reversed the decline: ROIC up from 22.9%, operating margin from 37.5%, FCF margin from 24.7% to 34.0%, and FCF conversion to 91.3% [Certain]. On its own history it is cheap: P/E 27.3x at the bottom of its 5y range, EV/EBITDA 19.7x and P/FCF 28.9x below their 5y minimums, and P/FCF in line with peers [Certain]. Installed-base reagent pull-through gives switching costs [Likely]. Insiders own 21.43% and there is no dilution [Certain]. The P/E-method base of 70.02 shows the upside if the multiple only returns toward its median [Certain]; the trend is healthy, above the 200-day average with a 3.47% FCF yield [Certain].
## Decision
```json
{
  "ticker": "SHE:300832",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin fall on the 3-year view, but the rolling 12 months reversed (ROIC 22.9% -> 29.4%, operating margin 37.5% -> 42.6%, FCF margin 24.7% -> 34.0%) with net cash intact (-1.21x) [RA-T, IS-T, CF-T, BS]; the cause of the FY2025 dip is not identified in the research.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "China diagnostics procurement/reimbursement policy capping reagent prices, turning the FY2025 margin dip structural; plus a de-rating of the extended price if growth slows.",
    "veto": null
  },
  "thesis": "A net-cash, high-margin immunoassay reagent franchise whose returns rebounded over the last 12 months trades at the bottom of its own multiple range, but the price already discounts strong growth and China pricing policy is unverified.",
  "rationale": "Quality and the rolling rebound are real and own-history multiples are low, but the DCF says the price needs demanding growth, the fair value is unreliable, and the decline's cause is unexplained. The scorecard does not reach the buy bar; cash is acceptable.",
  "price_at_decision": 60.55,
  "price_date": "2026-11-13",
  "research_note": "research/SHE-300832/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 38% (42.6% now), under the FY2025 level of 38.7%, showing the rebound reversed and pricing pressure is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM ROIC falls below 22% (29.4% now), back under the level of a year earlier.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 20% (34.0% now), showing the cash-conversion gain reversed.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) turns positive from -1.21x, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 70.02, "basis": "P/E re-rates toward its 5y median 30.4x [RA] as the rolling margin rebound holds, matching the P/E-method base fair value of 70.02 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 60.55, "basis": "P/E holds near 27.3x, the bottom of its 5y range [RA], with no confirmed growth step-up; above the unreliable blend base of 42.65 because the DCF assumes growth the rolling FCF margin of 34.0% [CF-T] does not show falling."},
    "bear": {"probability": 0.25, "target_price_12m": 42.65, "basis": "China pricing policy makes the FY2025 dip structural and the extended price de-rates toward the mechanical blend base fair value of 42.65 [fact sheet fair value; Bear case]."}
  },
  "entry_price": 34.12,
  "entry_basis": "valuation file: base 42.65 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
