# Evaluation: Micron Technology, Inc. (MU) — 2026-11-16
## Bear case
MU is a commodity memory producer at peak-cycle returns: TTM ROIC is 93.4% and operating margin 74.6%, against ROIC of -7.4% in FY2023 and 1.7% in FY2024 [RA] [Certain]. The 9.9x P/E looks cheap only because it sits on peak earnings; the 5y median is 14.4x and the mechanical base fair value is far below the price (flagged unreliable) [Certain]. The 10-K warns rival capacity additions could cut ASPs, which have swung from +200% to -50% a year over five years [company-reported] [Certain]. The trend is breaking: the price is -17.5% below its 50-day average, only 1.7% above its 200-day, and trails SPY by 15.0pp over 3 months on AI-spending doubts [HI] [Certain]. After a +217.8% year, an extended price risks a hard de-rating if memory pricing or AI capex slows [Likely]. Beta 2.40 and heavy capex (30.7bn USD [company-reported]) amplify the downside [Certain].
## Bull case
Every return and cash metric is at its 2-year high with no direction change: FCF margin 44.3% vs 4.5% a year earlier, net cash, Altman Z 9.72, Piotroski 8 [RA-T][ST] [Certain]. Take-or-pay strategic customer agreements with multi-year volumes and price bands, backed by 12.75bn USD of customer deposits, may damp the cycle; management says even floor-price margins would exceed past peaks [company-reported] [Likely]. About 60% of revenue is data centre, tied to AI demand that the filing calls hard to forecast but which keeps supply tight [company-reported] [Likely]. P/E is at 2% of its 5y range, P/FCF below its 5y minimum and the FCF yield is 6.70% [RA][ST] [Certain]. The recent fall is tied to a sector sell-off around Nvidia, not to Micron's own results [Likely]. If margins merely hold, the multiple has room to re-rate toward its own median [Guessing].
## Decision
```json
{
  "ticker": "MU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds ROIC, operating margin and FCF margin all rising over 1 and 3 years, each at its 2-year high [RA-T][IS-T][CF-T].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Memory ASPs reverse as rival capacity arrives or AI capex slows, collapsing peak margins (FY2023 ROIC -7.4% [RA]) and de-rating a price that has risen +217.8% in a year.",
    "veto": null
  },
  "thesis": "Micron is earning record, net-cash returns on AI-driven memory demand, but as a commodity producer at peak-cycle margins with a weakening price trend its low trailing multiples do not offer a margin of safety against an ASP reversal.",
  "rationale": "Quality, balance sheet and direction are excellent, but there is no durable moat, earnings sit at a cyclical peak, the key risk is high and the value blend sits well below the price, so the scorecard stays below the buy bar. Good but not compelling: AVOID.",
  "price_at_decision": 778.31,
  "price_date": "2026-11-13",
  "research_note": "research/MU/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55% (80.7% now), showing the pricing step-up is reversing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM FCF margin falls below 25% (44.3% now) while capex keeps rising.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 40% (93.4% now), a reversion toward mid-cycle returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Management discloses cancelled, renegotiated or price-reduced strategic customer agreements in a 10-K/10-Q or company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1073.44, "basis": "Strategic agreements hold pricing and margins, and the multiple re-rates toward its own 5y median P/E of 14.4x [RA], reaching the fact sheet's bull fair value."},
    "base": {"probability": 0.45, "target_price_12m": 778.31, "basis": "Supply stays tight but the market keeps a peak-earnings P/E near 9.9x [RA] while margins plateau, leaving the price roughly flat; above the unreliable mechanical base because the through-cycle DCF assumes an immediate reversion."},
    "bear": {"probability": 0.3, "target_price_12m": 326.67, "basis": "Rival capacity cuts ASPs as the 10-K warns [company-reported], EBITDA falls toward mid-cycle and the stock trades at the EV/EBITDA method's base value [valuation file]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock has no durable moat and earnings are at a cyclical peak, so the mechanical fair value (flagged unreliable) gives no sound anchor; a lower price driven by an ASP reversal would also cut earnings. Re-research on new results or if the cycle resets.",
  "replaces": null,
  "replacement_reason": null
}
```
