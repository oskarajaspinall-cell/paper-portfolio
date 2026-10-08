# Evaluation: The Hartford Insurance Group, Inc. (HIG) — 2026-10-07
## Bear case
The low P/E is a sector discount, not a stock-specific one. HIG at 8.7x is exactly in line with the peer median of 8.7x (TRV, CB, ALL, CINF) [Certain], so the market is pricing the whole P&C group for a cycle peak [Likely]. P/B of 1.8x sits at 66% of its 5y range (1.3x-2.0x) [Certain], leaving room to fall if ROE of 22.1% reverts toward the 11.5-13.0% of FY2021-22 [Guessing]. FCF conversion has fallen from 210.7% (FY2022) to 132.6% TTM [Certain]. A CEO handover, the Equitable Employee Benefits deal and the Hartford Funds sale all land at once, adding execution risk [Likely]. The stock lags SPY by 20.2pp over 12 months, and Q3 results on Oct 26, 2026 can confirm or break the earnings run-rate [Certain].
## Bull case
Returns have compounded: ROIC rose from 10.9% to 18.0% and ROE from 13.0% to 22.1% over five years [Certain]. P/E of 8.7x and EV/EBITDA of 6.9x are both below their own 5y minimums (9.7x, 7.7x) [Certain]. A 16.86% FCF yield and a 3.96% YoY share-count reduction fund returns without a re-rating [Certain]. Net debt/EBITDA has halved toward 0.76x [Certain]. The CEO successor is the internal president, confirmed by an SEC 8-K, which limits strategic drift [Likely]. Per the macro overlay, higher real yields with anchored breakevens lift reinvestment income on the float [Likely]. Beta of 0.49 makes HIG a low-correlation diversifier for this portfolio [Certain].
## Decision
```json
{
  "ticker": "HIG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return commercial and benefits insurer trades below its own 5-year P/E and EV/EBITDA ranges, but only in line with peers and near the top of its P/B range, so the discount reflects cycle-peak risk across the group rather than mispricing.",
  "rationale": "Quality is real, but valuation is no cheaper than peers (P/E 8.7x versus a peer median of 8.7x), and P/B of 1.8x already pays for a peak-level 22.1% ROE. CEO transition, M&A and falling FCF conversion add risk ahead of Q3 results. Good but not compelling: conviction 3, so AVOID under the owner rule.",
  "price_at_decision": 126.79,
  "price_date": "2026-10-06",
  "research_note": "research/HIG/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROE falls below 15%, showing the underwriting-cycle tailwind behind the re-rated returns has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "Debt/EBITDA rises back above 1.2x, reversing the FY2021-25 deleveraging (for example, after funding the Equitable Employee Benefits deal).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.2}},
    {"text": "FCF conversion (FCF/NI) falls below 100% on the cash-flow and income-statement pages, showing earnings quality is deteriorating."},
    {"text": "Upside review: Q3 2026 results (Oct 26, 2026) show ROE holding above 20% while FCF conversion stops falling. That would show returns are durable rather than at a cycle peak and would justify a re-initiation at higher conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 147.0, "basis": "ROE holds near 22.1% [RA] and P/E re-rates from 8.7x to its 5y median of 10.1x [RA] on unchanged TTM earnings; the macro overlay's neutral/small tilt (research/HIG/2026-10-07-macro.md) leaves this probability unchanged."},
    "base": {"probability": 0.55, "target_price_12m": 127.0, "basis": "P/E stays at the peer median of 8.7x [RA,P:TRV,P:CB,P:ALL,P:CINF] on flat earnings, and buybacks (shares -3.96% YoY [ST]) offset modest return normalisation; the macro overlay's neutral/small tilt (research/HIG/2026-10-07-macro.md) means no adjustment."},
    "bear": {"probability": 0.2, "target_price_12m": 92.0, "basis": "ROE reverts toward its FY2021-22 levels of 11.5-13.0% [RA], and P/B de-rates from 1.8x to its 5y minimum of 1.3x [RA] as a credit-spread or rate-reversal shock hits book value, per the macro overlay bear case (research/HIG/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
