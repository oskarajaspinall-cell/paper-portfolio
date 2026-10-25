# Evaluation: Ningxia Baofeng Energy Group (SHA:600989) — 2026-10-24
## Bear case
The low multiples come from earnings at the top of the cycle. TTM gross margin of 40.5%, operating margin of 34.7% and ROIC of 22.2% are the best since FY2021 [Certain]. In the FY2023–FY2024 trough, ROIC was 11.9% and 11.5% [Certain]. P/E of 9.2x on peak earnings is a value trap if olefin–coal spreads go back to normal [Likely]. The mechanical base fair value of 17.79 CNY is below the 21.33 close, so there is no margin of safety [Certain]. That value comes from EV/EBITDA alone, because the through-cycle DCF failed on three years of negative FCF [Certain]. The positive FCF depends on capex staying low. FY2022–FY2024 FCF margins were -11.8% to -14.2%, and if the next capacity phase starts, FCF turns negative again [Likely]. The Q3 2026 results filed 2026-10-21 are unread, so the direction of earnings is unknown [Certain]. Coal-chemical energy policy is a further risk [Likely].
## Bull case
The cost position is real. A coal-fed olefin producer with 35.09% insider ownership earns margins that commodity-chemical peers rarely reach [Likely]. The balance sheet has been repaired: net debt/EBITDA fell from 2.67x to 0.90x TTM, Piotroski F is 8 and Altman Z is 4.31 [Certain]. With capex past its peak, FCF margin reached 21.3% in FY2025 and 22.5% TTM, an 8.66% FCF yield, and the share count fell 1.28% [Certain]. Every earnings multiple is below its own 5-year minimum and below the peer median on P/E and EV/EBITDA [Certain]. The shares are down 25.9% over six months, so part of the fade is already priced in [Likely]. If spreads stay where they are, a re-rating toward the 5-year minimum P/E of 12.6x would add meaningful upside [Guessing].
## Decision
```json
{
  "ticker": "SHA:600989",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost coal-to-olefins producer with a repaired balance sheet looks cheap on trailing multiples, but those multiples rest on five-year-high, cyclical margins, and the price sits above the mechanical base fair value.",
  "rationale": "Strong cash generation and deleveraging are real, but earnings are likely near peak spreads, the only working valuation method puts base value below the price, Q3 2026 results are unread and capex may restart. Good but not compelling, so this is an AVOID. Cash is acceptable.",
  "price_at_decision": 21.33,
  "price_date": "2026-10-23",
  "research_note": "research/SHA-600989/2026-10-24.md",
  "triggers": [
    {"text": "TTM gross margin falls below 30%, the FY2023 trough level, showing the cost advantage does not protect through the cycle (this would rule out a future BUY).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 12%, back to the FY2023-FY2024 capex-phase trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.0x, signalling a new debt-funded capacity phase that would turn FCF negative again.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 29.2, "basis": "Spreads hold and P/E re-rates to its 5y minimum of 12.6x [RA] on TTM earnings. This is below the mechanical bull of 44.02, which applies a median multiple to peak EBITDA."},
    "base": {"probability": 0.45, "target_price_12m": 18.5, "basis": "Margins fade from the TTM 40.5% gross margin toward the FY2025 level of 35.9% [IS], in line with the EV/EBITDA base fair value of 17.79 [fact sheet]."},
    "bear": {"probability": 0.30, "target_price_12m": 12.38, "basis": "Spreads revert to the FY2023-FY2024 trough (ROIC 11.5%-11.9% [RA]), matching the mechanical EV/EBITDA bear value of 12.38 [fact sheet]."}
  },
  "entry_price": 14.23,
  "entry_basis": "valuation file: base 17.79 x 0.8. At that price even a fade to mid-cycle margins would leave a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```
