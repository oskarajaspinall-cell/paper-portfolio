# Evaluation: S&P Global Inc. (SPGI) — 2026-10-11
## Bear case
The "cheap" signal is relative to a richly priced history, not to intrinsic value: the DCF/FCFE base fair value is $262.59, 35.6% below the $407.82 close, and the price sits near the bull case ($435.59) [Certain] (factsheet). The reverse DCF needs 19.5% year-1 revenue growth with margins already near multi-year highs (operating 43.0% TTM) [Certain]. The 10y Treasury at 5.22% (+68bp/3m) raises the discount rate and threatens bond issuance, the driver of Ratings transaction revenue, into the Oct 27 print [Likely] (macro overlay). The stock is in a downtrend: 50-day below 200-day by 5.3%, -31.1pp vs SPY over 12 months [Certain]. ROIC of 11.1% post-IHS Markit is ordinary for the price paid [Certain]. The Mobility spin-off's financial effect is not yet visible in the figures [Likely].

## Bull case
This is a toll-road franchise: NRSRO ratings and index lock-in, shown by Cboe's 25-year S&P 500 options licence extension to 2051 [Certain] (https://www.prnewswire.com/news-releases/cboe-and-sp-dow-jones-indices-sign-25-year-extension-of-exclusive-licensing-agreement-through-2051-302892397.html). Margins are recovering: operating 35.2% (FY2022) → 43.0% TTM, FCF conversion 113.2% [Certain] (factsheet). Every multiple is below its own 5-year minimum: P/E 24.8x vs 33.6x min, EV/EBITDA 16.2x vs 22.6x [Certain]. It is also at or below peers on most multiples [Certain]. Shares fell 2.79% YoY with leverage only 1.43x [Certain]. The P/E-based fair value ($551.67–$658.06) points to material upside [Certain]. Shedding Mobility should lift the group's mix [Likely].

## Decision
```json
{
  "ticker": "SPGI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class ratings and index franchise with recovering margins trades below its own 5-year multiple range, but its intrinsic DCF value is well below the price and rising yields threaten both the discount rate and Ratings issuance volumes.",
  "rationale": "Quality is clear but valuation evidence conflicts: multiples are below their own history, while the DCF base ($262.59) is 36% below price and the reverse DCF needs 19.5% growth. The macro tilt is moderately bearish and Q3 results land Oct 27. That is good but not compelling, so it is an AVOID at conviction 3. Cash is acceptable.",
  "price_at_decision": 407.82,
  "price_date": "2026-10-09",
  "research_note": "research/SPGI/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below 36.5%, under the FY2023 level of 36.6%, reversing the post-merger margin recovery.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 36.5}},
    {"text": "TTM FCF margin falls below 28%, under the FY2023 level of 28.5%, showing cash conversion is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.5x, above the FY2022 post-merger peak of 2.09x, so leverage rather than cash would be funding buybacks.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "A 10-Q/10-K or earnings release shows Ratings or Indices revenue declining year on year for two consecutive quarters, or a named loss of an index mandate or NRSRO share."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 493, "basis": "Yields plateau and issuance recovers (overlay macro_bull), so P/E re-rates from 24.8x to about 30x, still below its 5y minimum of 33.6x [RA]. This lands between the DCF bull ($435.59) and the P/E fair value ($551.67) and is still under the 52-week high of 552.25 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 420, "basis": "Multiples hold near 24.8x P/E (in line with the 25.8x peer median [RA,P]), while margin gains (operating 43.0% TTM [IS]) and 2.79% share shrinkage [ST] add modest EPS growth. That is close to the DCF bull ($435.59) and well above the DCF base, because the DCF ignores the franchise's lock-in."},
    "bear": {"probability": 0.30, "target_price_12m": 300, "basis": "The macro overlay (2026-10-11-macro.md, moderate tilt toward bear) moves 5pp from bull to bear. Yields extend from 5.22% and issuance softens into the Oct 27 print, compressing P/E to about 18x, toward the DCF base of $262.59 [factsheet] but above it given 113.2% FCF conversion [CF,IS]."}
  },
  "entry_price": 210.07,
  "entry_basis": "valuation file: base 262.59 x 0.8 [IS,BS,CF,RA,ST]. The owner default is used because no fact-sheet anchor reconciles the DCF-versus-multiples conflict; a re-research at that price would test whether the DCF's own-history assumptions still hold.",
  "replaces": null,
  "replacement_reason": null
}
```
