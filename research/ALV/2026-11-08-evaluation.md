# Evaluation: Autoliv, Inc. (ALV) — 2026-11-08
## Bear case
Returns have peaked: ROIC is 4.8pp below its 2-year high of 23.3% and ROCE fell from 26.0% to 24.8% over the last year, contradicting the rising 5-year trend [Certain]. The driver is a stalled margin: TTM operating margin 10.2% vs 11.3% at the 2-year high, Q3 adjusted operating margin 9.7%, guidance pinned at the low end on raw materials, logistics and call-off volatility [company-reported], so the ROCE dip threatens the "margin expansion" leg of any thesis [Likely]. Q3 missed on sales and EPS with flat organic growth guided for FY26 [Certain]. This is a beta-1.37 cyclical tied to vehicle production; the DCF bear of 13.55 shows how margin-sensitive value is [Certain]. China growth is strong but its revenue share is unknown and policy risk unverified (macro overlay) [Guessing]. On P/E, EV/EBITDA and EV/Sales ALV trades at a premium to peers, and P/B sits above its 5y max [Certain].

## Bull case
A global oligopoly leader in passive safety with regulatory content and high barriers to entry [Likely]. Returns are high for auto parts: ROIC 18.5%, ROCE 24.8% [Certain]. Cash is improving even as margins stall: FCF margin rose from 5.4% to 6.6% over 12 months, FCF conversion 117.0%, FCF yield 8.20%, P/FCF 12.2x below its 5y minimum [Certain]. Shares fell 4.12% YoY on buybacks with leverage flat at 1.21x [Certain]. The reverse DCF implies only 1.8% growth, a low bar, and EV/EBITDA 6.9x sits near the bottom of its 5y range [Certain]. Base fair value 141.64 sits above the 123.47 close [Certain]. Tariffs are largely passed through [company-reported].

## Decision
```json
{
  "ticker": "ALV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return passive-safety oligopolist with strong cash conversion and buybacks trades near the low end of its own EV/EBITDA and P/FCF ranges, but stalled margins, falling ROCE and cyclical volume risk leave only modest upside to base fair value.",
  "rationale": "Quality and cash returns are real, but returns are rolling over from their 2024 high, Q3 missed with guidance at the low end, and base fair value sits only modestly above the price with a wide, margin-sensitive bear case. Good but not compelling for a beta-1.37 cyclical: conviction 3, AVOID until a margin of safety appears.",
  "price_at_decision": 123.47,
  "price_date": "2026-11-06",
  "research_note": "research/ALV/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9.0% (10.2% now), showing raw-material and call-off pressure is structural rather than offset by cost action.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9.0}},
    {"text": "TTM ROIC falls below 15% (18.5% now), breaking the step-up in returns since FY2022.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 4.0% (6.6% now), showing the cash-conversion improvement was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4.0}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.21x TTM now), showing buybacks or the MCF acquisition are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 152.0, "basis": "Margins recover toward the ~10.5% adjusted FY26 guide (Q3 transcript [OV]) and EV/EBITDA re-rates toward its 5y median 7.8x [RA]; between the EV/EBITDA bull 151.95 and the blended bull 157.90 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 135.0, "basis": "Flat organic sales per FY26 guidance with operating margin near TTM 10.2% [IS] and continued buybacks (shares -4.12% YoY [ST]); slightly below the base fair value 141.64 because ROCE is falling over the last year [RA-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 100.0, "basis": "Vehicle-production weakness and raw-material headwinds [company-reported, 10-Q] push margin back toward the FY2022 7.5% [IS] and EV/EBITDA to its 5y min 6.7x [RA]; below the EV/EBITDA bear 114.55 but far above the margin-sensitive DCF bear 13.55, which assumes a margin collapse."}
  },
  "entry_price": 113.31,
  "entry_basis": "valuation file: base 141.64 x 0.8; at that level the margin of safety offsets the stalled-margin and cyclical-volume risk and would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
