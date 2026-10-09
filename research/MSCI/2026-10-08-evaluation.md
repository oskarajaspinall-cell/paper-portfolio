# Evaluation: MSCI Inc. (MSCI) — 2026-10-08
## Bear case
The "below 5-year minimum" signal reflects a near-zero-rate period. Even after the de-rating, MSCI trades at P/E 30.4x and EV/EBITDA 23.7x, +16% and +51% above the peer median of SPGI, MCO, FDS and LSEG [Certain] (RA). At a 5.27% 10y yield, the mechanical DCF/FCFE fair value is 192.70 / 249.65 / 334.18, so even the bull case is 40% below the price. The reverse DCF implies 28.2% year-1 revenue growth [Certain] (fact sheet), well above anything the flat 82-83% gross and 54-56% operating margins suggest [Likely]. Real yields rose 0.61pp in 3 months while MSCI lagged SPY by 12.6pp, so rate-driven compression looks like it is already under way [Likely] (macro overlay). Leverage rose from 2.46x to 3.16x net debt/EBITDA [Certain] (RA). ABF revenue (26.6%) and BlackRock (11.8% of revenue) add market and client-concentration risk [Certain] (10-Q). Q3 results are due 2026-10-20 [Certain] (ST).
## Bull case
This is one of the highest-quality franchises in the index. ROIC rose from 25.1% to 39.9% and ROCE from 25.9% to 46.4% over five years, with an 83.0% gross margin, a 55.7% operating margin and a 47.9% FCF margin [Certain] (RA, IS, CF). FCF has exceeded net income in every year shown [Certain] (CF). Index benchmarks are embedded in mandates and prospectuses, so switching costs are high [Likely]. Shares outstanding fell 4.85% YoY [Certain] (ST), which compounds per-share earnings. Every multiple sits 9-16% below its 5-year minimum [Certain] (RA). The P/E method values the stock at 654.73-780.14 [Certain] (fact sheet). Management cites recurring net new sales up 24-25% year-to-date [Likely] (Barclays transcript, fact-sheet listing). Altman Z 6.20 and Piotroski 7 show no balance-sheet stress [Certain] (ST).
## Decision
```json
{
  "ticker": "MSCI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "MSCI is an elite, high-ROIC compounder de-rated below its own 5-year multiple range, but it still trades at a premium to peers and far above its cash-flow fair value, while real yields are rising, so the margin of safety is too thin for a high-conviction buy.",
  "rationale": "The business is exceptional, but the valuation case is not compelling. The DCF/FCFE range (192.70-334.18) sits entirely below the price, multiples remain above peers, and the macro overlay tilts toward the bear case with real yields rising. Q3 results are due 2026-10-20. Conviction 3 is below the buy threshold, so this is an AVOID and cash is acceptable.",
  "price_at_decision": 555.38,
  "price_date": "2026-10-07",
  "research_note": "research/MSCI/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC rises above 45%, well beyond the 39.9% TTM level, showing returns are compounding fast enough to justify the premium (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 45}},
    {"text": "TTM ROIC falls below 25%, the FY2021 5-year low, showing competitive erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM operating margin falls below 53.5%, the FY2024 5-year low, showing pricing power or cost discipline is weakening.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 53.5}},
    {"text": "Net debt/EBITDA rises above 4.0x from 3.16x TTM, meaning buybacks are being funded by leverage beyond what recurring revenue supports.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 655, "basis": "P/E re-rates back to its 5-year minimum of 35.9x [RA] on TTM EPS, consistent with the P/E method's bear value of 654.73 (fact sheet); the probability is cut by the overlay's moderate tilt toward bear (research/MSCI/2026-10-08-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 583, "basis": "P/E holds at 30.4x [RA] while the 4.85% YoY share-count reduction [ST] lifts EPS; this sits above the DCF base of 249.65 because that DCF discounts at a 5.27% risk-free rate with beta 1.24 [ST], which the market has never applied to this franchise."},
    "bear": {"probability": 0.35, "target_price_12m": 480, "basis": "P/E compresses to the 26.3x peer median [RA, P:SPGI/MCO/FDS/LSEG] as real yields keep rising and ABF (26.6% of revenue, 10-Q) comes under pressure; the probability is raised for the overlay's moderate tilt toward bear (research/MSCI/2026-10-08-macro.md), and the target stays above the DCF bear of 192.70 because cash-flow DCF has never anchored this stock's multiple."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
