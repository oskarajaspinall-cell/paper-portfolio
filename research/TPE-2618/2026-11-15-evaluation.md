# Evaluation: EVA Airways Corp. (TPE:2618) — 2026-11-15
## Bear case
This is an airline at or past peak-cycle profitability. Operating margin has faded from 16.6% to 14.2% over the last 12 months and sits 4.0pp below its 2-year high; ROCE fell from 13.5% to 12.4% and ROIC is 2.6pp below its 19.9% high [Certain]. The Direction change lines read as normalisation from a post-2022 upcycle, not a one-off dip [Likely]. The FCF margin rebound to 17.8% looks like timing, as FCF conversion was 106.1% in FY2025 [Likely]. The price is extended: 21.4% above its 200-day average, at its 52-week high with RSI 69.4, after a 38.6% six-month run, so a slower Q3 on Nov 17, 2026 could de-rate it quickly [Likely]. P/B of 1.8x is at the top of its 5-year range and above peers [Certain]. The 171.20 base fair value is flagged unreliable [Certain]. Fuel and Taiwan geopolitics are unhedgeable [Guessing].

## Bull case
The balance sheet has been transformed: net debt/EBITDA fell from 3.63x to 0.36x, Piotroski F is 7 and there is no dilution [Certain]. ROIC of 17.2% TTM is flat over the year and far above the FY2022 4.0% [Certain]. On cash it is cheap: a 17.39% FCF yield, P/FCF 5.8x, EV/EBITDA 4.5x below its 5-year minimum and P/E 20% below the peer median [Certain]. The reverse DCF implies a -24.2% revenue fall in year 1, a trough already priced [Likely]. Cargo demand tied to AI supply chains and premium cabins supported record passenger revenue per the Q1 2026 call headline [Guessing]. The trend is strong: above its 200-day average with relative strength vs SPY of +37.0pp over 6 months [Certain]. Beta of 0.51 keeps market risk low [Certain].

## Decision
```json
{
  "ticker": "TPE:2618",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "Operating margin 16.6% -> 14.2% and ROCE 13.5% -> 12.4% over the last 12 months [IS-T, RA-T], with ROIC 2.6pp below its 2-year high: a cyclical airline normalising from a post-2022 peak, not a guided reset or one-off; no company source verifies a recovery (note section 2).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Peak-cycle margin normalisation (fuel, fares) arriving into an extended price (52-week high, RSI 69.4) ahead of Nov 17, 2026 results, de-rating earnings and multiple together.",
    "veto": null
  },
  "thesis": "A deleveraged, cash-rich Taiwanese airline trading at low cash multiples, but with margins fading from a cyclical peak and no durable moat, so the cheapness is mostly the cycle being priced.",
  "rationale": "Balance sheet, FCF yield and trend are real, but a commodity airline with falling 12-month margins, no verified moat and a price at its 52-week high before results is good, not compelling. The scorecard lands well below the buy bar; cash is acceptable.",
  "price_at_decision": 47.75,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2618/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, giving up most of the post-2022 step-up from 4.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 10%, showing the cycle has turned rather than faded.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) rises above 1.5x (0.36x now), signalling fleet capex or losses are re-levering the balance sheet."},
    {"text": "TTM FCF margin falls below 8% for a second consecutive quarter, back under the 8.7% of a year earlier."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 68.24, "basis": "Results confirm cargo and premium strength and EV/EBITDA re-rates toward its 5y median 5.4x [RA]; the EV/EBITDA method's bull value 68.24 [fact sheet fair value], used instead of the through-cycle DCF, which is flagged unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 46.76, "basis": "Margins keep fading as in the rolling table [IS-T] and EV/EBITDA holds near today's 4.5x, below its 5y minimum [RA]: the EV/EBITDA method's base value 46.76, roughly today's price."},
    "bear": {"probability": 0.30, "target_price_12m": 41.45, "basis": "A weak Nov 17, 2026 report extends the operating-margin fade (16.6% -> 14.2% [IS-T]) and unwinds the 21.4% premium to the 200-day average [ST,HI]: the EV/EBITDA method's bear value 41.45."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2, so no entry price is required: the obstacle is a cyclical margin fade with no moat [IS-T], which a lower price alone would not fix.",
  "new_evidence": {"type": "method_change", "text": "The 2026-10-25 AVOID at conviction 3 predates the 2026-11-09 scorecard, which now sets conviction; the price also moved from 42.20 to 47.75 [HI]."}
}
```
