# Evaluation: Truist Financial Corporation (TFC) — 2026-10-09
## Bear case
The discount is earned, not mispriced. TTM ROE of 9.1% is below the 9.2% of FY2021, after -2.5% (FY23) and -0.1% (FY24) years [Certain] (RA). TFC's 0.9x P/B vs a 1.4x peer median simply reflects lower returns [Likely]. The fact sheet's base fair value of $47.05 is only +1.9% above the $46.18 close, so there is no margin of safety [Certain] (Fair value). Earnings quality has been erratic: FCF/NI was -789.6% in FY2023 and 44.9% in FY2024 [Certain] (CF,IS). The macro overlay tilts small toward bear. Real yields are up 0.61pp and HY spreads up 0.39pp over 3 months, which threatens the reaffirmed "modest NIM improvement" guidance before Q3 results on Oct 16 [Likely] (macro overlay). Piotroski F is only 4 [Certain] (ST). The stock trails SPY by 20.8pp over 6 months and has no catalyst until results [Certain] (HI).

## Bull case
At 10.5x P/E (26th percentile of its 5y range) and 0.9x P/B, the stock is cheap against peers at 11.7x and 1.4x [Certain] (RA, peers). FCF yield is 10.30% and shares fell 3.67% YoY, so cash is being returned [Certain] (ST). New CEO Mike Lyons is exiting non-core near-prime auto through a $5.5bn loan sale, and guidance was reaffirmed [Likely] (Reuters 2026-09-15; Barclays transcript). The 2s10s curve has steepened to +0.51pp, a NIM tailwind if credit holds [Likely] (macro overlay). If ROE closes the gap to peers, P/B could re-rate toward the $55.42 bull fair value (+20.0%) [Guessing]. The reverse DCF implies -5.5% revenue growth, which is a low bar [Certain] (Fair value).

## Decision
```json
{
  "ticker": "TFC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Truist is cheap on P/B and P/E but earns a sub-peer 9.1% ROE with a volatile record, and the base fair value sits only 1.9% above the price, so the discount looks deserved until the restructuring proves out.",
  "rationale": "Valuation is fair rather than cheap. The base fair value is +1.9% and the P/B discount matches the ROE gap. Execution is unproven and the macro tilt is toward bear before the Oct 16 results. Good but not compelling, so conviction 2 means no position. Cash is acceptable.",
  "price_at_decision": 46.18,
  "price_date": "2026-10-08",
  "research_note": "research/TFC/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above the FY2021 level of 9.2% and holds after the auto-loan sale, showing the clean-up is lifting returns toward peers (would reopen the case).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 9.2}},
    {"text": "TTM ROE falls below 8%, showing the restructuring is not restoring profitability (confirms AVOID).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin turns negative again, repeating the FY2023 pattern (confirms AVOID).", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 0}},
    {"text": "Net interest margin reported in Q3/Q4 2026 results improves in line with the reaffirmed 'modest NIM improvement' guidance despite higher real yields and credit spreads (would reopen the case)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 55.42, "basis": "NIM improves on the steeper curve and ROE lifts after the auto exit, so P/B re-rates toward the mechanical bull fair value of 55.42 (Fair value; macro overlay macro_bull); the probability is trimmed for the overlay's small tilt toward bear."},
    "base": {"probability": 0.45, "target_price_12m": 47.05, "basis": "ROE stays near its 9.1% TTM level [RA] and the stock converges on the blended base fair value of 47.05 (Fair value), roughly in line with today's price."},
    "bear": {"probability": 0.35, "target_price_12m": 37.69, "basis": "Funding costs and credit spreads squeeze NIM, as in the macro overlay's toward-bear tilt (moderately higher weight), and the stock falls to the P/B+ROE bear value of 37.69 (Fair value); this is above the 21.95 blended bear because the FCFE bear of -9.55 is not meaningful for a bank's cash flows."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
