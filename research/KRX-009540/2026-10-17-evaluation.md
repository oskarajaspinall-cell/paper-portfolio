# Evaluation: HD Korea Shipbuilding & Offshore Engineering (KRX:009540) — 2026-10-17
## Bear case
Shipbuilding is a textbook cycle, and a low P/E at peak margins usually signals peak earnings, not value [Likely]. Operating margin went from -9.0% (FY2021) to 15.5% TTM, and ROIC from 31.0% (FY2025) to 44.0% TTM. The note itself treats TTM as a possible peak [Likely]. FX is one of three margin drivers management cites, and it can reverse [Likely] (macro overlay). The stock is down 38.0% over 12 months, from a 6-month high of 488,000 to 265,000, and trades -23.2% below its 50-day average with no earnings reaction or company news to explain it. The market may be pricing order-cycle or pricing risk the fact sheet doesn't show [Guessing]. This is an intermediate holding company with listed subsidiaries, so consolidated margins and multiples may overstate what accrues to its shareholders [Guessing]. Altman Z is 2.36 (grey zone), FCF conversion is lumpy, and capital-return data is [data unavailable] [Certain].
## Bull case
Every multiple is below its 5-year minimum and far below peers: P/E 5.4x vs a 5y minimum of 13.3x and peer median 27.1x, EV/EBITDA 2.2x, P/FCF 4.0x, FCF yield 25.11% [Certain]. The balance sheet is net cash (-1.77x net debt/EBITDA) and Piotroski F is 7 [Certain]. Management credits the margin step-up to vessel pricing, productivity and a mix shift to gas carriers, with order intake on target each recent quarter [Likely] (transcripts Q1/Q2 2026). Multi-year order books give visibility on revenue [Likely]. The naval/defense links (HII, Palantir) add a second franchise [Likely]. Continued dollar strength supports the KRW margin [Likely] (macro overlay, small tilt toward bull). Even the EV/EBITDA method's bear fair value of 284,157.99 sits above the price [Certain].
## Decision
```json
{
  "ticker": "KRX:009540",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash shipbuilder at peak-cycle returns trades far below its own 5-year and peer multiples, but the unexplained price collapse and cyclical margin risk leave the durability of TTM earnings unproven.",
  "rationale": "Cheap on every multiple, but shipbuilding multiples are lowest at peak margins, the holding-company structure clouds attributable earnings, and the steep drawdown has no explanation in the evidence. That is good but not compelling. Q3 2026 results (around Nov 13, 2026) are the test of whether the margin is structural; cash is acceptable until then.",
  "price_at_decision": 265000.00,
  "price_date": "2026-10-16",
  "research_note": "research/KRX-009540/2026-10-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8%, showing the margin upcycle is reversing toward FY2024-type levels (5.6%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 15%, showing returns are reverting from the 44.0% TTM peak faster than any thesis assumes.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 5%, showing milestone cash collection is no longer sustaining recent levels.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Q3 2026 results (around Nov 13, 2026) hold operating margin at or above the 15.5% TTM level with order intake on target, which would support raising conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 494500, "basis": "Margins hold and P/E re-rates toward its 5y minimum of 13.3x [RA], retaking the 52-week high [HI]; probability raised slightly for the macro overlay's small tilt toward bull (dollar strength sustaining the FX margin driver, research/KRX-009540/2026-10-17-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 284158, "basis": "Margins ease back toward FY2025 levels (ROIC 31.0% [RA]) and the stock settles near the EV/EBITDA method's bear fair value of 284,157.99 [fact sheet]; well below the blended base fair value because that DCF extrapolates peak TTM margins, which the note treats as a ceiling."},
    "bear": {"probability": 0.30, "target_price_12m": 140201, "basis": "Cycle turns and operating margin reverts toward FY2024's 5.6% [IS], in line with the blended bear fair value of 140,201.08 [fact sheet]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the multiples are already at extremes. What's missing is evidence that the TTM margin is structural rather than a cyclical peak, plus an explanation for the drawdown. A lower price on the same evidence would not raise conviction; the Q3 2026 results will.",
  "replaces": null,
  "replacement_reason": null
}
```
