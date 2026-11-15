# Evaluation: ASML Holding N.V. (AMS:ASML) — 2026-11-15
## Bear case
The price already discounts an exceptional cycle: the reverse DCF needs 35.4% year-1 revenue growth and the close of 1,338.80 EUR sits above even the mechanical bull value of 1,100.30 [Certain]. Returns and cash are at peaks: ROIC 92.1% vs 59.9% a year earlier, FCF margin 53.6% vs 27.8%, FCF conversion 157.1%, likely flattered by customer prepayments that reverse in a capex slowdown (the FY2023 FCF margin was 11.9%) [Likely]. The **Direction change** (FCF margin falling over 5 fiscal years, rising over 12 months) is a working-capital swing, not a structural break, but it means P/FCF 24.2x overstates cheapness [Likely]. The trend has broken: 4.3% below the 200-day, -16.8% over 3 months [Certain]. Real yields rose 0.47pp in ~3m, pressuring a 38.3x P/E (macro overlay) [Certain]. China export-control exposure is unquantified [Guessing].

## Bull case
ASML is the sole EUV supplier, a wide moat that no competitor replicates, so returns persist through the cycle [Likely]. Every rolling metric is at its 2-year high: operating margin 38.6% (+3.7pp), ROCE 44.7%, gross margin 54.3% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.67x), Piotroski F 8, and the share count fell 1.34% [Certain]. Headlines report a Q3 beat and raised 2026 guidance on AI demand [Likely]. On its own history P/E (27% of range) and EV/EBITDA (17%) are in the lower part of the 5-year range, and the 50-day remains 5.5% above the 200-day, so the pullback may be a pause in a working business [Likely]. The mechanical fair value, built on a through-cycle history including the FY2023 trough, may understate a structurally higher demand base [Guessing].

## Decision
```json
{
  "ticker": "AMS:ASML",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC, operating margin and FCF margin are all rising on the rolling table [RA-T, IS-T, CF-T]; the 5-year FCF-margin fall is the FY2023 working-capital trough.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "A slowdown in AI-driven chipmaker capex reverses prepayments and compresses peak margins and the 38.3x P/E together, with China export controls an unquantified add-on.",
    "veto": null
  },
  "thesis": "A wide-moat, net-cash EUV monopolist at peak returns whose price already sits above the mechanical bull value and below its 200-day average, so neither a discount nor trend strength supports a buy.",
  "rationale": "Business quality is exceptional and improving, but the price needs 35.4% year-1 growth, sits above every mechanical fair value and has lost its uptrend, while real yields pressure the multiple. Good but not compelling: AVOID at conviction 3; re-research on a lower price or a restored uptrend.",
  "price_at_decision": 1338.80,
  "price_date": "2026-11-13",
  "research_note": "research/AMS-ASML/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 33% (38.6% now), showing the AI-capex cycle is rolling over into the margins.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 33}},
    {"text": "TTM ROIC falls below 60% (92.1% now), back to the FY2021 level.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "TTM gross margin falls below 50% (54.3% now), under the FY2022 five-year low of 50.5%, signalling pricing or mix pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "A new export-control rule restricting EUV/DUV sales or servicing to China, confirmed by an official or company source."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1700, "basis": "Raised 2026 guidance and AI demand (nasdaq.com headline in the note) keep margins at their 2-year highs [IS-T] and the P/E re-rates toward its 5y max of 48.8x [RA], retesting the 1,741.00 52-week high [HI]; above the mechanical bull because the through-cycle DCF ignores the EUV moat."},
    "base": {"probability": 0.42, "target_price_12m": 1300, "basis": "Earnings keep growing but the P/E drifts to its 5y median of 35.7x [RA], leaving the price near today's level; above the mechanical base of 581.45 because the model's through-cycle history includes the FY2023 cash trough."},
    "bear": {"probability": 0.33, "target_price_12m": 900, "basis": "Capex slowdown reverses the FCF spike (FY2023 FCF margin 11.9% [CF,IS]) and rising real yields compress the multiple below its 5y low of 34.3x [RA], toward the 822.20 52-week low [HI]; probability raised a small amount for the macro overlay's bear tilt (research/AMS-ASML/2026-11-15-macro.md)."}
  },
  "entry_price": 465.16,
  "entry_basis": "valuation file: base 581.45 x 0.8. The other path to conviction 4 is trend strength (close back above the 200-day average of 1,399.01 [ST,HI]), which a re-research would test.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```
