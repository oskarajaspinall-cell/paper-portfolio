# Evaluation: Marsh & McLennan Companies, Inc. (MRSH) — 2026-10-09
## Bear case
Cheap against its own past is not cheap: MRSH still trades at a premium to broker peers on P/E (21.6x vs 19.2x, +13%) and EV/EBITDA (13.5x vs 12.1x, +12%) [Certain]. The whole group has de-rated, so a return to the 5y median 25.7x P/E is not the natural anchor [Likely]. Returns are slipping, not rising: ROIC 16.5% to 14.5% TTM, ROE 31.0% to 25.9%, net margin 15.4% FY2025 to 14.2% TTM, while net debt/EBITDA climbed to 2.67x on acquisitions such as Accel [Certain]. A 5.65% FCF yield is modest next to the 9-14% yields the portfolio already owns [Certain]. The stock is down 13.3% over 12 months and lags SPY by 29.0pp, a sign the market sees an organic-growth slowdown in broking [Guessing]. Q3 results on Oct 15 are a near-term binary [Certain].

## Bull case
A capital-light oligopoly broker with 24.5% operating margin and FCF conversion of 119.8% of net income, up from ~99% in FY2021 [Certain]. FCF margin has risen to 17.1% TTM from 15.7% [Certain]. Every multiple sits below its own 5-year minimum, and the fact sheet's base fair value of $211.93 implies +20.0% [Certain]. Buybacks (-1.31% shares YoY) plus the $0.990 quarterly dividend return cash steadily [Certain]. Low beta (0.58) and 1.23% short interest make it a defensive compounder [Likely]. If Q3 shows organic growth holding up, the de-rating could reverse toward the base value [Guessing].

## Decision
```json
{
  "ticker": "MRSH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, capital-light insurance broker trades below its own 5-year multiple range, but at a peer premium, with returns drifting down and leverage rising, so the discount looks deserved rather than mispriced.",
  "rationale": "Quality is real, but ROIC, ROE and net margin are all falling while net debt/EBITDA rises to 2.67x. The stock still trades at a P/E and EV/EBITDA premium to peers, and a 5.65% FCF yield is thin next to the holdings. The +20% base fair value rests on own-history re-rating. Good but not compelling, so AVOID.",
  "price_at_decision": 176.67,
  "price_date": "2026-10-08",
  "research_note": "research/MRSH/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 13% (vs 14.5% TTM), showing the broking oligopoly's returns advantage is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM operating margin falls below 23% (vs 24.5% TTM), showing cost or pricing discipline is breaking down.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM FCF margin falls below 14.5%, the FY2022 five-year low, showing cash-earnings quality is fading.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14.5}},
    {"text": "Net debt/EBITDA (ratios page) rises above 3.0x (vs 2.67x TTM), showing M&A-funded leverage is outrunning earnings."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 221.09, "basis": "Q3 confirms steady organic growth and the P/E-led multiple reverts toward the 5y median 25.7x [RA], reaching the fact sheet's bull fair value of 221.09 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 195.59, "basis": "Partial re-rating only: midpoint of the fact sheet bear (179.24) and base (211.93) fair values, held below base because MRSH already trades at a +13% P/E premium to the 19.2x peer median [RA,P:AON,P:WTW,P:AJG,P:BRO]."},
    "bear": {"probability": 0.25, "target_price_12m": 157.04, "basis": "ROIC (14.5% TTM) and net margin (14.2% TTM) keep sliding [RA,IS] and the P/E compresses from 21.6x to the 19.2x peer median [RA,P:AON,P:WTW,P:AJG,P:BRO], below the fact sheet bear fair value of 179.24, which assumes own-history multiples hold."}
  },
  "entry_price": 169.54,
  "entry_basis": "valuation file: base 211.93 x 0.8; at that level the FCF yield and the peer-premium gap would compensate for the falling returns.",
  "replaces": null,
  "replacement_reason": null
}
```
