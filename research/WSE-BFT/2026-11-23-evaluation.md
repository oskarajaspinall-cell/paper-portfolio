# Evaluation: Benefit Systems S.A. (WSE:BFT) — 2026-11-23
## Bear case
The price already discounts the recovery. P/E 23.9x, P/FCF 20.4x and P/B 7.6x all sit above their own 5-year maxima [RA], and the reverse DCF needs 12.6% year-1 revenue growth [Certain]. After a +100.6% year and a close +30.8% above the 200-day average [ST], any slowdown risks a de-rating back towards the 5y median P/E of 17.4x [Likely]. Returns are fading: ROIC fell from 17.3% to 15.2% over the last year and sits 12.5pp below its 2-year high of 27.7% [RA-T], while leverage rose from 1.08x to 2.22x net debt/EBITDA and shares grew 6.20% YoY [ST] — growth partly bought with debt and dilution [Likely]. The Q3 2026 reaction (+5.8% on 3.1x volume) is unread, so the cause is unverified [Certain]. Foreign exposure (Turkey and others) is unconfirmed, a country risk the overlay could not check [Guessing]. The mechanical fair value is flagged unreliable (methods disagree 7.5x) [Certain].
## Bull case
A good business that is working. Operating margin 17.9% TTM is flat on a year ago, FCF margin recovered from 13.3% to 18.5% and ROCE rose 2.8pp [IS-T, CF-T, RA-T], so the ROIC decline reads as normalisation after a post-pandemic peak and debt-funded club expansion, not lost share [Likely]. ROE 35.5% and FCF/NI 116.7% show real cash earnings [Certain]. The MultiSport card has network effects: employers want venue breadth, clubs want card volume, and BFT has scale in Poland [Likely]. P/E is 28% below the peer median of 33.4x [RA], FCF yield is 4.89% [ST], and relative strength vs SPY is +96.5pp over 12 months with a held post-results jump [HI] [Certain]. Beta 0.50 and Altman Z 3.02 limit balance-sheet risk [ST] [Certain].
## Decision
```json
{
  "ticker": "WSE:BFT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC fell 17.3% -> 15.2% (RA-T) while operating margin stayed flat at 17.9% (IS-T), FCF margin rose 13.3% -> 18.5% (CF-T) and ROCE rose 2.8pp (RA-T): normalisation from the 27.7% post-pandemic peak plus debt-funded expansion (net debt/EBITDA 1.08x -> 2.22x, BS), not lost share or a price cap.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "De-rating: P/E, P/FCF and P/B sit above their 5-year maxima after a +100.6% year, so any growth slowdown against the 12.6% growth the price implies would compress the multiple.", "veto": null},
  "thesis": "A high-return Polish workplace-fitness network in a strong uptrend, but priced above its own history with fading ROIC and rising leverage and dilution.",
  "rationale": "Quality and trend are real, but the price is above its own 5-year multiple range (so no trend-strength or discount points), ROIC is fading, leverage and share count have risen and the Q3 results driving the jump are unread. The scorecard gives conviction 2; cash is acceptable.",
  "price_at_decision": 6250.00,
  "price_date": "2026-11-20",
  "research_note": "research/WSE-BFT/2026-11-23.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 14%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "ROIC (TTM) falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 3.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 8657.75, "basis": "Growth and margins hold, and the price reaches the DCF base of 8,657.75 PLN (fact sheet fair value), supported by the P/E discount to the peer median of 33.4x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 6156.37, "basis": "Growth roughly meets the 12.6% the reverse DCF implies and the price tracks the blended base fair value of 6,156.37 PLN (fact sheet, flagged unreliable)."},
    "bear": {"probability": 0.25, "target_price_12m": 4283.58, "basis": "Growth slows and P/E de-rates towards its 5y median of 17.4x [RA], in line with the DCF bear of 4,283.58 PLN (fact sheet fair value)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
