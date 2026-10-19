# Evaluation: Contemporary Amperex Technology Co., Limited (SHE:300750) — 2026-10-19
## Bear case
The mechanical base fair value of 300.73 CNY sits only +8.6% above the 277.00 close, while the bear value (85.62) is -69.1% below, so the skew is poor even before risks [Certain]. Battery cells are commoditising: gross margin fell to 19.1-19.5% in FY22-23 on overcapacity, and it is flat over 5y (24.5% TTM) despite record ROIC [Certain]. The 2026-07-24 WSJ headline says China EV demand is weakening, shifting growth to newer energy-storage demand [Likely]. US political pressure on Ford's CATL tie-up threatens Western customers [Likely]. Shares grew 3.68% YoY, diluting holders [Certain]. Price momentum is severe (-39.0% over 6 months, -47.8pp vs SPY) and Q3 results land on Oct 20, 2026, a binary event the research cannot see [Certain]. Record margins may be a cyclical peak, not a new floor [Guessing].

## Bull case
Quality is outstanding and improving: ROIC 69.5% TTM (from 35.6% FY21), operating margin 17.9%, FCF conversion above 100% of net income for three years, and net cash (-2.40x net debt/EBITDA) [Certain]. It trades below its own 5y minimum P/E (14.8x vs 16.3x) and EV/EBITDA (8.5x vs 8.6x), and well below peers on both [Certain]. A 6.76% FCF yield is generous for the global scale leader [Certain]. RSI 26.6 shows capitulation-type selling [Certain]. If returns persist, the bull value of 623.63 CNY is reachable [Guessing]; energy-storage demand is booming per the WSJ headline [Likely].

## Decision
```json
{
  "ticker": "SHE:300750",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 69.5%-ROIC global battery leader trades below its own 5-year minimum P/E and EV/EBITDA, but in a commoditising, overbuilt industry with US political risk the base fair value offers little upside against a deep bear case.",
  "rationale": "Exceptional returns and cheap multiples, but base fair value is barely above the price while the bear value is far below; margins are cyclical and dilution, US political pressure and tomorrow's results add uncertainty. Good but not compelling: conviction 3, AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 277.00,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-300750/2026-10-19.md",
  "triggers": [
    {"text": "TTM gross margin falls below 19%, under the FY2022-23 price-war trough, showing overcapacity is eroding pricing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 19}},
    {"text": "TTM ROIC falls below 40%, giving up most of the five-year rise from 35.6% to 69.5% and signalling moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM operating margin falls below 12%, under the FY2021 level of 12.4%, showing the margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 10%, well under the 16.8% TTM level, showing working-capital or capex strain.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 370.00, "basis": "P/E re-rates from 14.8x toward the 19.8x peer median [RA] on TTM earnings as storage demand offsets China EV weakness (WSJ 2026-07-24 headline); below the 623.63 bull fair value because a full return to the 23.2x 5y median P/E is unlikely in an overbuilt industry."},
    "base": {"probability": 0.45, "target_price_12m": 300.00, "basis": "In line with the 300.73 base fair value (DCF 315.94, EV/EBITDA 270.31) [IS,BS,CF,RA,ST]; margins hold near 17.9% operating [IS] but the multiple stays near its 5y floor; macro overlay tilt neutral/small (research/SHE-300750/2026-10-19-macro.md), so no change."},
    "bear": {"probability": 0.30, "target_price_12m": 186.00, "basis": "Price war returns gross margin toward the FY22-23 19.1-19.5% range [IS] and US pressure on Ford's partnership (note §6) hits Western demand, taking value to the 186.16 EV/EBITDA bear fair value [RA]."}
  },
  "entry_price": 240.58,
  "entry_basis": "valuation file: base 300.73 x 0.8 (fact sheet base fair value less the 20% margin of safety).",
  "replaces": null,
  "replacement_reason": null
}
```
