# Evaluation: Rollins, Inc. (ROL) — 2026-10-09
## Bear case
The 45.2% 52-week fall is a de-rating that has closed the valuation gap, not a gift: at 32.26 the stock sits just 1.6% below base fair value of 32.78, with no margin of safety [Certain]. The DCF alone gives 18.20–29.41; only the EV/EBITDA leg props the blend up [Certain]. The reverse DCF implies 16.2% year-1 revenue growth against a reaffirmed ~6% FY26 guide [Likely]. AI-search changes have pushed residential digital leads into double-digit declines since May 2026, a structural hit to Orkin's funnel that management cannot yet size [Likely]. EV/EBITDA (19.0x) is still 18% above the peer median and P/B 125% above [Certain]. Short interest rose 37.8% in a month, Piotroski F is 4, net debt/EBITDA has crept from 0.41x to 1.16x, and Q3 results land on Oct 21 with the trend unresolved [Certain].
## Bull case
This is a 25% ROIC, 52% gross-margin, 116%-FCF-conversion compounder with 99 consecutive quarters of revenue growth [Certain]. The lead problem is channel-specific: door-to-door and builder brands (Fox, HomeTeam) still grow double-digit, and recurring and commercial revenue stayed strong in Q2 [Likely]. P/E of 29.3x is in line with peers and far below ROL's own 5y minimum of 47.2x; P/FCF of 25.0x is below the peer median [Certain]. Leverage is low at 1.16x, leaving room for bolt-on M&A in a fragmented industry [Likely]. If marketing adapts and leads stabilise, a return toward the bull fair value of 37.97 is plausible [Guessing].
## Decision
```json
{
  "ticker": "ROL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A top-quality, high-return pest-control compounder has de-rated to roughly its base fair value, but an unresolved AI-search-driven decline in residential digital leads leaves no margin of safety ahead of Q3 results.",
  "rationale": "Quality is excellent, but price only matches base fair value (32.78), the DCF leg sits below price, and the reverse DCF needs 16.2% growth against a ~6% guide. The lead-decline problem is unresolved, and Q3 lands on Oct 21. That is good but not compelling, so we hold cash and wait for a lower entry price.",
  "price_at_decision": 32.26,
  "price_date": "2026-10-08",
  "research_note": "research/ROL/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 51% (52.4% TTM), signalling people/fuel cost pressure or lost pricing power is structural.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 51}},
    {"text": "TTM operating margin falls below 18% (18.7% TTM, 18.3% FY2022 five-year low), showing lead-acquisition costs are eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM ROIC falls below 22% (23.5% TTM vs 24.8-25.9% FY2021-25), indicating moat economics are weakening.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "Management reports organic revenue growth below the 'at least 6%' FY26 guide, or residential digital-lead declines that fail to stabilise for two more consecutive quarters (earnings releases/transcripts)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 37.97, "basis": "Lead declines stabilise as marketing adapts while Fox/HomeTeam and commercial keep growing (Q2 2026 transcript), so the price reaches the fact sheet's bull fair value of 37.97 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 32.78, "basis": "Growth stays near the reaffirmed ~6% guide (All Stars transcript), so the price converges on the base fair value of 32.78 [IS,BS,CF,RA,ST,HI]; the DCF leg (21.69) caps upside while the 29.3x P/E, in line with peers [RA], limits downside."},
    "bear": {"probability": 0.30, "target_price_12m": 29.42, "basis": "The double-digit digital-lead decline (All Stars transcript) spreads and Q3 misses the 6% guide, so the price falls to the bear fair value of 29.42 [IS,BS,CF,RA,ST,HI], near the 52-week low of 29.29 [HI]."}
  },
  "entry_price": 26.22,
  "entry_basis": "valuation file: base 32.78 x 0.8 = 26.22, a 20% margin of safety against the unresolved lead-generation risk.",
  "replaces": null,
  "replacement_reason": null
}
```
