# Evaluation: Gilead Sciences, Inc. (GILD) — 2026-10-11
## Bear case
The price already discounts success. The last close of 151.17 sits on the DCF base fair value of 151.99, and bull is only 153.46, against a bear of 76.71 [Certain] (fact sheet, Fair value). EV/EBITDA of 14.3x and EV/Sales of 6.9x are above their 5-year maxima of 11.4x and 5.7x [Certain] (RA). The 12-month rise of +27.8% has re-rated the stock rather than its earnings, and operating margin has fallen 3.6pp over five years to 38.9% [Certain] (IS). Revenue still depends on Biktarvy/Descovy, which face eventual generics and pricing pressure. The roughly $13bn of IPR&D charges in H1 2026 shows that growth is being bought, and those deals may not pay back [Likely] (10-Q). Earnings on Oct 29 add event risk to a stock trading near its 52-week high of 157.29 [Certain] (HI).
## Bull case
Returns are improving: ROIC is 34.4% TTM (+6.2pp over five years), ROCE is 30.9% and gross margin is steady near 79-80% [Certain] (RA, IS). The FCF margin of 42.5% supports a 6.91% FCF yield, and P/FCF of 14.5x is 31% below the peer median of 20.9x and mid-range of its own history [Certain] (RA, ST). Lenacapavir (Yeztugo) extends the HIV franchise into long-acting prevention, and access deals widen its reach [Likely] (Business Wire, 2026-09-16). The negative TTM net margin comes from one-off IPR&D charges, not from operations [Certain] (10-Q). Buybacks cut the share count by 1.39% YoY, and net debt/EBITDA stays moderate at 1.46x [Certain] (ST, BS). Beta of 0.33 makes this a defensive compounder [Certain] (ST).
## Decision
```json
{
  "ticker": "GILD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 34%-ROIC, 42%-FCF-margin HIV franchise extending its cycle with lenacapavir, but the price already equals the DCF base fair value with EV/EBITDA above its 5-year maximum, leaving no margin of safety.",
  "rationale": "The business is high quality, but the valuation is full. The price is at base fair value (+0.5%) with only +1.5% to the bull case and -49% to the bear case, and EV/EBITDA and EV/Sales are above their 5-year maxima. Good but not compelling, so no position; cash is acceptable. Re-examine nearer 122.",
  "price_at_decision": 151.17,
  "price_date": "2026-10-09",
  "research_note": "research/GILD/2026-10-11.md",
  "triggers": [
    {"text": "TTM gross margin falls below 75% (vs a 78.0%-79.8% five-year range), signalling HIV pricing or competitive erosion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 75}},
    {"text": "TTM ROIC falls below 20%, reverting to the FY2023 level of 19.0% and reversing the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 34%, under the FY2023 five-year low of 34.4%, showing business-development spending is diluting core profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 34}},
    {"text": "Combined Biktarvy + Descovy product revenue (earnings release / 10-Q) declines YoY for two consecutive quarters before lenacapavir offsets it."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 168, "basis": "P/FCF re-rates from 14.5x to its 5y max of 16.1x [RA] on TTM FCF [CF] as Yeztugo uptake and the oncology pipeline land; this is above the DCF bull of 153.46 because the mechanical model does not capture launch-driven growth."},
    "base": {"probability": 0.5, "target_price_12m": 150, "basis": "The price holds near the DCF base fair value of 151.99 (fact sheet), with the reverse DCF's implied 2.3% growth delivered and no further re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 117, "basis": "EV/EBITDA mean-reverts from 14.3x to its 5y max of 11.4x [RA] on TTM EBITDA with 1.46x net debt [BS,IS], near the 52-week low of 114.02 [HI]; this is less severe than the DCF bear of 76.71, which assumes a franchise collapse the ROIC trend does not show."}
  },
  "entry_price": 121.59,
  "entry_basis": "Valuation file: base 151.99 x 0.8 (20% margin of safety); at that level EV/EBITDA would also be back near its 5y range [RA].",
  "replaces": null,
  "replacement_reason": null
}
```
