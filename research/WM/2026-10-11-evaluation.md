# Evaluation: Waste Management, Inc. (WM) — 2026-10-11
## Bear case
The price is not cheap on intrinsic value: the fact sheet's own DCF/EV-EBITDA blend gives base $180.01 and even bull $201.13, both below the $208.83 close, and the reverse DCF needs 10.9% year-1 revenue growth [Certain]. ROIC has been flat for five years (11.6% TTM vs 10.8% FY21), and the ROE rise to 29.8% leans on leverage (net debt/EBITDA 2.93x, peaking at 3.73x in FY24) [Likely]. FCF conversion is volatile and the 5y trend is falling (-30.0pp) [Certain]. Real yields are up 56bp in 3 months and the macro overlay tilts moderately to bear for this long-duration, low-beta multiple [Likely]. A CEO transition is under way [Certain], and Q3 results on 2026-10-27 could reset expectations [Guessing]. Relative strength is poor: -24.9pp vs SPY over 6 months [Certain].

## Bull case
WM controls scarce landfill capacity, a structural pricing moat [Likely]. Margins really are expanding: gross margin +2.4pp and operating margin +2.1pp over five years, to 40.6%/18.9% TTM [Certain]. On multiples it is at the low end of its own history: EV/EBITDA 13.7x and P/FCF 23.4x sit below their 5y minimums, and P/E 29.5x is at the 8th percentile [Certain]. It also trades at a discount to peers (P/FCF -43%, EV/EBITDA -13%) [Certain]. TTM FCF margin of 13.9% is the best in five years, and Healthcare Solutions and recycling drove Q2 growth [Likely]. The EV/EBITDA method alone gives $228.00-$229.10 [Certain]. Beta of 0.43 and fee-based revenue make it a defensive compounder [Likely].

## Decision
```json
{
  "ticker": "WM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality landfill-moat compounder with expanding margins trades cheap against its own and peers' multiples, but its intrinsic value (base fair value $180.01) sits below the price while rising real yields pressure its long-duration multiple.",
  "rationale": "Quality and relative cheapness are real, but ROIC is flat, leverage has risen and the price already exceeds the bull-case DCF blend. The macro overlay tilts moderately to bear on rates. Good but not compelling: conviction 3, no position. Cash is acceptable; re-research at a lower entry price or on clear ROIC improvement.",
  "price_at_decision": 208.83,
  "price_date": "2026-10-09",
  "research_note": "research/WM/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17%, reversing most of the five-year expansion from 16.5% (FY21) to 18.9% and showing pricing power is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 10%, under the FY21 five-year low of 10.8%, showing acquisitions are diluting returns on the landfill/collection base.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 8.5%, under the FY23 five-year low of 8.9%, showing cash generation is structurally impaired rather than lumpy.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8.5}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 3.5x, showing Healthcare Solutions/M&A is funded beyond what the core business supports."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 229, "basis": "EV/EBITDA re-rates from 13.7x (below its 5y min of 14.3x [RA]) toward history, matching the EV/EBITDA fair value of $228.00-$229.10 [IS,RA]; the probability is cut because the macro overlay (research/WM/2026-10-11-macro.md) tilts moderately to bear."},
    "base": {"probability": 0.45, "target_price_12m": 201, "basis": "Margins keep expanding (operating margin 18.9% TTM [IS]) but rates cap the multiple, so the price drifts to the fact sheet's bull blend fair value of $201.13; the DCF weighting is kept rather than the EV/EBITDA-only value because ROIC is flat [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 180, "basis": "Real yields keep rising (macro overlay, moderate bear tilt, research/WM/2026-10-11-macro.md) and the price converges to the base blend fair value of $180.01 [IS,BS,CF,RA]; the $116.23 bear blend is not used because EV/EBITDA is already below its 5y minimum [RA]."}
  },
  "entry_price": 144.01,
  "entry_basis": "valuation file: base 180.01 x 0.8, a 20% margin of safety on base fair value [IS,BS,CF,RA,ST,HI].",
  "replaces": null,
  "replacement_reason": null
}
```
