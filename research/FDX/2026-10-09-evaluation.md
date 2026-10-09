# Evaluation: FedEx Corporation (FDX) — 2026-10-09
## Bear case
At 291.73 the stock sits above every point of its own fair-value range: base 259.21 (-11.1%) and even bull 272.70 (-6.5%) [Certain]. The reverse DCF already prices 4.7% year-1 revenue growth [Certain]. The FCF step-up to a 5.4% margin and 115.4% conversion coincides with capex at a record low as a % of revenue, so part of it is timing, not efficiency [Likely]. The cheapness against peers is mostly mix: XPO, CHRW and JBHT are asset-light and structurally trade at higher multiples [Likely]. The Freight spin-off muddies the 5y margin and ROIC trend [Likely]. Momentum is weak (-22.6% over 6 months, 50-day below the 200-day), FQ2 results are due Oct 28 [Certain], and the macro overlay flags a stronger dollar and higher real yields as a drag on international Express and on the discount rate [Likely].
## Bull case
Network 2.0 and DRIVE are structural cost-out programmes: operating margin has risen from 6.2% to 7.9% and ROIC from 8.3% to 9.2% [Certain], with management targeting about $6B of FCF by 2029 [Likely]. The FCF yield is 7.44% and P/FCF of 13.4x is below the 5y low of 17.5x [Certain]. EV/EBITDA of 8.3x matches its 5y median, and P/E of 15.7x is in the 31st percentile of its own range [Certain]. Net debt/EBITDA has fallen to 2.48x from 3.10x, the share count is down 1.65% YoY, and short interest is low and falling [Certain]. If margins keep expanding, the earnings base rises and the DCF moves up with it [Guessing].
## Decision
```json
{
  "ticker": "FDX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A carrier whose margins and returns are improving under Network 2.0, but at 291.73 it trades above its own blended fair-value range (base 259.21, bull 272.70), so the self-help story is already in the price.",
  "rationale": "The business is improving, but the price already reflects it. The stock is above even the bull fair value. The FCF step-up is partly capex timing, and the peer discount is mostly mix. Macro (stronger dollar, rising real yields) tilts toward the bear case, and earnings are due Oct 28. That is good but not compelling: conviction 3, so AVOID.",
  "price_at_decision": 291.73,
  "price_date": "2026-10-08",
  "research_note": "research/FDX/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 7.0%, signalling the Network 2.0 / DRIVE cost-out has stalled (now 7.9%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7.0}},
    {"text": "TTM FCF margin falls below 4%, showing the jump to 5.4% was capex timing rather than structural.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt/EBITDA rises above 2.9x, reversing the deleveraging from 3.10x to 2.48x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.9}},
    {"text": "TTM ROIC falls below 8.3%, the FY2022 5y low, reversing the improvement in returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 331.1, "basis": "Network 2.0 margin gains continue and EV/EBITDA re-rates toward the upper part of its 7.6x-11.1x 5y range [RA], i.e. the fact sheet's EV/EBITDA bull value of 331.10; probability trimmed by 0.05 for the macro overlay's small tilt toward bear (research/FDX/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 280.0, "basis": "EV/EBITDA holds near its 5y median 8.3x (EV/EBITDA base 290.62 [RA]) but is pulled toward the blended base fair value of 259.21 because the DCF already discounts at a 5.28% risk-free rate; we sit between the two and above the DCF because the cost-out programme is structural (Citi TMT transcript)."},
    "bear": {"probability": 0.3, "target_price_12m": 224.61, "basis": "The FCF margin reverts as capex normalises (AGM transcript), and a stronger dollar and higher real yields (macro overlay, tilt toward bear, +0.05 probability) drag on Express, sending the stock back to its 52-week low of 224.61 [HI], below the EV/EBITDA bear of 255.48 but far above the DCF bear of 56.43, which we treat as a tail."}
  },
  "entry_price": 207.37,
  "entry_basis": "valuation file: base 259.21 x 0.8 = 207.37; at that level the improving margins and the 7%+ FCF yield would be bought with a margin of safety against the own-history DCF.",
  "replaces": null,
  "replacement_reason": null
}
```
