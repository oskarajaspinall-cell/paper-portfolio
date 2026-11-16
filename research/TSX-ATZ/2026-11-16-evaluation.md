# Evaluation: Aritzia Inc. (TSX:ATZ) — 2026-11-16
## Bear case
The entry hit came from the price drifting to our level, not from a stock-specific fall: no results shock, and the close sits 13.9% above its 200-day average after a +53.3% year [Certain]. So there is no overreaction to buy. The price already equals the mechanical bull fair value (155.38) and implies 29.8% year-1 revenue growth; the base is 72.08 [Certain]. EV/Sales 4.2x and P/B 11.8x sit above their five-year maxima, and the P/E premium to peers is 157% [Certain]. An extended price risks a sharp de-rating if US growth slows from the investor-day plan's 15%-17% pace; beta is 1.70 [Likely]. Fashion brands are fickle and the five-year operating and FCF margin record is volatile (FY2024 operating margin 6.8%, FY2023 FCF margin -2.2%) [Certain]. US revenue share and any apparel tariff are unquantified (macro overlay) [Guessing].
## Bull case
The business is working: TTM ROIC 25.2% vs 16.0% a year earlier, gross margin 46.9% (a five-year high), operating margin 16.5% and FCF margin 15.3%, all at their two-year highs [Certain]. The five-year "falling" labels on operating and FCF margin reflect the FY2024 trough as a start point, not decay; the last 12 months rose strongly, so the direction change is a recovery, not a threat [Likely]. Q2 beat management's expectations and guidance was lifted; the five-year plan targets 15%-17% annual growth with about 100 bps of EBITDA margin expansion [Likely]. Net debt/EBITDA is 0.78x, Altman Z 6.29, FCF conversion 112.5% [Certain]. P/E 30.2x is at the 22% position of its own five-year range and P/FCF at 36%, so on own history the multiple is not stretched [Certain]. The DCF likely undercounts the US runway [Guessing].
## Decision
```json
{
  "ticker": "TSX:ATZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No metric is falling over 1 or 3 years: ROIC, operating margin and FCF margin are all rising and at their 2-year highs [RA-T, IS-T, CF-T]; the 5-year 'falling' labels start from the FY2022 peak before the FY2024 trough.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The price already discounts the five-year plan (reverse DCF 29.8% year-1 growth, price at the mechanical bull value); any slowdown in US growth or a fashion miss would de-rate a high-beta stock trading well above its 200-day average.",
    "veto": null
  },
  "thesis": "A high-return, self-funding women's apparel brand whose US expansion is driving rising margins and ROIC, but whose price already sits at the mechanical bull value and pays for the five-year plan.",
  "rationale": "Quality and momentum are excellent, but the entry hit was a rise, not a dip, and the price equals the bull fair value with a 29.8% implied growth rate. The scorecard gives conviction 3: good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 155.45,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-ATZ/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 43%, giving up the move to a five-year high and signalling markdowns or lost pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 43}},
    {"text": "TTM ROIC falls below 15%, back under the level of a year earlier, showing the US expansion is not earning its returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 12%, reversing the last year's recovery.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.0x, showing the store roll-out is outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 190, "basis": "The plan's 15%-17% growth and margin expansion are delivered and the P/E moves from 30.2x toward its 5y median 36.4x [RA] on rising earnings; above the mechanical bull 155.38 because the history-based model cannot see the US runway."},
    "base": {"probability": 0.45, "target_price_12m": 150, "basis": "Earnings grow with guidance but the P/E drifts lower within its 5y range [RA] as the market already prices the plan (reverse DCF 29.8% year-1 growth [IS,ST]); well above the mechanical base 72.08 because the DCF ignores the improved ROIC of 25.2% [RA-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 100, "basis": "A US slowdown or fashion miss de-rates the P/E to its 5y min 24.7x [RA] on lower earnings, back toward the 52-week low of 96.73 [HI]; above the mechanical bear 2.50, which reflects an unreliable negative DCF."}
  },
  "entry_price": 61.27,
  "entry_basis": "valuation file: base 72.08 x 0.85. The obstacle is price: the business is improving, but at today's level the value blend sits far below the price.",
  "replaces": null,
  "replacement_reason": null
}
```
