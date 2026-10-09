# Evaluation: Automatic Data Processing, Inc. (ADP) — 2026-10-09
## Bear case
The price already discounts more than the business has shown. At $270.73, ADP trades above the fact sheet's base fair value ($228.49, -15.6%) and even its bull case ($249.39, -7.9%). The reverse DCF needs 11.6% year-1 revenue growth, which the note judges well above ADP's recent organic trajectory [Likely]. The stock has re-rated +34.8% in six months, so the cheap entry is gone. On P/FCF (+22%) and P/B (+30%) it is also dearer than peers [Certain]. The macro overlay tilts small toward bear: the 10y real yield is 2.92% (+0.61pp over 3m), which pressures a premium multiple [Likely]. Weekly NER prints of 12,000–23,750 jobs a week point to soft hiring, a headwind for per-employee billing [Guessing]. Client-fund interest income turns into a drag if rates fall [Likely].
## Bull case
This is one of the highest-quality compounders in the index. ROIC is 60.5%, the operating margin 26.5% (+3.1pp over 5y) and the FCF margin 23.9% (+6.2pp), with FCF/NI at 118.8% [Certain]. The moat is real: switching costs, a ~13-year average client life in Employer Services, and payroll built into tax-authority and bank systems [Certain]. Net debt/EBITDA is only 0.20x and the share count fell 1.32% YoY [Certain]. On its own history it isn't stretched: P/E sits at the 43rd percentile and EV/EBITDA at 16.9x, -23% vs peers [Certain]. Higher fed funds (3.88%) support float income [Likely]. Margins are expanding ahead of targets, and Lyric is driving enterprise bookings [Likely]. Twelve-month relative strength of -23.2pp vs SPY leaves room to catch up if FQ1 (Oct 28) confirms the trend [Guessing].
## Decision
```json
{
  "ticker": "ADP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "ADP is an exceptional 60%-ROIC, 24%-FCF-margin payroll franchise, but at $270.73 it trades above even its bull-case fair value, and the reverse DCF needs 11.6% growth the business has not shown, so there is no margin of safety.",
  "rationale": "Quality is top-tier, but the valuation is not attractive. The price sits 7.9% above the bull fair value after a +34.8% six-month re-rating. The macro tilt (rising real yields) leans bearish. The probability-weighted 12-month outcome is below the current price. That makes ADP good but not compelling: conviction 3, so AVOID and keep the cash.",
  "price_at_decision": 270.73,
  "price_date": "2026-10-08",
  "research_note": "research/ADP/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 20%, reversing most of the five-year rise from 17.7% to 23.9% and undermining the cash-compounding case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 25%, under the FY2023 level of 25.3%, showing the margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 50%, under the FY2022 five-year low of 50.4%, signalling erosion of the moat economics.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "Fiscal-year revenue growth (income statement) reaches the 11.6% the reverse DCF implies, which would justify the price and turn this into a BUY candidate."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 292.44, "basis": "FQ1 confirms margin expansion and Lyric-led bookings (note, Citi TMT transcript [OV]); EV/Sales moves toward the top of its 5y range (6.2x max [RA]), matching the EV/Revenue bull fair value of 292.44 and the 52-week high of 292.80 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 276.22, "basis": "Multiples hold near the 5y median (EV/Sales 5.1x vs 4.9x now [RA]), matching the EV/Revenue base fair value of 276.22; this sits above the 228.49 blended base because the DCF at a 5.28% risk-free rate has historically undervalued ADP relative to the multiples the market pays."},
    "bear": {"probability": 0.35, "target_price_12m": 222.02, "basis": "Soft hiring (NER weekly prints [OV]) and real yields rising further (macro overlay research/ADP/2026-10-09-macro.md, tilt small toward bear, which lifts this probability from 0.30 to 0.35) push EV/Sales toward its 4.1x 5y minimum [RA], i.e. the EV/Revenue bear fair value of 222.02, close to the 228.49 blended base fair value."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
