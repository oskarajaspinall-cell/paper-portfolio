# Evaluation: Illinois Tool Works Inc. (ITW) — 2026-10-09
## Bear case
The multiples are not cheap; they sit at their own averages. EV/EBITDA of 17.5x is near its 5y median of 17.6x, P/E of 24.0x is above its median of 23.3x, and the 3.88% FCF yield sits below a 5.28% 10y Treasury [Certain] (fact sheet RA/ST/FRED). The reverse DCF implies 18.7% year-1 revenue growth against guided 4-5% [Certain]. ROIC is flat at 29.3% even as margins widened, and net debt/EBITDA rose from 1.52x to 1.84x [Certain]. Growth is mostly buybacks, with shares down 1.86% a year [Likely]. The stock trails SPY by 16.3pp over 6 months and reports on Oct 23, 2026. The macro overlay tilts moderately toward bear: real yields rose 61bp in 3 months, which pressures both the discount rate and capex demand in Welding and Test & Measurement [Likely] (research/ITW/2026-10-09-macro.md).
## Bull case
This is a best-in-class franchise. ROIC has held near 30% for five years, ROCE has climbed to 41.8%, gross margin has gained 2.8pp, FCF conversion is 91.5% and the Piotroski F-score is 7 [Certain] (fact sheet RA/IS/CF/ST). Q2 2026 organic growth was 4.5%, and both the FY26 EPS and revenue guidance were raised [Certain] (fact sheet news 2026-07-28). Capital returns are dependable: the dividend rose 7% and a $6bn buyback was authorised [Certain]. The stock trades 10-30% below peer medians on P/E, EV/EBITDA and P/FCF, and P/FCF sits in the 3rd percentile of its 5y range [Certain]. The mechanical DCF is harsh for a 30%-ROIC compounder, which makes the downside look larger than it is [Likely]. Still, this is a quality case, not a mispricing [Likely].
## Decision
```json
{
  "ticker": "ITW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 30%-ROIC, 80/20-driven industrial compounder whose multiples sit near their own 5-year medians, so the price already pays for quality, with no margin of safety against a rising-yield capex slowdown.",
  "rationale": "The quality is excellent but already priced in. EV/EBITDA and P/E sit at their 5y medians, the reverse DCF needs 18.7% growth against 4-5% guided, and the macro overlay tilts toward bear with earnings due Oct 23. This is good but not compelling, so no position; cash is acceptable.",
  "price_at_decision": 264.71,
  "price_date": "2026-10-08",
  "research_note": "research/ITW/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 42%, back to the FY2023 level, signalling 80/20 pricing and mix discipline is breaking down.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 42}},
    {"text": "TTM ROIC falls below 27%, below its five-year range, showing returns are being competed away.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 27}},
    {"text": "TTM operating margin falls below 24%, the FY2022 five-year low, reversing the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24}},
    {"text": "Organic revenue growth in the quarterly earnings release stays below 3% for two consecutive quarters, undercutting the raised FY26 guidance."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 288.55, "basis": "Raised FY26 guidance is delivered and capex segments keep accelerating, so EV/EBITDA re-rates to the fair-value bull of 288.55 [fact sheet EV/EBITDA method; IS,RA]; the DCF bull of 134.90 is set aside because its 5.28% risk-free rate understates a 30%-ROIC franchise."},
    "base": {"probability": 0.45, "target_price_12m": 261.14, "basis": "EV/EBITDA holds near its 5y median of 17.6x [RA], matching the fair-value EV/EBITDA base of 261.14, as 4-5% guided growth plus buybacks (shares -1.86% [ST]) only sustain the current multiple; this is well above the 167.26 blended base, which is driven by the harsh DCF."},
    "bear": {"probability": 0.30, "target_price_12m": 238.82, "basis": "Bear weight raised moderately per the macro overlay's toward-bear tilt (research/ITW/2026-10-09-macro.md): rising real yields hit capex segments and the guidance, so the stock revisits its 52-week low of 238.82 [HI], still above the 122.96 blended bear, which the DCF drags down."}
  },
  "entry_price": 238.82,
  "entry_basis": "52-week low of 238.82 [HI], where P/FCF would sit below its 5y low of 25.6x [RA]. That gives a real own-history margin of safety for a 30%-ROIC compounder. The default (base 167.26 x 0.8) is not used because it rests on a DCF the EV/EBITDA method (base 261.14) contradicts.",
  "replaces": null,
  "replacement_reason": null
}
```
