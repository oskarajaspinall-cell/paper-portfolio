# Evaluation: GoDaddy Inc. (GDDY) — 2026-10-07
## Bear case
Several securities class actions have been filed [Certain] alleging an undisclosed promotional discount hurt total-bookings growth; their merit is unproven [Guessing]. If true, part of the margin and FCF step-up was flattered and new-customer economics are weaker than reported [Guessing]. Short interest rose 43.9% month-on-month to 6.19% of float [Certain], and the shares are down 28.5% over 12 months, 45.0pp behind SPY [Certain]: the market is pricing a demand problem, not just a legal one [Likely]. AI coding and site-building tools may commoditise hosting and website builders, leaving GoDaddy with renewal pricing power only [Guessing]. Book equity is near zero (P/B 1,855.9x) and Altman Z is 1.63 [Certain], so a cash-flow shock would meet a thin cushion [Likely]. Q3 results on Oct 29, 2026 could confirm a slowdown [Likely].

## Bull case
ROIC has risen from 12.5% to 37.3% TTM and operating margin from 12.1% to 25.2% over five years, with a stable ~64% gross margin [Certain]. FCF margin is 33.4% TTM [Certain]. Yet EV/EBITDA (10.9x), EV/Sales (3.0x) and P/FCF (7.3x) sit below their own 5-year minimums, and the FCF yield is 13.70% [Certain]. Net debt/EBITDA fell from 4.35x to 1.91x while 6.24% of shares were retired in a year [Certain], so the per-share compounding is funded by cash flow, not leverage [Certain]. The last reported quarter showed 6% bookings growth, so the allegations are not yet visible in the numbers [Certain]. Domains and business email are sticky renewals [Likely]. Even with zero re-rating, the FCF yield plus buybacks gives a double-digit return [Likely]. A reported Gen Digital approach suggests strategic buyers see the value too [Guessing].

## Decision
```json
{
  "ticker": "GDDY",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A deleveraging, 37%-ROIC, 33%-FCF-margin domain and SMB-software franchise trades below its own 5-year minimum EV/EBITDA and P/FCF at a 13.7% FCF yield, pricing a litigation-driven bookings scare that its reported numbers do not yet show.",
  "rationale": "Valuation is the cheapest in five years while returns, margins and leverage are all improving; the FCF yield and buybacks give returns without a re-rating. The unproven bookings allegations, rising short interest and Q3 results in three weeks hold conviction at 4, not 5: standard 7% core size. Technology exposure and cash allow it.",
  "price_at_decision": 98.18,
  "price_date": "2026-10-06",
  "research_note": "research/GDDY/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year improvement from 12.5% to 37.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20%, erasing the post-2023 step-up (FY2024 20.4%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below the FY2024 level of 27.6%, showing the cash-generation gains were promotional or transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 27.6}},
    {"text": "Total bookings growth in the SEC 8-K earnings release falls below 4% y/y for two consecutive quarters, showing the promotional-discount allegations reflect a real demand problem."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 142, "basis": "Bookings hold near the 6% Q2 growth and the litigation fades, so P/FCF re-rates from 7.3x to its 5-year minimum of 10.6x [RA] on TTM FCF [CF]."},
    "base": {"probability": 0.5, "target_price_12m": 115, "basis": "Litigation lingers but fundamentals stay intact; the 13.70% FCF yield [ST] and 6.24% annual share retirement [ST] lift per-share value with only a partial re-rating toward the 10.6x P/FCF floor [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 73, "basis": "Q3 results confirm the alleged bookings slowdown (note, Unusual items) and P/E compresses from 14.6x to its 5-year minimum of 10.9x [RA] on TTM earnings [IS]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
