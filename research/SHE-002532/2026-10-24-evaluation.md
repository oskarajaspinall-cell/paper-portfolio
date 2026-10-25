# Evaluation: Tianshan Aluminum Group Co.,Ltd (SHE:002532) — 2026-10-24
## Bear case
This is a commodity smelter priced on cycle-high economics. TTM gross margin of 33.4% compares with 14.1% in FY2023, and ROIC swung from 17.8% to 7.5% and back to 18.5% within five years [Certain]. The low multiples (P/E 7.5x, P/FCF 7.1x, both below their 5y minimums) sit on peak earnings, so they likely price in mean reversion rather than offer a margin of safety [Likely]. The through-cycle DCF base is 7.59 and the blended base fair value 8.28, both below the 11.29 close, while the reverse DCF needs 9.4% year-1 revenue growth [Certain]. On EV/EBITDA and EV/Sales it is dearer than peers [Certain]. The trend is poor: down 36.1% over 6 months, with the 50-day average 16.0% below the 200-day [Certain]. Results due Oct 30, 2026 add gap risk, and the 3.5% China country premium applies [Certain]. No moat can be verified from the fact sheet [Guessing].

## Bull case
The cash is real. FCF conversion is 105.5% TTM, the FCF yield is 14.07%, and net debt/EBITDA fell from 2.93x (FY2023) to 0.50x [Certain]. Piotroski 8 and Altman Z 3.69 point to a sound balance sheet, and shares are down 1.82% YoY [Certain]. P/E is 21% and P/FCF 20% below the peer median [Certain]. If the cost position (likely captive power) keeps margins structurally higher than in FY2022-23, the mechanical through-cycle model understates value, and the bull fair value of 17.66 is within reach [Guessing]. A 0.74 beta and deleveraging limit financial-distress risk [Likely]. Still, none of this is evidence that today's margins can last, and the business case rests on that [Likely].

## Decision
```json
{
  "ticker": "SHE:002532",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-capitalised, cash-generative aluminium smelter looks cheap only on cycle-high margins; on through-cycle earnings the price sits above base fair value, so there is no margin of safety.",
  "rationale": "Strong cash conversion and a clean balance sheet, but TTM margins are far above the FY2022-23 trough and the through-cycle DCF base is below the price. Multiples below the 5y minimum reflect peak earnings, not a mispricing. The trend is negative and results are due in days. Good but not compelling: AVOID, with a margin-of-safety entry price.",
  "price_at_decision": 11.29,
  "price_date": "2026-10-23",
  "research_note": "research/SHE-002532/2026-10-24.md",
  "triggers": [
    {"text": "TTM gross margin rises above 33.4% after the Oct 30, 2026 results, evidence that margins are holding up rather than reverting to the cycle average.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 33.4}},
    {"text": "TTM ROIC rises above 18.5%, showing returns are still rising at this point in the cycle.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 18.5}},
    {"text": "TTM FCF margin holds above 23.0%, confirming cash generation is not peaking.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 23.0}},
    {"text": "Net share count shrinks faster than the current 1.82% YoY, showing peak cash is being returned to shareholders.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": -1.82}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 17.66, "basis": "Margins prove structurally higher on a cost advantage and the price reaches the mechanical bull fair value of 17.66 (fact sheet Fair value; FCF yield 14.07% [ST])."},
    "base": {"probability": 0.5, "target_price_12m": 9.65, "basis": "Margins partly revert from the 33.4% TTM gross margin [IS] and the price converges on the EV/EBITDA base of 9.65 (fact sheet Fair value), between the through-cycle DCF base of 7.59 and the close."},
    "bear": {"probability": 0.3, "target_price_12m": 7.1, "basis": "Aluminium spreads fall back toward FY2023 levels (gross margin 14.1%, ROIC 7.5% [RA]) and the price falls to the EV/EBITDA bear of 7.10 (fact sheet Fair value); the DCF bear of 1.26 is ignored as too extreme for a 0.50x-levered business."}
  },
  "entry_price": 6.62,
  "entry_basis": "valuation file: base 8.28 x 0.8 (20% margin of safety on the blended base fair value [IS,BS,CF,RA,ST]).",
  "replaces": null,
  "replacement_reason": null
}
```
