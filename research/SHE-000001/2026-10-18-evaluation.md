# Evaluation: Ping An Bank Co., Ltd. (SHE:000001) — 2026-10-18
## Bear case
Returns on equity are falling and nothing yet shows them stopping. ROE has dropped from 11.0% (FY2022) to 8.2% TTM [RA] [Certain], and the bank's own H2 2025 call admitted revenue and net profit fell [OV transcript] [Certain]. The rising net margin (47.3% TTM [IS]) comes from provisioning and business mix, not from stronger core earnings power [Likely]. The cheap 0.4x P/B [RA] is cheap for a reason: the market is pricing structural NIM compression and property-credit risk [Likely]. The mechanical fair value assumes a sustainable ROE that the trend contradicts, and the dividend-discount method gives only 6.05 CNY [Certain]. Shares grew 4.18% YoY [ST] [Certain], diluting holders while ROE falls. Piotroski is a middling 4 [ST] [Certain]. Q3 results land on Oct 24, 2026 [ST], a binary print six days away [Certain]. This would also be a fourth China/HK exposure in a book that already carries three, counting the pending order [Certain].
## Bull case
The valuation is near distressed levels: 5.4x P/E (23% of its 5y range) and 0.4x P/B, 27% and 39% below peer medians [RA] [Certain]. Even the mechanical bear fair value of 13.55 CNY sits above the 11.50 close, and the reverse DCF implies -14.7% revenue growth [Certain]. Management guided to a return to growth in 2026 with asset quality, cost control and retail improving [OV transcript] [Likely]. Low beta (0.51 [ST]) diversifies the portfolio [Certain]. If PBOC easing or property stabilisation slows margin erosion, P/B could re-rate toward the 0.7x peer median (macro overlay) [Guessing]. The CNY firming against the dollar argues against capital-outflow stress (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "SHE:000001",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Chinese joint-stock bank at 0.4x P/B and 5.4x P/E is cheap against history and peers, but ROE has been falling for years with no evidence yet of a floor.",
  "rationale": "Cheapness is real, but the core thesis needs ROE to stabilise, and every year shown says the opposite. Shares are being diluted, the F-score is middling, and Q3 results are six days away. Adding a fourth China exposure on a falling-return bank is good but not compelling. Conviction 3 means AVOID. Re-test after the Q3 print.",
  "price_at_decision": 11.50,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000001/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE rises above 9%, back to the FY2024 level, showing the downtrend has reversed (this would raise conviction).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 9}},
    {"text": "TTM ROE falls below 7%, confirming margin and asset-quality erosion is still accelerating.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "TTM net margin falls below 40%, reversing the five-year rise and signalling provisioning or funding-cost pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "Shares outstanding growth exceeds 5% YoY, dilution compounding against a falling ROE.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 16.88, "basis": "ROE stabilises and P/B re-rates toward the 0.7x peer median [RA], reaching the P/B + ROE base fair value of 16.88 CNY; the macro overlay's tilt is neutral/small, so probabilities are unchanged (research/SHE-000001/2026-10-18-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 12.20, "basis": "ROE keeps drifting lower (9.6% to 8.2% [RA]), so P/E holds near its 5y median 5.5x [RA] and the price stays close to the 12.08 52-week high [HI]; this sits well below the mechanical base fair value of 17.98 CNY because that model assumes a sustainable ROE the trend contradicts."},
    "bear": {"probability": 0.25, "target_price_12m": 9.5, "basis": "Property-credit stress pushes ROE below 7% (macro overlay bear chain) and P/E de-rates toward its 5y low 4.2x [RA], below the 9.99 52-week low [HI]; the mechanical bear fair value of 13.55 CNY ignores a further ROE decline, and the DDM value of 6.05 CNY shows the downside if payouts are what's valued."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below even its bear fair value of 13.55 CNY, and the default anchor (base 17.98 x 0.8) is above the price. Falling ROE is what blocks conviction 4, so a lower price would not change the decision. ROE stabilising in the Q3 print and after would.",
  "replaces": null,
  "replacement_reason": null
}
```
