# Evaluation: Dassault Systèmes SE (EPA:DSY) — 2026-11-24
## Bear case
The fall followed the 17 November Capital Markets Day, whose 2029 plan back-loads double-digit growth, reinvests part of the margin gain and needs subscription growth to accelerate [Likely]. That is a growth reset, not noise: the price implies 7.2% year-1 revenue growth while Q3 revenue grew 5% [Certain], so the discount to peers (P/E 22.4x vs 46.2x) may be deserved for a slower grower [Likely]. The AI and usage-based monetisation story is unproven and unquantified [Likely]. The five-year FCF margin decline (31.1% to 23.6%) means the recent TTM rebound to 27.3% may flatter the run-rate [Guessing]. The two fair-value methods disagree widely (DCF 19.21 vs EV/Revenue 37.80), so the base 25.41 is fragile [Certain]. The price is still above its 200-day average after a 52-week low of 15.82; if growth slows further, the de-rating can continue [Likely]. A weaker euro's translation effect is of unverified size [Guessing].
## Bull case
A sticky, mission-critical engineering-software franchise with 84.2% gross margin, net cash (net debt/EBITDA -0.57x) and shrinking share count [Certain]. The last 12 months are improving, not deteriorating: operating margin up 4.0pp to 25.5%, FCF margin up 4.0pp to 27.3%, ROIC 17.0% versus 15.7% a year earlier [Certain]. Q3 raised full-year revenue, margin and EPS guidance [Likely]. Yet every multiple sits below its own 5-year minimum (P/E 22.4x vs 26.2x, EV/EBITDA 14.5x vs 18.3x, P/FCF 16.9x vs 21.3x) at a 5.93% FCF yield [Certain]. The dip is a reaction to a long-dated plan, not to a broken quarter, and no single-day results-type reaction shows [Certain]. Beta 0.56 and founder control limit downside volatility [Likely].
## Decision
```json
{
  "ticker": "EPA:DSY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all rising (FCF margin 23.3% -> 27.3% TTM [CF-T,IS-T]); the 5-year FCF margin fall from 31.1% reflects a FY2021 base the note judges timing-inflated.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The CMD's back-loaded 2029 plan means near-term growth stays mid-single-digit, below the 7.2% the price implies, so the de-rating continues.",
    "veto": null
  },
  "thesis": "A net-cash, high-margin engineering-software franchise with improving rolling returns trades below its own 5-year minimum multiples after a Capital Markets Day that pushed growth out.",
  "rationale": "Quality is high and rolling trends improve, and the dip followed a back-loaded plan rather than a broken quarter. But base fair value sits only moderately above the price, the methods disagree widely, and the price already implies growth above the latest quarter. Good but not compelling: AVOID.",
  "price_at_decision": 22.14,
  "price_date": "2026-11-23",
  "research_note": "research/EPA-DSY/2026-11-24.md",
  "triggers": [
    {"text": "TTM gross margin falls below 80%, signalling pricing pressure from AI-native or cheaper rivals.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "TTM ROIC falls below 12%, giving up most of the rise from 10.5% in FY2021 to 17.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 20%, under the five-year low, showing the subscription shift is draining cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Shares outstanding change YoY rises above 2%, signalling acquisition-funded dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 32.54, "basis": "Guidance beats and the CMD growth path gains credibility, so multiples recover toward the bottom of their 5y ranges; matches the fact sheet's bull fair value 32.54 [RA,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 25.41, "basis": "Mid-single-digit growth with rising margins (operating margin 25.5% TTM [IS-T]) lifts the price to the base fair value 25.41, still below the 5y minimum multiples [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.83, "basis": "Growth stays below the 7.2% the reverse DCF implies and the de-rating extends to the DCF-led bear fair value 16.83 [IS,CF]."}
  },
  "entry_price": 21.6,
  "entry_basis": "valuation file: base 25.41 x 0.85.",
  "replaces": null,
  "replacement_reason": null
}
```
