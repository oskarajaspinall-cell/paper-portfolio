# Evaluation: Greatland Resources Limited (ASX:GGP) — 2026-11-15
## Bear case
GGP is a price-taker whose 85.8% ROIC rests on two good years after losses (FY2024 ROIC -19.1%) [Certain]; the 5y multiple history covers a loss-to-profit transition, so "below its 5y minimum" overstates cheapness [Likely]. Management calls FY2027 a transition year of lower production and higher investment [Likely], and FCF margin already fell from 44.3% to 34.7%, 11.1pp below its 2-year high [Certain]. Shares rose 28.51% YoY, with the use of that dilution not established [Certain]. The macro overlay tilts small toward bear: the 10y real yield is up 0.47pp and the dollar firmer over three months, a gold headwind [Likely]. The price is 13.6% below its 200-day average with 6-month momentum of -30.4%, so the market is not confirming [Certain]. No primary-source production, reserve or hedging data was read, and the Mine NAV method lacks data [Certain]. Havieron execution risk sits on top [Likely].

## Bull case
At 8.2x P/E, 4.3x EV/EBITDA and an 11.25% FCF yield, GGP trades at roughly half the peer medians (21.8x, 8.6x) despite a 52.2% operating margin [Certain]. The balance sheet is net cash (net debt/EBITDA -0.97x), Altman Z 7.08 and Piotroski F 7 [Certain], so Havieron can be funded from cash flow [Likely]. The FCF dip is explained by guided investment, not lost share or a broken model: the Q1 2027 quarter beat plan on gold and copper, AISC hit the low end of guidance and cash rose despite elevated tax payments, with guidance unchanged [Likely]. The mechanical base fair value is 16.51 AUD vs a 10.36 close [Certain]. Once Havieron ramps, output and FCF recover and the multiple can rebuild toward its 5y median of 7.7x [Guessing].

## Decision
```json
{
  "ticker": "ASX:GGP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 44.3% -> 34.7% [CF-T,IS-T] as management guided FY2027 as a transition year of lower production and higher Havieron investment (https://stockanalysis.com/quote/asx/GGP/transcripts/710196-q4-2026/); Q1 2027 beat plan with guidance unchanged and net cash intact (https://stockanalysis.com/quote/asx/GGP/transcripts/774787-q1-2027/).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "A gold/copper price fall (real yields and dollar rising per the macro overlay) on a transition-year output dip, with Havieron execution and unexplained dilution, compresses margins from a short, possibly peak-earnings history.",
    "veto": null
  },
  "thesis": "A net-cash, low-cost gold-copper producer at trough multiples whose FCF dip is a guided Havieron investment phase rather than a broken model.",
  "rationale": "Cheap on every multiple with net cash and an explained FCF dip, but a price-taker with no moat, a two-year profit history, unexplained dilution, a gold-headwind macro tilt and no primary-source reserve data. The scorecard does not reach the buy bar; cash is acceptable.",
  "price_at_decision": 10.36,
  "price_date": "2026-11-13",
  "research_note": "research/ASX-GGP/2026-11-15.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 30%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Operating margin (TTM) falls below 40%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "FCF margin (TTM) falls below 20%: the transition year erodes cash rather than dips it", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt / EBITDA turns positive above 0.5x: Havieron spending consumes the net cash"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 16.51, "basis": "Havieron progresses and gold holds; EV/EBITDA rebuilds toward its 5y median 7.7x [RA], matching the mechanical base fair value 16.51 [valuation]."},
    "base": {"probability": 0.45, "target_price_12m": 11.71, "basis": "Transition-year output caps EBITDA, so EV/EBITDA recovers only toward its 5y minimum 5.2x [RA] (mechanical bear 11.71), below the mechanical base because FY2027 earnings are guided lower [note s.2]."},
    "bear": {"probability": 0.30, "target_price_12m": 8.64, "basis": "Real yields and the dollar keep rising (macro overlay, tilt small toward bear, raising this probability), gold falls and the price retests its 6-month low 8.64 [HI]."}
  },
  "entry_price": 8.64,
  "entry_basis": "Below the mechanical bear fair value; the 6-month low 8.64 [HI] would price the bear scenario, giving a margin of safety on even the trough EV/EBITDA (the default base 16.51 x 0.8 sits above the current price, so cannot be used).",
  "replaces": null,
  "replacement_reason": null
}
```
