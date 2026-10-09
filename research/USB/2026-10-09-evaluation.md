# Evaluation: U.S. Bancorp (USB) — 2026-10-09
## Bear case
The price pays a premium for returns USB no longer earns. P/B is 1.5x, at the 87th percentile of its own 5y range (1.2x-1.5x) and 10% above the 1.3x peer median, while ROE has fallen from 14.6% (FY2021) to 12.6% TTM [Certain] [RA]. The mechanical fair value puts base at $51.84 (-9.1%) with bear $39.73 (-30.3%) against bull $61.22 (+7.3%): downside-skewed [Certain]. The macro overlay (primary, tilt toward bear, moderate) notes the 10y at 5.28% is a real-yield move that raises deposit costs and the discount rate together [Likely] (research/USB/2026-10-09-macro.md). Piotroski F-score of 4 flags mediocre quality [Certain] [ST]. Q3 results on Oct 15 add binary NIM risk [Certain] [ST].
## Bull case
On earnings USB is cheap: 11.4x P/E, 18th percentile of its 5y range and 4% below peers [Certain] [RA]. The reverse DCF implies -2.0% year-1 revenue growth, so little growth is priced [Certain]. Net margin and ROE have recovered from the FY2023 trough (21.1%, 10.2%) to 29.9% and 12.6% TTM [Certain] [IS][RA]. Fee franchises in Elavon payments and corporate trust diversify income, and management cited record consumer deposits and robust loan demand at the Barclays conference [Likely] (https://stockanalysis.com/stocks/usb/transcripts/749859-barclays-24th-annual-global-financial-services-conference/). Net buybacks continue (-0.35% shares YoY) [Certain] [ST]. A positive 2s10s slope helps term transformation over time [Likely] (macro overlay).
## Decision
```json
{
  "ticker": "USB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A diversified top-five US bank on a cheap P/E but a top-of-range P/B against compressed ROE, with a rate backdrop that skews the mechanical fair value to the downside.",
  "rationale": "Base fair value $51.84 sits 9.1% below the price and the bull case is only +7.3%, so the reward is asymmetric the wrong way. P/B at its 5y high against falling ROE leaves no cushion, and the primary macro tilt is toward bear. Decent franchise, not compelling at this price: AVOID.",
  "price_at_decision": 57.03,
  "price_date": "2026-10-08",
  "research_note": "research/USB/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 14%, back toward the FY2021 level of 14.6%, showing the post-2023 return compression has reversed and the P/B premium is earned.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 14}},
    {"text": "TTM net margin rises above 32%, recovering most of the 4.6pp five-year compression from 33.3%, evidencing NIM and fee strength despite higher funding costs.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 32}},
    {"text": "Net buybacks accelerate: shares outstanding fall more than 2% YoY (vs -0.35% now), signalling surplus capital beyond regulatory needs.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": -2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 61.22, "basis": "Rates stabilise, NIM holds and P/B stays at its 5y high of 1.5x [RA], matching the fact sheet's bull fair value $61.22; probability cut by 0.05 for the macro overlay's moderate toward-bear tilt (research/USB/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 51.84, "basis": "P/B drifts toward its 1.3x 5y median and peer median [RA] as ROE stays near 12.6% TTM, consistent with the fact sheet's base fair value $51.84 (P/B+ROE 67% / FCFE 33%)."},
    "bear": {"probability": 0.3, "target_price_12m": 39.73, "basis": "Real yields keep rising, deposit costs squeeze NIM and the higher CAPM rate compresses the multiple toward the 1.2x 5y P/B low [RA], the fact sheet's bear fair value $39.73; probability raised by 0.05 per the macro overlay's moderate toward-bear tilt (research/USB/2026-10-09-macro.md)."}
  },
  "entry_price": 41.47,
  "entry_basis": "valuation file: base 51.84 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
