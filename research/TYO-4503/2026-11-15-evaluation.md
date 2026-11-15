# Evaluation: Astellas Pharma Inc. (TYO:4503) — 2026-11-15
## Bear case
The low multiples sit on peak earnings from one drug. Management guides XTANDI sales lower from the fiscal third quarter on US IRA price negotiation, then US generic entry in 2027, and the rising margins have not yet absorbed it [Likely]. The 12.6x P/E and 6.6x EV/EBITDA, below their 5y minimums, may be a value trap if TTM EPS falls sharply [Likely]. The price is extended: 15.1% above the 200-day average after a 45.6% 12-month gain, so any sign that strategic brands are not replacing XTANDI risks a de-rating [Likely]. FCF margin is 2.8pp below its 2-year high of 23.5%, an early hint that cash has peaked as the cliff nears [Guessing]. Mechanical fair value is unreliable (methods disagree 2.3x) and the P/E method's base of 2,199.65 sits below the price [Certain]. Repeated licensing deals could re-lever a balance sheet that hit 2.38x net debt/EBITDA in FY2024 [Guessing].

## Bull case
Returns are at their 2-year highs on a rolling basis: ROIC 17.3%, operating margin 21.1%, both rising over 1 and 3 years [Certain]. The 2026-11-04 results raised full-year revenue and core-profit guidance on strategic brands and cost discipline [Likely]. The reverse DCF already implies revenue falling 7.2% in year 1, so the market prices the XTANDI cliff [Likely]. P/FCF of 9.8x and a 10.15% FCF yield, a third to half below Japanese pharma peers, leave room even if cash flow falls [Certain]. Net debt/EBITDA is back to 0.27x, Piotroski 7, and the share count is stable [Certain]. Beta of 0.04 and a small yen move make macro background only [Certain]. The FCF margin dip below its 2-year high is a step back within a rising year (+2.4pp on a year ago), not a break [Likely].

## Decision
```json
{
  "ticker": "TYO:4503",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin are all higher than a year earlier and three years earlier on a rolling basis [RA-T, IS-T, CF-T]; the FCF margin sits below its 2-year high but rose over the last year.", "moat": "narrow", "key_risk": "high", "key_risk_text": "XTANDI erosion from US IRA price negotiation and 2027 US generics is guided to begin now; current TTM margins are peak-looking and strategic brands may not replace the profit before the extended price de-rates.", "veto": null},
  "thesis": "A deleveraged, high-return drugmaker at multiples below its own 5-year minimums with raised guidance, but whose earnings rest on XTANDI ahead of a guided US price and patent cliff.",
  "rationale": "Quality, balance sheet and trend are strong and the multiples look low, but they sit on peak XTANDI earnings with erosion guided to start now and US generics in 2027. The fair value is unreliable and the P/E method sits below the price. Good but not compelling: no position.",
  "price_at_decision": 2699.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-4503/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15% (21.1% now), showing strategic brands are not replacing XTANDI profit.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 10% (17.3% now), a return toward the FY2024 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 12% (20.6% now), showing cash generation is breaking with the XTANDI cliff.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.27x TTM now) from debt-funded licensing deals.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3500, "basis": "Strategic brands offset XTANDI and EV/EBITDA re-rates toward its 5y median of 8.9x [RA], still below the DCF base of 5,108.48 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 2700, "basis": "XTANDI erosion trims earnings while the multiple holds near today's 9.8x P/FCF [RA], consistent with the reverse DCF already pricing a 7.2% year-1 revenue fall; below the unreliable blended base of 4,138.87 because that rests on peak TTM cash flow."},
    "bear": {"probability": 0.30, "target_price_12m": 2000, "basis": "Erosion outruns the pipeline and the extended price (15.1% above its 200-day average [ST,HI]) de-rates toward the P/E method's base of 2,199.65 and below [fact sheet fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the multiples are already below their 5y minimums; what blocks a buy is the unproven replacement of XTANDI earnings, which a lower price would not resolve. Re-check once results show strategic brands offsetting XTANDI erosion.",
  "replaces": null,
  "replacement_reason": null
}
```
