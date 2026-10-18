# Evaluation: Industrial Bank Co., Ltd. (SHA:601166) — 2026-10-18
## Bear case
Profitability has fallen every year shown: ROE from 12.7% (FY2021) to 8.2% TTM and net margin from 53.8% to 49.7% [Certain] [RA,IS]. Piotroski F-score is 4 [Certain] [ST]. The trend shows no sign of stopping, and the drivers (NIM compression, property and local-government credit) are sector-wide, so they are not something this bank can fix on its own [Likely]. The fact sheet has no NPL, provisioning or capital-adequacy data, so the cheap P/B of 0.4x cannot be checked against asset quality. The low price may simply reflect unrecognised losses [Likely]. P/E of 5.8x sits at the 81st percentile of its own 5-year range, so it is not cheap against its own history [Certain] [RA]. The mechanical base fair value of 29.60 assumes ROE stabilises, which contradicts the data [Likely]. The macro overlay tilts bear (small): rising US yields lift the model's discount rate [Certain] [macro].
## Bull case
P/B of 0.4x is below its own 5-year minimum and below the 0.5x peer median. P/E of 5.8x is below the 7.1x peer median [Certain] [RA]. The reverse DCF implies -12.4% year-one revenue growth, a deeper decline than a slow ROE fade would produce [Certain] [FV]. Even the mechanical bear fair value of 24.72 is well above the 18.45 close [Certain] [FV]. Net margin near 49.7% is still high, and dilution is minimal: shares rose only 0.20% YoY [Certain] [IS,ST]. Easy PBOC liquidity (DR007 ~1.49%) could help net interest margins stabilise [Likely] [macro]. If ROE stops falling at around 8%, a re-rating toward the 0.5x median P/B is plausible [Guessing].
## Decision
```json
{
  "ticker": "SHA:601166",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A Chinese joint-stock bank trading below its own 5-year minimum P/B, but with ROE and net margin falling every year and no visible asset-quality data, so the discount looks earned rather than mispriced.",
  "rationale": "Cheapness is real, but quality is deteriorating: five years of falling ROE, F-score 4, and no NPL or capital data to underwrite the book value. Mechanical fair value assumes ROE stabilisation the trend contradicts. Rising US yields tilt the model bearish. Good-looking multiples are not compelling evidence, so no position.",
  "price_at_decision": 18.45,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601166/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE rises back above 9.1% (the FY2024 level), showing the five-year profitability decline has reversed; would justify re-research toward a BUY.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 9.1}},
    {"text": "TTM net margin rises above 51.0% (the FY2024 level), showing NIM and credit-cost pressure is easing.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 51.0}},
    {"text": "Company filings disclose a falling non-performing loan ratio for two consecutive reports, giving the asset-quality evidence the fact sheet lacks."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 24.0, "basis": "ROE stabilises near 8.2% TTM [RA] and P/B re-rates toward its 0.5x 5y median [RA], close to the P/B+ROE bear value of 24.00 [FV]; below the mechanical bull because that assumes a recovered ROE."},
    "base": {"probability": 0.5, "target_price_12m": 19.4, "basis": "ROE keeps fading slowly [RA], P/B stays near 0.4x [RA] and book growth plus dividends add modest value; below the mechanical base of 29.60 [FV] because it assumes a sustainable ROE the falling trend does not support; probability trimmed slightly for the small bear macro tilt (research/SHA-601166/2026-10-18-macro.md)."},
    "bear": {"probability": 0.3, "target_price_12m": 15.9, "basis": "Credit costs rise again, earnings fall and P/E reverts to its 5.0x 5y median [RA] on lower profit; weight raised slightly for the small bear macro tilt in research/SHA-601166/2026-10-18-macro.md."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum P/B, and the problem is deteriorating profitability with unverifiable asset quality, so a lower price on the same evidence would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
