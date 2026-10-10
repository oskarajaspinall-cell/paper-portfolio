# Evaluation: General Dynamics Corporation (GD) — 2026-10-10
## Bear case
This is not cheap on earnings. P/E of 20.2x sits above its 5y median of 20.1x and 17% above peers; EV/EBITDA of 14.3x is at its 5y median and 13% above peers [Certain]. The "cheap" signal rests on P/FCF of 13.9x, below its 5y minimum, but that comes from TTM FCF conversion of 143.4% against 84.3%-114.7% in prior years. That looks like working-capital timing that will reverse, not a permanent step-up [Likely]. The DCF-driven base fair value of 392.42 runs on that elevated FCF, while the EV/EBITDA method gives 330.10, roughly today's price [Certain]. Gross and operating margins have fallen over five years (15.4% / 10.4% TTM) [Certain]. A CEO handover on 1 Jan 2027 and Q3 results on Oct 30 are near-term unknowns [Certain]. The stock trails SPY by 20.1pp over 12 months with no catalyst yet [Certain].

## Bull case
Electric Boat's sole-source Columbia/Virginia submarine franchise and Land Systems' Abrams/Stryker monopoly give multi-decade backlog visibility [Certain]. ROIC has risen to 14.6% TTM and net debt/EBITDA has fallen from 2.20x to 0.78x, so the balance sheet now has room for buybacks [Certain]. The reverse DCF implies just 0.2% year-1 growth, a low bar for a backlog-funded prime [Likely]. FCF yield is 7.19%, P/B sits at the bottom of its 5y range and 12% below peers, and beta is 0.33 [Certain]. RSI of 30.6 and the drop from the 400.00 high suggest pessimism is already in the price [Likely]. The CEO successor is an insider, with Novakovic staying on as Executive Chairman [Likely].

## Decision
```json
{
  "ticker": "GD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, deleveraging sole-source defense prime whose apparent cheapness rests on a likely-transient TTM FCF spike, while earnings multiples sit at or above its own 5-year median and peers.",
  "rationale": "The franchise is good, but the valuation is not compelling. P/E and EV/EBITDA are at their 5y medians and above peers. The P/FCF discount depends on 143% FCF conversion that probably reverses. The EV/EBITDA fair value (330.10) equals the price. Margins are drifting down, and Q3 results and the CEO transition are pending. Good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 331.27,
  "price_date": "2026-10-09",
  "research_note": "research/GD/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9%, near the FY2023 five-year low of 8.8%, showing Gulfstream/IT-services mix or program execution is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "TTM ROIC falls below 11%, reversing the improvement to 14.6% TTM.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 6%, under the FY2024 five-year low of 6.7%, showing cash conversion has deteriorated rather than normalised.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "A 10-K or earnings release discloses a multi-year delay, cost overrun charge or cancellation on the Columbia-class or Virginia-class submarine programs."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 420.0, "basis": "Backlog execution and buybacks from a 0.78x net-debt/EBITDA balance sheet [BS,IS] re-rate the stock past its 400.00 52-week high [HI], between the 392.42 base and 457.80 bull blended fair value [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 345.0, "basis": "EV/EBITDA holds near its 5y median of 14.4x [RA] as FCF conversion normalises from 143.4% [CF,IS], close to the 330.10 EV/EBITDA base value and below the DCF base, which runs on the elevated TTM FCF."},
    "bear": {"probability": 0.25, "target_price_12m": 275.0, "basis": "FCF conversion reverts and operating margin keeps falling from 10.4% [IS], pushing EV/EBITDA below the 304.39 bear EV/EBITDA value toward the 238.11 blended bear fair value [fact sheet Fair value]."}
  },
  "entry_price": 313.94,
  "entry_basis": "valuation file: base 392.42 x 0.8; a 20% margin of safety under base fair value would make the backlog quality compelling despite the earnings-multiple premium to peers.",
  "replaces": null,
  "replacement_reason": null
}
```
