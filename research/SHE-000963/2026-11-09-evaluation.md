# Evaluation: Huadong Medicine Co., Ltd (SHE:000963) — 2026-11-09
## Bear case
Returns are falling, not flat: TTM ROIC 14.6% vs 16.9% a year earlier and ROCE 14.9% vs 17.7%, both well below their 2-year highs; operating margin is 9.1% vs 10.4% [Certain] (RA-T, IS-T). The 5-year "rising" operating-margin read is contradicted by the last 12 months [Certain]. The cause is not established; China volume-based procurement and pricing pressure is the likeliest driver, which would be a permanent price cap rather than a cycle [Guessing]. The Q3 2026 report has not been read, so the latest quarter is unverified [Certain]. Cash backing is weak: FCF conversion 65.6% TTM, falling over five years, and P/FCF 21.5x is in line with peers, so it is cheap on earnings, not on cash [Certain]. The mechanical base fair value of 27.22 sits below the 27.72 price, the DCF says 15.78, and the reverse DCF needs 19.6% first-year growth; the fair value is flagged unreliable [Certain].

## Bull case
Every multiple sits below its own 5-year minimum: P/E 13.9x vs a 17.2x floor and 25.6x median, EV/EBITDA 9.2x vs 11.5x, EV/Sales 1.1x [Certain] (RA). Versus peers it is 23% cheaper on P/E and 41% on EV/EBITDA [Certain]. The balance sheet is net cash (-0.41x net debt/EBITDA) with Altman Z 5.00, so a pricing reset can be absorbed and the ADC and aesthetics pipeline funded [Certain] (ST). FY ROIC held 14-18% for five years and gross margin rose from 30.7% to 32.3%, so the franchise has survived earlier procurement rounds [Certain] (RA, IS). The FCF margin rose over the last year (5.1% vs 4.6%) [Certain] (CF-T). The P/E method gives a base of 50.11; if earnings stabilise, a partial re-rating towards the historical median is plausible [Guessing]. The share count is stable, so no dilution [Certain].

## Decision
```json
{
  "ticker": "SHE:000963",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "TTM ROIC 14.6% vs 16.9%, ROCE 14.9% vs 17.7% and operating margin 9.1% vs 10.4% a year earlier [RA-T, IS-T]; the note could not establish the cause and names China procurement/pricing pressure as likeliest [Guessing], a price cap rather than a guided reset, with no cited evidence of a temporary one-off.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "China drug procurement and pricing policy keeps compressing manufacturing margins, so returns keep sliding from the 2-year high and the low multiple proves a value trap.",
    "veto": null
  },
  "thesis": "A net-cash Chinese drug maker and distributor trades below its own 5-year minimum on every earnings multiple, but returns and margins are falling for an unexplained, possibly policy-driven reason and the stock is not cheap on free cash flow.",
  "rationale": "Cheap on earnings with a clean balance sheet, but ROIC and operating margin fell over the last year with no established temporary cause, FCF conversion is weak and P/FCF is in line with peers. The fair value is unreliable and the value blend shows no upside. Scorecard conviction 2: AVOID.",
  "price_at_decision": 27.72,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-000963/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, showing the decline from 16.9% is a lasting loss of returns rather than a reset.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 8%, under the FY2021 five-year low of 8.1%, showing pricing pressure is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 3.5%, close to the FY2022 low of 3.2%, showing working capital is absorbing the cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3.5}},
    {"text": "TTM gross margin falls below 30%, under the FY2021 five-year low of 30.7%, signalling procurement price cuts in the manufacturing segment.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.74, "basis": "Returns stabilise and the multiple recovers part of the way toward its 5y median P/E of 25.6x [RA], in line with the mechanical bull fair value 34.74 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 27.22, "basis": "Earnings drift with a soft operating margin (9.1% TTM [IS-T]) and the multiple stays below its 5y floor, matching the mechanical base fair value 27.22 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 17.41, "basis": "Procurement pressure keeps cutting ROIC (14.6% vs 16.9% [RA-T]) and the market values it on cash, near the DCF and the mechanical bear fair value 17.41 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the only obstacle: returns and operating margin are falling for an unexplained, possibly structural reason, so a lower price alone would not lift the same evidence to conviction 4; re-research after the cause is established from results.",
  "replaces": null,
  "replacement_reason": null
}
```
