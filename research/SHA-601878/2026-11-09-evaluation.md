# Evaluation: Zheshang Securities Co., Ltd. (SHA:601878) — 2026-11-09
## Bear case
This is a low-return, price-taking broker [Likely]. ROIC is 2.2% TTM and has been flat for five years. ROE fell from 10.2% in FY2021 to 6.8% TTM, below any reasonable cost of equity for a CNY reporter [Certain]. The 5-year rise in operating margin to 40.5% is a market-activity swing, not structural gain. It sits far below the 129.6% 2-year high, so earnings track A-share turnover [Likely]. FCF margin swung from 37.1% to -29.1% in a year as trading-book and margin balances absorbed cash. This is a balance-sheet feature of brokers, not a one-off, so there is no cash support [Likely]. P/E of 14.5x is 54% above the peer median of 9.4x [Certain]. Piotroski F is 3, shares are up 1.86% YoY, and the reverse DCF needs 11.2% growth [Certain]. The stock is down 22.7% over 12 months [Certain].
## Bull case
On its own history the stock is cheap: P/E 14.5x and P/B 0.8x both sit below their 5y minimums of 20.3x and 1.0x [Certain]. P/B is in line with peers at 0.8x, so the book is not priced at a premium [Certain]. A revival in A-share turnover would lift brokerage and trading income quickly, given the operating leverage the 2-year margin high shows [Guessing]. Beta of 0.52 limits market drawdown risk [Certain]. The P/E method gives a fair value of 14.20 CNY, and the mechanical fair value is flagged unreliable, so the low FCFE-based base of 4.73 is not decisive [Certain]. None of this adds up to a durable edge, though: the upside depends on a market cycle, not on the business [Likely].
## Decision
```json
{
  "ticker": "SHA:601878",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {"decline_cause": "structural", "decline_evidence": "FCF margin fell from 37.1% to -29.1% in the last 12 months [CF-T,IS-T] because trading-book and margin-lending balances absorbed cash; the note treats this as how the brokerage model works, recurring and erratic (FCF/NI -156.9% in FY2025 after two years above 300% [CF,IS]), not a guided reset or one-off, with ROIC flat at 2.2% [RA] (note sections 2 and 5).", "moat": "none", "key_risk": "high", "key_risk_text": "Earnings depend on A-share turnover and Chinese policy; a weaker market cuts the elevated TTM earnings that flatter the 14.5x P/E [IS-T, note section 3].", "veto": null},
  "thesis": "A cyclical, low-ROIC Chinese broker that is cheap only against its own history and trades above peers on P/E, with no moat or cash support.",
  "rationale": "Returns are well below the cost of equity (ROE 6.8%, ROIC 2.2%), there is no moat, FCF is negative and the P/E is above peers. The upside depends on a market-turnover cycle, not the business. This is not high conviction, so no position.",
  "price_at_decision": 8.87,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601878/2026-11-09.md",
  "triggers": [
    {"text": "ROE (TTM) rises above 10%, showing earnings power returned to the FY2021 level", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "ROIC (TTM) rises above 4%, a durable step up from the five-year 2.2%-3.2% range", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 4}},
    {"text": "Operating margin (TTM) falls below 30%, confirming the earnings cycle has turned down", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.64, "basis": "A-share turnover revives and the operating leverage shown by the 129.6% 2-year margin high [IS-T] returns the price to its 52-week high of 11.64 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 8.87, "basis": "ROE holds near 6.8% [RA] and P/B stays in line with peers at 0.8x [RA]; the price is roughly unchanged, between the unreliable FCFE base of 4.73 and the P/E method's 14.20 [valuation]."},
    "bear": {"probability": 0.3, "target_price_12m": 6.0, "basis": "Market activity cools and the P/E derates from 14.5x toward the 9.4x peer median [RA, peers] on lower earnings, still above the 4.73 FCFE base, which is flagged unreliable [valuation]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3; the obstacle is quality (no moat, ROIC 2.2%, negative FCF), not price, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
