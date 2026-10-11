# Evaluation: The Hershey Company (HSY) — 2026-10-11
## Bear case
The moat did not protect margins: FY2025 gross margin fell to 33.5% from 47.4% and ROIC to 11.3% when cocoa spiked [Certain] (RA, IS). The margin is recovering only by pricing, and North American confectionery volumes fell meaningfully in Q2 on elasticity [Likely] (Barclays transcript), so the recovery may cost volume. On EV/EBITDA (13.9x, +58%), EV/Sales (+61%) and P/FCF (+53%) the stock still trades well above its peers [Certain] (fact sheet). The P/E looks low only against a 5y range set when returns were much higher. A new CFO and a new International president arrive during the restoration year [Certain] (OV news). Q3 results land on Oct 29, 2026 [Certain] (ST), so the margin evidence is binary and close. Bear fair value of $109.82 is 32.5% below the price, against 15.7% upside to base [Certain] (fact sheet). The skew is not asymmetric enough.

## Bull case
The shock looks cyclical: Q2 2026 gross margin recovered to 45.3% from 30.5% a year earlier [Certain] (sec.gov 10-Q). TTM ROIC of 17.7% and operating margin of 18.0% are already climbing back from the FY2025 trough [Certain] (RA, IS). Cash held up through the squeeze: TTM FCF margin is 18.3% and the FCF yield 6.81% [Certain] (ST, CF). P/FCF of 14.7x and EV/Sales of 3.1x sit below their own 5y minimums, and the price implies only 1.4% revenue growth [Certain] (fact sheet). If FY2024-level margins return, base ($188.32) to bull ($210.96) fair value is reachable [Likely]. Leverage is easing to 1.89x net debt/EBITDA [Certain] (RA). Brand leadership (Reese's) supports pricing power over a cycle [Likely].

## Decision
```json
{
  "ticker": "HSY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A branded US confectionery leader whose cocoa-driven margin collapse is reversing trades below its own 5-year P/FCF and EV/Sales minimums, but the 15.7% upside to base fair value is not enough against the 32.5% bear-case downside while volumes are falling.",
  "rationale": "The margin recovery is real but recent, it comes from price rather than volume, and it gets tested on Oct 29. Upside to base fair value is +15.7% against -32.5% to the bear case, and the stock still trades at a large premium to peers on EV/EBITDA and P/FCF. That is good but not compelling, so conviction 3 means no position.",
  "price_at_decision": 162.74,
  "price_date": "2026-10-09",
  "research_note": "research/HSY/2026-10-11.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, showing cocoa pass-through and margin restoration have stalled after Q2 2026's 45.3%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM ROIC falls below 11%, under the FY2025 trough of 11.3%, showing the return collapse is structural rather than a one-year commodity shock.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "TTM operating margin falls below 12.6%, the FY2025 trough, signalling the profit-restoration year has failed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.6}},
    {"text": "North American confectionery volumes, as reported in quarterly filings or earnings releases, decline for two further consecutive quarters, showing pricing elasticity is worse than management's view."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 211, "basis": "Gross margin holds near Q2 2026's 45.3% (sec.gov 10-Q), so returns head back toward FY2024's 29.4% ROIC [RA]. That reaches the fact sheet's bull fair value of $210.96 [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 188, "basis": "Margin restoration continues but volumes stay soft (Barclays transcript), so the stock converges on the mechanical base fair value of $188.32 (DCF/P/E blend, fact sheet)."},
    "bear": {"probability": 0.25, "target_price_12m": 113, "basis": "Volume elasticity and renewed cocoa pressure stall the recovery, and P/E de-rates to its 5y minimum of 15.4x [RA] on TTM EPS. This matches the P/E bear value of $112.89 (fact sheet)."}
  },
  "entry_price": 150.66,
  "entry_basis": "valuation file: base 188.32 x 0.8. With that 20% margin of safety, the same margin-recovery evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
