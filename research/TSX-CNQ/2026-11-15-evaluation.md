# Evaluation: Canadian Natural Resources Limited (TSX:CNQ) — 2026-11-15
## Bear case
The last-12-month rebound (ROIC 12.5% to 17.9%, operating margin 23.0% to 30.7% [RA-T, IS-T]) tracks higher crude prices and output, not a structurally better business [Likely]; the five fiscal years still show ROIC falling from 13.7% to 10.8% and operating margin from 31.6% to 21.1% [RA, IS] [Certain]. The **Direction change** is therefore cyclical: it flatters the score at what may be a commodity high [Likely]. The price is extended on asset and cash multiples: EV/EBITDA 7.0x sits at 89% of its 5y range and above peers' 5.6x, P/B 3.1x and EV/Sales 3.3x exceed their 5y maxima [RA] [Certain]. The mechanical base fair value of 60.55 CAD is below the 70.91 close [Certain]. After a +56.1% year, a softer oil tape or wider heavy-oil differentials would de-rate the multiple and cut earnings at once [Likely]. Buybacks at these multiples add less value [Guessing].

## Bull case
A low-decline, long-life asset base with a strong balance sheet: net debt/EBITDA 0.67x, Piotroski 8 [ST] [Certain]. FCF yield is 8.99% and management has reached its net debt target, now directing all free cash flow to buybacks on top of the dividend (https://www.nasdaq.com/articles/canadian-natural-resources-limited-achieves-13-billion-net-debt-target-and-targets-100) [Likely]. P/E 10.5x is below peers' 12.6x and P/FCF 11.1x in line with peers [RA] [Certain]. Trend is healthy: 9.4% above the 200-day, 50-day 10.0% above the 200-day, beating SPY by 45.7pp over 12 months [ST, HI] [Certain]. Early Horizon maintenance completion supports next-quarter production [Likely]. The fair value rests on EV/EBITDA alone because Reserve NAV is [data unavailable], so it likely understates long-life reserves [Likely].

## Decision
```json
{
  "ticker": "TSX:CNQ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over the last 1 or 3 years: TTM ROIC, ROCE, operating and FCF margin all rose (ROIC 12.5% to 17.9%) [RA-T, IS-T, CF-T]; the 5-year fiscal declines reflect the commodity cycle.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A fall in crude prices or wider Canadian heavy-oil differentials reverses the cyclical rebound in returns while the extended multiple (EV/EBITDA at 89% of its 5y range, P/B above its 5y max) de-rates.",
    "veto": null
  },
  "thesis": "A low-leverage, long-life oil sands producer now returning all free cash flow through buybacks is working, but its rebound in returns is commodity-driven and its price already sits above the mechanical fair value at near-peak cash multiples.",
  "rationale": "Quality, balance sheet and trend are good, but the scorecard gives conviction 3: the return rebound is cyclical, EV/EBITDA and P/B are at or above the top of their 5y ranges, and the base fair value is below the price. Good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 70.91,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-CNQ/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, back to the level of a year earlier, showing the return rebound has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 18%, under the FY2023 low of 20.7%, so buyback capacity shrinks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.67x TTM), abandoning the net debt target.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Shares change YoY turns positive, i.e. issuance replaces buybacks.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 80.0, "basis": "Oil stays firm and all-FCF buybacks on an 8.99% FCF yield [ST] hold EV/EBITDA near its 5y max of 7.3x [RA], taking the price above the 78.60 52-week high [HI]; above the mechanical bull of 61.22 because NAV is unavailable and reserves are long-life."},
    "base": {"probability": 0.5, "target_price_12m": 66.0, "basis": "EV/EBITDA drifts from 7.0x toward its 5y median 6.3x [RA] as returns normalise, partly offset by buybacks; above the mechanical base 60.55 [valuation] for the shareholder-yield support."},
    "bear": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Crude or heavy-oil differentials weaken, reversing the rebound in operating margin from 23.0% to 30.7% [IS-T] while the multiple de-rates toward the mechanical bear of 42.52 [valuation]."}
  },
  "entry_price": 48.44,
  "entry_basis": "valuation file: base 60.55 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
