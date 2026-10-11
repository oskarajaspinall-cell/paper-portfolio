# Evaluation: Citizens Financial Group, Inc. (CFG) — 2026-10-11
## Bear case
CFG is valued above its own history while profitability keeps slipping. P/B of 1.1x sits above its 5-year maximum of 1.0x, and P/E of 13.8x is at the 82nd percentile of its range and 19% above the peer median of 11.7x [Certain] [RA]. Meanwhile ROE fell from 10.1% (FY21) to 8.3% TTM and net margin from 32.9% to 26.1% [Certain] [RA, IS]. The mechanical fair value ($43.38 base, $56.40 bull) is below the $63.57 close [Certain]. Regional banking has little moat against KEY, RF, FITB, HBAN and MTB, so returns follow the rate cycle [Likely]. The macro overlay tilts toward the bear case: a real-yield back-up of +0.56pp raises the cost of equity on a rich multiple [Likely] (research/CFG/2026-10-11-macro.md). Piotroski F of 4 is middling [Certain] [ST]. The stock is down 9.0% over 3 months and lags SPY by 12.6pp, with Q3 results due Oct 16 [Certain] [HI].
## Bull case
TTM ROE of 8.3% is up from the FY24 trough of 6.2%, so the earnings recovery is underway [Certain] [RA]. FCF conversion of 110.7% and an 8.79% FCF yield fund buybacks, with shares down 2.67% YoY [Certain] [CF, ST]. The Series G preferred redemption simplifies the capital stack [Certain] (Business Wire, 2026-09-01). P/FCF of 11.4x and P/B of 1.1x are 12% and 10% below peer medians [Certain] [ST]. The FCFE DCF base of $62.04 roughly matches the price [Certain]. A steeper curve could lift NIM faster than deposit costs [Guessing]. Even so, the stock only re-rates if ROE returns to around 10%, and the 5-year trend does not yet show that [Likely].
## Decision
```json
{
  "ticker": "CFG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A no-moat regional bank whose ROE and margins have declined for five years trades above its own 5-year P/B range and 19% above peers on P/E, so the price already assumes a profitability recovery the fundamentals have not delivered.",
  "rationale": "Price sits above even the bull fair value; multiples are at or above 5-year highs while ROE and net margin trend down; macro tilt (rising real yields) leans bear. Probability-weighted 12-month value is below the close. Not a high-conviction setup, so no position; cash is acceptable.",
  "price_at_decision": 63.57,
  "price_date": "2026-10-09",
  "research_note": "research/CFG/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROE rises above 10.1%, back to the FY2021 level, showing the five-year profitability decline has reversed.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10.1}},
    {"text": "TTM net margin rises above 27.5% (FY2022 level), showing margin erosion has ended.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 27.5}},
    {"text": "TTM FCF margin rises above 30.5% (FY2021 level), evidencing durable cash earnings power.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 30.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 72.0, "basis": "ROE keeps recovering from the 6.2% FY24 trough toward 10.1% [RA] and P/E holds at 13.8x [RA], retesting the high end of the 52-week range (high 75.33 [HI]), above the $56.40 bull fair value because that model is anchored on depressed 5-year ROE."},
    "base": {"probability": 0.45, "target_price_12m": 53.9, "basis": "P/E reverts from 13.8x to the 11.7x peer median [RA, peers] on flat TTM earnings, landing between the $43.38 blended base fair value and the $62.04 FCFE base; probability shifted from bull to bear for the small bearish macro tilt (research/CFG/2026-10-11-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 46.2, "basis": "P/B reverts from 1.1x to its 5-year median of 0.8x [RA] as rising real yields lift the cost of equity and the ROE slide persists (research/CFG/2026-10-11-macro.md); this sits above the $32.40 bear fair value because buybacks support book per share [ST]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
