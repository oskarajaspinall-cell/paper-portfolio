# Evaluation: CME Group Inc. (CME) — 2026-10-11
## Bear case
CME is an excellent business priced as one. The fact sheet's best-method DCF/FCFE blend puts base fair value at 206.10, 26.5% below the 280.56 close, and even the bull case (236.73) sits below the price [Certain]. The reverse DCF needs 13.3% year-one revenue growth sustained into a fade, a high bar for a mature exchange [Likely]. EV/EBITDA (21.5x), EV/Sales (15.2x) and P/FCF (23.9x) carry 34-49% premiums to ICE/CBOE/NDAQ, and P/B (3.8x) is above its own 5y maximum [Certain]. Earnings are flattered by record volumes and high short rates: the macro overlay shows a dovish pivot would cut collateral interest income and normalise ADV simultaneously, a double hit with no margin of safety [Likely]. Relative strength vs SPY is -20.7pp over 6 months and Q3 results land 2026-10-21, an event risk we would buy straight into [Certain].

## Bull case
Quality is exceptional and improving: ROIC 7.1%→12.2%, operating margin 55.5%→65.7%, FCF margin 62.3%, FCF/NI 98.3%, net debt/EBITDA 0.33x [Certain]. The moat is structural: a systemically important clearinghouse with exclusive S&P 500, Nasdaq (to 2039) and Russell (to 2037) futures licences [Certain] (10-K, https://www.sec.gov/Archives/edgar/data/1156375/000115637526000009/cme-20251231.htm). Demand is strong: record September ADV up 22% y/y and record Q3 ADV [Likely] (https://www.prnewswire.com/news-releases/cme-group-reports-record-average-daily-volume-for-september-and-q3-driven-by-growth-across-asset-classes-302897134.html). On earnings, it is not expensive: P/E 23.8x sits at the 12th percentile of its 5y range and in line with peers (23.7x), and the P/E method gives base 283.49 [Certain]. Beta 0.27 and rate-volatility-driven volume make it a diversifier in a higher-for-longer regime [Likely].

## Decision
```json
{
  "ticker": "CME",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class, 65.7%-operating-margin derivatives utility with rising ROIC trades at a fair P/E but well above its own DCF fair value and at 34-49% EV premiums to peers, so the quality is already paid for.",
  "rationale": "Quality and moat merit ownership, but the price offers no margin of safety: best-method base fair value 206.10 vs 280.56, a 13.3% implied growth bar, and earnings at a rate/volume cyclical peak. Only the P/E lens supports the price. Expected 12-month return is roughly flat; good but not compelling, so AVOID and wait for a better entry.",
  "price_at_decision": 280.56,
  "price_date": "2026-10-09",
  "research_note": "research/CME/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, giving up most of the five-year rise from 7.1% to 12.2% [RA].", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM net margin falls below 55%, back into the FY2021-FY2024 range of 53.6%-57.8% [IS], showing fee pricing or interest income is eroding.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below the FY2022 level of 59.8%, reversing the operating-leverage gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 59.8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 325, "basis": "Record ADV (Sept +22% y/y, PRNewswire link) and elevated short rates lift earnings while P/E holds near its 5y median 24.0x [RA], retesting the 52-week high 329.16 [HI]; probability raised a small step per the macro overlay's 'toward bull, small' tilt (research/CME/2026-10-11-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 284, "basis": "P/E stays around its 5y median 24.0x on steady earnings, matching the P/E-method base fair value 283.49 [IS,RA,ST]; above the DCF base 206.10 because CME's 65.7% operating margin and licence moat have improved beyond the history the DCF extrapolates."},
    "bear": {"probability": 0.25, "target_price_12m": 225, "basis": "A dovish pivot cuts collateral interest income and normalises volume (macro overlay bear), de-rating toward the 52-week low 218.31 [HI] and the DCF bull value 236.73 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 218.31,
  "entry_basis": "52-week low 218.31 [HI]: there P/E would sit well below its 5y minimum 22.8x [RA] for a business with rising ROIC; the default base 206.10 x 0.8 = 164.88 is not used because the DCF ignores the P/E-method base 283.49 and CME's improved margins.",
  "replaces": null,
  "replacement_reason": null
}
```
