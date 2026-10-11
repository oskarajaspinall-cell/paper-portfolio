# Evaluation: Gold Fields Limited (JSE:GFI) — 2026-10-11

## Bear case
Gold Fields is a price-taker with no pricing power, so its record returns (ROIC 41.7%, operating margin 53.1% TTM vs 31.6%-38.4% in FY2022-24 [IS,RA]) come from the gold price, not a durable edge [Likely]. The low P/E of 7.6x and P/FCF of 7.5x [RA] are peak-earnings multiples. P/B, the least cyclical measure, sits 24% above peers [RA] [Certain]. The normalized EV/EBITDA fair value is 26,410 ZAc base, 56.7% below the price [ST] [Certain]. The macro overlay flags a primary, accelerating headwind: real yields up 0.56pp in 3 months and a stronger dollar, which the stock's +9.7% 3-month bounce does not yet reflect (macro overlay) [Likely]. Management is pursuing Northern Star after its first proposal was rejected. A sweetened, partly stock-funded bid would re-lever the balance sheet or dilute holders just as the cycle may turn [Likely].

## Bull case
At current gold prices the cash generation is exceptional: FCF margin 38.9%, FCF conversion 100.7% and a 13.35% FCF yield [CF,ST] [Certain]. Net debt/EBITDA is only 0.06x [RA] [Certain]. Capital returns are real: a 35% FCF dividend policy plus $300m of H1 2026 buybacks (transcript) [Certain], with shares up only 0.22% YoY [ST] [Certain]. The stock is already 17.9% down over 12 months and 9.4% below its 50-day average [ST,HI]. If gold holds, P/E and P/FCF below their own 5-year minimums [RA] leave room to re-rate toward the bull fair value of 86,578 ZAc [ST] [Guessing]. Management also says a standalone path to 3m oz by 2030 is fully funded (transcript) [Likely].

## Decision
```json
{
  "ticker": "JSE:GFI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A best-in-class cash generator at peak gold-price margins whose cheap trailing multiples hide a normalized fair value far below the price, against a rising real-yield and dollar headwind and an open-ended Northern Star bid.",
  "rationale": "Trailing multiples are cheap only on peak, gold-driven earnings. The normalized base fair value sits 56.7% below the price, the primary macro tilt is toward the bear case, and a possible stock-funded Northern Star bid adds capital-allocation risk. We have no moat to underwrite through a cycle. This is good but not compelling, so we take no position.",
  "price_at_decision": 61028.00,
  "price_date": "2026-10-09",
  "research_note": "research/JSE-GFI/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below 40%, giving back most of the FY2025-TTM expansion (49.7% to 53.1%) toward the FY2021-24 31.6%-38.4% norm, confirming the returns were gold-price cyclicality.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 20%, cash conversion normalizing off its 38.9% TTM peak.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Debt/EBITDA rises above 1.0x, showing the Northern Star pursuit or bolt-ons are funded with real leverage (vs 0.06x net TTM).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Shares outstanding growth YoY exceeds 15%, i.e. a large stock-funded Northern Star deal (vs 0.22% today).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 86578, "basis": "Gold holds and the 53.1% operating margin [IS] persists, so the stock re-rates to the fact sheet's EV/EBITDA bull fair value of 86,578 ZAc [ST]. Probability is cut from 0.25 by the overlay's moderate tilt toward the bear case (research/JSE-GFI/2026-10-11-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 57000, "basis": "Operating margin eases from 53.1% TTM back toward the FY2025 49.7% [IS] at an unchanged 4.7x EV/EBITDA [RA]. The target sits above the 26,410 ZAc mechanical base fair value [ST] because a full reversion to through-cycle margins within 12 months is not evidenced while the 13.35% FCF yield [ST] funds dividends and buybacks."},
    "bear": {"probability": 0.35, "target_price_12m": 35000, "basis": "Rising real yields and the dollar push the gold price down, and margins revert toward the FY2021-24 31.6%-38.4% operating norm [IS], heading toward the 23,382-26,410 ZAc bear/base fair values [ST]. Probability is raised from 0.30 by the overlay's moderate tilt toward the bear case (research/JSE-GFI/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2, below the entry-watch threshold. The obstacle is peak-cycle gold-driven earnings with no moat, plus an unresolved Northern Star bid, not price; a discount to base fair value would itself rest on cyclical assumptions.",
  "replaces": null,
  "replacement_reason": null
}
```
