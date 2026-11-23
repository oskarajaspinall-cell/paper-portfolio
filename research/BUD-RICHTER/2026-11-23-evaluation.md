# Evaluation: Gedeon Richter (BUD:RICHTER) — 2026-11-23
## Bear case
The FCF margin has turned: 26.8% TTM against 29.3% a year earlier, 2.6pp below its 2-year high, even as operating margin rose [Certain]. If that gap is capex or receivables rather than timing, cash conversion is peaking with it [Guessing]. P/E 10.0x and P/B 1.7x already sit in the upper half of their 5y ranges, and the stock is up 37.0% in 12 months and 7.3% above its 200-day average: part of the case rests on trend strength, so a slowdown from the high single-digit 2026 guidance could de-rate it back toward the 5y median P/E of 9.1x [Likely]. Revenue by country is [data unavailable]; CIS/emerging-Europe exposure and HUF translation (Q1 2026 currency headwinds) remain an unsized open item [Likely]. The Q3 2026 release of 2026-11-10 was not read, so the latest quarter's mix is unverified [Certain]. Generic pricing and patent expiries are ongoing [Guessing].
## Bull case
Returns and margins are rising on both views: TTM ROIC 22.2% vs 17.4% a year earlier, operating margin 34.5% vs 28.7%, gross margin 67.8% from 55.4% in FY2021 [Certain]. The FCF dip is from a high base, with conversion still 103.6% of net income, so it reads as timing, not a profit problem [Likely]. Net cash (net debt/EBITDA -0.61x), Altman Z 6.64, beta 0.31 and a flat share count make it a low-risk compounder [Certain]. The price is cheap: FCF yield 10.43%, EV/EBITDA 5.6x at 20% of its 5y range and P/FCF 9.6x at 10%, far below peers, while the reverse DCF implies -6.2% revenue growth in year 1 against guided high single-digit growth [Certain]. Mix shift toward Women's Health, CNS and BioTech explains the margin rise [Likely].
## Decision
```json
{
  "ticker": "BUD:RICHTER",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Only the rolling FCF margin is falling (29.3% -> 26.8%), while operating margin rose 28.7% -> 34.5% and FCF conversion is 103.6% of net income [CF-T, IS-T, IS]: a cash-timing or investment effect, not lost profitability.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Unsized CIS/emerging-Europe and HUF exposure plus generic pricing could slow growth below the high single-digit guidance and de-rate a stock that has run 37.0% in 12 months.", "veto": null},
  "thesis": "A net-cash pharma with rising returns and margins trades low in its own EV/EBITDA and P/FCF ranges while in a healthy uptrend.",
  "rationale": "Thesis intact: ROIC and operating margin at 2-year highs, net cash, FCF yield 10.43%; the rolling FCF dip is timing, not profitability. No new evidence since the 2026-11-18 entry and the position sits close to its target size, so hold rather than add.",
  "price_at_decision": 13290.0,
  "price_date": "2026-11-20",
  "research_note": "research/BUD-RICHTER/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28%, reversing most of the rise from 28.7% a year earlier to 34.5%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 16%, back to the FY2021 level and erasing the returns improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 18%, showing the rolling slide from 29.3% is structural, not timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA (ratios page) rises above 1.0x from -0.61x, signalling a debt-funded deal."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 18416.37, "basis": "Margins hold near 34.5% and the market prices guided growth, reaching the mechanical base fair value of 18,416.37 [IS, valuation]; below the 21,506.87 bull as the bull DCF assumes growth beyond guidance."},
    "base": {"probability": 0.5, "target_price_12m": 14574.46, "basis": "EV/EBITDA moves back toward its 5y median 6.4x on TTM EBITDA, the EV/EBITDA base of 14,574.46 [RA, valuation]; the DCF base is not used as it leans on the DCF's high sensitivity."},
    "bear": {"probability": 0.25, "target_price_12m": 11141.92, "basis": "Growth slows and the trend de-rates, EV/EBITDA bear of 11,141.92 [RA, valuation]; the DCF bear of 5,405.58 assumes a collapse net cash and 22.2% ROIC do not support."}
  },
  "entry_price": null,
  "entry_basis": "Not applicable: the scorecard already gives conviction 4 at today's price [ST, valuation file], so price is not the obstacle; a lower price would not change this HOLD of a position near its target size.",
  "replaces": null,
  "replacement_reason": null
}
```
