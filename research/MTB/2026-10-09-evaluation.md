# Evaluation: M&T Bank Corporation (MTB) — 2026-10-09
## Bear case
The cheapness is not there on the bank-appropriate method. P/B of 1.2x sits above its own 5y max of 1.1x [RA] [Certain]. The fact sheet's best method, P/B + sustainable ROE, puts base fair value at 219.38 against a 217.56 close [Certain]. The +28% blended upside depends on an FCFE DCF (base 397.67), and bank "FCF" is a noisy number [Likely]. ROE of 10.7% TTM has drifted down over five years [RA] [Certain], and is only modestly above a cost of equity built on a 5.28% risk-free rate [Likely]. The macro overlay is primary and tilts toward bear (moderate): 10y +0.72pp in 3 months and a 2y yield pricing more hikes hit funding costs and AOCI, so book value is pressured [Likely]. Office CRE criticized loans are expected to rise over 1-2 years (Q2 2026 call) [Likely]. Q3 results on Oct 16 are a binary event [Certain].

## Bull case
Earnings and cash flow are cheap: P/E 11.5x is 10% below peers' 12.8x and P/FCF 8.7x is 39% below peers [RA] [Certain]. The reverse DCF implies -8.5% revenue in year 1, harsher than the Q2 2026 call's record EPS, loan growth and nine straight quarters of lower criticized commercial loans [Likely]. Capital return is heavy: shares -7.97% YoY and a $1.50 quarterly dividend [ST] [Certain]. Beta 0.61 and conservative underwriting make it a defensive financial [Likely]. The stock is 7.8% below its 50-day MA with RSI 31.9, so sentiment is washed out ahead of earnings [Certain]. If rates stabilise, P/B could rerate toward the blended base of 278.81 [Guessing].

## Decision
```json
{
  "ticker": "MTB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A conservatively underwritten regional bank that is cheap on P/E and P/FCF but fairly priced on P/B + ROE, its bank-appropriate method, while the rate path is moving against its book value.",
  "rationale": "The P/B + ROE fair value (219.38) is roughly the price, P/B is above its 5y max, ROE is near the cost of equity, and the primary macro overlay tilts toward bear. Upside depends on a bank FCFE DCF we do not trust. Good but not compelling: conviction 3, so no position.",
  "price_at_decision": 217.56,
  "price_date": "2026-10-08",
  "research_note": "research/MTB/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 8%, near the cost of equity, showing returns no longer cover capital (now 10.7%).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 25%, under the FY2022 low of 26.0%, signalling NIM or credit-cost compression.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "TTM ROE rises above 12%, above the FY2021 5y high of 10.9%, which would justify the premium P/B and turn the view constructive.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12}},
    {"text": "The Q3 2026 or later earnings release reports a rise in non-accrual or criticized commercial loans, ending the nine-quarter decline cited on the Q2 2026 call."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 260, "basis": "Rates stabilise and NIM holds (overlay macro_bull), so the stock moves past the P/B + ROE bull of 240.13 toward the blended base of 278.81 [fact sheet Fair value]. Capped below that because the FCFE leg is unreliable for a bank; probability trimmed for the overlay's moderate bear tilt (research/MTB/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 222, "basis": "P/B + ROE base fair value of 219.38 [fact sheet Fair value], ROE ~10.7% [RA], plus buyback accretion (shares -7.97% YoY [ST]); P/B already above its 5y max of 1.1x [RA] limits rerating."},
    "bear": {"probability": 0.3, "target_price_12m": 185, "basis": "Overlay macro_bear: further hikes (2y 4.77% vs fed funds 3.88%) deepen AOCI marks and office CRE criticized loans rise (Q2 2026 call, https://stockanalysis.com/stocks/mtb/transcripts/649590-q2-2026/), so P/B falls back below its 5y median of 1.1x [RA], under the P/B + ROE bear of 201.98; probability raised for the moderate bear tilt (research/MTB/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
