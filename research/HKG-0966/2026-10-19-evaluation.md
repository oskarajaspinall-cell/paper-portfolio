# Evaluation: China Taiping Insurance Holdings Company Limited (HKG:0966) — 2026-10-19
## Bear case
The headline cheapness comes from peak earnings. ROE jumped from 10.0% (FY2024) to 28.9% TTM almost entirely in FY2025/TTM, which coincides with the China/HK equity rally. That makes it [Likely] investment gains on the float, not better underwriting. P/E at 2.0x sits below its 5y minimum, while P/B at 0.4x is near the top of its own 5y range [Certain]. On book value the stock is not cheap against its own history. Base fair value of HKD 18.81 is only 7.7% above the close, and the bear value is 12.36 [Certain]. The macro overlay tilts moderately toward bear: US 10y at 5.10% (+0.53pp/3m) raises the discount rate, and fading China risk appetite would reverse the investment income [Likely]. A SASAC-linked SOE has opaque reporting and no clear edge over larger peers [Likely]. Momentum is broken: -21.8% over 6 months, RSI 21.5 [Certain].
## Bull case
On every peer measure the stock is cheap: P/B 0.4x against a 1.1x peer median, and P/E 2.0x against 4.8x [Certain]. Even if ROE halves, book value compounding at that rate would justify more than 0.4x book [Guessing]. Leverage has fallen steadily, with net debt/EBITDA (site definition) down from 5.06x to 2.35x [Certain]. Operating cash flow has exceeded net income in every year, and the Piotroski score is 6 [Certain]. China stimulus that sustains the equity gains would move value toward the P/B+ROE bull of 22.54 [Guessing]. The stock is oversold (RSI 21.5) ahead of the Nov 25, 2026 results [Certain]. If those results show earnings durability, the market's reversion discount could unwind [Guessing].
## Decision
```json
{
  "ticker": "HKG:0966",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging state-owned life insurer looks cheap against peers, but its ROE surge is likely market-driven investment income, so the base fair value offers little margin of safety at today's price.",
  "rationale": "Base fair value sits barely above the price, the earnings spike is likely non-recurring, P/B is near the top of its own 5y range and the macro tilt is moderately bearish. Cheap peer multiples are not enough for conviction 4. Wait for the full-year results to test ROE durability, or for a price with a real margin of safety.",
  "price_at_decision": 17.46,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-0966/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, showing the FY2025 surge was a one-off investment gain rather than a durable improvement (would confirm AVOID; staying above it after FY2026 results would argue for re-research).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises back above 4x, reversing the five-year deleveraging from 5.06x to 2.35x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4}},
    {"text": "FCF conversion (cash-flow vs income statement) falls below 150% of net income, signalling deteriorating float economics."},
    {"text": "Piotroski F-score on the statistics page falls below 5, indicating broad fundamental deterioration."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 22.54, "basis": "ROE holds well above pre-2025 levels and the P/B+ROE bull value of 22.54 [ST,RA] is reached; set below the blended bull of 31.79 because the P/E leg capitalises spiked TTM earnings, per the note's section 3."},
    "base": {"probability": 0.45, "target_price_12m": 18.81, "basis": "Earnings revert partly toward the pre-2025 run-rate while book value holds, matching the mechanical base fair value of 18.81 [IS,BS,RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 12.36, "basis": "Investment gains reverse and ROE falls back toward the 7.5%-10.0% FY2022-FY2024 range [RA], giving the bear fair value of 12.36; probability raised from 0.25 by the macro overlay's moderate tilt toward bear (rising US 10y and dollar, research/HKG-0966/2026-10-19-macro.md)."}
  },
  "entry_price": 15.05,
  "entry_basis": "valuation file: base 18.81 x 0.8 (20% margin of safety); at that level the reversion risk is priced with a cushion.",
  "replaces": null,
  "replacement_reason": null
}
```
