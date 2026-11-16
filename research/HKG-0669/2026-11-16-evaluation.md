# Evaluation: Techtronic Industries (HKG:0669) — 2026-11-16
## Bear case
The price has run ahead of every valuation anchor: the close of 141.80 HKD sits above the mechanical base (103.07) and even the bull fair value (113.80), and the reverse DCF needs 14.7% year-1 revenue growth, demanding next to the 4.4% FY2025 revenue growth [Likely]. P/E of 25.3x is a premium to peers' 19.1x [Certain]. After a +56.7% year, a stock 14.4% above its 200-day average with beta 1.75 risks a de-rating if growth slows; results are due Nov 18 [Certain], so a soft print would hit an extended multiple [Likely]. The macro overlay flags rising real yields and spreads against high-multiple, high-beta names (tilt toward bear, small) [Likely]. Operating margin is flat at 9.1% versus 8.9% in FY2021, so gross-margin gains are not reaching profit [Certain]. ROIC is still below FY2021's 21.0% on the 5-year view [Certain]. Region mix is unverified [Certain].
## Bull case
A good business that is working: TTM ROIC rose from 17.2% to 19.1% in the last 12 months, reversing the post-FY2021 trough, so the 5-year decline reflects a peak-to-trough cycle now recovering [Likely]. Gross margin climbed from 38.8% to 42.6%, consistent with pricing power and Milwaukee mix [Likely]. Cash conversion is excellent (FCF/NI 149.8%, FCF margin 12.5%) and the balance sheet moved from 1.31x net debt/EBITDA to net cash [Certain]. Piotroski 8, Altman Z 4.81 [Certain]. H1 2026 was a record half with a raised FCF target [Likely]. Own-history multiples are mid-range or low (EV/EBITDA at the 28% position, P/FCF at 24%), the FCF yield is 5.93%, and the trend is strong without being severely overextended [Certain]. Insiders own 22.24% [Certain].
## Decision
```json
{
 "ticker": "HKG:0669",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Nothing is falling over the last 1 or 3 years: TTM ROIC rose from 17.2% to 19.1% [RA-T], operating and FCF margin are flat [IS-T, CF-T]; the 5-year ROIC fall from 21.0% (FY2021) to a 14.0% FY2023 trough [RA] has since recovered, with net cash and gross margin up to 42.6% [IS].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "The price rests on trend, not value (above base and bull fair value, reverse DCF needs 14.7% growth): a growth slowdown at the Nov 18 results or rising real yields could de-rate a beta-1.75, 25.3x P/E stock.",
  "veto": null
 },
 "thesis": "A high-return, net-cash cordless-tool franchise with recovering ROIC and rising gross margin is in a strong uptrend, but the price already sits above even its bull fair value and implies growth well ahead of recent results.",
 "rationale": "Quality, cash conversion and balance sheet are excellent and the trend is healthy, but the price is above every mechanical fair value and requires 14.7% growth with results imminent and macro tilting against high-beta multiples. Good but not compelling at this price: AVOID, with an entry price where valuation support returns.",
 "price_at_decision": 141.80,
 "price_date": "2026-11-13",
 "research_note": "research/HKG-0669/2026-11-16.md",
 "triggers": [
  {"text": "TTM gross margin falls below 40%, reversing the pricing-and-mix gain (42.6% now).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
  {"text": "TTM ROIC falls below 15%, back toward the FY2023 trough of 14.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
  {"text": "TTM FCF margin falls below 8%, showing cash conversion was working-capital release rather than durable.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
  {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) rises above 1.0x from -0.32x, ending the net-cash position through debt-funded M&A or buybacks."}
 ],
 "scenarios": {
  "bull": {"probability": 0.25, "target_price_12m": 165, "basis": "Results confirm the H1 2026 record trend [OV transcript] and P/E holds near the current 25.3x [RA] on growing earnings, as the reverse DCF's 14.7% growth [fact sheet fair value] is met."},
  "base": {"probability": 0.45, "target_price_12m": 135, "basis": "Growth continues but the multiple drifts toward its 5y median EV/EBITDA of 16.5x [RA], between the EV/EBITDA method base of 123.60 and today's price; above the DCF base because the DCF ignores the recovered ROIC and net cash [RA, BS]."},
  "bear": {"probability": 0.30, "target_price_12m": 100, "basis": "P/E de-rates toward its 5y low of 17.6x [RA], close to the blended base fair value of 103.07; probability raised for the macro overlay's small tilt toward bear on real yields and spreads (research/HKG-0669/2026-11-16-macro.md)."}
 },
 "entry_price": 82.46,
 "entry_basis": "valuation file: base 103.07 x 0.8 (20% margin of safety) [ST]; price is the obstacle, the business case is intact.",
 "replaces": null,
 "replacement_reason": null
}
```
