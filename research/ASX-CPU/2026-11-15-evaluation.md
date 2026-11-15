# Evaluation: Computershare Limited (ASX:CPU) — 2026-11-15
## Bear case
Profits sit near peak: operating margin went from 12.4% (FY2022) to 28.5% TTM, and part of that is margin income on client cash, which falls with policy rates [Likely]. The macro overlay tilts toward bear (small): favourable rates look priced, and a rate-cut surprise or higher real yields would hit both earnings and the 29.0x P/E [Guessing]. The rolling year is flat, not rising: operating margin -0.6pp and FCF margin -0.4pp [Certain]. The price is extended: +23.8% above the 200-day average, RSI 73.1, at its 52-week high, with EV/Sales and P/B above their 5y maxima and P/FCF at 95% of its range [Certain]. An extended price risks a de-rating if FY2027's guided mid-single-digit EPS growth disappoints [Likely]. The mechanical DCF base of 26.15 sits far below the 44.73 close; the reverse DCF needs 17.4% year-1 revenue growth [Certain]. Revenue by country is unverified [Certain].

## Bull case
A high-return, unlevered franchise: ROE 28.0%, ROIC 26.2% at its 2-year high, net debt/EBITDA 0.28x, Altman Z 5.30, Piotroski 7 [Certain]. FCF margin 24.5% and FCF/net income 129.5% fund buybacks (shares -1.45% YoY) [Certain]. Registry and plan administration carry switching costs and scale [Likely]. All three core businesses grew in FY2026 and FY2027 guidance was affirmed at the AGM [Likely]. The trend is strong: +27.6% over 12 months, beating SPY by +17.2pp, with a 4.48% FCF yield [Certain]. P/E is only at 33% of its 5y range, and the P/E method's base of 39.28 is far closer to the price than the DCF, which capitalises a margin that may persist if US rates hold higher, as the 2y yield implies [Likely].

## Decision
```json
{
  "ticker": "ASX:CPU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Rolling 12 months: ROIC +2.3pp, operating margin -0.6pp and FCF margin -0.4pp, flat rather than falling [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Margin income on client balances fades with lower US rates while the extended multiple de-rates from near-peak profits (macro overlay, tilt toward bear).", "veto": null},
  "thesis": "A high-return, unlevered registry and plan-administration franchise in a strong uptrend, but on near-peak, rate-assisted margins and an extended multiple.",
  "rationale": "Quality, balance sheet and trend strength are real, but earnings lean on rate-sensitive margin income near peak, the price is extended above every cash multiple's 5y range, and the macro tilt is toward bear. Scorecard conviction 3: good but not compelling, so AVOID, no position.",
  "price_at_decision": 44.73,
  "price_date": "2026-11-13",
  "research_note": "research/ASX-CPU/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROE falls below 22%, giving up most of the rise from 10.3% (FY2022) to 28.0%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 22}},
    {"text": "TTM operating margin falls below 24%, showing margin income on client balances is fading.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24}},
    {"text": "TTM FCF margin falls below 20%, back near the FY2023 level of 19.9%, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.28x TTM now) without an earnings-accretive acquisition.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 46.43, "basis": "Rates hold higher (macro overlay), margin income persists and the P/E method's bull value of 46.43 [IS,RA] is reached on affirmed FY2027 guidance [OV]."},
    "base": {"probability": 0.45, "target_price_12m": 39.28, "basis": "P/E drifts toward its 5y median 24.9x [RA] as guided mid-single-digit EPS growth meets an extended price; the P/E method's base of 39.28 is used because the DCF base of 26.15 capitalises a harsh margin path."},
    "bear": {"probability": 0.30, "target_price_12m": 26.15, "basis": "Rate cuts shrink margin income and the multiple de-rates to the mechanical DCF base of 26.15 [IS,BS,CF]; probability raised a little for the macro overlay's small tilt toward bear (research/ASX-CPU/2026-11-15-macro.md)."}
  },
  "entry_price": 20.92,
  "entry_basis": "valuation file: base 26.15 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]).",
  "replaces": null,
  "replacement_reason": null
}
```
