# Evaluation: Swissquote Group Holding SA (SWX:SQN) — 2026-11-08
## Bear case
Returns are falling on every view. ROIC fell from 32.3% in FY2021 to 18.0% TTM, and in the last 12 months it fell from 20.7%, now 5.9pp below its 2-year high [Certain]. Operating margin reads "rising" over five fiscal years, but it fell from 49.4% to 46.3% over the last year [Certain]. The Direction change lines come from slowing revenue, the core thesis risk: H1 2026 net revenue rose only 1.7%, and 2026 guidance was cut from CHF 760m revenue and CHF 385m pre-tax profit to CHF 730m and CHF 365m (transcripts, [OV]) [Likely]. Rate-sensitive interest income and cyclical retail trading are rolling over [Likely]. The FCF margin falling from 296.6% to 159.6% only reflects client-deposit flows and says nothing about quality [Likely]. The mechanical FCFE base of CHF 41.49 capitalises that deposit cash. The P/E method's base of CHF 25.09 sits below the price [Certain]. Piotroski F-score is 4 [Certain].

## Bull case
This is a high-return franchise: ROE 28.0% and operating margin 46.3% TTM, with net margin up to 47.0% [Certain]. Client assets rose 19.8% to CHF 96.3bn on CHF 5.1bn net new money in H1 2026, and 2028 targets were maintained (H1 transcript, [OV]) [Likely]. That asset base drives future revenue once trading volumes recover. The VIX at 28.18 may help (macro overlay) [Guessing]. The stock is -29.0% over 12 months. P/E of 14.1x sits at the 20th percentile of its 5y range and below the peer median of 14.6x [Certain]. The reverse DCF implies only 4.2% year-1 revenue growth [Certain]. Insiders own 22.56% and the share count is stable [Certain]. If margins stabilise, a re-rating toward the 5y median P/E of 15.4x or higher is plausible [Likely].

## Decision
```json
{
  "ticker": "SWX:SQN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROE Swiss online broker trades near the low end of its own P/E range, but returns and margins are falling on a rolling basis and 2026 guidance was cut, so the skew is only modestly positive.",
  "rationale": "Quality is high but deteriorating: ROIC and operating margin are falling over the last year and guidance was lowered. The FCFE fair value is inflated by deposit flows, and the P/E value sits below the price. Expected value is close to the price. This is good but not compelling, so it stays below the buy bar.",
  "price_at_decision": 33.80,
  "price_date": "2026-11-06",
  "research_note": "research/SWX-SQN/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 49.4% (its level a year earlier), showing revenue growth and operating leverage have resumed.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 49.4}},
    {"text": "TTM ROIC recovers above 20.7% (a year earlier), reversing the rolling decline in returns.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 20.7}},
    {"text": "TTM ROE falls below 22%, which would confirm structural erosion and end any case for buying even at a lower price.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 22}},
    {"text": "The H2 2026 results (due Mar 18, 2027) meet or beat the CHF 730m revenue and CHF 365m pre-tax profit guidance and keep the 2028 targets."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Client-asset growth to CHF 96.3bn (H1 transcript [OV]) turns into revenue growth again and P/E re-rates from 14.1x to between its 5y median of 15.4x and max of 19.9x [RA]; this is below the mechanical bull of 67.08 because that FCFE figure capitalises deposit-driven FCF."},
    "base": {"probability": 0.5, "target_price_12m": 35.0, "basis": "The lowered 2026 guidance is met and the margin settles near the TTM 46.3% [IS-T], with P/E holding around its current 14.1x [RA]; this is below the mechanical base of 41.49 because the FCFE method rests on a 159.6% FCF margin that reflects client deposits, while the P/E method gives 25.09."},
    "bear": {"probability": 0.25, "target_price_12m": 26.0, "basis": "ROIC and operating margin keep falling from their 2-year highs [RA-T, IS-T] as rate and trading income fade, and P/E slips to its 5y low of 12.7x [RA] on lower earnings; this is in line with the mechanical bear of 25.98."}
  },
  "entry_price": 30.4,
  "entry_basis": "P/E back at its 5y low of 12.7x [RA] on current earnings. The default (base fair value 41.49 x 0.8) is not used because the FCFE base is inflated by deposit flows; at the bottom of its own range a 28.0% ROE business would justify conviction 4 if returns stabilise.",
  "replaces": null,
  "replacement_reason": null
}
```
