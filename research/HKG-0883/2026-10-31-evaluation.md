# Evaluation: CNOOC Limited (HKG:0883) — 2026-10-31
## Bear case
Earnings sit on spike-level oil: Brent was $123.10 on 2026-10-27 after a war-driven peak of $135.51, and a de-escalation that sends it back toward $70-90 would cut revenue and margin sharply (macro overlay) [Likely]. The stock is not cheap against its own history. P/E 7.2x, EV/EBITDA 2.8x and P/FCF 8.6x sit at 82-90% of their 5-year ranges, and P/B 1.2x is above the 5-year max [RA] [Certain]. Mechanical base fair value is 21.36 HKD, below the 24.70 close, with bear 15.73 [valuation] [Certain]. The peer discount reflects a persistent state-owned and China discount, so it is no catalyst [Likely]. Other risks: the Lingshui 17-2 accident, a corruption probe at the former parent chairman level, and CNY/country risk [Likely]. Reserve NAV, the best method for this industry, is [data unavailable].

## Bull case
This is a low-cost, net-cash producer. TTM ROIC is 23.9%, operating margin 43.7%, net debt/EBITDA -0.98x and Piotroski F 7 [RA, ST] [Certain]. FCF conversion recovered to 87.2% TTM and the FCF yield is 11.58% [CF, ST] [Certain]. Q3 brought record production and higher profit (transcript headline [OV]) [Likely]. Beijing's push for domestic output supports volume [Likely]. Versus peers it trades at a 55% P/E discount and a 57% EV/EBITDA discount [Certain]. The stock is already 15.9% below its price six months ago while Brent stayed near $120, so some oil mean reversion may be priced in (macro overlay) [Guessing]. Beta is 0.34 [ST] [Certain].

## Decision
```json
{
  "ticker": "HKG:0883",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 23.9%-ROIC offshore producer is high quality, but its earnings rest on spike-level Brent, and the price sits above mechanical base fair value with multiples near the top of their own 5-year ranges.",
  "rationale": "Quality and cash generation are excellent, but this is near-peak, oil-driven earnings bought at 82-90% of the own-history multiple range, above base fair value. The macro overlay tilts moderately to the bear side. The skew does not justify conviction 4. Cash is acceptable; we revisit at a lower price.",
  "price_at_decision": 24.70,
  "price_date": "2026-10-30",
  "research_note": "research/HKG-0883/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 35%, under every fiscal year in the five-year range (low 37.9%), showing the low-cost advantage or realised prices have eroded.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "TTM ROIC falls below 15%, under the FY2021 five-year low of 15.1%, showing returns have broken below the cycle floor.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Shares change YoY rises above +2%, showing dilution replacing the current slight share shrinkage.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}},
    {"text": "Net debt/EBITDA on the ratios page rises above 0.3x (-0.98x TTM now), meaning the net cash position is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 26.09, "basis": "Brent holds above $110 (macro overlay), so margins and the 11.58% FCF yield [ST] hold and EV/EBITDA stays near the top of its range, matching the mechanical bull fair value of 26.09 [valuation]."},
    "base": {"probability": 0.45, "target_price_12m": 21.36, "basis": "Oil eases partly and EV/EBITDA drifts from 2.8x back toward its 5-year median of 2.1x [RA], giving the mechanical base fair value of 21.36 [valuation]."},
    "bear": {"probability": 0.35, "target_price_12m": 15.73, "basis": "Brent reverts toward $70-90 and the multiple compresses from a near-peak base, giving the mechanical bear fair value of 15.73 [valuation]; probability raised for the macro overlay's moderate tilt toward bear (research/HKG-0883/2026-10-31-macro.md)."}
  },
  "entry_price": 17.09,
  "entry_basis": "valuation file: base 21.36 x 0.8; at that price the same oil-cyclical evidence would carry enough margin of safety for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
