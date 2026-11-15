# Evaluation: Altria Group (MO) — 2026-11-15
## Bear case
The stock has re-rated, not compounded: EV/EBITDA 11.8x and P/FCF 14.4x sit above their 5y maxima of 9.5x and 10.7x [RA] [Certain]. The price is at base fair value (78.67) with a bull of only 80.81 against a bear of 54.87, so skew is poor [Certain]. After a 35.5% 12-month run and 12.9% above the 200-day average, any slowdown in earnings growth risks a de-rating back toward the 5y median multiples [Likely]. Volume is structurally shrinking: adjusted cigarette volume fell an estimated 4% and discount brands' share rose to 34.1% [company-reported] (https://www.sec.gov/Archives/edgar/data/764180/000076418026000114/mo-20260930.htm) [Certain]. The last 12 months show ROIC down 1.4pp and FCF margin down 1.6pp, and the NJOY impairment shows the next-generation strategy has destroyed value [Likely]. Faster FDA approvals could legitimise pouch and vape competitors [Guessing].

## Bull case
This is an exceptional cash franchise: ROIC 37.4%, operating margin 61.2%, FCF margin 44.0% TTM [RA,IS] [Certain]. Pricing power still outruns volume loss: Q3 adjusted EPS grew 4.8%, FY26 guidance was raised and the buyback expanded (Business Wire, 2026-10-29) [Certain]. The FCF yield of 6.93% is real and well covered, net debt/EBITDA has eased to 1.66x and shares fell 0.87% YoY [ST] [Certain]. The reverse DCF implies -0.6% year-1 revenue growth, a low bar [Likely]. The recent dips in ROIC and FCF margin are small and against an unusually high 2024 base rather than erosion; operating margin is flat-to-up over the year [Likely]. P/E of 16.2x sits at the 30% point of its 5y range and in line with peers [RA] [Certain]. Beta 0.46 and a working trend: up 35.5% in 12 months, beating SPY by 25.1pp [Certain].

## Decision
```json
{
  "ticker": "MO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC (-1.4pp) and FCF margin (-1.6pp) slipped over 12 months while operating margin was flat-to-up, Q3 adjusted EPS grew 4.8% and FY26 guidance was raised (Business Wire 2026-10-29); the 2-year highs (2024-09-30) are an unusually high base, not lost pricing power.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating: cash multiples sit above their 5y maxima after a 35.5% run, so a slowdown in EPS growth as cigarette volume falls and discount share rises could compress the multiple back toward its 5y median.",
    "veto": null
  },
  "thesis": "A high-return, pricing-power nicotine franchise whose cash returns are intact, but the price now sits at base fair value with cash multiples above their 5y range.",
  "rationale": "Quality and cash returns are excellent and the trend is working, but the price equals base fair value, the bull case barely exceeds it, and the bear case is far lower. Volume decline is structural and the next-generation bet has been impaired. Good but not compelling: AVOID, with an entry price below fair value.",
  "price_at_decision": 78.64,
  "price_date": "2026-11-13",
  "research_note": "research/MO/2026-11-15.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 30%: pricing no longer offsets volume loss.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "FCF margin (TTM) falls below 40%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "Operating margin (TTM) falls below 55%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 55}},
    {"text": "Net debt / EBITDA rises above 2.5x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 86.74, "basis": "Pricing keeps outrunning volume and the buyback lifts EPS, supporting the DCF bull value of 86.74 [IS,CF,RA] with guidance raised in Q3 (Business Wire 2026-10-29)."},
    "base": {"probability": 0.5, "target_price_12m": 78.67, "basis": "EPS grows in line with raised FY26 guidance and the multiple holds, leaving the price near the blended base fair value of 78.67 [fact sheet fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 54.87, "basis": "Discount-brand share gains and volume decline slow EPS and cash multiples de-rate toward their 5y medians (EV/EBITDA 9.1x [RA]), consistent with the blended bear fair value of 54.87."}
  },
  "entry_price": 62.94,
  "entry_basis": "valuation file: base 78.67 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
