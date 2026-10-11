# Evaluation: Crown Castle Inc. (CCI) — 2026-10-11
## Bear case
ROIC has been flat around 6% (5.7% in FY2021, 6.1% in FY2023), so the ROE rise to 37.2% comes from leverage, not from a better business [Certain]. Net debt/EBITDA rose from 7.39x to 10.62x in FY2025 and is 8.31x TTM. Management cites 6.3x, a gap the note could not reconcile [Certain]. Management itself says organic growth bottoms in 2026 [Likely]. The macro overlay is primary and tilts moderately toward bear. The 10y yield is 5.22% and real yields and high-yield (HY) spreads are still widening, which hits a highly levered REIT twice: through its discount rate and its refinancing cost [Certain]. The +15.6% jump on 2026-10-09 had no company catalyst [Certain]. It took the price back above the 50-day average just before the Q3 results on 2026-10-21, so it could fade [Guessing]. Margins and FCF conversion are [data unavailable] [Certain].
## Bull case
CCI is now a pure-play US tower operator. It is one of three in an effective oligopoly, with long carrier leases, annual escalators and high switching costs [Likely]. P/E of 32.5x and EV/EBITDA of 20.9x are both below their 5-year minimums, and 29% and 8% below the peer medians [Certain]. The FCF yield is 7.10% and the share count is broadly flat (+0.57%) [Certain]. Base fair value of 97.83 is 22.8% above the 79.64 close [Certain]. If yields and spreads roll over, the multiple could re-rate toward peers, and the September payrolls miss may mark that turn [Guessing]. Short interest is low at 2.31% [Certain]. Spectrum releases and 6G could re-accelerate tower leasing after 2026 [Likely].
## Decision
```json
{
  "ticker": "CCI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A pure-play US tower REIT at 5-year-low P/E and EV/EBITDA, but flat ~6% ROIC, 8.31x net debt/EBITDA with an unreconciled leverage figure, a self-declared 2026 growth trough and an adverse primary rate overlay leave the discount looking deserved for now.",
  "rationale": "The multiples are cheap, but the edge depends on rates turning and on leverage the data cannot confirm. ROIC has not improved, margins are unverifiable, management is changing and Q3 results are ten days away. The probability-weighted value sits below the price after the macro tilt. Good, not compelling: AVOID, and re-research at the entry price or after Q3 results.",
  "price_at_decision": 79.64,
  "price_date": "2026-10-09",
  "research_note": "research/CCI/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 5.7%, the FY2021 low, showing the towers-only model is not lifting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5.7}},
    {"text": "TTM ROIC rises above 6.9%, the FY2022 high, evidencing post-divestiture returns are genuinely improving (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 6.9}},
    {"text": "Debt/EBITDA rises back above 10.62x, the FY2025 level, showing deleveraging from fiber-sale proceeds has failed.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 10.62}},
    {"text": "Q3 2026 results (2026-10-21) or later releases show organic tower growth not improving after the 2026 trough management describes."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 97.83, "basis": "Rates roll over and P/AFFO re-rates to the fact sheet's base fair value of 97.83, not the 118.60 bull, because the macro overlay (research/CCI/2026-10-11-macro.md, primary, toward bear, moderate) caps the re-rating while real yields stay elevated."},
    "base": {"probability": 0.45, "target_price_12m": 81.6, "basis": "P/E holds near its 5y minimum of 33.3x [RA] on TTM earnings while organic growth bottoms in 2026 (BofA conference transcript, fact sheet headline), so the stock is roughly flat."},
    "bear": {"probability": 0.35, "target_price_12m": 62.23, "basis": "Real yields and HY spreads keep widening on 8.31x net debt/EBITDA [RA], pushing value to the fact sheet's bear fair value of 62.23; the macro overlay's moderate bear tilt (research/CCI/2026-10-11-macro.md) moved 0.10 of probability from bull to bear."}
  },
  "entry_price": 78.26,
  "entry_basis": "valuation file: base 97.83 x 0.8 = 78.26; at that margin of safety the same evidence, including the leverage and rate risk, would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
