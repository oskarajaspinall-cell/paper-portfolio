# Evaluation: Orion Oyj (HEL:ORNBV) — 2026-11-15
## Bear case
Profit now rests on one product Orion does not sell: Nubeqa royalties from Bayer drove Q3 and the FY26 guidance raise [Likely], and management says the royalty rate peaked in Q2, so further growth needs Bayer's market sales to keep rising [Likely]. Management declined to address competing generics and a US tariff/supply impact on Q4 [Likely]. The price has run far ahead: up 72.0% in 12 months, 35.3% above the 200-day average, RSI 81.5, P/B and EV/Sales above their 5y maxima, and the reverse DCF needs 24.6% year-1 revenue growth [Certain]. An extended price on a single royalty stream risks a sharp de-rating if Nubeqa growth merely slows [Likely]. Cash lags profit: FCF conversion 62.7% TTM and FCF margin down over five fiscal years [Certain]; the base fair value of 51.76 EUR sits far below the 103.00 close [Certain].
## Bull case
Returns are exceptional and still climbing on a rolling basis: TTM ROIC 49.9% vs 32.1% a year earlier, operating margin 38.1% vs 26.7% [Certain]. The 5-year FCF-margin decline has reversed over the last 12 months (15.3% to 19.0%), consistent with capacity investment rather than a broken model [Likely]. The balance sheet is effectively net cash (-0.02x), Altman Z 13.15, Piotroski 7, with buybacks running [Certain]. Royalties carry no commercial cost, so incremental Nubeqa sales fall almost straight to profit, and label expansion could extend the runway [Likely]. P/E of 22.0x sits mid-way in its own 5y range and only slightly above peers [Certain], so the earnings re-rating is modest; the price trend is strong with a 2.86% FCF yield [Certain].
## Decision
```json
{
  "ticker": "HEL:ORNBV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over 1 or 3 years; only the 5-fiscal-year FCF margin is down (-3.3pp [CF,IS]), and the rolling 12 months have reversed it (15.3% to 19.0% [CF-T,IS-T]); the note attributes the cash lag partly to capacity investment.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Single-product concentration: Nubeqa royalties drive profit, the royalty rate peaked in Q2, and generics/tariff questions were left unanswered (Q3 2026 call); at an extended price (RSI 81.5, reverse DCF 24.6% growth) any slowdown would de-rate the stock.",
    "veto": null
  },
  "thesis": "An exceptionally profitable, net-cash Finnish pharma whose returns have stepped up on Bayer's Nubeqa royalties, but whose price already discounts sustained royalty growth from a single product whose royalty rate has peaked.",
  "rationale": "Quality, balance sheet and trend are strong, but profit is concentrated in one Bayer-controlled royalty stream whose rate has peaked, while the price is extended and implies high growth. The scorecard does not reach the buy bar; good but not compelling is an AVOID.",
  "price_at_decision": 103.00,
  "price_date": "2026-11-13",
  "research_note": "research/HEL-ORNBV/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30% (38.1% now), showing Nubeqa royalty growth has stalled or reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 30% (49.9% now), giving up the royalty-driven step-up.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 12% (19.0% now), showing cash conversion is not recovering.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Orion or Bayer discloses generic competition to Nubeqa in a major market, or a guidance cut tied to Nubeqa royalties."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 120.00, "basis": "Nubeqa market sales keep growing after the Q3 guidance raise [OV transcript] and P/E holds near today's 22.0x [RA] on higher earnings, above the mechanical bull fair value of 112.69 because royalties carry no commercial cost."},
    "base": {"probability": 0.45, "target_price_12m": 96.00, "basis": "Royalty rate has peaked (Q3 2026 call) so earnings growth slows and P/E drifts to its 5y median 20.5x [RA]; well above the mechanical base fair value of 51.76, which the DCF anchors on a weaker FCF history [CF]."},
    "bear": {"probability": 0.30, "target_price_12m": 70.00, "basis": "Nubeqa growth slows or generics/tariff risk emerges (Q3 2026 call), P/E falls toward its 5y low 17.9x [RA] on lower earnings, still above the mechanical bear fair value of 21.06."}
  },
  "entry_price": 41.41,
  "entry_basis": "valuation file: base 51.76 x 0.8; at that price the single-product concentration would be priced in.",
  "replaces": null,
  "replacement_reason": null
}
```
