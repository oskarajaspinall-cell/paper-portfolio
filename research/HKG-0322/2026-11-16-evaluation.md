# Evaluation: Tingyi (Cayman Islands) Holding Corp. (HKG:0322) — 2026-11-16
## Bear case
Returns sit at a peak: ROIC 35.6% TTM vs 16.7% FY2021 and net margin only 5.9%, so an input-cost swing (palm oil, wheat, PET) moves earnings hard [Likely]. Earnings multiples look cheap on peak margins; P/B 5.2x is above its 5y max [Certain]. ROCE fell from 31.0% to 28.8% over the last 12 months while ROIC and margins rose; that points to a larger capital base, not lost pricing, so it does not threaten the thesis yet [Likely]. The reverse DCF implies -0.8% revenue growth: the market already expects a flat top line in a mature China category [Certain]. Base fair value 15.08 is only modestly above the price; the bear value 6.39 is far below [Certain]. The price is 11.6% above its 200-day average with RSI 76.3; an extended price risks a de-rating if the 23 Nov results show margin gains fading [Likely]. China-only exposure; PBOC and policy unverified (macro overlay) [Certain].

## Bull case
A dominant noodle and beverage brand with scale distribution has lifted gross margin from 30.4% to 35.4% and operating margin from 5.5% to 8.4% over five years, with the last 12 months still rising [Certain]. Cash is real: FCF conversion 124.2%, FCF yield 8.61%, net cash and no dilution [Certain]. P/E 14.4x is at the 9th percentile of its 5y range and below peers' 18.2x; EV/EBITDA 6.6x is below its 5y minimum [Certain]. DCF and P/E methods agree near 15, and the price only needs a flat top line [Likely]. The stock is in a healthy uptrend (+14.8% over 12 months, beating SPY) with very low beta 0.14, a defensive compounder [Likely]. CNY is stable, so no translation shock (macro overlay) [Certain].

## Decision
```json
{
  "ticker": "HKG:0322",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds ROIC, operating margin and FCF margin all rising over the last year (ROIC 23.0% -> 35.6%, operating margin 7.4% -> 8.4%, FCF margin 5.9% -> 7.3% [RA-T, IS-T, CF-T]); only ROCE dipped (31.0% -> 28.8%), consistent with a larger capital base rather than margin loss.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Margins at a five-year high partly reflect benign input costs; a palm oil/wheat/PET reversal would cut thin-net-margin earnings and, with the price above its 200-day average, trigger a de-rating.", "veto": null},
  "thesis": "A net-cash, high-return Chinese noodle and beverage staple with rising margins and an 8.61% FCF yield trades low in its own P/E range, but on peak margins with modest upside to base fair value.",
  "rationale": "Quality and cash conversion are strong and the multiples sit low in their own range, but margins are near a peak driven partly by input costs, upside to base fair value is modest against a deep bear value, and the scorecard does not reach the buy bar. Cash is an acceptable outcome.",
  "price_at_decision": 13.63,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-0322/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, giving up most of the rise from 22.3% (FY2025) to 35.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 6.5%, under the FY2024 level of 6.9%, showing input costs have reversed the margin gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6.5}},
    {"text": "TTM FCF margin falls below 4%, back toward FY2023 levels, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, balance sheet / ratios page) rises above 1.0x from -0.23x TTM, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 16.28, "basis": "Mechanical bull fair value, P/E method 18.79 near the peer median 18.2x [RA, peers], as margins hold at the TTM 8.4% operating level [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 15.08, "basis": "Mechanical base fair value where DCF 15.02 and P/E 15.18 agree on a flat top line, matching the reverse DCF's -0.8% implied growth [fact sheet fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 10.5, "basis": "Input costs reverse and operating margin drifts back toward the FY2024 6.9% [IS] while P/E de-rates toward its 5y min 13.3x [RA]; less severe than the DCF bear 3.13 because net cash and FCF conversion 124.2% support the floor [CF, BS]."}
  },
  "entry_price": 12.06,
  "entry_basis": "valuation file: base 15.08 x 0.8, a margin of safety that would compensate for the peak-margin risk.",
  "replaces": null,
  "replacement_reason": null
}
```
