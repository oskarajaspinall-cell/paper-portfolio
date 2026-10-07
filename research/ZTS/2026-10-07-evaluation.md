# Evaluation: Zoetis Inc. (ZTS) — 2026-10-07
## Bear case
This is a franchise being competed away, not a cyclical dip. US dermatology in-clinic share fell 10pp YoY to ~86% as entrants discounted and bundled [Certain]; management cut FY2026 to organic revenue -3% to -1% and adjusted net income down 9%-5% [Certain]. Q2 livestock strength was partly transitory screwworm demand [Likely]. A trailing 11.6x P/E is a value trap if the earnings base keeps resetting [Guessing]. ROE of 64.9% is leverage-flattered, with net debt/EBITDA up from 1.03x to 1.86x funding buybacks into a falling share price [Certain]. Momentum is broken (-50.6% over 12 months, 26.9% below the 200-day MA) and put flow is bearish into the 5 Nov print [Certain]; another cut there could push the multiple lower still [Guessing].

## Bull case
Even after the cut, this is a 71.7% gross margin, 38.1% operating margin, 27.3% ROIC business converting 87.8% of net income to FCF [Certain]. At 71.33 it trades on 11.6x P/E, 9.1x EV/EBITDA and a 7.86% FCF yield, 25-28% below its own 5-year minimum multiples and 36-68% below peer medians [Certain]. The guided earnings decline is single-digit; the de-rating is roughly 50%, so the price discounts permanent erosion well beyond the evidence [Likely]. Margins, FCF conversion and Altman Z 5.87 show no operational distress [Certain]. Shares are shrinking 4.22% YoY, compounding per-share value at trough prices [Certain]. Livestock and international are growing, and the pipeline (CKD, oncology) plus Simparica Trio's peer-reviewed heartworm data give US companion animal a route to stabilise [Likely].

## Decision
```json
{
  "ticker": "ZTS",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A 27% ROIC, 38% operating-margin animal-health franchise trades below its own 5-year minimum multiples at a 7.86% FCF yield, pricing permanent erosion far larger than the single-digit guided earnings decline.",
  "rationale": "Quality metrics remain intact while valuation sits 25-28% below its 5-year minimums and far below peers; the guided earnings cut is modest relative to the de-rating. Competitive share loss caps conviction at 4, not 5: 7% core size. Ample cash, one holding, Healthcare exposure stays well inside the 30% cap.",
  "price_at_decision": 71.33,
  "price_date": "2026-10-06",
  "research_note": "research/ZTS/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below the FY2022 5-year low of 69.7%, signalling structural loss of pricing power rather than cyclical volume softness.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 69.7}},
    {"text": "TTM operating margin falls below the FY2023 5-year low of 35.9%, showing competition is eroding profitability, not just growth.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35.9}},
    {"text": "US companion-animal in-clinic share (dermatology), as reported on the earnings call, declines again in a second consecutive quarter beyond the -10pp YoY already seen."},
    {"text": "Management cuts FY2026 adjusted net income guidance below the low end of the current 9%-5% decline range on the Q3 2026 call or later."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 115, "basis": "Dermatology share stabilises and EV/EBITDA re-rates from 9.1x toward the 14.3x peer median [RA, P:IDXX/ELAN/MRK/PAHC] on TTM EBITDA [IS], still below the 14.9x 5-year minimum."},
    "base": {"probability": 0.5, "target_price_12m": 83, "basis": "Earnings land within the guided 9%-5% decline (Q2 2026 call transcript) and EV/Sales closes its 13% discount to the 4.5x peer median [RA, peers], with 4.22% YoY buybacks [ST] supporting per-share value."},
    "bear": {"probability": 0.3, "target_price_12m": 58, "basis": "Share loss deepens past the -10pp YoY dermatology decline (Q2 2026 call transcript) so earnings fall about twice the guided 9% while P/E stays near 11.6x [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
