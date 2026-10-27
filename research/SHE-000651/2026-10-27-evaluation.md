# Evaluation: Gree Electric Appliances, Inc. of Zhuhai (SHE:000651) — 2026-10-27
## Bear case
The fall coincides with the Q3 2026 report filed on 2026-10-26, and we cannot read its figures, so the cause is unexplained [Certain]. What the fact sheet does show is a profitability peak rolling over: TTM ROIC 34.1% vs 46.8% in FY2025, ROE 16.3% vs 19.8%, operating margin 16.4% vs 17.5%, net margin 15.5% vs 17.0% [Certain]. FCF conversion dropped to 93.6% from 154.0%, so the FY2025 cash surge is not repeating [Certain]. Even after the dip, P/E 8.3x sits 86% up its 5y range and P/FCF 8.8x 88% up its range, so the stock is not cheap against its own earnings history while earnings fall [Certain]. Shares rose 0.87% YoY: no buyback support [Certain]. Domestic AC demand is tied to China property and consumption, which no available series tracks (macro overlay) [Likely]. The DCF bear of 0.92 shows how sensitive value is to falling cash flow [Certain].

## Bull case
Gree remains a net-cash (net debt/EBITDA -2.29x), high-margin franchise: gross margin 29.0% and operating margin 16.4% are still well above FY2021 [Certain]. The FCF yield is 11.36% and P/E 8.3x is far below the peer median of 13.4x [Certain]. The reverse DCF implies a -15.6% year-1 revenue fall, a harsher outcome than the margin data show [Likely]. The base fair value of 51.99 sits well above the 37.18 close [Certain]. Beta 0.28 and a stable yuan limit macro shock (macro overlay) [Likely]. If Q3 shows only a mild earnings dip, the reaction is an overreaction [Guessing].

## Decision
```json
{
  "ticker": "SHE:000651",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-margin AC leader at an 11.36% FCF yield is cheap on cash flow, but returns and margins are falling from a peak, the P/E sits near the top of its own 5-year range, and the Q3 report behind the dip is unread.",
  "rationale": "The dip coincides with an unread Q3 filing and extends a trend of falling ROIC, ROE and margins. The fall removes no obstacle: P/E is still high in its own range as earnings decline. Cash yield and net cash keep conviction at 3, not lower, but good-not-compelling is an AVOID. No position.",
  "price_at_decision": 37.18,
  "price_date": "2026-10-26",
  "research_note": "research/SHE-000651/2026-10-27.md",
  "triggers": [
    {"text": "TTM gross margin falls below 27%, under every year since FY2022, showing AC pricing power is eroding.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 27}},
    {"text": "TTM operating margin falls below 15%, reversing most of the five-year expansion from 11.7%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROE falls below 15%, confirming the post-FY2024 profitability decline is structural rather than a dip.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 51.99, "basis": "Q3 shows only a mild dip and the price implies a far worse -15.6% revenue fall than occurs, so the stock re-rates to the blended base fair value of 51.99 [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 36.86, "basis": "Earnings keep drifting lower (TTM ROIC 34.1% vs 46.8% FY2025 [RA]) and EV/EBITDA holds near its 5y median 4.4x, matching the EV/EBITDA base value of 36.86 [RA]; below the blended base because the DCF leans on a cash surge (FCF conversion 154.0% FY2025 [CF,IS]) that is not repeating."},
    "bear": {"probability": 0.3, "target_price_12m": 26.18, "basis": "Margins keep falling and EV/EBITDA returns toward its 5y low 2.4x [RA], giving the EV/EBITDA bear value of 26.18; above the blended bear of 9.34 because net cash (net debt/EBITDA -2.29x [BS,IS]) and positive FCF make the DCF bear of 0.92 implausible."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the base fair value already sits well above the close, yet ROIC, ROE and margins are falling and the Q3 report behind the dip is unread; a lower price would not change the decision until the earnings trend is visible.",
  "replaces": null,
  "replacement_reason": null
}
```
