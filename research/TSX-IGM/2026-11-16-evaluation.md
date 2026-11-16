# Evaluation: IGM Financial Inc. (TSX:IGM) — 2026-11-16
## Bear case
The re-rating has outrun the business. P/E 15.5x, EV/EBITDA 10.3x and P/B 2.1x all sit above their own 5-year maximums after a 55.9% 12-month rise [Certain]. The mechanical base fair value is 74.33 CAD against a close of 89.34, and even the bull case is only 92.53 [Certain]; the reverse DCF needs 6.8% year-1 revenue growth [Certain]. Fees track equity markets, so a drawdown hits earnings and the multiple together [Certain]. The price is 14.4% above its 200-day average: an extended price risks a de-rating if flows or EPS growth slow [Likely]. The ROIC rebound (12.6% to 14.9% over 12 months) reverses a 5-year decline and FCF margin is still 2.5pp below its 2024 high, so the recovery is young and partly market-driven [Likely]. Power Corporation control and further Wealthsimple capital calls leave minority holders dependent on the parent's discipline [Likely].
## Bull case
A light-balance-sheet fee franchise that is clearly working. TTM ROIC 14.9% and operating margin 41.9% are at 2-year highs, FCF conversion is 91.2% and net debt/EBITDA 0.60x [Certain]. The 5-year ROIC and FCF-margin declines have turned up over the last 12 months on operating leverage from higher client assets and flows, a temporary dip, not a structural loss [Likely]. Adjusted EPS rose 19% in Q3 after 32% in Q2, per the earnings calls [Likely]. A 6.05% FCF yield funds substantial capital returns and a shrinking share count [Certain]. It trades below peers on P/E, P/FCF and P/B [Certain], and the Wealthsimple stake is optional upside the multiples barely credit [Guessing]. Sticky advisor relationships give a narrow moat [Likely].
## Decision
```json
{
  "ticker": "TSX:IGM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing is falling over 1 or 3 years: ROIC and FCF margin fell over 5 fiscal years but rose over the last 12 months (ROIC 12.6% to 14.9%, FCF margin 22.8% to 24.9%) with operating margin at a 2-year high of 41.9% [RA-T, IS-T]; Q3 adjusted EPS up 19% on asset growth and flows (https://stockanalysis.com/quote/tsx/IGM/transcripts/720321-q3-2026/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A de-rating: multiples sit above their own 5-year maximums after a 55.9% rise, so an equity-market pullback that slows flows and fee growth would cut earnings and the multiple together.", "veto": null},
  "thesis": "A low-leverage Canadian wealth and asset manager with returns and margins at 2-year highs, but priced above its own 5-year multiple range and above the mechanical fair value after a 55.9% rise.",
  "rationale": "The business is working and the balance sheet is light, but every own-history multiple sits above its 5-year maximum and the base fair value is below the price, so the scorecard does not reach the buy bar. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 89.34,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-IGM/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 38%, under the FY2023 five-year low of 38.1%, showing fee pressure is eroding the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM ROE falls below 12%, under the FY2024 low of 12.8%, showing the returns recovery has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 18%, under the FY2022 five-year low of 20.2%, showing cash conversion is breaking down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.60x TTM now), e.g. debt-funded Wealthsimple or other investments.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 104.97, "basis": "Flows and operating leverage keep margins at 2-year highs and the DCF bull value of 104.97 is reached (fact sheet Fair value, IS/CF/RA)."},
    "base": {"probability": 0.5, "target_price_12m": 79.23, "basis": "Fundamentals hold but the multiples above their 5-year maximums drift back toward the DCF base value of 79.23 (fact sheet Fair value; RA 5y ranges), above the blended base of 74.33 because the DCF is the best method."},
    "bear": {"probability": 0.25, "target_price_12m": 58.8, "basis": "An equity-market pullback slows flows and fees, the P/E reverts toward its 5y median of 11.2x [RA] and the price reaches the DCF bear value of 58.80 (fact sheet Fair value)."}
  },
  "entry_price": 59.46,
  "entry_basis": "valuation file: base 74.33 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
