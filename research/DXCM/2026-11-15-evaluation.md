# Evaluation: DexCom, Inc. (DXCM) — 2026-11-15
## Bear case
The price already asks a lot: the reverse DCF implies 32.1% year-1 revenue growth, far above the guided pace, and the DCF base is 36.89 against a close of 83.33 [Certain]. Multiples are low only versus DexCom's own inflated history; versus peers P/E is +29% and EV/Sales +64% [Certain]. The stock sits 11.0% above its 200-day average after a 39.8% year; if US growth slows or Abbott presses on price, an extended name de-rates fast, and beta is 1.44 [Likely]. FCF margin has faded from 29.7% to 21.5% over the last year (the **Direction change**), while gross margin is still below FY2021's 68.6% [Certain]. Securities, derivative and G6/G7 product class actions are open, and closure of the FDA warning letter is unconfirmed [Guessing]. 3-month relative strength is -5.9pp: momentum is stalling [Certain].

## Bull case
Returns and margins are at five-year highs and still climbing: TTM ROIC 45.9%, operating margin 24.0% versus 17.2% a year earlier, ROCE 30.7% [Certain]. Q3 beat, FY26 revenue guidance was narrowed upward, and management guides an operating margin of approximately 24% (headline: https://www.tipranks.com/news/the-fly/dexcom-narrows-fy26-revenue-view-to-5-20b-5-25b-consensus-5-23b-thefly-news) [Likely]. The FCF fade looks temporary: operating margin rose over the same year and FCF still converts at 110.8% of net income, so it reflects cash timing and investment rather than a broken model [Likely]. Net cash, a $1bn buyback and shares down 3.92% YoY add capital returns [Certain]. A recurring sensor base with reimbursement access is a durable, if contested, moat [Likely]. P/E 32.7x and EV/EBITDA 20.5x sit at the bottom of their 5y ranges while the trend is healthy (above the 200-day, FCF yield 3.53%) [Certain].

## Decision
```json
{
  "ticker": "DXCM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling (23.5% to 21.5% TTM, below the 29.7% 2-year high) while operating margin rose from 17.2% to 24.0% and FCF/NI is 110.8% [CF-T, IS-T, CF]; the fade is cash timing/investment, not lost share or a price cap.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Abbott CGM price/share competition slowing US growth, which would de-rate a stock priced for growth well above guidance (reverse DCF 32.1%) and trading above its 200-day average.",
    "veto": null
  },
  "thesis": "A high-return, net-cash CGM franchise whose margins are expanding, priced at the low end of its own history but still above peers and above what the DCF supports.",
  "rationale": "Quality and direction are strong, but the price implies growth far above guidance, peers are cheaper and the fair value disagrees 3.0x; the scorecard gives conviction 3, below the buy bar, so AVOID and no position.",
  "price_at_decision": 83.33,
  "price_date": "2026-11-13",
  "research_note": "research/DXCM/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin TTM falls below 20%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "FCF margin TTM falls below 15%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "ROIC TTM falls below 30%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Gross margin TTM falls below 58%, or an FDA enforcement action interrupts G7 production or supply", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 109.3, "basis": "Margin gains continue and the market pays the P/E method's base value of 109.30 [IS,RA], below the mechanical bull 142.62 because peers trade at a 25.3x P/E median [P:PODD,P:ABT,P:MDT,P:TNDM]."},
    "base": {"probability": 0.5, "target_price_12m": 85, "basis": "Earnings grow on the guided ~24% operating margin while P/E holds near today's 32.7x at the bottom of its 5y range [RA]; above the blend base 61.03, which the fact sheet flags unreliable (methods disagree 3.0x)."},
    "bear": {"probability": 0.25, "target_price_12m": 61.03, "basis": "US growth slows under Abbott competition and the stock de-rates toward the blend base fair value 61.03 [IS,BS,CF,RA,ST,HI], not the DCF bear, given net cash and 110.8% FCF conversion [CF,IS]."}
  },
  "entry_price": 48.82,
  "entry_basis": "valuation file: base 61.03 x 0.8 [IS,BS,CF,RA,ST,HI] (default margin of safety); the base is flagged unreliable, so a hit means a full re-research, not a buy.",
  "replaces": null,
  "replacement_reason": null
}
```
