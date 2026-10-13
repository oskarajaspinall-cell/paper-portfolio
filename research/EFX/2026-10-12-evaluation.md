# Evaluation: Equifax Inc. (EFX) — 2026-10-12
## Bear case
Cheap multiples mask a business whose returns are falling: ROIC fell from 12.3% (FY2021) to 8.9% TTM, operating margin from 23.1% to 18.3%, gross margin from 60.5% to 55.5% [RA, IS] [Certain]. ROIC near 9% against a 5.22% risk-free rate and 1.34 beta leaves little spread over the cost of capital [Likely]. The mechanical DCF base is only 106.61, and the bear blend 64.22, because cash returns don't support the old 48.0x median P/E [Certain]. Mortgage volumes, the note's largest swing factor, depend on yields that the macro overlay shows rising +68bp in 3 months on a real-rate basis, with no cuts priced [Likely]. Net debt/EBITDA is still 2.75x while M&A continues [Certain]. Q3 results on Oct 20 add binary risk, and negative 12-month relative strength (-54.9pp vs SPY) shows no sign of the market turning [Certain].

## Bull case
Equifax is one of three national credit bureaus, a regulatory-scale oligopoly with proprietary data, and the Work Number adds a hard-to-copy income/employment asset [Likely]. Every multiple sits below its 5-year minimum: EV/EBITDA 11.7x vs a 16.8x minimum, P/FCF 15.5x vs 23.4x [RA] [Certain]. EV/EBITDA is also 16% below the peer median [Certain]. FCF margin has recovered to 17.1% with 160% conversion, giving a 6.45% FCF yield [CF, ST] [Certain]. That cash is shrinking the share count (-2.88% YoY) and paying down debt (3.46x to 2.75x) [ST, BS] [Certain]. VantageScore 4.0 adoption at $1 pricing could take share in mortgage scoring [Likely]. Any mortgage recovery would bring high-incremental-margin volume back to a cost base already cut [Guessing]. The base fair value of 166.84 sits 14.4% above the price [Certain].

## Decision
```json
{
  "ticker": "EFX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A credit-bureau oligopoly trading below its own 5-year minimum multiples, but with five years of falling ROIC and margins and a mortgage recovery hostage to rising real yields, so the cheapness is not yet a high-conviction mispricing.",
  "rationale": "The valuation is genuinely depressed, but the quality trend is negative on every return and margin line. Base fair value is only +14.4%, the DCF alone sits below the price, and the macro tilt is moderately bearish with Q3 results on Oct 20. That is good but not compelling, so we hold cash and wait for a lower entry.",
  "price_at_decision": 145.78,
  "price_date": "2026-10-09",
  "research_note": "research/EFX/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 7%, a new multi-year low under the FY2023 trough of 7.6%, showing the moat is not earning its cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "TTM operating margin falls below 17%, under the FY2023 low of 18.4%, signalling erosion beyond mortgage cyclicality.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM FCF margin falls below 10%, around the FY2023 level of 9.8%, reversing the cash-conversion recovery.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 3.2x, reversing the FY2023-FY2025 deleveraging from 3.46x to 2.71x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 194.87, "basis": "Yields roll over and mortgage volumes recover, so the market pays the fact sheet's bull fair value 194.87 [IS,BS,CF,RA,ST,HI], still well below the 5y-minimum EV/EBITDA of 16.8x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 166.84, "basis": "FCF margin holds near 17.1% [CF,IS] and multiples partly normalise to the blended base fair value 166.84 [IS,BS,CF,RA,ST,HI], with the reverse-DCF's 9.8% implied growth roughly met."},
    "bear": {"probability": 0.35, "target_price_12m": 106.61, "basis": "Mortgage recovery is pushed out and returns keep sliding (ROIC 8.9% TTM, falling [RA]), so the price converges on the DCF-only base of 106.61 [IS,BS,CF,RA,ST]. We do not use the blended bear of 64.22, which comes from a negative DCF bear (-14.59). Bear probability is raised by 0.10 for the macro overlay's moderate bear tilt (real-yield back-up, research/EFX/2026-10-12-macro.md)."}
  },
  "entry_price": 133.47,
  "entry_basis": "valuation file: base 166.84 x 0.8 = 133.47; the 20% margin of safety would compensate for the falling-quality trend.",
  "replaces": null,
  "replacement_reason": null
}
```
