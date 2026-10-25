# Evaluation: Bank of Jiangsu Co., Ltd. (SHA:600919) — 2026-10-25
## Bear case
The re-rating has already happened: P/E of 6.5x sits above its 5y maximum of 5.9x and P/B of 0.6x is at the top of its 0.4x–0.6x range [RA] [Certain]. Returns are drifting down, with ROE at 10.8% TTM against 12.7% in FY2022 [RA] [Certain], and a 0.6x book multiple is consistent with a cost of equity near that ROE once the 3.5% China risk premium is priced [Guessing]. Asset quality, NIM and provisioning are [data unavailable], so the key bank risk (Chinese property and local credit) cannot be tested [Certain]. Most of the fair-value upside comes from an FCFE leg built on deposit-driven cash flows (FCF conversion of 1,204.0%) that are not meaningful for a bank [Likely]. The DDM leg values the stock below the price [Certain]. The F-score is a middling 4 [ST] [Certain], and Q3 results land on Oct 30, 2026 [Certain].
## Bull case
The stock still trades 18% below the peer median P/B and 6% below on P/E [RA] [Certain], at a discount to book while earning a roughly 11% ROE [Certain]. Net margin has risen from 47.9% to 52.7% over five years [IS] [Certain], suggesting cost and funding discipline. The best-fit P/B + ROE method gives a base of 13.55 and a bull of 15.07, both above the 12.00 close [Certain]. A franchise in a wealthy, industrial province may sustain loan growth better than peers [Guessing]. A beta of -0.07 makes it a diversifier against global equity risk [Certain]. The price is above its 200-day average and up 9.8% over 12 months, so sentiment is not deteriorating [Certain].
## Decision
```json
{
  "ticker": "SHA:600919",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A regional Chinese bank earning a flat-to-falling ~11% ROE has already re-rated to the top of its own 5-year P/B and P/E ranges, and without asset-quality data the residual peer discount is not a compelling edge.",
  "rationale": "Only the distrusted FCFE leg drives the headline fair-value upside; the P/B + ROE method leaves modest upside, and asset quality, NIM and provisioning cannot be checked. Multiples sit at or above five-year highs while ROE drifts down. Good but not compelling: no position.",
  "price_at_decision": 12.00,
  "price_date": "2026-10-23",
  "research_note": "research/SHA-600919/2026-10-25.md",
  "triggers": [
    {"text": "TTM ROE rises above 12.5%, back to the FY2022-FY2023 level, showing returns are recovering rather than drifting down.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12.5}},
    {"text": "TTM ROE falls below 9%, under the FY2021 five-year low of 10.7%, confirming earnings power is eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "TTM net margin falls below 48%, reversing the five-year rise from 47.9% and signalling credit-cost or margin pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 48}},
    {"text": "The Q3 2026 or later results show asset-quality disclosure (NPL ratio or provisioning) that a primary-source filing confirms is stable or improving, removing the main unverified risk."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 15.07, "basis": "ROE holds near 10.8% and the peer P/B discount closes, matching the mechanical P/B + ROE bull value of 15.07 [RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 12.6, "basis": "P/B stays near its 5y high of 0.6x [RA] while book grows with retained earnings at a flat ROE, below the 13.55 P/B + ROE base because ROE is drifting down from 12.7% [RA]; the FCFE-weighted 16.97 blend is set aside as bank cash flows are not meaningful."},
    "bear": {"probability": 0.25, "target_price_12m": 10.0, "basis": "P/B reverts to its 5y median of 0.5x [RA] as ROE slips further or untested property/local-credit losses surface, near the 52-week low of 9.65 [HI]."}
  }
}
```
