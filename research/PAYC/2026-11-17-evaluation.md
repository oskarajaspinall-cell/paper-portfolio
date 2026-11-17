# Evaluation: Paycom Software, Inc. (PAYC) — 2026-11-17
## Bear case
The price has already re-rated: up 83.0% in six months and 49.7% above the 200-day average, just under the overextended line, with base fair value only +2.1% above the close [Certain]. An extended price is exposed to a de-rating if growth slows; the reverse DCF already asks for 10.2% year-1 revenue growth [Certain]. Part of the margin step-up (operating margin 33.9% vs 27.9% a year earlier) comes from lower headcount, not growth, and may not repeat [Likely]. Fiscal-year ROIC was flat over five years, so the TTM jump is one year of evidence [Certain]. Buybacks (shares -12.61% YoY) are now revolver-funded, with $750.0 million [company-reported] drawn, moving net debt / EBITDA from -0.44x to 0.75x [Certain]. Rising real yields are a multiple headwind (macro overlay, context only) [Likely]. Piotroski F of 5 is middling [Certain].

## Bull case
A high-quality payroll franchise that is working: TTM ROIC 39.3%, operating margin 33.9%, FCF margin 30.1% and gross margin 88.4%, all at their 2-year highs and rising over 1 and 3 years on the rolling table [Certain]. Q3 results came with higher FY26 guidance [Likely]. Despite the run, the stock is cheap against its own history and peers: P/E 23.9x at 4% of its 5y range, EV/EBITDA 14.1x at 1% and 30% below peers, P/FCF 16.9x below its 5y minimum, FCF yield 5.91% [Certain]. Payroll is embedded in client workflows and the single-database design is hard to copy, supporting switching costs [Likely]. Leverage stays modest and the share count is shrinking fast, compounding per-share value [Certain]. Relative strength vs SPY is +39.1pp over 12 months [Certain].

## Decision
```json
{
 "ticker": "PAYC",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds ROIC, operating margin and FCF margin all rising over 1 and 3 years (RA-T, IS-T, CF-T); nothing is falling.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "De-rating of an extended price (49.7% above the 200-day average) if the partly cost-driven margin step-up fades and growth slows below the 10.2% the reverse DCF implies.",
  "veto": null
 },
 "new_evidence": {
  "type": "method_change",
  "text": "The 2026-11-15 AVOID at conviction 3 came before the 2026-11-17 scorecard rule (strength_at_value_points): two trend-strength points now count as three when the value blend is at or above the price, as it is here. The evidence itself is unchanged."
 },
 "thesis": "A high-return, cash-generative payroll software franchise whose margins are stepping up while trading low in its own multiple history and in a healthy uptrend.",
 "rationale": "The scorecard gives conviction 4: top quality, rising returns, modest leverage and trend strength with the value blend above the price. Python sets the volatility-scaled size. Cash above the 1.5% floor can't fund it, so conviction-3 JKHY is sold to pay for it.",
 "price_at_decision": 254.75,
 "price_date": "2026-11-16",
 "research_note": "research/PAYC/2026-11-17.md",
 "triggers": [
  {
   "text": "Operating margin (TTM) falls below 27%, giving up the step-up from 27.9% a year earlier.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 27
   }
  },
  {
   "text": "ROIC (TTM) falls below 30%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 30
   }
  },
  {
   "text": "FCF margin (TTM) falls below 20%.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 20
   }
  },
  {
   "text": "Net debt / EBITDA rises above 2.0x as debt-funded buybacks overreach.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 2.0
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 354.14,
   "basis": "Margins hold and the multiple recovers toward its 5y median EV/EBITDA 22.8x [RA]; anchored on the DCF bull 354.14 rather than the blended 422.60, which leans on an EV/Revenue multiple well above today's."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 260.07,
   "basis": "Mechanical base fair value 260.07 (DCF 67% + EV/Revenue 33%) with TTM margins sustained and growth near the reverse-DCF 10.2% [IS,CF,RA]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 170.86,
   "basis": "Cost-driven margin gains fade and the extended price de-rates; EV/Revenue bear 170.86 [RA], above the DCF bear 64.91, which assumes a collapse the rising quality trend does not support."
  }
 },
 "replaces": "JKHY",
 "replacement_reason": "JKHY is held at conviction 3, and its own thesis says the price now implies growth above the company's framework. PAYC clears the buy bar with higher, rising returns and multiples low in its own range. Selling JKHY also frees Technology sector room for PAYC.",
 "second_opinion": {
  "file": "research/PAYC/2026-11-17-evaluation-2.md",
  "conviction": 4
 }
}
```
