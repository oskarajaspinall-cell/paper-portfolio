# Evaluation: MMG Limited (HKG:1208) — 2026-11-16
## Bear case
This is a price-taking copper/zinc miner with no evident moat at what looks like peak-cycle profitability: TTM operating margin of 42.6% against 11.8% in FY2023, when net margin was 0.2% [Certain]. The 5-year FY trend in operating and FCF margin is falling, and the rolling-12-month rise (33.4% to 42.6%; 25.5% to 31.9%) is driven by metal prices, not a structural improvement [Likely]. The shares are down 28.9% over six months with no identified stock-specific cause [Certain]; the low EV/EBITDA of 3.2x may simply be the market capitalising peak EBITDA, as is normal for miners [Likely]. Real yields and the dollar rose over three months, a headwind for metals (macro overlay, tilt toward bear, small) [Likely]. Peru (Las Bambas) disruption risk is unverified [Guessing]. Shares rose 3.43% YoY [Certain]. Results are due Nov 18, 2026, two sessions away [Certain].
## Bull case
Even on mid-cycle earnings the stock looks cheap: P/E 9.3x at 2% of its 5y range, EV/EBITDA 3.2x below its 5y minimum of 4.1x, P/FCF 4.0x and a 24.70% FCF yield, at large discounts to FCX, SCCO and HKG:1378 [Certain]. The balance sheet has been repaired: net debt/EBITDA fell from 3.44x (FY2022) to 0.16x, Piotroski F is 7 [Certain]. ROIC TTM of 20.3% doubled from 10.2% a year earlier, with lower cost guidance at Las Bambas, Khoemacau and Rosebery and growth at Kinsevere and Khoemacau (source: https://stockanalysis.com/quote/hkg/1208/transcripts/714438-q2-2026/) [Likely]. The base fair value is 8.13 HKD and RSI 28.6 is oversold [Certain]. If the fall is copper sentiment rather than an asset problem, the multiple can re-rate toward its 4-6x history (macro overlay) [Guessing].
## Decision
```json
{
  "ticker": "HKG:1208",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over the last year: ROIC 10.2% to 20.3%, operating margin 33.4% to 42.6%, FCF margin 25.5% to 31.9% [RA-T, IS-T, CF-T]; the FY-endpoint declines reflect the FY2021 cyclical peak, not a broken model.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Margins are at a cyclical high for a price-taking miner while the shares fell 28.9% in six months for an unidentified reason; a copper downturn or a Peru/Las Bambas disruption would return margins toward FY2023 levels (11.8% operating margin) [IS].",
    "veto": null
  },
  "thesis": "A deleveraged copper miner at very low cash multiples, but on peak-cycle margins with no moat and an unexplained six-month fall ahead of results.",
  "rationale": "Cheap on every multiple with a repaired balance sheet, but the earnings base is cyclical, the cause of the fall is unknown and the macro tilt is toward bear. Good but not compelling; conviction 3 is an AVOID. A lower price would not fix this; the Nov 18 results and the cause of the fall would.",
  "price_at_decision": 6.57,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-1208/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (20.3% now), showing the profit upswing has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 30% (42.6% now), a move back toward mid-cycle.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 15% (31.9% now).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA on the ratios page rises above 2.0x (0.16x now), or the company discloses a production stoppage at Las Bambas."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.96, "basis": "Copper steadies and EV/EBITDA re-rates toward its 4.1x-6.9x 5y range [RA], back to the 52-week high [HI]; below the mechanical bull of 17.86 because that capitalises peak TTM EBITDA at a full-history multiple."},
    "base": {"probability": 0.45, "target_price_12m": 8.13, "basis": "Mechanical base fair value on EV/EBITDA [fact sheet Fair value], with margins holding near the TTM 42.6% [IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 5.18, "basis": "Mechanical bear fair value as margins fall toward mid-cycle; bear probability raised for the macro overlay's small tilt toward bear (higher real yields and dollar, research/HKG-1208/2026-11-16-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the default anchor (base 8.13 x 0.85). The obstacles are cyclical peak margins, no moat and an unexplained six-month fall; a lower price would not change the decision. Re-check on the Nov 18, 2026 results.",
  "replaces": null,
  "replacement_reason": null
}
```
