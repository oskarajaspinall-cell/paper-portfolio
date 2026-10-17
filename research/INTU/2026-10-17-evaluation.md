# Evaluation: Intuit Inc. (INTU) — 2026-10-17
## Bear case
The market has halved the stock in a year (52-week change -49.8%) and is pricing the guided fiscal 2027 "reset" as permanent [Certain]. If AI-native and free/public-sector tax filing erode TurboTax pricing, the Consumer segment loses its cash engine; the FY2026 10-K added exactly this risk-factor language [company-reported] [Likely]. Gross margin has slipped 1.2pp over five years, the one soft quality metric [Certain]. The FCF margin of 40.4% jumped in a single year and may not repeat [Guessing]. Real yields rose +0.43pp in 3 months, mechanically compressing DCF value, and the 50-day average sits 14.9% below the 200-day, so the downtrend is not yet repaired [Certain]. The reverse DCF already implies only 1.5% growth, but a bear DCF of 212.88 shows downside remains if growth truly stalls [Certain].
## Bull case
Every quality metric is improving: ROIC 22.9% vs 14.7% in FY2022, operating margin 28.8% (+8.1pp), FCF conversion 189.7%, net debt/EBITDA 0.18x [Certain]. Yet P/E 20.1x, EV/EBITDA 13.1x and P/FCF 10.2x sit at the floor of the 5-year range, and P/FCF is 51% below the peer median [Certain]. A 9.82% FCF yield funds buybacks (shares -2.12% YoY) and bolt-ons like Sequence without leverage [Certain]. The price implies just 1.5% year-1 growth against base fair value of 557.68 [Certain]. Rates look largely priced after the de-rating from a 60x median P/E (macro overlay) [Likely]. The Nov 19, 2026 report is a catalyst if the reset proves temporary [Likely].
## Decision
```json
{
  "ticker": "INTU",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, 40%-FCF-margin franchise with five years of rising ROIC and operating margin trades at the floor of its own 5-year multiples and a 9.82% FCF yield, pricing a guided fiscal 2027 reset as permanent.",
  "rationale": "Thesis intact: returns, margins and FCF all still rising, no trigger near, valuation still at the 5-year floor. Conviction stays 4, not 5, given AI/free-filing risk to TurboTax and a small bearish macro tilt. The position already sits around its volatility-scaled conviction-4 size, so HOLD rather than ADD.",
  "price_at_decision": 330.17,
  "price_date": "2026-10-15",
  "research_note": "research/INTU/2026-10-17.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, back to the FY2022 level, showing the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 23%, under the FY2024 level of 23.7%, showing restructuring and AI spend are not turning into efficiency.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM FCF margin falls below 29%, back to the FY2024 level, meaning the FY2026 cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 29}},
    {"text": "TTM gross margin falls below 78%, under the FY2023 five-year low of 79.3%, signalling free/AI tax-filing competition is forcing price cuts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 557.68, "basis": "The fiscal 2027 reset proves temporary and the multiple re-rates to the fact sheet's base fair value 557.68 (DCF + EV/Revenue blend) [IS,CF,RA]; probability trimmed for the macro overlay's small tilt toward bear on rising real yields (research/INTU/2026-10-17-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 400.0, "basis": "P/E moves from 20.1x toward the 24.4x peer median on unchanged TTM earnings [RA,P:ADP,P:PAYX,P:GPN,P:CRM], below the mechanical base fair value because the 5y median multiples (60.1x P/E) reflect a zero-rate era that the overlay says will not return soon."},
    "bear": {"probability": 0.3, "target_price_12m": 244.65, "basis": "Free/AI tax-filing competition (new FY2026 10-K risk factor, https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm) makes the reset look permanent and the price falls to the fact sheet's bear fair value 244.65 [IS,CF,RA]; probability raised for the macro overlay's small bear tilt (research/INTU/2026-10-17-macro.md)."}
  },
  "entry_price": 309.8,
  "entry_basis": "Base fair value 557.68 x 0.8 is above the current price, so it cannot anchor; instead the 2026-09-10 swing low 309.80 [HI], where P/FCF would be back at its 5y low of 10.0x [RA], is the level at which the same evidence would justify an ADD toward conviction-4 size after re-research.",
  "replaces": null,
  "replacement_reason": null
}
```
