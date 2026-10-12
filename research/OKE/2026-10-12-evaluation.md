# Evaluation: ONEOK, Inc. (OKE) — 2026-10-12
## Bear case
Returns are eroding: ROIC fell from 9.8% (FY21) to 8.4% TTM and ROE from 24.9% to 16.3% [Certain] [RA]. Cash quality is weakening: FCF conversion fell from 123.3% to 79.5% and FCF margin to 7.4% [Certain] [CF,IS]. The balance sheet is stretched: net debt/EBITDA is 4.28x with an Altman Z of 1.55 [Certain] [RA,ST]. Shares rose 4.61% YoY [Certain] [ST]. Growth now comes from acquisitions funded by Apollo equity that ranks ahead of common shareholders, so integration risk stays with them [Likely] (transcript). The 10y yield is 5.22% and real yields and HY spreads both rose over the past 3 months, which raises the cost of capital for a leveraged bond proxy [Certain] (macro overlay). On P/FCF the stock is not cheap: 19.5x sits at the 84th percentile of its 5y range [Certain] [RA].

## Bull case
OKE trades at a discount to its own history and its peers: 15.5x P/E against a 17.1x 5y median, and 11.7x EV/EBITDA against a 14.2x peer median [Certain] [RA,P:*]. Fee-based pipelines are natural monopolies [Likely] (oneok.com). The reverse DCF implies only 3.3% year-1 revenue growth [Certain] (fact sheet). Brazos doubles Midland processing capacity, and management guides leverage down to 3.25x with year-1 synergies [Likely] (transcript). Base fair value is 104.43, which is +16.3% [Certain] (fact sheet). Margins are higher than in FY21 (operating +1.6pp) [Certain] [IS].

## Decision
```json
{
  "ticker": "OKE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A fee-based midstream network trading below its own and peer multiples, but with falling ROIC, weakening cash conversion, 4.28x leverage and dilutive, acquisition-led growth, so the modest +16.3% base upside does not make it compelling.",
  "rationale": "The discount to peers and history is real. But it comes with falling returns, FCF conversion down to 79.5%, 4.61% dilution, Apollo equity that ranks ahead of common shareholders, and rising real yields. The expected return across the scenarios is only low single digits. Good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 89.80,
  "price_date": "2026-10-09",
  "research_note": "research/OKE/2026-10-12.md",
  "triggers": [
    {"text": "TTM net debt/EBITDA falls below 3.92x (the FY2022 5y low), proving the Apollo-funded deleveraging is delivered.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 3.92}},
    {"text": "TTM ROIC rises back above 9.8% (FY2021 level), showing the Brazos acquisition is accretive to returns rather than dilutive.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.8}},
    {"text": "TTM FCF margin recovers above 11.2% (FY2021 level), showing cash conversion has stopped deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 11.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 110.0, "basis": "Brazos synergies and deleveraging re-rate P/E toward its 5y max of 19.3x on TTM EPS [RA], close to the fact sheet's 104.43 base fair value; the 343.10 mechanical bull case is ignored as an extreme extrapolation; probability trimmed for the macro overlay's small tilt toward bear."},
    "base": {"probability": 0.45, "target_price_12m": 95.0, "basis": "P/E drifts part of the way back toward its 5y median of 17.1x [RA], held back by falling ROIC (8.4% TTM [RA]) and the senior Apollo claim (note); sits below the 104.43 base fair value because the 5.22% risk-free rate and rising spreads (macro overlay, small tilt toward bear) cap the re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 72.0, "basis": "Integration slips and rates keep rising, so P/E falls below its 5y min of 13.6x [RA] on pressured earnings with 4.28x leverage [RA], in line with the 70.73 bear fair value; probability raised for the macro overlay's tilt toward bear."}
  },
  "entry_price": 83.54,
  "entry_basis": "valuation file research/OKE/2026-10-12-valuation.md: base 104.43 x 0.8 (20% margin of safety) [IS,BS,CF,RA]; at that price the same evidence would give enough upside to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
