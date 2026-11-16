# Evaluation: Engie Brasil Energia S.A. (BVMF:EGIE3) — 2026-11-16
## Bear case
The fall to the entry level is not an overreaction; returns are eroding while leverage climbs. ROCE slid from 17.1% (FY2021) to 10.8% TTM, 2.4pp under its 2-year high [Certain]. Net debt/EBITDA rose from 3.15x to 4.14x despite a mid-2026 equity raise that lifted shares 5.01% YoY [Certain]. Q3 2026 showed only modest earnings growth, so new capital is not yet earning its keep [Likely]. The mechanical base fair value of 23.72 BRL is below the 26.25 close and the bull value roughly equals the price: the price already discounts the good outcome [Certain]. P/B fell because the raise expanded equity, and ROE is flattered by leverage [Likely]. The FCF margin is lumpy (FY2024 -23.1%) and 4.0pp off its 2-year high; heavy transmission and battery capex can swing it negative again [Likely]. Selic at 13.75% keeps refinancing costly [Certain].

## Bull case
Contracted, long-dated BRL cash flows with a 0.36 beta give a utility-like floor [Likely]. FCF margin of 22.1% TTM against -0.1% a year earlier and an 8.53% FCF yield show the capex cycle is starting to convert to cash [Certain]. P/FCF of 11.7x and P/B of 1.7x sit below their 5-year minimums and P/E is near the bottom of its range [Certain]. Q3 adjusted EBITDA still grew, the Jirau acquisition and liability prepayment should lift profitability, and management keeps a 55% payout policy with a stated leverage focus [Likely]. The ROCE decline is plausibly temporary: dilution and not-yet-earning assets inflate the denominator rather than signal lost share [Likely]. Selic is easing slowly, a mild tailwind for a levered, rate-sensitive name [Likely]. On the EV/EBITDA method the bull value is well above the price [Certain].

## Decision
```json
{
  "ticker": "BVMF:EGIE3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "The scorecard finds none of its tracked metrics (ROE for this name, FCF margin) falling over 1 or 3 years; the ROCE slide to 10.8% TTM is addressed in the bear case and reflects a 5.01% share issuance and new assets entering the base before earning (https://stockanalysis.com/quote/bvmf/EGIE3/transcripts/669525-q3-2026/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Debt-funded capex keeps earning below the cost of capital at a high Selic, so ROCE keeps falling and net debt/EBITDA (4.14x) climbs further, forcing more dilution.",
    "veto": null
  },
  "thesis": "A contracted Brazilian power producer that is cheap on its own book and cash-flow history, but whose returns are eroding and leverage rising while the price already sits near the mechanical bull value.",
  "rationale": "The fall to the entry level follows a dilutive raise and modest Q3 growth, not a break in the business, but it is no bargain: price sits above base fair value, leverage scores zero on the balance sheet and ROCE is falling. Scorecard conviction 2, so AVOID with no position.",
  "price_at_decision": 26.25,
  "price_date": "2026-11-13",
  "research_note": "research/BVMF-EGIE3/2026-11-16.md",
  "triggers": [
    {"text": "ROCE (ratios page, TTM) falls below 9%, showing new assets are not earning their cost of capital."},
    {"text": "Net debt/EBITDA (site definition, statistics page) rises above 4.5x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "TTM FCF margin falls below 10%, showing the cash conversion was capex timing reversing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Shares outstanding grow more than 10% year on year, a further dilutive raise.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 31.11, "basis": "New assets lift EBITDA and EV/EBITDA moves to the upper part of its 5y range, matching the EV/EBITDA bull value of 31.11 [RA,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 25.67, "basis": "EV/EBITDA stays near its 5y median of 7.6x on TTM EBITDA (EV/EBITDA base 25.67) [RA,IS]; above the DCF base of 22.74 because FY2024's negative FCF depresses the DCF inputs."},
    "bear": {"probability": 0.25, "target_price_12m": 22.63, "basis": "Leverage keeps rising and the multiple sits at the EV/EBITDA bear value of 22.63 [RA,BS]; the negative DCF bear is an artefact of the FY2024 FCF margin of -23.1% [CF] and is not used."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
