# Evaluation: Eli Lilly and Company (LLY) — 2026-10-09
## Bear case
The price already assumes the best outcome. The reverse DCF implies 37.6% year-1 revenue growth. Even the fact sheet's bull fair value ($1,126.00) is 3.7% below the $1,169.60 close, and the base ($508.24) is 56.5% below [Certain]. Cash backing is thin: FCF yield is 1.75%, P/FCF 57.3x, and FCF/NI is 68.1% against 108.5% in FY2021 [Certain]. LLY trades at a premium to peers on EV/EBITDA (+65%), EV/Sales (+117%) and P/FCF (+137%) [Certain]. Patent and data-protection expiries come quickly: Trulicity and US tirzepatide data protection in 2027, then Jardiance in 2029 (sec.gov 10-K) [Certain]. Compounded incretins and new oral GLP-1s threaten pricing [Likely]. Real yields rose 0.61pp in 3 months (macro overlay), which presses on a long-duration valuation [Likely]. The 3-month return lags SPY by 7.6pp [Certain].
## Bull case
This is a best-in-class franchise whose quality is still rising. TTM ROIC is 42.2%, operating margin 49.7% (+16.3pp in 5y) and gross margin 83.4% [Certain]. On earnings, LLY looks cheap against its own history: P/E of 39.3x and EV/EBITDA of 26.1x are both below their 5-year minimums, and P/E is 26% below the peer median [Certain]. The balance sheet is strong: net debt/EBITDA is 1.10x, Altman Z 6.55 and Piotroski 7 [Certain]. FCF margin has recovered from 2.3% (FY2023) to 22.8% TTM as capacity spending matures [Certain]. The pipeline keeps adding options, including Jaypirca's expanded label and orphan designation for olomorasib [Likely]. Beta is low at 0.45 [Certain]. If earnings keep compounding, P/E multiples can stay where they are while the share price rises [Guessing].
## Decision
```json
{
  "ticker": "LLY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "An exceptional, still-improving incretin franchise whose price already exceeds even the bull-case fair value and implies 37.6% year-1 revenue growth, at a 1.75% FCF yield, ahead of 2027 patent and data-protection expiries.",
  "rationale": "Quality is outstanding, but the core rule needs good business AND attractive valuation. Price sits above the bull fair value, FCF yield is 1.75%, and LLY trades at peer premiums on every cash-flow multiple. Low P/E against its own history reflects peak-growth earnings, not a margin of safety. Rising real yields add pressure. Cash is the better holding.",
  "price_at_decision": 1169.60,
  "price_date": "2026-10-08",
  "research_note": "research/LLY/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 78% (FY2022 level), signalling payer or compounded-incretin price pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "TTM ROIC falls below 30% (near the FY2023 level of 28.0%), showing incretin returns are being competed away.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 13.8% (FY2025 level), showing the cash-conversion recovery has stalled.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 13.8}},
    {"text": "Net debt/EBITDA rises above 2.0x, meaning the capacity build is debt-funded without a demand payoff.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1336, "basis": "Earnings keep compounding and P/E re-rates from 39.3x to its 5y minimum of 44.9x [RA] on TTM EPS [IS], above the fact sheet's bull fair value of 1,126.00 because the mechanical DCF caps growth well below the 37.6% the reverse DCF implies."},
    "base": {"probability": 0.45, "target_price_12m": 1126, "basis": "Growth is delivered but the 2027 Trulicity/tirzepatide data-protection expiries (sec.gov 10-K) cap the multiple, so the price settles at the fact sheet's bull fair value of 1,126.00 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.30, "target_price_12m": 595.38, "basis": "Pressure from compounded and oral GLP-1s brings the market down to the P/E-method base value of 595.38 [RA,IS], still above the blended base of 508.24; probability raised from 0.25 to 0.30 for the macro overlay's small tilt toward bear (DFII10 +0.61pp/3m, research/LLY/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
