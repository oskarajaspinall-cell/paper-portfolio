# Evaluation: NetEase, Inc. (HKG:9999) — 2026-10-07

## Bear case
The discount is structural, not an anomaly. VIEs held 85.2% of FY2025 revenue, so ownership rests on contracts PRC authorities could challenge [Certain]. Tighter minors'-playtime, loot-box and approval rules can cap monetization at any time [Certain]. Mean reversion therefore may not happen: P/E at 16.0x is above its 5y median of 15.4x, so on earnings the stock is not cheap versus its own history [Certain]. Net margin dipped to 27.9% TTM from 30.0% in FY2025 [Certain], and ROIC of 368.3% is inflated by a tiny invested-capital base rather than showing incremental strength [Likely]. Shares outstanding rose 0.39% YoY despite buybacks, so SBC absorbs repurchases [Certain]. Momentum is poor: -21.6% over 12 months and -38.0pp versus SPY [Certain]. A hit-driven pipeline makes Ananta's January launch a binary event [Guessing].

## Bull case
Quality has risen every year: operating margin 35.2% TTM vs 18.7% in FY2021, gross margin 67.2% vs 53.6%, FCF margin 43.5% vs 26.6% [Certain]. Earnings are cash-backed: FCF conversion 156.0% TTM [Certain]. Yet EV/EBITDA (8.2x) and P/FCF (10.1x) sit below their own 5-year minimums (9.3x, 10.7x) and below peer medians, with a 9.86% FCF yield [Certain]. Net cash (-3.76x net debt/EBITDA) cushions a regulatory shock and funds dividends and buybacks [Certain]. Q2 2026 gross margin improved to 70.5% on new titles including Marvel Rivals and Sea of Remnants [Likely]. Beta of 0.77 and Altman Z of 8.53 make it a low-risk way to own high-return gaming IP [Certain]. Holding at the 7% conviction-4 size already captures this; a 10% size needs evidence the regulatory discount is narrowing, which the research does not show [Likely].

## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, high-margin game developer with five years of rising returns trades below its own 5-year EV/EBITDA and P/FCF minimums at a 9.86% FCF yield, pricing in a regulatory overhang rather than the quality it has delivered.",
  "rationale": "Thesis intact on every fundamental: margins and FCF conversion at highs, net cash, multiples below 5y minimums. Conviction stays 4, not 5, because VIE and PRC regulatory risk are structural and P/E is not below its 5y median. The position is already at the 7% conviction-4 size, so HOLD; no ADD.",
  "price_at_decision": 185.60,
  "price_date": "2026-10-06",
  "research_note": "research/HKG-9999/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in an SEC 20-F/6-K filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 226.0, "basis": "FCF margin holds near 43.5% TTM [CF,IS] and P/FCF re-rates from 10.1x to its 5y median 12.3x [RA] as new titles extend the gross-margin gains."},
    "base": {"probability": 0.5, "target_price_12m": 196.6, "basis": "Fundamentals stay at TTM levels and P/FCF recovers only to its 5y minimum 10.7x from 10.1x [RA], with the regulatory/VIE discount persisting (20-F)."},
    "bear": {"probability": 0.25, "target_price_12m": 157.8, "basis": "A PRC monetization curb or weak launch compresses P/E from 16.0x to its 5y minimum 13.6x [RA] on flat TTM earnings, per the 20-F regulatory risk."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
