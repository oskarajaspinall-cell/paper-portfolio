# Evaluation: DexCom, Inc. (DXCM) — 2026-11-17
## Bear case
The price already needs a lot: the reverse DCF implies 31.6% year-1 revenue growth, far above the 11% Q3 growth on the earnings call, and the mechanical base fair value of 60.90 sits below the 81.61 close [Certain]. Valuation points come from trend strength, not a discount, so a growth slowdown risks a de-rating on a beta-1.44 stock that already trades at a premium to peers on P/E (+27%) and EV/EBITDA (+32%) [Certain]. FCF margin fell to 21.5% TTM from 23.5% a year earlier, 8.2pp below its 2-year high, even as operating margin rose; the note's timing/capex explanation is a guess, not a disclosure [Guessing]. Gross margin is still below FY2021 (63.4% vs 68.6%), and Abbott is a scaled rival on price [Likely]. International grew only 5% [Certain]. FDA warning-letter closure is inferred from dropped risk factors, not confirmed [Likely].
## Bull case
Returns are rising fast on every rolling measure: ROIC 45.9% TTM vs 27.8% a year earlier, operating margin 24.0% vs 17.2%, both at 2-year highs [Certain]. The balance sheet is net cash (-0.28x net debt/EBITDA), Piotroski 7, and shares fell 3.92% YoY with a new buyback announced [Certain]. Q3 beat, FY26 revenue guidance was narrowed to $5.20B-$5.25B and the call cited US share gains and G7 15 Day adoption [Likely]. P/E 32.0x sits at 1% of its 5-year range and EV/EBITDA is below its 5-year minimum, so the de-rating has already happened while returns rose [Certain]. FCF conversion of 110.8% says earnings quality is intact; the FCF-margin dip coincides with G6 discontinuation inventory charges and higher advertising flagged in the MD&A, a temporary pattern [Likely]. The stock is above its 200-day average, up 40.6% in 12 months, not overextended [Certain].
## Decision
```json
{
 "ticker": "DXCM",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "Only FCF margin is falling (23.5% -> 21.5% TTM) while operating margin and ROIC rose to 2-year highs and FCF conversion is 110.8% [CF-T,IS-T]; the 10-Q MD&A flags G6 discontinuation inventory charges and higher advertising (https://www.sec.gov/Archives/edgar/data/1093557/000109355726000195/dxcm-20260930.htm).",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Growth slows (Abbott price competition, weak international) while the price already implies 31.6% year-1 growth, producing a de-rating of a high-beta stock whose valuation points rest on trend strength.",
  "veto": null
 },
 "new_evidence": {
  "type": "method_change",
  "text": "The 2026-11-15 AVOID at conviction 3 predates the 2026-11-17 scorecard change (strength_at_value_points): two trend-strength points now count as three when the value blend is at or above the price, which lifts the same evidence from 8 to 9 points."
 },
 "thesis": "A net-cash CGM leader with sharply rising returns and margins trades at the bottom of its own multiple range while in a healthy uptrend, with buybacks shrinking the share count.",
 "rationale": "Scorecard gives conviction 4: top-tier and rising returns, net cash, and trend-strength valuation points with the price near the expected-value blend. Python sets the volatility-scaled size; cash cannot fund it above the 1.5% floor, so the conviction-3 OTIS holding is sold to fund it.",
 "price_at_decision": 81.61,
 "price_date": "2026-11-16",
 "research_note": "research/DXCM/2026-11-17.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 25%, giving up most of the rise from 24.1% in FY2024 to 45.9%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 25
   }
  },
  {
   "text": "TTM gross margin falls below 58%, under the FY2025 low of 60.1%, signalling CGM price competition.",
   "check": {
    "source": "statistics",
    "field": "grossMargin",
    "op": "<",
    "value": 58
   }
  },
  {
   "text": "TTM operating margin falls below 18%, reversing the step-up from 17.2% a year earlier to 24.0%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 18
   }
  },
  {
   "text": "A new FDA warning letter, recall order or production shutdown disclosed in a 10-Q/8-K."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 109,
   "basis": "Rising ROIC and G7 15 Day adoption [RA-T, Q3 transcript] let P/E hold near current levels on growing earnings, reaching the P/E method's base fair value of 109.30 [fact sheet fair value]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 85,
   "basis": "Guided growth and buybacks [OV news] offset a modest de-rating toward the peer P/E median of 25.2x [RA], leaving the price near the 50-day average of 84.17 [HI]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 58,
   "basis": "Growth falls well short of the 31.6% the price implies [reverse DCF] and the stock de-rates toward the blended base fair value of 60.90 and the 52-week low of 56.72 [HI]; the DCF base of 36.71 is ignored as the fair value is flagged unreliable."
  }
 },
 "replaces": "OTIS",
 "replacement_reason": "OTIS is held at conviction 3 with a balanced rather than compelling skew, price above its mechanical fair value, falling operating margin and rising leverage (its own thesis); DXCM clears the buy bar at conviction 4 with rising returns and net cash, and cash cannot fund a full position above the 1.5% floor.",
 "second_opinion": {
  "file": "research/DXCM/2026-11-17-evaluation-2.md",
  "conviction": 4
 }
}
```
