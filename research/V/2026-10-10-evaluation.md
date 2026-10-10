# Evaluation: Visa Inc. (V) — 2026-10-10
## Bear case
The business is excellent, but the price leaves no room for error. P/FCF of 33.7x and P/B of 20.4x sit above their 5y maximums, and the FCF yield is 2.97% [Certain]. The reverse DCF implies 22.6% year-one revenue growth, well above Visa's recent trend [Certain]. Mechanical fair value is 211.42 base and 292.83 bull, so even the bull case is 24.0% below the close [Certain]. FCF margin has fallen 6.3pp to 47.2% and FCF conversion 10.4pp to 93.0% [Certain]. Interchange-reform legislation has reportedly gained presidential support, which threatens the fee pool behind issuer economics [Likely]. Real yields rose 56bp in three months to 2.87%, barely below the FCF yield. That can compress the multiple with no change in the business [Likely]. Results on Oct 27 add event risk to a stock at its 52-week high [Likely].
## Bull case
Visa is among the highest-quality franchises listed. ROIC is 54.8% and rising (+19.3pp over 5y), operating margin is 66.9% and gross margin 97.7% [Certain]. The network effect is two-sided and entrenched, and new rails such as stablecoins and agentic payments are being built on Visa rather than around it [Likely]. Leverage is negligible at 0.32x net debt/EBITDA, and the share count fell 2.88% YoY through buybacks [Certain]. The DCF fair value is blind to a moat this durable and is run at a 5.22% risk-free rate [Likely]. The P/E-based fair value of 315.79–375.63 is closer to the price [Certain]. Relative strength vs SPY is +10.5pp over 6m and short interest is just 1.09% [Certain]. Interchange bills have stalled before [Guessing].
## Decision
```json
{
  "ticker": "V",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Visa is a best-in-class network with rising 54.8% ROIC, but at 33.7x P/FCF (above its 5y max), a 2.97% FCF yield and a reverse-DCF 22.6% growth requirement, the price already discounts more than the business is likely to deliver.",
  "rationale": "Quality is not in doubt; price is. Every own-history multiple sits at or above the top of its range, and even the P/E fair-value bull case (375.63) is below the close. Rising real yields (macro overlay) and the interchange bill add downside. The 12-month expected return is negative, so this is good-but-not-compelling: AVOID and wait for the entry price.",
  "price_at_decision": 385.45,
  "price_date": "2026-10-09",
  "research_note": "research/V/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 40%, reversing most of the five-year rise from 29.8% to 54.8% and signalling moat or pricing erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 45%, extending the decline from 60.2% (FY2021) to 47.2% and showing cash conversion is structurally weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 45}},
    {"text": "TTM operating margin falls below 60%, under the 5y range of 65.6%-67.2%, showing client incentives or regulation are compressing network economics.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 60}},
    {"text": "The interchange-reform credit-card bill (WSJ, 2026-10-08) advances to a floor vote in either chamber of Congress."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 430.13, "basis": "Fundamentals stay strong (ROIC 54.8% rising [RA]) and P/E re-rates to its 5y max of 36.6x [RA] on TTM EPS. Probability is cut from 0.25 by the macro overlay's moderate bear tilt, because rising real yields cap re-rating (research/V/2026-10-10-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 346.56, "basis": "P/FCF eases to its 5y max of 30.3x [RA] on TTM FCF as the FCF margin drifts lower (47.2% TTM [CF,IS]). The target sits above the DCF base of 211.42 [fact sheet] because that DCF ignores the rising ROIC and buybacks (-2.88% shares [ST]); it is within the P/E fair-value range of 315.79-375.63."},
    "bear": {"probability": 0.3, "target_price_12m": 273.88, "basis": "The interchange bill advances (WSJ URL in the fact sheet) and real yields keep climbing, compressing P/E to the P/E-method bear fair value of 273.88 [fact sheet], about its 5y min of 23.3x [RA]. Probability is raised from 0.25 by the macro overlay's moderate bear tilt (research/V/2026-10-10-macro.md)."}
  },
  "entry_price": 315.79,
  "entry_basis": "P/E-method base fair value of 315.79 [fact sheet], roughly P/E back at its 5y median of 26.9x [RA]. The default (DCF base 211.42 x 0.8) is not used: a DCF at a 5.22% risk-free rate never values a 54.8%-ROIC, buyback-funded compounder at any price it has traded at in 5 years (52-week low 293.89 [HI]), so it would never trigger a re-research.",
  "replaces": null,
  "replacement_reason": null
}
```
