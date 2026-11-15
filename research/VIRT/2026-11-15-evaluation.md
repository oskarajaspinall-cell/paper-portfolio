# Evaluation: Virtu Financial, Inc. (VIRT) — 2026-11-15
## Bear case
Virtu's earnings are a function of volumes and volatility, and TTM looks like a peak: operating margin 42.4% against 19.8% in FY2023 [Certain]. The P/E of 8.7x is only cheap if those earnings persist; on its own history the market has always paid single-digit multiples for this cyclicality (5y median 8.0x) [Certain]. ROIC of 10.5% is below FY2021's 15.8% and ROE of 57.0% is flattered by leverage [Likely]. FCF margin of 24.7% sits well under its 2-year high of 41.4% and FCF/NI has fallen from 240.5% to 140.3%, so cash conversion is weakening [Certain]. Debt rose with a $300.0 million incremental Term B-2 draw [company-reported] [Certain]. The valuation points come from trend strength after a +64.8% year: an extended price risks a de-rating as soon as volumes normalise [Likely]. The mechanical fair value is flagged unreliable, so it gives no margin-of-safety anchor [Certain].
## Bull case
The rolling 12 months are rising, not falling: ROIC 8.9% to 10.5%, operating margin 34.3% to 42.4%, FCF margin 14.2% to 24.7% [Certain]; the 5-year declines reflect the FY2023 volume trough, not lost share [Likely]. Nine-month revenue grew 29.2% [company-reported] [Certain], and Q3 was a record trailing EBITDA and EPS period per the results release [Likely]. At 8.7x earnings and a 9.54% FCF yield, far below exchange and broker peers (P/E median 28.2x), the reverse DCF implies -12.4% year-1 revenue, a harsh assumption against current growth [Likely]. Scale and technology in electronic market making plus new venues (Saudi and Abu Dhabi block crossing) widen the franchise [Likely]. A possible sale of the agency brokerage unit could release capital [Guessing]. The stock is above its 200-day average by 11.8%, not severely overextended, with beta 0.69 [Certain].
## Decision
```json
{
  "ticker": "VIRT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 5-year ROIC and 3-year FCF-margin declines start from the FY2021 volume peak and run through the FY2023 trough (operating margin 19.8%); over the last 12 months ROIC rose from 8.9% to 10.5% and FCF margin from 14.2% to 24.7% [RA-T, CF-T], a cyclical pattern with the business intact, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Trading volumes and volatility normalise from record levels, cutting the peak-like operating margin of 42.4% and de-rating a stock that has risen 64.8% in a year.",
    "veto": null
  },
  "thesis": "A scale electronic market maker earning record cyclical profits at 8.7x earnings and a 9.54% FCF yield, but the low multiple mostly reflects earnings that depend on volumes staying elevated.",
  "rationale": "Rolling returns and margins are rising and the stock is cheap against peers, but earnings look cyclically elevated, cash conversion is weaker, the moat is narrow and the fair value is unreliable. The scorecard sets conviction 3, below the buy bar, so this is an AVOID.",
  "price_at_decision": 59.33,
  "price_date": "2026-11-13",
  "research_note": "research/VIRT/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, showing the volume-driven margin gains have reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 8%, back under the level of a year earlier.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 14%, the level of a year earlier, showing cash conversion is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Shares outstanding growth rises above 5% YoY, i.e. earnings are diluted rather than returned.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 75.0, "basis": "Volumes stay elevated and TTM earnings grow with nine-month revenue up 29.2% [company-reported] while the P/E holds near 8.7x [RA], taking the price above the 52-week high of 68.76 [HI]; well below the unreliable mechanical bull of 175.50."},
    "base": {"probability": 0.45, "target_price_12m": 58.0, "basis": "Earnings ease from the peak-like 42.4% operating margin [IS] and the P/E stays near its 5y median of 8.0x [RA]; far below the mechanical base of 124.06, which is flagged unreliable (methods disagree 4.9x, P/E method base 25.33)."},
    "bear": {"probability": 0.30, "target_price_12m": 47.26, "basis": "Volumes normalise toward the FY2023 trough (operating margin 19.8% [IS]) and the stock de-rates from its +64.8% year [ST], meeting the mechanical bear fair value of 47.26."}
  },
  "entry_price": 54.6,
  "entry_basis": "P/E back at its 5y median of 8.0x [RA] on TTM earnings; the mechanical base x 0.8 is above the price and the fair value is flagged unreliable, so the own-history multiple is the anchor.",
  "replaces": null,
  "replacement_reason": null
}
```
