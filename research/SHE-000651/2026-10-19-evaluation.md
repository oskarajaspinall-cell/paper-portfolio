# Evaluation: Gree Electric Appliances, Inc. of Zhuhai (SHE:000651) — 2026-10-19
## Bear case
Gree is not cheap against itself: P/E 7.9x sits at the 74% point of its 5y range (5.8x–8.7x) [RA] [Certain]; the low multiple is a permanent China A-share/AC-cycle discount, not a mispricing [Likely]. ROIC has collapsed from 210.2% to 41.2% [RA] [Certain], and the fact sheet shows no revenue-growth figure, so the business may be ex-growth [Guessing]. The +84.8% base fair value rests on a DCF that capitalises a FCF margin that swung from -2.0% to 26.2% [CF,IS] [Certain]; the DCF bear is 8.28 CNY, and the multiple-based EV/EBITDA method gives only 34.82–49.89 [Certain]. Altman Z 1.75 and dilution of 1.16% [ST] add noise [Certain]. No catalyst: 12-month change -3.3% and lagging SPY by -18.0pp [ST,HI] [Certain]; results on Oct 27, 2026 could reset expectations either way [Likely].
## Bull case
Margins have risen every year: gross 24.0% to 30.0%, operating 11.7% to 18.1% [IS] [Certain], showing the duopoly with Midea holds pricing power [Likely]. Net cash (net debt/EBITDA -3.27x) and FCF conversion of 127.0% TTM [BS,CF] [Certain] back a 16.05% FCF yield [ST] [Certain]. EV/EBITDA of 3.3x is at the 25% point of its 5y range and far below the 9.5x peer median; P/FCF 6.2x against a 13.8x peer median [RA] [Certain]. The reverse DCF implies -28.7% year-1 revenue growth [Certain], far worse than rising margins suggest [Likely]. Beta 0.28 [ST] gives diversification [Certain]. Piotroski 7 confirms fundamentals are sound [Certain].
## Decision
```json
{
  "ticker": "SHE:000651",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash AC duopolist with rising margins and a 16.05% FCF yield is cheap against peers but only mid-range against its own history, with no visible growth or catalyst to close a persistent discount.",
  "rationale": "Quality is real and cash yield high, but P/E is near the top of its own 5y range, ROIC is falling, revenue growth is not shown and the DCF upside leans on volatile FCF. Multiple-based value sits close to the price. Good but not compelling: conviction 3, AVOID; buy nearer the EV/EBITDA bear value.",
  "price_at_decision": 39.49,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000651/2026-10-19.md",
  "triggers": [
    {"text": "TTM gross margin falls below 27%, reversing the five-year rise to 30.0% and signalling the AC duopoly's pricing power is breaking.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 27}},
    {"text": "TTM operating margin falls below 15%, giving up the step-up from 13.2% (FY2023) to 18.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROE falls below 15%, showing the ROIC decline has spread into equity returns that have held near 19.0%-24.9%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "The balance sheet turns from net cash to net debt (net debt/EBITDA positive on the ratios page), signalling demand or capital-allocation stress."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 49.89, "basis": "EV/EBITDA re-rates toward its 5y median 4.4x [RA] on rising margins [IS], matching the EV/EBITDA method's bull value 49.89 in the fact sheet fair-value table."},
    "base": {"probability": 0.5, "target_price_12m": 42.0, "basis": "P/E holds between its 5y median 7.7x and max 8.7x [RA] on flat-to-higher earnings, below the mechanical base 72.98 because that DCF capitalises a FCF margin that has swung from -2.0% to 26.2% [CF,IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 29.0, "basis": "P/E de-rates to its 5y minimum 5.8x [RA] on TTM earnings as China AC demand softens, above the mechanical bear 17.13 because net cash (net debt/EBITDA -3.27x [BS]) limits downside."}
  },
  "entry_price": 34.82,
  "entry_basis": "Default base 72.98 x 0.8 is above the price, so anchored instead on the EV/EBITDA method's bear value 34.82 [RA,IS] in the valuation file: at that level even the low-multiple case is priced and the cash yield would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
