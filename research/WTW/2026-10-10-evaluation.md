# Evaluation: Willis Towers Watson Public Limited Company (WTW) — 2026-10-10
## Bear case
The broking cycle is turning against WTW: its own survey shows large commercial property rates down 14.5% in Q2 2026, the sharpest decline in a decade [Likely], which compresses commission revenue industry-wide. Gross margin has already slipped from 45.0% to 42.5% TTM [Certain], and net debt/EBITDA has risen from 0.34x to 1.93x [Certain]. The "cheapness" is partial: P/E of 18.2x sits at the 58th percentile of its own 5y range, not at a low [Certain]; only EV/EBITDA is below its 5y minimum. The stock has lagged SPY by 29.5pp over 12 months [Certain] and reports Q3 on Oct 29, 2026, so a soft organic-growth print could reset estimates lower [Guessing]. Altman Z of 1.39 and Piotroski F of 5 [Certain] offer no quality confirmation. Holding peers at their own 5y minimums on every multiple is a better use of capital [Likely].
## Bull case
Returns have structurally improved: ROIC 9.4% to 14.5% TTM, ROCE 8.6% to 15.7%, operating margin 19.4% to 23.7% [Certain]. FCF conversion of 107.9% and a 6.14% FCF yield fund buybacks that cut shares 3.98% YoY [Certain]. WTW trades at a discount to MMC, AON, AJG and BRO on every multiple (P/E -12%, EV/Sales -22%) [Certain] and EV/EBITDA 11.7x is below its own 5y minimum of 12.2x [Certain]. The fair-value base of 347.25 is 17.2% above the 296.26 close [Certain]. A 0.47 beta [Certain] and recurring advisory fees cushion a softening pricing cycle [Likely]; the FY2024 loss was a one-off, not underlying economics [Likely].
## Decision
```json
{
  "ticker": "WTW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A broker with rising returns and buyback-supported FCF trades at a peer discount, but a decade-sharp drop in commercial property rates and a mid-range own-history P/E leave the upside too modest for high conviction.",
  "rationale": "Quality is improving and the peer discount is real, but P/E sits mid-range in its own 5y history, the pricing cycle is softening against commissions and Q3 results are three weeks away. A 17.2% gap to base fair value is good, not compelling, against holdings bought at 5y-minimum multiples. Conviction 3: AVOID, with an entry price.",
  "price_at_decision": 296.26,
  "price_date": "2026-10-09",
  "research_note": "research/WTW/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9.4%, the FY2021 five-year low, reversing the returns improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9.4}},
    {"text": "TTM operating margin falls below 19.4%, the FY2021 level, showing the softening pricing cycle is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19.4}},
    {"text": "TTM FCF margin falls below 11.6%, the FY2023 level, undermining buyback capacity.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11.6}},
    {"text": "Organic revenue growth reported in the quarterly earnings release turns negative for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 370.14, "basis": "Returns keep rising (ROIC 14.5% TTM [RA]) and the peer P/E discount closes, matching the fact sheet's bull fair value of 370.14 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 338.25, "basis": "EV/EBITDA recovers from 11.7x toward its 5y median 13.5x [RA], the fact sheet's EV/EBITDA base of 338.25, held a little below the 347.25 blended base because softening property rates (WTW survey, https://www.globenewswire.com/news-release/2026/10/01/3373107/0/en/commercial-property-rates-post-sharpest-decline-in-a-decade-willis-report-finds.html) cap P/E re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 240.62, "basis": "A soft-market commission slowdown revisits the 52-week low of 240.62 [HI]; set above the mechanical 175.80 bear because that P/E bear (114.11) leans on the distorted FY2024 loss year [RA], while the EV/EBITDA bear is 299.17."}
  },
  "entry_price": 277.80,
  "entry_basis": "valuation file: base 347.25 x 0.8 = 277.80; at that margin of safety the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
