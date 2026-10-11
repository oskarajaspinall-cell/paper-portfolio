# Evaluation: Capgemini SE (EPA:CAP) — 2026-10-11

## Bear case
This is not a post-earnings drift. The 2026-10-01 jump (+7.4% on 2.9x volume) came more than two months after the 2026-07-30 H1 results, and no cited release explains it [Certain]. So the setup's edge, a results beat the market is still digesting, is missing; what's left is an unexplained momentum spike [Likely]. The volatility stop at 99.85 sits 13.2% below the close. To reach 2:1, the target has to be 145.45, +26.4% in eight weeks, from a stock whose 50-day average is only +0.4% above its 200-day [Certain]. That is a shallow trend. Fundamentals are softening: TTM ROIC is 9.5% against 13.9% in FY2023, FCF margin is falling, and net debt/EBITDA has risen to 2.56x from 1.03x [Certain]. Altman Z of 2.20 is grey-zone [Certain]. The stock is at a 6-month high with RSI at 64.4, so it is chasing, not buying a dip [Likely].

## Bull case
The price action is strong. The stock still holds 138% of the jump six sessions on, is +29.3% over three months, and its relative strength against SPY over 3 months is +25.7pp [Certain]. Overhead looks clear: the 52-week high of 153.05 sits above the 145.45 target [Certain]. Valuation does not create crowding or gap risk. EV/EBITDA of 8.2x and P/FCF of 8.9x are below their 5-year minimums, the FCF yield is 11.21%, and the reverse DCF implies -5.9% growth [Certain]. Mechanical fair value (bear 142.13, base 175.65) sits above the price [Certain]. The 2026-09-12 sale of Capgemini Government Solutions and management's AI-modernisation narrative could support a re-rating [Guessing]. Next earnings (2027-02-16) fall outside the trade window, so there is no event gap [Certain].

## Decision
```json
{
  "ticker": "EPA:CAP",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "An unexplained, non-earnings momentum spike in a shallow-trend IT-services stock offers no clear drift edge to justify a 13.2% volatility stop and a +26.4% eight-week target.",
  "rationale": "The drift setup requires a real results beat that the price is still digesting. The jump came two months after H1 results, with no cited cause, so the edge is unproven. A 2:1 plan needs +26.4% in eight weeks from a shallow trend, at a 6-month high. Good but not compelling: AVOID, keep cash.",
  "price_at_decision": 115.05,
  "price_date": "2026-10-09",
  "research_note": "research/EPA-CAP/2026-10-11.md",
  "exit_plan": {"target": 145.45, "stop": 99.85, "time_limit": "2026-12-06"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 175.65, "basis": "Price re-rates to the fact sheet's base fair value of 175.65 [IS,BS,CF,RA,ST,HI] as EV/EBITDA recovers from 8.2x toward its 5y median of 10.9x [RA]."},
    "base": {"probability": 0.50, "target_price_12m": 125.19, "basis": "Set at the EV/EBITDA bear value of 125.19, below the 175.65 blended base, because TTM ROIC (9.5%) and FCF margin (9.3%) are falling and net debt/EBITDA has risen to 2.56x [RA,CF,IS], so the history-based DCF looks too generous."},
    "bear": {"probability": 0.25, "target_price_12m": 85.62, "basis": "The unexplained 2026-10-01 spike fades and the price retests the 6-month low of 85.62 [HI], consistent with the 52-week change of -5.7% and relative strength vs SPY of -21.4pp [ST,HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
