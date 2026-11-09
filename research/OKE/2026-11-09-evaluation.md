# Evaluation: ONEOK, Inc. (OKE) — 2026-11-09
## Bear case
Cash, not EBITDA, is what common holders get, and it is deteriorating: FCF margin fell from 9.3% to 5.9% over 12 months and FCF conversion is 62.2% vs 94.5% in FY24 [Certain]. Operating margin dropped from 18.0% to 14.2%, 8.6pp below its 2-year high, partly on higher operating costs the 10-Q cites [company-reported] [Likely]; if costs, not timing, drive it, the decline is structural. P/FCF of 21.2x sits above its 5y maximum, so the stock is cheap only on EBITDA, and P/E is flattered by a one-off tax benefit [Certain]. Apollo's $9 billion Class B ranks ahead of common cash flows [company-reported] [Certain], shares rose 2.75% YoY and Altman Z is 1.65 [Certain]. The Middle East refined-products tailwind may fade [Likely], and Brazos integration risk is untested [Guessing]. The mechanical bear of 77.94 is below the price [Certain].
## Bull case
The direction change looks explained, not structural. Returns on capital did not fall: TTM ROIC rose 0.9pp to 8.8%, its 2-year high, and ROCE is flat [Certain], which is hard to square with a broken model. The cash gap is attributed to unfractionated NGL inventory build and continuing growth capex (Permian plants, NGL expansion) [company-reported] [Likely]: working capital and investment, both temporary. The franchise is about 90% fee-based [company-reported] [Likely]; Q3 volumes rose and 2026 guidance was raised again [Likely]. The balance sheet is improving: net debt/EBITDA fell from 5.29x (FY24) to 3.68x and S&P and Fitch upgraded to BBB+ [company-reported] [Certain]. Yet EV/EBITDA of 10.7x is at its 5y minimum and 19% below peers; the reverse DCF needs only 3.3% year-1 revenue growth; base fair value is 101.12 [Certain]. Macro is context only (research/OKE/2026-11-08-macro.md).
## Decision
```json
{
  "ticker": "OKE",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A fee-based US midstream network with ROIC at its 2-year high, falling leverage and a twice-raised 2026 guide trades at its 5-year minimum EV/EBITDA and below peers, while the margin and FCF dip is explained by inventory build and growth capex rather than a structural decline.",
  "rationale": "The rolling-12-month fall is a cash-timing and investment effect: ROIC rose, leverage fell and ratings improved. EBITDA-based cheapness against own history and peers gives a positive skew. Conviction capped at 4, standard size, because FCF conversion is weak, Apollo Class B ranks ahead of common and the mechanical bear sits below the price.",
  "price_at_decision": 85.19,
  "price_date": "2026-11-06",
  "research_note": "research/OKE/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12% (14.2% now), showing the cost increases are structural rather than an inventory and timing effect.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 7% (8.8% now), showing the growth capex and Brazos are not earning their cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA rises above 4.5x (3.68x now) once Brazos is in the numbers, reversing the deleveraging behind the BBB+ upgrade.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "TTM FCF conversion (FCF/NI, cash-flow and income-statement pages) falls below 50% (62.2% now), meaning the NGL inventory build is not reversing into cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 112.0, "basis": "Inventory build reverses and Brazos lifts EBITDA so EV/EBITDA re-rates from its 5y minimum 10.7x toward its 5y median 12.6x [RA]; far below the mechanical bull of 381.97, which the note rejects as not credible."},
    "base": {"probability": 0.5, "target_price_12m": 98.0, "basis": "Raised 2026 guidance is delivered (Q3 release, https://www.globenewswire.com/news-release/2026/10/27/3389643/0/en/oneok-announces-higher-third-quarter-2026-earnings-and-increases-2026-financial-guidance.html) with a partial multiple recovery; slightly below the mechanical base of 101.12 because FCF conversion of 62.2% [CF,IS] and the Apollo Class B ahead of common argue against full DCF credit."},
    "bear": {"probability": 0.25, "target_price_12m": 76.0, "basis": "Operating margin keeps falling from 14.2% [IS-T] on structural cost increases and FCF stays weak, so the stock trades near the mechanical bear of 77.94 [fact sheet Fair value]; macro is context only and does not shift the odds (research/OKE/2026-11-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
