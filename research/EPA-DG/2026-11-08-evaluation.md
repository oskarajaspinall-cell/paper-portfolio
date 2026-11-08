# Evaluation: Vinci SA (EPA:DG) — 2026-11-08
## Bear case
The stock fell 16.4% over six months and trades 9.1% below its 200-day average while reported results were reaffirmed [Certain]. Nothing in the research explains the de-rating [Certain]. The likeliest cause is French concession politics (toll-tax or concession-term risk), which the note could not test from primary sources [Guessing]. Toll-road concessions have finite lives. A mechanical DCF that capitalises today's concession FCF into perpetuity overstates value, so the base fair value of 327.83 EUR is not credible [Likely]. Leverage is rising again, net debt/EBITDA 2.02x from 1.80x in FY2025, and Altman Z is 1.13 [Certain]. Piotroski F is 5 [Certain]. The segment and geographic mix is [data unavailable], so country risk is unverified (overlay) [Certain]. Rolling ROIC is flat at 10.3%, below its 2-year high of 10.7% [Certain]. This is a steady business, not an improving one [Likely].

## Bull case
Every earnings multiple is cheap against Vinci's own history. EV/EBITDA is 6.6x, below its 5y minimum of 7.3x, P/E is 12.4x (5y median 13.6x) and the FCF yield is 14.96% [Certain]. The reverse DCF implies -18.3% revenue growth, yet Q3 revenue growth accelerated, the backlog expanded and 2026 guidance was reaffirmed (Q3 transcript) [Likely]. The last 12 months show no deterioration: operating margin +0.4pp, FCF margin +0.7pp and ROCE at its 2-year high of 12.5% [Certain]. Shares fell 1.32% YoY on buybacks [Certain]. Inflation-linked concessions are a moat [Likely]. Even the EV/EBITDA leg alone gives a bear value of 119.91 and a base of 141.07 EUR, both above the 111.60 price [Certain]. Macro is context only (overlay) [Likely].

## Decision
```json
{
  "ticker": "EPA:DG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A stable-return concessions and contracting group trades below its own 5-year EV/EBITDA minimum, but an unexplained six-month de-rating, finite concession lives and untested French regulatory risk leave the skew good rather than compelling.",
  "rationale": "The stock is cheap on its own history and the fundamentals are flat-to-up, but the research cannot explain the de-rating. The mechanical DCF overstates finite concession cash flows, and the expected value on the EV/EBITDA leg only modestly beats the price. That is conviction 3, so AVOID. Re-research at a P/E near its 5y low.",
  "price_at_decision": 111.60,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-DG/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9% (10.3% now; 5y peak 11.5%), showing concession or contracting returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 11% (12.3% now), reversing most of the five-year expansion from 9.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 9% (12.2% now), showing concession cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 2.7x (2.02x TTM now), showing leverage is rebuilding toward FY2021 levels.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 141.07, "basis": "EV/EBITDA recovers to the level of the fact sheet's EV/EBITDA-leg base fair value of 141.07 EUR as Q3 growth and backlog expansion (Q3 transcript) are confirmed; set below the blended base of 327.83 because the DCF capitalises finite concession FCF."},
    "base": {"probability": 0.45, "target_price_12m": 122.0, "basis": "Fundamentals stay flat, with ROIC 10.3% and operating margin 12.3% [RA-T, IS-T], and P/E re-rates partway from 12.4x toward its 5y median of 13.6x [RA]; well below the mechanical base because concession lives are finite."},
    "bear": {"probability": 0.30, "target_price_12m": 100.0, "basis": "The unexplained six-month fall of 16.4% [HI] proves to be French concession or toll-tax risk, and P/E slips below its 5y low of 11.5x [RA] with leverage at 2.02x and Altman Z at 1.13 [ST]; below the mechanical bear of 233.64 for the same finite-concession reason."}
  },
  "entry_price": 103.5,
  "entry_basis": "P/E back at its 5y low of 11.5x [RA] on TTM earnings, near the 52-week low of 104.25 [HI]; the valuation-file default (base 327.83 x 0.8) is above the price and rests on a DCF that overstates finite concessions.",
  "replaces": null,
  "replacement_reason": null
}
```
