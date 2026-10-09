# Evaluation: Hasbro, Inc. (HAS) — 2026-10-09
## Bear case
The cheapness depends on margins that are at a peak. EV/Sales of 3.1x is above its 5-year maximum of 3.0x [Certain] [RA]. So the stock only looks cheap on earnings and FCF because the TTM operating margin (23.6%) and FCF margin (24.4%) sit well above FY2025's 17.7% FCF margin [Certain] [IS,CF]. That uplift comes from one hit-driven franchise. Wizards of the Coast is 58% of revenue, and tabletop grew 30% on Magic releases [Certain] (10-Q). Collectible-card cycles normalise, so if the mix shift stalls, margins revert [Likely]. The P/E is below its 5-year minimum of 20.5x mostly because FY2023/FY2025 earnings were impairment-depressed, not because the stock is cheap [Likely]. Consumer Products still carries tariff and cyber-incident damage [Certain]. Shares rose 1.43% YoY despite buybacks [Certain] [ST]. The 6-month return lags SPY by 15.9pp [Certain] [HI], and Q3 results land on Oct 20 [Certain].
## Bull case
Returns have been transformed. ROIC went from 10.4% in FY21 to 28.3% TTM and gross margin from 50.5% to 63.8% [Certain] [RA,IS]. Net debt/EBITDA fell from 5.72x to 1.92x [Certain] [RA]. Magic and D&D have 30-year network effects that toy peers cannot copy [Likely]. At 92.50 the FCF yield is 9.30% [ST]. P/FCF of 10.8x and EV/EBITDA of 12.0x sit near their 5-year minimums (10.4x / 11.7x) [Certain] [RA]. The reverse DCF implies -8.9% revenue growth next year against double-digit YTD growth [Certain] [FV]. The mechanical base fair value is 124.54 [FV]. Beta is 0.44 [ST], and the macro overlay rates macro as context only [Certain]. Licensing deals such as Upper Deck extend the IP flywheel [Likely]. Reported Mattel interest adds optionality [Guessing].
## Decision
```json
{
  "ticker": "HAS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Hasbro's Wizards-driven mix shift has lifted ROIC to 28.3% and the FCF yield to 9.30%, but with EV/Sales above its 5-year maximum, the valuation rests on peak margins from a hit-driven card franchise.",
  "rationale": "The business is good, but the stock is not compellingly cheap. It looks inexpensive only on TTM margins well above FY2025, while EV/Sales is above its 5-year maximum and 58% of revenue depends on one card-game cycle. Q3 results on Oct 20 could reset that. Conviction 3 is below the buy threshold, so AVOID and hold cash.",
  "price_at_decision": 92.50,
  "price_date": "2026-10-08",
  "research_note": "research/HAS/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 18%, under the FY2024 level of 18.3%, which would show the Wizards-driven margin gain was a release-cycle peak.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM gross margin falls below 55%, which would mean the mix shift toward Wizards of the Coast is reversing and the thesis is broken.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "Net debt/EBITDA rises back above 3.0x, reversing the deleveraging from 5.72x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "Wizards of the Coast & Digital Gaming segment revenue growth (10-Q MD&A) falls below high-single digits for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.30, "target_price_12m": 124.54, "basis": "Wizards-led margins (23.6% operating, 24.4% FCF [IS,CF]) prove durable, and the price reaches the fact sheet's mechanical base fair value of 124.54 [FV], with the DCF at 130.08."},
    "base": {"probability": 0.40, "target_price_12m": 92.50, "basis": "Below the 124.54 base fair value [FV], because that DCF capitalises a TTM FCF margin of 24.4% vs 17.7% in FY2025 [CF,IS]; EV/EBITDA stays near 12.0x, close to its 5-year minimum of 11.7x [RA], as peak-margin doubt persists."},
    "bear": {"probability": 0.30, "target_price_12m": 69.50, "basis": "The Magic release cycle normalises and margins revert toward FY2024's 18.3% operating margin [IS], so the price returns to its 52-week low of 69.50 [HI]; this sits above the 34.99 bear fair value [FV] because the 1.92x leverage and 63.8% gross margin [RA,IS] do not support the 7.84 DCF-bear collapse."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
