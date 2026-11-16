# Evaluation: Paylocity Holding Corporation (PCTY) — 2026-11-16
## Bear case
The price is extended: +39.2% above the 200-day average and +71.0% over six months, near the 52-week high of 181.56 [Certain]. The reverse DCF needs 16.2% year-1 revenue growth against 10.7% reported in Q1 FY27, so if growth slows the stock de-rates toward its 5y P/FCF low of 11.3x [Likely]. The price sits above the mechanical base fair value of 161.22, and P/E and EV/EBITDA are well above ADP/PAYX/PAYC [Certain]. The Direction change line: ROIC is 4.4pp below its 2-year high of 29.5%; the note ties this to acquisition capital (Airbase, Aidora), a temporary denominator effect while operating margin and FCF margin both rose over the last year [Likely]. Net cash has gone to roughly zero (-0.02x) as revolver draws funded buybacks [Certain], and the amortisation change flatters margins slightly [company-reported] [Likely]. Falling rates would cut float income [Guessing].
## Bull case
A high-return, still-improving mid-market HCM franchise: TTM ROIC 25.1%, operating margin 21.7% (9.9% in FY2022), FCF margin 27.1%, and every rolling metric rose over the last year [Certain]. Q1 FY27 beat guidance and the FY27 revenue and margin outlook was raised [Likely]. Payroll switching costs and embedded client data support a narrow moat, with gross margin steady near 68.9% [Likely]. Despite the run, multiples sit low in their own 5y ranges (P/E 16th, EV/EBITDA 11th, P/FCF 13th percentile) and the FCF yield is 5.30% [Certain]. Share count fell 3.92% YoY [Certain]. Beta of 0.41 and falling short interest (-20.0%) suggest a durable, not speculative, uptrend [Likely]. A business that is working, with momentum confirmed by results [Likely].
## Decision
```json
{
  "ticker": "PCTY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Rolling ROIC, ROCE, operating and FCF margin all rose over the last year [RA-T, IS-T, CF-T]; ROIC below its 2-year high reflects acquisition capital (Airbase, Aidora) per the note.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The price implies 16.2% year-1 revenue growth versus 10.7% reported; a growth slowdown would de-rate an extended price (+39.2% over the 200-day).",
    "veto": null
  },
  "thesis": "A high-return, improving mid-market HCM franchise in a strong uptrend, priced above its mechanical base fair value but low in its own 5-year multiple range.",
  "rationale": "The scorecard gives 3: top quality, rising rolling returns, a clean balance sheet and trend strength, but only a narrow moat and a medium de-rating risk, with the price above base fair value and implying growth faster than reported. Good but not compelling, so AVOID; cash is acceptable (owner rule: high conviction only).",
  "price_at_decision": 178.22,
  "price_date": "2026-11-13",
  "research_note": "research/PCTY/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, giving up the rolling rise to 25.1% and showing acquisitions are diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 18%, reversing most of the expansion to 21.7%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM FCF margin falls below 22%, under the FY2023 level of 22.2%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 22}},
    {"text": "TTM gross margin falls below 66%, under the FY2022 low of 66.5%, signalling pricing pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 66}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 242.93, "basis": "Raised FY27 outlook holds and the multiple moves toward its 5y median P/E of 44.1x [RA], matching the mechanical bull fair value 242.93 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 180, "basis": "Growth near the 10.7% reported in Q1 FY27 [OV news] keeps the multiple near today's 34.7x P/E [RA]; above the base fair value 161.22 because the DCF ignores the rising margins and buybacks."},
    "bear": {"probability": 0.25, "target_price_12m": 106, "basis": "Growth falls short of the 16.2% the reverse DCF implies [IS,BS,CF,RA,ST,HI] and P/FCF de-rates toward its 5y low of 11.3x [RA]; above the unreliable DCF-led bear 53.67."}
  },
  "entry_price": 128.98,
  "entry_basis": "valuation file: base 161.22 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
