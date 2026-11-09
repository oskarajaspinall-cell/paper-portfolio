# Evaluation: Ingredion Incorporated (INGR) — 2026-11-09
## Bear case
The last year has reversed the five-year improvement: TTM ROIC 12.0% vs 15.0% a year earlier, operating margin 12.0% vs 14.6%, FCF margin 4.8% vs 7.6% [RA-T, IS-T, CF-T] [Certain]. Part of the cause is one-off (the Argo thermal event, the Colombia earthquake), but part is not: tapioca inflation, higher manufacturing costs and soft US/Canada demand forced a Q3 miss and a guidance cut, and Argo's recovery is slower than management expected [Likely]. FCF conversion is weak (61.6% TTM), so P/FCF 16.5x sits above its 11.6x median [CF, RA] [Certain]. The pending Tate & Lyle purchase lifts debt from about $1.8 billion to up to about $6.0 billion [company-reported], needs four antitrust clearances into 2H 2027, and a sold sterling put adds FX risk [Certain]; a weaker peso and real hit LATAM (macro overlay) [Likely]. A new CFO and rising short interest (7.55%) add execution doubt [Certain].
## Bull case
The direction change looks mostly temporary, not structural: the filing attributes it to a plant incident, an earthquake, raw-material costs and FX, while T&HS keeps growing volume and gaining share, so no lost franchise shows [Likely]. The balance sheet is intact today (net debt/EBITDA 0.72x [RA]), buybacks cut shares 2.81% and the dividend was raised [Certain]. The stock is cheap on depressed earnings: P/E 10.4x near its 9.6x 5y low and against peers at 15.2x; EV/EBITDA 6.0x and P/B 1.3x both below their 5y minimums [RA] [Certain]. The reverse DCF prices revenue falling 2.2% while guidance is flat sales [Likely]. If Argo normalises, margins can revert toward the FY2025 operating margin of 14.4% and the P/E toward its 13.0x median [Guessing]; Tate & Lyle would tilt the mix to higher-margin specialty [Guessing].
## Decision
```json
{
  "ticker": "INGR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A specialty-tilted ingredients maker with an intact balance sheet trades below its own 5-year EV/EBITDA and P/B minimums on earnings depressed by a largely temporary plant, weather and cost hit, but a guidance cut, weak cash conversion and a large debt-funded Tate & Lyle deal in regulatory limbo leave the skew balanced rather than compelling.",
  "rationale": "Re-judged afresh: the falling last 12 months looks mostly temporary (Argo, earthquake, costs), not structural, so direction is not the obstacle. But the recovery is unproven after a guidance cut, FCF conversion is weak, the leveraged Tate & Lyle deal dominates the next 18 months, and expected value sits only modestly above the price. Good, not compelling: no position.",
  "price_at_decision": 91.72,
  "price_date": "2026-11-06",
  "research_note": "research/INGR/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, showing the decline from 15.0% is a structural loss of returns rather than an Argo and cost one-off.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 11% after Argo is back in full production, showing the margin reset is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "Net debt/EBITDA rises above 3.0x pro forma after the Tate & Lyle financing, or the deal is financed on worse terms than disclosed.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "T&HS net sales volume in the 10-Q segment note turns negative year on year, breaking the specialty growth engine."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 120.0, "basis": "Argo normalises and operating margin reverts toward the FY2025 14.4% [IS] while P/E re-rates toward its 13.0x 5y median [RA], near the mechanical P/E bull of 122.03 [fact sheet Fair value]; well below the DCF bull of 324.17, which extrapolates too wide a margin range."},
    "base": {"probability": 0.5, "target_price_12m": 100.0, "basis": "Lowered 2026 guidance holds and margins stabilise near the TTM 12.0% [IS-T] with a partial EV/EBITDA recovery from 6.0x toward its 6.3x 5y minimum [RA]; below the mechanical base of 108.91 because deal limbo and the guidance cut (Q3 2026 transcript, /stocks/ingr/transcripts/723792-q3-2026/) cap the re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 80.0, "basis": "Argo and tapioca costs persist and Tate & Lyle leverage weighs, so P/E stays at its 9.6x 5y low [RA] on lower earnings, below the mechanical P/E bear of 84.64; far above the blended bear of 9.03, whose negative DCF ignores a business with net debt/EBITDA of 0.72x [RA]."}
  },
  "entry_price": 87.13,
  "entry_basis": "valuation file: base 108.91 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]). Price is the obstacle: at that margin of safety the same evidence (temporary-looking dip, intact balance sheet, unresolved deal and recovery risk) would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
