# Evaluation: New China Life Insurance Company Ltd. (SHA:601336) — 2026-10-19
## Bear case
TTM ROE of 42.8% sits far above the FY2021–FY2023 band (14.2%, 20.8%, 8.6%) and ROIC troughed at 3.8% in FY2023 [Certain] (RA): earnings track China's investment cycle, so the 3.7x P/E is measured on peak profits [Likely]. On book value, the steadier yardstick for a life insurer, the stock is 1.2x versus a 0.8x peer median, a premium a reverting ROE would not support [Likely] (RA, peers). The P/E fair-value method gives a base of only 37.25 CNY, and the mechanical bear of 23.89 CNY shows the downside if the cycle turns [Certain] (fact sheet). Price is in a downtrend (-20.2% vs 200-day, 50-day below 200-day) with results due Oct 31, 2026 [Certain] (HI, ST). No dividend, buyback or solvency data is available to cushion the case [Certain] (note §5). The macro overlay tilts slightly toward bear on tightening global conditions [Certain] (macro overlay).
## Bull case
Profitability is genuinely improving: ROE has risen from 14.2% (FY2021) to 34.9% (FY2025) and 42.8% TTM, and management's Q2 2026 call cited net profit up 54%, premium growth and high persistency [Likely] (RA; OV transcript). P/E of 3.7x is below its own 5-year minimum and well below the 5.2x peer median [Certain] (RA). The best-fit P/B + ROE method gives a base of 69.20 CNY and the blended base fair value is 58.55 CNY, above the 52.31 close, with a bull of 87.87 CNY [Certain] (fact sheet). RSI of 24.6 shows the stock oversold after a fall from its 85.85 52-week high [Certain] (ST, HI). CNY is firm with no country-risk stress [Certain] (macro overlay). If the Oct 31 results confirm that investment returns are holding, normalisation fears could ease [Guessing].
## Decision
```json
{
  "ticker": "SHA:601336",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A life insurer on a 3.7x P/E that looks cheap only on a likely-peak 42.8% TTM ROE, while trading at a premium to peers on book value with modest base fair-value upside, so the market already prices profit normalisation.",
  "rationale": "Earnings are cyclical investment-spread profits at a probable peak; the earnings discount is offset by a book-value premium to peers. Base fair value offers only modest upside, the bear case is deep, no capital-return data exists, and results land within weeks. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 52.31,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601336/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE falls below 15% on the statistics page, showing the profit cycle has reverted to the FY2021-FY2023 range and recent profits were a cyclical peak (would confirm AVOID and remove the entry price).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 8%, back toward the FY2023 trough of 3.8%, indicating investment losses are eroding capital generation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Positive case: FY2026 annual results show ROE holding above 25% with continued premium growth and persistency in the company's annual report, evidencing that profitability is structurally higher rather than cyclical (would lift conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 87.87, "basis": "ROE holds well above its FY2021-FY2023 range as the Q2 2026 call's premium and persistency momentum continues, and the stock reaches the fact sheet's bull fair value of 87.87 CNY (P/B + ROE bull 84.97, P/E bull 93.66) [IS,BS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 55.0, "basis": "ROE partly normalises from 42.8% TTM [RA], so the value lands between the P/E base of 37.25 and the P/B + ROE base of 69.20, a little below the blended base fair value of 58.55 because the P/B premium to the 0.8x peer median [RA] limits re-rating; probability trimmed slightly for the overlay's small bear tilt (research/SHA-601336/2026-10-19-macro.md)."},
    "bear": {"probability": 0.3, "target_price_12m": 25.74, "basis": "Investment returns roll over as in FY2023 (ROIC 3.8%, ROE 8.6%) [RA] and the market prices the P/E bear value of 25.74 CNY, near the mechanical bear fair value of 23.89; weight raised for the macro overlay's small tilt toward bear on tightening global conditions (research/SHA-601336/2026-10-19-macro.md)."}
  },
  "entry_price": 46.84,
  "entry_basis": "valuation file: base 58.55 x 0.8; at that price even the partial-normalisation base case leaves enough margin to absorb peak-ROE reversion.",
  "replaces": null,
  "replacement_reason": null
}
```
