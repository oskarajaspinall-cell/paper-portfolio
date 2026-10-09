# Evaluation: Huntington Bancshares Incorporated (HBAN) — 2026-10-09
## Bear case
Returns are mediocre and slipping: ROE eased to 9.0% TTM from 10.1% in FY25, below any sensible cost of equity with a 5.28% risk-free rate [Certain] [RA]. Shares outstanding rose 18.32% YoY, diluting per-share value [Certain] [ST]. Piotroski F-score is 4, a weak health read [Certain] [ST]. On Sept 16 management cut its 2027 EPS outlook, citing persistent NIM pressure and competition, which points to a scale deposit franchise without pricing power [Likely] (transcript [OV]). Since then the Fed has hiked and the 2y has risen, so funding costs are probably running worse than the cut guidance assumed (macro overlay, primary weight) [Likely]. FCF conversion fell from 170.4% (FY22) to 111.9% TTM [Certain] [CF,IS]. The base fair value of 16.20 is only +5.4% above the price, with the bear case at -23.9% [Certain]. Q3 results on Oct 22 could bring another reset [Guessing].

## Bull case
The stock looks cheap. P/E of 12.0x sits at the 25th percentile of its 5y range and 6% below peers, and P/B of 1.0x is 18% below the 1.3x peer median [Certain] [RA, peers]. The reverse DCF implies -1.8% revenue growth, which is pessimistic for a bank that just raised its prime rate [Likely] [OV]. The FCF yield is 8.64% [Certain] [ST]. Management is stepping up buybacks and reports strong organic growth and integration progress [Likely] (transcript [OV]). If the Fed pauses and the curve steepens, NIM could bottom and the stock could re-rate toward peer P/B, roughly the bull fair value of 19.31 (+25.6%) [Guessing]. Short interest of 2.61% is low, so crowding risk is small [Certain] [ST].

## Decision
```json
{
  "ticker": "HBAN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A regional bank on cheap headline multiples but with a 9% ROE, 18% share dilution and a guidance cut on NIM pressure that the latest rate moves make worse, so the cheapness is not a margin of safety.",
  "rationale": "The base fair value is only +5.4% above the price against -23.9% in the bear case. ROE is falling and below the cost of equity, the F-score is 4 and dilution is heavy. The primary-weight macro overlay tilts moderately toward the bear case. Good-but-not-compelling at best, so AVOID; cash is fine.",
  "price_at_decision": 15.37,
  "price_date": "2026-10-08",
  "research_note": "research/HBAN/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 12%, back to the FY2022 high, showing NIM pressure has passed and returns clear the cost of equity.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12}},
    {"text": "TTM net margin rises above 30%, back toward the FY2022 32.2% level, showing funding-cost pressure has eased.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 30}},
    {"text": "Q3 2026 or later results (SEC 8-K) show NIM stabilising and management reaffirms or raises its 2027 EPS outlook instead of cutting it again."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 19.31, "basis": "NIM troughs and P/B re-rates toward the 1.3x peer median, in line with the fact sheet's bull fair value of 19.31 [IS,BS,CF,RA,ST,HI]; probability cut from the default per the macro overlay's moderate bear tilt (research/HBAN/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 16.2, "basis": "ROE holds around 9-10% [RA] and P/B stays near its 1.1x 5y median, matching the base fair value of 16.20 (P/B+ROE 67% / FCFE 33% blend)."},
    "bear": {"probability": 0.35, "target_price_12m": 11.69, "basis": "Funding costs outpace asset yields after the Fed hike and the rise in the 2y, forcing another NIM/EPS cut (research/HBAN/2026-10-09-macro.md, moderate bear tilt raises this probability); the bear fair value is 11.69 [IS,BS,CF,RA,ST,HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
