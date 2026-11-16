# Evaluation: UniCredit S.p.A. (BIT:UCG) — 2026-11-16
## Bear case
The re-rating is done: P/B of 1.7x sits above its 5y maximum of 1.6x and 18% above peers, and P/E of 11.2x is far above its 5y median of 6.3x [Certain]. An extended price risks a de-rating if growth slows: ROE near 16% is partly a rate peak [Guessing], and the macro overlay flags that a faster-than-priced ECB easing or a credit-spread widening would hit ROE and the multiple together [Likely]. The Commerzbank control bid adds German political and integration risk, and competes with the guided cash distributions for capital [Likely]. Piotroski F of 4 is weak [Certain]. The mechanical fair value is flagged unreliable (methods disagree 3.0x) and its base is only +4.0% above the close, while the reverse DCF already prices about zero growth [Certain]. Bank FCF is erratic (FY2023 margin -181.7%), so the 13.60% FCF yield says little [Certain].

## Bull case
Returns have structurally improved: ROE rose from 3.5% (FY2021) to 16.8% (FY2025), 16.1% TTM, and net margin to 45.1% TTM [Certain]. Q3 2026 was a record quarter and 2026 profit guidance was raised, with a CET1 ratio reported at 15% [Likely]. Buybacks shrink the share count 1.54% YoY [Certain]. The stock is a business that is working: 10.7% above its 200-day average, not overextended, +22.9% over 12 months and beating SPY [Certain]. On P/E it trades in line with peers at 11.0x, so the premium is on book, which its higher ROE justifies [Likely]. Unconditional EU clearance of Commerzbank control would add scale and cost synergies in Germany [Guessing].

## Decision
```json
{
 "ticker": "BIT:UCG",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {"decline_cause": "none", "decline_evidence": "ROE rose to 16.8% (FY2025) and 16.1% TTM; FCF margin TTM 68.6% is at its 2-year high [RA, CF-T].", "moat": "narrow", "key_risk": "high", "key_risk_text": "A de-rating from a P/B above its 5y maximum if a faster ECB easing or credit widening pulls ROE back toward 12% (macro overlay), compounded by Commerzbank integration and political risk.", "veto": null},
 "thesis": "A re-rated, mid-teens-ROE European bank in a healthy uptrend whose price already sits above its own book-multiple history, leaving a rate-sensitive, de-rating-prone skew.",
 "rationale": "Quality and trend are real, but P/B is above its 5y maximum, the fair value is unreliable with little base upside, and the macro overlay tilts the skew to the downside. Good but not compelling: AVOID; no position.",
 "price_at_decision": 83.68,
 "price_date": "2026-11-13",
 "research_note": "research/BIT-UCG/2026-11-16.md",
 "triggers": [
  {"text": "TTM ROE falls below 12%, giving up most of the rise to 16.1% and showing the returns step-up was a rate peak.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
  {"text": "TTM net margin falls below 35%, reversing the rise to 45.1%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}},
  {"text": "Shares change YoY rises above +3%, i.e. dilution to fund the Commerzbank deal.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
 ],
 "scenarios": {
  "bull": {"probability": 0.2, "target_price_12m": 101.19, "basis": "ROE holds in the mid-teens and the multiple holds, reaching the mechanical bull fair value [IS,BS,CF,RA]; probability trimmed for the macro overlay's small tilt toward bear (research/BIT-UCG/2026-11-16-macro.md)."},
  "base": {"probability": 0.5, "target_price_12m": 87.06, "basis": "Raised 2026 guidance and buybacks sustain ROE near 16.1% [RA], in line with the blended base fair value [IS,BS,CF,RA]."},
  "bear": {"probability": 0.3, "target_price_12m": 73.17, "basis": "A faster ECB easing or credit widening pulls the P/B back from above its 5y maximum toward the P/B+ROE base value [RA]; probability raised for the macro overlay's tilt toward bear (research/BIT-UCG/2026-11-16-macro.md); the 14.46 mechanical bear is ignored as the fair value is flagged unreliable."}
 },
 "entry_price": 69.65,
 "entry_basis": "valuation file: base 87.06 x 0.8",
 "replaces": null,
 "replacement_reason": null
}
```
