# Evaluation: Insulet Corporation (PODD) — 2026-10-10

## Bear case
At 135.28 the stock still trades 16.1% above its base fair value of 113.48, and the reverse DCF implies 31.2% year-1 revenue growth just as management has cut guidance on type 2 attrition [Certain] (fact sheet; Wells Fargo transcript 2026-09-09). Two Omnipod device corrections and a securities class action over device safety and reliability are unresolved. A third correction or an FDA escalation would hit the moat itself, which rests on prescriber trust [Likely]. TTM FCF margin has slipped to 9.6% from 13.9% in FY2025, so P/FCF of 31.9x is 45% above the peer median [Certain] (CF, RA). Short interest of 7.36% rose 14.3% in a month, and the stock is 28.6% below its 200-day average, so sentiment has not washed out [Certain] (ST). The 10y real yield rose 0.56pp in 3 months, a further headwind for a long-duration DCF [Certain] (macro overlay, FRED DFII10).

## Bull case
This is a quality franchise at a historic discount. ROIC is 21.3% (11.6% in FY2021), gross margin 71.1% and operating margin 16.9%, all on five-year uptrends [Certain] (RA, IS). P/E of 25.5x and EV/EBITDA of 15.9x are below their 5-year minimums of 43.8x and 36.0x, and EV/EBITDA is 7% under peers [Certain] (RA). The balance sheet is clean: net debt/EBITDA is 0.67x, Piotroski F is 8 and the share count fell 1.19% [Certain] (RA, ST). Revenue is recurring pod consumables, and post-90-day retention is described as high, so attrition looks concentrated in early type 2 starts that four corrective actions target [Likely] (Bernstein transcript 2026-09-24). If the Q3 print on Nov 4 shows attrition stabilising, a re-rating toward the DCF bull of 167.69 is plausible [Guessing].

## Decision
```json
{
  "ticker": "PODD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, recurring-revenue insulin-pump franchise trades below its own 5-year multiple range, but the price still sits above base fair value while type 2 attrition, device corrections and litigation are unresolved.",
  "rationale": "Quality is real, but the price is 16.1% above base fair value 113.48 and implies 31.2% growth into a guidance cut. Device-correction and litigation risk are open, and the probability-weighted target sits below the last close. Good but not compelling: no position. Q3 results on Nov 4 are the next test.",
  "price_at_decision": 135.28,
  "price_date": "2026-10-09",
  "research_note": "research/PODD/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, reversing the five-year rise from 11.6% to 21.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 68%, the FY2021/FY2023 level, showing the corrective actions or device corrections are hurting unit economics.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "TTM FCF margin turns negative again, as in FY2021-FY2022.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "The Q3 2026 release or call (Nov 4, 2026) reports a further guidance cut on type 2 attrition or a third Omnipod medical device correction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 167.69, "basis": "Corrective actions stabilise early type 2 attrition (Bernstein transcript 2026-09-24) and the stock re-rates to the DCF bull fair value of 167.69 [IS,BS,CF,RA,ST], still far below the 5y minimum P/E of 43.8x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 135.28, "basis": "P/E holds at 25.5x [RA] as growth offsets attrition. This sits between DCF base 68.97 and P/E base 202.51, above blended base 113.48, because the DCF runs off a TTM FCF margin of 9.6% that is depressed against FY2025's 13.9% [CF,IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 109.56, "basis": "Attrition or device-correction and litigation news worsen and the price falls to the P/E bear fair value of 109.56 [IS,BS,CF,RA,ST]. Bear probability is raised 5pp for the macro overlay's small bear tilt: 10y real yield up 0.56pp in 3m (research/PODD/2026-10-10-macro.md)."}
  },
  "entry_price": 90.78,
  "entry_basis": "valuation file: base 113.48 x 0.8. At that level the same evidence (21.3% ROIC, 0.67x leverage) would justify conviction 4 despite the unresolved attrition and litigation risk.",
  "replaces": null,
  "replacement_reason": null
}
```
