# Evaluation: International Games System Co.,Ltd. (TPEX:3293) — 2026-11-15
## Bear case
The price already reflects the quality. The base fair value of 843.28 TWD is only +5.5% above the 799.00 close, and the bear value of 562.38 is -29.6% away, so the skew is thin [Certain]. Valuation support comes partly from the trend: the price is 6.9% above its 200-day average. If growth slows, an extended price risks a de-rating towards the EV/Revenue value of 634.92 [Likely]. P/B of 12.1x is 90% above peers [Certain]. Revenue is hit-driven content sold to gaming operators, with licensing exposure in each market, and the revenue mix by country is [data unavailable]. The macro overlay could not size that exposure [Likely]. ROCE sits 32.5pp below its 2-year high of 112.6%, and FCF margin is 2.3pp below its 56.3% peak. These are small giveback signs from a very high base [Likely]. The moat comes from a proprietary game library, which is unverified from a primary source [Guessing].
## Bull case
The economics are exceptional and still improving. Gross margin is 97.7%, operating margin 59.8% (+1.2pp over the year) and FCF margin 54.0% (+3.7pp), with ROE at 74.3% [Certain]. ROIC's 5-year "falling" label is a base effect from FY2021's 716.4%. Over the last 12 months ROIC rose from 277.6% to 475.1% [Certain]. The company holds net cash (-1.06x net debt/EBITDA), FCF conversion is 105.0% and dilution is small at 0.60% [Certain]. P/E of 17.8x and P/FCF of 16.6x sit low in their own 5-year ranges and about 40% below peers, with a 6.03% FCF yield [Certain]. The reverse DCF implies only 6.9% year-1 growth [Certain]. Beta is 0.28, and the stock beat SPY by +8.7pp over 6 months [Certain]. If margins hold, the DCF base of 947.47 is reachable [Likely].
## Decision
```json
{
  "ticker": "TPEX:3293",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 12 months (ROIC 277.6% to 475.1%, operating margin +1.2pp, FCF margin +3.7pp [RA-T, IS-T, CF-T]); the 5-year ROIC fall is a base effect from FY2021's 716.4%.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Hit-driven game content and operator licensing in unverified foreign markets could let margins slip from a 59.8% peak, de-rating a price already near base fair value.", "veto": null},
  "thesis": "An exceptional net-cash, 54%-FCF-margin games developer whose price already sits close to its mechanical base fair value, leaving a thin skew despite improving returns.",
  "rationale": "The quality is top-tier and still improving, but the price is near the base fair value and the trend support is modest: the 12-month change is +7.4%. Country mix and moat are unverified. Good but not compelling at 799.00, so AVOID, with an entry price where a margin of safety returns.",
  "price_at_decision": 799.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPEX-3293/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 50%, under the FY2022 five-year low of 50.3%, showing content or pricing erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 40%, under the FY2024 five-year low of 41.0%, showing cash generation is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "TTM gross margin falls below 95%, under the five-year low of 95.9%, signalling a mix shift away from licensed content.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 95}},
    {"text": "Net debt/EBITDA on the ratios page turns positive from -1.06x TTM, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1224.18, "basis": "Margins hold at the 59.8% operating level and the market pays the DCF-led bull fair value of 1,224.18 [IS, valuation file]."},
    "base": {"probability": 0.5, "target_price_12m": 843.28, "basis": "Returns stay near current levels and P/E stays near 17.8x against a 15.9x 5y median, in line with the blended base fair value of 843.28 [RA, valuation file]."},
    "bear": {"probability": 0.25, "target_price_12m": 562.38, "basis": "Hit-driven content fades and the multiple de-rates towards the EV/Revenue value of 634.92 and the blended bear value of 562.38 [RA, valuation file]."}
  },
  "entry_price": 674.62,
  "entry_basis": "valuation file: base 843.28 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
