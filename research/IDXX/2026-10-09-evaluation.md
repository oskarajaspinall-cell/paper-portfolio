# Evaluation: IDEXX Laboratories, Inc. (IDXX) — 2026-10-09
## Bear case
Cheap only against its own bubble-era history: P/E 36.6x and EV/EBITDA 25.5x are still 138-150% above the peer median [Certain]. The fact sheet's fair value is $353.57 base and even $371.07 bull, 28-31% below the $513.14 close, and the reverse DCF implies 33.3% year-1 revenue growth, far above the double-digit organic target, with management flagging a soft-visit headwind [Likely]. With a 1.55 beta, the 10y real yield up 0.61pp in three months raises the discount rate on exactly this kind of long-duration multiple (macro overlay, tilt toward bear, small) [Likely]. Momentum is broken: -12.0% below the 200-day, 50-day under the 200-day by 7.5%, and -33.2pp versus SPY over 12 months [Certain]. Zoetis and Mars/Antech are pushing into diagnostics [Likely], and the portfolio already owns ZTS in animal health [Certain]. Q3 results on Nov 2 are a near-term gap risk [Likely].

## Bull case
This is one of the highest-quality franchises in healthcare: ROIC 47.2%, ROCE 68.1%, gross margin rising to 62.4%, FCF conversion 110% and net debt/EBITDA 0.55x [Certain]. Over 80% of Companion Animal Group revenue is recurring, and instrument placements lock in reagent pull-through with high switching costs [Likely]. P/E, EV/EBITDA and P/FCF all sit below their 5y minimums after a -17.6% 12-month de-rating, while operating margin and FCF margin kept rising [Certain]. New platforms (inVue Dx, Cancer Dx, Catalyst proBNP) and AI workflow software (CoVetAI) lift utilisation per visit, supporting raised guidance [Likely]. Buybacks shrink the share count 2.40% a year [Certain]. The mechanical DCF uses a 5.28% risk-free rate and a high beta, which likely understates a business of this durability; the EV/Revenue method gives a $713.71 base [Likely].

## Decision
```json
{
  "ticker": "IDXX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class recurring vet-diagnostics franchise with 47% ROIC is de-rated to below its own 5-year multiples, but at 36.6x P/E, with a price implying 33% year-1 growth and rising real yields, the absolute valuation leaves no margin of safety.",
  "rationale": "The business is excellent and improving, but the price is still well above the DCF-led fair value range, even its bull case. Peer multiples sit far lower, momentum is negative, and macro tilts toward bear for a high-beta, long-duration stock. Earnings are also due Nov 2. Good but not compelling, and the portfolio already owns animal-health exposure via ZTS. Cash is acceptable.",
  "price_at_decision": 513.14,
  "price_date": "2026-10-08",
  "research_note": "research/IDXX/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 60%, reversing the 5-year rise to 62.4% and signalling pricing or mix pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}},
    {"text": "TTM ROIC falls below 35%, breaking five years of returns above 40%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM operating margin falls below 29%, giving up the 5-year expansion from the FY2021 level of 29.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 29}},
    {"text": "Companion Animal Group recurring revenue organic growth, per the quarterly earnings release, falls below high-single-digit for two consecutive quarters, against management's 10%+ target."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 624.0, "basis": "New platforms keep raising utilisation and real yields plateau (macro overlay), so the stock re-tests its 6-month high of 624.15 [HI], a P/E still below its 5y median of 51.0x [RA]; this sits between the DCF bull 198.34 and the EV/Revenue base 713.71, consistent with the EV/Revenue leg of the fair value."},
    "base": {"probability": 0.45, "target_price_12m": 560.0, "basis": "P/E holds near today's 36.6x [RA] while EPS compounds on rising margins (operating margin 32.2% TTM [IS]) and buybacks (-2.40% shares [ST]); above the 353.57 base fair value because the DCF leg's high discount rate (5.28% risk-free, beta 1.55 [ST]) understates a 47.2% ROIC franchise [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 400.0, "basis": "Real yields keep rising and a soft-visit Q3 drives further de-rating toward the 353.57 base fair value [fact sheet Fair value]; probability raised by the macro overlay's small tilt toward bear (research/IDXX/2026-10-09-macro.md), held above the 201.73 bear fair value because recurring revenue and 27.5% FCF margin [CF,IS] protect earnings."}
  },
  "entry_price": 282.86,
  "entry_basis": "valuation file: base 353.57 x 0.8 [IS,BS,CF,RA,ST,HI] (default 20% margin of safety); at that level the same quality evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
