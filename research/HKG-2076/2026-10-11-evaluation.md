# Evaluation: Kanzhun Limited (HKG:2076) — 2026-10-11
## Bear case
Kanzhun is a pure bet on China's white-collar and blue-collar hiring cycle, and the shares are down -36.2% in 12 months despite improving reported numbers [Certain]. That decline may reflect a VIE/HFCAA risk premium that does not close inside 12 months [Likely]. Shares outstanding rose 4.74% YoY even with buybacks, so per-share value creation lags headline profit growth [Certain]. TTM net margin of 52.8% sits well above the 34.8% operating margin, so the 10.4x P/E is flattered by non-operating income and is not a clean earnings multiple [Likely]. Gross margin is down 1.9pp over five years, and the 2026-09-01 change in directors' executive roles is unexplained [Certain]. The portfolio already holds HKG:9999, so this adds China VIE exposure that could fall at the same time on one regulatory headline [Likely].
## Bull case
BOSS Zhipin is China's leading direct-chat recruitment platform. Its network effect is reducing the need to buy growth: S&M fell from 33.5% to 20.5% of revenue between 2023 and 2025 [Likely]. Q2 2026 revenue grew 14.1% YoY, described as accelerating [Certain]. Operating margin expanded from 11.0% to 34.8% TTM, ROCE from 4.3% to 14.0%, and FCF margin is 50.9% [Certain]. The net-cash balance sheet (net debt/EBITDA -5.79x) funds an annual dividend and repeated buybacks [Certain]. At 10.8x P/FCF (9.28% FCF yield) and 7.2x EV/EBITDA, the stock is below the minimum of its own 5-year range on every multiple and 61-63% below peers on P/E and EV/EBITDA [Certain]. Even the mechanical bear fair value of 71.75 HKD is above the 60.00 close [Certain]. A low 0.49 beta adds diversification against a US-heavy book [Likely].
## Decision
```json
{
  "ticker": "HKG:2076",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "China's leading direct-chat recruitment platform, with net cash, a 50.9% FCF margin and accelerating 14.1% revenue growth, trades below its own 5-year minimum on every multiple at a 9.28% FCF yield, pricing a China/VIE discount that its fundamentals do not show.",
  "rationale": "Quality is rising, the business is cash-backed and the price is below its own 5-year minimum multiples, so the asymmetry justifies the 7% conviction-4 size. Two things keep conviction off 5: 4.74% dilution and a China VIE exposure that overlaps with HKG:9999. Communication Services goes to about 14% of the portfolio and cash stays far above the reserve, so no replacement is needed.",
  "price_at_decision": 60.00,
  "price_date": "2026-10-09",
  "research_note": "research/HKG-2076/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 16.0%, showing the AI-matching and network-effect cost advantage has eroded.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 16.0}},
    {"text": "TTM gross margin falls below the FY2023 five-year low of 82.2%, signalling pricing or competitive pressure on employer paid services.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 82.2}},
    {"text": "TTM FCF margin falls below the FY2023 level of 35.1%, showing the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35.1}},
    {"text": "Reported quarterly revenue (company release / income statement) declines YoY for two consecutive quarters, ending the growth acceleration seen in Q2 2026 (+14.1%)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 131.83, "basis": "Growth acceleration and buybacks close the China discount to the mechanical base fair value of 131.83 HKD [fact sheet Fair value], which is roughly P/FCF back near its 5y median of 24.6x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 83.30, "basis": "P/FCF re-rates only to its 5y minimum of 15.0x from 10.8x [RA] on flat TTM FCF; this is below the 131.83 base fair value because the VIE/HFCAA discount that drove the -36.2% 12m decline [ST] is assumed to persist."},
    "bear": {"probability": 0.30, "target_price_12m": 48.36, "basis": "A China hiring slowdown or VIE/regulatory headline [20-F, sec.gov] takes the shares back to the 52-week low of 48.36 [HI], below the mechanical bear of 71.75 because the market keeps the multiple below its own 5y minimum."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
