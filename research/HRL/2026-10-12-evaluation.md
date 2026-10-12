# Evaluation: Hormel Foods Corporation (HRL) — 2026-10-12
## Bear case
Every return measure is falling: ROIC 11.4% (FY21) to 6.6% TTM, ROE 13.6% to 4.3%, net margin 8.0% to 2.8% [Certain] [RA, IS]. Gross margin is down 1.3pp despite iconic brands, so pricing power is not offsetting input costs [Likely]. P/E of 30.9x sits above its 5y max of 27.4x on depressed earnings [Certain] [RA]. The ~$1.055bn debt-funded Brakebush deal is accretive only from FY2028 and adds integration risk and leverage as real yields rise (DFII10 +0.56pp/3m, macro overlay) [Likely]. Short interest is 7.17% and up 21.7% month on month; 12-month relative strength is -35.3pp vs SPY [Certain] [ST, HI]. Base fair value of 19.87 is only +3.5% above the price, with the bear case at 12.03 (-37.3%) [Certain]. That leaves no margin of safety [Likely].
## Bull case
The cash-flow multiples are cheap. EV/EBITDA of 9.9x and P/FCF of 13.5x are below their 5y minimums of 12.5x and 16.9x, and the FCF yield is 7.39% [Certain] [RA, ST]. A high P/E next to a low EV/EBITDA suggests earnings are depressed by non-cash or one-off items, not cash flow: FCF conversion is 227.9% TTM [Certain] [CF, IS]. The reverse DCF implies -1.3% year-one revenue growth, a low bar [Certain]. Net debt/EBITDA of 1.57x leaves room for Brakebush [Certain] [RA]. If margins return to the FY2024 levels (gross 17.0%, operating 9.2%), the DCF bull of 30.02 comes into view [Guessing]. Beta of 0.29 and an RSI of 25.0 suggest the stock is oversold within a defensive name [Likely] [ST].
## Decision
```json
{
  "ticker": "HRL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A branded packaged-food maker with cheap cash-flow multiples but five years of falling returns and margins, now taking on a debt-funded acquisition, at a price roughly equal to its base fair value.",
  "rationale": "Quality is still deteriorating on every measure. Base fair value is only 3.5% above the price, and the bear case sits 37% below it. Brakebush adds leverage and integration risk just as real yields rise. Cheap EV/EBITDA and P/FCF multiples do not make up for the absence of any evidence that margins are recovering. AVOID; cash is the better use.",
  "price_at_decision": 19.19,
  "price_date": "2026-10-09",
  "research_note": "research/HRL/2026-10-12.md",
  "triggers": [
    {"text": "TTM gross margin recovers above the FY2024 level of 17.0%, showing pricing power is again offsetting input costs.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 17.0}},
    {"text": "TTM operating margin recovers above the FY2024 level of 9.2%, evidencing a margin recovery rather than secular decline.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 9.2}},
    {"text": "TTM ROIC rises back above the FY2022 level of 10.2%, showing returns have turned despite the Brakebush capital outlay.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10.2}},
    {"text": "TTM FCF margin rises above the FY2024 level of 8.5%, confirming cash generation is improving, not just earnings optics.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 8.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 25.32, "basis": "Margins recover toward FY2024 levels (gross 17.0%, operating 9.2% [IS]) and the market re-rates toward the fact sheet's bull fair value of 25.32; the probability is cut slightly for the macro overlay's small tilt toward bear (research/HRL/2026-10-12-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 19.87, "basis": "Margins stabilise near TTM levels (operating 8.2% [IS]) while Brakebush integrates, so the price converges on the fact sheet's blended base fair value of 19.87 (DCF 21.96 / P/E 15.67)."},
    "bear": {"probability": 0.3, "target_price_12m": 12.03, "basis": "ROIC and margins keep falling (ROIC 6.6% TTM [RA]) while debt-funded Brakebush and rising real yields (macro overlay: DFII10 +0.56pp/3m, small tilt toward bear, research/HRL/2026-10-12-macro.md) compress value to the fact sheet's bear fair value of 12.03."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3, and price is not the obstacle: returns and margins are still falling and the Brakebush deal is debt-funded, so a lower price alone would not justify conviction 4. A margin or ROIC recovery (see triggers) would.",
  "replaces": null,
  "replacement_reason": null
}
```
