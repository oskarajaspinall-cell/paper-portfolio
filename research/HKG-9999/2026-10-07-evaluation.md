# Evaluation: NetEase, Inc. (HKG:9999) — 2026-10-07

## Bear case
The discount is structural, not mispricing: VIEs carry 85.2% of FY2025 revenue and PRC playtime, loot-box and approval rules can cap monetization at any time [Certain]. A cheap multiple can stay cheap; the stock is -21.6% over 12 months and -38.0pp versus SPY, below both its 50-day and 200-day averages, so the market is not yet rewarding the margin expansion [Certain]. Shares outstanding still rose 0.39% YoY despite buybacks, so SBC absorbs capital return [Certain]. TTM net margin (27.9%) has slipped below FY2025 (30.0%) and ROE fell to 20.4% from 22.6%, hinting the profit peak may be in [Likely]. Growth now leans on hit-driven launches; a weak January Ananta global launch would leave a single-franchise-dependent earnings base with little re-rating catalyst [Guessing].

## Bull case
Quality has compounded for five years: operating margin 35.2% TTM vs 18.7% FY2021, FCF margin 43.5% vs 26.6%, ROCE 23.3% vs 15.9% [Certain]. Yet EV/EBITDA (8.2x) and P/FCF (10.1x) sit below their own 5-year minimums and the P/E (16.0x) is 27% under the peer median [Certain]. A 9.86% FCF yield with net cash at -3.76x net debt/EBITDA gives downside protection and funds returns [Certain]. FCF conversion of 156.0% shows earnings are cash-backed [Certain]. Q2 2026 gross margin of 70.5% per the transcript points to further mix improvement [Likely]. Ananta's global launch in January, before the 12-month horizon ends, is a concrete catalyst for re-rating toward the 5y median multiple [Likely].

## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, high-margin game developer with five years of rising returns trades below its own 5-year EV/EBITDA and P/FCF minimums at a 9.86% FCF yield, pricing a regulatory overhang rather than delivered quality.",
  "rationale": "Nothing in the fundamentals has changed since entry: margins, ROCE and FCF conversion remain above every trigger. Position is ~7%, matching conviction 4. Conviction is not 5 because VIE/PRC regulatory risk is binary and price momentum is negative, so no ADD; valuation below 5y minimums argues against trimming.",
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
    "bull": {"probability": 0.30, "target_price_12m": 226.0, "basis": "P/FCF re-rates from 10.1x to its 5y median 12.3x [RA] on TTM FCF, supported by the January Ananta global launch [OV news] and margins still rising (op margin 35.2% TTM [IS]); weighted below base because the stock has not traded at the median since its -21.6% 12m fall [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 196.6, "basis": "P/FCF recovers only to its 5y minimum 10.7x [RA] on flat TTM FCF, as the regulatory/VIE discount (85.2% VIE revenue, 20-F) persists; most likely because EV/EBITDA and P/FCF already sit below every fiscal-year-end level in 5y [RA], favouring partial mean reversion."},
    "bear": {"probability": 0.25, "target_price_12m": 157.8, "basis": "P/E compresses from 16.0x to its 5y minimum 13.6x [RA] on a PRC monetization/loot-box rule or weak launch named in the 20-F risk section; probability capped by net cash at -3.76x net debt/EBITDA [RA] and a 9.86% FCF yield [ST] that limit downside."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
