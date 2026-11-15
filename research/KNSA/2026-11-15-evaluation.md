# Evaluation: Kiniksa Pharmaceuticals International, plc (KNSA) — 2026-11-15
## Bear case
KNSA is a single-product story: almost all revenue is ARCALYST in one US indication, so one competitive or payer setback hits the whole franchise [Likely]. The price already discounts a lot: P/E 72.8x sits at the 82nd percentile of its 5y range and far above the 25.1x peer median, P/B 10.6x is above its 5y max and the FCF yield is only 2.60% [Certain]. The stock is 53.3% above its 200-day average after a 137.4% 12-month rise, so any slowing of ARCALYST growth risks a sharp de-rating toward the mechanical base fair value of 62.70 [Likely]. Gross margin has fallen from 74.2% to 54.3% over five years [Certain]. KPL-387 pivotal data in H2 2027 is a binary event the follow-on moat depends on [Likely]. Shares outstanding rose 8.67% YoY and short interest is 10.58%, up 14.1% [Certain]. Rates are context only per the overlay.
## Bull case
The business is working: TTM ROIC 68.3%, operating margin 13.8% and FCF margin 20.8% are all rising on the rolling-12-month table, with no direction change [Certain]. Q3 beat and 2026 ARCALYST guidance was raised to $1.045B-$1.050B [Certain]. The balance sheet is net cash (net debt/EBITDA -4.24x), Altman Z 10.42, Piotroski 7, so growth and Phase 3 spending are self-funded [Certain]. FCF conversion is strong (180.0%) and P/FCF of 38.4x is at the 10th percentile of its own range, because FCF is compounding faster than the price [Certain]. ARCALYST's niche position in recurrent pericarditis plus the KPL-387 monthly follow-on could extend the franchise well beyond today's earnings, which the mechanical P/E fair value cannot see [Guessing]. Beta 0.08 and non-cyclical US specialty demand limit macro risk [Likely].
## Decision
```json
{
  "ticker": "KNSA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are all rising over 1 and 3 years on the rolling table [RA-T, IS-T, CF-T]; no Python-listed metric is falling.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Single-product concentration at a P/E far above peers and a price 53.3% above its 200-day average: any slowdown in ARCALYST growth or a KPL-387 miss would drive a sharp de-rating.",
    "veto": null
  },
  "thesis": "A fast-improving, net-cash single-product biotech whose ARCALYST growth is real, but whose price is extended well above its trend and mechanical fair value.",
  "rationale": "Quality, direction and balance sheet are strong, but the price is above the base fair value and too far above its 200-day average to earn trend-strength points, while single-product and KPL-387 risk is high. Good but not compelling at this price: AVOID, with an entry price at the base fair value less the margin of safety.",
  "price_at_decision": 96.33,
  "price_date": "2026-11-13",
  "research_note": "research/KNSA/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8%, reversing the rise to 13.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 12%, showing the cash step-up to 20.8% was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM gross margin falls below 48%, extending the slide from 74.2% to 54.3%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 48}},
    {"text": "Company-reported pivotal KPL-387 data fails its primary endpoint, or ARCALYST net revenue guidance is cut (sec.gov filings or company release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 115.96, "basis": "Continued ARCALYST growth after the raised 2026 guidance [OV] carries earnings to the mechanical bull fair value of 115.96 [IS,RA]."},
    "base": {"probability": 0.45, "target_price_12m": 88, "basis": "Earnings keep growing on raised guidance [OV] but the P/E of 72.8x compresses toward its 5y median of 53.0x [RA], leaving the price somewhat below today."},
    "bear": {"probability": 0.30, "target_price_12m": 50, "basis": "Growth slows and the stock de-rates toward the mechanical base fair value of 62.70 and beyond toward the 6-month low of 46.10 [HI]; the mechanical bear of 6.72 is a P/E artefact of the loss-making history and is not used."}
  },
  "entry_price": 50.16,
  "entry_basis": "valuation file: base 62.70 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
