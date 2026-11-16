# Evaluation: The Descartes Systems Group (TSX:DSG) — 2026-11-16
## Bear case
The price is carried by trend, not discount. At 134.65 CAD it sits 13.4% above the base fair value of 116.63, and the reverse DCF needs 18.5% year-1 revenue growth, which is demanding for this business [Likely]. It is 28.6% above its 200-day average after +48.1% in six months, with RSI 66.0 [Certain]. An extended price like this risks a de-rating if growth slows, and the next test is earnings on Dec 2, 2026 [Likely]. On cash it is not cheap: P/FCF 27.5x is +29% and EV/Sales +54% versus peers, and the FCF yield is only 3.64% [Certain]. FCF margin fell over five fiscal years (40.3% to 35.7%) and FCF conversion fell from 198.5% to 158.8% [Certain]. The cause is unexplained (the note guesses acquisition and tax timing) [Guessing]. Geographic mix could not be sourced [Certain].
## Bull case
Quality is high and improving on every rolling measure: ROIC 14.6%, operating margin 32.0% and FCF margin 38.5% are all at their 2-year highs, up from a year earlier [Certain]. The five-year FCF margin fall has reversed over the last 12 months (33.8% to 38.5%), so it reads as temporary, not erosion [Likely]. Net cash (net debt/EBITDA -1.19x), Altman Z 14.81 and Piotroski F 7 leave room for bolt-on acquisitions [Certain]. Multiples sit low in their own 5-year range (P/E 17%, EV/EBITDA 19%, P/FCF 13% position), and P/E is -12% versus peers [Certain]. Embedded logistics workflows and network services give switching costs [Likely]. Beta 0.23 and relative strength of +46.5pp over six months show a business that is working [Certain].
## Decision
```json
{
  "ticker": "TSX:DSG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No metric is falling over 1 or 3 years: ROIC, operating margin and FCF margin are all at their 2-year highs on the rolling view [RA-T, IS-T, CF-T]; the 5-year FCF margin fall (40.3% to 35.7%) has reversed to 38.5% TTM.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating of an extended price (28.6% above the 200-day average, 13.4% above base fair value) if growth falls short of the 18.5% year-1 revenue growth the reverse DCF implies, tested at the Dec 2, 2026 results.",
    "veto": null
  },
  "thesis": "A net-cash, high-margin logistics-software franchise with every rolling quality measure at its 2-year high, but priced above its mechanical fair value on demanding implied growth after a sharp run.",
  "rationale": "Quality and direction are strong, but the price sits above base fair value, the reverse DCF needs 18.5% growth and the stock is extended after a +48.1% six-month run. The scorecard gives conviction 3, below the buy bar; good but not compelling is an AVOID. Entry price set at base fair value less the margin of safety.",
  "price_at_decision": 134.65,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-DSG/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28% (32.0% now), reversing the five-year expansion from 25.9%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 11% (14.6% now), under the FY2022 level of 11.6%, showing acquisitions are diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 32% (38.5% now), under the FY2025 five-year low of 32.6%, showing the cash recovery was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 32}},
    {"text": "Net debt/EBITDA rises above 1.0x (-1.19x now) through debt-funded acquisitions.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165.51, "basis": "Rolling margin gains continue and EV/Sales moves back toward its 5y median 12.6x [RA], matching the EV/Revenue base fair value of 165.51 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 134.65, "basis": "Growth roughly meets the 18.5% the reverse DCF implies, so multiples hold low in their 5y range (P/E 17% position [RA]) and the price is flat; above the 116.63 base fair value because the DCF does not credit the rolling margin step-up [IS-T, CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 84.20, "basis": "Growth slows at the Dec 2, 2026 results and the extended price de-rates toward the mechanical bear fair value of 84.20 [fact sheet Fair value], near the 52-week low of 85.26 [HI]."}
  },
  "entry_price": 93.3,
  "entry_basis": "valuation file: base 116.63 x 0.8 (20% margin of safety); price, not quality, is the obstacle.",
  "replaces": null,
  "replacement_reason": null
}
```
