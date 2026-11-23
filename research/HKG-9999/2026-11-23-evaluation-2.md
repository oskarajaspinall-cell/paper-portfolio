# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-23
## Bear case
Q3 revenue fell year on year as some self-developed games weakened and missed consensus (https://www.marketbeat.com/instant-alerts/transcript-what-netease-ntes-said-on-its-q3-earnings-call-2026-11-19/) [Likely]; the stock fell to 154.00, near its 52-week low of 150.30 [Certain]. Games are hit-driven: a thin release slate can shrink revenue for several quarters, and the reverse DCF's -11.7% year-1 growth could prove right [Guessing]. The gross-margin gain came from lower revenue-sharing costs, which may not repeat [Likely]. Rolling FCF margin is 3.3pp below its 2-year high of 45.0%, and ROIC dropped from 144.6% to 33.7%; the ROIC swing is a small-capital-base artefact, not a profit collapse, since operating margin rose 5.0pp [Likely]. There is no trend support: 18.5% below the 200-day average, -28.6% over 12 months [Certain], so this can stay a value trap. China game-approval and minors rules, and plaintiff-firm solicitations, add event risk [Likely].
## Bull case
The business is still improving where it counts: TTM operating margin is 36.6%, its 2-year high, up 5.0pp in a year; ROCE is 23.2% and rising; games gross margin expanded to 74.3% from 69.3% (https://www.fool.com/earnings/takeaways/2026/11/19/netease-3-key-takeaways-for-long-term-investors/) [Likely]. Cash generation is exceptional: FCF margin 41.7%, FCF conversion 149.9%, net cash at -3.84x EBITDA [Certain]. The price sits below its own 5-year minimum on every multiple: P/FCF 8.7x versus a 10.7x low, EV/EBITDA 5.7x versus 9.3x, an 11.49% FCF yield [Certain]. The reverse DCF prices a revenue contraction far deeper than a one-quarter dip with rising margins shows [Likely]. Mechanical base fair value is 218.17 HKD [Certain]. A dividend and ongoing buybacks continue (https://stockanalysis.com/quote/hkg/9999/transcripts/736905-q3-2026/) and insiders own 45.32% [Likely].
## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Python flags ROIC falling (144.6% to 33.7% TTM): a tiny invested-capital base on a net-cash balance sheet, not profit erosion, since operating margin rose 5.0pp to its 2-year high of 36.6% and ROCE rose to 23.2% [RA-T, IS-T]; FCF margin is flat over the year (-0.9pp) [CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A thin game pipeline turns the Q3 revenue dip into a multi-quarter decline that ends the margin expansion (marketbeat Q3 call summary).",
    "veto": null
  },
  "thesis": "A net-cash games franchise with operating margin at its 2-year high of 36.6% and a 41.7% FCF margin trades below its own 5-year minimum multiples, where the price implies a revenue decline far deeper than one weak quarter shows.",
  "rationale": "Margins, cash and net cash are intact after the Q3 miss; the fall is a reaction to one quarter, not a broken thesis. The scorecard sets the conviction. No ADD: buying more needs a replacement as cash sits at the floor and China/HK exposure is near its cap, so the position keeps its size.",
  "price_at_decision": 154.00,
  "price_date": "2026-11-20",
  "research_note": "research/HKG-9999/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related action forces deconsolidation, as disclosed in a company filing or release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 244.87, "basis": "New titles restore revenue growth and the market re-rates toward the mechanical bull fair value of 244.87 [IS,BS,CF,RA,ST,HI] as margins hold at 36.6% [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 187.23, "basis": "Revenue stabilises and the multiple recovers only partly, to the EV/Revenue base of 187.23 [RA,ST], below the DCF base because the Q3 revenue dip argues against a full re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 138.40, "basis": "The Q3 revenue decline persists for several quarters (marketbeat Q3 call summary) and the price settles at the DCF bear value of 138.40 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 140.00,
  "entry_basis": "Valuation file: base 218.17 x 0.85 is above the price, so not usable; anchored instead below the 52-week low of 150.30 [HI] near the DCF bear value of 138.40, where the ADD case would no longer depend on any re-rating.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```
