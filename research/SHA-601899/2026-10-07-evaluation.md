# Evaluation: Zijin Mining Group Company Limited (SHA:601899) — 2026-10-07

## Bear case
Every quality metric is at a five-year high because copper and gold prices are high, not because the moat has widened. Gross margin went from 15.4% (FY2021) to 34.6% TTM [Certain], and Zijin is a price-taker [Likely]. "Below five-year minimum" multiples on peak margins is the classic cyclical value trap: P/E of 12.0x on TTM earnings could look expensive if metal prices fall [Likely]. Part of the 25-58% discount to FCX/BHP/SCCO/NEM is a lasting A-share and governance discount, not mispricing [Likely]. Insider ownership is 0.09% [Certain]. Momentum is weak: -10.4% vs the 200-day MA and -9.0% over 6 months, with Q3 results due Oct 23, 2026 [Certain]. Shares rose 1.17% YoY [Certain].

## Bull case
This is a rare mix of cheapness and quality. ROIC rose from 13.5% to 24.3% TTM, FCF conversion from 37.8% to 101.0% and net debt/EBITDA fell from 1.88x to 0.44x [Certain]. The balance sheet is strong (Altman Z 3.61, Piotroski 7) [Certain], so a commodity downturn would not threaten solvency [Likely]. FCF yield is 8.83% and P/FCF of 11.3x sits below the five-year low of 16.2x [Certain]. Even if margins halve, cash generation would likely stay above FY2021-FY2023 levels, when conversion was 19-38% [Guessing]. Diversified copper and gold reserves give it scale and cost advantages over single-asset peers [Likely].

## Decision
```json
{
  "ticker": "SHA:601899",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A diversified copper-gold miner with structurally improved cash conversion and a deleveraged balance sheet trades below its own five-year valuation range and well below peers.",
  "rationale": "Quality and valuation both screen strongly, and leverage of 0.44x net debt/EBITDA limits downside risk. Size is capped at 5%, not 7%, because the margin gains are mostly commodity-driven, at a cyclical peak, and part of the peer discount is a structural A-share discount. Nothing is replaced because the portfolio is empty.",
  "price_at_decision": 29.79,
  "price_date": "2026-09-30",
  "research_note": "research/SHA-601899/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin falls below 20% (the FY2024 level), showing the margin expansion was purely cyclical", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "ROIC falls below 15%, back toward the FY2021-FY2023 range", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "FCF margin falls below 7.9% (the FY2024 level), reversing the cash-conversion improvement", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7.9}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 1.9x, reversing the deleveraging"}
  ],
  "replaces": null,
  "replacement_reason": null
}
```
