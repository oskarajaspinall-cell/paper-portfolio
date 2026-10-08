# Evaluation: Constellation Brands, Inc. (STZ) — 2026-10-07
## Bear case
The discount is to STZ's own history, not to its peers. EV/EBITDA of 8.8x is only 5% below the 9.2x peer median, and P/FCF of 10.9x is level with the peers' 10.7x [Certain] (RA). The whole alcohol group has de-rated, which points to a structural reset in US drinking rather than mispricing in one stock [Likely]. Management itself describes industry-wide softening in beer demand, and Barron's reports weak demand for two flagship brands [Likely] (CNBC, Barron's headlines [OV]). Beer is most of the profit, so the multiple has little to fall back on [Likely]. Gross and operating margins are down 1.8pp and 2.1pp over five years, and marketing is stepping up [Certain] (IS, transcript). Net debt/EBITDA of 2.96x limits flexibility [Certain] (RA). The share is 19.1% below its 200-day average and short interest rose 15.2% [Certain] (ST), so sellers are not exhausted [Guessing].
## Bull case
STZ trades below its 5-year minimum on every multiple: P/E 10.4x against a minimum of 16.2x, at a 9.2% FCF yield [Certain] (RA, ST). The franchise is still high quality: a 33.0% operating margin, a 20.0% FCF margin, 95.6% FCF conversion and ROIC rising to 12.9% [Certain] (IS, CF, RA). Q2 beat, FY27 comparable EPS guidance was reaffirmed, and September trends support the high end [Likely] (transcript [OV]). Shares outstanding fell 3.32% YoY, with buyback authorisation remaining [Certain] (ST, transcript). The Veracruz brewery is ~85% complete, so capex should ease after FY2028 and lift FCF [Likely]. A beta of 0.43 makes it a defensive diversifier for a portfolio with no Consumer Staples exposure [Certain] (ST, state.json). If beer volumes merely stabilise, a return to even the bottom of its EV/EBITDA range implies material upside [Likely].
## Decision
```json
{
  "ticker": "STZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, cash-generative US imported-beer franchise trades below its own 5-year minimum multiples, but only in line with de-rated peers on EV/EBITDA and P/FCF while its core beer demand is softening.",
  "rationale": "Quality and cash generation are real, but the discount is mostly a sector-wide de-rating: EV/EBITDA and P/FCF are only in line with peers. Flagship beer demand is weakening, margins are drifting lower, leverage is near 3x and momentum is negative. This is good but not compelling, so conviction is 3, which is below the buy threshold. Cash is acceptable.",
  "price_at_decision": 115.67,
  "price_date": "2026-10-06",
  "research_note": "research/STZ/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, signalling that pricing/mix and marketing pressure is breaking beyond the 5-year drift (current 33.0% [IS]).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 15%, under the FY2024 level of 15.2%, showing that cash conversion is breaking down (current 20.0% [CF,IS]).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 8%, reversing the recovery to 12.9% [RA] and compressing returns toward the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Management cuts FY27 comparable EPS guidance below the reaffirmed range on a later earnings call, confirming that beer depletion weakness is structural."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 161, "basis": "Beer trends at the high end of guidance [transcript, OV] re-rate EV/EBITDA from 8.8x to its 5y minimum of 11.1x [RA] on unchanged EBITDA and net debt/EBITDA of 2.96x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 124, "basis": "EV/EBITDA converges to the 9.2x peer median [RA, P:BF.B, P:DEO, P:TAP, P:SAM] on flat EBITDA, as reaffirmed guidance [transcript, OV] offsets tepid demand [CNBC, OV]."},
    "bear": {"probability": 0.3, "target_price_12m": 88, "basis": "Softening beer demand [CNBC, Barron's, OV] cuts the FCF margin from 20.0% back to the FY2024 level of 15.2% [CF, IS] at an unchanged 10.9x P/FCF [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
