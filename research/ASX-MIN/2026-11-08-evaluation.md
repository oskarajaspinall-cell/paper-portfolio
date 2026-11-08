# Evaluation: Mineral Resources Limited (ASX:MIN) — 2026-11-08
## Bear case
The low multiples sit on a cyclical recovery high, not a steady earnings base [Likely]. ROIC ran 13.1% (FY2022), 4.8% (FY2024), -7.8% (FY2025), then 12.3% (FY2026) [RA], and FCF margin was negative for four straight years before the 13.5% turn [CF] [Certain]. The rolling-12-month figures are all at their 2-year highs [RA-T], so the next move depends on iron ore and lithium prices rather than franchise strength [Likely]. Altman Z of 2.01 is in the grey zone, and net debt/EBITDA of 1.74x is still above the FY2022 0.76x [RA] [Certain]. Management is guiding to brownfield expansion and a copper push, which risks another capex-funded cash burn [Guessing]. Shares fell to a 41.62 low after the Q1 FY2027 release, cause unread [Guessing]. The base fair value of 50.84 gives little margin of safety, while the bear value of 27.79 [IS,RA] is far below. China exposure is unverified (macro overlay) [Certain].

## Bull case
Operating margin went from -14.8% to 22.7% and FCF margin from -58.8% to 13.5% in a year [IS-T,CF-T], with leverage falling from 7.15x to 1.74x [RA] [Certain]. Management reports record services and lithium volumes and all divisions beating guidance (H2 2026 transcript) [Likely]. P/E of 8.7x and EV/EBITDA of 5.5x are below their 5y minimums and well below peers [RA], with a 9.51% FCF yield [ST] [Certain]. Piotroski F of 7 confirms improving fundamentals [ST] [Certain]. The fee-based mining services arm cushions commodity swings [Likely]. Insiders own 10.77% [ST] [Certain]. If commodity prices hold, the de-rating after a -32.8% six-month fall [HI] could reverse sharply [Guessing].

## Decision
```json
{
  "ticker": "ASX:MIN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A diversified mining-services and iron ore/lithium producer is cheap on recovery-high earnings after de-leveraging, but its returns and cash flow are commodity-cycle driven with a long cash-burn history, so the low multiples may reflect peak rather than trough profits.",
  "rationale": "Multiples are below own-history lows, yet earnings sit at a cyclical recovery high, the base fair value offers little margin of safety and the bear value is far below the price. Expected value is near the price. Good but not compelling: AVOID, with an entry price at a margin of safety to base fair value.",
  "price_at_decision": 46.59,
  "price_date": "2026-11-06",
  "research_note": "research/ASX-MIN/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, showing the FY2026 recovery is fading with commodity prices.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM operating margin falls below 12%, about half the current 22.7%, signalling a commodity downturn is compressing earnings.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM FCF margin turns negative, showing a return to capex-funded cash burn.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA rises above 3.0x (1.74x TTM now), reversing the de-leveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 74.94, "basis": "Commodity prices hold and EV/EBITDA re-rates from 5.5x toward its 5y minimum of 7.2x [RA], taking the price back to its 52-week high of 74.94 [HI]; below the mechanical bull of 139.88 because that applies a mid-cycle multiple to recovery-high EBITDA."},
    "base": {"probability": 0.45, "target_price_12m": 50.84, "basis": "Margins hold near the TTM 22.7% [IS-T] and the stock reaches the mechanical EV/EBITDA base fair value of 50.84 [fact sheet Fair value]; macro is context only (research/ASX-MIN/2026-11-08-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 27.79, "basis": "Iron ore and lithium prices soften and EBITDA falls back toward the FY2024-FY2025 trough levels when operating margin was 6.0% and -14.8% [IS], matching the mechanical bear fair value of 27.79 [fact sheet Fair value]."}
  },
  "entry_price": 40.67,
  "entry_basis": "valuation file: base 50.84 x 0.8, a margin of safety against the cyclical earnings risk.",
  "replaces": null,
  "replacement_reason": null
}
```
