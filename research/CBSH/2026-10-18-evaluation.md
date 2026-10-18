# Evaluation: Commerce Bancshares, Inc. (CBSH) — 2026-10-18
## Bear case
Returns are fading: ROE has slid from 17.8% (FY23) to 14.7% TTM and the net margin trend is falling (-2.5pp) [Certain] (RA, IS). The "cheap" signals are weak for a bank: P/FCF of 6.6x and a 207.9% FCF conversion reflect balance-sheet swings, not distributable cash [Likely] (CF, IS). On book value it is not cheap: P/B 1.8x is 36% above the peer median of 1.4x [Certain] (RA). Piotroski F-score is only 4 [Certain] (ST). Shares rose 1.15% YoY with two acquisitions (FineMark, Nolan) to integrate [Likely]. The macro overlay tilts toward bear (small): 10y Treasury at 5.10% and real yields up +0.43pp in 3m raise the discount rate [Likely] (macro overlay). Q3 results on Oct 20, 2026 can reset every figure within days [Certain] (ST).
## Bull case
A conservatively underwritten, low-cost-deposit franchise with a large trust/wealth fee base (beta 0.59) [Likely] (ST). ROE of 14.7% is still above most regional peers, which justifies part of the P/B premium [Likely] (RA). P/E of 13.6x sits at the 14th percentile of its 5y range and P/B is below its 5y minimum [Certain] (RA). Mechanical fair value is above the price in every scenario: bear 59.24, base 65.95, bull 70.72 [Certain] (fact sheet), and the reverse DCF implies -0.8% year-1 revenue growth [Certain]. FineMark adds Sunbelt wealth assets ($8.7bn under administration [company-reported], https://www.sec.gov/Archives/edgar/data/22356/000002235626000190/cbsh-20260630.htm) and Q2 showed an expanding net interest margin [Likely].
## Decision
```json
{
  "ticker": "CBSH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, low-cost-deposit regional bank trading near the low end of its own multiple history, but with fading ROE and a book-value premium to peers the upside is not compelling.",
  "rationale": "Quality is real but returns are drifting down, P/B is rich versus peers, FCF-based cheapness is unreliable for a bank, and the macro overlay tilts slightly bearish. Base fair value upside is modest and Q3 results arrive in two days. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 55.70,
  "price_date": "2026-10-16",
  "research_note": "research/CBSH/2026-10-18.md",
  "triggers": [
    {"text": "ROE falls below 12% TTM (vs 14.7% now): franchise/margin deterioration beyond the rate cycle", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Net (profit) margin falls below 28% TTM (vs 31.6% now): credit or funding-cost pressure not offset by fee income", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Efficiency ratio rises above 63% [company-reported, 10-Q]: FineMark integration costs running above plan"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 70.72, "basis": "NIM expansion continues and ROE stabilises, so the blended fair value bull case of 70.72 (P/B + ROE and FCFE DCF) is reached [fact sheet Fair value; RA]."},
    "base": {"probability": 0.5, "target_price_12m": 62.0, "basis": "ROE holds near 14.7% TTM [RA] so P/B + ROE values the stock between its bear 60.86 and base 65.79; set below the mechanical base 65.95 because the macro overlay tilts toward bear (small) on a rising discount rate (research/CBSH/2026-10-18-macro.md)."},
    "bear": {"probability": 0.3, "target_price_12m": 49.62, "basis": "ROE keeps sliding toward the 12% trigger and higher real yields compress the multiple, taking the stock back to its 6-month low of 49.62 [HI]; probability raised by the overlay's bear tilt (research/CBSH/2026-10-18-macro.md)."}
  },
  "entry_price": 52.76,
  "entry_basis": "valuation file: base 65.95 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
