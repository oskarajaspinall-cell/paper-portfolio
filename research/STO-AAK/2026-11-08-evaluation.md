# Evaluation: AAK AB (publ.) (STO:AAK) — 2026-11-08
## Bear case
The FY2024 margin peak looks partly cyclical: gross margin has eased from 28.8% to 25.9% TTM, and the Q3 2026 call cites pricing pressure across all segments with flat volumes [Likely]. The **Direction change** lines confirm it: ROCE fell from 22.4% to 19.1% over the last 12 months and ROIC sits 2.7pp below its 17.9% two-year high [Certain]. That is the core of the threat. If pricing keeps slipping, the cheap 13.4x P/E rests on earnings that are still falling [Likely]. FCF is erratic: FY2025 FCF margin was -0.9% and FY2022 -2.6%, swinging with raw-material working capital [Certain]. The best valuation method, the DCF, gives a base of 146.06 SEK, below the 182.60 close, and its bear case is negative [Certain]. Karlshamn production issues in Q2 point to execution risk [Likely]. Country revenue mix is [data unavailable], so FX exposure is unmodelled [Certain].
## Bull case
On every multiple the shares trade below their 5-year range: P/E 13.4x against a 19.8x minimum, EV/EBITDA 9.0x against 12.8x [Certain]. Returns are still well above 2021-22 levels (ROIC 15.1% vs 12.0%), and operating margin has held at 10.5% TTM even through the pricing pressure [Certain]. The balance sheet is strong at 0.60x net debt/EBITDA, the TTM FCF margin has recovered to 6.2% (a 6.01% FCF yield), and management has proposed higher dividends and a buyback [Certain]/[Likely]. Long-term 2030 targets were unchanged at Q3 [Likely]. The 31.0% fall over 12 months may already price in more margin normalisation than happens. If margins stabilise, a partial return toward historical multiples gives a P/E-based value well above the price [Guessing].
## Decision
```json
{
  "ticker": "STO:AAK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A quality specialty-fats processor at a historic-low multiple, but with returns and pricing still deteriorating there is no evidence yet that earnings have stopped falling.",
  "rationale": "Cheap against its own history and peers with a strong balance sheet, but ROCE and gross margin are falling, Q3 cited pricing pressure across segments, and the DCF base sits below the price. Base fair value offers only modest upside. Good but not compelling; wait for margin stabilisation or a lower price.",
  "price_at_decision": 182.60,
  "price_date": "2026-11-06",
  "research_note": "research/STO-AAK/2026-11-08.md",
  "triggers": [
    {"text": "Gross margin (TTM) falls below 23%: pricing pressure is structural, not cyclical", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 23}},
    {"text": "ROIC (TTM) falls below 12%: returns back to 2021-22 levels", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "FCF margin (TTM) falls below 3%: cash conversion reverts to its erratic pattern", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt / EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 265.28, "basis": "Margins stabilise and pricing recovers, so the DCF bull case of 265.28 SEK [IS,CF] is reached as P/E re-rates toward its 5y minimum of 19.8x [RA]; below the blended bull of 295.08 because the P/E method leans on peak-era multiples."},
    "base": {"probability": 0.45, "target_price_12m": 202.39, "basis": "Operating margin holds near 10.5% TTM [IS] with pricing pressure persisting but not deepening, so the shares reach the blended base fair value of 202.39 SEK [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 146.06, "basis": "Pricing pressure across segments (Q3 2026 transcript, /quote/sto/AAK/transcripts/532943-q3-2026/) keeps ROCE falling from 19.1% [RA-T], and the price converges on the DCF base of 146.06 SEK; above the mechanical bear of 51.17 given 0.60x net debt/EBITDA [RA]."}
  },
  "entry_price": 161.91,
  "entry_basis": "valuation file: base 202.39 x 0.8 (20% margin of safety); at that level the cheap multiple would compensate for the unresolved margin trend.",
  "replaces": null,
  "replacement_reason": null
}
```
