# Evaluation: Kyowa Kirin Co., Ltd. (TYO:4151) — 2026-11-08
## Bear case
Cheap for a reason. Over five fiscal years ROIC fell from 17.9% (FY2023) to 12.0% TTM, and operating margin sits 3.7pp below its 2-year high of 21.7% [RA, IS-T] [Certain]. The last year's rebound (ROIC 8.1% -> 12.0%, FCF margin 7.5% -> 13.8%) comes off a trough. It does not prove a return to the FY2023 level, and FCF margin has swung between 8.3% and 22.7% across fiscal years [CF] [Certain]. Patent and biologic exclusivity erodes at expiry, and the discount to peers may simply price a patent cliff [Guessing]. US drug-pricing deals are a sector-wide risk to overseas revenue. The note could not confirm the revenue mix by country [Guessing]. The Q3 2026 results came out on 2 November and remain unread [Likely]. Base fair value 2,605.76 is only +7.4% above the price, so the margin of safety is thin [Certain].
## Bull case
On its own history the stock is at a trough multiple. P/E is 14.8x, below the 5y minimum of 15.7x, and P/B is 1.4x, also below its minimum. EV/EBITDA is 8.1x against a 5y median of 8.9x [RA] [Certain]. It trades 22% below peers on P/E [RA] [Certain]. The price implies only 3.2% year-1 revenue growth [Certain]. The balance sheet holds net cash (net debt/EBITDA -1.91x), with Altman Z 6.03 and Piotroski 7 [ST] [Certain]. Gross margin is steady at 74.7% TTM [IS] [Certain]. The last 12 months show returns and cash conversion recovering, not deteriorating [RA-T, CF-T] [Certain]. The bull fair value of 4,521.38 gives positive skew if margins return toward FY2023 [Likely]. With a beta of 0.16 it is defensive ballast [Certain].
## Decision
```json
{
  "ticker": "TYO:4151",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash specialty pharma at the bottom of its own valuation range, with recovering returns, whose base fair value offers too little margin of safety to offset patent-erosion risk and unverified latest results.",
  "rationale": "Cheap on history and peers, and the balance sheet is strong. But the base fair value is barely above the price, returns are still well below the 2-year highs, the regional mix and the Q3 results are unverified, and the discount may reflect patent exposure. Good but not compelling: AVOID, and watch the entry price.",
  "price_at_decision": 2427.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-4151/2026-11-08.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 9%, showing the recovery has reversed", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Gross margin (TTM) falls below 70%, signalling lost pricing power or patent erosion", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 70}},
    {"text": "Operating margin (TTM) falls below 15%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "FCF margin (TTM) falls below 8%, back to its trough", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3665.98, "basis": "Margins recover toward the FY2023 peak of 21.7% and EV/EBITDA re-rates toward its history, matching the EV/EBITDA bull value [IS, RA]; it sits below the DCF-led blended bull of 4,521.38 because the bull DCF growth is not evidenced."},
    "base": {"probability": 0.5, "target_price_12m": 2605.76, "basis": "Returns hold at about 12.0% ROIC TTM and EV/EBITDA drifts toward its 5y median of 8.9x, in line with the blended base fair value [RA, fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 1915.41, "basis": "Patent erosion or US pricing pressure pushes the FCF margin back toward the 7.5% of a year earlier, in line with the blended bear fair value [CF-T, fact sheet Fair value]."}
  },
  "entry_price": 2084.61,
  "entry_basis": "valuation file: base 2,605.76 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
