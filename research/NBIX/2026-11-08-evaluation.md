# Evaluation: Neurocrine Biosciences (NBIX) — 2026-11-08
## Bear case
At 164.63 the stock sits only +5.3% below its base fair value of 173.37, after a +13.4% jump on 3.2x volume following Q3 [Certain]. RSI is 69.4 and short interest rose 10.2% on the month, so the beat looks largely priced [Likely]. The multiples sit below their 5-year minimums, but those ranges were set in a higher-growth phase; the cheapness partly reflects concentration: INGREZZA is by far the largest product [company-reported] and management itself flags 2027 pricing pressure (transcript) [Likely]. The Direction change line shows ROIC 5.0pp below its 2-year high of 25.2%: it reflects the FY2025 trough and the Soleno purchase enlarging invested capital, and it threatens the thesis only if VYKAT XR does not earn its cost [Likely]. VYKAT XR now carries serious adverse-event reports in the 10-Q [company-reported], gross margin has fallen from 69.8% to 64.7%, and net cash has narrowed to -0.27x [Certain].

## Bull case
This is a high-return, net-cash franchise: TTM ROIC 20.2%, operating margin 26.6% (+6.0pp in a year) and FCF margin 28.1%, all rising on the rolling view [Certain]. Q3 revenue and EPS beat and INGREZZA 2026 guidance was raised, with all three products contributing [Likely]. P/E of 24.4x, EV/EBITDA of 15.3x and P/FCF of 16.0x are all below their 5-year minimums, with a 6.24% FCF yield [Certain]. CRENESSITY has no approved direct competitor in classic CAH, giving a second growth leg [Likely]. The reverse DCF implies 9.8% year-one revenue growth fading to terminal, a bar recent growth clears comfortably if INGREZZA pricing holds [Likely]. Macro is context only (research/NBIX/2026-11-08-macro.md).

## Decision
```json
{
  "ticker": "NBIX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, net-cash neuroscience drugmaker trades below its own 5-year multiple ranges, but after the post-Q3 jump the price sits close to base fair value while INGREZZA concentration, 2027 pricing pressure and VYKAT XR safety reports cap the skew.",
  "rationale": "Quality and cash generation are strong and improving, yet the price already sits near the mechanical base value after the earnings jump, and the expected value across scenarios is only modestly above it. Product concentration, guided 2027 pricing pressure and an unresolved VYKAT XR safety question make this good but not compelling: conviction 3, no position.",
  "price_at_decision": 164.63,
  "price_date": "2026-11-06",
  "research_note": "research/NBIX/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 58% (64.7% now), showing the acquired VYKAT XR and product mix are eroding unit economics.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "TTM ROIC falls below 15% (20.2% now), showing the Soleno acquisition is diluting returns rather than a temporary denominator effect.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 20% (28.1% now), showing pricing pressure is reaching cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "INGREZZA quarterly net sales (10-Q) fall year on year, or CRENESSITY quarterly net sales fall sequentially for two quarters, or a VYKAT XR label change is disclosed."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 215.0, "basis": "Raised INGREZZA guidance and CRENESSITY growth lift earnings while P/E re-rates from 24.4x toward its 5y minimum of 29.5x [RA]; below the mechanical bull of 365.44, which assumes growth well beyond the reverse-DCF 9.8% [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 175.0, "basis": "Margins hold near the TTM 26.6% operating and 28.1% FCF levels [IS-T, CF-T] and 2027 growth offsets pricing pressure as management guides (Q3 2026 transcript), in line with the base fair value of 173.37 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 120.0, "basis": "2027 INGREZZA pricing pressure plus a VYKAT XR safety label change (10-Q risk factor, research note section 6) send the stock back toward its 52-week low of 122.14 [HI]; above the mechanical bear of 63.94 because net cash and a 28.1% FCF margin [CF-T] limit downside."}
  },
  "entry_price": 138.7,
  "entry_basis": "valuation file: base 173.37 x 0.8; at that level the same evidence offers enough margin of safety against concentration and pricing risk for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
