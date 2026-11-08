# Evaluation: GoDaddy Inc. (GDDY) — 2026-11-07
## Bear case
The 10-Q now carries new risk factors saying natural-language AI site and app builders could cut demand and pricing for websites, hosting and domains [Certain]. That is the market's central fear, and the company has now disclosed it. Growth is thin and partly priced in. Q3 total bookings grew 5.7% [company-reported], helped by price increases and partly offset by email customers renewing with fewer seats. Nine-month Core revenue grew only 3.7% [company-reported], so volume may already be stalling [Likely]. TTM ROIC has eased from 31.1% in FY2025 to 28.7% [Certain]. Amortisation roll-off flatters reported earnings but not cash [Certain]. Altman Z of 1.44 reflects thin book equity [Certain]. A securities class action is pending, and we cannot judge its merit [Guessing]. The stock's 12-month change is still -14.1% after a sharp 3-month rebound, so sentiment may turn again [Likely].
## Bull case
The numbers do not show disintermediation. Operating margin rose from 12.1% to 26.1% and FCF margin from 20.4% to 33.7%, with gross margin flat [Certain]. Q3 beat, and the revenue outlook moved to the higher end of its range [Likely]. P/FCF is 8.0x and EV/EBITDA 11.6x, both below their 5-year minimums (10.6x and 15.7x), on a 12.57% FCF yield [Certain]. The reverse DCF implies -7.5% revenue growth in year 1, while bookings are still growing [Likely]. Buybacks cut the share count 7.62% year on year, funded by FCF, while net debt/EBITDA fell from 4.35x to 1.88x [Certain]. Piotroski F is 8 [Certain]. Domain registrations are a sticky installed base with high switching costs [Likely]. If bookings simply hold, buybacks plus a partial re-rating carry the shares well above today's price [Likely].
## Decision
```json
{
  "ticker": "GDDY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A deleveraging, high-ROIC domain and SMB-software franchise with a 33.7% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline that growing bookings and raised guidance do not show.",
  "rationale": "Thesis intact: Q3 beat, margins and cash still rising, valuation still below own-history floors. Newly disclosed AI risk, a Core segment growing only slowly, partly price-led bookings and the class action keep conviction at 4, not 5, so no ADD. The position is already around its conviction size; hold it.",
  "price_at_decision": 114.38,
  "price_date": "2026-11-06",
  "research_note": "research/GDDY/2026-11-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year improvement from 12.5% (FY2021) to 28.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20%, erasing the post-2023 step-up (FY2024 20.4%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 level of 27.6%, showing the cash gains were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Total bookings growth in the 10-Q/earnings release falls below 4% y/y for two consecutive quarters (AI substitution showing in demand), or net debt/EBITDA on the ratios page rises above 3.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 187.26, "basis": "Bookings keep growing and the AI-disruption discount fades, so the price reaches the fact sheet's blended base fair value of 187.26 (DCF 206.35, EV/Revenue 149.08 [IS,CF,RA]); below the mechanical bull of 203.79 because the new AI risk factor (sec.gov 10-Q in the note) caps the re-rating."},
    "base": {"probability": 0.5, "target_price_12m": 149.08, "basis": "Bookings growth holds near the Q3 5.7% [company-reported] and EV/Sales recovers only part of the way to its 5y range (3.5x-6.7x [RA]), matching the EV/Revenue base of 149.08; it sits under the DCF base because the AI overhang keeps the multiple low."},
    "bear": {"probability": 0.25, "target_price_12m": 94.91, "basis": "AI site builders erode Core volumes, which grew only 3.7% over nine months [company-reported], and the market keeps pricing decline (reverse DCF -7.5%), consistent with the DCF bear of 94.91 and the blended bear of 102.86 [IS,CF,RA]."}
  },
  "entry_price": null,
  "entry_basis": "Already conviction 4 and held at about its conviction size; price is not what stops an ADD. Conviction 5 needs evidence that bookings and Core volumes are resilient to AI site builders, and a lower price would not change that.",
  "replaces": null,
  "replacement_reason": null
}
```
