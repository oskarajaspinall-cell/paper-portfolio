# Evaluation: Brown & Brown, Inc. (BRO) — 2026-10-09
## Bear case
The cheapness is partly an illusion. EV/EBITDA of 9.8x and P/B of 1.7x look cheap mainly because the Accession deal added debt and equity, not because the market has mispriced the business [Likely]. Returns are falling. ROIC dropped from 12.0% to a TTM 9.5%, and ROE from 14.8% to 10.0% [Certain]. Net debt/EBITDA rose from 1.52x to 3.45x at FY25 [Certain]. Shares grew 17.07% YoY, so per-share value was diluted [Certain]. Organic revenue fell 0.7% in Q2 2026, per the company's release [Certain]. An Altman Z of 1.80 sits on the edge of the grey zone [Certain]. Risks from the captive-tax rules and litigation are still open [Likely]. Real yields and HY spreads are rising, which makes debt-funded M&A more expensive (macro overlay) [Certain]. The stock has fallen 33.3% in 12 months and lagged SPY by 48.9pp [Certain]. Q3 results on Oct 26 could confirm the organic slowdown [Guessing].

## Bull case
This is a fee-based broker with no underwriting risk [Certain]. It turns cash well: FCF conversion is 120% and the FCF margin is 21.7% TTM [Certain]. It also scores a Piotroski F of 7 [Certain]. P/E of 20.1x is below its 5-year minimum of 23.6x and close to the peer median of 19.8x [Certain]. The FCF yield is 6.78% [Certain]. All three own-history fair values sit above the 63.75 close, from a 67.05 bear to a 72.46 base [Certain]. If Accession integrates well, leverage should fall from the TTM 2.47x and organic growth should return [Guessing]. The operating margin has held at 28% or better for five years [Certain]. A beta of 0.59 limits drawdowns [Certain]. Short interest is falling [Certain].

## Decision
```json
{
  "ticker": "BRO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative, fee-based broker trades below its 5-year P/E range, but its returns are compressing, organic growth is negative and leverage and dilution rose after Accession, so the discount looks earned rather than mispriced.",
  "rationale": "Valuation is undemanding, but the quality trend points the wrong way: ROIC is down to 9.5%, ROE to 10.0%, shares grew 17.07% and organic revenue fell 0.7% in Q2. Upside to the fair-value base is only about 14%. The macro tilt leans to the bear side. Good, not compelling: no position, and the cash stays.",
  "price_at_decision": 63.75,
  "price_date": "2026-10-08",
  "research_note": "research/BRO/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 11%, back to the FY2024 level of 11.2%, showing Accession is earning its cost of capital.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 11}},
    {"text": "Debt/EBITDA falls below 2.2, back toward the FY2024 level of 2.13x, showing leverage repair after the deal.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.2}},
    {"text": "Organic revenue growth in the company's earnings release turns positive for two consecutive quarters, after the -0.7% in Q2 2026."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 74.85, "basis": "Organic growth recovers and P/E re-rates from 20.1x to its 5-year minimum of 23.6x [RA]; this sits below the 113.73 mechanical bull, which assumes a full return to history that the falling ROIC [RA] does not support; probability cut 0.05 for the macro overlay's small tilt toward bear (research/BRO/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 67.05, "basis": "Earnings hold and the multiple stays near the 19.8x peer median [RA,P]; this matches the fair-value bear of 67.05 rather than the 72.46 base, because Q2 organic revenue fell 0.7% (GlobeNewsWire release in the fact sheet) and ROIC is still falling (9.5% TTM [RA])."},
    "bear": {"probability": 0.30, "target_price_12m": 54.0, "basis": "Q3 confirms the organic decline and debt/EBITDA stays near 3.45x [RA], so the stock retests its 53.81 52-week low [HI], below the mechanical bear given the Altman Z of 1.80 [ST]; probability raised 0.05 for the macro overlay's small bear tilt on rising real yields and HY spreads (research/BRO/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
