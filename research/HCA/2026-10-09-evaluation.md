# Evaluation: HCA Healthcare, Inc. (HCA) — 2026-10-09
## Bear case
The price already discounts the good news. At 445.01 USD, HCA trades on 14.9x P/E, in the 81st percentile of its own 5y range, and at a 73% P/E premium to peers [Certain]. The blended fair value is 396.35, 10.9% below the price, and the reverse DCF implies 6.8% year-1 revenue growth [Certain]. That growth looks optimistic while ACA-exchange attrition costs about $400m of EBITDA [Likely]. Net margin fell 2.9pp over 5y to 8.8% [Certain]. Buybacks (shares -8.97% YoY) have flattered EPS while net debt/EBITDA rose to 3.20x and Altman Z sits at 2.64 [Certain]. The macro overlay flags a moderate bear tilt: real yields are up 0.49pt and HY spreads up 0.41pt in a month, which hits a levered, premium-multiple name [Likely]. Q3 results on Oct 27 are a near-term event risk if the Medicaid supplemental-payment offsets fade [Guessing].

## Bull case
HCA is the highest-quality operator in its group. ROIC is 21.8% and ROCE 26.3%, up 3.5pp over 5y, while gross margin rose 3.2pp to 42.6% [Certain]. Certificate-of-Need laws and metro density protect pricing [Likely]. FCF conversion is 87.7% TTM, with FY2025 above 100%, and the FCF yield is 6.22% [Certain]. Management reports strong demand and modest share gains [Likely]. On EV/EBITDA the stock is only mid-range (9.3x vs a 9.1x median), so a clean Q3 print could re-rate it toward the 571.97 bull value [Guessing]. Piotroski F of 7 shows broad fundamentals intact [Certain].

## Decision
```json
{
  "ticker": "HCA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A high-return hospital franchise whose price sits above its own-history fair value and at a large peer premium, with payer-mix headwinds, rising leverage and a hawkish rate backdrop leaving no margin of safety.",
  "rationale": "Quality is real, but the valuation is not attractive. The price is 10.9% above the base fair value, P/E is in the 81st percentile of its 5y range, and the reverse DCF needs 6.8% growth against exchange headwinds. Leverage is rising and the macro tilt is toward bear. The probability-weighted target is below the price, so this is no position.",
  "price_at_decision": 445.01,
  "price_date": "2026-10-08",
  "research_note": "research/HCA/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin rises above the FY2025 level of 10.2%, showing cash generation is absorbing the exchange-patient headwind (would raise the fair value).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 10.2}},
    {"text": "TTM net margin rises back above the FY2022 level of 9.4%, showing the payer-mix pressure was transitory.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 9.4}},
    {"text": "Net debt/EBITDA falls below 2.81x (the FY2021 level), showing buybacks no longer come at the cost of balance-sheet slack.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.81}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 571.97, "basis": "Payer-mix headwind proves transitory, yields roll over and the DCF bull case of 571.97 is reached on a rising ROCE (+3.5pp over 5y [RA]) and >100% FY2025 FCF conversion [CF,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 404.48, "basis": "EV/EBITDA reverts to around its 5y median of 9.1x [RA] on TTM EBITDA, matching the EV/EBITDA fair value of 404.48 [IS,BS,RA], because the 6.8% growth the reverse DCF implies is not delivered against the $400m exchange headwind (Q2 2026 transcript [OV])."},
    "bear": {"probability": 0.3, "target_price_12m": 298.05, "basis": "Net margin keeps falling (-2.9pp over 5y to 8.8% [IS]) and net debt/EBITDA rises (3.20x [RA]) while real yields and HY spreads widen. The macro overlay's moderate bear tilt (research/HCA/2026-10-09-macro.md) lifts this probability from 0.25 to 0.3, toward the 298.05 bear fair value."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
