# Evaluation: Bank of Nanjing Co., Ltd. (SHA:601009) — 2026-10-19
## Bear case
Returns are eroding every year: ROE fell from 13.8% (FY2021) to 10.7% TTM [Certain] [RA], consistent with China-wide margin compression that shows no sign of turning [Likely]. Shareholders are paying more for less: P/E of 6.7x sits at the 96% point of its own 5y range (4.4x–6.8x) [Certain] [RA], so the re-rating has already happened while earnings power declined. The mechanical base fair value of 15.78 CNY is flattered by the FCFE leg (20.17 CNY), built on bank cash flows the note itself says to disregard (FCF conversion 854.3% TTM) [Certain] (note §2, §5); the best-fit P/B + ROE method alone gives 13.58 CNY [Certain]. Credit quality, the key risk for a regional lender, cannot be verified from stockanalysis.com [Certain] (note §2). Piotroski F-Score is only 4 [Certain] [ST], and dividend data is unavailable [Certain].
## Bull case
At 0.7x P/B, in line with peers' 0.7x and with ROE still 10.7%, the bank earns well above what the price implies [Certain] [RA]. Net margin has risen to 53.5% TTM (+2.4pp over five years) [Certain] [IS], so cost and provisioning discipline is holding while revenue yield compresses [Likely]. No dilution: shares change YoY 0.00% [Certain] [ST]. The reverse DCF implies -9.4% revenue growth in year 1 [Certain] (fact sheet), a pessimistic bar for a lender in wealthy Jiangsu [Likely]. Even the P/B + ROE bear value of 13.10 CNY sits above the 11.74 close [Certain]. Beta of -0.02 makes it a portfolio diversifier [Certain] [ST]. If ROE merely stabilises near 11.0% (FY2025), the stock could re-rate toward the P/B + ROE base [Guessing].
## Decision
```json
{
  "ticker": "SHA:601009",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cheap-looking Jiangsu regional bank at 0.7x book whose ROE is still falling every year, with its P/E already at the top of its own range and credit quality unverifiable.",
  "rationale": "Optically cheap on P/B, but ROE has declined every year and P/E is near its 5y high, so the re-rating is spent. The headline fair value leans on FCFE built from distorted bank cash flows; P/B + ROE alone offers modest upside. Credit quality cannot be checked. Good but not compelling: AVOID.",
  "price_at_decision": 11.74,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601009/2026-10-19.md",
  "triggers": [
    {"text": "ROE falls below 9% (TTM 10.7%), showing margin or asset-quality erosion beyond the trend already seen.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "Net (profit) margin drops below 45% (TTM 53.5%), a step-down in net interest or fee economics.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}},
    {"text": "Shares outstanding rise more than 2% YoY (now 0.00%), signalling a dilutive capital raise forced by asset-quality stress.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}},
    {"text": "Reported ROE stabilises at or above the FY2025 level of 11.0% in the Q3 2026 results due Oct 29, 2026, which would lift conviction (no statistics check: needs the trend, not a level)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 14.28, "basis": "ROE stabilises near FY2025's 11.0% [RA] and the price re-rates toward the blended bear fair value of 14.28 CNY, above the P/B + ROE base of 13.58 CNY (fact sheet fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 12.2, "basis": "P/B holds at 0.7x [RA] as ROE drifts slightly lower; below the mechanical base of 15.78 CNY because its FCFE leg (20.17 CNY) rests on bank cash flows the note says to disregard (note §2) and P/E is already at the 96% point of its 5y range [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 9.85, "basis": "ROE keeps falling from 10.7% TTM toward the 9% trigger [RA] and P/E reverts toward its 5y median of 6.0x [RA], taking the price back to its 52-week low of 9.85 CNY [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at 0.7x P/B the stock already trades below every mechanical fair value; what blocks conviction 4 is the unbroken annual ROE decline and unverifiable credit quality, so a lower price alone would not change the decision; evidence of ROE stabilising would.",
  "replaces": null,
  "replacement_reason": null
}
```
