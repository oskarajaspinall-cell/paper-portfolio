# Evaluation: Dollar General Corporation (DG) — 2026-10-12
## Bear case
This is a one-quarter recovery being priced as a turnaround. ROIC has fallen from 12.9% (FY2022) to 8.1% TTM and operating margin from 9.4% to 5.7% [RA, IS] [Certain]. The Q2 FY2026 operating-profit jump comes off the FY2025 trough of 4.8%, so it proves little yet [Likely]. Net debt/EBITDA of 3.96x is still above the FY2022 3.60x, and Altman Z of 2.59 sits in the grey zone [RA, ST] [Certain]; that leverage is why the mechanical bear fair value is only 27.23 [Certain]. The macro overlay is a moderate tilt toward bear: a 10y Treasury at 5.22% raises the discount rate and refinancing cost, and inflation squeezes the low-income core shopper that management itself flagged (research/DG/2026-10-12-macro.md) [Likely]. Base fair value is only +15.3% above the price, so there is little margin of safety for a business whose returns are still well below where they were [Certain].
## Bull case
DG is cheap against its own history and its peers: EV/EBITDA 11.8x sits at the 12th percentile of its 5y range and 13% below peers, P/FCF 14.0x at the 4th percentile, and the FCF yield is 7.16% [RA, ST] [Certain]. Cash generation is recovering faster than earnings, with FCF conversion at 118% TTM against a 17.5% trough [CF, IS] [Certain]. Q2 FY2026 delivered same-store sales of +3.5%, operating profit +29.2% and a raised full-year outlook (investor.dollargeneral.com) [Certain]. Leverage is falling, from 5.64x to 3.96x [RA] [Certain]. The reverse DCF implies just 1.8% year-1 growth, a low bar for a rural-moat retailer that is also gaining higher-income trade-down shoppers [Likely]. If margins keep normalising, the P/E could re-rate toward its 19.7x median [RA] [Guessing].
## Decision
```json
{
  "ticker": "DG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rural small-box discount leader trading near the bottom of its own 5-year multiple range is starting a margin and leverage recovery, but one quarter of evidence, 3.96x leverage and only +15.3% to base fair value do not yet give a compelling margin of safety.",
  "rationale": "Valuation is undemanding and cash conversion is improving, but returns are still falling over five years, leverage is elevated and the recovery rests on one quarter. Rate and consumer pressure (macro tilt moderate toward bear) widen the downside. This is good but not compelling, so we take no position and wait for the entry price or a second quarter of proof.",
  "price_at_decision": 127.23,
  "price_date": "2026-10-09",
  "research_note": "research/DG/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2025 trough of 4.8%, showing the margin recovery has stalled.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 4.8}},
    {"text": "TTM ROIC falls below the FY2025 trough of 6.3%, showing returns have resumed their multi-year decline.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6.3}},
    {"text": "Net debt/EBITDA (ratios page) rises back above the FY2025 peak of 5.64x, meaning deleveraging has reversed."},
    {"text": "Same-store sales growth turns negative in a quarterly release (investor.dollargeneral.com), proving the Q2 FY2026 +3.5% inflection was a one-off."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 160.78, "basis": "The margin recovery holds and the P/E re-rates toward its 5y median of 19.7x [RA], in line with the P/E bull fair value of 160.78 [fact sheet]. This is set below the blended bull of 196.36 because the macro overlay's moderate tilt toward bear caps how far the discount rate can ease (research/DG/2026-10-12-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 144.01, "basis": "Steady normalisation with FCF conversion of 118% TTM [CF, IS] supports the DCF base fair value of 144.01 [fact sheet]. This is slightly below the blended base of 146.67 to reflect the overlay's rising 10y yield (research/DG/2026-10-12-macro.md)."},
    "bear": {"probability": 0.3, "target_price_12m": 106.96, "basis": "The inflation-squeezed core shopper stalls the one-quarter recovery and the multiple stays near its 5y low, matching the P/E bear fair value of 106.96 [fact sheet]. This is above the blended bear of 27.23, whose negative DCF bear is a leverage artefact rather than a realistic 12-month price. The probability is raised by the overlay's moderate tilt toward bear (research/DG/2026-10-12-macro.md)."}
  },
  "entry_price": 117.34,
  "entry_basis": "Valuation file: base 146.67 x 0.8 = 117.34, the 20% margin of safety that would justify conviction 4 on the same evidence; this is near the recent swing lows of about 117.3 [HI].",
  "replaces": null,
  "replacement_reason": null
}
```
