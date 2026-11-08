# Evaluation: Suzuki Motor Corporation (TYO:7269) — 2026-11-08
## Bear case
The last 12 months are going the wrong way. TTM ROIC fell from 12.5% to 11.4%, ROCE from 14.3% to 11.8% (2.8pp below its 2-year high) and operating margin from 10.8% to 9.4% [RA-T, IS-T] [Certain]. The FY2025 peak (ROIC 14.4%) looks like the top of the cycle, and the 5-year "rising" trend is mostly a recovery off FY2022 [Certain]. What drives the fall: India, the profit engine, where buyers now want features over no-frills value (Reuters, 2026-07-20) [Likely], and the government's appeal to save fuel [Likely]. That threatens the margin side of any thesis. India's share of revenue cannot be sized [data unavailable], and the overlay sees no macro tilt [Likely]. Base fair value is only +6.4% above the price, the through-cycle DCF bear is negative, and results land on Nov 10 just after a +8.9% jump. That leaves little margin of safety [Certain].
## Bull case
Suzuki is cheap on earnings and cash: P/E 8.1x sits below its 5-year minimum of 8.2x and 16% below peers, P/FCF is 13.2x against a 23.9x median, and the FCF yield is 7.58% [RA, ST] [Certain]. The balance sheet holds net cash (net debt/EBITDA -0.28x) and Altman Z is 3.10 [Certain]. FCF conversion rose from 12.8% to 77.4% over the fiscal years, so earnings are turning into cash [CF] [Certain]. In India, hybrids are gaining share over EVs, which suits Suzuki's low-cost engineering [Likely] (CNBC, 2026-04-23). A stronger rupee gives a mild translation tailwind (macro overlay) [Likely]. If operating margin holds near 9.4% and multiples revert to their medians, the stock re-rates [Guessing].
## Decision
```json
{
  "ticker": "TYO:7269",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash small-car maker with good but cyclical returns trades at the bottom of its own P/E range, but returns and margins are falling from a FY2025 peak and the price already sits close to base fair value.",
  "rationale": "Cheap on P/E and FCF yield with net cash, but ROIC, ROCE and operating margin are all falling over the last 12 months. India mix risk can't be sized, and base fair value is only modestly above the price, with results due in two days. Good but not compelling: conviction 3, so AVOID.",
  "price_at_decision": 2196.5,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-7269/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8% (9.4% now, 10.8% a year earlier), showing the India pricing and mix squeeze is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 10% (11.4% now), giving up most of the five-year improvement from 8.1%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 3% (4.9% now), showing the cash-conversion step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt/EBITDA on the ratios page rises above 0.5x, meaning the net cash position is lost."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 2830, "basis": "Operating margin recovers toward its FY2025 11.0% [IS] and EV/EBITDA moves toward its 5y max of 5.8x [RA]: about the EV/EBITDA bull fair value of 2,832.97 [fact sheet Fair value]; below the 4,545.20 blended bull, whose through-cycle DCF assumes growth a cyclical automaker has not shown."},
    "base": {"probability": 0.5, "target_price_12m": 2300, "basis": "Margins stabilise near TTM 9.4% [IS-T] and EV/EBITDA holds near 5.2x [RA]: in line with the base fair value of 2,336.51 [fact sheet Fair value] and the 6.5% revenue growth the reverse DCF implies."},
    "bear": {"probability": 0.25, "target_price_12m": 1700, "basis": "The rolling decline in ROCE (14.3% to 11.8%) and operating margin continues on Indian feature-led competition (Reuters 2026-07-20 in the note), taking the price back near its 52-week low of 1,670.00 [HI]; above the mechanical bear of 663.39 because that rests on a negative through-cycle DCF that the net cash balance sheet (-0.28x) [RA] makes implausible."}
  },
  "entry_price": 1869.21,
  "entry_basis": "valuation file: base 2,336.51 x 0.8 (20% margin of safety); at that level the same evidence (cheap earnings, net cash, falling but still double-digit ROIC) would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
