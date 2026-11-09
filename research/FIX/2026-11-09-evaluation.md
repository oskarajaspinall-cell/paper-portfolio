# Evaluation: Comfort Systems USA, Inc. (FIX) — 2026-11-09
## Bear case
Today's returns are probably close to their peak. ROIC went from 41.9% in FY2024 to 103.2% TTM, and operating margin from 10.6% to 16.8% [RA][IS], both on one data-center boom [Likely]. About 94.7% of revenue comes from fixed-price project bids [company-reported] (https://www.sec.gov/Archives/edgar/data/1035983/000110465926118159/fix-20260930x10q.htm). Management expects cost and supply-chain pressure to last several quarters (same 10-Q), so margins can reset quickly [Likely]. The FCF margin of 19.5% is helped by billings in excess of costs and deferred revenue, which is timing that can reverse [Likely]. The CFO is retiring and leadership changes in 2027 [Certain]. The base fair value of 991.73 is below the price, and its methods disagree 3.8x. The EV/EBITDA method, which uses normalised earnings, gives only 347.80 [Certain]. At 22.0x P/E the stock is priced on peak earnings [Likely]. The stock fell 40.6% in three months after a beat, on worries about margins [Certain].
## Bull case
Every quality measure is rising, on both the 5-year and the rolling 12-month views. ROIC, ROCE, operating margin and FCF margin are all at their 2-year highs [RA-T][IS-T][CF-T] [Certain]. Q3 backlog hit a record of 17.8B, against 14.06B in June. Revenue rose 54% year on year, giving visibility into 2027 [Likely] (/stocks/fix/transcripts/715227-q3-2026/). The company holds net cash (net debt/EBITDA -0.81x), its Altman Z is 7.27, the share count is falling and the dividend was raised [Certain]. P/FCF of 14.6x sits at 6% of its 5-year range and is 35% below peers. EV/EBITDA is at 14% of its range [RA] [Certain]. The price implies only 9.5% revenue growth in year 1 while the backlog is compounding [Certain]. Scarce skilled MEP labour gives it a narrow but real edge [Likely].
## Decision
```json
{
  "ticker": "FIX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin are all rising over 1 and 3 years [RA-T][IS-T][CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Peak margins on fixed-price data-center projects revert as cost pressure persists and working-capital inflows reverse (10-Q), cutting earnings toward the normalised EV/EBITDA value.", "veto": null},
  "thesis": "A net-cash, record-backlog MEP contractor whose cash-flow multiples sit near 5-year lows, but on what are probably peak margins from one data-center cycle, with the price near the mechanical base fair value.",
  "rationale": "The business quality is excellent, but the price sits about at the mechanical base fair value and the earnings are probably peak-cycle. A margin reset would leave large downside, and the upside is not enough to reach high conviction. Avoid; re-research at the entry price.",
  "price_at_decision": 1017.50,
  "price_date": "2026-11-06",
  "research_note": "research/FIX/2026-11-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 22%, reversing most of the expansion from 21.0% in FY2024 to 25.7%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 22}},
    {"text": "TTM operating margin falls below 12%, showing the data-center margin step-up has reset.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 10%, showing the working-capital inflow has reversed.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Reported backlog (10-Q/10-K MD&A) declines sequentially for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1560, "basis": "Record backlog of 17.8B sustains margins and the DCF bull case holds, in line with the fact sheet's bull fair value of 1,562.62 [IS,CF,RA]."},
    "base": {"probability": 0.45, "target_price_12m": 1000, "basis": "Growth roughly matches the 9.5% the reverse DCF implies and margins stay flat, close to the base fair value of 991.73 [fact sheet fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 600, "basis": "Cost pressure flagged in the 10-Q pushes the operating margin back toward the FY2024 level of 10.6% [IS], moving the price toward the normalised EV/EBITDA value of 347.80, though the backlog limits how far it falls."}
  },
  "entry_price": 793.38,
  "entry_basis": "valuation file: base 991.73 x 0.8 (default 20% margin of safety) [IS,BS,CF,RA,ST,HI]. The fair value is flagged unreliable, so a hit triggers re-research only.",
  "replaces": null,
  "replacement_reason": null
}
```
