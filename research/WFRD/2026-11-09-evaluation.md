# Evaluation: Weatherford International plc (WFRD) — 2026-11-09
## Bear case
Weatherford's returns came from a cyclical upswing and restructuring, not a moat: ROIC was 4.8% in FY2021 [Certain]. The cycle is now turning against it. Revenue fell 6% over nine months on Middle East disruption, weaker North America and higher SG&A [company-reported], ROCE dropped from 21.4% to 16.9% and operating margin from 15.5% to 13.2% in a year, and ROIC sits 10.0pp below its 2-year high [Certain]. This is a fall in activity, not a one-off, and the 2027 growth outlook assumes the Middle East stays flat [Likely]. EV/EBITDA of 7.3x is above its own 5y maximum, and the EV/EBITDA method gives only 72.60, below the price [Certain]. Russia rose to 9% of revenue [company-reported], with sanctions and ruble status unverified [Guessing]. The redomestication's tax effects are unquantified [Certain]. Altman Z of 2.55 and Piotroski F of 5 are middling [Certain].

## Bull case
The balance sheet is the strongest it has been: net debt/EBITDA is 0.52x and the 8.625% notes are being redeemed [Certain]. Cash is improving even as margins soften: FCF margin rose from 7.7% to 12.3%, a 2-year high, conversion is 143.0% of net income, and the FCF yield is 9.46% [Certain]. Q3 beat and management raised cash-conversion guidance [Likely]. The stock trades at a discount to peers on every earnings multiple (P/E 15.0x vs 20.0x, P/FCF 10.6x vs 16.5x) [Certain], and the reverse DCF implies -6.9% revenue growth, so a downturn is already priced [Likely]. The base fair value is 117.55 [Certain]. Equinor and Eni contract wins help diversify away from the Middle East [Likely], and shares are falling 1.30% a year [Certain]. ROIC at 24.6% is still high in absolute terms [Certain].

## Decision
```json
{
  "ticker": "WFRD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROCE and operating margin fall with a 6% nine-month revenue decline driven by Middle East disruption, weaker North America and higher SG&A [company-reported, 10-Q https://www.sec.gov/Archives/edgar/data/1603923/000160392326000122/wfrd-20260930.htm]; a cyclical activity trough with net debt/EBITDA at 0.52x and FCF margin at a 2-year high of 12.3%, not lost share or a broken model.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "A deeper or longer fall in international E&P spending (Middle East, plus Russia sanctions on 9% of revenue) pushes margins and ROIC back toward the pre-2023 levels, since there is no durable pricing power.",
    "veto": null
  },
  "thesis": "A deleveraged oilfield-services company with a 9.46% FCF yield trades below peers and prices a revenue decline, but its returns are cyclical, falling over the last year and without a moat, so the skew is good but not compelling.",
  "rationale": "Cheap on cash flow with a clean balance sheet, but margins and ROCE are falling with activity, EV/EBITDA is above its own 5y maximum and the earnings-based method sits below the price. Without a moat, the scorecard gives conviction 3: below the buy bar, so no position.",
  "price_at_decision": 84.43,
  "price_date": "2026-11-06",
  "research_note": "research/WFRD/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 11% (13.2% now), showing the activity downturn is compressing profitability beyond a cyclical dip.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 8% (12.3% now), showing the cash-conversion improvement was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 18% (24.6% now), a reversion toward pre-2023 returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.52x now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 144.33, "basis": "Middle East activity stabilises and the 2027 growth outlook holds, so the stock reaches the mechanical bull fair value of 144.33 [IS,BS,CF,RA] while FCF margin stays at its 12.3% high [CF-T]."},
    "base": {"probability": 0.45, "target_price_12m": 100.0, "basis": "FCF holds and the peer discount narrows partly, but margins stay off their highs; set below the mechanical base 117.55 because the DCF leans on near-peak cash flow and the EV/EBITDA method gives only 72.60 [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 67.48, "basis": "Revenue keeps falling with Middle East and North America activity [10-Q], operating margin slides further from 13.2% [IS-T] and the multiple compresses to the mechanical bear fair value of 67.48."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the base fair value less 20% (117.55 x 0.8) is already above the price. The obstacle is the falling margin and ROCE direction and the lack of a moat in a cyclical business, so a lower price alone would not change the decision; a stabilising operating margin would.",
  "replaces": null,
  "replacement_reason": null
}
```
