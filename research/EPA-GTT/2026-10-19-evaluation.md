# Evaluation: Gaztransport & Technigaz SA (EPA:GTT) — 2026-10-19
## Bear case
GTT is a superb business priced at a cyclical peak. Operating margin of 70.1% TTM and ROE of 79.6% are five-year highs (IS, RA) [Certain], earned on royalties tied to the LNG-carrier new-build cycle, which turns [Likely]. A below-median P/E (17.7x vs 22.0x 5y median, RA) is normal for a cyclical at peak profitability, so it is not clear evidence of mispricing [Likely]. ROIC has more than halved from 310.8% (FY2023) to 144.8% TTM, the net cash cushion narrowed from -1.16x to -0.52x net debt/EBITDA, and Piotroski F is only 5 (RA, ST) [Certain]. The mechanical EV/EBITDA value of 141.15 EUR sits well below the 211.60 close; only the DCF leg, which capitalises peak margins, lifts base fair value to 263.54 [Certain]. Chinese shipyards building more carriers could back a rival containment technology [Guessing].
## Bull case
A near-monopoly licensor with gross margin of 96.8%, FCF margin of 57.0% and FCF conversion of 102.9% TTM (IS, CF) [Certain] trades at 17.7x P/E, below its 5y median and at a discount to peers' 27.8x (RA) [Certain]. Record order intake and confirmed 2026 guidance (https://stockanalysis.com/quote/epa/GTT/transcripts/548715-q2-2026/) give multi-year revenue visibility, because royalties are recognised over vessel construction [Likely]. The reverse DCF implies only 6.2% year-one revenue growth, which looks low against that order momentum [Likely]. Net cash, beta 0.42 and an Altman Z of 11.88 (ST) limit balance-sheet risk [Certain]. If the market re-rates GTT toward its 22.0x median P/E, the stock reaches the mechanical base fair value of 263.54 EUR [Likely].
## Decision
```json
{
  "ticker": "EPA:GTT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An exceptional, net-cash LNG containment licensor whose below-median multiples mostly reflect record, cyclically elevated margins rather than clear mispricing.",
  "rationale": "Quality is outstanding and the order book gives visibility, but margins and returns sit at cyclical highs, the EV/EBITDA fair value is below the price and only the peak-margin DCF supports upside. Probability-weighted return near zero: good but not compelling. Cash is acceptable; re-research at a P/E near its 5y low.",
  "price_at_decision": 211.60,
  "price_date": "2026-10-16",
  "research_note": "research/EPA-GTT/2026-10-19.md",
  "triggers": [
    {"text": "TTM gross margin falls below 90% (96.8% now), showing royalty economics are eroding.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 90}},
    {"text": "TTM operating margin falls below 49%, under the FY2022 five-year low of 49.5%, showing licensing pricing pressure or a falling order cycle.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 49}},
    {"text": "TTM ROIC falls below 60% (144.8% now), signalling competitive or pricing pressure on licence fees.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "Annual revenue (income statement) declines year on year in two consecutive fiscal years, showing the order book running down faster than new orders replace it."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 263, "basis": "P/E re-rates to its 22.0x 5y median [RA] on TTM earnings as record order intake (Q2 2026 transcript, /quote/epa/GTT/transcripts/548715-q2-2026/) extends the cycle, matching base fair value 263.54; the 408.83 bull value capitalises peak margins and is not credited."},
    "base": {"probability": 0.5, "target_price_12m": 220, "basis": "P/E holds near 17.7x [RA] with modest earnings growth under confirmed 2026 guidance [OV]; below the 263.54 base fair value because its EV/EBITDA leg (141.15) is under the price and the DCF leg extrapolates a 70.1% operating margin [IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 150, "basis": "The market looks past peak margins and the multiple derates toward the 5y low P/E of 13.7x [RA] on lower earnings, near the mechanical bear fair value of 147.43."}
  },
  "entry_price": 163.78,
  "entry_basis": "P/E back at its 5y low of 13.7x [RA] on TTM earnings (211.60 / 17.7 x 13.7): peak-cycle risk then priced in; preferred to base 263.54 x 0.8, which sits at the current price and would ignore the cyclical-peak concern.",
  "replaces": null,
  "replacement_reason": null
}
```
