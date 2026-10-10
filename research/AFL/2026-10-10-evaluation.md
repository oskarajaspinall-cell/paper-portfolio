# Evaluation: Aflac Incorporated (AFL) — 2026-10-10
## Bear case
At 114.54 the stock already sits at the model's base fair value of 116.44 (+1.7%), so there is no margin of safety [Certain]. Returns stepped down sharply: ROE fell from 22.6% (FY2024) to 13.1% (FY2025) and ROIC from 16.7% to 9.8%, and the note's "one-off Japan repositioning" explanation comes from management, not the numbers [Likely]. Net debt/EBITDA rose from 1.48x to 2.67x TTM [Certain]. The macro overlay tilts small toward bear: the 10y yield is up 68bp in 3 months and the dollar is firmer, which erodes book value (AOCI) under the P/B-based fair value and cuts reported yen earnings [Likely]. The stock is lagging SPY by 13.3pp over 12 months and Piotroski is a middling 5 [Certain]. FCF metrics are [data unavailable], so cash conversion cannot be verified [Certain].

## Bull case
AFL trades at 12.2x P/E and 11.1x EV/EBITDA, 18-26% below the peer median, with P/B of 1.9x under its own 5y median of 2.2x [Certain]. TTM ROE has already recovered to 16.9% from 13.1% in FY2025, which supports reading the dip as transitory [Certain]. Buybacks cut the share count 5.75% YoY [Certain]. The worksite and Japan distribution moat is durable, and US lines are scaling [Likely]. If ROE normalises toward the FY2023-24 level of ~22%, the P/B+ROE bull value of 176.21 and the blended bull of 150.45 are reachable [Guessing]. Beta of 0.56 and short interest of 2.33% point to low crowding risk [Certain].

## Decision
```json
{
  "ticker": "AFL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A durable supplemental-insurance franchise with buybacks and a peer discount, but priced at its base fair value after a FY2025 returns step-down, with rate and dollar headwinds to book value and reported earnings.",
  "rationale": "Quality is good, but the price (114.54) already sits at the base fair value (116.44), so there is no margin of safety. ROE/ROIC fell sharply in FY2025 and only partly recovered, leverage is rising and the macro tilt is toward bear. A good business at a fair price is not compelling. Cash is acceptable.",
  "price_at_decision": 114.54,
  "price_date": "2026-10-09",
  "research_note": "research/AFL/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, under the FY2025 trough of 13.1%, showing the returns step-down is structural rather than a one-off Japan repositioning effect.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 9%, under the FY2025 low of 9.8%, confirming capital efficiency is deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA (ratios page, standard definition) rises above 3.0x from 2.67x TTM, showing leverage is becoming a balance-sheet risk."},
    {"text": "US segment premium growth in the quarterly earnings release stays below management's 3-6% target range for two consecutive quarters, showing the newer US lines are failing to scale."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 150.45, "basis": "TTM ROE keeps recovering from 13.1% (FY2025) to 16.9% and on toward the FY2023-24 ~22% level [RA], lifting the blended P/B+ROE/P/E value to the fact sheet's bull fair value of 150.45; probability trimmed for the macro overlay's small bear tilt (research/AFL/2026-10-10-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 116.44, "basis": "ROE holds near the TTM 16.9% [RA] and buybacks (-5.75% shares YoY [ST]) offset modest growth, so the price converges on the fact sheet's base fair value of 116.44."},
    "bear": {"probability": 0.3, "target_price_12m": 89.38, "basis": "The macro overlay's small toward-bear tilt (10y +68bp/3m, firmer dollar; research/AFL/2026-10-10-macro.md) erodes AOCI/book value and reported Japan EPS while ROE drifts back toward FY2025's 13.1% [RA], pulling value to the fact sheet's bear fair value of 89.38; probability raised from 0.25 for that tilt."}
  },
  "entry_price": 93.15,
  "entry_basis": "valuation file: base 116.44 x 0.8 = 93.15 (20% margin of safety); at that level the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
