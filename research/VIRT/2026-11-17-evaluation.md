# Evaluation: Virtu Financial, Inc. (VIRT) — 2026-11-17
## Bear case
The entry-price hit is a drift, not news: no earnings-type reaction followed the Nov 5 results and the stock is down 2.0% over three months as volumes cooled from the August high of 68.76 [Certain]. The obstacle is unchanged: earnings track volumes and volatility, and TTM operating margin of 42.4% against 19.8% in FY2023 looks cyclically elevated [Likely]. The Direction change lines matter: ROIC is below FY2021's 15.8% and FCF margin of 24.7% sits well under its 2-year high of 41.4%, with FCF/NI down from 240.5% to 140.3%; those are cycle effects, but they show how fast cash and returns can fall [Likely]. P/FCF and P/B are above their 5y maxima [Certain]. Valuation support comes from trend strength after a +61.8% year: an extended price risks a de-rating if volumes normalise [Likely]. The mechanical fair value is flagged unreliable, so there is no margin-of-safety anchor [Certain].
## Bull case
The last 12 months are rising: ROIC 8.9% to 10.5%, operating margin 34.3% to 42.4%, FCF margin 14.2% to 24.7% [Certain]; the 5-year declines run from the FY2021 peak through the FY2023 trough, not lost share [Likely]. Nine-month revenue grew 29.2% [company-reported] and Q3 set record trailing EBITDA and EPS per the call transcript [Likely]. At 8.4x earnings and a 9.94% FCF yield, far below the peer P/E median of 26.3x, the reverse DCF implies -12.6% year-1 revenue, a harsh assumption against current growth [Likely]. New Saudi and Abu Dhabi block-crossing venues extend the franchise [Likely]. A possible agency-brokerage sale could release capital [Guessing]. The price is +9.5% above its 200-day average with beta 0.69 [Certain].
## Decision
```json
{
  "ticker": "VIRT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 5-year ROIC and 3-year FCF-margin declines start at the FY2021 volume peak and pass through the FY2023 trough (operating margin 19.8% [IS]); over the last 12 months ROIC rose from 8.9% to 10.5% and FCF margin from 14.2% to 24.7% [RA-T, CF-T], a cyclical pattern with the business intact, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Trading volumes and volatility normalise from record levels, cutting the peak-like 42.4% operating margin and de-rating a stock up 61.8% in a year.",
    "veto": null
  },
  "thesis": "A scale electronic market maker earning record cyclical profits at 8.4x earnings and a 9.94% FCF yield, but the low multiple mostly reflects earnings that depend on volumes staying elevated.",
  "rationale": "The fall to the entry level is a drift as volumes cooled, not a stock-specific overreaction, and it does not remove the obstacle: earnings look cyclically elevated, the moat is narrow and fair value is unreliable. Evidence matches the 2026-11-15 AVOID; the scorecard keeps conviction 3, below the buy bar.",
  "price_at_decision": 58.30,
  "price_date": "2026-11-16",
  "research_note": "research/VIRT/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, back to the FY2024 level, showing the volume-driven margin gains have reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 8%, under the level of a year earlier.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 14%, the level of a year earlier, showing cash conversion is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "A loss-making trading quarter or a risk-limit breach is disclosed in a 10-Q or 8-K."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 75.0, "basis": "Volumes stay elevated, earnings grow with nine-month revenue up 29.2% [company-reported] and the P/E holds near 8.4x [RA], lifting the price above the 52-week high of 68.76 [HI]; well below the unreliable mechanical bull of 174.11."},
    "base": {"probability": 0.45, "target_price_12m": 58.0, "basis": "Earnings ease from the peak-like 42.4% operating margin [IS] while the P/E stays near its 5y median of 8.0x [RA]; far below the mechanical base of 123.12, flagged unreliable (methods disagree 4.9x, P/E method base 25.33)."},
    "bear": {"probability": 0.30, "target_price_12m": 46.91, "basis": "Volumes normalise toward the FY2023 trough (operating margin 19.8% [IS]) and the stock de-rates from its +61.8% year [ST], meeting the mechanical bear fair value of 46.91."}
  },
  "entry_price": 54.6,
  "entry_basis": "P/E back below its 5y median of 8.0x [RA] on TTM earnings, as set on 2026-11-15; the mechanical base x 0.85 is above the price and the fair value is flagged unreliable, so the own-history multiple is the anchor.",
  "replaces": null,
  "replacement_reason": null
}
```
