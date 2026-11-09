# Evaluation: Orient Securities Company Limited (SHA:600958) — 2026-11-09
## Bear case
Returns are poor and the business is commoditised. ROE is 7.0% TTM against 8.6% in FY2021, and ROIC is 2.0% [Certain]. Brokers have no durable pricing power [Likely]. The operating margin of 47.9% TTM, up from 30.2%, reflects a strong A-share turnover cycle, so earnings look near a cyclical peak and the 12.2x P/E flatters [Likely]. On peers it is not cheap: P/E is above the 9.4x peer median and P/B is in line at 0.8x [Certain]. On the Direction change, FCF margin fell from 71.9% to 33.7% over the last 12 months [Certain]. For a broker that swing comes from the trading book and working capital, not lost share: noise, not a structural break, but FCF can't anchor value [Likely]. The mechanical base fair value of 5.71 sits below the price [Certain]. State-led consolidation (the reported buyout) and the cross-border trading crackdown add integration, dilution and regulatory risk [Likely].

## Bull case
The stock trades below its own 5-year minimum P/E (16.0x) and P/B (0.9x), at 0.8x book [Certain]. Margins have risen to their 2-year area, with operating margin up 5.0pp in the last year [Certain]. The P/E-method fair value of 12.05 sits above the price [Certain]. Beijing-backed consolidation could make Orient a scale winner, with assets enlarged by the buyout [Guessing]. The FCF yield is 7.51% [Certain]. A sustained recovery in A-share turnover would lift ROE further [Guessing]. The macro overlay finds CNY stable and rates as context only [Certain].

## Decision
```json
{
  "ticker": "SHA:600958",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The only falling metric, FCF margin (71.9% to 33.7% TTM [CF-T]), swings with the broker's trading book and working capital (-0.9% FY2025, 112.8% FY2022 [CF]); ROIC is flat and operating margin is rising [RA-T, IS-T], so this is not lost share or a broken model.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Earnings sit on a cyclical high in A-share turnover (operating margin 47.9% vs 30.2% FY2021 [IS]); a turnover downturn, or regulation such as the cross-border trading crackdown, would cut ROE back toward the 3.5% FY2023 level [RA].",
    "veto": null
  },
  "thesis": "A commoditised onshore-China broker with single-digit ROE looks cheap only against its own history and on cyclically high margins, and is not cheap against peers.",
  "rationale": "ROE of 7.0% is below the quality bar, there is no moat, and earnings are cyclically elevated. It is cheap against its own history but not against peers, and the mechanical fair value is below the price. Conviction is below the buy bar, so AVOID. Low quality, not price, is the obstacle.",
  "price_at_decision": 8.38,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-600958/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE on the statistics page rises above 10% and holds there, showing returns have structurally improved beyond the cycle.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "TTM operating margin falls below 35%, showing the cyclical earnings boost is unwinding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "Shares outstanding rise more than 5% year on year through deal-related issuance.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 12.05, "basis": "A turnover recovery and consolidation re-rate earnings toward the P/E-method base fair value of 12.05 [fact sheet valuation file]."},
    "base": {"probability": 0.45, "target_price_12m": 8.38, "basis": "P/B stays in line with the 0.8x peer median [RA] as ROE holds near 7.0% [RA], so the price is flat."},
    "bear": {"probability": 0.3, "target_price_12m": 5.71, "basis": "Turnover fades from cyclically high margins [IS] and the price falls to the FCFE/DCF base fair value of 5.71 [fact sheet valuation file]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: low ROE, no moat and cyclical earnings would not change at a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```
