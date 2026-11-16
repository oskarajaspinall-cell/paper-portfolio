# Evaluation: China Merchants Bank Co., Ltd. (SHA:600036) — 2026-11-16
## Bear case
ROE drifted from 15.1% (FY2021) to 11.5% TTM [Certain], and the Q3 2026 call guides to continued NIM pressure and slower loan growth [Likely]. That looks like a lasting low-rate regime squeezing a deposit franchise, not a one-off [Likely]. The valuation is no bargain: P/E 7.4x sits above its 5y median of 7.1x and the peer median of 6.5x, and P/B 0.8x is at its own median but above peers at 0.4x [Certain]. The fair value is flagged unreliable (methods disagree 3.0x; the DDM gives 20.36) [Certain]. Valuation support leans on trend strength (price 8.9% above its 200-day average): if growth slows further, a de-rating toward the 5y P/B low of 0.6x is the risk [Likely]. China rate cuts and an unverified PBOC policy direction are live country risks (macro overlay) [Likely]. The FCF direction-change flag is deposit-flow noise for a bank [Likely].

## Bull case
China Merchants Bank has the strongest retail and wealth franchise among Chinese joint-stock banks, a narrow but real moat [Likely]. Net margin has risen from 45.2% to 50.8% TTM, so profitability per unit of revenue is intact; the ROE drift reflects a growing equity base and lower rates rather than credit losses [Likely]. Q3 2026 showed 9M income up and net profit up, with NPLs reported low [Likely]. Share count fell 0.63% YoY and management prioritises internally generated capital, so a dilutive raise looks unlikely [Likely]. The reverse DCF implies -6.8% year-1 revenue growth: the market prices a shrinking bank, while the P/B + ROE method gives a base of 55.74 [Certain]. Beta of 0.41 and a stable CNY (macro overlay) limit portfolio volatility [Certain]. Price is above both moving averages with 6-month momentum of +14.6% [Certain].

## Decision
```json
{
  "ticker": "SHA:600036",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 or 3 years; the 5-year ROE drift [RA] and the Q3 2026 guidance of continued NIM pressure (https://stockanalysis.com/quote/sha/600036/transcripts/741728-q3-2026/) are weighed in the bear case and key risk.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Further PBOC rate cuts compress NIM and push ROE toward 10%, de-rating P/B toward its 5y low from a price that leans on trend strength.",
    "veto": null
  },
  "thesis": "A best-in-class Chinese retail bank at an own-median P/B, but with ROE drifting lower under guided NIM pressure.",
  "rationale": "Quality is solid but ROE has drifted lower under guided NIM pressure, the valuation sits at its own median and above peers, and the fair value is flagged unreliable; valuation points come only from modest trend strength. Good but not compelling: no position.",
  "price_at_decision": 42.93,
  "price_date": "2026-11-13",
  "research_note": "research/SHA-600036/2026-11-16.md",
  "triggers": [
    {"text": "ROE (statistics) falls below 10%, showing the NIM squeeze is breaking the franchise's returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net margin (statistics profit margin) falls below 45%, signalling credit costs or fee erosion.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}},
    {"text": "Shares change YoY rises above +3%, i.e. a dilutive recapitalisation.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "Management states in a results release or call that NIM has stabilised and ROE has bottomed."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 55.74, "basis": "ROE holds near 11-12% and the market prices it at the P/B + ROE base fair value of 55.74 [IS,BS,RA], against a reverse DCF that implies shrinking revenue."},
    "base": {"probability": 0.5, "target_price_12m": 44.18, "basis": "P/B stays near its 5y median of 0.8x [RA] as guided NIM pressure (Q3 2026 call) offsets modest profit growth; roughly the P/B + ROE bear value of 44.18."},
    "bear": {"probability": 0.25, "target_price_12m": 32.2, "basis": "Further rate cuts push ROE lower and P/B de-rates toward its 5y low of 0.6x [RA]; the DDM at 20.36 shows downside the blended fair-value range ignores."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the base fair value less 20% is above today's price and the fair value is unreliable; the issue is ROE drifting lower under guided NIM pressure. A lower price alone would not change the decision; evidence that NIM and ROE have bottomed would.",
  "replaces": null,
  "replacement_reason": null
}
```
