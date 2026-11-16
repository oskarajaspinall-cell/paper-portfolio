# Evaluation: ASML Holding N.V. (AMS:ASML) — 2026-11-16
## Bear case
The price already pays for a long AI up-cycle: the reverse DCF needs 35.4% year-1 revenue growth, and the mechanical base fair value of 581.47 EUR sits 56.6% below the 1,338.80 EUR close; even the bull fair value is 17.8% below it [Certain]. TTM margins and returns are at 2-year highs, so this is peak-cycle earnings on a P/E of 37.4x, above the peer median [Certain]. The FCF margin swing (11.9% in FY2023, 53.6% TTM) is lumpy prepayment timing, so P/FCF below its 5y minimum overstates cheapness [Likely]. The trend has broken: 4.4% below the 200-day average, -16.8% over 3 months, trailing SPY by 13.8pp [Certain]. The macro overlay flags the real yield up 0.47pp in 3 months on a long-duration multiple [Certain]. China/export-control exposure is unquantified [Guessing].
## Bull case
This is one of the best businesses in the universe: ROIC 92.1% TTM, operating margin 38.6% and rising on a rolling basis, net cash, Piotroski F 8 and a shrinking share count [Certain]. The 5-year FCF-margin decline reverses over the last 12 months (27.8% to 53.6%), driven by prepayments and record sales rather than any loss of position, and guidance was raised after a strong Q3 [Likely]. Its near-monopoly in advanced lithography is a wide moat [Likely]. The de-rating leaves P/E at 21% and EV/EBITDA at 12% of their 5-year ranges, and the 4.24% FCF yield is real [Certain]. If AI capex holds, earnings growth can carry the price back to the 52-week high of 1,741.00 [Guessing]. But nothing in the evidence makes the current price a discount; the case needs the up-cycle to run.
## Decision
```json
{
 "ticker": "AMS:ASML",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing is falling over 1 or 3 years: ROIC, operating margin and FCF margin are all rising on the rolling view [RA-T, IS-T, CF-T]; the 5-year FCF-margin fall is lumpy prepayment timing now reversed.", "moat": "wide", "key_risk": "medium", "key_risk_text": "An AI-capex slowdown or a higher real yield de-rates a 37.4x P/E built on peak-cycle margins, with the price already below its 200-day average.", "veto": null},
 "thesis": "A wide-moat lithography monopoly at peak returns whose price, below its 200-day average and far above every mechanical fair value, already discounts a long AI up-cycle.",
 "rationale": "Superb quality and a wide moat, but the price offers neither a discount (base fair value far below) nor trend strength (below the 200-day average). Good but not compelling: AVOID, waiting for a lower price or a restored uptrend.",
 "price_at_decision": 1338.80,
 "price_date": "2026-11-13",
 "research_note": "research/AMS-ASML/2026-11-16.md",
 "triggers": [
  {"text": "TTM operating margin falls below 33%, reversing the rolling expansion and signalling the up-cycle is fading.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 33}},
  {"text": "TTM ROIC falls below 60%, back to its FY2021 level.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
  {"text": "TTM gross margin falls below 49%, under the five-year low, signalling pricing power erosion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 49}},
  {"text": "A new or changed China export-control rule on lithography is confirmed by an official or company source."}
 ],
 "scenarios": {
  "bull": {"probability": 0.25, "target_price_12m": 1741.00, "basis": "AI capex holds and the raised guidance is delivered, so the price returns to its 52-week high of 1,741.00 [HI]; above the mechanical bull fair value 1,100.35 because that model is blind to the current up-cycle."},
  "base": {"probability": 0.45, "target_price_12m": 1399.84, "basis": "P/E holds near its 5y median 35.7x [RA] as earnings grow modestly, leaving the price around its 200-day average 1,399.84 [HI]; above the base fair value 581.47 because the through-cycle DCF ignores the rolling margin step-up [IS-T]."},
  "bear": {"probability": 0.30, "target_price_12m": 1100.35, "basis": "Capex slows and the multiple compresses toward the mechanical bull fair value 1,100.35 [fact sheet]; probability raised a little for the macro overlay's small toward-bear tilt on the real yield (research/AMS-ASML/2026-11-16-macro.md)."}
 },
 "entry_price": 465.18,
 "entry_basis": "valuation file: base 581.47 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]). Price is the obstacle; quality is not.",
 "replaces": null,
 "replacement_reason": null
}
```
