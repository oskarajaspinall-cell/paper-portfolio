# Evaluation: Permian Resources Corporation (PR) — 2026-11-15
## Bear case
PR is a price taker: returns follow oil, and the note finds no moat beyond low-cost Delaware inventory [Likely]. The stock is up 73.2% in 12 months and sits at the top of its own history: EV/EBITDA 5.1x is at 81% of its 5y range, P/B 1.6x is above its 5y max, and P/FCF 18.8x is well above the peer median 11.9x [Certain]. An extended price risks a de-rating if oil or production growth slows [Likely]. The mechanical fair value (base 10.62, bull 23.87) puts the price near the bull case, though EV/EBITDA alone is crude for an E&P [Likely]. Operating margin of 35.4% is 8.5pp below its 2-year high of 43.9%, a commodity-price effect rather than lost share, showing how fast margins move [Likely]. FCF conversion is 64.6% and shares rose 13.52% YoY, so per-share cash lags headline growth [Certain]. Waha gas realisations went negative in April 2026 [Certain].

## Bull case
Rolling returns are rising: ROIC 12.0% vs 9.3% a year earlier and FCF margin 16.2% vs 13.6% [Certain]. The five-year FCF-margin fall reflects reinvestment for growth, not a broken model, and the last 12 months have reversed it [Likely]. Net debt/EBITDA has fallen to 0.71x from 1.66x and the company is investment grade at all three agencies [company-reported] [Certain]. Q3 2026 came with an improved full-year outlook and bolt-on acquisitions adding inventory [Likely]. The trend is healthy: the close is 10.9% above the 200-day average, relative strength vs SPY is +62.8pp over 12 months, and the FCF yield is a real 5.33% [Certain]. On peers it is not expensive on EV/EBITDA (5.1x vs 5.3x) [Certain]. Beta is 0.58 and the business is US-only [Certain].

## Decision
```json
{
  "ticker": "PR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 year: ROIC 9.3% -> 12.0%, FCF margin 13.6% -> 16.2%, operating margin flat at 35.4% [RA-T, IS-T, CF-T]; operating margin's distance from its 2-year high of 43.9% tracks commodity prices.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "An oil-price fall compresses margins and de-rates a stock already at the top of its own EV/EBITDA and P/B ranges after a 73.2% 12-month run.",
    "veto": null
  },
  "thesis": "A low-leverage Delaware Basin producer with rising rolling returns and a strong uptrend, but no moat and a price at the top of its own multiple history, leaving returns hostage to oil.",
  "rationale": "Quality and balance sheet are sound and the trend is strong, but returns are commodity-driven with no durable edge, the multiples sit at their 5y highs and the mechanical fair value is far below the price. Good but not compelling: AVOID.",
  "price_at_decision": 23.05,
  "price_date": "2026-11-13",
  "research_note": "research/PR/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, under the year-earlier 9.3%, showing the returns recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.71x TTM), showing acquisitions are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin falls below 10%, showing growth capex is absorbing the cash again.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 28%, well below the 35.4% now.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26.07, "basis": "Oil holds, rolling ROIC keeps rising and EV/EBITDA moves to its 5y max of 5.4x [RA], retesting the 52-week high of 26.07 [HI]; above the mechanical bull of 23.87 because acquisitions add EBITDA the model does not see."},
    "base": {"probability": 0.5, "target_price_12m": 22.61, "basis": "EV/EBITDA eases to its 5y median of 5.0x [RA] on flat TTM EBITDA, near the recent swing low of 22.61 [HI]; well above the mechanical base of 10.62, which ignores reserve NAV ([data unavailable])."},
    "bear": {"probability": 0.25, "target_price_12m": 13.18, "basis": "Oil falls and EV/EBITDA de-rates toward its 5y min of 3.9x [RA], back to the 52-week low of 13.18 [HI], between the mechanical bear 7.39 and base 10.62 and the current price."}
  },
  "entry_price": 18.44,
  "entry_basis": "Mechanical base 10.62 x 0.8 is unreliable for an E&P without reserve NAV; instead a de-rating to about 80% of today's price (23.05 x 0.8), near the 6-month low of 17.90 [HI], would move the valuation from trend to discount with the same fundamentals.",
  "replaces": null,
  "replacement_reason": null
}
```
