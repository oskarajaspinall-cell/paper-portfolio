# Evaluation: Lennox International Inc. (LII) — 2026-10-09
## Bear case
The cheap multiples are a trap: P/E 16.1x and EV/EBITDA 12.4x sit below 5-year minimums because earnings are rolling over, not because the market is wrong [Likely]. ROIC has fallen from 44.7% (FY2024) to 26.4% TTM and ROCE to 33.8% [Certain]. Residential (59% of 1H26 sales) fell 7.3% YoY in Q2 and management has pushed recovery to 2027 after cutting EPS guidance [Certain]. The mechanical base fair value of $356.77 is below the $361.54 close, the reverse DCF still implies 11.6% year-1 revenue growth, and the bear value of $154.34 is -57.3% [Certain]. The macro overlay tilts moderately toward bear: the 10y yield at 5.28% works against residential financing and the discount rate [Likely]. Short interest is up 24.5% to 6.93%, and an open Sherman Act class action has no estimable loss range [Certain]. Q3 results on Oct 28 could bring another cut [Guessing].
## Bull case
Lennox's franchise is intact: gross margin of 33.3% and operating margin of 19.8% TTM are near five-year highs despite the residential slump [Certain]. Commercial grew 24% in Q2, so the mix is moving toward the steadier business [Certain]. FCF conversion of 93.7% TTM, a 5.89% FCF yield, buybacks (-1.82% shares) and a $1.36 quarterly dividend show cash generation holding up [Certain]. Net debt/EBITDA of 1.68x is manageable and Altman Z is 7.15 [Certain]. P/FCF of 17.0x against a 26.7x-42.1x 5-year range and a -49% EV/EBITDA discount to peers price in a long trough [Certain]. If residential replacement demand that has been deferred comes back in 2027, earnings and the multiple could both recover toward the EV/EBITDA-method value [Likely]. Lower yields would speed this up [Guessing].
## Decision
```json
{
  "ticker": "LII",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A high-margin HVAC franchise trades below its own 5-year multiple range, but falling returns, a residential downturn pushed out to 2027 and rising yields leave the price at, not below, through-cycle fair value.",
  "rationale": "Multiples look cheap, but the mechanical base fair value ($356.77) is below the $361.54 close. Downside to the bear value (-57.3%) dwarfs upside to the bull value (+8.6%). ROIC is falling, and the macro overlay tilts moderately toward bear. Q3 results on Oct 28 are a near-term risk. Good business, but not a compelling price: AVOID, cash preferred.",
  "price_at_decision": 361.54,
  "price_date": "2026-10-08",
  "research_note": "research/LII/2026-10-09.md",
  "triggers": [
    {"text": "Home Comfort Solutions (residential) segment net sales return to YoY growth in a 10-Q, showing the residential recovery is arriving earlier than management's 2027 timeline."},
    {"text": "TTM ROIC rises back above the FY2025 level of 34.2%, showing the decline in returns has reversed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 34.2}},
    {"text": "TTM FCF margin rises above the FY2024 level of 14.6%, showing cash generation is strengthening through the residential trough.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 14.6}}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 392.66, "basis": "Residential deferrals unwind in 2027 and margins hold near the 19.8% TTM operating margin [IS], so the stock reaches the mechanical bull fair value of $392.66 (factsheet Fair value); probability is reduced by the macro overlay's moderate bear tilt (research/LII/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 356.77, "basis": "Commercial growth offsets residential softness (Q2 residential -7.3%, commercial +24%, sec.gov 10-Q), and the stock settles at the blended base fair value of $356.77 (factsheet Fair value)."},
    "bear": {"probability": 0.35, "target_price_12m": 244.90, "basis": "Residential weakness runs past 2027 and ROIC keeps falling from 26.4% TTM [RA], so value converges on the best-method DCF base of $244.90 rather than the extreme $154.34 blended bear (factsheet Fair value); probability is raised by the macro overlay's moderate bear tilt from 5.28% 10y yields (research/LII/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
