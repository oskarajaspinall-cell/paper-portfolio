# Evaluation: Bridgestone Corporation (TYO:5108) — 2026-11-16
## Bear case
Earnings multiples already price the recovery: P/E 12.6x sits at 76% of its 5y range and 42% above the peer median, EV/EBITDA 5.7x at 96% of range, and P/B 1.5x above its 5y max [RA] [Certain]. The price is extended after the trend run (+20.1% over the 200-day average, RSI 67.7, 6-month gain 32.2%) [Certain]; if margins slip back, a de-rating toward the EV/EBITDA leg's 4,100.61 JPY base is the natural path [Likely]. The Direction change (TTM ROIC 10.6% -> 13.9%, operating margin 8.9% -> 13.3%) contradicts a falling 5-year record (FY ROIC 12.9% -> 11.5%), and part of the lift is yen depreciation, not structure [Likely]. Raw-material and Middle East cost pressure plus the Tosu plant fire remain open [Likely]. The DCF-led base fair value is fragile: the bear DCF is 438.74 JPY [Certain]. Americas exposure is unquantified [Guessing].

## Bull case
A global tyre leader with scale, brand and dealer networks delivering record nine-month revenue and adjusted operating profit, with revenue guidance raised (Q3 call) [Likely]. Returns are at five-year highs on the trailing view: ROIC 13.9%, ROCE 13.4%, operating margin 13.3%, all rising over 1 and 3 years [Certain]. Cash backs the earnings: FCF margin 9.9%, conversion 106.3%, FCF yield 8.59%, P/FCF 11.6x near its 5y low [Certain]. The balance sheet is near net cash (0.17x net debt/EBITDA, Altman Z 3.60) and shares fell 3.23% YoY on buybacks [Certain]. The price implies -4.3% year-1 revenue growth, undemanding if margins hold, and the base fair value of 5,555.33 JPY sits above the close [Likely]. Low beta (0.48) and a working uptrend fit the mandate [Certain].

## Decision
```json
{
  "ticker": "TYO:5108",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing falls over 1 or 3 years: TTM ROIC 10.6% -> 13.9%, operating margin 8.9% -> 13.3%, FCF margin 8.6% -> 9.9% [RA-T, IS-T, CF-T]; the 5-year FY dip (ROIC 12.9% -> 11.5%) has reversed.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Margin reversal from raw-material and Middle East costs, the Tosu fire or a yen reversal, de-rating an earnings multiple already near its 5y high (Q3 call, /quote/tyo/5108/transcripts/727158-q3-2026/).", "veto": null},
  "thesis": "A cash-generative, near-net-cash tyre leader whose margins have recovered to five-year highs, but whose earnings multiples already sit near the top of their own range.",
  "rationale": "Quality, cash conversion and balance sheet are sound and the trend is working, but returns are only mid-teens, the recovery is partly yen-driven and P/E, EV/EBITDA and P/B are at or above their 5y highs. Good but not compelling; no position.",
  "price_at_decision": 4402.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-5108/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 5%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Net debt/EBITDA rises above 1.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 5555.33, "basis": "Margins hold at the TTM 13.3% and the market pays the mechanical base fair value of 5,555.33 JPY [fact sheet Fair value], backed by an 8.59% FCF yield [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 4500, "basis": "P/E stays near today's 12.6x, already at 76% of its 5y range [RA], so the return is modest earnings growth plus buybacks (shares -3.23% YoY [ST]); below the DCF-led base because the EV/EBITDA leg gives 4,100.61 JPY."},
    "bear": {"probability": 0.25, "target_price_12m": 3570.19, "basis": "Cost pressure and the Tosu fire (Q3 call) push margins back toward the FY2024 10.8% [IS] and EV/EBITDA de-rates to the bear EV/EBITDA value of 3,570.19 JPY [fact sheet Fair value]."}
  },
  "entry_price": 3570.19,
  "entry_basis": "The valuation file's base 5,555.33 x 0.8 sits above the close, so anchor instead on the EV/EBITDA bear value of 3,570.19 JPY [RA], where earnings multiples would be back near their 5y median and give a real discount.",
  "replaces": null,
  "replacement_reason": null
}
```
