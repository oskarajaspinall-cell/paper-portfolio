# Evaluation: JCHX Mining Management Co.,Ltd. (SHA:603979) — 2026-10-31
## Bear case
The close of CNY 58.15 sits above the mechanical base fair value of CNY 44.17, so there is no margin of safety on intrinsic value [Certain]. The "cheap" signal is against the stock's own history at a time of record returns: TTM operating margin of 27.9% and ROIC of 26.3% are five-year highs, and a contract miner is normally a price-taker whose owned-resource earnings ride the commodity cycle [Likely]. P/E 12.8x below its 5y minimum may simply be the market capitalising peak earnings [Likely]. Cash conversion is erratic (FCF/NI -105.0% in FY2022, 62.9% TTM) and shares rose 2.26% YoY [Certain]. The 21.5% three-month fall followed Q3 results that the research did not read, so the cause is unknown [Certain]. NAV, the best method for a miner, is [data unavailable], leaving the valuation on one method [Certain].
## Bull case
Returns have risen every year: ROIC from 11.2% in FY2021 to 26.3% TTM, operating margin from 15.7% to 27.9% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.23x) with Piotroski F of 7 and Altman Z of 4.47 [Certain]. EV/EBITDA of 6.0x is below its 5y minimum of 7.7x and in line with peers at 6.1x, and the FCF yield is 5.33% [Certain]. Contract mining carries switching costs and know-how in hard jurisdictions, which may make part of the margin gain durable [Guessing]. If margins hold, a re-rating toward even the bottom of its own EV/EBITDA range would carry the price well above today [Likely]. Macro is context only, with no stress in the overlay [Likely].
## Decision
```json
{
  "ticker": "SHA:603979",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash contract miner with ROIC rising to 26.3% trades below its own 5y multiples, but on likely peak-cycle margins and above its mechanical base fair value, with an unexplained post-results fall.",
  "rationale": "Quality trend is genuinely strong, but the price exceeds base fair value, margins look cyclical-peak, NAV is unavailable and the Q3 results behind the 21.5% fall are unread. The probability-weighted scenarios sit below the price. Good, not compelling: AVOID, watch for an entry well below base fair value.",
  "price_at_decision": 58.15,
  "price_date": "2026-10-30",
  "research_note": "research/SHA-603979/2026-10-31.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, back to the FY2023 level, showing the returns expansion was cyclical.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 20%, reversing most of the expansion from 15.7% and confirming peak-cycle margins.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 1.0x (-0.23x TTM now), showing capex is again outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "TTM FCF margin turns negative (12.2% now), repeating the FY2022-FY2023 cash burn.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 89.77, "basis": "Margins hold near 27.9% TTM [IS] and EV/EBITDA re-rates toward its 5y minimum of 7.7x [RA], retesting the 52-week high of 89.77 [HI]; below the mechanical bull of 116.50, which assumes a full return to the 12.0x median."},
    "base": {"probability": 0.5, "target_price_12m": 50.0, "basis": "EV/EBITDA stays near the 6.1x peer median [RA] while operating margin eases from the 27.9% peak [IS], landing between the mechanical base of 44.17 and the current price."},
    "bear": {"probability": 0.3, "target_price_12m": 29.08, "basis": "Commodity-linked margins revert toward FY2023 levels (operating margin 20.4% [IS]) and the stock trades at the mechanical bear fair value of 29.08 [fact sheet Fair value]."}
  },
  "entry_price": 35.34,
  "entry_basis": "valuation file: base 44.17 x 0.8; only at that margin of safety would peak-cycle margin risk and the single-method valuation justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
