# Evaluation: Zoetis Inc. (ZTS) — 2026-11-23
## Bear case
Companion animal, two-thirds of revenue, is losing ground: the Q3 10-Q cites softer demand, "an increasingly competitive landscape", dermatology pressure, generics on Convenia and Cerenia and lower Librela sales [Certain]. Q3 revenue fell 1% and management is planning cautiously for 2027 [Certain]. Every multiple sits below its own 5-year minimum because the market prices a lasting growth reset [Likely]; the DCF base of 89.25 is only modestly above the 79.11 close and the blended fair value is flagged unreliable [Certain]. The Direction change lines matter: ROIC is 2.4pp and ROCE 2.9pp below their 2-year highs, and rolling FCF margin is -0.7pp [Certain]; if competition is the driver, that is structural [Guessing]. Net debt/EBITDA rose from 1.26x to 1.92x as buybacks outran flat sales [Certain]. The price is 12.5% below its 200-day average with a -32.4% 12-month change: no trend support [Certain].
## Bull case
Returns remain elite: ROIC 26.6%, operating margin 37.9% (flat on the year), gross margin 71.6%, FCF margin 23.5% [Certain]. The ROIC/ROCE gaps to their highs are small and both are flat to up over 3 years; restructuring, the PetMedix impairment and the recast fiscal calendar muddy comparisons rather than show margin erosion [Likely]. Livestock and diagnostics grew in Q3 [Likely]. Cytopoint Plus, USDA-licensed on 2026-11-11 with 75 days of itch relief, defends dermatology [Certain]. At P/E 13.4x, EV/EBITDA 9.9x and a 6.95% FCF yield, the price implies only 1.6% year-1 revenue growth [Certain], while the share count fell 5.45% in a year [Certain]. Altman Z 5.43 and beta 0.68 mean low balance-sheet risk [Certain]. Macro is context only (research/ZTS/2026-11-23-macro.md) [Likely].
## Decision
```json
{
  "ticker": "ZTS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "new_evidence": {"type": "new_information", "text": "Since the 2026-11-16 review: USDA licensed the Poulvac Procerta HVT-ND-ILT poultry vaccine on 2026-11-19 (https://www.businesswire.com/news/home/20261118551715/en/Zoetis-Receives-USDA-License-for-Poulvac%C2%AE-Procerta%C2%AE-HVT-ND-ILT-Vaccine-for-Chickens/), adding to the livestock offset, and the close fell from 83.82 to 79.11 on unchanged fundamentals, lifting the value-blend upside into the scorecard's hold band. The fundamentals themselves are unchanged."},
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Rolling ROIC is -0.4pp and FCF margin -0.7pp on the year, both marked flat; operating margin is 37.9% vs 37.6% a year earlier [IS-T]; ROIC and ROCE sit below 2-year highs but are flat to up over 3 years [RA-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Companion-animal share loss (dermatology competition, Librela, Convenia/Cerenia generics) turns into falling total revenue and margins in 2027, as the cautious 2027 planning suggests.",
    "veto": null
  },
  "thesis": "A high-return animal-health franchise with intact margins trades below its own 5-year minimum multiples, pricing near-stagnation, but companion-animal competition keeps the upside uncertain.",
  "rationale": "Quality and cash returns are intact and the price sits below every own-history multiple floor, but companion-animal competition is real, the fair value is unreliable and there is no trend support. The scorecard lands in the hold band, below the add threshold: keep the position at its current size, no ADD.",
  "price_at_decision": 79.11,
  "price_date": "2026-11-20",
  "research_note": "research/ZTS/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2023 5-year low of 35.9%, showing competition is eroding profitability, not just growth.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35.9}},
    {"text": "TTM gross margin falls below the FY2022 5-year low of 69.7%, signalling structural loss of pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 69.7}},
    {"text": "TTM ROIC falls below 22%, a clear break below the five-year range, showing the moat's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "Companion-animal revenue declines operationally for two further consecutive quarters with dermatology cited in the 10-Q MD&A, or 2027 guidance implies a total revenue decline."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 123.31, "basis": "Cytopoint Plus stabilises dermatology and growth beats the 1.6% the reverse DCF implies, so the price reaches the blended base fair value of 123.31 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 89.25, "basis": "Margins hold near 37.9% [IS] with flat sales and buybacks shrink the share count; the price moves to the DCF base of 89.25 [fact sheet Fair value], weighting the DCF since the blend is flagged unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 70.0, "basis": "2027 planning implies falling companion-animal sales (Reuters 2026-11-05 headline in fact sheet) and the price retests the 52-week low of 68.77 [HI], below the bear fair value of 74.38 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle to an ADD: every multiple already sits below its 5-year floor; the gap to the add threshold is companion-animal competition risk, an unreliable fair value and no trend support, so a lower price alone would not change the decision. Re-check on 2027 guidance.",
  "replaces": null,
  "replacement_reason": null
}
```
