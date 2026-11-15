# Evaluation: PharmaEssentia Corporation (TPE:6446) — 2026-11-15
## Bear case
This is a one-drug company: ropeginterferon alfa-2b carries the revenue, so any competitive, pricing or licensing setback hits all of it at once [Likely]. The 2025 ICC award went to licensee AOP Health, and nobody has checked what it costs commercially [Guessing]. The price is extended. P/E is 62.8x, at 82% of its 5y range, against a peer median of 19.0x. FCF yield is only 1.20%, and the price sits 45.4% above its 200-day average after a +206.2% year [Certain]. All of the valuation support comes from trend strength, not a discount: the base fair value of 1,137.23 is below the 1,380.00 close [Certain]. If growth slows or the ET indication disappoints, the multiple could fall back toward its 5y median of 51.7x or its 34.5x low, a de-rating even with margins intact [Likely]. FCF conversion of 75.6% trails net income [Certain]. The regional revenue split is unverified [Certain].
## Bull case
The business is working and getting better. TTM ROIC is 58.3% against 44.0% a year earlier. Operating margin is up +12.0pp to 40.3%, FCF margin is up +6.0pp to 27.9% and gross margin is 92.7%. None of these is falling, and the fact sheet prints no direction change [Certain]. The balance sheet is net cash (net debt/EBITDA -2.53x), with a Piotroski score of 7, an Altman Z of 25.46 and shares up only 0.35% YoY [Certain]. The FDA accepted an sBLA for essential thrombocythemia, a second indication that could lengthen the drug's growth runway [Likely]. Because earnings compounded so fast, EV/EBITDA (32%), P/FCF (44%) and EV/Sales (11%) sit low or mid in their own 5y ranges [Certain]. The Q3 2026 results reaction on 2026-11-06 held 229% of its jump, so the market is still absorbing improving numbers [Certain]. Patent and regulatory protection on a biologic gives a narrow moat [Likely].
## Decision
```json
{
  "ticker": "TPE:6446",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rising over 1 and 3 years [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "high", "key_risk_text": "Single-product concentration at an extended multiple (P/E 62.8x, 82% of its 5y range, price 45.4% above the 200-day): any slowdown or licensing setback would de-rate the stock sharply; likely enough to matter within 12 months.", "veto": null},
  "thesis": "A high-return, net-cash single-biologic company whose margins are still expanding, priced for continued growth.",
  "rationale": "Quality, direction and balance sheet are excellent, but valuation support comes only from trend strength, the base fair value is below the price, and a one-drug franchise at a 62.8x P/E carries a high de-rating risk. Good but not compelling at this price.",
  "price_at_decision": 1380.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-6446/2026-11-15.md",
  "triggers": [
    {"text": "ROIC TTM falls below 30%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Gross margin falls below 80%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "FCF margin TTM falls below 15%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Operating margin TTM falls below 25%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1645.00, "basis": "ET approval and further margin expansion (operating margin +12.0pp in a year [IS-T]) take the price back to its 52-week high [HI], above the mechanical bull of 1,517.24 because earnings are still growing."},
    "base": {"probability": 0.45, "target_price_12m": 1380.00, "basis": "Earnings growth offsets a P/E drift from 62.8x toward the 5y median 51.7x [RA]; above the mechanical base 1,137.23, which puts a median P/E on TTM EPS with no forward growth."},
    "bear": {"probability": 0.30, "target_price_12m": 757.21, "basis": "Growth stalls or the AOP licensing dispute bites, and P/E de-rates toward its 5y low of 34.5x [RA], matching the mechanical bear fair value."}
  },
  "entry_price": 909.78,
  "entry_basis": "valuation file: base 1137.23 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
