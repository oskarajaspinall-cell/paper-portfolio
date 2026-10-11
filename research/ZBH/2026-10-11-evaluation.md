# Evaluation: Zimmer Biomet Holdings, Inc. (ZBH) — 2026-10-11
## Bear case
Cheap for a reason. TTM ROIC is 6.2% and ROCE 7.2%, flat over five years, below a plausible cost of capital for most of the period [Certain]/[Likely]. Gross margin has slid to 69.5% from 71.3% and operating margin to 16.6% from a 20.8% FY2024 peak, which points to mix and cost pressure rather than pricing power [Certain]. FCF conversion has fallen from 362.4% to 148.8% [Certain]. Net debt/EBITDA has risen back to 2.83x from 2.35x, and Altman Z of 2.51 sits in the grey zone [Certain]. The Americas sales-channel overhaul runs until end-2027, so execution risk sits across the whole 12-month horizon [Likely]. Relative strength is -25.0pp vs SPY over 12 months, and Q3 results land on Nov 4 [Certain]. Multiples below their 5-year lows may simply reflect a lower-quality franchise that is re-rating permanently [Guessing].
## Bull case
Every multiple is below its own 5-year minimum: 21.7x P/E, 9.6x EV/EBITDA and 14.2x P/FCF, with a 7.06% FCF yield [Certain]. EV/EBITDA is 17% below the peer median [Certain]. The reverse DCF implies only 1.0% year-1 revenue growth, while Q2 2026 organic growth was 4.0% and full-year guidance was raised [Certain]. The base fair value of 105.35 is 18.2% above the 89.14 close [Certain]. Buybacks are shrinking the share count 1.95% a year [Certain]. Demand is demographic and procedure-driven, and beta is 0.49 [Certain]. The oligopoly structure and surgeon switching costs protect volumes [Likely]. If the channel overhaul lifts productivity, operating margin can rebuild toward the 20%+ FY2023-24 levels [Guessing].
## Decision
```json
{
  "ticker": "ZBH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-return, margin-eroding orthopaedics franchise trades below its own 5-year minimum multiples at a 7.06% FCF yield, but the discount reflects flat ~6% ROIC and falling gross and operating margins more than mispricing.",
  "rationale": "The valuation is undemanding (1.0% implied growth vs 4.0% organic), but quality is mediocre and slipping: ROIC 6.2%, gross margin down 1.6pp, leverage up to 2.83x, and the turnaround is unproven until 2027. That is good but not compelling, so conviction is 3: AVOID. The stock becomes a buy at 84.28, the base fair value less a 20% margin of safety.",
  "price_at_decision": 89.14,
  "price_date": "2026-10-09",
  "research_note": "research/ZBH/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 5%, under the FY2022 five-year low of 5.0%, confirming returns are structurally sub-cost-of-capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5}},
    {"text": "TTM gross margin falls below 68%, extending the drift from 71.3% (FY2021) to 69.5% and showing pricing/mix erosion is structural.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "TTM operating margin falls below 15%, under the five-year FY range low of 17.0%, showing the sales-channel overhaul is costing margin rather than lifting it.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "Organic constant-currency revenue growth in a quarterly earnings release turns negative or full-year guidance is cut, undermining the commercial-transformation thesis."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 120.0, "basis": "The channel overhaul delivers, organic growth beats the 1.0% reverse-DCF bar, and P/E re-rates toward its 5y median 25.3x [RA] on TTM EPS; this is set well below the 179.17 bull fair value because the P/E bull leg (272.03) is inflated by the 115.6x depressed-earnings year [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 100.0, "basis": "Organic growth around the 4.0% Q2 2026 level [OV transcript] lets multiples recover partway from below their 5y minimum toward the peer median 11.6x EV/EBITDA [RA,P]; this is a modest discount to the 105.35 base fair value because flat 6.2% ROIC and falling gross margin [RA,IS] justify a persistent quality discount."},
    "bear": {"probability": 0.25, "target_price_12m": 73.21, "basis": "Gross and operating margins keep drifting (69.5%/16.6% TTM [IS]), leverage stays near 2.83x [RA] and the overhaul disrupts sales; the price falls to the 73.21 bear fair value [fact sheet Fair value]."}
  },
  "entry_price": 84.28,
  "entry_basis": "valuation file: base 105.35 x 0.8 = 84.28; at that level the 1.0% implied growth and below-minimum multiples would compensate for the mediocre quality.",
  "replaces": null,
  "replacement_reason": null
}
```
