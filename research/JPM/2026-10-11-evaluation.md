# Evaluation: JPMorgan Chase & Co. (JPM) — 2026-10-11
## Bear case
The quality is real but already in the price. P/B of 2.5x sits above its entire 5y range (1.3x-2.4x) and 25% above the peer median of 2.0x; P/E of 14.3x is at the 74th percentile of its range and 8% above peers [Certain]. At 332.99 the stock is above even the mechanical bull fair value of 320.88, and the base fair value of 274.70 is 17.5% lower [Certain]. Net margin has drifted down 3.0pp over five years to 34.9% [Certain]. The macro overlay records a fresh fed funds hike and a 56bp rise in the 10y real yield in 3 months. That raises the cost of equity, and higher deposit costs could compress NIM as in 2022-23 [Likely]. A rich multiple leaves no cushion for that. Q3 results on Oct 13 are an event risk [Likely]. The stock trails SPY by 4-7pp over 3-12 months [Certain].

## Bull case
JPM is a best-in-class franchise. ROE is 17.8% TTM, above every fiscal year in the last five, and held 12.8% even at the FY2022 trough [Certain]. Shares fell 3.56% YoY, so buybacks compound per-share value [Certain]. Scale, deposit funding and capital barriers sustain a premium to peers [Likely]. Short interest of 0.91% and a 50-day MA 8.7% above the 200-day show a healthy uptrend that is cooling off (RSI 38.3, 4.9% below the 50-day) rather than breaking [Certain]. The reverse DCF implies only 3.9% year-1 growth, which is undemanding for a bank earning near-18% ROE [Likely]. The mechanical P/B+ROE method caps sustainable ROE and may understate a structurally higher-return franchise [Guessing].

## Decision
```json
{
  "ticker": "JPM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "JPM is a high-ROE, buyback-compounding franchise, but at a P/B above its own 5-year range and above the mechanical bull fair value, the price already discounts the quality while a renewed hiking cycle threatens NIM.",
  "rationale": "Quality is excellent, but valuation is the obstacle: P/B is above its 5y max and above peers, and the price exceeds the bull fair value. The probability-weighted 12-month value is below the current price once the overlay's moderate bear tilt is applied. That makes this good but not compelling, so conviction 3 and AVOID. The entry price is set at base fair value less a 20% margin of safety.",
  "price_at_decision": 332.99,
  "price_date": "2026-10-09",
  "research_note": "research/JPM/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROE falls below 13%, near the FY2022 five-year trough of 12.8%, showing returns are not structurally higher.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 13}},
    {"text": "TTM net margin falls below 30%, under the FY2022 low of 30.8%, extending the five-year downtrend into credit-cycle compression.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "Shares outstanding stop shrinking and turn to net issuance (YoY change above 0%), reversing the -3.56% buyback-driven reduction.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 367.92, "basis": "ROE holds near the 17.8% TTM high and buybacks continue (-3.56% shares [ST]), so P/E re-rates to its 5y max of 15.8x [RA] on TTM EPS (332.99/14.3). This is above the mechanical bull FV of 320.88 because the P/B+ROE method caps ROE."},
    "base": {"probability": 0.45, "target_price_12m": 307.38, "basis": "P/E converges to the 13.2x peer median [RA, P:BAC/WFC/GS/MS] on TTM EPS, between the base (274.70) and bull (320.88) fair values. Probability is shifted from bull toward base and bear per the macro overlay's moderate bear tilt (research/JPM/2026-10-11-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 256.15, "basis": "Continued hikes lift deposit costs and compress NIM, so P/E reverts to its 5y median of 11.0x [RA] on TTM EPS, near the base fair value of 274.70. Probability is raised for the macro overlay's moderate bear tilt (fed funds +25bp/1m, 10y real yield +56bp/3m; research/JPM/2026-10-11-macro.md)."}
  },
  "entry_price": 219.76,
  "entry_basis": "valuation file: base 274.70 x 0.8 (20% margin of safety); this is close to the 5y-median P/B of 1.6x [RA] and would make the quality case compelling.",
  "replaces": null,
  "replacement_reason": null
}
```
