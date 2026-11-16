# Evaluation: United Bankshares, Inc. (UBSI) — 2026-11-16
## Bear case
An ordinary bank priced as a good one. ROE is 9.4% TTM and sat between 7.6% and 8.9% for five fiscal years [Certain] [RA], below a 10% quality bar. P/B 1.2x is at 97% of its 5y range and P/FCF at 96%, +33% above peers [Certain] [RA]. The base fair value of 41.95 is below the 48.15 close, though flagged unreliable [Certain]. Valuation points come from trend strength (+31.4% over 12 months, 6.7% above the 200-day) [Certain] [ST]; an extended price risks a de-rating if net interest margin gains stall [Likely]. The macro overlay tilts toward bear: the 2y is up 71bp in about 3 months, the curve is flat and rising real yields hurt CRE values [Likely]. The CRE-led loan book is the risk most likely to break the thesis [Likely]. The 5-year FCF margin decline is normalisation after FY2021-22 working-capital swings; it rose over 12 months (42.1% to 43.7%) [Likely].

## Bull case
Earnings are improving. Net margin rose from 36.9% FY2024 to 40.8% TTM and Q3 net interest margin was above Q2 [Certain] [IS]. FCF/NI has been above 100% for five years, the share count is down 1.12% YoY and a new buyback was authorised [Certain] [ST]. The balance sheet is defensive: beta 0.74, risk-based capital described as solid, credit spreads calm at 3.20% [Likely]. Relative strength is strong (+21.1pp vs SPY over 12 months) with RSI 51.9, so the trend is not stretched [Certain] [HI]. Piedmont is absorbed and the Florida de novo adds low-risk organic growth [Likely]. If the curve re-steepens, ROE could drift above 9.4% and a P/B at the top of its range could hold [Guessing].

## Decision
```json
{
  "ticker": "UBSI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Neither ROE nor FCF margin is falling over 1 or 3 years: ROE 9.4% TTM vs 8.9% FY2025 [RA]; FCF margin 42.1% to 43.7% over 12 months and +5.4pp over 3 years [CF-T]. The 5-year FCF fall reflects inflated FY2021-22 working-capital swings.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "CRE credit deterioration as rates rise (2y +0.71pp over ~3m per macro overlay), combined with a de-rating from a P/B at 97% of its 5y range if margin gains stall.",
    "veto": null
  },
  "thesis": "A steady, buyback-supported regional bank whose sub-10% ROE and full own-history multiples leave the case resting on price trend rather than a quality franchise.",
  "rationale": "ROE of 9.4% is below the quality bar and moat evidence is thin; valuation is full (P/B at 97% of its 5y range, P/FCF above peers) and the macro overlay tilts toward bear. Trend strength alone does not make it high conviction. Good but not compelling: AVOID.",
  "price_at_decision": 48.15,
  "price_date": "2026-11-13",
  "research_note": "research/UBSI/2026-11-16.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 7.5%, below the FY2024 low: earnings power eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7.5}},
    {"text": "Net (profit) margin TTM falls below 35%, reversing the margin gains.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}},
    {"text": "Shares outstanding grow more than 3% YoY (dilutive M&A or capital raise).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "Company reports a material rise in CRE non-performing loans or charge-offs in a 10-Q/earnings release (text trigger)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 52.0, "basis": "Curve re-steepens, NIM keeps rising (3.86% Q3 vs 3.81% Q2 [OV news]) and ROE drifts above 9.4% [RA], so P/B holds at the top of its 5y range on a growing book; above the mechanical bull 43.71 because that P/B+ROE model ignores the margin uptrend."},
    "base": {"probability": 0.5, "target_price_12m": 47.0, "basis": "ROE holds near 9.4% [RA] and P/E stays near its 5y median 13.6x [RA]; buybacks offset a mild multiple drift, above the unreliable base fair value 41.95 whose methods disagree 2.5x."},
    "bear": {"probability": 0.3, "target_price_12m": 35.0, "basis": "Macro overlay bear (tilt toward bear, small, raising this probability): hikes and wider spreads hit CRE credit, P/B falls from 97% of its 5y range toward its 1.0x median [RA], matching the mechanical bear fair value 35.00."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: ROE of 9.4% sits below the quality bar and moat evidence is thin, so a lower price alone would not make this conviction 4; it would need ROE sustainably above the bar.",
  "replaces": null,
  "replacement_reason": null
}
```
