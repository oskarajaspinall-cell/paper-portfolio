# Evaluation: Bank of America Corporation (BAC) — 2026-10-09
## Bear case
The price already exceeds every mechanical fair-value scenario: base $40.56 is 24.3% below the $53.61 close, and even the bull case ($45.08) is 15.9% below it [Certain]. P/B of 1.4x is above its own 5-year max of 1.3x [Certain], so the re-rating has already happened. Returns don't justify more. ROE is 11.2% TTM, below the FY2021 level of 11.8% [Certain]. With the 10y at 5.28% and beta at 1.21, the cost of equity is roughly equal to ROE, which caps justified P/B near book. That is why P/B+ROE gives only $29.84–34.30 [Likely]. The macro overlay tilts toward bear: the 10y real yield is up 0.61pp in 3 months, which pressures securities AOCI in a 2023-style echo [Likely]. Piotroski is 4/9 [Certain]. Q3 results are due Oct 14, so binary risk lands immediately [Certain].
## Bull case
On P/E, BAC is 10% below the 13.7x peer median, and on P/B it is 30% below the 2.0x peer median [Certain]. ROE has recovered every year since its FY2024 trough of 9.2%, to 11.2% TTM [Certain]. Shares are down 3.72% YoY, so buybacks compound EPS [Certain]. The stock is 11% below its 50-day average with RSI at 24.5, and it has lagged SPY by 11.9pp over 3 months. Much of the rate scare may already be priced in [Likely]. In a higher-for-longer world with no credit stress (HY spread 3.09%, well below 5.0%), asset repricing could outrun deposit costs [Guessing]. The Fed's stress-test overhaul may also ease capital planning [Likely]. The FCFE DCF base of $53.82 roughly supports today's price [Certain].
## Decision
```json
{
  "ticker": "BAC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A well-diversified bank earning an ROE (11.2%) roughly equal to its cost of equity trades above its own 5-year P/B range and above every own-history fair-value scenario, so the recovery looks priced in.",
  "rationale": "Price sits above all three fair values and P/B is above its 5-year max. ROE has no edge over a 5.28%-risk-free cost of equity. The macro overlay is primary with a bear tilt, and earnings on Oct 14 add binary risk. The peer discount reflects lower returns, not mispricing. That is good but not compelling, so AVOID.",
  "price_at_decision": 53.61,
  "price_date": "2026-10-08",
  "research_note": "research/BAC/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 13%, clearly above FY2021's 11.8% and the cost of equity, showing structurally higher returns that would justify a higher P/B.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13}},
    {"text": "TTM net margin rises above 32%, back toward FY2021's 34.1%, evidencing NII/fee strength beyond the cyclical recovery.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 32}},
    {"text": "TTM ROE falls below 9%, under the FY2024 trough of 9.2%, confirming the recovery was purely cyclical (thesis for avoiding strengthens).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 59.66, "basis": "Higher-for-longer rates without credit stress (macro overlay macro_bull) re-rate P/E to its 5y max of 13.8x [RA] on TTM EPS; this sits above the fact-sheet bull fair value of $45.08 because it assumes multiple expansion, not the P/B+ROE method's cost-of-equity cap."},
    "base": {"probability": 0.45, "target_price_12m": 51.45, "basis": "P/E reverts to its 5y median of 11.9x [RA] on TTM EPS; this is above the $40.56 blended fair value because the FCFE DCF base ($53.82) [fact sheet] supports today's level, while the P/B+ROE method is penalised by the 5.28% risk-free rate."},
    "bear": {"probability": 0.35, "target_price_12m": 42.54, "basis": "Real-yield back-up pressures AOCI and NIM (macro overlay, primary weight, small bear tilt, which moves 0.10 of probability from base/bull to bear); the price falls to the FCFE DCF bear of $42.54 [fact sheet], within the blended fair-value range of $34.07–45.08."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
