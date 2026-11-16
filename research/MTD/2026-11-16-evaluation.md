# Evaluation: Mettler-Toledo International (MTD) — 2026-11-16
## Bear case
The price is extended: +28.6% above the 200-day average after +69.6% in six months, RSI 64.1 [Certain]. Q3 sales grew only 6% and 2027 guidance calls for ~5% local-currency growth [Likely], while the reverse DCF implies 32.2% year-1 revenue growth [Certain]. If growth slows the multiple de-rates; P/E 37.7x against a 5y median of 33.3x leaves room to fall with earnings unchanged [Certain]. EV/EBITDA 29.2x is 19% above peers [Certain]. FCF margin is 1.8pp lower year on year and 2.9pp below its 2-year high, ROCE 7.0pp below its high, and nine-month results carry a one-time tariff-refund gain, so underlying margins are softer than reported [Likely]. New Section 301 tariffs (12.5% on Switzerland and China) [company-reported] and a China segment near 17.6% of sales add demand and cost risk [Likely]. Rising real yields (10y TIPS 2.86%, macro overlay) press the multiple [Likely].

## Bull case
A franchise with ROIC of 46.6% TTM, never below 40.9% in five fiscal years, a 59.2% gross margin and net debt/EBITDA of 1.58x [Certain]. Rolling ROIC rose from 39.2% to 46.6% in a year, so returns are improving, not fading [Certain]. The installed base, service tail (service $817.2m of $3,068.7m nine-month sales [company-reported]) and regulated-workflow switching costs make returns durable [Likely]. Q3 growth of 6% with China +13% locally and raised guidance show the business is working; the Investor Day targets 6%+ sales growth and mid-teens adjusted EPS growth [Likely]. Buybacks cut shares 2.84% a year [Certain]. P/E sits at only 37% of its own 5y range and in line with peers (37.5x) [Certain]. The FCF-margin dip is explained by tariff costs and working capital, not lost share [Likely]. The mechanical fair value is flagged unreliable (methods disagree 3.1x) and is weighed lightly [Certain].

## Decision
```json
{
  "ticker": "MTD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "FCF margin (-1.8pp TTM) and 3-year operating margin/ROCE drift reflect new Section 301 tariff costs and working capital [company-reported, https://www.sec.gov/Archives/edgar/data/1037646/000103764626000074/mtd-20260930.htm], while rolling ROIC rose to 46.6% [RA-T], Q3 sales grew 6% and guidance was raised (https://stockanalysis.com/stocks/mtd/transcripts/721311-q3-2026/): no share loss.", "moat": "wide", "key_risk": "medium", "key_risk_text": "De-rating of an extended price: P/E 37.7x against a 5y median of 33.3x [RA], +28.6% above the 200-day average [ST,HI], if ~5% 2027 growth disappoints or real yields keep rising.", "veto": null},
  "thesis": "A wide-moat precision-instrument franchise with 46.6% ROIC and improving rolling returns, in a strong uptrend, but priced at a premium to peers that leaves the return dependent on the multiple holding.",
  "rationale": "Scorecard conviction 3: elite returns, a wide moat and trend strength are offset by falling FCF and operating margins, moderate leverage and a premium multiple whose de-rating is the key threat. Good but not compelling at this price, so no position; cash is acceptable.",
  "price_at_decision": 1738.91,
  "price_date": "2026-11-13",
  "research_note": "research/MTD/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 38%, under the rolling level of 39.2% a year earlier, showing returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 38}},
    {"text": "TTM operating margin falls below 26%, under the five-year low of 27.1%, showing tariffs or pricing are compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM FCF margin falls below 17%, under the five-year low of 18.8%, showing cash conversion is breaking down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 17}},
    {"text": "Chinese Operations segment sales in the 10-Q decline year on year for two consecutive quarters [company-reported]."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1948, "basis": "P/E holds at 37.7x [RA] on adjusted EPS growth at the top of the 10%-12% 2027 guidance (https://stockanalysis.com/stocks/mtd/transcripts/721311-q3-2026/)."},
    "base": {"probability": 0.45, "target_price_12m": 1689, "basis": "EPS grows about 10% per 2027 guidance while P/E reverts to its 5y median 33.3x [RA]; well above the unreliable mechanical base 810.08, whose methods disagree 3.1x, because the EV/Revenue method (base 1,480.01) better reflects a franchise that the DCF on 5-6% growth undervalues."},
    "bear": {"probability": 0.30, "target_price_12m": 1379, "basis": "Growth slows and P/E de-rates to its 5y low 29.9x [RA] on flat EPS; probability raised a little for the macro overlay's small tilt toward bear (real yields pressing the multiple, research/MTD/2026-11-16-macro.md)."}
  },
  "entry_price": 1379,
  "entry_basis": "P/E back at its 5y low of 29.9x [RA] on TTM EPS, where a real discount to own history would replace reliance on trend strength; the mechanical base fair value is flagged unreliable, so the default base x 0.8 is not used.",
  "replaces": null,
  "replacement_reason": null
}
```
