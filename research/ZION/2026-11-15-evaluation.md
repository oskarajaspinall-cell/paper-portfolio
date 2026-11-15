# Evaluation: Zions Bancorporation, National Association (ZION) — 2026-11-15
## Bear case
The cheapness rests on earnings that are not run-rate. TTM ROE of 16.7% is the best in the series, but Q3 growth came from a provision benefit against a charge a year ago, while NIM slipped and the efficiency ratio worsened [company-reported] (https://www.sec.gov/Archives/edgar/data/109380/000010938026000127/zions-20260930.htm) [Certain]. Ex credit benefits, ROE sits in the FY2021-25 band of 12.8-14.7% on a falling five-year trend, and P/B of 1.3x equals its 5y median [Certain]. The fair value is flagged unreliable (methods disagree 4.3x); its FCFE leg uses bank cash flows, so the 56.5% FCF margin and 22.12% FCF yield are not owner earnings [Likely]. Macro tilts small toward bear: real yields and HY spreads rose over 3m on a flat curve, pressuring deposit costs and provisions (macro overlay) [Likely]. The price sits only 3.4% above its 200-day, so trend support is thin if credit normalises [Likely]. Piotroski F is 4 [Certain].

## Bull case
A Western regional bank with a local deposit franchise at 8.1x earnings, below its 5y minimum P/E and below the 11.8x peer median, with P/B under peers [Certain]. Q3 EPS rose 20% year on year to beat (https://www.prnewswire.com/news-releases/zions-bancorporation-national-association-reports-third-quarter-financial-results-302912931.html) [Certain], and 2027 guidance points to stronger NII and fee growth (fact-sheet transcript headline) [Likely]. Capital is returning: shares down 0.57% YoY and a fresh Q4 buyback authorisation [Certain]. The reverse DCF implies -11.5% year-one revenue growth, a low bar [Likely]. The stock is above its 200-day average and up 26.5% over 12 months, beating SPY [Certain]. The P/B + ROE base of 81.88 sits above the 66.34 close even if TTM ROE fades somewhat [Likely]. HY spreads at 3.2% remain low in absolute terms (macro overlay) [Certain].

## Decision
```json
{
  "ticker": "ZION",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A reasonably priced Western regional bank whose discount to history and peers mostly reflects TTM earnings flattered by credit benefits and earlier one-off gains, with core ROE average.",
  "rationale": "Q3 beat came from a provision benefit while NIM and efficiency worsened, so core ROE stays inside its five-year band and P/B is at its 5y median. The fair value is flagged unreliable. Rising real yields and spreads tilt risk slightly bearish. Good but not compelling: AVOID; cash is acceptable.",
  "price_at_decision": 66.34,
  "price_date": "2026-11-13",
  "research_note": "research/ZION/2026-11-15.md",
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: TTM ROE 16.7% and net margin 32.2% [RA,IS] are above FY2025, though partly lifted by a Q3 provision benefit (note section 2).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Credit normalisation: provisions revert from the Q3 benefit as real yields and HY spreads rise (macro overlay), pulling ROE back into the 12.8-14.7% band and compressing P/E and P/B.",
    "veto": null
  },
  "triggers": [
    {"text": "TTM ROE falls below 12%, under the FY2023 low, showing credit or funding costs are breaking the franchise's returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM net margin falls below 25%, under the FY2024 level, as provisions revert.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "Nonperforming assets in the 10-Q rise above 0.75% of loans (note section 4)."},
    {"text": "Shares change YoY turns positive by more than 2%, i.e. dilution to fund losses.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 81.88, "basis": "Core ROE holds near TTM as 2027 NII and fee guidance is met (transcript headline [OV]), so value reaches the P/B + ROE base of 81.88 [IS,BS,RA] as P/B moves toward the 1.4x peer median [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 70.0, "basis": "The provision benefit fades and ROE reverts toward FY2025's 13.5% [RA], P/B stays near its 1.3x 5y median [RA] on modest book growth plus buybacks, below the unreliable mechanical base of 94.19 whose FCFE leg uses bank cash flows (note section 3)."},
    "bear": {"probability": 0.3, "target_price_12m": 56.0, "basis": "Real yields and HY spreads keep widening, provisions revert and P/B falls to its 1.1x 5y low [RA]; probability raised from 0.25 for the overlay's small toward-bear tilt (research/ZION/2026-11-15-macro.md)."}
  },
  "valuation_overrides": [
    {"method": "pb_roe", "scenario": "base", "field": "roe", "value": 0.135, "reason": "TTM ROE of 16.7% [RA] is lifted by a Q3 provision benefit flagged non-recurring (note section 2, sec.gov 10-Q); FY2025 ROE of 13.5% [RA] is the sustainable run-rate."},
    {"method": "pb_roe", "scenario": "bear", "field": "roe", "value": 0.128, "reason": "FY2023 ROE of 12.8% [RA], the five-year low, is the downside if credit normalises under rising real yields and spreads (macro overlay)."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades well below base fair value less the margin of safety, but that value is flagged unreliable and rests on credit-flattered ROE and bank FCFE. Evidence of core ROE sustainably above the FY2021-25 range (NIM and efficiency improving without provision benefits) would change the decision, not a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```
