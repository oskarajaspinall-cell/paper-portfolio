# Evaluation: NVIDIA Corporation (NVDA) — 2026-11-16
## Bear case
Earnings land on Nov 17, 2026, the next trading day, while headlines question Jensen Huang's status as CEO; neither is resolved by a company source [Certain]. Rolling returns are falling: ROIC 175.0% to 92.0%, ROCE 82.4% to 71.3%, FCF margin 43.6% to 41.9%, FCF conversion 65.8% from 80.5% [Certain]. The cause looks partly structural, not a reset: supply and capacity commitments rose to $279 billion from $119 billion [company-reported], $99 billion of equity investments partly fund customers, and a guarantee capped at $105 billion [company-reported] ties NVIDIA to OpenAI-linked capacity [Likely]. Revenue increasingly depends on customers' access to capital, which is circular [Likely]. The through-cycle base fair value of 86.02 sits far below the 162.85 close, and the price implies 40.4% year-1 growth [Certain]. Price is below its 200-day average, 26.8pp behind SPY over 12 months; no trend support [Certain]. China export rules tightened again [Likely].
## Bull case
The economics remain exceptional: TTM operating margin 65.2% is a 2-year high, gross margin 74.7%, ROIC 92.0%, net cash [Certain]. The ROIC fall reflects a bigger capital base, not eroding margins [Likely]. P/E 20.1x and EV/EBITDA 19.4x sit below their 5-year minimums and under the peer medians of 42.6x and 23.0x, so the market already prices a peak [Certain]. CUDA and the annual architecture cadence (Blackwell, Vera Rubin shipping) are a durable moat [Likely]. Buybacks cut shares 1.04% YoY [Certain]. If results and the CEO question resolve cleanly, a re-rating toward the bull fair value of 208.52 is plausible [Guessing]. RSI 23.6 shows a washed-out price [Certain].
## Decision
```json
{
  "ticker": "NVDA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "ROIC, ROCE and FCF margin fall on a rolling basis while operating margin rises: the denominator and cash are absorbed by supply commitments up to $279 billion from $119 billion, equity investments partly funding customers and a guarantee capped at $105 billion [company-reported] (https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); FCF conversion fell to 65.8% from 80.5%. A business-model shift toward vendor financing, not a guided one-off.",
    "moat": "wide",
    "key_risk": "high",
    "key_risk_text": "AI capex financed partly by NVIDIA itself (commitments, customer financing, OpenAI-linked guarantee) slows, exposing peak earnings that the through-cycle fair value of 86.02 already assumes; earnings on Nov 17, 2026 could show it.",
    "veto": {"code": "governance", "reason": "Headlines report Jensen Huang as 'former CEO' with a possible return; no company source confirms the CEO's status, and earnings report the next trading day (https://nypost.com/2026/11/16/business/nvidia-stock-falls-for-third-straight-day-over-huang-affair-fallout/)."}
  },
  "thesis": "A wide-moat AI-compute leader with exceptional margins trades below its own 5-year multiple range, but rising vendor financing, unresolved CEO status and next-day earnings make the earnings base too uncertain to buy.",
  "rationale": "Margins are best in class and multiples sit below their 5-year range, but returns and cash conversion are falling as NVIDIA finances its own demand, the price sits far above the through-cycle fair value and below its 200-day average, and the CEO question is unresolved. Conviction 3: AVOID; cash is acceptable.",
  "price_at_decision": 162.85,
  "price_date": "2026-11-13",
  "research_note": "research/NVDA/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 55% (65.2% now), showing pricing power or mix is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 55}},
    {"text": "TTM gross margin falls below 68% (74.7% now), showing competition from custom silicon or AMD is forcing price cuts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "Debt/EBITDA rises above 0.5x, meaning guarantees or purchase commitments are being funded with debt.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0.5}},
    {"text": "Positive: a company release confirms the CEO succession and TTM FCF conversion (FCF/NI, cash-flow statement) recovers above 80% with supply commitments no longer rising, removing the vendor-financing concern."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 208.52, "basis": "Clean results and a resolved CEO question let multiples recover toward the bull fair value of 208.52 [fact sheet Fair value], still below the 5y minimum P/E of 38.0x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 160.0, "basis": "Multiples stay below their 5y range (P/E 20.1x vs min 38.0x [RA]) as falling ROIC and FCF conversion [RA-T, CF] cap any re-rating; price roughly flat."},
    "bear": {"probability": 0.3, "target_price_12m": 86.02, "basis": "Customer-financed AI demand slows and margins revert toward the through-cycle base fair value of 86.02 [fact sheet Fair value], the risk the note's $279 billion commitments [company-reported] create."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unresolved CEO status, next-day earnings and the shift toward vendor financing would not be fixed by a lower price; re-research after results and a company statement on leadership."
}
```
