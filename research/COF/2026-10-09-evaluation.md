# Evaluation: Capital One Financial Corporation (COF) — 2026-10-09
## Bear case
Profitability has collapsed: ROE fell from 20.4% (FY2021) to 2.4% (FY2025), net margin from 38.3% to 7.5% [Certain] [RA, IS]. Shares outstanding rose 52.31% YoY on the Discover deal, and accretion is not yet visible in returns [Certain] [ST]. Piotroski F-Score is 4 [Certain] [ST]. The headline cheapness (P/FCF 4.1x, FCF yield 24.28%) is a lender cash-flow artefact, not normalized cash generation [Likely]. On earnings, P/E 12.8x is a 20% premium to peers [Certain] [RA]. The fair-value base of 216.68 is only 8.7% above the 199.40 close, and the bear case is 62.61 [Certain]. Higher-for-longer rates and a widening HY spread lean against card credit (overlay: tilt toward bear, small) [Likely]. Political and regulatory exposure (AML review of Trump-linked accounts, fighting the administration) adds a binary tail risk for a supervised bank [Likely] (Reuters, fact sheet news).

## Bull case
TTM ROE has already rebounded to 9.0% and net margin to 21.9% from the FY2025 trough, consistent with one-off deal accounting rather than structural decline [Likely] [RA, IS]. Management says the Discover integration is on track with stable delinquencies, and owning a payments network is a structural advantage no card peer has [Likely] (Barclays transcript [OV]). P/B 1.2x is 19% below the peer median of 1.5x [Certain] [RA]. The reverse DCF implies only 0.5% growth [Certain]. Short interest is a low 1.63% and falling [Certain] [ST]. If ROE normalizes toward the FY2022 13.0%, the P/E-method bull value of 247.83 is reachable [Guessing]. Q3 results on Oct 20, 2026 could show the synergies arriving [Guessing].

## Decision
```json
{
  "ticker": "COF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A post-Discover card lender and network owner whose earnings power is still normalizing trades only 8.7% below its base fair value, too thin a margin for unproven merger accretion, macro credit headwinds and a live political/regulatory dispute.",
  "rationale": "Returns are recovering but unproven. ROE is 9.0% TTM against 20.4% in FY2021, and dilution from a 52.31% rise in share count is not yet earned back. The P/FCF cheapness is a lender artefact, and P/E sits at a premium to peers. With only 8.7% base upside, a small adverse macro tilt and binary regulatory risk, this is good but not compelling. No position.",
  "price_at_decision": 199.40,
  "price_date": "2026-10-08",
  "research_note": "research/COF/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 13.0% (the FY2022 level), showing Discover accretion is real and earnings power is normalizing. That would raise conviction.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13.0}},
    {"text": "TTM net margin falls below 17.3% (the FY2024 level), showing provisions or integration costs are reversing the TTM recovery.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 17.3}},
    {"text": "TTM ROE falls back below 8.0% (the FY2024 level), confirming the post-merger collapse in returns is structural.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8.0}},
    {"text": "Piotroski F-Score (statistics page) falls to 3 or below, signalling broad deterioration in profitability, leverage or efficiency."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 247.83, "basis": "ROE recovers toward the FY2022 13.0% [RA] as Discover synergies arrive (Barclays transcript [OV]), supporting the P/E-method bull value of 247.83 rather than the FCFE bull of 416.78, which capitalizes lender FCF that the note shows is distorted."},
    "base": {"probability": 0.45, "target_price_12m": 216.68, "basis": "Gradual normalization from the 9.0% TTM ROE [RA] converges on the fact sheet's FCFE/DCF base fair value of 216.68, consistent with the reverse DCF's implied 0.5% growth."},
    "bear": {"probability": 0.30, "target_price_12m": 166.17, "basis": "Rising card credit losses and the political/regulatory overhang (Reuters, fact sheet news) push P/B back to its 5y median of 1.0x from 1.2x [RA]. The probability is raised from 0.25 for the overlay's small tilt toward bear (research/COF/2026-10-09-macro.md). A P/B floor is used instead of the 62.61 FCFE bear, which extrapolates distorted lender FCF."}
  },
  "entry_price": 173.34,
  "entry_basis": "valuation file: base 216.68 x 0.8. At that price the 20% margin of safety would offset the unproven merger accretion and macro credit risk.",
  "replaces": null,
  "replacement_reason": null
}
```
