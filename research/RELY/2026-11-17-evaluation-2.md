# Evaluation: Remitly Global (RELY) — 2026-11-17
## Bear case
Profitability is young: ROIC turned positive only in FY2025 [Certain], so the TTM 45.5% ROIC and 13.0% operating margin have never been tested through a price war with Wise, Western Union and banks [Likely]. Net margin of 19.1% above operating margin suggests a non-operating or tax lift in TTM earnings, flattering the 12.4x P/E [Guessing]. The early FY2027 view points to slower, high-teens growth while new products absorb investment [Likely], and the stock fell from 28.00 on results day to 21.93 with no news: the market is de-rating the growth path, not the quarter [Guessing]. The mechanical fair value rests on EV/Revenue alone (DCF unavailable), so its +43.2% base is low reliability; the bear value 15.83 shows the downside if margins revert [Likely]. Shares still grew 2.75% YoY despite buybacks [Certain], and the AUSTRAC AML matter has no estimable loss `[company-reported]` [Likely].

## Bull case
Remitly is a turnaround that has crossed into strong, cash-backed profitability: operating margin rose to 13.0% from 2.2% a year earlier and FCF margin to 20.8% from 11.1%, with FCF conversion of 108.5% [Certain]. Q3 2026 was a record quarter with send volume up 25%, revenue up 22% and raised FY2026 guidance (globenewswire release in the fact sheet) [Likely]. The balance sheet is net cash (net debt/EBITDA -2.45x, Altman Z 7.69) [Certain], and the buyback authorization was raised to $500M [Likely]. Yet P/FCF of 11.1x sits at 3% of its own 5y range and the FCF yield is 8.98% [Certain]: the price assumes the margin step-up is a peak, while guidance still implies high-teens growth with 50 bps of further margin expansion [Likely]. The post-results fall to 21.93 looks like profit-taking after a 65.1% twelve-month gain rather than a broken thesis [Guessing]; the price remains above its 200-day average.

## Decision
```json
{
  "ticker": "RELY",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 1 and 3 years [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Price competition from Wise, Western Union and banks compresses take rates before the young margin structure is proven, alongside the unresolved AUSTRAC AML matter.",
    "veto": null
  },
  "thesis": "A net-cash, newly profitable digital remittance leader with a 20.8% FCF margin and still-growing volume trades at the bottom of its own P/FCF range, pricing a margin peak that raised guidance does not show.",
  "rationale": "Quality and direction are strong and verified on rolling figures, the balance sheet is net cash, and P/FCF near its own 5y low gives a real discount. Short profit history and competition keep conviction at 4, not 5; Python sizes the position.",
  "price_at_decision": 21.93,
  "price_date": "2026-11-16",
  "research_note": "research/RELY/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8%, reversing most of the step-up from 2.2% a year earlier to 13.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 20%, showing the turnaround returns are fading.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 12%, back near the 11.1% of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "A regulatory outcome (AUSTRAC or US remittance rules) restricting a major corridor is disclosed in a filing or company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.95, "basis": "Margins hold and growth meets the high-teens FY2027 view, so EV/Sales re-rates toward the mechanical bull value 33.95 [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 28.0, "basis": "FY2026 guidance is delivered and the post-results sell-off reverses to the 28.00 results-day high [HI], below the mechanical base 31.39 because that EV/Revenue-only value is low reliability."},
    "bear": {"probability": 0.25, "target_price_12m": 15.83, "basis": "Competition compresses take rates and margins revert, taking EV/Sales to the mechanical bear value 15.83 [IS,RA]."}
  },
  "new_evidence": {"type": "method_change", "text": "The 2026-11-15 AVOID 3 was scored under an earlier scorecard rule set; re-scored under the current rules it lands on the other side of the buy line. The business evidence itself is unchanged."},
  "replaces": null,
  "replacement_reason": null
}
```
