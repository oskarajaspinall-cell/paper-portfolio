# Evaluation: Best Buy Co., Inc. (BBY) — 2026-10-09
## Bear case
Returns are in structural decline: ROIC fell from 68.4% (FY22) to 26.0% TTM and operating margin from 5.8% to 4.3% [Certain]. At $88.40 the stock sits 6% above base fair value of $83.12, with bull only $96.97 against a $33.62 bear [Certain], so the risk-reward is skewed the wrong way. P/FCF at the 8th percentile of its range is flattered by 139% FCF conversion against 54-63% in FY23-FY24 [Likely]. The computing strength comes from higher prices (memory inflation) on falling units, not demand [Likely]. Tariff refunds are a one-off [Certain]. Short interest is 8.12% and rose 13.7% [Certain]. Real yields are up 0.61pp in 3 months ahead of a financing-dependent holiday quarter (macro overlay) [Likely]. P/E sits mid-range at 14.7x, so it is not cheap on its own history [Certain].
## Bull case
FY27 guidance was raised after Q2: comps grew 4.1% and EPS rose 15% [Certain]. ROIC has held at 23-26% for three years and gross margin has stayed flat at around 22.5%, so the decline may have bottomed [Likely]. Marketplace and Best Buy Ads are higher-margin mix levers that could lift operating margin [Likely]. Leverage is low at 0.66x net debt/EBITDA, the FCF yield is 9.54% and the share count is shrinking 1.1% a year [Certain]. The reverse DCF implies only 0.4% revenue growth [Certain]. The 50-day average is 19.3% above the 200-day average, so the trend is firm [Certain]. Even so, the upside to bull fair value is under 10% [Certain].
## Decision
```json
{
  "ticker": "BBY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-leverage, cash-generative but low-moat electronics retailer with eroding returns trades 6% above its base fair value, leaving under 10% upside to bull against a large downside tail.",
  "rationale": "Execution is solid and guidance was raised, but returns and margins are lower than five years ago. The price already sits above base fair value with bull only 9.7% higher. FCF cheapness rests on unusually high conversion, and rising real yields lean against the holiday quarter. This is a good business but not a compelling buy, so conviction is 3: AVOID.",
  "price_at_decision": 88.40,
  "price_date": "2026-10-08",
  "research_note": "research/BBY/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC rises above 35.2% (the FY2023 level), showing the five-year returns decline has reversed via mix (marketplace/ads).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 35.2}},
    {"text": "TTM operating margin rises above 5.8% (the FY2022 level), evidencing marketplace and ads are a real margin driver.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 5.8}},
    {"text": "TTM FCF margin holds above 4.9% (the FY2022 level), showing cash conversion is structural rather than working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 4.9}},
    {"text": "Comparable sales stay positive in the next two quarterly reports while gross margin holds at or above 22.5% despite memory cost inflation."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 96.97, "basis": "Raised FY27 guidance plus marketplace/ads mix lift margins toward the fact sheet's bull fair value 96.97 [IS,RA]; probability trimmed for the macro overlay's moderate bear tilt on real yields (research/BBY/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 83.12, "basis": "Flat 22.6% gross and 4.3% operating margins [IS] converge the price to base fair value 83.12, consistent with EV/EBITDA near its 5y median 7.3x [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 68.3, "basis": "Weak holiday comps and normalising FCF conversion (54-63% in FY23-FY24 [CF,IS]) push the price to the EV/EBITDA bear value 68.30, not the DCF-driven 33.62 blend, which assumes an implausible collapse for a 0.66x-levered retailer [BS,IS]; probability raised for the macro overlay's moderate bear tilt (research/BBY/2026-10-09-macro.md)."}
  },
  "entry_price": 66.5,
  "entry_basis": "valuation file: base 83.12 x 0.8 = 66.50; at that level the asymmetry turns favourable on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```
