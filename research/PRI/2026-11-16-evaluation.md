# Evaluation: Primerica, Inc. (PRI) — 2026-11-16
## Bear case
The term-life engine is shrinking at the front end: the 10-Q reports falling new recruits, new life-licensed representatives and new policies issued, a smaller life-licensed force than in December, and lapses above historical levels [Certain]. Recruiting leads term growth, so today's 31.2% ROE and 19.3% ROIC describe the in-force book, not future production [Likely]. Q3 strength came from investment sales, which are market-sensitive and could reverse with asset prices [Likely]. The mechanical base fair value of 261.22 sits below the 293.39 close; the P/E leg is only 193.06 [Certain]. Buying on trend strength (price above the 200-day average, 12-month change +13.3%) risks a de-rating if term production keeps falling and ISP growth slows, while 3-month momentum is already -6.2% [Likely]. Higher rates added unrealized investment losses [Certain]. Rolling ROIC is flat, just under its 2-year high of 19.7% [Certain].

## Bull case
A capital-light distributor earning ROIC 19.3% and ROE 31.2%, both up over five years, trades at 11.6x earnings, 7% of its own 5-year P/E range, and 8.8x EV/EBITDA, below peers on both [Certain]. FCF yield is 10.47% and conversion 116.8% of net income, funding a share count down 4.86% YoY; nine-month buybacks of $377.8M and dividends of $112.7M [company-reported] [Certain]. Leverage has fallen to 0.85x (site definition) [Certain]. Record investment sales and client assets diversify earnings away from term life [Likely]. The price already discounts franchise erosion; even a flat earnings path compounds per-share value via buybacks [Likely]. The P/B + ROE fair-value leg of 295.31, the industry's best method, is near the price [Certain].

## Decision
```json
{
  "ticker": "PRI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC is flat over the last year (19.3% TTM vs 18.3% a year earlier, 2-year high 19.7%) [RA-T]; nothing Python tracks is falling, though recruiting and new policies issued fell per the 10-Q.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Falling recruiting and life-licensed headcount erode term-life production, while an extended trend price de-rates if ISP growth slows with markets.",
    "veto": null
  },
  "thesis": "A high-return, deleveraging, buyback-heavy life-insurance distributor trades low in its own P/E range, but a shrinking sales force and a price above the mechanical fair value leave a balanced rather than compelling skew.",
  "rationale": "Quality, cash returns and balance sheet are strong, but the front end of the franchise is weakening and the price sits above the blended fair value, so upside rests on buybacks and trend rather than a discount. Conviction is below the buy bar: AVOID, with an entry price on a real discount.",
  "price_at_decision": 293.39,
  "price_date": "2026-11-13",
  "research_note": "research/PRI/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15% (19.3% now), giving up the five-year improvement from 15.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM ROE falls below 25% (31.2% now), showing the term-life book's returns are eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 25}},
    {"text": "Net debt/EBITDA (site definition) rises above 2.0x (0.85x now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "The life-licensed sales force count in the 10-Q MD&A is below the prior year's level for two consecutive quarters with new policies issued still falling."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 320.0, "basis": "P/E re-rates toward its 5y median 12.6x [RA] as ISP strength and buybacks offset soft term production, above the mechanical bull 304.27 because buybacks shrink the share count [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 295.0, "basis": "Price tracks the P/B + ROE fair-value leg of 295.31 [ST,RA], the industry's best method, with ROE held near 31.2% [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 247.0, "basis": "Recruiting and new-policy declines in the 10-Q persist (https://www.sec.gov/Archives/edgar/data/1475922/000119312526449402/pri-20260930.htm) and the price falls to the mechanical bear fair value 246.75."}
  },
  "entry_price": 248.0,
  "entry_basis": "Mechanical bear fair value 246.75 rather than base x 0.8: the P/B + ROE leg (295.31) shows the base is depressed by the P/E leg; near 248 the P/E would sit at its 5y low of 11.0x [RA] or below, a real discount for this quality.",
  "replaces": null,
  "replacement_reason": null
}
```
