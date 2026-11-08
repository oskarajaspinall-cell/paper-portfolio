# Evaluation: Sony Financial Group (TYO:8729) — 2026-11-08
## Bear case
The cheapness is mostly an artefact. P/FCF of 2.1x and an FCF yield of 46.55% reflect insurance float, not distributable cash [Likely]. The "below 5y min" readings on P/E and P/B come from a short, distorted spin-off history [Likely]. On the method that suits a life insurer, P/B + ROE, base fair value is 115.41 JPY, below the 141.20 close [Certain]. Against peers, P/E is 11.2x vs 9.9x and P/B 1.1x vs 1.2x, so there is no clear discount [Certain]. ROE swings between 6.3% and 18.4%, which points to market-linked earnings rather than a moat [Likely]. Solvency (ESR), JGB-rate sensitivity and the dividend are unverified, and those drive a life insurer's value [Guessing]. The macro overlay gives context weight only: the BoJ path is unchecked [Certain]. Results land on Nov 12, 2026, and the price is below both moving averages [Certain].
## Bull case
Returns are improving fast. ROIC rose from 0.3% in FY2022 to 7.4% in FY2026, and TTM is 16.0% against 11.4% a year earlier, a 2-year high [Certain]. The fact sheet prints no direction change [Certain]. The share count fell 6.17% YoY, so buybacks are returning capital [Certain]. Site-definition leverage fell from 5.58x in FY2024 to 2.98x TTM [Certain]. Beta is 0.04, so the stock barely tracks equity markets [Certain]. Sony-brand distribution and digital integration could support above-peer growth [Guessing]. At P/B 1.1x with TTM ROE of 11.8%, a sustained re-rating toward the P/B + ROE bull value of 190.36 JPY is possible if ROE holds [Likely]. Still, nothing in the data shows a durable edge, and the key solvency metrics are missing [Guessing].
## Decision
```json
{
  "ticker": "TYO:8729",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "An improving, buyback-funded Japanese life insurer that trades at roughly peer multiples, with the insurer-appropriate P/B + ROE fair value below the price and solvency data unverified.",
  "rationale": "ROIC momentum and buybacks are real, but the apparent cheapness is a float and spin-off artefact. The P/B + ROE base sits below the price, peers are no dearer, and solvency and rate sensitivity are unknown. Good but not compelling, so no position.",
  "price_at_decision": 141.20,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-8729/2026-11-08.md",
  "triggers": [
    {"text": "ROIC (ratios page, TTM) falls below 8%, reversing the return recovery", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "ROE (TTM) falls below 7%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "Shares change YoY turns positive: dilution replaces the buyback", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Net debt / EBITDA (site definition) rises above 4.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 190.36, "basis": "TTM ROIC of 16.0% [RA-T] and ROE of 11.8% [RA] hold, so the stock re-rates to the P/B + ROE bull value of 190.36 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 141.20, "basis": "P/B stays near 1.1x against a peer median of 1.2x [RA, peers], so the price holds; the blended base of 814.24 is set aside because its P/E leg rests on distorted spin-off history (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 102.38, "basis": "ROE reverts toward the 6.3%-6.7% years [RA] and the stock falls to the fact sheet's bear fair value of 102.38."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is unverified solvency, rate sensitivity and earnings stability, not price alone. A lower price would not change the decision without that evidence.",
  "replaces": null,
  "replacement_reason": null
}
```
