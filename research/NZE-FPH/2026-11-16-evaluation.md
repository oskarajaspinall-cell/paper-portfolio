# Evaluation: Fisher & Paykel Healthcare Corporation Limited (NZE:FPH) — 2026-11-16
## Bear case
The price already assumes perfection. P/E 61.3x is +37% above the peer median, EV/EBITDA 35.8x sits at 85% of its 5y range, and EV/Sales 12.2x and P/B 13.5x are above their 5y maxima [Certain]. The reverse DCF implies 46.6% year-1 revenue growth [Certain], which is not a credible hurdle [Likely]. The stock is +18.7% above its 200-day average after +49.7% in 6 months [Certain]: an extended price risks a de-rating if growth slows, with no earnings miss needed [Likely]. Results land Nov 25, 2026, a near-term gap risk [Certain]. The macro overlay tilts small toward bear: real yields up 0.47pp in ~3m and a 1.72% FCF yield leave the multiple exposed (research/NZE-FPH/2026-11-16-macro.md) [Likely]. FCF margin fell 2.3pp over the last 12 months to 21.2% [Certain], probably capex for manufacturing expansion [Guessing]. FY2023-24 showed ROIC can halve in a downturn [Certain].

## Bull case
A high-quality, working business. TTM ROIC 26.2%, ROCE 27.0%, gross margin 63.7% and operating margin 27.6%, all at or near 2-year highs and up on a year earlier [Certain]. The 5-year "falling" ROIC and operating-margin labels reflect a FY2023-24 trough (ROIC 10.9%) fully recovered, not erosion [Likely]. Net cash (net debt/EBITDA -0.41x), Altman Z 20.22, Piotroski 7, dilution 0.14% [Certain]. FCF conversion 104.7% of net income [Certain]. Recurring consumables on an installed base give a narrow moat [Likely]. P/E is only 32% up its own 5y range and P/FCF at 6% [Certain], so on its own history the earnings multiple is not extreme [Likely]. Relative strength vs SPY is +18.5pp over 12 months [Certain]; the AGM cited revenue and profit up significantly and higher dividends (https://stockanalysis.com/quote/nze/FPH/transcripts/680720-agm-2026/) [Likely].

## Decision
```json
{
  "ticker": "NZE:FPH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin fell over 5 fiscal years only because FY2022 was a peak and FY2023-24 a trough (ROIC 10.9%); TTM ROIC is up 4.8pp and operating margin up 2.4pp on a year earlier [RA-T, IS-T]. The 2.3pp FCF-margin dip coincides with manufacturing-expansion investment cited at the AGM (https://stockanalysis.com/quote/nze/FPH/transcripts/680720-agm-2026/).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "De-rating: at 61.3x P/E with EV/Sales and P/B above their 5y maxima and the reverse DCF implying 46.6% year-1 growth, any growth slowdown (Nov 25 results) or further real-yield rise compresses the multiple without an earnings miss.",
    "veto": null
  },
  "thesis": "Excellent, recovering respiratory-care franchise with net cash and 26% ROIC, but priced for growth far above anything its history supports.",
  "rationale": "Quality and direction are strong and the decline was a cyclical trough now reversed, but the valuation is stretched on peers and on EV/Sales and P/B history, the trend is extended ahead of Nov 25 results, and macro tilts toward bear. Good but not compelling at this price: AVOID.",
  "price_at_decision": 48.48,
  "price_date": "2026-11-13",
  "research_note": "research/NZE-FPH/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 18%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Operating margin (TTM) falls below 23%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "Gross margin falls below 59%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 59}},
    {"text": "Debt/EBITDA rises above 1.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 56.0, "basis": "Nov 25 results extend the margin and ROIC recovery [IS-T, RA-T] and P/E holds near today's 61.3x [RA] on higher earnings."},
    "base": {"probability": 0.45, "target_price_12m": 45.0, "basis": "Earnings grow but P/E drifts toward its 5y median 52.1x [RA], partly offset by growth; macro overlay's small bear tilt on real yields (research/NZE-FPH/2026-11-16-macro.md) keeps the multiple capped."},
    "bear": {"probability": 0.30, "target_price_12m": 29.57, "basis": "Growth slows and the multiple de-rates to the P/E-method bear fair value 29.57 [fact sheet fair value], consistent with the overlay's 10-15% macro compression plus an earnings reset; probability raised for the overlay's bear tilt (research/NZE-FPH/2026-11-16-macro.md)."}
  },
  "entry_price": 33.06,
  "entry_basis": "The blended base (21.52) is flagged unreliable (methods disagree 3.6x), so the anchor is the P/E-method base fair value: 41.33 x 0.8 [fact sheet fair value], with P/E then near its 5y low of 37.3x [RA].",
  "replaces": null,
  "replacement_reason": null
}
```
