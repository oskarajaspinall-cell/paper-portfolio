# Evaluation: Jyske Bank A/S (CPH:JYSK) — 2026-11-15
## Bear case
The re-rating is done. P/E of 13.6x and P/B of 1.2x both sit above their 5y maxima of 9.9x and 1.0x [RA] [Certain], after a 44.8% 12-month gain [ST] [Certain]. The price is 16.1% above its 200-day average with RSI 67.8 [ST] [Certain]: an extended price that de-rates toward its own history if earnings growth slows [Likely]. Returns don't justify the premium: ROE is 9.8% TTM, below 13.6% in FY2023 [RA] [Certain], as the euro-area rate peak fades (macro overlay) [Likely]. The mechanical base fair value of 1,004.83 DKK is below the close, though flagged unreliable [Certain]. Piotroski F is 4 [ST] [Certain]. The fact sheet's FCF Direction change line is lending/deposit flow noise for a bank, not a signal either way [Likely]. Formuepleje acquisition terms are unverified [Likely].

## Bull case
Earnings are compounding: Q3 EPS rose 14% ex value adjustments with Q3 RoTE 11.1%, and Q2 cost/income improved to 47% (transcript headlines [OV]) [Likely]. Buybacks shrank the share count 5.25% YoY [ST] [Certain]. Net margin of 36.3% TTM sits just under its recent band [IS] [Certain]. Against Danish peers it remains cheaper: P/E 28% and P/B 29% below the peer medians [RA, peers] [Certain]. Beta of 0.37 [ST] and a clean uptrend (50-day 10.7% above the 200-day) [ST] [Certain] fit the "business that is working" mandate. AUM growth and the Formuepleje deal add fee income [Likely].

## Decision
```json
{
  "ticker": "CPH:JYSK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds nothing falling over 1y or 3y; ROE is below its FY2023 peak of 13.6% [RA] but the Q3 2026 headline shows EPS up 14% ex value adjustments [OV].", "moat": "none", "key_risk": "medium", "key_risk_text": "De-rating: P/E and P/B already above their 5y maxima [RA] after a 44.8% run [ST]; if EPS growth slows as rates normalise, multiples can revert toward history.", "veto": null},
  "thesis": "A steady Danish bank with buybacks and an uptrend, but sub-10% ROE and multiples above their own history leave no edge for a high-conviction buy.",
  "rationale": "Quality is middling (ROE 9.8% TTM), there is no structural moat and the price already trades above its 5y valuation range; the peer discount and trend are real but not enough. Scorecard conviction is well below the buy bar, so AVOID.",
  "price_at_decision": 1144.00,
  "price_date": "2026-11-13",
  "research_note": "research/CPH-JYSK/2026-11-15.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 8%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "Net (profit) margin TTM falls below 32%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 32}},
    {"text": "Share count change YoY turns positive (buybacks stop / dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1349.14, "basis": "EPS growth and buybacks continue and the price converges on the FCFE DCF base of 1,349.14 DKK [fair value table], narrowing the discount to the peer P/B of 1.7x [peers]."},
    "base": {"probability": 0.5, "target_price_12m": 1144.00, "basis": "P/B holds at 1.2x [RA] as earnings growth offsets some de-rating; above the unreliable mechanical base of 1,004.83 DKK because the peer discount supports the current multiple."},
    "bear": {"probability": 0.25, "target_price_12m": 778.33, "basis": "Rates normalise, ROE drifts down from 9.8% [RA] and multiples revert toward their 5y range, matching the mechanical bear fair value of 778.33 DKK."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE below 10% and no moat keep quality too low for conviction 4 at any price; a sustained ROE recovery, not a lower price, would change the decision.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```
