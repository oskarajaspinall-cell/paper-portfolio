# Evaluation: The Allstate Corporation (ALL) — 2026-10-07
## Bear case
The 4.5x P/E is a peak-cycle number, not a bargain. TTM ROE of 46.1% and ROIC of 32.6% sit far above the FY2021 levels of 18.7% and 15.5%, and only three years ago both were negative [Certain]. P&C margins mean-revert as competitors re-enter on rate and states cap pricing [Likely]. On book value, the less cyclical yardstick, ALL is at 1.8x: mid-range in its 5-year band (1.3x-2.4x) and only 11% below peers, so it is not obviously cheap [Certain]. Catastrophe losses are structural to the homeowners book: $748m in August and $682m in July [Certain]. FCF conversion has swung wildly, from -2,106.9% in FY2023 to 92.1% TTM, so the 21.6% FCF yield is not a dependable floor [Certain]. Piotroski F of 4 is weak [Certain]. The stock trails SPY by 10.0pp over 12 months, and Q3 results come on Nov 4 [Certain].
## Bull case
Even if earnings halve, ALL would trade near its 5-year median P/E of 11.2x [Guessing]. The balance sheet is conservative and leverage keeps falling: net debt/EBITDA is 0.44x TTM, down from 1.04x in FY2021 [Certain]. That funds buybacks, and shares outstanding fell 1.96% YoY [Certain]. Book value compounds quickly at a 46.1% ROE, so even a flat 1.8x P/B lifts the price as equity grows [Likely]. The macro overlay is tilted toward bull, small: higher reinvestment yields, with the 10y at 5.31%, lift net investment income as underwriting normalises [Likely]. Beta of 0.13 and negligible short interest (0.01%) limit market-driven downside [Certain]. RSI of 29.6 shows the stock is oversold after a -9.7% 3-month move [Certain].
## Decision
```json
{
  "ticker": "ALL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Allstate is a well-capitalised P&C insurer whose 4.5x P/E reflects peak-cycle 46% ROE; on book value (1.8x, mid-range and only 11% below peers) the market is rightly pricing underwriting mean reversion, leaving a good but not compelling setup.",
  "rationale": "The earnings-multiple discount is cyclical, not mispricing: P/B sits mid-range and close to peers. Catastrophe losses, the history of volatile cash conversion, weak F-score and Q3 results on Nov 4 cap conviction at 3. The small macro tilt toward bull does not change that. Below the conviction-4 owner bar, so no position; cash is acceptable.",
  "price_at_decision": 224.27,
  "price_date": "2026-10-06",
  "research_note": "research/ALL/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROE falls below 15%, under the FY2021 level of 18.7%, confirming the underwriting-cycle tailwind has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below the FY2021 level of 15.5%, showing the current return profile was cycle-driven, not structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15.5}},
    {"text": "Net debt/EBITDA rises above 1.5x, signalling the balance-sheet cushion behind buybacks is eroding.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.30, "target_price_12m": 299.03, "basis": "Elevated ROE proves stickier and P/B re-rates to its 5y max of 2.4x from 1.8x [RA]. Probability is raised 5pp from bear per the macro overlay (research/ALL/2026-10-07-macro.md, tilt toward bull, small), because higher reinvestment yields support net investment income."},
    "base": {"probability": 0.45, "target_price_12m": 249.19, "basis": "P/B moves to the 2.0x peer median from 1.8x [RA, P:PGR, P:TRV, P:CB, P:HIG] as buybacks (-1.96% shares YoY [ST]) and book growth offset partial ROE normalisation from 46.1% TTM [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 161.97, "basis": "Underwriting margins mean-revert and catastrophe losses ($748m August, $682m July [OV news]) persist, pushing P/B back to its 5y min of 1.3x [RA]. Probability is cut 5pp per the macro overlay's small bull tilt (research/ALL/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
