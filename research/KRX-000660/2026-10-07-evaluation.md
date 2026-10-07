# Evaluation: SK hynix Inc. (KRX:000660) — 2026-10-07
## Bear case
This is a memory-cycle business priced on what looks like peak earnings [Likely]. TTM gross margin of 76.3% and operating margin of 68.0% sit far above every fiscal year shown, and FY2023 swung to -1.6% gross and -27.8% net margin [Certain]. A 7.8x P/E at peak margins is the classic cyclical trap; EV/Sales (6.6x) and P/B (4.9x) are already above their own 5-year highs, so the price assumes the margins hold [Certain]. TTM net margin (85.6%) exceeds operating margin (68.0%), implying non-operating gains flatter earnings and ROE [Likely]. FCF conversion fell to 56.6% from 76.1% in FY2021 [Certain]. The stock is -24.3% over three months, off a 2,987,000 high, which may mean the market is already discounting a turn [Guessing]. Beta of 2.39 and KRW exposure add volatility in an empty portfolio [Certain].
## Bull case
SK hynix is the leading HBM supplier into AI accelerators, a position protected by multi-year qualification and heavy capex [Likely]. ROIC is 61.6% TTM, the balance sheet is net cash (-0.47x net debt/EBITDA), Piotroski F is 7 and Altman Z is 7.28 [Certain]. Even on earnings that have fully converted to cash, P/FCF of 14.1x (7.10% FCF yield) is 30% below the peer median and P/E is 45% below it [Certain]. Share count is flat (+0.14% YoY) [Certain]. If HBM keeps memory pricing structurally higher than in past cycles, today's earnings base is closer to normal than peak and the stock re-rates toward peers [Guessing]. Earnings on Oct 29, 2026 could confirm durability [Likely].
## Decision
```json
{
  "ticker": "KRX:000660",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "thesis": "An exceptional HBM franchise, but a 12-month core holding at record sales and book multiples is a bet that peak-cycle memory margins persist, which the evidence cannot support.",
  "rationale": "Low P/E reflects record margins (76.3% gross), not cheapness: EV/Sales and P/B exceed 5-year highs, net margin exceeds operating margin, and FCF conversion is falling. A commodity-cycle stock with 2.39 beta should be bought on normalised, not peak, earnings. Quality and net cash make it a re-entry candidate after a cycle reset.",
  "price_at_decision": 1773000.00,
  "price_date": "2026-10-06",
  "research_note": "research/KRX-000660/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin falls below the FY2021 level of 44.1% while the balance sheet stays net cash: the cycle has reset with the franchise intact, so re-evaluate for entry on trough-like earnings.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 44.1}},
    {"text": "ROIC falls below the FY2021 normal-cycle level of 13.4%: returns have normalised, giving a sound base for a valuation that does not depend on peak margins.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13.4}},
    {"text": "FCF conversion (FCF/NI) recovers above the FY2024 level of 70.0% while gross margin holds above the FY2025 level of 60.4%, showing upcycle earnings are cash-backed and durable rather than peak."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```
