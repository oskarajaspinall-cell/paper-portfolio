# Evaluation: Intuit Inc. (INTU) — 2026-11-23
## Bear case
The market is not doubting past results; it is doubting the franchise's next five years. Management cut next-year revenue guidance with the 19 November results and the stock fell about 10% the next session [Likely]. Senior product leaders at TurboTax and QuickBooks have left [Likely], and the new 10-Q adds risk language on free and low-cost rivals, government free filing and AI-enabled fraud [Certain]. If AI agents become the "front door" for tax filing and credit discovery, TurboTax and Credit Karma lose pricing power and the 80.6% gross margin is the first casualty [Guessing]. Mean-reversion on multiples is no comfort when a 60.1x median was set in a different regime; P/E at 15.4x can fall further on a falling knife (RSI 26.8, 22.1% below the 200-day) [Certain]. The base fair value is flagged unreliable, so the apparent discount is weak evidence [Certain].
## Bull case
Every quality metric is at its high on a rolling basis: ROIC 22.7%, operating margin 29.8%, FCF margin 41.3%, all up over the last year [Certain]. Nothing in delivered results shows the AI erosion the price assumes: the reverse DCF implies revenue shrinking 5.8% in year 1 [Certain]. At a 12.68% FCF yield, P/FCF 7.9x and P/E below its 5y minimum and 36% under peers, the price already discounts serious damage [Certain]. Net debt/EBITDA is 0.33x and shares fell 3.10% YoY; selling the struggling Mailchimp for about $3.68 billion [company-reported] and using proceeds for buybacks at this price is accretive [Likely]. QuickBooks' data and switching costs are not easily replaced by a chatbot [Likely].
## Decision
```json
{
  "ticker": "INTU",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no falling ROIC, operating margin or FCF margin; all are at 2-year highs on a rolling basis [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "AI agents and free filing erode TurboTax/Credit Karma pricing and volumes; the cut revenue guidance and executive exits make it live, but delivered margins and FCF do not yet show it.",
    "veto": null
  },
  "thesis": "A low-debt financial-software franchise with ROIC, operating and FCF margins at their 2-year highs trades below its own 5-year minimum multiples at a 12.68% FCF yield, pricing a revenue decline its results do not show.",
  "rationale": "Fundamentals are at their best, yet the price implies shrinkage; the guidance cut and AI-disintermediation risk are real but not yet visible in margins or cash. The scorecard sets the conviction; the position keeps its size, with no ADD while the guidance cut is unexplained by a primary source.",
  "price_at_decision": 270.44,
  "price_date": "2026-11-20",
  "research_note": "research/INTU/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 16%, giving up most of the rise from 18.7% a year earlier to 22.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 30%, back near the FY2024 level of 28.8%, meaning the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 78%, under the FY2023 five-year low of 79.3%, signalling free or AI-native rivals are forcing price cuts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "Consumer segment revenue (10-Q) declines year on year for two consecutive reported periods, showing free filing and AI eroding the TurboTax base."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 425, "basis": "Results keep contradicting the AI fear and P/E re-rates toward the 24.2x peer median [RA, P:ADBE, P:CRM, P:ADSK, P:WDAY]; still below the unreliable DCF base 495.55 [IS,CF]."},
    "base": {"probability": 0.45, "target_price_12m": 330, "basis": "Margins hold near 29.8% operating [IS-T] and P/E recovers only to its 5y minimum 18.9x [RA], well short of the mechanical base, which is flagged unreliable."},
    "bear": {"probability": 0.30, "target_price_12m": 229, "basis": "The guidance cut proves the start of AI-led erosion and the price settles near the DCF bear value 229.21 [IS,BS,CF], below the 52-week low 252.84 [HI]."}
  },
  "entry_price": 229.21,
  "entry_basis": "Valuation file: DCF bear value 229.21 [IS,BS,CF,RA,ST]. The mechanical base is flagged unreliable, so the default base x 0.85 is not used; at the bear value the price would discount the bear scenario itself.",
  "replaces": null,
  "replacement_reason": null
}
```
