# Evaluation: Intuit Inc. (INTU) — 2026-10-07
## Bear case
The market has cut INTU 57.4% in 12 months and every multiple sits below its 5-year floor [Certain]. That pricing implies a lasting change: AI-native tools could commoditise DIY tax and small-business bookkeeping, and management itself says price is the top reason DIY tax customers leave [Certain]. Management has called FY2027 a "reset year" with slower growth [Certain], so earnings momentum stalls just as the stock needs proof. A 40.4% FCF margin is a five-year high, up from 28.8% in FY2024 [Certain]. If it falls back, the 11.2% FCF yield is overstated [Likely]. Gross margin has slipped 1.2pp over five years [Certain]. The 10y real yield is up 71bp in 3 months, which caps any re-rating (macro overlay) [Certain]. The shares are 25.7% below their 200-day average [Certain], and cheap software stocks can stay cheap for a long time [Guessing].
## Bull case
Quality is still improving. ROIC rose from 14.7% to 22.9%, operating margin gained 8.1pp to 28.8% and FCF margin reached 40.4% [Certain]. That does not look like a franchise in decline [Likely]. The valuation already prices in a decline: P/E 17.3x against a 5-year minimum of 18.9x, P/FCF 8.9x against 10.0x, and discounts of 22% to the peer median P/E and 47% on P/FCF [Certain]. The balance sheet is effectively unlevered at 0.18x net debt/EBITDA, and the share count fell 2.12% YoY [Certain], so buybacks at an 11.2% FCF yield build value per share [Likely]. Management says the "big bets" are 30% of revenue and each is growing over 30%. It also reports no meaningful tax share loss to AI entrants [Likely]. Short interest is low at 2.69% and fell 11.8% last month, and Piotroski F is 7 [Certain]. The FY2027 reset is a known, guided event rather than a hidden one [Likely].
## Decision
```json
{
  "ticker": "INTU",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, 40%-FCF-margin franchise with five years of rising ROIC and operating margin trades below its own 5-year minimum on every multiple and at an 11.2% FCF yield, pricing a guided FY2027 growth reset as a permanent impairment.",
  "rationale": "Quality and returns keep rising while every multiple sits below its 5y floor and well below peers. The net-cash balance sheet and buybacks limit the downside. Conviction is 4, not 5: AI-driven pricing pressure in DIY tax and the FY2027 reset make the timing of a re-rating uncertain. Size 7%; Technology exposure and cash allow it.",
  "price_at_decision": 289.81,
  "price_date": "2026-10-06",
  "research_note": "research/INTU/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, back to the FY2022 level, showing the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 23%, under the FY2024 level of 23.7%, showing AI/mid-market spending is not turning into efficiency.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM FCF margin falls below 29%, back to the FY2024 level, meaning the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 29}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 368, "basis": "As big bets grow above 30% [investor-day transcript], P/E re-rates from 17.3x to the 22.0x peer median [RA,P:ADP,P:PAYX,P:ADBE,P:WDAY]; the macro overlay's neutral/small tilt (research/INTU/2026-10-07-macro.md) leaves this probability unchanged."},
    "base": {"probability": 0.5, "target_price_12m": 326, "basis": "FCF margin holds at 40.4% [CF,IS] and P/FCF returns only to its 5y minimum of 10.0x from 8.9x [RA] as the guided FY2027 reset plays out."},
    "bear": {"probability": 0.25, "target_price_12m": 233, "basis": "FCF margin falls back from 40.4% to the FY2025 32.5% [CF,IS] on DIY-tax price churn [Goldman transcript] while P/FCF stays at 8.9x [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
