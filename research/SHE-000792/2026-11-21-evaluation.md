# Evaluation: Qinghai Salt Lake Industry (SHE:000792) — 2026-11-21
## Bear case
Earnings are commodity-driven: ROIC swung from 126.2% (FY2022) to 25.4% (FY2024) and is back at 57.5% TTM [Certain], so the low P/E of 8.8x sits on near-peak margins (operating margin 57.8% TTM, a 2-year high) [Certain] and a commodity reversal would re-rate earnings, not the multiple [Likely]. The Direction change cuts the wrong way for cash: FCF margin fell from 66.1% to 42.2% over 12 months and FCF conversion is 74.7% TTM [Certain]; the cause (working capital or capex) is unverified because the Q3 filing was unreadable [Guessing]. The fall is unexplained: price is -36.0% over 6 months and 30.3% below its 200-day average with no earnings-type reaction [Certain]; the market may be pricing lower lithium/potash prices the TTM figures don't yet show [Guessing]. Bear fair value is 13.31 [Certain]. CNY reporting carries a 3.5% country premium [Certain].
## Bull case
A low-cost brine resource with a net-cash balance sheet (net debt/EBITDA -2.42x, Altman Z 12.89) survives any trough [Likely]. ROIC and ROCE are rising over the last 12 months (24.4% to 57.5%; 15.5% to 22.3%), so the 5-year decline is a cyclical trough already passed, not structural [Likely]. Valuation is at the bottom of its own history: P/E and EV/EBITDA at 2% of their 5y ranges, P/B below its 5y minimum, FCF yield 8.54% [Certain]. EV/EBITDA is below the peer median [Certain]. The reverse DCF implies -4.3% year-1 revenue growth, so the price already discounts a decline [Certain]. Base fair value 25.44 sits above the 21.04 close [Certain]. No dilution (shares 0.00% YoY) [Certain].
## Decision
```json
{
  "ticker": "SHE:000792",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC and ROCE fell over 5 fiscal years from the FY2022 commodity peak but are rising over the last 12 months (ROIC 24.4% -> 57.5%, ROCE 15.5% -> 22.3% [RA-T]); the FCF margin drop (66.1% -> 42.2% [CF-T]) comes with record operating margin and a net-cash balance sheet, consistent with a cyclical swing rather than lost share; cause of the FCF fall unverified (Q3 filing unreadable).", "moat": "narrow", "key_risk": "high", "key_risk_text": "Potash/lithium price reversal: TTM margins are at a 2-year high and the 6-month price fall with no earnings reaction may signal the market pricing lower commodity prices that would cut earnings back toward FY2024 levels.", "veto": null},
  "thesis": "A net-cash, low-cost brine producer trading at the bottom of its own valuation history, but on near-peak commodity earnings whose durability is unverified.",
  "rationale": "Cheap on own history and peers with net cash, but earnings are cyclical and near a 2-year margin high, cash conversion is falling and the cause of the price fall is unverified. The scorecard sets conviction below the buy bar; good but not compelling, so AVOID.",
  "price_at_decision": 21.04,
  "price_date": "2026-11-20",
  "research_note": "research/SHE-000792/2026-11-21.md",
  "triggers": [
    {"text": "ROIC TTM falls below 25%, the FY2024 level: returns revert to mid-cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "Operating margin TTM falls below 40%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "FCF margin TTM falls below 30%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "Net debt/EBITDA rises above 0x on the ratios page: the net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.40, "basis": "Commodity prices hold, ROIC stays near 57.5% TTM [RA] and EV/EBITDA re-rates toward its own history, matching the EV/EBITDA base fair value of 33.40 [valuation file]."},
    "base": {"probability": 0.45, "target_price_12m": 21.46, "basis": "Margins ease from the 57.8% TTM 2-year high [IS-T] toward mid-cycle, so value follows the through-cycle DCF base of 21.46 [valuation file] rather than the blended 25.44."},
    "bear": {"probability": 0.30, "target_price_12m": 13.31, "basis": "Commodity reversal returns returns toward the FY2024 ROIC of 25.4% [RA] with FCF conversion already down to 74.7% [CF,IS], matching the blended bear fair value of 13.31 [valuation file]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades at the bottom of its 5y multiple ranges; what is missing is evidence that near-peak commodity earnings and falling FCF conversion are durable, which a lower price would not supply."
}
```
