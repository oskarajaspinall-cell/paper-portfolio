# Evaluation: Viatris Inc. (VTRS) — 2026-10-12
## Bear case
This is a low-return generics book that has already re-rated: the stock is up 82.1% in 12 months and sits above its own 5-year maximum on EV/EBITDA (7.5x vs 7.1x), P/FCF (10.4x vs 7.5x) and P/B (1.4x vs 1.0x) [Certain]. TTM ROIC of 5.9% is likely below the cost of capital, net margin is -2.8% and ROE -2.8% after repeated impairments [Certain]. Altman Z of 1.10 is in the distress zone [Certain]. Management is now redirecting deleveraging cash into a $1.65bn cash purchase of Pacira, which should push net debt/EBITDA back up from 2.82x just as real yields (+56bp/3m) and HY spreads (+45bp/3m) rise (macro overlay) [Likely]. Generics pricing gives little moat, so the 40.3% gross margin is exposed [Likely]. The mechanical DCF bear value (17.77) is today's price [Certain].

## Bull case
FCF is real and steady: FCF margin of 13-16% every year since FY2021 and a 9.65% FCF yield [Certain]. Net debt/EBITDA fell from 4.10x to 2.82x and shares fell 2.44% YoY [Certain]. ROIC, gross margin and operating margin all improved over five years [Certain]. The price implies -4.6% revenue growth in year 1, harsher than this record [Certain]; the base DCF is 22.22 (+26%) and the stock trades 28% below peers on EV/EBITDA and 62% below on P/FCF [Certain]. Pacira adds patent-protected, high-margin US brands (EXPAREL, ZILRETTA) that management calls immediately accretive, and Wakix's Japan approval shows the specialty mix is growing, which could lift margins and justify a higher multiple [Likely].

## Decision
```json
{
  "ticker": "VTRS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative but sub-cost-of-capital generics business, already re-rated above its own 5-year multiple range, is re-levering for a $1.65bn cash acquisition, so the 26% base-case upside does not pay for the quality and balance-sheet risk.",
  "rationale": "The FCF yield and the reverse-DCF gap are real, but ROIC of 5.9%, negative net income, Altman Z of 1.10 and debt-funded M&A into rising real yields make this good-but-not-compelling. Multiples are above their own 5-year highs after an 82% run. Conviction 3 means AVOID under the owner rule; revisit once Q3 results disclose Pacira financing.",
  "price_at_decision": 17.64,
  "price_date": "2026-10-09",
  "research_note": "research/VTRS/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC rises above 8%, showing the five-year improvement from 2.4% to 5.9% is moving returns toward the cost of capital (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 8}},
    {"text": "TTM net margin turns sustainably positive above 3%, ending the impairment-driven losses (TTM -2.8%) that depress earnings quality (would raise conviction).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 3}},
    {"text": "Net debt/EBITDA rises above 3.5x after the Pacira close, reversing the deleveraging from 4.10x to 2.82x (confirms AVOID).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "TTM FCF margin falls below 10%, under the five-year floor of 13.3%-16.4%, removing the cash-yield support (confirms AVOID).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 29.91, "basis": "Pacira's high-margin brands and the specialty mix lift margins, the market abandons the -4.6% revenue decline implied by the reverse DCF, and the stock reaches the mechanical bull DCF value of 29.91 [IS,CF,RA,ST]."},
    "base": {"probability": 0.4, "target_price_12m": 22.22, "basis": "FCF margin holds near 13.3% [CF,IS] and leverage stays manageable, so the stock converges on the base DCF of 22.22; probability cut by 0.05 to bear for the overlay's small toward-bear tilt from rising real yields and HY spreads into a debt-funded deal (research/VTRS/2026-10-12-macro.md)."},
    "bear": {"probability": 0.4, "target_price_12m": 13.67, "basis": "Multiples above their own 5-year max (EV/EBITDA 7.5x vs 7.1x, P/FCF 10.4x vs 7.5x [RA]) fall back into range as Pacira debt lifts leverage above 2.82x on a Z-score of 1.10 [ST], taking the price back to its 6-month low of 13.67 [HI], below the mechanical bear of 17.77 because that DCF ignores the added acquisition debt; includes the overlay's small bear tilt (research/VTRS/2026-10-12-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the close of 17.64 is already below base fair value less 20% (22.22 x 0.8 = 17.78). The obstacles are sub-cost-of-capital ROIC, negative net income, a distress-zone Altman Z of 1.10 and unknown Pacira financing, so a lower price on this evidence would not justify conviction 4; re-research after the 2026-11-05 Q3 results.",
  "replaces": null,
  "replacement_reason": null
}
```
