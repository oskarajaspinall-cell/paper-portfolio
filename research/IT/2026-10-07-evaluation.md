# Evaluation: Gartner, Inc. (IT) — 2026-10-07

## Bear case
The de-rating below every 5-year multiple floor (P/E 17.1x vs 24.9x min) most likely reflects a structural question: whether generative AI erodes demand for paid research seats. Cheapness alone does not answer it [Likely]. The fundamentals already show slippage. Gross, operating and net margins all fell over five years (-1.1pp, -2.4pp, -5.5pp), and FCF margin of 19.9% is well below the FY2021 26.5% [Certain]. Consulting is shrinking and Conferences is growing, a lower-recurring mix [Certain]. Short interest is 14.53% of float and rose 13.6% month-on-month despite a 36.9% three-month rally. Informed money is adding to the bear side [Certain]. The fact sheet has no revenue or contract-value growth series, so the key thesis variable cannot be verified from stockanalysis.com [Certain]. ROE of 113.6% is inflated by buybacks shrinking equity, not by operating improvement [Likely].

## Bull case
This is a 36.0% ROIC subscription franchise with 166% FCF conversion and net debt/EBITDA of only 1.33x [Certain]. At 9.1x P/FCF it trades at an 11.04% FCF yield, 36% below its 5-year minimum and 62% below peers [Certain]. Buybacks cut the share count 8.83% YoY, so per-share value compounds even if the multiple never moves [Certain]. The Q2 2026 call reported accelerating contract value and raised full-year guidance, which suggests the AI-disruption fear may be overdone [Likely] (/stocks/it/transcripts/660529-q2-2026/). Altman Z of 4.10 and Piotroski F of 6 rule out distress [Certain]. If the market even partly reverts toward the 5-year floor multiples, the upside is large [Guessing].

## Decision
```json
{
  "ticker": "IT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 36% ROIC research-subscription franchise trades at an 11% FCF yield below every 5-year multiple floor, but declining margins, rising short interest and unverifiable growth leave the AI-disruption question unresolved.",
  "rationale": "Valuation and cash returns are compelling. But margins have declined on every line for five years, short interest is rising, and the fact sheet cannot confirm the contract-value growth the thesis rests on. That is good, not compelling: conviction 3, below the buy threshold. Three similar below-floor value buys are already pending, so cash is acceptable.",
  "price_at_decision": 184.92,
  "price_date": "2026-10-06",
  "research_note": "research/IT/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below its 5-year low of 25.4%, showing research pricing power is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25.4}},
    {"text": "TTM gross margin falls below 67%, showing the mix shift is spreading into core Research.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 67}},
    {"text": "TTM FCF margin falls below its 5-year low of 17.8% (FY2023), showing cash generation is structurally weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 17.8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 269, "basis": "AI-disruption fears fade on accelerating contract value (Q2 2026 transcript, OV), and P/E re-rates from 17.1x to its 5-year minimum of 24.9x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 201, "basis": "Multiples stay below their 5-year floors (P/E 17.1x [RA]), while the 8.83% YoY share-count reduction [ST], funded by the 11.04% FCF yield [ST], lifts per-share value."},
    "bear": {"probability": 0.30, "target_price_12m": 124, "basis": "Margin erosion continues (operating margin -2.4pp over 5y [IS]) and rising short interest of 14.53% [ST] is vindicated, so the shares retest the 52-week low of 124.25 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
