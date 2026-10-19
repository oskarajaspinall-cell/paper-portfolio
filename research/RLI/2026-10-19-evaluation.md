# Evaluation: RLI Corp. (RLI) — 2026-10-19
## Bear case
The cheapness is mostly an artefact of earnings mix. P/E of 12.8x sits low in its own range, but the Q2 2026 release shows net earnings far above operating earnings, so TTM EPS is flattered by investment gains [Likely]. The owner's best method (P/B + ROE) puts fair value at 61.10 base, essentially the 61.07 close [Certain]. P/B of 3.2x is still a 45% premium to peers and P/FCF a 25% premium [Certain]. Property pricing is softening and the 59.4% property combined ratio [company-reported] is a peak-cycle figure likely to normalise, while casualty runs at 98.2% [company-reported], close to breakeven, with core CPI pressuring claims [Likely]. Premium growth was only 3% in Q2 [Likely]. Short interest of 10.81% is rising [Certain]. Q3 results land tonight, an unpriced binary [Certain].

## Bull case
RLI is a best-in-class specialty underwriter: ROE 25.2% and ROIC 21.3% TTM, ROIC rising over 5y [Certain], 36 consecutive years on the Ward's 50 list [Likely]. It walks away from mispriced business rather than chase volume [Likely]. Leverage is minimal (net debt/EBITDA 0.56x) and FCF conversion is 117.9% [Certain]. P/B and EV/Sales sit below their own 5y minimums [Certain]. Elevated rates keep lifting net investment income, up 17% in Q2 [Likely], and beta of 0.32 makes it a portfolio diversifier [Certain]. The blended base fair value of 69.54 is above the price [Certain].

## Decision
```json
{
  "ticker": "RLI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A top-tier specialty underwriter with 25% ROE trades near the bottom of its own P/B range, but its best-method fair value sits at the price and the soft property cycle caps the re-rating.",
  "rationale": "Quality is excellent, but the P/B + ROE value equals the price; the P/E upside relies on gain-inflated net earnings, property margins look peak-cycle and casualty is near breakeven. Good but not compelling at this price, with Q3 results tonight. Conviction 3: AVOID, watch for a lower entry.",
  "price_at_decision": 61.07,
  "price_date": "2026-10-16",
  "research_note": "research/RLI/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE falls below 15%, breaking the five-year record of 23%+ and signalling underwriting or reserving deterioration.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "Casualty segment or overall combined ratio (10-Q MD&A, company-reported) exceeds 100% for two consecutive quarters."},
    {"text": "Casualty prior-year reserve development (10-Q MD&A, company-reported) turns adverse for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 73.96, "basis": "Rates stay elevated so investment income keeps compounding (macro overlay macro_bull, research/RLI/2026-10-19-macro.md) and P/B recovers toward its 5y median 4.3x [RA], reaching the mechanical bull fair value 73.96."},
    "base": {"probability": 0.5, "target_price_12m": 64.0, "basis": "Value sits between the best-method P/B + ROE base 61.10 and the blended base 69.54 [fact sheet], below the blend because the P/E leg (86.43) uses TTM net earnings flattered by investment gains; macro tilt neutral/small, no probability change."},
    "bear": {"probability": 0.25, "target_price_12m": 55.0, "basis": "Soft property pricing normalises the 59.4% property combined ratio [company-reported, 10-Q] and casualty loss-cost inflation pushes ROE down, taking the price toward the mechanical bear 56.73 and the 54.50 swing low [HI]."}
  },
  "entry_price": 55.63,
  "entry_basis": "valuation file: base 69.54 x 0.8; at that level the excellent underwriting quality would be bought below even the best-method P/B + ROE bear value of 60.79.",
  "replaces": null,
  "replacement_reason": null
}
```
