# Evaluation: Valley National Bancorp (VLY) — 2026-11-16
## Bear case
Returns are sub-par: ROE is 9.4% TTM, below its FY2022 9.9%, and the five-year trend is falling (-1.9pp) [Certain]. Piotroski F is only 4 [Certain]. Credit is turning: net charge-offs were $37.1 million in Q3 2026 versus $14.6 million a year earlier [company-reported] [Certain]. The price has run +29.4% in 12 months and P/B of 1.0x sits at 79% of its 5y range, so the recovery is largely priced; an extended price risks a de-rating toward the 0.7x low if margin gains stall [Likely]. The macro overlay tilts toward bear (small): a flattening curve and a 2y about 1pp above fed funds pressure deposit costs; spread widening hits CRE credit [Likely]. Two acquisitions at once (Providence, Bluevine) add integration and deposit-transition risk from April 2027 [Likely]. Short interest is 11.05% of float and rising [Certain]. The base fair value of 12.03 is below the 14.34 close, though flagged unreliable [Certain].
## Bull case
Earnings are recovering: net margin rose to 35.8% TTM from 25.0% in FY2024 and ROE to 9.4% from 5.4% [Certain]. Management reports strong core deposit growth, lower expenses and an efficiency ratio below 50%, guiding to further margin expansion [Likely]. P/E of 11.4x is 12% below the peer median and P/B 19% below peers [Certain]. Bluevine brings low-cost digital deposits and is expected to be accretive to 2028 EPS [Likely]. The reverse DCF implies -1.6% year-1 revenue growth, a low bar [Certain]. The price is above its 200-day average with positive 6-month and 12-month relative strength versus SPY [Certain]. Share count is stable [Certain].
## Decision
```json
{
  "ticker": "VLY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROE is recovering over 1 and 3 years (5.4% FY2024 and 7.6% FY2023 to 9.4% TTM [RA]); only the 5-year endpoint versus FY2021 is lower.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Credit costs keep rising (net charge-offs $37.1m vs $14.6m a year earlier [company-reported]) while a flattening curve squeezes margin, stalling the ROE recovery the extended price already discounts and de-rating P/B toward its 0.7x low.",
    "veto": null
  },
  "thesis": "A sub-10% ROE regional bank in earnings recovery, cheap versus peers but no longer versus its own book-value history after a +29.4% run.",
  "rationale": "ROE of 9.4% is below a quality bar, there is no moat, credit costs are rising and the price already reflects the recovery. Peer discount and trend strength are not enough for high conviction; no position.",
  "price_at_decision": 14.34,
  "price_date": "2026-11-13",
  "research_note": "research/VLY/2026-11-16.md",
  "triggers": [
    {"text": "ROE falls below 7% TTM (recovery reverses).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "Net margin falls below 28% TTM.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Shares change YoY exceeds 5% (acquisition dilution).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}},
    {"text": "Quarterly net loan charge-offs exceed $50 million for two consecutive quarters (10-Q MD&A)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 16.0, "basis": "Margin expansion lifts ROE above 10% and P/B re-rates toward the peer median 1.3x [RA,P], above the 15.58 bull fair value [valuation]; probability trimmed for the macro overlay's small bear tilt (research/VLY/2026-11-16-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 14.0, "basis": "P/E holds at its 5y median 11.4x [RA] on roughly flat earnings as rising charge-offs offset margin gains; above the unreliable 12.03 base fair value because the P/B+ROE method uses a depressed history."},
    "bear": {"probability": 0.30, "target_price_12m": 10.0, "basis": "Curve flattening and CRE credit losses push P/B back toward its 5y low 0.7x [RA]; probability raised for the macro overlay's small bear tilt (research/VLY/2026-11-16-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3: the obstacle is sub-10% ROE and no moat, not price, so a lower price alone would not make it a BUY.",
  "replaces": null,
  "replacement_reason": null
}
```
