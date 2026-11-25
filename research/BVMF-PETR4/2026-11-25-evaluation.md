# Evaluation: Petróleo Brasileiro S.A. - Petrobras (BVMF:PETR4) — 2026-11-25
## Bear case
The fall has a cause in the company itself: the 2027-2031 plan, published 2026-11-24, raises investment and leaves less cash for shareholders than the market expected [Likely]. The state controls capex, dividends and fuel pricing, and fuel pricing was questioned on the Q3 call [Likely]. Cash conversion is already weak. FCF margin is 19.0%, flat on the year and well below its 2-year high of 28.2%. FCF/NI is 80.0% [Certain]. More capex points lower [Likely]. Over three years ROIC, operating margin and FCF margin all fell from the FY2022 oil peak. The rebound over the last year, with ROIC at 21.3%, rests on oil prices that no fact-sheet figure confirms will last [Likely]. P/FCF is 5.0x, above its 5y max [Certain]. The macro overlay finds a weak real and a risk-off market, both of which hit a USD holder [Likely]. The fair value is flagged unreliable [Certain].
## Bull case
Earnings are cheap: P/E 3.8x against 11.7x for peers, EV/EBITDA 2.7x against 5.7x, and a 19.88% FCF yield [Certain]. The reverse DCF implies revenue shrinking 15.1% in year 1, while Q3 brought raised guidance and record refinery output [Likely]. The last year is a cyclical recovery, not a breakdown. Over the year ROIC went from 14.6% to 21.3% and operating margin from 29.6% to 38.1%. Piotroski F is 8 and net debt/EBITDA is 1.11x [Certain]. An extraordinary dividend was approved on 2026-11-23 [Likely]. Low-cost pre-salt reserves are a real scale advantage [Likely]. RSI of 23.9 shows the stock is deeply oversold [Certain]. The price drop may already price in the bad news of less cash to shareholders, which a weaker real partly offsets in BRL earnings [Guessing].
## Decision
```json
{
  "ticker": "BVMF:PETR4",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC, operating margin and FCF margin date from the FY2022 oil-price peak (ROIC 33.5%) [RA]. The last 12 months are rising (ROIC 14.6% -> 21.3%, operating margin 29.6% -> 38.1%) [RA-T, IS-T] with net debt/EBITDA at 1.11x [BS,IS]. The weaker FCF margin reflects heavy capex rather than lost share, per the note's capital-allocation section.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "State-directed capital allocation: the 2027-2031 plan raises capex and leaves less cash for shareholders than expected, and fuel-pricing scrutiny persists (note sections 5-6). Higher capex can push FCF conversion lower and widen the governance discount.",
    "veto": null
  },
  "new_evidence": {
    "type": "guidance",
    "text": "The 2027-2031 strategic plan was published on 2026-11-24, after the 2026-11-15 AVOID, and the price fell 10.7% since that decision (https://www.marketbeat.com/instant-alerts/event-petrobras-unveils-122-billion-plan-sees-potential-for-10-billion-more-in-dividends-2026-11-24/)."
  },
  "thesis": "A cash-rich pre-salt producer trades at a deep discount to peers, but the state-directed capex plan cuts the cash that reaches minority shareholders, so the discount may be deserved.",
  "rationale": "The drop is a reaction to a capex-heavy plan that lowers shareholder cash and confirms the governance risk. It is not an overreaction that leaves the case intact. Cheapness is real, but FCF conversion is weakening and the trend is broken (below the 200-day). Conviction 3: AVOID.",
  "price_at_decision": 40.55,
  "price_date": "2026-11-24",
  "research_note": "research/BVMF-PETR4/2026-11-25.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, under the FY2024-25 lows, showing returns are breaking beyond a cyclical normalisation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 12%, showing the capex plan is eating the cash that funds dividends.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 28%, under the year-earlier 29.6%, signalling fuel-price intervention or an oil downturn.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.0x, showing the capex plan is debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 59.79, "basis": "The plan's dividend upside and the Q3 guidance raise re-rate the stock back to its 6-month high of 59.79 [HI] with EV/EBITDA near its 5y max of 3.7x [RA]. This is far below the unreliable DCF bull, which is flagged outside the sanity band."},
    "base": {"probability": 0.45, "target_price_12m": 46.0, "basis": "EV/EBITDA moves from 2.7x toward its 5y median of 3.0x [RA] on TTM EBITDA, with the governance discount to peers (5.7x) intact. This sits below the DCF base of 99.27 because that value is flagged unreliable and SOTP/NAV is unavailable."},
    "bear": {"probability": 0.30, "target_price_12m": 31.0, "basis": "Capex absorbs cash, oil normalises and the multiple compresses toward its 5y lows (EV/EBITDA 1.7x [RA]), back near the 52-week low of 29.53 [HI]. The bear probability is raised slightly for the macro overlay's small tilt toward bear (weak BRL, risk-off; research/BVMF-PETR4/2026-11-25-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock is already far below every multiple anchor. What holds it back is state-directed capital allocation and weakening FCF conversion, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
