# Evaluation: Protagonist Therapeutics (PTGX) — 2026-11-15
## Bear case
Revenue is licence, milestone and collaboration income, not product sales, so TTM profitability is milestone timing: FY2025 operating margin was -343.6% against 58.6% TTM [Certain]. The FCF margin is falling over the last 12 months (30.5% to 19.8%) and sits far below its 2-year high of 161.3%; FCF conversion is only 31.9% of net income [Certain]. That Direction change reflects lumpy milestone receipts rather than lost share [Likely], but it means the 58.6% margin is not a stable base [Likely]. At 78.3x P/FCF (78% of its 5y range, well above peers) and a 1.28% FCF yield, the valuation points come from trend strength, not a discount: if royalty ramps from J&J and Takeda disappoint, an extended multiple de-rates hard [Likely]. Shares rose 8.19% YoY despite the buyback, and short interest is 19.16% of float [Certain]. Icotrokinra was non-inferior, not superior, to ustekinumab [Certain].
## Bull case
Two first-in-class peptides were approved this year, icotrokinra (J&J) and MIMRYLO (Takeda), turning a cash-burning discoverer into a profitable royalty platform: TTM operating margin 58.6% versus 9.1% a year earlier, ROCE 29.6% [Certain]. The balance sheet is net cash (net debt/EBITDA -2.44x), funding a buyback and the oral IL-17 and obesity pipeline without dilution risk [Likely]. Q3 revenue and EPS beat per headline, and Phase III UC enrollment completed ahead of schedule [Likely]. The stock is in an uptrend (above its 200-day average, 12-month +54.3%) and P/E of 26.6x is below the peer median [Certain]. Partner-run launches mean royalties scale with little cost, so margins can stay high as milestones give way to recurring royalties [Guessing].
## Decision
```json
{
  "ticker": "PTGX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell from 30.5% to 19.8% over the last 12 months because cash milestone receipts are lumpy (FCF conversion 31.9% of net income, receivable timing) while TTM operating margin rose to 58.6% on two 2026 approvals [IS-T, CF-T; note section 2].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Profit depends on partner-controlled launches and milestone timing (FY2025 operating margin -343.6%); a slower royalty ramp would both cut earnings and de-rate an extended 78.3x P/FCF multiple.",
    "veto": null
  },
  "thesis": "Two approved first-in-class peptides could turn Protagonist into a durable royalty platform, but current profits are milestone-driven and the cash-flow multiple already prices persistence.",
  "rationale": "Quality has inflected and the balance sheet is net cash, but earnings rest on lumpy partner milestones, cash conversion is weak and the base fair value offers little discount. Good but not compelling: AVOID; re-research if the price offers a real margin of safety.",
  "price_at_decision": 130.95,
  "price_date": "2026-11-13",
  "research_note": "research/PTGX/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20% (income statement, trailing).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 10% (statistics page).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Shares change YoY rises above 12% despite the buyback.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 12}},
    {"text": "Icotrokinra or MIMRYLO suffers a label restriction, safety action or partner termination (company or SEC filings)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 200.0, "basis": "Royalty ramps from J&J and Takeda sustain the 58.6% TTM operating margin and EV/Sales moves toward its 5y median 16.7x [RA], below the mechanical bull of 385.39 which assumes the 5y max multiple."},
    "base": {"probability": 0.5, "target_price_12m": 144.52, "basis": "Launches progress in line, EV/Sales holds near current levels: the mechanical EV/Revenue base fair value of 144.52 [valuation file]."},
    "bear": {"probability": 0.25, "target_price_12m": 77.0, "basis": "Milestone revenue lumps lower as in FY2025 (operating margin -343.6% [IS]) and P/FCF de-rates from 78% of its 5y range [RA]; set at the 52-week low of 77.00 [HI], above the mechanical bear 43.50 as royalties now provide a floor."}
  },
  "entry_price": 115.62,
  "entry_basis": "valuation file: base 144.52 x 0.8 (fact sheet Fair value, EV/Revenue [RA])",
  "replaces": null,
  "replacement_reason": null
}
```
