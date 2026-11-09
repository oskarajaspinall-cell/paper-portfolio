# Evaluation: China Resources Beer (HKG:0291) — 2026-11-09
## Bear case
Earnings below the operating line are eroding: net margin fell from 13.7% (FY2021) to 7.2% TTM and ROE from 20.1% to 6.3% while operating margin rose, and the fact sheet does not explain why [Certain]; an impairment or a lower-return non-beer asset is plausible [Guessing]. ROIC peaked at 16.0% in FY2022 and is 11.9% TTM, below its FY2021 level, so the margin gains have not turned into higher returns on capital [Certain]. The 52-week fall of 21.5% and a reverse DCF implying -6.9% year-1 revenue growth say the market expects China beer demand or pricing to weaken [Likely]. Results are due Nov 13, 2026, days after a decision [Certain]. A CNY reporter carries the owner-set 3.5% country premium, and the cheap own-history EV/EBITDA is only near the peer median of 6.5x, so a re-rating to history is not assured [Likely].
## Bull case
The operating business is improving: gross margin rose from 39.2% to 42.3% and operating margin from 9.0% to 14.9% TTM, at the 2-year high on a rolling basis, consistent with premium mix in a scale oligopoly [Likely]. The rolling ROIC dip is flat (-0.5pp) and TTM ROIC has recovered from 10.4% in FY2025 [Certain]. Cash is strong and rising: FCF margin 15.3% TTM versus 12.9% a year earlier, FCF conversion 213.2%, net cash at -1.55x EBITDA [Certain]. The stock trades below its own 5-year minimum EV/EBITDA, EV/Sales, P/FCF and P/B, at a 9.96% FCF yield, while the price implies shrinkage the margins and cash flow do not show [Certain]. Mechanical base fair value is 34.56 HKD, with the DCF alone at 28.65, both well above the 20.92 close [Certain]. Low beta of 0.38 suits a staples position [Certain].
## Decision
```json
{
  "ticker": "HKG:0291",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: rolling ROIC is flat (-0.5pp), operating margin (14.9% TTM) is flat near its 2-year high and FCF margin is rising (15.3% TTM vs 12.9%) [RA-T, IS-T, CF-T]. The 5-year ROIC fall from the FY2022 peak is not a current decline.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "China beer demand or pricing weakens (the price implies -6.9% year-1 revenue growth), and the unexplained fall in net margin to 7.2% and ROE to 6.3% signals below-the-line charges that the Nov 13, 2026 results could extend.",
    "veto": null
  },
  "thesis": "A net-cash China brewer with rising operating and FCF margins trades below its own 5-year minimum cash multiples at a 9.96% FCF yield, pricing a revenue decline its operations do not show.",
  "rationale": "Scorecard conviction 4: improving operating and cash margins, net cash, and cash multiples below their own 5-year minimums with a price implying shrinkage. Unexplained below-the-line erosion and China demand keep it at 4, not 5. Python sizes it; China/HK exposure would breach its 25% cap, so it replaces a China holding.",
  "price_at_decision": 20.92,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-0291/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12.0% (14.9% now), reversing the premiumisation margin gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 10.0% (15.3% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 9% (11.9% now), under the FY2025 low of 10.4%, showing returns on capital are eroding structurally.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA on the ratios page rises above 0.0x (net cash lost), e.g. through debt-funded M&A."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.56, "basis": "Price reaches the blended base fair value of 34.56 HKD [fact sheet Fair value] as operating margin holds at 14.9% [IS] and cash multiples move off their below-5y-minimum levels [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 28.65, "basis": "The DCF base of 28.65 HKD [fact sheet Fair value] on a 15.3% FCF margin [CF-T], below the blended base because the EV/EBITDA method assumes a return to a 5y range whose minimum of 9.1x sits above the 6.5x peer median [RA, peers]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.82, "basis": "The mechanical bear fair value of 16.82 HKD [fact sheet Fair value] if China demand shrinks as the reverse DCF's -6.9% implies and below-the-line charges keep net margin falling from 7.2% [IS]."}
  },
  "replaces": "HKG:2076",
  "replacement_reason": "Adding a full position would take China/HK exposure (three holdings) above its 25% cap. Of the three, HKG:2076 has risen furthest above its entry price, so less of its re-rating is left, while 0291 adds a low-beta staple trading below every own-history cash multiple; this is my judgement, and the portfolio rules re-check the swap."
}
```
