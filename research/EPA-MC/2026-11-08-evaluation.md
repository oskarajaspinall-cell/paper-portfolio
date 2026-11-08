# Evaluation: LVMH Moët Hennessy - Louis Vuitton (EPA:MC) — 2026-11-08
## Bear case
Returns are still eroding: ROIC fell from 19.6% (FY2021) to 12.4% TTM and operating margin from 26.7% to 21.8% [RA,IS] [Certain]. The fact sheet's Direction change lines matter: ROIC and ROCE sit 4.2pp below their 2-year highs and operating margin 3.7pp below its 25.5% high [RA-T,IS-T] [Certain]. The last year is only flat (ROIC -0.8pp, operating margin +0.2pp), a pause, not a turn [Certain]. The driver is demand: fashion and leather goods organic sales fell in Q3 as Chinese consumers cut back (Bangkok Post, NY Post links in the fact sheet) [Likely], and Zenith job cuts point to weak watches [Likely]. The macro overlay finds China exposure material but unquantified; the risk is demand, not currency [Likely]. FCF margin of 18.0% is helped by working capital that may not repeat [Guessing]. No results until Jan 25, 2027, and the mechanical bear value of 334.48 sits below the October low [Certain].

## Bull case
The stock trades below its 5-year minimum on every multiple: P/E 18.6x vs 24.1x-30.4x, EV/EBITDA 9.8x vs 15.6x-20.7x, P/FCF 14.0x, a 7.13% FCF yield [RA,ST] [Certain]. The reverse DCF prices only 1.5% year-1 revenue growth fading to terminal [Certain]. Gross margin of 66.4% still shows real brand pricing power, and FCF conversion of 132.1% backs earnings with cash [IS,CF] [Certain]. Leverage is moderate at 1.24x net debt/EBITDA, with a small net buyback (shares -0.61% YoY) [ST] [Certain]. Base fair value is 476.05 and the P/E method alone gives 555.11 [Likely]. If leather goods stabilise, the de-rating reverses from a low base [Guessing].

## Decision
```json
{
  "ticker": "EPA:MC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A world-leading luxury brand portfolio with still-high gross margins trades below its own 5-year multiple ranges, but returns and margins have not stopped falling and leather goods demand is still declining, so cheapness alone does not yet make a compelling skew.",
  "rationale": "Valuation is undemanding, but quality is still eroding below its 2-year highs, Q3 leather goods sales fell, China exposure is unquantified and no results arrive before January. Base fair value upside is modest against a bear value well below the price: good but not compelling, so AVOID at conviction 3 with an entry price.",
  "price_at_decision": 408.75,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-MC/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20% (21.8% now), showing the margin reset is deepening rather than stabilising.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 11% (12.4% now), showing returns are still eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "TTM gross margin falls below 64% (66.4% now), signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 64}},
    {"text": "TTM FCF margin falls below 14% (18.0% now), showing the cash recovery was working-capital driven.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 555.11, "basis": "Leather goods demand stabilises and P/E re-rates toward the bottom of its 5y range of 24.1x [RA]: the fact sheet's P/E-method base value of 555.11, below the blended bull of 673.06 because returns are unlikely to regain the FY2021-23 levels within 12 months."},
    "base": {"probability": 0.45, "target_price_12m": 440.0, "basis": "Operating margin holds near the flat TTM 21.8% [IS-T] while multiples stay well below their 5y minimum [RA]; below the mechanical base of 476.05 because Q3 fashion and leather goods sales still fell (Bangkok Post link in the fact sheet) and no results arrive before Jan 25, 2027 [ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 334.48, "basis": "Chinese demand keeps falling and margins slide further from the 25.5% 2-year high [IS-T]: the mechanical bear fair value of 334.48 [fact sheet Fair value]; macro overlay is context only and does not move this."}
  },
  "entry_price": 380.84,
  "entry_basis": "valuation file: base 476.05 x 0.8 (20% margin of safety), near the October swing lows of 375.65-380.05 [HI].",
  "replaces": null,
  "replacement_reason": null
}
```
