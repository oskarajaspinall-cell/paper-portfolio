# Evaluation: Kuaishou Technology (HKG:1024) — 2026-10-25
## Bear case
The cheapness is on accounting earnings, not cash: P/FCF of 11.6x is in line with peers (11.8x), and FCF margin has fallen from 17.1% in FY2024 to 6.3% TTM as AI capex rises, with FCF conversion down to 57.3% [Certain]. ROIC has slid from 61.5% to 29.4% TTM [Certain]. Revenue growth slowed to low single digits in Q1 and Q2 2026 while Douyin and Tencent contest the market [Likely]. Kling AI, the one growth engine, is being funded by Alibaba and Tencent ahead of a planned spin-off, so the parent's share of any AI value is shrinking [Likely]. A Tencent unit selling stock is a supply overhang, and the price trend is broken: down 62.2% over 12 months and 42.6% below the 200-day average [Certain]. The mechanical bear fair value is negative, showing how sensitive value is to capex [Certain]. Piotroski F of 4 [Certain].

## Bull case
At 6.8x P/E and 2.6x EV/EBITDA the stock trades below its own 5-year minimum multiples (10.9x, 7.6x) and far below the 22.8x peer P/E [Certain]. The balance sheet is net cash (net debt/EBITDA -1.97x) and operating margin of 10.8% TTM is still far above the FY2021 loss [Certain]. The reverse DCF implies -1.6% year-1 revenue growth, while revenue still grew in Q1 and Q2 2026 [Likely]. The 8.64% FCF yield holds even at depressed capex-heavy cash flow [Certain]. Outside Kling funding cuts the parent's capital need, and a listing could crystallise value [Guessing]. Base fair value of 48.04 HKD sits well above the 27.90 close [Certain]. If capex peaks in 2026, FCF margin can recover toward FY2023-24 levels and the earnings multiple re-rates [Guessing].

## Decision
```json
{
  "ticker": "HKG:1024",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash short-video platform trades below its own 5-year minimum earnings multiples, but falling FCF margin from AI capex, slowing growth, Kling dilution and a Tencent selling overhang mean the cheapness is not yet backed by cash.",
  "rationale": "Earnings multiples are deeply cheap and the balance sheet is net cash, but P/FCF is only peer-level, cash conversion and ROIC are falling, growth has stalled, and AI value is moving into a separately funded Kling. Good but not compelling: conviction 3, so no position. Price is not the obstacle; FCF recovery is.",
  "price_at_decision": 27.90,
  "price_date": "2026-10-23",
  "research_note": "research/HKG-1024/2026-10-25.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 12%, showing AI capex has peaked and cash conversion is returning toward FY2023-24 levels (14.0%-17.1%); this would justify re-research for a BUY.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 12}},
    {"text": "TTM operating margin falls below 7%, showing AI spend and competition are eroding the core platform's profitability (thesis for avoiding confirmed).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7}},
    {"text": "Quarterly revenue growth in the company results release re-accelerates to high single digits for two consecutive quarters with Kling consolidated, reversing the low-single-digit slowdown of Q1-Q2 2026."},
    {"text": "Net debt/EBITDA on the statistics page rises above 0x, i.e. net cash is lost to AI capex.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 48.04, "basis": "Capex peaks and FCF margin recovers toward FY2024's 17.1% [CF,IS], lifting the stock to the mechanical base fair value of 48.04 HKD, still below the 5y median 13.3x P/E [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 32.0, "basis": "Low-single-digit growth and FCF margin near 6.3% TTM [CF,IS] keep P/FCF around 11.6x, in line with peers [RA]; a modest recovery from the 26.68 52-week low [HI] only, below base fair value because the DCF assumes cash margins not being earned."},
    "bear": {"probability": 0.30, "target_price_12m": 21.0, "basis": "Revenue turns down as the reverse DCF already implies (-1.6%) while AI capex keeps FCF conversion falling from 57.3% [CF,IS] and the Tencent sale overhang persists (https://www.reuters.com/world/asia-pacific/tencent-unit-seeks-up-155-billion-kuaishou-share-sale-term-sheet-shows-2026-07-06/); the negative mechanical bear value shows the downside is capex-driven."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value 48.04 x 0.8 sits above the 27.90 close. The obstacle is falling FCF margin and conversion under AI capex plus Kling dilution; a lower price would not change the decision until cash flow recovers.",
  "replaces": null,
  "replacement_reason": null
}
```
