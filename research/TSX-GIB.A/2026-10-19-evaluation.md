# Evaluation: CGI Inc. (TSX:GIB.A) — 2026-10-19
## Bear case
The de-rating is industry-wide, not company-specific: peers trade at a 9.3x EV/EBITDA median [RA], so CGI's discount to peers is only modest and the "below its 5y minimum" signal mostly reflects a sector that markets now price for AI-driven compression of labour-based IT services [Likely]. The mechanical fair value (base 196.18) is built on own-history multiples of 13.4x EV/EBITDA that the group no longer earns, so it likely overstates value [Likely]. Quality is edging down at the margin: TTM ROIC of 14.3% is the lowest in the series and ROE fell to 17.0% [Certain]. Leverage has nearly doubled from 0.71x to 1.31x net debt/EBITDA with new notes issued in September 2026 [Certain]. The fact sheet shows no revenue-growth figure, so we cannot confirm the top line is holding [Certain]; the stock is down 12.4% over 12 months [Certain].
## Bull case
The price implies a 9.4% revenue decline in year one [Certain], against five years of flat 16.1%-16.5% operating margins and 20% gross margins [Certain] that show no sign of pricing pressure yet. An 11.39% FCF yield [Certain] with FCF conversion of 143% [Certain] funds buybacks that cut the share count 5.11% in a year [Certain], so even a flat business compounds per-share value at a double-digit rate [Likely]. CGI is still cheaper than peers on P/E (13.2x vs 16.2x), P/FCF and P/B [Certain], and long-duration government and banking contracts carry high switching costs [Likely]. Beta of 0.19, Altman Z of 3.39 and short interest of 0.63% [Certain] signal neither distress nor a crowded short. Steady contract wins (France's Ministry of Agriculture, CGI Federal) and tuck-ins like Callibrity point to a functioning franchise [Likely]. Even a re-rating only to its 5y-minimum P/E of 16.5x [RA] offers meaningful upside [Likely].
## Decision
```json
{
  "ticker": "TSX:GIB.A",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A stable-margin, 14%-ROIC IT services franchise with an 11.39% FCF yield and 5% annual share shrinkage trades below its own 5-year minimum on every multiple and below peers on P/E, where the price implies a 9.4% revenue decline its fundamentals do not show.",
  "rationale": "Cash yield plus buybacks cushion the downside even if no re-rating comes, and margins remain steady. Sector-wide AI-disruption pricing, slipping ROIC/ROE, rising leverage and no revenue-growth data cap conviction at 4, not 5: standard volatility-scaled core size. Mechanical fair value likely overstates value, so scenario targets sit well below it.",
  "price_at_decision": 106.42,
  "price_date": "2026-10-16",
  "research_note": "research/TSX-GIB.A/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, well under the five-year range of 14.8%-16.5%, signalling the switching-cost moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 15%, breaking the 16.1%-16.5% band held for five years, showing AI-driven pricing pressure or broken cost discipline.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 11%, under the five-year low of 13.3%, showing cash generation can no longer fund buybacks and tuck-ins.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11}},
    {"text": "Annual revenue (income statement) declines year on year for a full fiscal year, evidencing real displacement of labour-based services by AI."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165, "basis": "Margins hold and the multiple recovers toward the EV/EBITDA-method base of 163.32 (fair value, own 5y median [RA]); kept below the 196.18 blended base because DCF assumes history-level multiples peers no longer pay (peer median 9.3x [RA])."},
    "base": {"probability": 0.5, "target_price_12m": 133, "basis": "Flat 16.4% operating margin [IS] and buybacks [ST] with P/E recovering only to its 5y minimum of 16.5x [RA] on TTM EPS, below the mechanical bear 148.17 because the sector de-rating looks durable."},
    "bear": {"probability": 0.25, "target_price_12m": 88, "basis": "AI-disruption fears hit revenue, ROIC keeps sliding from 14.3% [RA] and the multiple stays at its current lows, taking the price back toward the 52-week low of 83.34 [HI]."}
  }
}
```
