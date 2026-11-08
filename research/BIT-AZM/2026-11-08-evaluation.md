# Evaluation: Azimut Holding S.p.A. (BIT:AZM) — 2026-11-08
## Bear case
The stock is no longer cheap against itself: P/E 9.9x and EV/EBITDA 7.1x both sit above their 5-year maxima of 9.7x and 6.8x [RA] [Certain]. The rolling year shows the real problem. Operating margin fell from 48.4% to 43.0% and ROIC from 37.0% to 32.5% [IS-T, RA-T] [Certain], so the 5-year "rising margin" reading is stale. The likely driver is lower performance fees or a mix shift toward lower-margin business, which the note could not confirm [Guessing]. Fees are market-sensitive, and the VIX is up sharply (macro overlay) [Likely]. The TTM FCF jump (FCF margin from -10.0% to 50.4%) is working-capital timing after negative years in FY2022 and FY2024 [CF] [Likely], and it inflates the DCF. Q3 results due Nov 5, 2026 are not in the research [Likely]. The bear value of 30.31 is further below the price than the base is above it [Certain].
## Bull case
Azimut has net cash (net debt/EBITDA -0.31x [RA]), almost no dilution (shares change YoY 0.06% [ST]) and ROIC still above 30% [Certain]. Management reported record net inflows and growth in recurring profit, and set out a capital-return plan (Q4 2025 transcript) [Likely]. Against Italian financial peers it trades at a discount on P/E and P/B [ST] [Certain], although those peers are imperfect comparisons. The reverse DCF prices -4.2% year-1 revenue growth [fact sheet Fair value], which looks harsh for a franchise taking in record flows [Likely]. If the drop in performance fees is cyclical and recurring fees keep compounding, margins could recover toward the 2-year high and the bull value of 51.85 is reachable [Guessing]. The FCF yield of 15.56% points to large capital returns, even if it overstates the run-rate [Likely].
## Decision
```json
{
  "ticker": "BIT:AZM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-ROIC Italian asset manager with strong inflows, but its multiples are above their own 5-year range while the rolling-year operating margin and ROIC are falling, so the price leaves only modest upside against a larger bear downside.",
  "rationale": "The quality is real, but multiples are above their 5-year maxima, the last year shows operating margin and ROIC falling, the TTM FCF that lifts the DCF is lumpy, and Q3 results are not yet in the research. The upside to base value is modest and smaller than the bear downside. Good but not compelling: AVOID.",
  "price_at_decision": 35.82,
  "price_date": "2026-11-06",
  "research_note": "research/BIT-AZM/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 48% (43.0% now, 48.4% a year earlier), showing the year-on-year compression was a temporary performance-fee dip, not structural mix erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 48}},
    {"text": "TTM ROIC rises back above 37%, its 2-year high, showing returns have resumed compounding.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 37}},
    {"text": "TTM ROIC falls below 28% or net debt/EBITDA on the ratios page rises above 0.5x, confirming deterioration and removing any case to buy.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 51.85, "basis": "Record inflows (Q4 2025 transcript) carry recurring fees higher, operating margin recovers toward its 49.2% 2-year high [IS-T], and the stock reaches the mechanical bull fair value of 51.85 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 36.5, "basis": "Margins hold near the TTM 43.0% [IS-T]; set below the mechanical base of 38.65 because its DCF leg capitalises a TTM FCF margin of 50.4% that followed -14.4% in FY2024 [CF], while the P/E method gives only 25.92 [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 30.31, "basis": "Falling markets and lower performance fees extend the drop in operating margin from 48.4% to 43.0% [IS-T], and P/E falls back from 9.9x toward its 5y median of 7.2x [RA], in line with the mechanical bear fair value of 30.31 [fact sheet Fair value]."}
  },
  "entry_price": 30.92,
  "entry_basis": "valuation file: base 38.65 x 0.8; at that level the margin of safety would offset the falling rolling-year margin and the lumpy FCF.",
  "replaces": null,
  "replacement_reason": null
}
```
