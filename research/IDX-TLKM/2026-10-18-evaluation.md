# Evaluation: PT Telekomunikasi Indonesia Tbk (IDX:TLKM) — 2026-10-18
## Bear case
Every return and margin metric has fallen for five straight years: ROIC 19.8% to 14.4%, operating margin 30.2% to 24.1%, ROE 25.6% to 16.1% [RA,IS] [Certain]. That steady slide looks structural, not cyclical, and points to competition taking pricing power [Likely]. The share has fallen -38.3% in 12 months, with repeated single-session drops, the latest -12.9% on 2026-10-16 at the 52-week low of 1,900.00 [OV,HI] [Certain]. No allowlisted primary source explains them, and no IR domain or SEC filing was available to check [Certain]. A cheap multiple next to an unexplained, accelerating sell-off can mean the market knows about a dividend, regulatory or state-shareholder event that the TTM figures don't show yet [Guessing]. Earnings on Oct 28, 2026 could confirm it [Certain]. Majority state control and 0.01% insider ownership limit minority alignment [Certain].
## Bull case
The price implies -26.0% revenue growth in year 1 [Fair value], a collapse that mid-to-high-teens ROIC (TTM 16.2%) and ROCE (18.0%) don't support [RA] [Likely]. Cash generation is improving, not falling: FCF margin rose to 28.9% TTM and FCF/NI to 241.0% [CF,IS] [Certain]. The result is a 23.11% FCF yield, P/FCF 4.3x against a 5y minimum of 7.5x, and EV/EBITDA 3.3x against a 5y minimum of 4.9x and a peer median of 4.8x [RA,ST] [Certain]. Net debt/EBITDA is just 0.38x and the share count is flat [BS,ST] [Certain]. Even the mechanical bear fair value of 3,566.38 sits well above the price [Fair value] [Certain]. RSI of 17.8 shows capitulation-level selling [ST] [Certain]. Beta of 0.15 and a domestic IDR business would diversify a US/China-heavy book [ST; macro overlay] [Likely].
## Decision
```json
{
  "ticker": "IDX:TLKM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Indonesia's dominant telecom trades far below its own 5-year minimum multiples at a 23.11% FCF yield, but five years of falling returns and a repeated, unexplained sell-off mean the cheapness may reflect an impairment the data cannot yet show.",
  "rationale": "Valuation is deeply cheap and cash flow is strong, but quality has declined for five consecutive years. The repeated sharp drops, the latest at the 52-week low, have no primary-source explanation we can verify, and results arrive Oct 28. That is not high conviction; cash is acceptable. Reassess after the results and a verifiable cause.",
  "price_at_decision": 1900.00,
  "price_date": "2026-10-16",
  "research_note": "research/IDX-TLKM/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (TTM 16.2%), confirming return erosion has become unsustainable.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 20% (TTM 24.2%), confirming structural margin pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15% (TTM 28.9%), removing the cash-generation offset to the profitability decline.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "A primary-source company or regulatory disclosure explains the repeated sell-off as a lasting earnings, dividend or licence impairment (thesis broken) or rules one out (conviction could rise)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3566.38, "basis": "The sell-off proves non-fundamental and the stock re-rates to the mechanical bear fair value of 3,566.38, still below the DCF base because the five-year ROIC decline [RA] argues against the history-based growth the base case assumes."},
    "base": {"probability": 0.45, "target_price_12m": 2340.00, "basis": "Quality keeps drifting lower [RA,IS] but strong FCF (28.9% margin [CF]) holds a floor, and the price recovers toward the recent 2,340.00 swing high [HI], well below mechanical fair value because that model cannot see the unexplained news-flow (note section 6)."},
    "bear": {"probability": 0.30, "target_price_12m": 1500.00, "basis": "The repeated drops reflect a real impairment confirmed at the Oct 28 results, and EV/EBITDA stays far below its 5y minimum of 4.9x [RA] as earnings and margins step down again."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: it already sits far below the base fair value of 5,914.27 and even the bear of 3,566.38. What blocks a BUY is the five-year quality decline and an unexplained, recurring sell-off, so a lower price would not change the decision without a verifiable cause.",
  "replaces": null,
  "replacement_reason": null
}
```
