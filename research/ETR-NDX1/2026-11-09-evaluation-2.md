# Evaluation: Nordex SE (ETR:NDX1) — 2026-11-09
## Bear case
Nordex is a cyclical onshore turbine OEM that lost money or broke even in four of the last five fiscal years [Certain]; the TTM operating margin of 10.1% and ROCE of 27.2% are the best in the series, so the stock is being valued on what may be peak margins [Likely]. FCF of 200.6% of net income likely leans on customer prepayments and working capital that reverse when orders slow [Guessing]. Shareholders were diluted 12.14% in a year and Altman Z of 2.63 sits in the grey zone [Certain]. P/B of 6.4x and EV/Sales of 1.0x are above their 5y maxima [Certain]. The mechanical bear fair value is negative, showing how sensitive the DCF is to margin assumptions [Certain]. Management itself flags execution, permitting and policy uncertainty, and the Turkey/US order exposure is unquantified and its country risk unverified per the macro overlay [Likely]. No Direction change line is printed: every rolling metric is rising [Certain].
## Bull case
The recovery is real and accelerating on a rolling basis: operating margin 10.1% vs 4.3% a year earlier, FCF margin 11.7% vs 7.7% [Certain]. Q3 2026 revenue rose 28% with EBITDA margin 12.7% and FY2026 margin guidance was raised to 11.5%-12.5% [Likely] (Q3 call transcript, fact sheet). Order intake rose on Turkey and US recovery [Likely] (Reuters, fact sheet). The balance sheet is net cash at -2.41x net debt/EBITDA [Certain]. At 8.4x EV/EBITDA, P/FCF 10.3x and a 9.71% FCF yield it trades at a deep discount to peers on every multiple (EV/EBITDA peer median 18.4x) [Certain], and the reverse DCF implies -5.9% year-1 revenue growth, a downturn that the backlog and guidance do not show [Likely]. A growing service fleet should make margins stickier than in past cycles [Guessing].
## Decision
```json
{
  "ticker": "ETR:NDX1",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no falling metric: ROCE, operating margin and FCF margin all rise over 1 and 3 years [RA-T, IS-T, CF-T].",
    "moat": "none",
    "moat_text": "Onshore turbines are a competitive, cyclical market; four loss or near-zero years in five show no pricing power through a downturn; the service base is not yet proven as a moat [IS].",
    "key_risk": "medium",
    "key_risk_text": "Margins at a series high revert as the order cycle or wind policy turns and prepayment-driven cash flow reverses; management cites execution, permitting and policy uncertainty (Q3 2026 call).",
    "veto": null
  },
  "thesis": "A net-cash onshore wind OEM with sharply recovering margins trades at a deep peer discount, but the price is set on series-high margins in a cyclical, moat-less industry.",
  "rationale": "Cheap on cash multiples with net cash and accelerating margins, but no proven moat, peak-like cyclical margins, dilution and an unreliable mechanical bear make the skew good, not compelling. Conviction set by the scorecard; no position.",
  "price_at_decision": 42.98,
  "price_date": "2026-11-06",
  "research_note": "research/ETR-NDX1/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 6%, giving up most of the recovery from 2.3% (FY2024) to 10.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6}},
    {"text": "TTM gross margin falls below 20%, back under the FY2024 level of 20.5%, signalling turbine pricing pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 3%, under the FY2024 level of 3.6%, showing the prepayment-driven cash inflow has reversed.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt/EBITDA rises above 1.0x (-2.41x now), meaning the net-cash cushion is gone.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 62.81, "basis": "Raised FY2026 margin guidance is delivered and sustained, matching the mechanical bull fair value 62.81 [valuation file] with the peer discount narrowing (EV/EBITDA peer median 18.4x [RA])."},
    "base": {"probability": 0.45, "target_price_12m": 48.0, "basis": "Margins hold near TTM; value sits between the EV/EBITDA method 39.80 and DCF 63.81 [valuation file], below the blended base 55.81 because the DCF capitalises series-high cyclical margins [IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 30.0, "basis": "Order cycle or policy turns, operating margin reverts toward the FY2025 7.3% [IS] and EV/EBITDA sits at its 5y min 8.0x [RA] on lower EBITDA; the mechanical bear -4.23 is not meaningful for a net-cash company."}
  },
  "entry_price": 33.24,
  "entry_basis": "Base fair value 55.81 x 0.8 is above the price, so it cannot anchor; used the 6-month low 33.24 [HI], where EV/EBITDA would sit below its 5y min 8.0x [RA] and the price would discount the bear scenario.",
  "replaces": null,
  "replacement_reason": null
}
```
