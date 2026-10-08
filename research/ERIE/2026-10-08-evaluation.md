# Evaluation: Erie Indemnity Company (ERIE) — 2026-10-08
## Bear case
ERIE is cheap only against its own inflated history. At 19.8x P/E and 4.6x P/B it still trades at +129% and +127% premiums to P&C peers, and its 4.86% FCF yield is thin for a business whose fee rate already sits at the 25% cap [Certain]. Growth must therefore come entirely from Exchange premium volume, which management says is moderating, with lower retention [Likely]. The single customer is the Exchange, and Indemnity's own Board sets the fee against the policyholder-owners' capital needs; a weather-hit Exchange could pressure that rate [Likely]. Short interest of 9.5% of float is high for this kind of company, and the stock is down 31.1% over 12 months [Certain]. A de-rating toward peer multiples, or margins slipping back to FY2022 levels, would leave real downside [Guessing].

## Bull case
This is a capital-light fee monopoly over its only client ("no direct competition", 10-K) with no underwriting risk, negative net debt (-0.29x) and a 0.33 beta [Certain]. Returns and margins have risen for five years: ROIC from 21.4% to 27.4% and operating margin from 11.9% to 18.4%, with FCF conversion of 95.9% [Certain]. Every multiple sits below its 5-year minimum: P/E 19.8x vs a 26.8x low, EV/EBITDA 13.3x vs 17.9x [Certain]. Q1 and Q2 2026 showed better underwriting and higher net income, which supports fee sustainability [Likely]. If premium growth stabilises, part of the 5-year multiple could come back [Guessing].

## Decision
```json
{
  "ticker": "ERIE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, debt-free fee monopoly over the Erie Exchange trades below its own 5-year minimum multiples, but at a capped fee rate, moderating premium growth and a still-large premium to peers the de-rating looks more like normalisation than mispricing.",
  "rationale": "The quality is real, but the stock is only cheap against its own rich history. Its 4.86% FCF yield, +129% P/E premium to peers, 25% fee cap and slowing premium growth leave little margin of safety and no clear re-rating catalyst. Good but not compelling: conviction 3, so no position. Cash is acceptable.",
  "price_at_decision": 217.77,
  "price_date": "2026-10-07",
  "research_note": "research/ERIE/2026-10-08.md",
  "triggers": [
    {"text": "TTM net margin falls below 10% (TTM 14.0%), signalling fee-rate pressure or cost inflation.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "TTM ROE falls below 15% (TTM 24.8%), signalling the fee economics are deteriorating.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 10% (TTM 17.9%), signalling a material cut in the management fee rate below the 25% ceiling.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 294.76, "basis": "Premium growth stabilises and P/E re-rates from 19.8x to its 5-year minimum of 26.8x [RA] on flat TTM earnings [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 217.77, "basis": "P/E holds at 19.8x [RA] as margin gains (operating margin 18.4% TTM [IS]) offset moderating premium growth noted on the Q2 2026 call [OV]."},
    "bear": {"probability": 0.25, "target_price_12m": 163.33, "basis": "Net margin reverts from 14.0% TTM to the FY2022 level of 10.5% [IS] at an unchanged 19.8x P/E [RA], reflecting fee-rate pressure from a weather-hit Exchange (Bear case)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
