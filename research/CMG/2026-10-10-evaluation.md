# Evaluation: Chipotle Mexican Grill, Inc. (CMG) — 2026-10-10
## Bear case
The de-rating has a fundamental cause: Q2 2026 comps grew only 2.2% with traffic +1.0%, and management cites food-safety headwinds, a direct hit to the brand trust that underpins the moat [Certain]. Operating margin has slipped from 17.3% (FY2024) to 15.3% TTM while net debt/EBITDA rose from 1.36x to 2.08x [Certain]. Even after the fall, the price sits above the blended base fair value of $29.31, and the reverse DCF needs 21.7% year-1 revenue growth, far above what 2.2% comps plus unit growth deliver [Likely]. The FCF yield is only 3.92%, thin for a business whose growth is slowing [Certain]. The last close likely carries a premium from unconfirmed Starbucks takeover speculation that Starbucks has not confirmed and could fade [Guessing]. Q3 results land on Oct 28, an unresolved event risk, and rising real yields pressure the discount rate (macro overlay) [Likely].

## Bull case
CMG is one of the highest-quality restaurant franchises: ROIC rose from 14.8% to 22.7% over five years, ROE 49.6% TTM, Altman Z 6.53 [Certain]. Every multiple is below its own five-year minimum (P/E 29.3x vs min 31.9x; P/FCF 25.5x vs 33.8x) and P/E is 50% below peers [Certain]. Unit growth stays strong (100 openings in Q2 2026, 80 with Chipotlanes) and digital mix rose to 38.3% [Certain]. Buybacks cut the share count 3.92% YoY [Certain]. If food-safety concerns fade, comps and margins could recover, and the multiple could re-rate toward its historical range [Likely]. A Starbucks bid would be an extra option, though it is unconfirmed [Guessing].

## Decision
```json
{
  "ticker": "CMG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return fast-casual franchise de-rated to below its own 5-year multiple range, but traffic is weak on a food-safety trust problem and the price still sits above base fair value with only a 3.92% FCF yield.",
  "rationale": "Quality is real, but the stock is cheap only against its own rich history. The price is above base fair value ($29.31) and implies 21.7% growth against 2.2% comps. Margins are slipping, leverage is rising, Q3 results are due Oct 28, and takeover talk may be propping up the price. Good but not compelling, so no position.",
  "price_at_decision": 31.59,
  "price_date": "2026-10-09",
  "research_note": "research/CMG/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin falls below 14%, showing the food-safety and traffic softness is compressing profitability structurally (now 15.3%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 15%, giving up most of the five-year improvement from 14.8% to 22.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 3.0x, from 2.08x TTM, showing buybacks are being funded by leverage as earnings weaken.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "Comparable restaurant sales in the 10-Q or earnings release turn negative for two consecutive quarters, after +2.2% in Q2 2026."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 36.0, "basis": "Food-safety headwinds fade, traffic recovers and P/E re-rates to its 5y minimum of 31.9x [RA], above the $34.09 bull fair value [IS,BS,CF,RA,ST,HI] because unit growth and buybacks (-3.92% shares [ST]) raise EPS."},
    "base": {"probability": 0.45, "target_price_12m": 30.0, "basis": "Comps stay low single digit (Q2 2026 +2.2%, 10-Q https://www.sec.gov/Archives/edgar/data/1058090/000105809026000066/cmg-20260630.htm) and the price drifts toward the $29.31 base fair value [IS,BS,CF,RA,ST,HI] as takeover speculation fades."},
    "bear": {"probability": 0.30, "target_price_12m": 22.0, "basis": "The trust problem deepens, operating margin keeps falling from 15.3% [IS] and the price moves toward the $17.62 bear fair value [IS,BS,CF,RA,ST,HI]; bear probability raised by a small amount for rising real yields per the macro overlay (research/CMG/2026-10-10-macro.md, tilt toward bear, small)."}
  },
  "entry_price": 23.45,
  "entry_basis": "valuation file: base 29.31 x 0.8, a 20% margin of safety below the mechanical base value given the unresolved traffic trend.",
  "replaces": null,
  "replacement_reason": null
}
```
