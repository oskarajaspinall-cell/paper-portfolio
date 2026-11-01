# Evaluation: Pool Corporation (POOL) — 2026-10-31
## Bear case
The 2026-10-22 reaction (+14.4% on 3.0x volume [HI]) followed results that only confirmed full-year guidance, with gross margin down and freight, mix and weak pool construction still headwinds [Likely]. This is relief from a depressed base, not a beat that forces estimates up, so drift has no fundamental engine [Likely]. The volatility stop below the reaction-day low (175.3 [HI]) sits far beneath the 205.95 close, and the honest first resistance, the 221.02 six-month high [HI], gives well under 1:1 reward against that risk [Certain]. A 2:1 target would need the price near the bull fair value 302.96, which the evidence does not support [Likely]. RSI 75.6 [ST] is overbought, the 50-day MA sits 13.6% below the 200-day [ST], and ROIC has fallen from 35.3% to 15.8% [RA] with net debt/EBITDA up to 2.22x [BS,IS] [Certain].

## Bull case
Sales growth accelerated in Q3 and the reaction held 135% of the jump [HI], a sign of real buying rather than a fade [Likely]. Short interest of 10.40% of float [ST] could fuel further squeezing [Guessing]. Valuation offers no crowding risk: P/E 19.0x vs a 32.1x peer median and EV/Sales and P/FCF below their 5-year minimums [RA], with a 6.01% FCF yield [ST] and shares down 3.20% YoY [ST] [Certain]. Price sits at base fair value 201.90, with bull 302.96 [Certain]. Macro is context only: calm credit and mostly maintenance demand [macro overlay] [Likely]. None of this repairs the reward:risk of the plan within eight weeks [Likely].

## Decision
```json
{
  "ticker": "POOL",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A post-earnings drift on results that only confirmed guidance lacks a fundamental engine, and the volatility stop is too far below the price for any evidence-supported target to reach 2:1.",
  "rationale": "The drift signal is real but rests on a relief rally, not a guidance raise. The ATR stop below the reaction-day low leaves the six-month high as the only supportable target, far short of 2:1; reaching 2:1 needs bull-case fair value. Overbought RSI and an unrepaired long-term trend add gap risk. No position.",
  "price_at_decision": 205.95,
  "price_date": "2026-10-30",
  "research_note": "research/POOL/2026-10-31.md",
  "exit_plan": {"target": 221.02, "stop": 173.45, "time_limit": "2026-12-26"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 284.98, "basis": "Sales acceleration persists and multiples recover toward their 5y medians (EV/EBITDA 21.2x [RA]), retaking the 52-week high 284.98 [HI], just below the bull fair value 302.96."},
    "base": {"probability": 0.5, "target_price_12m": 201.9, "basis": "Guidance is merely met with margins flat, so the price settles at the blended base fair value 201.90 (DCF 67% + EV/EBITDA 33%) where the reverse DCF already implies 8.0% year-1 growth."},
    "bear": {"probability": 0.25, "target_price_12m": 152.7, "basis": "Operating margin keeps sliding from 10.7% [IS] with leverage at 2.22x [BS,IS], retesting the 52-week low 152.70 [HI]; set above the mechanical bear 94.56 because the EV/EBITDA bear 183.52 and a 6.01% FCF yield [ST] support value."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
