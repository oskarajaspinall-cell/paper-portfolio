# Evaluation: Bank of Changsha Co., Ltd. (SHA:601577) — 2026-10-18
## Bear case
Returns are eroding every year: ROE fell from 12.8% (FY2021) to 10.0% TTM [Certain], and the note links this to sector-wide margin compression [Likely]. We cannot see the variables that decide a bank's value: no NPL ratio, provision coverage or capital adequacy is published on stockanalysis.com [Certain], so LGFV and property credit exposure is unassessable [Likely]. The low P/B is not new: 0.4x is the 5y median and the multiple never exceeded 0.6x [Certain], so the "discount" is a persistent structural rating, not a dislocation with a catalyst [Likely]. P/E of 4.8x is near the top of its 5y range (86%) [Certain]. Piotroski F-score of 4 is middling [Certain]; FCF figures are deposit-flow artifacts, so the headline FCF yield of 141.78% is meaningless [Certain]. Retail/state-dominated float (institutions 13.7%) and adding a third China name concentrate country risk [Likely].

## Bull case
At 0.4x book and 4.8x earnings the bank trades below peer medians of 0.6x and 6.6x [Certain] while still earning a 10.0% ROE [Certain]. Net margin has risen five years running to 46.6% [Certain], suggesting cost and provision discipline [Likely]. Shares outstanding fell 3.39% YoY [Certain]. The mechanical fair value (P/B + ROE, FCFE) puts even the bear case at 15.56 against a 9.58 close, and the reverse DCF implies a -17.2% year-1 revenue decline [Certain] — a price that discounts severe deterioration [Likely]. Beta of 0.11 [Certain] would diversify the portfolio's US-equity risk [Likely]. Stabilising ROE at Q3 results (Oct 31, 2026) could start a re-rating toward the peer P/B [Guessing].

## Decision
```json
{
  "ticker": "SHA:601577",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cheap Hunan city commercial bank at 0.4x book whose discount is persistent and whose falling ROE and undisclosed asset quality prevent us from distinguishing undervaluation from a correctly priced credit risk.",
  "rationale": "Cheap on every own-history and peer measure, but the 0.4x P/B is its normal level, ROE is falling every year and asset-quality data is unavailable; the mechanical fair value cannot see credit risk. Good but not compelling, so AVOID. Adding a third China name also concentrates country risk.",
  "price_at_decision": 9.58,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601577/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE rises back above 12%, its FY2022-FY2023 level, reversing the five-year decline and showing earning power is stabilising (would raise conviction).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12}},
    {"text": "TTM ROE falls below 8%, confirming the downtrend is accelerating into a credit or margin problem.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 40%, reversing its five-year rise and signalling a credit-cost or NIM shock.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "The company's quarterly/annual report discloses asset-quality data (NPL ratio, provision coverage, capital adequacy) showing stable or improving credit, closing the disclosure gap that blocks conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 12.5, "basis": "ROE stabilises and P/B re-rates toward its 5y max of 0.6x and the 0.6x peer median [RA], still below the mechanical bear fair value of 15.56 because the bank has never traded near the model's implied book multiple."},
    "base": {"probability": 0.55, "target_price_12m": 10.2, "basis": "P/B holds at its 5y median 0.4x [RA] on book grown by a roughly 10% ROE [RA]; the mechanical base fair value of 19.19 is not used because its P/B + ROE method ignores the persistent China regional-bank discount evident in the 0.4x-0.6x 5y range."},
    "bear": {"probability": 0.25, "target_price_12m": 7.4, "basis": "ROE keeps falling from 10.0% TTM [RA] as credit costs rise and P/E reverts to its 5y min of 3.7x [RA] on TTM earnings."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default anchor (base 19.19 x 0.8) is already far above the price, and the stock has sat at 0.4x book for years. What blocks conviction 4 is falling ROE and missing asset-quality disclosure; a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
