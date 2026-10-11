# Evaluation: NVIDIA Corporation (NVDA) — 2026-10-11
## Bear case
The price already assumes the AI-capex supercycle runs for years: the reverse DCF implies 50.9% revenue growth in year 1 [Certain] (fact sheet), and even the mechanical bull fair value of 208.22 sits 9.2% below the 229.28 close [Certain] (fact sheet). Cash quality is slipping: FCF conversion fell from 90.8% (FY2024) to 65.8% TTM and the net-cash cushion shrank from -0.43x to -0.12x net debt/EBITDA [Certain] (CF, IS, BS). Demand is concentrated in a few hyperscalers and AI labs that are building custom silicon [Likely] (SEC 10-Q; note). Real yields rose 0.56pp in 3 months and HY spreads are widening, which raises the cost of leveraged AI capex and a beta-2.22 stock's discount rate [Likely] (macro overlay; ST). Export-control enforcement and a possible ~$25bn Reflection AI deal add policy and capital-allocation risk [Guessing] (Reuters; TipRanks headlines).
## Bull case
Economics are exceptional and still improving: TTM ROIC 92.0%, operating margin 65.2%, gross margin 74.7%, net margin 63.7% [Certain] (RA, IS). CUDA plus the full chip-network-software stack is a moat a pure silicon rival struggles to copy [Likely] (nvidia.com). On its own history the stock has never been cheaper: P/E 29.0x, EV/EBITDA 27.4x and P/FCF 43.6x are all below their 5-year minimums, and P/E is 24% below the peer median [Certain] (RA). The mechanical fair value is anchored on a through-cycle DCF that averages in the FY2023 trough (ROIC 29.3%, operating margin 20.7%), so it likely understates the step-changed earnings base [Likely] (RA, IS). The balance sheet is net cash, shares fell 1.04% YoY, and the trend is strong (+13.4% vs the 200-day, +5.6pp vs SPY over 12 months) [Certain] (ST, HI).
## Decision
```json
{
  "ticker": "NVDA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class, net-cash AI compute franchise trades below its own 5-year multiple range, but the price already embeds ~51% year-1 growth and sits above even the mechanical bull fair value, leaving no margin of safety against custom-silicon competition or an AI-capex digestion.",
  "rationale": "Quality is unmatched and own-history multiples are low, but those multiples rest on peak-cycle earnings with falling FCF conversion and concentrated customers. The price exceeds the bull fair value and the probability-weighted target sits below the close; a small macro tilt toward bear adds to it. Good but not compelling: AVOID, watch for a lower entry.",
  "price_at_decision": 229.28,
  "price_date": "2026-10-09",
  "research_note": "research/NVDA/2026-10-11.md",
  "triggers": [
    {"text": "TTM gross margin falls below 65%, showing custom silicon and price competition are eroding pricing power (bear case confirmed; reassess at a far lower entry).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 65}},
    {"text": "TTM ROIC falls below 50%, showing returns are being competed away rather than merely normalising from the FY2025 peak of 190.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 30%, showing capex and working capital are outrunning cash generation from the buildout.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "The next results (Nov 18, 2026) show hyperscaler/AI-lab demand broadening beyond a few concentrated customers with FCF conversion recovering toward the FY2024 level of 90.8%, which would lift conviction on the growth the price implies."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 300.0, "basis": "AI capex stays funded and P/E re-rates from 29.0x to its 5y minimum of 38.0x [RA] on TTM earnings; above the mechanical bull fair value 208.22 because the through-cycle DCF averages in the FY2023 trough (operating margin 20.7% [IS])."},
    "base": {"probability": 0.45, "target_price_12m": 215.0, "basis": "Earnings grow but FCF conversion keeps drifting (65.8% TTM [CF,IS]) and the multiple de-rates further, landing near the mechanical bull fair value 208.22; well above the base fair value 85.79 because ROIC of 92.0% [RA] is not a trough-cycle business."},
    "bear": {"probability": 0.30, "target_price_12m": 120.0, "basis": "Custom silicon and AI-capex digestion push gross margin back toward FY2023's 56.9% [IS] and EV/EBITDA toward the mechanical EV/EBITDA base of 97.04; probability raised by the macro overlay's small tilt toward bear (real yields +0.56pp, HY spreads widening; research/NVDA/2026-10-11-macro.md)."}
  },
  "entry_price": 164.27,
  "entry_basis": "52-week low 164.27 [HI], used instead of base fair value 85.79 x 0.8 because the through-cycle DCF averages in the FY2023 trough (ROIC 29.3% [RA]) and understates the step-changed economics; at that level the multiples would sit far below the 5y minimums (P/E 38.0x [RA]) with margin for the 30% bear case.",
  "replaces": null,
  "replacement_reason": null
}
```
