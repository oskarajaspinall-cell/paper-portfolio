# Evaluation: Uber Technologies, Inc. (UBER) — 2026-10-09
## Bear case
The 52-week fall of 28.2% and relative strength of -43.8pp versus SPY show the market is pricing a structural risk, most plausibly robotaxi disintermediation, which the note itself calls unresolved [Likely]. Headline cheapness overstates value: net margin (FY2024 22.4% vs operating 6.4%) has been inflated by non-operating items, so P/E 15.3x flatters [Likely]; EV/EBITDA and P/FCF "below 5y min" compare against loss-making years, not a mature franchise [Certain]. Mechanical base fair value is only $76.76 (+9.3%), with a DCF bear below zero, so the margin of safety is thin [Certain]. Fresh capital is going to a $2.3bn all-cash ezCater deal with unproven margin benefit while net debt/EBITDA rose to 1.25x TTM [Certain]. Macro overlay tilts small toward bear: the 10y at 5.28% (+72bp/3m) compresses the DCF [Certain]. Wait times are rising per a third-party study [Guessing].

## Bull case
Uber has become a genuine compounder: ROIC 19.2% TTM from -19.2% in FY2021, operating margin 12.1% and FCF margin 18.3%, all still rising [Certain]. The 7.05% FCF yield and P/FCF of 14.2x price a mature low-growth business, and the reverse DCF implies only 12.5% year-1 revenue growth [Certain]. Shares outstanding fell 2.28% YoY on buybacks, and EV/EBITDA of 19.8x sits 65% below the peer median [Certain]. Network density across Mobility and Delivery could make Uber the demand-aggregation layer for AV operators (Pony.ai, Wayve) rather than its victim [Guessing]. Low short interest (2.25%) and an Altman Z of 3.74 show no distress [Certain].

## Decision
```json
{
  "ticker": "UBER",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A marketplace whose ROIC and FCF margin have inflected to 19.2% and 18.3% trades at a 7.05% FCF yield, but unresolved robotaxi disintermediation and a thin 9.3% gap to base fair value leave the reward short of compelling.",
  "rationale": "Quality is real and improving, but the cheapness is partly optical (multiples versus loss-making years, P/E flattered by non-operating gains), base fair value is only +9.3%, the AV threat is unresolved, M&A is resuming and macro tilts bearish. Good but not compelling: AVOID, with an entry at base fair value less 20%.",
  "price_at_decision": 70.24,
  "price_date": "2026-10-08",
  "research_note": "research/UBER/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, reversing most of the climb from 5.8% (FY2023) to 19.2%, evidence that AV or competitive pressure is eroding marketplace economics.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 10%, back near the FY2023 level of 9.0%, breaking the cash-generation thesis.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 9%, giving back the expansion since FY2024 (6.4%) and signalling take-rate pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 100.0, "basis": "Margin expansion continues and P/FCF re-rates from 14.2x toward its 5y minimum 17.4x [RA] and beyond, toward the bull fair value of 108.78 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 76.0, "basis": "Fundamentals track the reverse-DCF's 12.5% growth and the price converges on the mechanical base fair value of 76.76 [fact sheet Fair value], held back by AV uncertainty."},
    "bear": {"probability": 0.30, "target_price_12m": 50.0, "basis": "AV disintermediation fears deepen and EV/Sales falls toward its 5y minimum 1.7x [RA], near the EV/Revenue bear value of 43.09 but cushioned by the 7.05% FCF yield [ST]; probability raised from 0.25 by the macro overlay's small tilt toward bear (research/UBER/2026-10-09-macro.md); the negative DCF bear of -11.38 is a model artefact of loss-making history and is ignored."}
  },
  "entry_price": 61.41,
  "entry_basis": "valuation file: base 76.76 x 0.8 = 61.41; at that price the same evidence would offer enough margin of safety against the unresolved AV risk to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
