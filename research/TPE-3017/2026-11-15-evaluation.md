# Evaluation: Asia Vital Components Co., Ltd. (TPE:3017) — 2026-11-15
## Bear case
The price already capitalises peak AI-server economics. P/E 33.9x, EV/EBITDA 20.5x and P/B 17.7x all sit above their 5y maxima and above peers [RA] [Certain]; the reverse DCF needs 23.4% year-1 revenue growth [Certain]. Margins have roughly doubled since FY2021 on one demand wave; if hyperscaler capex slows or customers qualify rival cooling suppliers, both earnings and the multiple fall together [Likely]. The extended price is the main exposure: +20.4% over the 200-day and +102.0% in 12 months, so a growth slowdown means a de-rating with no cushion [Likely]. Direction change: ROIC is 102.1pp below its 2-year high and FCF margin 5.1pp below its high; that looks like capacity-expansion capex and a swelling capital base rather than lost share, but it shows the peak may be behind [Guessing]. Q3 detail is unread, rising real yields offer no multiple support (macro overlay), and Taiwan concentration risk is unpriced [Likely].
## Bull case
This is a business that is clearly working. Operating margin rose every year from 10.2% to 25.5% TTM and gross margin to 30.8%; on a rolling basis both are at their 2-year highs and well above a year ago [IS-T] [Certain]. Net cash (net debt/EBITDA -0.72x), Piotroski 7, Altman Z 5.33 and no dilution [ST] [Certain]. FCF margin of 19.3% self-funds the liquid-cooling capacity build [CF] [Certain], and the Q2 2026 call cites liquid-cooling adoption and automation supporting growth [Likely]. P/FCF 30.2x is only mid-range in its own history and below the one peer [RA] [Certain]. The trend is intact: above the 200-day average, not severely overextended, FCF yield 3.31% [Certain]. If AI thermal content per rack keeps rising, earnings can grow into the multiple, with the mechanical bull value of 3,448.92 [Guessing].
## Decision
```json
{
  "ticker": "TPE:3017",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years; ROIC and FCF margin are only below their 2026-06-30 2-year highs (102.1pp and 5.1pp) while well above a year ago (+86.6pp, +4.4pp) [RA-T, CF-T], consistent with capacity-expansion investment (https://stockanalysis.com/quote/tpe/3017/transcripts/596848-q1-2026/).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "AI-server capex slows or customers dual-source cooling, cutting peak margins while multiples above their 5y maxima de-rate; the extended price (+102.0% in 12 months) leaves no cushion.",
    "veto": null
  },
  "thesis": "A net-cash AI-server thermal supplier with sharply rising margins is working, but trades above its own 5-year multiple range on what may be peak-cycle earnings.",
  "rationale": "Quality, balance sheet and trend are excellent, but every earnings multiple sits above its 5y maximum, the price needs high growth, and the moat is unproven against a cyclical AI capex wave. The scorecard lands at conviction 3, below the buy bar; cash is acceptable.",
  "price_at_decision": 3040.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-3017/2026-11-15.md",
  "triggers": [
    {"text": "TTM gross margin falls below 25%, giving back the FY2025-to-TTM expansion and signalling pricing pressure in thermal parts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 25}},
    {"text": "TTM operating margin falls below 19%, back under the FY2025 level of 19.7%, showing the AI-cooling margin step-up was cyclical.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 10%, showing capacity capex is outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA turns positive (net cash lost).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3448.92, "basis": "AI thermal demand keeps margins rising and the multiple holds; matches the mechanical bull fair value of 3,448.92 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 3000, "basis": "Earnings keep growing but the P/E of 33.9x, above its 5y max of 30.6x [RA], drifts lower, roughly offsetting; above the mechanical base of 1,842.67 because that range is flagged unreliable (methods disagree 4.5x) and the DCF base alone is 2,489.24."},
    "bear": {"probability": 0.30, "target_price_12m": 2180, "basis": "Growth slows and P/E de-rates to its 5y median of 24.3x [RA] on TTM earnings; probability raised a small step for the macro overlay's small tilt toward bear on rising real yields (research/TPE-3017/2026-11-15-macro.md)."}
  },
  "entry_price": 1474.14,
  "entry_basis": "valuation file: base 1,842.67 x 0.8; at that level the same quality would come with a real discount instead of a price above every 5y multiple maximum.",
  "replaces": null,
  "replacement_reason": null
}
```
