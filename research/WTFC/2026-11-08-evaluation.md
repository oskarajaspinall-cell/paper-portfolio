# Evaluation: Wintrust Financial Corporation (WTFC) — 2026-11-08
## Bear case
The quality is already priced. P/B is 1.5x, above its 5y maximum of 1.3x and 21% above peers [RA] [Certain]. The best-fit bank method (P/B + ROE) gives 138.25, below the 151.27 close; the 172.52 base only clears the price because the FCFE DCF is used, and bank FCF is noisy [Likely]. The **Direction change** on FCF margin (falling over 5 fiscal years from 60.7% to 32.7%, yet 57.0% TTM vs 33.5% a year earlier [CF-T]) reflects balance-sheet cash swings, not better economics. It does not threaten the thesis, but it means FCF-based value is not reliable support [Likely]. ROE of 12.9% is decent, not exceptional, for a regional lender exposed to commercial real estate [Guessing]. The macro overlay sees VIX at 28.18 and HY spreads widening +0.77 over 3m; a risk-off move would hit a multiple that has no cushion (research/WTFC/2026-11-08-macro.md) [Likely]. Piotroski F is 4 [ST] [Certain].

## Bull case
Earnings are compounding steadily. ROE rose from 10.8% (FY2021) to 12.9% TTM and net margin from 26.3% to 32.8% [RA, IS] [Certain]. Q3 2026 was a seventh consecutive record quarter, with 8% annualized loan and deposit growth, a stable 3.51% NIM and stable credit (Q3 2026 transcript) [Likely]. Growth is organic, with only 0.62% share growth [ST] [Certain]. P/E of 11.6x sits in line with the peer median of 11.7x and below its own 5y median of 11.8x [RA] [Certain], so earnings growth could carry the price higher without a re-rating. Beta is only 0.86 [ST]. The reverse DCF implies -4.4% revenue growth, which delivered growth contradicts [Likely].

## Decision
```json
{
  "ticker": "WTFC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-run, organically growing Chicago commercial bank with rising ROE trades at a P/B above its own 5-year maximum, so steady compounding is fairly priced rather than mispriced.",
  "rationale": "Fundamentals are solid and improving, but the best-fit bank valuation (P/B + ROE) sits below the price and the multiple is above its 5-year range, with a small bear tilt from macro. Expected value is only modestly above the price: good but not compelling, so AVOID.",
  "price_at_decision": 151.27,
  "price_date": "2026-11-06",
  "research_note": "research/WTFC/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 10.0%, giving up the five-year improvement from 10.8% and signalling credit costs or margin pressure.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 27.0%, reversing most of the rise from 26.3% to 32.8%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 27}},
    {"text": "Shares outstanding growth YoY exceeds 4.0%, signalling dilution or equity-funded acquisitions.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 4}},
    {"text": "A 10-Q adds a substantive new commercial real estate credit-risk factor, or the reserve build outpaces loan growth for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 193.44, "basis": "ROE keeps rising from 12.9% [RA] with record earnings and loan growth (Q3 2026 transcript), reaching the mechanical bull fair value of 193.44 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 158.0, "basis": "Earnings grow organically and P/E holds near 11.6x, in line with its 5y median 11.8x [RA]; below the mechanical base of 172.52 because that blend leans on an FCFE DCF built on noisy bank FCF, while P/B + ROE gives 138.25 [fact sheet Fair value]; probability cut from an even split for the overlay's small bear tilt (research/WTFC/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 123.22, "basis": "HY spreads widen with CRE stress and P/B retreats from 1.5x toward its 5y range of 1.1x-1.3x [RA], the P/B + ROE bear of 123.22 [fact sheet Fair value]; probability raised for the overlay's small toward-bear tilt (research/WTFC/2026-11-08-macro.md)."}
  },
  "entry_price": 138.02,
  "entry_basis": "valuation file: base 172.52 x 0.8; it also sits near the P/B + ROE base of 138.25, the best-fit bank method.",
  "replaces": null,
  "replacement_reason": null
}
```
