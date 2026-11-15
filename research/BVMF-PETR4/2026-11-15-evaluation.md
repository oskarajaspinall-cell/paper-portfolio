# Evaluation: Petróleo Brasileiro S.A. - Petrobras (BVMF:PETR4) — 2026-11-15
## Bear case
The discount is to peers, not to Petrobras's own history: P/FCF of 5.6x and EV/Sales of 1.6x sit above their 5y maxima and EV/EBITDA is at 71% of its range [RA] [Certain]. The direction changes cut both ways: ROIC (13.9% to 18.8%) and operating margin (29.5% to 34.9%) rose over 12 months but remain below 2-year highs and fell over 3 years, a cyclical rebound rather than a reversed decline [Likely]; FCF margin is flat at 19.0%, 9.2pp below its 2-year high, as raised capex absorbs cash [CF-T] [Certain]. The state controls fuel pricing, dividends and investment, and the Venezuela interest and bolt-on deals hint at non-commercial capital use [Likely]. The real is about 10% weaker in a month, hurting a USD holder (macro overlay) [Certain]. The trend points come from a +40.2% 12-month move: if oil or guidance slips, the multiple de-rates [Likely].
## Bull case
A 17.73% FCF yield, 4.2x P/E and 3.2x EV/EBITDA against peer medians of 12.7x and 6.2x price in a lot of bad news [ST, RA] [Certain]; the reverse DCF implies revenue falling 22.1% in year 1 [Certain]. Q3 delivered record production and refinery output, raised 2026 production and cash-flow guidance, and net profit rose 21.5% (Reuters and transcript headlines in the fact sheet) [Likely]. Rolling returns are recovering: ROIC 18.8%, operating margin 34.9%, net debt/EBITDA down to 1.05x, Piotroski F 8, no dilution [RA-T, ST] [Certain]. The trend is intact: price above its 200-day average, 50-day 13.9% above the 200-day, RSI 34.4 after a pullback from the 59.79 high [HI, ST] [Certain]. Low-cost pre-salt reserves are a real scale advantage [Likely].
## Decision
```json
{
  "ticker": "BVMF:PETR4",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost pre-salt producer with recovering returns and a raised Q3 outlook trades at a deep peer discount, but that discount reflects state control over pricing, payouts and capex while FCF margin stays well below its recent high.",
  "rationale": "The scorecard gives conviction 3, the same verdict as 2026-11-08. Q3 was strong and the trend holds, but the peer discount reflects state control over pricing, payouts and capex, FCF margin is flat well below its recent high, and the stock is not cheap against its own P/FCF history. Good but not compelling: AVOID.",
  "price_at_decision": 45.36,
  "price_date": "2026-11-13",
  "research_note": "research/BVMF-PETR4/2026-11-15.md",
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The 3-year falls in ROIC, operating margin and FCF margin follow oil prices off the FY2022 peak plus heavier investment: ROIC and operating margin rose over the last 12 months [RA-T, IS-T], net debt/EBITDA fell to 1.05x [BS], and capex rose with the raised Q3 investment forecast (https://www.marketbeat.com/instant-alerts/transcript-petroleo-brasileiro-sa-petrobras-q3-earnings-call-highlights-2026-11-11/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "State-directed fuel pricing, dividends or non-commercial investment (Venezuela interest) leaks value from minority holders, or a slip in oil prices de-rates a stock up 40.2% in 12 months.", "veto": null},
  "triggers": [
    {"text": "TTM ROIC falls below 12%, showing the rolling rebound from 13.9% has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 12%, meaning capex or pricing policy is consuming the cash behind distributions.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.05x TTM now), showing the balance sheet funds state-directed investment.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "Shares change YoY above 3%, signalling a state-driven capital raise.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 60.0, "basis": "Raised Q3 guidance is delivered and EV/EBITDA moves from 3.2x toward its 5y max of 3.7x [RA], taking the price back to the 59.79 52-week high [HI]; far below the mechanical DCF bull of 428.62, which the fact sheet flags unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 51.0, "basis": "ROIC holds near 18.8% [RA-T] and EV/EBITDA stays near its 5y median of 3.0x [RA] on higher guided output, the price recovering to the 50-day average of 50.96 [ST]; below the base fair value of 168.49 because P/FCF is already above its 5y max of 4.5x [RA] and SOTP/NAV are unavailable."},
    "bear": {"probability": 0.30, "target_price_12m": 36.0, "basis": "Fuel-price or dividend intervention and a weaker real (macro overlay, context only) compress P/E toward its 5y median of 3.7x [RA] on lower earnings, near the 37.40 6-month low [HI]; below the mechanical bear of 108.66, which assumes no political value leakage."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the mechanical fair value is flagged unreliable, and the case turns on state pricing/dividend policy and FCF margin recovering, so a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```
