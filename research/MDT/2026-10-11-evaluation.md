# Evaluation: Medtronic plc (MDT) — 2026-10-11
## Bear case
Medtronic is cheap because its returns are falling, not because the market is ignoring it. Over five years gross margin fell 3.0pp to 65.3%, operating margin 1.6pp, net margin 2.7pp and FCF margin 3.9pp [Certain] [IS,CF]. At 8.6%, TTM ROIC is roughly the CAPM cost of equity implied by a 5.22% risk-free rate, so growth creates little value [Likely] [RA]. Net debt/EBITDA rose from 1.51x to 1.86x [Certain] [RA]. The mechanical base fair value of 84.90 sits 4.0% below the 88.48 close; the DCF alone gives 70.96 [Certain]. The reverse DCF needs 7.9% year-1 revenue growth, which is demanding for a business with this margin record [Likely]. The MiniMed split-off muddies the reported base until the 2026-11-17 results [Likely]. The stock is -25.3pp behind SPY over 12 months, and short interest rose 20.1% [Certain] [HI,ST].

## Bull case
MDT trades below its own 5-year minimum P/E (21.8x vs 22.3x) and P/FCF (18.5x vs 19.7x). It is cheaper than SYK, BSX, ABT and ZBH on every multiple, including P/E -14% and EV/EBITDA -12% [Certain] [RA,P]. FCF yield is 5.42%, FCF conversion stays above 100% at 117%, and Piotroski is 7 [Certain] [ST,CF]. The MiniMed split-off removes the diabetes unit and leaves cardiovascular, neuroscience and surgical franchises [Likely]. Category I CPT codes for Symplicity Spyral and Altaviva, plus the Affera Prism-2 clearance, open reimbursed growth in renal denervation and pulsed-field ablation [Likely] (prnewswire, 2026-10-01/09-30). A re-rating toward the 27.8x median P/E would drive the P/E-method value to 112.79 [Certain]. Beta of 0.57 limits drawdowns [Certain] [ST].

## Decision
```json
{
  "ticker": "MDT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale medtech now at the bottom of its own and peers' multiple ranges, but with five years of margin and ROIC erosion that the discount largely reflects, leaving price near base fair value with no margin of safety.",
  "rationale": "The stock is cheap on multiples, but the quality trend is negative: every margin and ROIC are falling and leverage is rising. Price sits above the 84.90 base fair value, and the probability-weighted target is below the close. The post-split margin story is unproven until results on 2026-11-17. This is good but not compelling, so no position.",
  "price_at_decision": 88.48,
  "price_date": "2026-10-09",
  "research_note": "research/MDT/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin rises above 22%, above the FY2022 level of 21.6%, showing the post-MiniMed mix has reversed the five-year margin erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 22}},
    {"text": "TTM ROIC rises above 10%, clearly above the FY2022 level of 9.3% and the cost of equity, showing returns are re-expanding.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "TTM gross margin rises above 67%, recovering half the 3.0pp five-year decline and evidencing restored pricing/mix.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 67}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 102.0, "basis": "The fact sheet's bull fair value of 102.00 [IS,BS,CF,RA,ST,HI]: post-split margins rise and CPT-coded Spyral/Altaviva plus Affera drive growth, re-rating P/E from 21.8x toward its 27.8x 5y median [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 84.9, "basis": "The fact sheet's base fair value of 84.90 (DCF 67% + P/E 33%): margins stay near 20.1% operating [IS] and the multiples stay at the bottom of their 5y range."},
    "bear": {"probability": 0.25, "target_price_12m": 64.21, "basis": "The fact sheet's bear fair value of 64.21: margin erosion continues (gross -3.0pp over 5y [IS]) and net debt/EBITDA keeps rising [RA], so the market values MDT on the bear DCF."}
  },
  "entry_price": 67.92,
  "entry_basis": "valuation file: base 84.90 x 0.8 [IS,BS,CF,RA,ST,HI]. At that level the 5y-low multiples plus a 20% margin of safety would compensate for the eroding margin trend.",
  "replaces": null,
  "replacement_reason": null
}
```
