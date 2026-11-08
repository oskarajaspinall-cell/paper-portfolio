# Evaluation: Chailease Holding Company Limited (TPE:5871) — 2026-11-08
## Bear case
This looks like a value trap. ROE has fallen every year, from 21.0% in FY2021 to 11.0% in FY2025 (11.3% TTM), and ROIC from 3.9% to 2.3% TTM [RA] [Certain]. The rolling-12-month ROIC is flat, but it is still below its 2.7% 2-year high [RA-T], so the decline has paused, not reversed [Likely]. A P/E of 9.1x and P/B of 0.9x [RA] already price in returns staying low. The mechanical bear value of 104.79 is close to the price, so there is little buffer if credit costs rise [Likely]. The China and ASEAN loan exposure is unsized, and the overlay leaves China credit and regulation as an open, unquantified risk (research/TPE-5871/2026-11-08-macro.md) [Likely]. The fact sheet shows no margins, leverage or credit-loss data, so book quality cannot be checked [Certain]. Results are due Nov 12, a binary event [Certain].
## Bull case
Every multiple is below its own 5-year minimum. P/E is 9.1x against a 9.4x–19.6x range (median 12.7x), P/B 0.9x against a 0.9x median-1.9x range, and P/FCF 8.0x with a 12.55% FCF yield [RA,ST] [Certain]. Taiwanese financial peers trade at a median 19.0x P/E and 2.0x P/B [Certain], though as banks they are imperfect comparables [Likely]. The base fair value is 142.28 [fact sheet] [Certain]. ROE near 11% is still respectable for a lender at book value [Likely], and the flat rolling ROIC suggests the erosion may be bottoming [Guessing]. The share count is falling slightly (-0.23% YoY) and beta is 0.67 [ST] [Certain]. If the Nov 12 results show stable credit and ROE, the stock could move back toward its median multiple [Guessing].
## Decision
```json
{
  "ticker": "TPE:5871",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A regional SME leasing franchise trading below its own 5-year minimum P/E and P/B, but with ROE halved since FY2021, unsized China credit exposure and no visible margin or credit-loss data, so cheapness alone does not establish an edge.",
  "rationale": "The multiples are cheap, but returns have fallen for four years and only paused in the last twelve months. The China exposure and credit quality cannot be checked from the available data, and results are four days away. That makes this good but not compelling: conviction 3, so no position.",
  "price_at_decision": 102.00,
  "price_date": "2026-11-06",
  "research_note": "research/TPE-5871/2026-11-08.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock already trades below base fair value 142.28 x 0.8, and the issue is falling ROE and unverifiable China/ASEAN credit quality. A lower price would not change the decision; evidence of an ROE recovery would.",
  "triggers": [
    {"text": "TTM ROE recovers above the FY2024 level of 13.5%, showing the multi-year return erosion has reversed.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13.5}},
    {"text": "TTM ROIC rises above its 2-year high of 2.7% on the trailing ratios page, confirming the spread business is re-earning.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 2.7}},
    {"text": "Shares outstanding rise more than 3% year on year (dilutive capital raising to fund the book or cover losses), which would deepen the bear case.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140.0, "basis": "ROE stabilises near 11.3% and P/E re-rates toward its 5y median 12.7x [RA], close to the mechanical base/bull fair value of 142.28-143.95 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 112.0, "basis": "ROIC stays flat as the rolling table shows [RA-T] and P/E recovers only partway from 9.1x toward its 9.4x 5y minimum and beyond [RA]; below the mechanical base of 142.28 because that assumes a median multiple that a four-year ROE decline from 21.0% to 11.0% [RA] does not support."},
    "bear": {"probability": 0.30, "target_price_12m": 85.0, "basis": "ROE keeps falling on China/ASEAN credit costs, the open, unsized risk in the overlay (research/TPE-5871/2026-11-08-macro.md), and P/B stays below its 0.9x 5y minimum [RA]; below the mechanical bear of 104.79 because that P/E method uses TTM earnings that a credit-cost rise would cut."}
  }
}
```
