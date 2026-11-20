# Evaluation: First Solar, Inc. (FSLR) — 2026-11-20
## Bear case
The cheapness is on accounting earnings, not cash: P/FCF is 69.2x and FCF yield 1.45% [Certain]. FCF margin fell from 12.2% to 4.6% over the last 12 months, 26.1pp below its 2-year high, because nine-month operating cash flow was -$402.7m as government grants receivable rose $1,285.8m [company-reported] (https://www.sec.gov/Archives/edgar/data/1274494/000127449426000212/fslr-20260930.htm) [Certain]. Much of the margin is policy subsidy; TTM gross margin of 49.3% sits above any fiscal year (high 44.2%), so this looks like peak earnings the market refuses to capitalise [Likely]. Q3 revenue fell 22.8% [company-reported] and bookings moderated on Section 232 uncertainty [Likely]. The trend is broken: 28.0% below the 200-day, -40.2% over 12 months, beta 1.71, short interest 11.04% [Certain]. Rising real yields lift developers' financing costs (macro overlay, tilt toward bear, small) [Likely]. The buyback is not funded by operations [Likely].

## Bull case
Returns are high and rising on a rolling basis: TTM ROIC 19.8% (+2.3pp a year), operating margin 37.7% at its 2-year high, net cash at -0.52x net debt/EBITDA, debt only $107.7m against $1,624.1m cash and securities [company-reported] [Certain]. P/E 8.6x and EV/EBITDA 6.0x sit below their 5-year minimums (14.6x, 10.1x) and half the peer median of 12.0x [Certain]. The cash shortfall is a timing gap: a grants receivable from the government, not lost sales, plus capex for the Gaffney plant [Likely]. US-made, non-Chinese supply is favoured by tariffs and foreign-entity credit limits, and thin film sits outside crystalline-silicon trade remedies [Likely]. State-level Democratic gains may support utility-scale demand (https://www.barrons.com/articles/first-solar-stock-upgrade-midterm-elections-c4eeebbb) [Guessing]. Base fair value 173.44 is above the price [Certain].

## Decision
```json
{
  "ticker": "FSLR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 12.2% -> 4.6% TTM because government grants receivable rose $1,285.8m and inventory/receivables built over nine months, while operating margin and ROIC rose [company-reported] (https://www.sec.gov/Archives/edgar/data/1274494/000127449426000212/fslr-20260930.htm); a receivable timing gap and Gaffney capex, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Policy-driven earnings peak: if the manufacturing credit, tariff protection or the trade investigation outcome turn, gross margin (49.3% TTM vs a FY high of 44.2%) and bookings fall back together.",
    "veto": null
  },
  "thesis": "A net-cash, high-return US module maker trades below its own 5-year minimum P/E and EV/EBITDA, but on policy-boosted peak earnings that are not yet converting to cash.",
  "rationale": "Quality and balance sheet are strong and multiples are below their own history, but the earnings are subsidy-heavy, FCF has collapsed on a grants receivable, bookings moderated and the trend is broken. The scorecard does not reach the buy bar; good but not compelling is an AVOID.",
  "price_at_decision": 151.95,
  "price_date": "2026-11-19",
  "research_note": "research/FSLR/2026-11-20.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing the policy-driven returns are fading.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 40%, i.e. the credit benefit or module pricing erodes.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin turns negative, i.e. grants receivable keep outrunning cash receipts.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA (ratios page) rises above 1.0x, i.e. net cash is spent on buybacks and capex."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 240, "basis": "Grants receivable convert to cash and bookings recover, so EV/EBITDA re-rates from 6.0x toward its 10.1x 5y minimum [RA] on TTM EBITDA [IS]; below the mechanical bull 303.53 because Q3 bookings moderated (note)."},
    "base": {"probability": 0.45, "target_price_12m": 173.44, "basis": "Mechanical EV/EBITDA base fair value 173.44 [IS,RA]: earnings hold near TTM and the multiple stays well below its 5y median 11.9x [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 125, "basis": "Gross margin reverts from 49.3% toward the FY2025 40.6% [IS] as policy support or pricing fades while the multiple stays near 6.0x [RA]; below the mechanical bear 148.49, and the bear weight raised slightly per the macro overlay's small tilt toward bear on rising real yields (research/FSLR/2026-11-20-macro.md)."}
  },
  "entry_price": 147.42,
  "entry_basis": "valuation file: base 173.44 x 0.85.",
  "replaces": null,
  "replacement_reason": null
}
```
