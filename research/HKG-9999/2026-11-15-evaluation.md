# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-15
## Bear case
The price has done nothing for a year: the 12-month change is -14.1%, about 24.5pp behind SPY, and the stock sits at its 50- and 200-day averages, so there is no trend support [Certain]. Earnings are on Nov 19, 2026, and a games business depends on new-title success; a weak pipeline update or a miss on the January global launch would hit sentiment [Likely]. China game-licensing rules and US-China listing risk are unverified this run and could reprice the stock regardless of margins [Guessing]. Insiders own 45.32%, so minority holders have little say over capital allocation [Certain]. The mechanical bear value of 144.01 HKD, with the owner-set 3.5% China premium, shows the downside if multiples stay compressed [Certain]. Peer P/E comparison rests on n=1, so "cheap vs peers" is weak evidence [Certain].
## Bull case
Every quality metric is rising on both the 5-year and rolling view: operating margin 35.2% TTM (+3.8pp in a year), gross margin 67.2%, FCF margin 43.5%, ROCE 23.3%; no Direction change fired [Certain]. FCF conversion is 156.0% and the balance sheet is large net cash (net debt/EBITDA -3.76x) [Certain]. EV/EBITDA 8.5x and P/FCF 10.4x sit below their own 5-year minimums, with a 9.61% FCF yield, and the reverse DCF implies -3.1% year-1 revenue growth, which improving fundamentals do not show [Certain]. Base fair value 217.18 HKD sits above the 190.40 close [Certain]. A diversified franchise portfolio, not a single hit, makes returns durable [Likely]. Nothing in the thesis has changed since the 2026-11-08 HOLD [Certain].
## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python flags nothing falling: operating margin +3.8pp, FCF margin +2.3pp and ROCE +1.5pp over the last year [IS-T, CF-T, RA-T]; no Direction change line.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "PRC game-licensing or VIE/listing regulation restricting monetization, plus new-title execution around the Nov 19 results and January global launch; unverified this run, covered only by the 3.5% China premium.",
    "veto": null
  },
  "thesis": "A net-cash games franchise with operating margin rising to 35.2% and a 43.5% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline its improving fundamentals do not show.",
  "rationale": "Fundamentals keep improving and the stock still trades below its own 5-year minimum cash multiples with modest upside to base fair value; no new evidence since the 2026-11-08 HOLD. Not an ADD: discount is moderate, there is no trend strength, and the position is at its conviction size.",
  "price_at_decision": 190.40,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-9999/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in a company filing or release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 244.11, "basis": "Margin expansion continues and the DCF/EV-Revenue bull blend of 244.11 HKD is reached as cash multiples recover from below their 5y minimums [RA, fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 217.18, "basis": "Fundamentals hold at 35.2% operating and 43.5% FCF margin and the price moves to the mechanical base fair value of 217.18 HKD, against a price implying -3.1% growth [IS, CF, fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 144.01, "basis": "A regulatory or new-title setback keeps multiples at the bottom of range, matching the mechanical bear of 144.01 HKD with the 3.5% China premium [fact sheet Fair value; macro overlay country_risk, context weight]."}
  },
  "entry_price": 173.74,
  "entry_basis": "valuation file: base 217.18 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
