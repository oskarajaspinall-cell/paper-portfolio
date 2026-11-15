# Evaluation: NVIDIA Corporation (NVDA) — 2026-11-15
## Bear case
The price did not fall on the business. The CEO and co-founder resigned on 12 Nov with immediate effect, the board has outside counsel investigating a possible foreign-intelligence angle, and no successor is named [Certain]. Earnings arrive on 17 Nov, so the outcome is binary within days [Certain]. Under the surface, capital is being committed faster than profit grows: TTM ROIC fell from 175.0% to 92.0% and FCF conversion to 65.8%, as supply commitments rose to $279 billion from $119 billion, equity investments reached $99 billion and guarantees for OpenAI-hosting leases are capped at $105 billion [company-reported] (https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) [Certain]. That is vendor financing of demand [Likely]. Extended payment terms are already lowering cash conversion [Certain]. Chip-smuggling reports add export-control risk [Guessing]. The mechanical base fair value of 86.01 sits well below the price [Certain].

## Bull case
The economics are still exceptional and improving at the operating line: TTM operating margin rose 7.1pp to 65.2%, its 2-year high, with gross margin 74.7% and net cash [Certain] (https://stockanalysis.com/stocks/nvda/financials/ratios/). The ROIC fall is a larger capital base (cash, investments), not lost share [Likely]. CUDA and system-level integration remain a durable moat no leadership change removes quickly [Likely]. At 20.6x P/E the stock is below its 5y minimum of 38.0x and 42% below peers, with EV/EBITDA 19.4x under its 5y floor of 33.9x [Certain]. Reports cast doubt on the espionage allegation and major investors ask the board to keep Huang's return open [Likely] (https://www.cnbc.com/2026/11/14/nvidia-investors-jensen-huang-return-board-letter.html). RSI 24.9 shows a capitulation-style sell-off into results [Certain].

## Decision
```json
{
  "ticker": "NVDA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and FCF margin fall while TTM operating margin rose 7.1pp to a 2-year high of 65.2% [IS-T]: the capital base (cash, $99 billion equity investments [company-reported]) and extended customer payment terms grew, not lost share or a price cap (note s.2, s.5).",
    "moat": "wide",
    "key_risk": "high",
    "key_risk_text": "Leadership vacuum and board investigation after the CEO's immediate resignation, compounded by customer vendor-financing commitments ($279 billion supply commitments, $105 billion lease guarantees [company-reported]) that could turn demand circular.",
    "veto": {"code": "governance", "reason": "CEO/co-founder resigned 12 Nov 2026 with immediate effect amid a board investigation into a possible foreign-intelligence effort; no successor and earnings on 17 Nov make this an unresolved governance and binary event the score cannot see."}
  },
  "thesis": "A wide-moat AI-compute leader at the lowest multiples of its 5-year history, but an unresolved CEO exit and investigation plus growing customer-financing commitments make the outcome binary now.",
  "rationale": "The fall is driven by the CEO's sudden resignation and a board investigation, not results; earnings land on 17 Nov. Until leadership and the investigation are resolved the risk is unpriceable, and the price sits above the mechanical base fair value. Governance veto caps conviction at 3: AVOID, no position.",
  "price_at_decision": 162.85,
  "price_date": "2026-11-13",
  "research_note": "research/NVDA/2026-11-15.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unresolved CEO exit and board investigation are. A lower price would not change the decision; a re-research is warranted once a permanent CEO is in place and the investigation concludes.",
  "triggers": [
    {"text": "TTM operating margin falls below 55%, showing the AI build-out pricing power is fading.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 55}},
    {"text": "Net debt/EBITDA rises above 0.5x, i.e. net cash gives way to leverage as commitments and guarantees are drawn.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0.5}},
    {"text": "TTM FCF margin falls below 35%, showing extended customer payment terms are becoming a structural cash drain.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35}},
    {"text": "The board names a permanent CEO (or reinstates Huang) and the investigation concludes without finding a foreign-intelligence compromise, as disclosed in a company release or filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 208.51, "basis": "Leadership resolved quickly and results confirm the 65.2% operating margin [IS-T], so the multiple recovers toward the mechanical bull fair value 208.51 [fact sheet Fair value], still below the 52-week high 243.37 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 162.85, "basis": "Earnings hold but a governance and vendor-financing discount keeps P/E near 20.6x, below its 5y minimum 38.0x [RA]; above the mechanical base 86.01 because the through-cycle DCF treats TTM margins as peak (note s.3)."},
    "bear": {"probability": 0.25, "target_price_12m": 86.01, "basis": "Leadership vacuum persists and customer commitments sour (note s.5), margins normalise to through-cycle levels and the price falls to the mechanical base fair value 86.01 [fact sheet Fair value]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
