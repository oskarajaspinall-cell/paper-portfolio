# Evaluation: Zoetis Inc. (ZTS) — 2026-11-16
## Bear case
Companion animal, the profit engine, is losing ground: the Q3 10-Q cites softer demand, a more competitive landscape, dermatology pressure, generics on Convenia and Cerenia and lower Librela sales [Certain]. Q3 revenue fell 1% and management is planning cautiously for 2027 on fewer vet visits [Likely]. Every multiple sits below its own 5-year minimum because the market is pricing a lasting growth reset, not a dip [Likely]; the DCF base of 87.23 is barely above the 83.82 close, and the fair value is flagged unreliable [Certain]. Rolling ROIC is -0.5pp and FCF margin -0.7pp on the year, and ROCE is 2.9pp below its 2-year high [Certain]. Leverage has climbed from 1.03x to 1.92x net debt/EBITDA as buybacks run ahead of flat sales [Certain], leaving less cushion if the downturn persists [Likely]. The price is 8.2% below its 200-day average with a -30.8% 12-month change: no trend support [Certain].
## Bull case
The franchise still earns elite returns: ROIC 26.4%, operating margin 37.9% (flat-to-up on the year), gross margin 71.6%, FCF margin 23.5% [Certain]. The ROCE gap to its high and the small ROIC dip reflect restructuring and the PetMedix R&D write-off, not margin erosion [Likely]. Q3 beat and full-year EPS guidance was raised to $6.25-$6.35 [Likely]; livestock and diagnostics grew [Likely]. Cytopoint Plus, USDA-licensed on 2026-11-11, gives dermatology a 75-day defence [Certain]. At P/E 14.1x, EV/EBITDA 10.4x and a 6.56% FCF yield, the price implies only 3.1% year-1 revenue growth [Certain], while the share count fell 5.45% in a year [Certain]. Beta 0.68 and Altman Z 5.43 mean low balance-sheet risk [Certain]. Macro is context only: the overlay sees company-specific drivers (research/ZTS/2026-11-16-macro.md) [Likely].
## Decision
```json
{
  "ticker": "ZTS",
  "decision": "TRIM",
  "position_type": "CORE",
  "conviction": 3,
  "new_evidence": {"type": "method_change", "text": "The 2026-11-08 HOLD at conviction 4 predates the 2026-11-09 scorecard; the scorecard now sets conviction 3 on the same fundamentals."},
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists no falling metric over 1 or 3 years; rolling ROIC and FCF margin are flat and operating margin held at 37.9% vs 37.6% a year earlier [IS-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Companion-animal share loss (dermatology competition, Librela, Convenia/Cerenia generics) turns into falling total revenue and margins in 2027, as the cautious 2027 planning suggests.",
    "veto": null
  },
  "thesis": "A high-return animal-health franchise whose margins remain intact despite companion-animal share loss trades below its own 5-year minimum multiples, pricing near-stagnation that growing livestock and diagnostics and raised EPS guidance do not show.",
  "rationale": "Quality and cash returns are intact and the price sits below every own-history multiple floor, but companion-animal competition is real, the fair value is unreliable and the DCF base offers little cushion. Scorecard conviction 3 with the thesis intact: keep the position, trimmed to the smaller conviction-3 size under the sizing rules.",
  "price_at_decision": 83.82,
  "price_date": "2026-11-13",
  "research_note": "research/ZTS/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2023 5-year low of 35.9%, showing competition is eroding profitability, not just growth.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35.9}},
    {"text": "TTM gross margin falls below the FY2022 5-year low of 69.7%, signalling structural loss of pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 69.7}},
    {"text": "TTM ROIC falls below 22%, a clear break below the five-year range, showing the moat's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "Companion-animal revenue declines for two further consecutive quarters with dermatology share loss cited in the 10-Q MD&A, or 2027 guidance implies a total revenue decline."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 121.97, "basis": "Cytopoint Plus stabilises dermatology and growth beats the 3.1% the reverse DCF implies, so the price reaches the blended base fair value of 121.97 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 92.0, "basis": "Margins hold near 37.9% [IS] with flat sales; the price moves modestly above the DCF base of 87.23 [fact sheet Fair value] as buybacks shrink the share count, weighting the DCF since the blend is flagged unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 70.0, "basis": "2027 guidance implies falling companion-animal sales (Reuters 2026-11-05 headline in fact sheet) and the price retests the 52-week low of 68.77 [HI], near the bear fair value of 73.54 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: valuation already scores a discount to its own 5-year floors; the gap to conviction 4 is the companion-animal competition risk and an unreliable fair value, so a lower price alone would not change the decision. Re-check on 2027 guidance.",
  "replaces": null,
  "replacement_reason": null
}
```
