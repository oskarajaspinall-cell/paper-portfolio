# Evaluation: Remitly Global (RELY) — 2026-11-17

## Bear case
Remitly has been profitable only since FY2025 (ROIC -11.6% in FY2024, 45.5% TTM [RA]), so there is no through-cycle evidence that today's 13.0% operating margin [IS] holds [Certain]. Remittance pricing is contested by Wise, Western Union and banks; the moat is modest and a fee war would compress take rates [Likely]. The early FY2027 view points to slower, high-teens growth with spending on new products, and the stock fell from 28.00 to 21.93 after results with no news, consistent with a de-rating on deceleration [Guessing]. EV/EBITDA of 14.6x is well above peers (n=2) [RA], and the fair value rests on EV/Revenue alone (DCF unavailable), so its reliability is low [Likely]. Net margin of 19.1% above operating margin flatters P/E [Guessing]. Share count still rises 2.75% YoY despite buybacks [ST]. The AUSTRAC AML matter is unquantified `[company-reported]` [Certain]. Bear value 15.83 [IS,RA] if margins revert.

## Bull case
Q3 2026 was a record: revenue up 22%, raised FY2026 guidance and a buyback authorization raised to $500M [Likely] (https://www.globenewswire.com/news-release/2026/11/04/3395827/0/en/remitly-reports-record-third-quarter-results-and-raises-full-year-2026-outlook.html). Every rolling metric is rising with no direction-change flag: operating margin +10.8pp and FCF margin +9.6pp over the last year [IS-T,CF-T] [Certain]. Net cash (net debt/EBITDA -2.45x) and Altman Z 7.69 remove balance-sheet risk [Certain]. At P/FCF 11.1x, 3% of its own 5y range, and an 8.98% FCF yield [RA,ST], the price discounts a fade the guidance does not show [Likely]. The price sits above its 200-day average (21.11) after a 65.1% twelve-month gain, so the trend is intact despite the pullback [Certain]. Base fair value 31.39 is well above the price [IS,BS,CF,RA,ST]. Macro is context only (68.4% US-sent revenue, research/RELY/2026-11-17-macro.md) [Certain].

## Decision
```json
{
 "ticker": "RELY",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "ROIC, operating margin and FCF margin are all rising over 1 and 3 years on the rolling table [RA-T, IS-T, CF-T].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Price competition from Wise, Western Union and banks compresses take rates as growth slows toward high-teens, reversing a margin step-up with only two years of profit history; the extended twelve-month run leaves room for a de-rating.",
  "veto": null
 },
 "new_evidence": {
  "type": "method_change",
  "text": "The 2026-11-15 AVOID at conviction 3 predates the 2026-11-17 scorecard change (strength_at_value_points: 2 trend points become 3 when the value blend is at or above the price); the same evidence now scores 9."
 },
 "thesis": "A net-cash, newly profitable digital remitter with sharply rising margins and an 8.98% FCF yield trades at the bottom of its own P/FCF range, pricing a fade its raised guidance does not show.",
 "rationale": "Scorecard gives conviction 4: high, rising returns, net cash, and both discount and trend points. Python sets the volatility-scaled core size; cash cannot fund a full position above the 1.5% floor, so the conviction-3 HRB holding is sold to fund it.",
 "price_at_decision": 21.93,
 "price_date": "2026-11-16",
 "research_note": "research/RELY/2026-11-17.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 8%, reversing most of the step-up from 2.2% a year earlier to 13.0%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 8
   }
  },
  {
   "text": "TTM ROIC falls below 20%, showing the returns step-up was not durable.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 20
   }
  },
  {
   "text": "TTM FCF margin falls below 12%, back near the 11.1% of a year earlier.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 12
   }
  },
  {
   "text": "A regulatory outcome (AUSTRAC or US remittance rules) restricts a major corridor or imposes a material penalty, disclosed in a filing."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 33.95,
   "basis": "Margins keep rising on raised guidance and EV/Sales re-rates toward the mechanical bull value 33.95 [IS,BS,CF,RA,ST]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 28.0,
   "basis": "High-teens growth and a stable 13.0% operating margin [IS] lift the price back to its 52-week high 28.00 [HI], below base fair value 31.39 because that value rests on EV/Revenue alone with no DCF."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 15.83,
   "basis": "Take-rate competition reverses the margin step-up and EV/Sales falls toward its 5y low 1.5x [RA], matching the mechanical bear value 15.83."
  }
 },
 "replaces": "HRB",
 "replacement_reason": "HRB is held at conviction 3 with its remaining upside mostly shareholder yield after a re-rating (its own thesis); RELY clears the buy bar at conviction 4 with rising margins and a discount, and current cash cannot fund a full position above the 1.5% floor.",
 "second_opinion": {
  "file": "research/RELY/2026-11-17-evaluation-2.md",
  "conviction": 4
 }
}
```
