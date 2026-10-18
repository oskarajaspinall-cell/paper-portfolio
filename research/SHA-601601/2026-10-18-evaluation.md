# Evaluation: China Pacific Insurance (Group) Co., Ltd. (SHA:601601) — 2026-10-18
## Bear case
The low multiple is probably a value trap, not a mispricing. ROE rose from 12.2% to 17.5% while ROIC stayed flat at about 10.9%, so the improvement looks driven by leverage and mix rather than better underwriting [Certain] (RA). Net debt/EBITDA (site definition) rose from 1.33x to 2.47x [Certain] (RA). Falling Chinese long-term rates squeeze the life segment's investment spread, and management flagged a new asset-liability regulation with a "profound impact" [Likely] (transcript). Our data cannot test the thesis: no margins, new business value, CSM or solvency figures on stockanalysis.com, and the macro overlay could not get China's yields [Certain]. Shares grew 3.34% YoY [Certain] (ST). The stock is in a downtrend (6-month -22.6%) with results due Oct 28, 2026 [Certain] (HI, ST). It would also be a third China name in a book that already has two, plus one pending [Certain] (state).
## Bull case
On 5.2x P/E, the stock is below its own 5-year minimum of 5.6x and below the peer median of 6.2x. It trades at 0.8x book while TTM ROE is 17.5% [Certain] (RA). Even the mechanical bear fair value of 31.07 CNY is above the price, and the base is 42.28 CNY [Certain] (valuation). That base already includes a 3.5% country-risk premium [Certain]. H1 2026 brought net profit growth, strong new-business-value growth, better P&C profitability and a first interim dividend, which suggests confidence in capital [Likely] (transcript). CPIC is a scaled, licence-protected composite insurer, and tighter ALM rules may favour incumbents like it over smaller rivals [Likely] (note). With a 5y beta of 0.45, it would also diversify the book [Certain] (ST).
## Decision
```json
{
  "ticker": "SHA:601601",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scaled, licence-protected Chinese composite insurer trades below its own 5-year minimum P/E and at 0.8x book despite a 17.5% ROE, but falling domestic rates and unverifiable insurer-specific metrics leave the discount possibly deserved.",
  "rationale": "Cheap on every own-history multiple, but the ROE gain looks leverage-driven with ROIC flat. Our data cannot see new business value, CSM, solvency or China yields. Momentum is negative, results are imminent, and it would add a third China name. Good but not compelling: avoid, and revisit once the evidence improves.",
  "price_at_decision": 29.32,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601601/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 13%, reversing the five-year improvement the re-rating case depends on.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 13}},
    {"text": "TTM ROIC falls below 8%, under the FY2023 five-year low of 8.3%, showing investment spread compression is hitting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Life new business value growth turns negative in a reported period (company filings/transcripts), signalling loss of distribution momentum."},
    {"text": "P&C combined ratio rises above 100% in a reported period (company filings), eroding the second underwriting engine."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 42.28, "basis": "Steady ROE near 17.5% [RA] and confirmed new-business-value growth [transcript] re-rate P/B toward the ROE-justified level, i.e. the mechanical base fair value 42.28 [valuation]."},
    "base": {"probability": 0.45, "target_price_12m": 33.0, "basis": "Earnings hold, but the China-financials discount persists, so P/B moves only partway back toward its 5y median 1.0x [RA], between the bear and base fair values; we stay below the mechanical base because we cannot verify ROE durability."},
    "bear": {"probability": 0.3, "target_price_12m": 24.0, "basis": "Falling domestic rates compress the life spread [transcript] and ROE slides toward the FY2023 11.9% [RA], so P/B falls below its 5y minimum 0.8x [RA], under the mechanical bear 31.07, which assumes no ROE reversion."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below base fair value less the margin of safety. The decision turns on evidence we cannot verify yet (new business value, solvency, China yields, the effect of the ALM rules), so a lower price would not lift conviction to 4. A re-research after the Oct 28, 2026 results would.",
  "replaces": null,
  "replacement_reason": null
}
```
