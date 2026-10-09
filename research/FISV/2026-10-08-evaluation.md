# Evaluation: Fiserv, Inc. (FISV) — 2026-10-08
## Bear case
The cheapness looks like a value trap: margins and returns are no longer improving. Operating margin fell from 26.9% (FY2025) to 21.4% TTM, ROIC from 8.7% to 6.8%, and gross margin from 59.4% to 56.2% [Certain] [IS,RA]. Net debt/EBITDA rose from 2.72x to 3.54x while the company kept buying back stock, and the Altman Z of 1.47 sits in the distress zone [Certain] [RA,ST]. A restructuring 8-K, the "Project Elevate" cost plan and Jana's push for deeper cuts suggest management is reacting to pressure, not leading from strength [Likely] (note §2, §6). The -64.5% 12-month fall, -10.6% 50/200-day spread and Q3 results on Nov 3 mean the trailing figures the multiples rely on may still be too high [Likely] [ST,HI]. The fair-value result of +287% is a sign of stale inputs, not of mispricing [Likely].
## Bull case
At 8.7x P/E, 6.7x EV/EBITDA and a 16.29% FCF yield, FISV trades below its own 5-year minimum on every multiple and 20-46% below FI/GPN/JKHY/PYPL [Certain] [RA,ST]. The reverse DCF prices a -15.1% revenue decline in year 1, which TTM revenue and an 18.8% FCF margin do not show [Certain] [CF,IS]. Core banking and Clover have high switching costs, and Clover keeps adding venue wins (Hard Rock Stadium, CFL) [Likely] [OV]. Buybacks shrank the share count 5.21% YoY and short interest fell 9.8% month on month [Certain] [ST]. An activist is pushing for cost cuts that could rebuild margins [Likely]. Even a re-rating to its 5-year minimum P/E of 10.4x would lift the price about a fifth [Guessing].
## Decision
```json
{
  "ticker": "FISV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "FISV is optically very cheap (8.7x P/E, 16.29% FCF yield, below every 5-year multiple floor), but falling margins and ROIC, rising leverage, a distress-zone Altman Z, restructuring and activist pressure make it a likely value trap until results show margins stabilising.",
  "rationale": "Valuation is compelling only if TTM earnings hold. Operating margin, ROIC and leverage are all moving the wrong way, Altman Z is 1.47, and Q3 results land Nov 3. That is good-but-not-compelling evidence: conviction 3, below the buy threshold. Cash is the better outcome until fundamentals stop deteriorating.",
  "price_at_decision": 45.31,
  "price_date": "2026-10-07",
  "research_note": "research/FISV/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2025 level of 26.9%, showing Project Elevate cost cuts are rebuilding profitability (would make a BUY case).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 26.9}},
    {"text": "TTM ROIC climbs back above the FY2025 level of 8.7%, showing the five-year returns uptrend has resumed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 8.7}},
    {"text": "Net debt/EBITDA (ratios page) falls back to the FY2024 level of 2.72x or below while buybacks continue, removing the balance-sheet strain behind the 1.47 Altman Z."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 54.2, "basis": "Margins stabilise after Project Elevate and P/E re-rates from 8.7x to its 5-year minimum of 10.4x [RA] on TTM EPS. This is far below the mechanical 230.11 bull fair value, whose history-based growth and margins ignore the 21.4% vs 26.9% operating margin drop [IS]."},
    "base": {"probability": 0.45, "target_price_12m": 47.7, "basis": "Earnings hold and P/E stays at 8.7x [RA], with per-share value lifted only by the 5.21% YoY share count reduction [ST]. This is well below the 175.20 base fair value because the reverse DCF's -15.1% implied growth and the rising 3.54x leverage [RA] show the market rejecting the historical assumptions."},
    "bear": {"probability": 0.30, "target_price_12m": 36.0, "basis": "Q3 (Nov 3 [ST]) shows a second step of margin compression of the same size as FY2025→TTM (operating margin 26.9%→21.4% [IS]) at an unchanged 8.7x P/E, as the -64.5% 12-month trend and 1.47 Altman Z [ST] suggest. This is below the 103.00 bear fair value, which assumes historical margins."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
