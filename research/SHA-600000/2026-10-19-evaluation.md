# Evaluation: Shanghai Pudong Development Bank Co., Ltd. (SHA:600000) — 2026-10-19

## Bear case
Returns are eroding structurally: ROE fell from 8.1% (FY2021) to 6.3% TTM, below any plausible cost of equity for a CNY lender [Certain] (RA). Net margin has slipped to 46.7% TTM [Certain] (IS), and the bank has little pricing power under PBOC-administered rates [Likely]. Shares outstanding rose 2.71% YoY, diluting holders [Certain] (ST). The P/B discount to peers (0.4x vs 0.6x) likely reflects weaker perceived asset quality or capital, which stockanalysis.com data cannot disprove [Likely]. The base fair value of 10.65 CNY offers only +9.4% against a -22.8% bear case, and the dividend-discount value (3.84-4.78 CNY) sits far below the price [Certain] (fair-value table). Piotroski F-Score is a middling 4 [Certain] (ST). Macro tilt is small toward bear via higher US yields in the discount rate [Likely] (macro overlay).

## Bull case
At 0.4x book and 6.9x earnings, the stock is in line with peers on P/E and near the low of its own P/B range, so expectations are depressed [Certain] (RA). ROE has stabilised from the FY2023 trough of 5.2% to 6.4% (FY2025), and net margin recovered from 38.3% (FY2023) [Certain] (RA, IS). The reverse DCF prices a -9.1% year-1 revenue decline, leaving room for upside if the China credit cycle simply stops worsening [Likely]. CNY has firmed against the dollar, removing a PBOC tightening risk to NIM [Likely] (macro overlay). The FCFE DCF value of 14.35 CNY points above the price [Certain] (fair-value table), though FCF is not meaningful for a bank [Certain] (note). Still, there is no catalyst and no moat [Guessing].

## Decision
```json
{
  "ticker": "SHA:600000",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A moatless Chinese joint-stock bank with ROE falling from 8.1% to 6.3% trades at a low P/B for a reason, and its base fair value offers only a thin margin of safety against a deeper bear case.",
  "rationale": "Falling ROE below the cost of equity, mild dilution, no pricing power and a peer P/B discount that likely reflects asset-quality doubts. Base fair-value upside is thin against a larger bear downside, and the macro overlay tilts slightly toward bear. Cheapness alone is not a compelling thesis; cash is preferable.",
  "price_at_decision": 9.73,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600000/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE rises above 8%, back to the FY2021 level, evidencing the returns decline was cyclical rather than structural.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 8}},
    {"text": "TTM net margin rises above 47.4%, the FY2021 five-year high, showing NIM and credit costs are improving.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 47.4}},
    {"text": "Shares outstanding stop growing (YoY change below 0%), ending per-share dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 12.34, "basis": "ROE recovers from the FY2023 trough and US yields ease, lifting the value to the mechanical bull fair value of 12.34 CNY (fair-value table; macro overlay macro_bull)."},
    "base": {"probability": 0.45, "target_price_12m": 10.65, "basis": "ROE holds near 6.3% TTM [RA] and P/B stays near its 5y median of 0.4x, consistent with the P/B+ROE and FCFE blend base fair value of 10.65 CNY (fair-value table)."},
    "bear": {"probability": 0.35, "target_price_12m": 7.51, "basis": "ROE keeps falling [RA] and higher US yields raise the discount rate, compressing value to the bear fair value of 7.51 CNY; probability raised slightly toward bear per the macro overlay's small bear tilt (research/SHA-600000/2026-10-19-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
