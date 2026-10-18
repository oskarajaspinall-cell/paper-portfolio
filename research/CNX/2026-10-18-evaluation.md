# Evaluation: CNX Resources Corporation (CNX) — 2026-10-18
## Bear case
CNX is a price-taker on Appalachian gas, and the US is in a glut where some producers must pay to have gas taken away (Reuters, 2026-05-01) [Likely]. Reported earnings are unreliable: operating margin swung from 153.1% in FY2023 to 0.4% in FY2024 and back to 59.1% TTM [IS], a pattern consistent with hedge mark-to-market rather than operating change [Likely]; FCF conversion is only 55.4% TTM [CF,IS] and the hedge book lost $166m in cash YTD [company-reported] [Certain]. The mechanical fair value runs from -1.94 to 178.78 [Fair value], so the model gives no anchor [Certain]. Altman Z of 1.71 [ST] sits in the distress zone, short interest is 11.69% and rising [ST], a new CFO arrived in September, and Q3 results land on Oct 29 [ST,OV] [Certain]. The cheap P/E is near the middle of its own 5y range, not at a floor [RA] [Certain].
## Bull case
On cash rather than accounting earnings, CNX is cheap: a 9.90% FCF yield [ST] and P/FCF of 10.1x against a 13.7x peer median [RA] [Certain]. FCF margin has risen for five years to 24.6% TTM [CF,IS], net debt/EBITDA is down to 1.30x [BS,IS] and Piotroski F is 8 [ST] [Certain]. Owned midstream gives a cost edge in-basin [Likely], and management prioritises buybacks with capex on guidance (Q2 2026 call) [Likely]. H1 2026 net income of $551m vs $235m a year earlier [company-reported] shows operating leverage to any gas recovery, and LNG-export demand is a structural tailwind the market may be underpricing [Guessing]. Every peer multiple is at a discount despite comparable leverage [RA] [Certain].
## Decision
```json
{
  "ticker": "CNX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-generative Appalachian gas producer trades at a discount to peers on FCF, but its value depends on a gas price it cannot control and its reported earnings are too hedge-distorted to anchor a high-conviction core position.",
  "rationale": "The FCF discount to peers is real, but earnings quality is poor, the fair-value range is uninformative, gas is in a US glut and Q3 results plus a new CFO are imminent. Good but not compelling: conviction 3, so AVOID and hold cash.",
  "price_at_decision": 35.91,
  "price_date": "2026-10-16",
  "research_note": "research/CNX/2026-10-18.md",
  "triggers": [
    {"text": "Net debt/EBITDA (ratios page) rises above 3.0x, showing the deleveraging has reversed.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM FCF margin falls below 10%, reversing the five-year rise to 24.6%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 8%, giving up most of the improvement to 14.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Sales volumes in the 10-Q MD&A decline more than guided for two consecutive quarters beyond normal depletion."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 48.5, "basis": "P/FCF re-rates toward the 13.7x peer median [RA] on stable TTM FCF as gas demand from LNG exports absorbs the glut; well below the mechanical bull 178.78 because the 173.4x EV/EBITDA peak [RA] inflates that case."},
    "base": {"probability": 0.5, "target_price_12m": 37, "basis": "Multiples stay near current P/FCF 10.1x [RA] with buybacks adding modestly; far below the mechanical base 76.14 because that model uses a 13.7x 5y-median EV/EBITDA [RA] distorted by near-zero FY2021-22 EBITDA."},
    "bear": {"probability": 0.25, "target_price_12m": 23, "basis": "Gas glut (Reuters 2026-05-01) and hedge losses compress cash flow and P/B falls to its 5y low 0.7x [RA]; above the mechanical bear -1.94, which is a model artefact rather than a going-concern signal."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below peers on every multiple; the block is hedge-distorted earnings, gas-price dependence and an uninformative fair-value range, so a lower price would not change the decision before Q3 results show cash-flow quality.",
  "replaces": null,
  "replacement_reason": null
}
```
