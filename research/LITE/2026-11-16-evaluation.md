# Evaluation: Lumentum Holdings Inc. (LITE) — 2026-11-16
## Bear case
LITE is no longer a standalone fundamental bet: a signed all-stock takeover by Marvell at a fixed 4.500 ratio [company-reported] makes its price mostly a derivative of Marvell's, and shareholders on both sides panned the terms [Certain]. If the deal breaks (votes, antitrust, remedies) the stock loses its anchor, and LITE may owe a $2.9bn termination fee [company-reported] in some cases [Likely]. On its own numbers it is expensive: EV/EBITDA 43.5x, +59% vs peers, P/FCF 141.9x, a 0.70% FCF yield, and a base fair value of 254.21 vs a 596.62 close [Certain]. The ROIC and FCF direction change is a cyclical rebound from loss years FY2023-25, not a proven through-cycle record [Likely]; FCF/NI is -5.4% and shares rose 11.16% YoY [Certain]. The price is 26.8% under its 200-day average, so no trend strength; rising real yields (10y TIPS 2.86%) hurt this duration [Likely]. FCC Covered List risk is unresolved [Likely].
## Bull case
The business is working: TTM ROIC 23.0% vs -3.6% a year earlier, operating margin 23.4% vs -5.7%, gross margin 48.0%, all at 2-year highs [Certain]. The 5-year falling ROIC and FCF trends reflect the FY2023-25 trough; the last 12 months are rising because AI/cloud demand is outpacing supply, per management [Likely]. Net cash (net debt/EBITDA -0.48x), Altman Z 10.48 and Piotroski 7 make the balance sheet sound [Certain]. EV/EBITDA sits only 27% through its own 5-year range [Certain]. The 32.2% 3-month fall partly reflects merger reaction rather than operations, and combination with Marvell could add laser-electronics co-design benefits [Guessing]. Still +138.5% over 12 months [Certain].
## Decision
```json
{
  "ticker": "LITE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years; the 5-year fiscal declines in ROIC and FCF margin come from the FY2023-25 loss years, and the rolling 12 months are rising (ROIC -3.6% -> 23.0%, FCF margin -4.8% -> 9.5%) on AI/cloud demand outpacing supply (https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/lite-20260926.htm).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The pending fixed-ratio all-stock Marvell takeover makes the price track Marvell's equity and a deal break, not Lumentum's fundamentals; at 43.5x EV/EBITDA and a 0.70% FCF yield a cyclical slowdown would also de-rate it.",
    "veto": {"code": "binary_event", "reason": "Signed all-stock merger with Marvell at a fixed 4.500 ratio needing both shareholder votes and antitrust approval; the outcome, not the business, drives the 12-month return (research note section 6)."}
  },
  "thesis": "A recovering AI-optics supplier with strong rolling returns whose share price is now a fixed-ratio derivative of a contested Marvell takeover and trades far above its mechanical fair value.",
  "rationale": "The pending all-stock Marvell deal is a binary event that decides the outcome independently of the fundamentals, the price is well above every base valuation anchor with a thin FCF yield, and it sits below its 200-day average, so neither a discount nor trend strength supports a buy. Cash is acceptable.",
  "price_at_decision": 596.62,
  "price_date": "2026-11-13",
  "research_note": "research/LITE/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, reversing the mix and utilisation gains.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM operating margin falls below 15%, showing the AI-demand recovery is fading.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin turns negative as capex outruns cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "The Marvell merger agreement is terminated or its terms are amended, as disclosed in a company filing or release (re-assess LITE as a standalone business)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 860.68, "basis": "Deal closes and Marvell's equity recovers, taking LITE back to its 50-day average of 860.68 [ST,HI], below the bull fair value of 1,148.66 because the fixed ratio caps standalone re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 596.62, "basis": "Price stays tied to Marvell under the fixed 4.500 ratio (note section 6), with strong rolling margins [IS-T] offset by a 43.5x EV/EBITDA [RA]; above the 254.21 base fair value, which rests on EV/EBITDA alone with DCF unusable."},
    "bear": {"probability": 0.35, "target_price_12m": 254.21, "basis": "Deal fails or Marvell de-rates and LITE reverts to the mechanical base fair value of 254.21 on EV/EBITDA [IS,RA]; probability raised slightly for the macro overlay's small tilt toward bear on rising real yields (research/LITE/2026-11-16-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unresolved Marvell takeover is a binary event that decides the return; a lower price would not change the decision until the deal closes or breaks.",
  "replaces": null,
  "replacement_reason": null
}
```
