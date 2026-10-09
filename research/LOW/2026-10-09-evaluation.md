# Evaluation: Lowe's Companies, Inc. (LOW) — 2026-10-09
## Bear case
Returns on capital are falling fast: ROIC 38.5% (FY2022) to 22.4% TTM, ROCE 48.6% to 29.5% [RA] [Certain], because debt-funded Pro acquisitions grew invested capital faster than earnings [Likely]. Leverage climbed from 1.99x to 3.52x net debt/EBITDA (FY2026) [RA] [Certain], so buybacks are paused and shares fell only 0.44% YoY [ST] [Certain], removing the per-share support Home Depot still has [Likely]. Management sees no housing improvement in H2 [Likely], and the 10y Treasury rose to 5.28%, up 0.50pp in a month (macro overlay) [Certain], which squeezes both renovation demand and the DCF. The mechanical base fair value of $183.32 sits 2.9% below the $188.85 close, and the bear case is $131.22 [Certain]. The cheap multiples look like a correct re-rating for lower returns and higher leverage, not mispricing [Likely]. Price momentum is weak: -21.3% over 12 months, 18.0% below the 200-day [ST] [Certain].

## Bull case
Every multiple sits below its own 5-year minimum: P/E 16.0x vs 16.4x, EV/EBITDA 11.4x vs 12.2x, P/FCF 15.1x vs 19.1x. LOW also trades 19-32% below the peer median [RA] [Certain]. The FCF yield is 6.61% [ST], and FCF conversion is 105.4% and rising [CF,IS] [Certain]. Gross margin is steady at 33.0-33.5% and operating margin at 11.4% TTM [IS] [Certain], so the franchise is not breaking [Likely]. The reverse DCF implies only 2.9% year-1 revenue growth [Certain], a low bar if the housing market turns or the Pro acquisitions grow into their capital [Guessing]. Management cites share gains and positive comps [Likely]. Once deleveraging is done, buybacks can resume [Likely]. Short interest is low at 1.68% [ST] [Certain]. A fall in yields would lift both demand and the DCF toward the $210.30 bull case (macro overlay) [Guessing].

## Decision
```json
{
  "ticker": "LOW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale home-improvement franchise with stable gross margins trades below its own 5-year multiple range, but falling ROIC, higher leverage and paused buybacks leave the price close to base fair value with little margin of safety.",
  "rationale": "The discount to history and peers is real, but the base fair value of $183.32 is below the $188.85 close. ROIC is decaying and leverage is up at 3.52x, so buybacks are paused. Rising yields tilt risk toward the bear case. Good but not compelling, so conviction is 3: AVOID, and watch for entry near base fair value less the margin of safety.",
  "price_at_decision": 188.85,
  "price_date": "2026-10-08",
  "research_note": "research/LOW/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing the Pro acquisitions are structurally diluting returns rather than a transition cost.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 6%, under the FY2023 five-year low of 7.0%, showing cash generation cannot fund deleveraging and the dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "TTM gross margin falls below 32%, under the five-year 33.0-33.5% band, signalling tariff or promotional pressure is not being offset by private-brand and Pro mix.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 32}},
    {"text": "Net debt/EBITDA on the ratios page rises above the FY2026 level of 3.52x in the next fiscal year instead of falling, showing the deleveraging plan is failing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.22, "target_price_12m": 210.3, "basis": "Yields ease and housing stabilises, revenue beats the 2.9% reverse-DCF growth and the price reaches the fact sheet's bull fair value of 210.30 [IS,BS,CF,RA,ST,HI]; the probability is trimmed from 0.25 for the macro overlay's small tilt toward bear (research/LOW/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 183.32, "basis": "Flat housing as management guides, with ROIC still drifting lower (22.4% TTM [RA]), keeps the stock near the fact sheet's base fair value of 183.32, a DCF/P-E blend [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.28, "target_price_12m": 131.22, "basis": "Rising yields (10y up 0.50pp in a month per the macro overlay, research/LOW/2026-10-09-macro.md) prolong weak turnover, and with leverage at 3.52x [RA] the price falls to the bear fair value of 131.22 [IS,BS,CF,RA,ST,HI]; the probability is raised from 0.25 for that small tilt toward bear."}
  },
  "entry_price": 146.66,
  "entry_basis": "valuation file: base 183.32 x 0.8 (20% margin of safety); at that level the 6.61% FCF yield and the below-5y-minimum multiples [RA] would offset the ROIC decay and leverage risk enough to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
