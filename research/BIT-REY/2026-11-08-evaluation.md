# Evaluation: Reply S.p.A. (BIT:REY) — 2026-11-08
## Bear case
The re-rating has happened: the price is up 31.1% in six months and base fair value of 139.20 EUR is only +6.6% above the close [Certain]. The reverse DCF already prices 6.6% year-1 revenue growth, close to delivered growth, leaving little margin for error [Likely]. **Direction change:** FCF margin fell from 13.0% to 10.4% over the last 12 months while operating margin held at 15.2%. That points to working-capital or capex timing, not lost pricing, but the note can't explain it [Guessing]. The moat is soft (talent, client relationships), gross margin is flat at 17.1%, and labour-based IT services face AI substitution of billable work [Guessing]. P/FCF and P/B carry premiums of +56% and +53% to peers [Certain]. Results due Nov 12, 2026 are a gap risk, and the mechanical bear value of 96.55 sits well below the price [Certain].
## Bull case
This is a net-cash IT-services group (net debt/EBITDA -0.92x, Altman Z 4.36) with ROIC of 24.3% TTM, up 4.1pp in the last year, and an operating margin of 15.2% near its 2-year high [Certain]. EV/EBITDA of 9.3x is at the 1st percentile of its own 5y range (median 12.4x) and in line with peers despite higher returns. P/E is at the 6th percentile [Certain]. FCF conversion stays near 100% (102.4% TTM) and the share count fell 1.18%, so earnings are cash-backed [Certain]. Q1 and H1 2026 showed growth in revenue and EBIT [Likely]. If the multiple recovers toward its EV/EBITDA bull value of 172.02, the upside is large [Likely]. The FCF dip alongside stable margins looks like timing, not structural decline [Guessing].
## Decision
```json
{
  "ticker": "BIT:REY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-ROIC Italian IT-services group trades at the bottom of its own 5-year multiple ranges, but after a sharp six-month rebound the price sits just below base fair value and already implies growth in line with delivery, leaving a balanced rather than compelling skew.",
  "rationale": "The quality is real and the multiples are cheap against the stock's own history, but the base fair value leaves little upside after the rebound. The bear value sits well below the price, the moat is soft, the FCF-margin dip is unexplained and results are four days away. Good but not compelling: AVOID, with an entry price below the market.",
  "price_at_decision": 130.60,
  "price_date": "2026-11-06",
  "research_note": "research/BIT-REY/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18% (24.3% now), showing the specialist positioning no longer earns premium returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 12.5%, under the FY2023 five-year low of 12.9%, showing price pressure or AI substitution of billable work.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.5}},
    {"text": "TTM FCF margin falls below 8% (10.4% now, 13.0% a year earlier), showing the cash decline is structural, not working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA on the ratios page turns positive (net debt instead of net cash), for example from a debt-funded acquisition."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 172.0, "basis": "ROIC holds near 24.3% [RA-T] and EV/EBITDA re-rates from 9.3x toward its 5y median 12.4x [RA], matching the EV/EBITDA bull value of 172.02 [fact sheet Fair value]; below the blended bull of 191.85 because the soft moat argues against DCF bull growth."},
    "base": {"probability": 0.5, "target_price_12m": 139.2, "basis": "Operating margin stays near 15.2% [IS-T] with growth close to the 6.6% the reverse DCF implies, so the price converges on the mechanical base fair value of 139.20 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 96.55, "basis": "FCF margin keeps falling from 13.0% toward 10.4% and below [CF-T], with AI pressure on billable services, giving the mechanical bear fair value of 96.55 [fact sheet Fair value]."}
  },
  "entry_price": 111.36,
  "entry_basis": "valuation file: base 139.20 x 0.8; at that level the same quality and own-history cheapness would leave a margin of safety large enough for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
