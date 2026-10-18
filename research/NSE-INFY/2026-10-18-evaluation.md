# Evaluation: Infosys Limited (NSE:INFY) — 2026-10-18
## Bear case
The discount is a sector de-rating, not a mispricing of Infosys: P/E 15.2x and EV/EBITDA 10.2x sit in line with the peer medians of 15.8x and 10.0x [Certain]. All four peers are being repriced for the same risk, most plausibly AI-driven deflation of labour-arbitrage services, which a fair value built from the stock's own history cannot see [Guessing]. Profitability is drifting the wrong way: gross margin from 32.6% to 29.7% and operating margin from 23.0% to 20.4% over five years [Certain]. The US PERM suspension adds a policy overhang on the onshore delivery model [Likely]. Price trend confirms it: down 21.2% over 12 months, 36.0pp behind SPY, 50-day average below the 200-day [Certain]. The decisive evidence, Q2 results and guidance, arrives on Oct 23, 2026 [Certain], so buying now is a bet on an unseen print.
## Bull case
Quality is rising, not falling: ROIC 41.7% TTM up from 36.7%, ROE 32.0%, FCF conversion 114.5% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.49x) and shares fell 1.37% YoY [Certain]. Every multiple sits below its own 5-year minimum, with a 7.65% FCF yield [Certain]. The reverse DCF implies -0.9% year-1 revenue growth, a pessimistic bar for a business with multi-year enterprise contracts [Likely]. Base fair value of 1,514.40 INR is +30.4% above the 1,161.20 close, and even the bear value of 1,027.49 limits the mechanical downside [Certain]. Management says the PERM suspension has no material impact [Likely]. Beta of 0.12 would diversify a US-heavy book [Guessing].
## Decision
```json
{
  "ticker": "NSE:INFY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 41.7%-ROIC IT services franchise trades below its own 5-year minimum multiples, but in line with peers that are being de-rated for structural growth risk while its margins drift lower.",
  "rationale": "Quality and cash returns are excellent, but the cheapness is sector-wide, operating margin has fallen for five years, and the AI-deflation and PERM questions are unresolved with results due Oct 23. Good but not compelling; cash is acceptable. Revisit on the print, not on price.",
  "price_at_decision": 1161.20,
  "price_date": "2026-10-16",
  "research_note": "research/NSE-INFY/2026-10-18.md",
  "triggers": [
    {"text": "TTM operating margin falls below 18%, confirming the five-year margin erosion is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM ROIC falls below 30%, indicating the pricing and cost advantage is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below the FY2023 five-year low of 13.9%, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 13.9}},
    {"text": "Results or revenue guidance on Oct 23, 2026 or later show a sustained growth slowdown or large-deal weakness beyond the near-flat growth the price implies."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1745.82, "basis": "Results show stable growth and margins, and multiples recover toward the bull fair value of 1,745.82 INR on rising ROIC of 41.7% [RA] and a 7.65% FCF yield [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 1382.06, "basis": "Growth stays modest but above the -0.9% the reverse DCF implies, supporting the DCF base value of 1,382.06 INR rather than the full blend, since peers at a 15.8x P/E median [P:NSE:TCS] cap multiple re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 1027.49, "basis": "AI deflation and PERM pressure push operating margin further below 20.4% [IS] and the sector de-rating persists, at the bear fair value of 1,027.49 INR."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the base fair value less the margin of safety; what is missing is evidence on growth and margins (Oct 23 results/guidance) and on the sector's AI exposure, so a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
