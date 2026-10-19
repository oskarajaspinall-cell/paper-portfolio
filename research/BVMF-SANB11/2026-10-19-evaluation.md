# Evaluation: Banco Santander (Brasil) S.A. (SANB11) — 2026-10-19
## Bear case
Returns are falling, not cyclical noise: ROE has dropped from 14.7% (FY2021) to 11.2% TTM and net margin from 33.1% to 28.7% [Certain] [RA, IS]. Management's shift to secured and high-income lending structurally lowers spreads, so the FY2021 return level is unlikely to come back soon [Likely] (https://stockanalysis.com/quote/bvmf/SANB11/transcripts/545723-q2-2026/). The P/B discount to peers (0.8x vs 1.1x) matches that ROE gap, so it is not a clear mispricing [Likely]. Piotroski F-score is only 4, capital ratios are [data unavailable], and the parent controls most of the float (institutions 2.8%), which brings minority and liquidity risk [Likely] [ST]. Results come out on Oct 28, 2026 with Q2 already showing higher credit costs [Likely] (https://www.marketbeat.com/instant-alerts/banco-santander-brasil-q2-earnings-call-highlights-2026-07-29/). The price trend is negative: below both the 50-day and the 200-day averages [Certain] [ST, HI].

## Bull case
The stock is cheap on its own history: P/E 7.7x sits near the bottom of its 5y range (6.6x-12.7x) and P/B 0.8x is close to its 5y low of 0.7x [Certain] [RA]. Base fair value of 33.91 BRL is above the 28.37 close, and the reverse DCF implies -5.8% year-1 revenue growth, a lot of pessimism [Certain] (fact sheet Fair value). Q2 ROAE of 12.5% was above the TTM ROE, which hints that the de-risked book is stabilising [Guessing] (https://stockanalysis.com/quote/bvmf/SANB11/transcripts/545723-q2-2026/). Shares change of 0.22% means no dilution, and management signals a return to its historical payout once earnings normalise [Likely]. Low beta (0.14) helps diversification, although that probably reflects the thin float [Guessing] [ST].

## Decision
```json
{
  "ticker": "BVMF:SANB11",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cheap Brazilian bank whose discount mostly reflects a structural fall in ROE from its mix shift to lower-spread secured lending, with no visible catalyst for a re-rating.",
  "rationale": "The valuation is undemanding, but ROE and margins are still falling, capital ratios can't be checked and results are due within weeks. The P/B discount to peers is explained by the lower returns. Good but not compelling, so conviction is 3 and the decision is AVOID; it is worth revisiting at a deeper margin of safety.",
  "price_at_decision": 28.37,
  "price_date": "2026-10-16",
  "research_note": "research/BVMF-SANB11/2026-10-19.md",
  "triggers": [
    {"text": "ROE (statistics) rises above 14%, showing the de-risked book earns peer-level returns (bullish change of mind)", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 14}},
    {"text": "ROE (statistics) falls below 8%, worse than the FY2023 trough of 8.4%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "Net (profit) margin falls below 24%, below the FY2023 level of 24.3%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 24}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 38.02, "basis": "ROE stabilises with Q2 ROAE of 12.5% (transcript) and P/B re-rates toward the peer median of 1.1x [RA], in line with the P/B+ROE bull value of 38.02 (fact sheet Fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 31.63, "basis": "ROE holds around the TTM 11.2% [RA] and P/B drifts toward its 5y median of 1.0x, matching the primary P/B+ROE base value of 31.63; this is below the blended 33.91 because the FCFE leg relies on volatile bank cash flows [CF]."},
    "bear": {"probability": 0.3, "target_price_12m": 23.30, "basis": "Credit costs keep rising and ROE heads back toward the FY2023 8.4% trough [RA], with P/B returning to its 5y low of 0.7x, in line with the blended bear fair value of 23.30."}
  },
  "entry_price": 27.13,
  "entry_basis": "valuation file: base 33.91 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
