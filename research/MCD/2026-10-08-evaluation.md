# Evaluation: McDonald's Corporation (MCD) — 2026-10-08
## Bear case
The de-rating is a reset, not a mispricing. MCD now trades at peer multiples (P/E 18.8x vs 18.2x; P/FCF 21.1x vs 21.4x) [Certain], so the "below 5y minimum" signal mostly reflects a lost premium. US traffic is weakening despite value deals [Likely], franchisees are resisting an ~$800,000 revamp bill [Likely], and a new antitrust class action targets the AI pricing system at the core of the franchise model [Likely]. FCF conversion fell 10.2pp to 88.3% and FCF margin 3.9pp to 28.0% [Certain], while net debt/EBITDA of 3.60x limits balance-sheet support [Certain]. Rising US real yields press on a bond-proxy multiple (macro overlay, small bear tilt) [Likely]. Shares are -22% over 12 months, 20% under the 200-day average, with short interest up 10.3% into the Nov 4 print [Certain]; another soft US comp could extend the slide [Guessing].

## Bull case
The landlord model (owns ~56% of land, ~80% of buildings) collects rent regardless of franchisee margins [Certain]. Returns are intact: ROIC 17.8%, ROCE 22.7%, operating margin 45.7%, gross margin 57.4%, Piotroski 7, Altman Z 4.98 [Certain]. Every multiple sits below its 5-year minimum (EV/EBITDA 14.5x vs 18.6x floor) [Certain], and a 4.75% FCF yield plus a 50-year dividend record and buybacks pay holders to wait [Certain]. RSI of 24.7 is deeply oversold [Certain]; any stabilisation in US comps on Nov 4 could start a re-rating toward the historical P/E band [Guessing]. Beta of 0.45 makes it a low-risk compounder [Certain].

## Decision
```json
{
  "ticker": "MCD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class, real-estate-backed franchisor trades at its cheapest multiples in five years, but only at peer-level P/E and P/FCF, with weakening US traffic, franchisee friction and pricing litigation making the de-rating look justified rather than mispriced.",
  "rationale": "Quality is excellent but valuation is merely peer-level, not cheap, while FCF conversion is falling, leverage is 3.6x, and US traffic, litigation and a small macro bear tilt cloud the next 12 months. Probability-weighted upside is modest. Good but not compelling: conviction 3, below the buy threshold, so no position.",
  "price_at_decision": 230.88,
  "price_date": "2026-10-07",
  "research_note": "research/MCD/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2021 5-year low of 43.7%, showing franchisee-economics pressure is overwhelming the royalty and rent model.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 43.7}},
    {"text": "TTM FCF margin falls below the FY2022 5-year low of 23.7%, extending the decline in cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 23.7}},
    {"text": "TTM ROIC falls below the FY2022 5-year low of 17.0%, showing the franchise's return on capital is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 17.0}},
    {"text": "Change of mind (upside): US comparable sales in the next 10-Q/10-K (sec.gov) show traffic-led growth while the AI-pricing suit is dismissed or not certified, removing the two main fundamental overhangs."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 310.70, "basis": "US traffic stabilises and P/E re-rates to its 5y minimum of 25.3x [RA] on unchanged TTM earnings implied by the current 18.8x P/E [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 234.16, "basis": "Multiple holds at peer level as the de-rating proves a reset: P/FCF moves to the 21.4x peer median [P:QSR,P:YUM,P:SBUX,P:WEN] from 21.1x on flat TTM FCF [CF]."},
    "bear": {"probability": 0.35, "target_price_12m": 213.73, "basis": "Traffic weakness and franchisee pushback (note §6, TipRanks headlines [OV]) cut operating margin from 45.7% to the FY2021 low of 43.7% [IS] and P/E settles at the 18.2x peer median [RA]; bear weight raised by the macro overlay's small toward-bear real-yield tilt (research/MCD/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
