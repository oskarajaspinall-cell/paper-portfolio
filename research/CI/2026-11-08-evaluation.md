# Evaluation: The Cigna Group (CI) — 2026-11-08
## Bear case
2027 is a guided headwind year: management flagged PBS rebate changes, GLP-1 cost pressure and the exit from Individual and Family Plans from the start of 2027 (Q3 2026 transcript; SEC 10-Q) [Certain]. Gross margin has fallen from 13.2% to 9.1% over five years and FCF margin of 2.9% TTM now sits below the FY2025 five-year low of 3.1% [IS, CF] [Certain]. Over the last year ROIC, ROCE and both margins are only flat, and ROIC is 1.6pp below its March 2026 peak of 14.3% [RA-T]; no Direction change line fired, but there is no real improvement either [Certain]. Rebate reform could turn a cyclical squeeze into structural PBM margin loss, and the mechanical bear fair value of 268.11 is below the price [Likely]. GAAP Q3 EPS fell year on year despite the adjusted beat (WSJ headline) [Likely].

## Bull case
The price implies -2.7% year-1 revenue growth while Q3 revenue grew and FY26 adjusted EPS guidance rose to at least $30.60 [fact sheet Fair value; PRNewswire] [Certain]. P/E 13.0x sits near the bottom of its 5y range (median 15.1x) and EV/EBITDA 7.9x is below its 5y minimum of 8.4x, at a 10.69% FCF yield [RA, ST] [Certain]. FCF conversion is 138.0%, shares are down 2.66% a year and net debt/EBITDA has fallen from 2.84x to 1.87x [CF, ST, RA] [Certain]. The macro overlay is context only (beta 0.25, US-centric revenue, no country risk) [Certain]. Accelerate to One cost savings and Signature adoption support earnings beyond 2027 [Likely]. Headwinds are known and largely priced [Likely].

## Decision
```json
{
  "ticker": "CI",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A deleveraging PBM and employer-health franchise with stable ROIC of 12.7% and a 10.69% FCF yield trades near the bottom of its own 5-year P/E range and below its EV/EBITDA minimum, where the price implies revenue decline that raised 2026 guidance does not show.",
  "rationale": "Thesis intact: Q3 beat, guidance raised, leverage down, valuation still near own-history lows and below base fair value. But flat recent returns, FCF margin at a five-year low and guided 2027 rebate/GLP-1 headwinds stop short of adding. Conviction 4 keeps the current size; HOLD rather than ADD.",
  "price_at_decision": 293.59,
  "price_date": "2026-11-06",
  "research_note": "research/CI/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, giving up most of the five-year improvement from 8.8% to 12.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 3.5%, under the FY2025 five-year low of 3.7%, showing PBS rebate reform or medical cost pressure is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3.5}},
    {"text": "TTM FCF margin falls below 2.0%, well under the current 2.9%, signalling cash generation and buyback capacity are deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.0}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.87x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 421.42, "basis": "2027 headwinds prove manageable and the stock reaches the mechanical blended base fair value of 421.42 [fact sheet Fair value]; set well below the DCF-driven mechanical bull of 852.56, which the note gives little weight."},
    "base": {"probability": 0.5, "target_price_12m": 342.42, "basis": "Raised FY26 guidance holds and P/E recovers toward its 5y median of 15.1x [RA], the mechanical P/E base value of 342.42 [fact sheet Fair value]; set below the DCF base of 460.91 because the guided 2027 PBS rebate, GLP-1 and IFP-exit headwinds (Q3 2026 transcript) make the DCF's growth path optimistic."},
    "bear": {"probability": 0.25, "target_price_12m": 268.11, "basis": "Rebate reform makes the margin squeeze structural, with gross margin extending its fall from 13.2% to 9.1% [IS]: the mechanical bear fair value of 268.11 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Already held at conviction 4, the buy bar; no lower price is needed to justify conviction 4, and an ADD is held back by the guided 2027 headwinds, not by price.",
  "replaces": null,
  "replacement_reason": null
}
```
