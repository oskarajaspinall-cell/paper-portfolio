# Evaluation: Fair Isaac Corporation (FICO) — 2026-11-19
## Bear case
The fall is not a results miss; it is the market pricing a reset of the mortgage Scores economics that the trailing figures cannot yet show [Likely]. The 10-K's new risk factors say FHFA "lender choice" lets mortgage lenders pick VantageScore, owned by the three bureaus, and that this could hurt revenue [Certain]. Management withheld FY27 guidance while moving to bespoke mortgage pricing, so the 51.0% operating margin and 80.2% ROIC describe the old flat-fee regime [Likely]. Buybacks are debt-funded and net debt/EBITDA has risen to 3.87x, leaving less room if pricing resets [Certain]. Short interest is 12.24% and rose 12.7% in a month [Certain]. The trend is broken: price is -36.5% versus its 200-day average and -71.3pp against SPY over 12 months [Certain]. Higher yields (10y 5.1%) weigh on mortgage volume, though the overlay treats macro as context only [Likely].

## Bull case
On reported numbers this is an exceptional franchise: 86.1% gross margin, 42.2% FCF margin and ROIC of 80.2%, all still rising over the last 12 months [Certain]. FY26 revenue rose 27% and FCF 40% per the results call [Certain]. At 18.1x P/E, 14.9x EV/EBITDA and 13.5x P/FCF, the shares sit near the bottom of their 5-year ranges and below the peer median, a 7.38% FCF yield [Certain]. The reverse DCF implies only 8.6% year-1 revenue growth, well under recent growth [Certain]. Large lenders (DHI Mortgage, LoanDepot, CMG Financial) have joined the FICO Preferred Program and keep pulling FICO Scores [Likely]. Software platform ARR grew 72% [Likely]. Shares outstanding fell 6.40% in a year [Certain]. If the bespoke-pricing transition settles without a deep price cut, the multiple has room to recover [Guessing].

## Decision
```json
{
  "ticker": "FICO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A franchise with 80.2% ROIC trades near its 5-year multiple lows, but the discount prices an unquantified reset of mortgage Scores pricing under FHFA lender choice that guidance no longer bounds.",
  "rationale": "The entry-price hit came from no new adverse results: the fall reflects withheld FY27 guidance and the mortgage pricing reset. Reported quality is superb, but the key risk is high and unbounded, leverage is 3.87x and the reliable DCF base sits near the price. Scorecard conviction 2; below the buy bar (owner rule: high conviction only), so AVOID.",
  "price_at_decision": 677.75,
  "price_date": "2026-11-18",
  "research_note": "research/FICO/2026-11-19.md",
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 12 months and 3 years [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "FHFA lender choice and the bespoke mortgage pricing transition cut Scores pricing; FY27 guidance withheld, so the size is unknown.",
    "veto": null
  },
  "triggers": [
    {"text": "TTM operating margin falls below 45%, showing the mortgage pricing reset is eroding Scores economics.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "TTM ROIC falls below 50%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 35%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35}},
    {"text": "Scores segment revenue falls year on year in a 10-Q or 10-K, evidencing mortgage price or volume loss to VantageScore."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 982.86, "basis": "Bespoke pricing settles with lenders staying in the Preferred Program and the price reaches the blended base fair value 982.86 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 732.28, "basis": "The pricing overhang persists and the price tracks the DCF base 732.28, used over the blend because the fair value is flagged unreliable (methods disagree 2.0x) [fact sheet fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 397.97, "basis": "Lender choice moves mortgage volume to VantageScore and the price falls to the bear fair value 397.97 [fact sheet fair value], as the new 10-K risk factors warn (research/FICO/2026-11-19.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unbounded mortgage Scores pricing reset under FHFA lender choice is. A lower price would not change the decision until guidance or filings size the reset.",
  "replaces": null,
  "replacement_reason": null
}
```
