# Evaluation: The Progressive Corporation (PGR) — 2026-10-07
## Bear case
The low multiples are low against peak earnings. TTM ROE of 34.9% sits near a cyclical high after the FY2022 trough of 4.2% [Certain]. Management itself describes a soft market, with more carriers taking on risk, and is cutting rates in 16 states [Likely]. August operating results reportedly missed on the core loss ratio [Guessing]. If ROE mean-reverts, today's 10.7x P/E is not cheap. At 3.6x P/B, a 106% premium to the peer median of 1.7x, the stock has room to de-rate toward book [Certain]. FCF conversion is falling, from 174.9% in FY2024 to 136.4% TTM [Certain]. Buybacks are negligible, with shares down only 0.14% YoY [Certain], so capital return will not cushion an earnings decline. Q3 results on Oct 14 could confirm the margin squeeze [Likely].

## Bull case
This is a best-in-class underwriter with ROIC that rose from 15.4% to 32.9% between FY21 and FY25, and net debt/EBITDA falling to 0.54x [Certain]. Its scale, pricing data and low-cost direct model let it capture most of the 2025 growth in industry auto premiums [Likely]. P/E 10.7x, EV/EBITDA 8.5x and P/FCF 7.7x all sit below their 5-year minimums, at a 12.94% FCF yield [Certain]. The shares are 13.7% lower over 12 months and 30.1pp behind SPY, so some soft-market risk is already priced [Likely]. The property turnaround is largely complete [Likely]. Per the macro overlay, rising real yields with flat breakevens lift float income without matching claims inflation [Likely]. A beta of 0.23 diversifies the portfolio [Certain].

## Decision
```json
{
  "ticker": "PGR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A top-quality personal-auto underwriter looks cheap against its own history, but the low multiples rest on cycle-peak ROE while management flags a softening market, so the valuation is not a clear margin of safety.",
  "rationale": "Quality is excellent but the cheapness is on near-peak underwriting earnings, and the shares still carry a 106% P/B premium to peers. The soft-market pricing and the reported August loss-ratio miss point to margin normalisation. Q3 results are due Oct 14. Good but not compelling: conviction 3, below the buy threshold, so AVOID.",
  "price_at_decision": 212.05,
  "price_date": "2026-10-06",
  "research_note": "research/PGR/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROE falls below 20%, confirming that the FY2022-style underwriting downturn is recurring.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 2x, signalling balance-sheet or reserve deterioration.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2}},
    {"text": "Personal Lines policies-in-force growth stays positive while the property combined ratio holds below 90% in quarterly shareholder letters, which would show the growth edge survives the soft market."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 242, "basis": "ROE holds near the TTM 34.9% [RA] and EV/Sales re-rates from 1.4x toward its 5y median 1.6x [RA]; the probability is raised slightly for the small toward-bull real-yield float-income tilt in research/PGR/2026-10-07-macro.md."},
    "base": {"probability": 0.45, "target_price_12m": 212, "basis": "The P/E stays at 10.7x [RA] on roughly flat TTM earnings, as soft-market rate cuts flagged on the Q2 2026 call (stockanalysis.com/stocks/pgr/transcripts/650481-q2-2026/) offset growth in policies in force."},
    "bear": {"probability": 0.30, "target_price_12m": 194, "basis": "ROE normalises from the cycle-high 34.9% [RA] and P/B de-rates from 3.6x to its 5y minimum of 3.3x [RA], near the 52-week low of 189.20 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
