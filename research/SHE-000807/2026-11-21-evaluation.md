# Evaluation: Yunnan Aluminium (SHE:000807) — 2026-11-21
## Bear case
The cheapness is a peak-earnings mirage [Likely]. TTM ROIC 60.7% and operating margin 26.8% sit far above the FY2021-FY2025 range (operating margin 11.1%-17.4%) [Certain]; the five-year ROCE and operating-margin trend is falling, and the last-12-month surge (operating margin 11.8% to 26.8%) is a commodity-price upswing, not a structural gain [Likely]. P/E 5.5x and EV/EBITDA 2.8x are below their 5y minimums because the market prices mean reversion [Likely]; the reverse DCF already implies -11.7% year-1 revenue. The price is 25.8% below its 200-day average, down 31.0% over six months with RSI 21.3, and no earnings reaction explains the fall [Certain]: the driver is unverified, possibly a falling aluminium price that has not yet reached reported margins [Guessing]. The moat is at best power-cost position [Guessing]; a commodity smelter has no pricing power [Likely]. The mechanical fair value is built on peak cash flows [Likely].
## Bull case
Even through the cycle this is a good smelter: ROIC 17.0%-28.0% across FY2021-FY2025 [Certain], net cash (net debt/EBITDA -1.05x), Altman Z 10.53, Piotroski F 8 and FCF above net income every year shown [Certain]. FCF yield 20.80% and a base fair value of 30.58 CNY (bear 26.57) leave room even if margins halve [Likely]. Shares are not being diluted (-0.20% YoY) [Certain]. The fall coincides with a broad market dip (SPY -9.5% over 3 months) rather than a reported deterioration: the Q3 report of 2026-10-29 produced no earnings-type reaction [Certain], and TTM margins were still rising at 2026-09-30 [Certain]. If aluminium holds, the cash build funds dividends from a net-cash balance sheet [Guessing].
## Decision
```json
{
  "ticker": "SHE:000807",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 or 3 years: TTM ROIC, ROCE, operating and FCF margin all rose to 2-year highs at 2026-09-30 [RA-T, IS-T, CF-T]; the 5-year FY decline in ROCE and operating margin reflects the FY2021 cyclical high, now exceeded.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Earnings are at a cyclical peak (TTM operating margin 26.8% vs 11.1%-17.4% in FY2021-FY2025 [IS]); a fall in the aluminium price would revert margins and make today's low multiples a value trap. The 31.0% six-month price fall with no earnings reaction suggests the market already sees it.",
    "veto": null
  },
  "thesis": "A net-cash, high-return aluminium smelter trading at below-history multiples, but on peak-cycle earnings with a broken price trend and an unexplained fall.",
  "rationale": "Quality and balance sheet are strong and multiples are cheap, but the cheapness rests on peak commodity margins, the moat is a cost position at best, and the fall is unexplained. The scorecard lands below the buy line; good but not compelling is an AVOID.",
  "price_at_decision": 21.01,
  "price_date": "2026-11-20",
  "research_note": "research/SHE-000807/2026-11-21.md",
  "triggers": [
    {"text": "TTM operating margin falls below 14% (back to the FY2025 level) [IS-T].", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 20% [RA].", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "FCF margin falls below 10% [CF].", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 30.58, "basis": "Aluminium holds and peak margins persist, so the price returns to the mechanical base fair value of 30.58 CNY [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 23.0, "basis": "Margins ease from the 26.8% TTM peak toward the FY2025 14.7% [IS] while P/E stays well below its 5y median 10.7x [RA], leaving the price near the EV/EBITDA method's 20.84 base plus net cash support [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 15.0, "basis": "Operating margin reverts toward the FY2024 11.1% [IS] and the multiple does not re-rate, so earnings roughly halve; below the 26.57 mechanical bear because that is built on peak TTM cash flows (Bear case)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5y minimum multiples; the block is peak-cycle earnings, no moat and an unexplained fall. A lower price on the same evidence would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
