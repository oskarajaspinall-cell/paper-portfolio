# Evaluation: 3SBio Inc. (HKG:1530) — 2026-10-11
## Bear case
The "cheapness" rests on one unexplained year. FY2025 ROIC jumped from 14.0% to 63.0%, operating margin from 28.7% to 59.3% and gross margin to 92.4% against a stable FY2021-24 base [Certain] [RA, IS]; no allowlisted source explains the driver [Certain], and biosimilar franchises like TPIAO/EPIAO do not structurally earn 90%+ gross margins [Likely]. If the item is non-recurring, TTM EPS roughly halves back toward the FY2024 net margin of 23.0% [Likely], and a 4.0x P/E becomes about 8x, its 5y median: not cheap. The market agrees: -51.3% over 12 months, 50-day 18.2% below the 200-day [Certain] [ST, HI]. The fair value (base 25.52 HKD) is EV/Revenue on the same possibly inflated TTM revenue, so it inherits the error [Likely]. Shares rose 2.48% y/y: dilution, not buybacks [Certain] [ST].
## Bull case
Even if the step-change partly reverses, the balance sheet is clean: net cash (net debt/EBITDA -1.42x), Altman Z 10.01, Piotroski F 7 [Certain] [RA, ST]. FCF conversion is 109.2% TTM, so the profit surge is backed by cash, not accruals [Certain] [CF, IS]. P/B is 1.1x against peers' 4.7x [Certain] [RA], and every earnings multiple sits below its own 5y minimum [Certain]. If the higher-margin revenue proves recurring, a 27.75% FCF yield [Certain] [ST] is mispriced and even the fair value's bear case (20.50 HKD, +36%) is upside [Likely]. Results due 2026-11-11 [Certain] [ST] could resolve the question either way [Guessing].
## Decision
```json
{
  "ticker": "HKG:1530",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash Chinese biologics maker looks optically cheap at 4.0x P/E, but the cheapness depends on an unexplained FY2025 margin and ROIC step-change that may well be non-recurring.",
  "rationale": "The whole valuation case rests on an unexplained FY2025 margin surge. If it is one-off, normalised earnings put the stock near its 5y median P/E, not below its minimum. The fair value inherits the same inflated revenue. The balance sheet limits the downside, but this is not high conviction. AVOID, and wait for the next results to explain the driver.",
  "price_at_decision": 15.07,
  "price_date": "2026-10-09",
  "research_note": "research/HKG-1530/2026-10-11.md",
  "triggers": [
    {"text": "A company filing or results release on the stockanalysis.com filings index identifies the FY2025 margin driver as recurring product or royalty income, which would reopen a core initiation.", "check": null},
    {"text": "TTM gross margin falls below 88%, confirming the FY2025 margin surge was non-recurring and the AVOID is right.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 88}},
    {"text": "TTM ROIC falls below 20%, showing the step-change in returns did not persist.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 20.50, "basis": "The margin driver proves recurring and the stock re-rates to the fact sheet's EV/Revenue bear fair value of 20.50 HKD [IS,BS,RA,ST], still below base because that model's TTM revenue remains unverified."},
    "base": {"probability": 0.45, "target_price_12m": 15.26, "basis": "TTM EPS roughly halves as net margin falls from 46.3% back toward FY2024's 23.0% [IS], and P/E returns to its 5y median 8.1x [RA] (15.07 x 8.1/4.0 x 0.5); this is below the mechanical fair value because that model assumes the inflated TTM revenue persists."},
    "bear": {"probability": 0.30, "target_price_12m": 12.06, "basis": "Earnings halve as the step-change reverses and the downtrend (-51.3% 12m, 50-day 18.2% below the 200-day [ST,HI]) holds P/E at its 5y minimum 6.4x [RA] (15.07 x 6.4/4.0 x 0.5)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
