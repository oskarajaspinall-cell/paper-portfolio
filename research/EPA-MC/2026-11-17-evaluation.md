# Evaluation: LVMH Moët Hennessy - Louis Vuitton (EPA:MC) — 2026-11-17
## Bear case
Returns have stepped down, not dipped: ROIC fell from 19.6% (FY2021) to 12.4% TTM and operating margin from 26.7% to 21.8%; ROIC sits 4.2pp and operating margin 3.7pp below their 2-year highs [RA-T, IS-T] [Certain]. The last year is only flat, with no recovery yet [Certain]. China demand is weak and nine-month organic growth was 2% (Q3 transcript) [Likely]; if Chinese luxury spending has reset permanently, the 5-year multiples (P/E median 25.3x) are the wrong anchor and "below every 5y minimum" is a value trap [Guessing]. Rivals are cutting prices (Gucci, WSJ 2026-11-15), threatening the pricing power behind a 66.4% gross margin [Guessing]. The price is 12.2% below its 200-day average with negative 3/6/12-month momentum: no trend support [Certain]. Macro tilts small toward bear on rising real yields and a higher VIX (overlay) [Likely]. Mechanical bear value 327.27 is 19.0% below the 404.00 close [Certain].

## Bull case
This is a cyclical trough in an intact franchise: gross margin has held between 66.2% and 68.8% for five years, FCF margin is at its 2-year high of 18.0% and FCF conversion is 132.1% [IS, CF-T] [Certain]. Net debt/EBITDA of 1.24x and Altman Z 3.36 mean no balance-sheet stress [Certain]. The price implies only 2.2% year-1 revenue growth (reverse DCF), P/E 17.9x vs a 5y low of 24.1x and an FCF yield of 7.36%, so much of the China weakness is priced [Certain]. Europe, the US and Japan grew in Q3, and Wines & Spirits, Watches & Jewelry and Selective Retailing advanced [Likely]. A weaker euro against the yuan and dollar lifts translated sales (overlay) [Likely]. Base fair value 463.50 sits 14.7% above the close; buybacks trimmed shares 0.61% [Certain]. Louis Vuitton declining to follow price cuts signals pricing discipline [Guessing].

## Decision
```json
{
  "ticker": "EPA:MC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 or 3 years: the last 12 months are flat (operating margin +0.2pp, FCF margin +0.7pp to its 2-year high) [RA-T, IS-T, CF-T]. The earlier fall in ROIC and margin came with the luxury downturn and weak China demand (Q3 2026 transcript, https://stockanalysis.com/quote/epa/MC/transcripts/716218-q3-2026/), with gross margin at 66.4% and net debt/EBITDA 1.24x.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "Chinese luxury demand proves structurally lower and rival price cuts (WSJ 2026-11-15) erode pricing power, keeping ROIC stuck near 12.4% instead of recovering.",
    "veto": null
  },
  "thesis": "A wide-moat luxury group in a cyclical trough with an intact balance sheet and 7.36% FCF yield trades below every 5-year minimum multiple, but returns show no recovery yet and the price trend is down.",
  "rationale": "Python scorecard gives 3: quality and balance sheet are solid and the discount is real, but ROIC and margins sit well below their 2-year highs with no recovery yet, momentum is negative and macro tilts slightly bear. Good but not compelling: AVOID, with the entry price at base fair value less the margin of safety.",
  "price_at_decision": 404.00,
  "price_date": "2026-11-16",
  "research_note": "research/EPA-MC/2026-11-17.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, showing the decline from 19.6% is structural rather than a cyclical trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 19%, showing pricing power is eroding beyond the downturn.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 14%, showing the cash strength was a working-capital release.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) rises above 2.0x from 1.24x TTM."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 544.00, "basis": "China stabilises and P/E returns to its 5y minimum of 24.1x [RA] on TTM earnings, between base and bull fair value; probability trimmed for the small bear macro tilt (research/EPA-MC/2026-11-17-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 463.50, "basis": "Flat-to-low growth with margins holding (last-year direction flat [RA-T]) lets the multiple drift toward the mechanical base fair value of 463.50 [fact sheet fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 327.27, "basis": "Further China weakness and rival price cuts (WSJ 2026-11-15) push margins lower and the price to the mechanical bear value 327.27; probability raised for the small bear macro tilt (research/EPA-MC/2026-11-17-macro.md)."}
  },
  "entry_price": 393.98,
  "entry_basis": "valuation file: base 463.50 x 0.85"
}
```
