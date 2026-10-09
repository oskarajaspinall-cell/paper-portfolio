# Evaluation: Roper Technologies, Inc. (ROP) — 2026-10-09
## Bear case
Roper's returns are low. ROIC is 6.7% and ROCE 7.3% [RA], which is probably below its cost of equity at a 5.28% risk-free rate [Likely]. Each acquisition earns little more than it costs. The engine is also getting harder to fund. Net debt/EBITDA has risen to 3.38x from 2.53x in FY2023 [BS,IS] [Certain], and FCF conversion has dropped to 104.7% from 142-172% [CF,IS] [Certain]. The 15.3x P/E is flattered: the TTM net margin of 30.2% sits against a 5y run of 19-24% [IS], which points to a one-off gain [Likely]. The 10-K names the risk the market is pricing: AI commoditising vertical software [Likely]. Gross margin has slipped 1.3pp over five years [IS] [Certain]. Rising real yields raise both the discount rate and the cost of M&A debt (macro overlay) [Likely]. Q3 results on Oct 22 [ST] could confirm the de-rating [Guessing].

## Bull case
Every cash-flow multiple is below its 5-year floor: EV/EBITDA 14.5x vs a 18.2x minimum, P/FCF 13.7x vs 19.2x, EV/Sales 5.7x vs 7.2x [RA] [Certain]. The FCF yield is 7.28% [ST]. The price implies only 2.5% revenue growth [fair value], a low bar for a serial acquirer [Likely]. Operating margin has held at 27.6-28.4% for five years [IS] [Certain], and the FCF margin is still 31.7% [CF,IS]. So far AI has not dented the economics [Likely]. ROIC has risen every year [RA], and shares fell 2.63% YoY [ST] [Certain]. The mechanical base fair value of 534.52 is 46.8% above the 364.23 close [Likely]. Short interest is falling (-6.5%) [ST].

## Decision
```json
{
  "ticker": "ROP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Roper is optically cheap, below every 5-year multiple floor at a 7.28% FCF yield, but a 6.7% ROIC, rising leverage (3.38x), falling FCF conversion and an unresolved AI-disruption debate on vertical software make it good, not compelling.",
  "rationale": "The valuation is attractive, but the quality case is weak. ROIC is near the cost of capital, leverage and cash conversion are moving the wrong way, the P/E is flattered by one-off earnings, and AI-disruption risk is not yet disproven. Rising real yields add a small headwind. Conviction 3, so AVOID; holding cash is acceptable.",
  "price_at_decision": 364.23,
  "price_date": "2026-10-08",
  "research_note": "research/ROP/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC rises above 7.5%, extending the five-year uptrend (6.7% TTM) and showing acquired capital is starting to earn its cost; this would argue for re-initiation.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 7.5}},
    {"text": "TTM operating margin falls below 27.5%, under the 5-year floor of 27.6%, evidencing AI commoditisation or cloud-cost pressure eroding software economics; this would harden the AVOID.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 27.5}},
    {"text": "TTM FCF margin falls below 28%, from 31.7%, confirming the FCF-conversion slide is structural rather than timing; this would harden the AVOID.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}}
  ],
  "scenarios": {
    "bull": {"probability": 0.23, "target_price_12m": 480, "basis": "Q3 results ease the AI fear and EV/Sales recovers toward its 5y floor of 7.2x from 5.7x [RA]; the target sits below the 534.52 base fair value because leverage of 3.38x [BS,IS] caps the re-rating within 12 months, and the probability is trimmed slightly for the macro overlay's small bear tilt (research/ROP/2026-10-09-macro.md)."},
    "base": {"probability": 0.47, "target_price_12m": 390, "basis": "Multiples stay below their 5y floors (EV/EBITDA 14.5x vs 18.2x min [RA]), and the return comes from the 7.28% FCF yield [ST] and the 2.63% share shrink [ST]; this is well below the 534.52 base fair value because the market keeps pricing the reverse-DCF 2.5% growth."},
    "bear": {"probability": 0.30, "target_price_12m": 290, "basis": "Operating margin breaks its 27.6% floor [IS] on AI pressure while net debt/EBITDA stays above 3.38x [BS,IS], so the stock falls below the 305.96 52-week low [HI], though not to the 226.50 bear fair value given the FCF margin of 31.7% [CF,IS]; the probability is raised by the macro overlay's small bear tilt from a +0.61pp 3m rise in real yields (research/ROP/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock already trades below every 5-year multiple floor [RA] and below the default anchor (base 534.52 x 0.8 = 427.62, above the current price). The missing evidence is about the business: ROIC versus the cost of capital, the leverage and FCF-conversion trend, and the AI-disruption risk. Q3 results due Oct 22 [ST] should help settle it. A lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
