# Evaluation: Rightmove plc (LON:RMV) — 2026-10-19
## Bear case
The return profile is exceptional but slowly eroding: operating margin fell from 73.4% to 66.7%, net margin from 60.1% to 49.7% and FCF margin from 63.7% to 54.3% over five years [IS,CF] [Certain], and ROIC drifted down 35.3pp [RA] [Certain]. That shows a business spending more to defend its position, not one with spare pricing power [Likely]. The cheap multiples largely reflect that de-rating: EV/EBITDA and P/FCF sit below their 5y minimums [RA] [Certain], but the 5y range includes frothier years, and a 6.09% FCF yield [ST] is a fair price for mid-single-digit growth, not a deep discount [Likely]. Competition from better-funded portals (CoStar, a listed peer) and AI-led property search could pressure agent fees [Guessing]. The shares are up 18.8% in three months with RSI at 69.7 [HI,ST], partly on unconfirmed takeover rumours [Guessing]. There is no mechanical fair value to check the price against [data unavailable] [Certain].
## Bull case
Rightmove is the UK's dominant two-sided property marketplace: 100% gross margin, ROIC of 497.4% and FCF conversion above 100% of net income every year [IS,RA,CF] [Certain]. Revenue grew 7% in H1 2026 with EPS up 6% (stockanalysis.com transcript listing) [Likely], yet P/E sits at the 4th percentile of its 5y range and P/E, EV/EBITDA and P/FCF are 27-32% below peers [RA] [Certain]. Net cash (net debt/EBITDA -0.10x [BS,IS]) and a 2.63% annual share-count reduction [ST] [Certain] give a cash return that compounds with growth [Likely]. Subscription revenue is insulated from transaction volumes and rates (macro overlay, context weight) [Likely]. A confirmed bid would put a floor under the price [Guessing].
## Decision
```json
{
  "ticker": "LON:RMV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A dominant, net-cash UK property portal with exceptional returns trades below its own 5-year minimum EV/EBITDA and P/FCF, but five years of steady margin and ROIC erosion and a 6.09% FCF yield make it fairly priced rather than mispriced.",
  "rationale": "Quality is outstanding, but margins and ROIC are falling steadily, the FCF yield is modest against the portfolio's bar, no mechanical fair value can be computed, and the three-month rebound partly prices unconfirmed takeover talk. Good but not compelling: conviction 3, so AVOID with a watch price.",
  "price_at_decision": 541.40,
  "price_date": "2026-10-16",
  "research_note": "research/LON-RMV/2026-10-19.md",
  "triggers": [
    {"text": "TTM operating margin falls below 60%, from 66.7%, showing the investment-led margin drift has become a break in pricing power.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 60}},
    {"text": "TTM FCF margin falls below 50%, under the FY2024 five-year low of 53.9%, showing cash generation is eroding faster than the trend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 50}},
    {"text": "TTM ROIC falls below 400%, from 497.4%, a step down in the durability of returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 400}},
    {"text": "Shares outstanding rise year on year, reversing the -2.63% buyback-driven decline.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 662, "basis": "P/E re-rates to its 5y median of 23.1x [RA] on TTM EPS as H1 2026 revenue growth of 7% (transcript listing [OV]) persists; no mechanical fair value exists to cross-check [data unavailable]."},
    "base": {"probability": 0.5, "target_price_12m": 574, "basis": "P/E holds near 18.9x [RA] while EPS grows roughly in line with the 6% H1 2026 increase (transcript listing [OV]) helped by the -2.63% share-count decline [ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 457, "basis": "Takeover-rumour premium (2026-10-08 headline [OV]) unwinds and continued margin erosion (operating margin down 5.7pp over five years [IS]) takes the price back to its 200-day average of 457.20 [ST], with P/E below its 5y minimum of 18.2x [RA]."}
  },
  "entry_price": 457.20,
  "entry_basis": "No base fair value is computable [data unavailable], so the anchor is the 200-day average of 457.20 [ST]: there P/E would sit below its 5y minimum of 18.2x [RA] and the FCF yield would be high enough to compensate for the margin drift.",
  "replaces": null,
  "replacement_reason": null
}
```
