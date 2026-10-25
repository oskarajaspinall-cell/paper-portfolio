# Evaluation: Industrias Peñoles (BMV:PE_OLES) — 2026-10-24
## Bear case
Earnings are at a cyclical peak, not a new norm [Certain]: TTM operating margin is 39.1% against 1.1% in FY2023, and ROIC 38.7% against 0.9% [RA, IS]. A price-taking miner has no pricing power, so the low multiples (P/E 8.7x, EV/EBITDA 3.9x, both below their 5y minimum [RA]) are the classic cyclical trap [Likely]. Asset-based measures already price in high margins: EV/Sales 1.8x against a 1.4x median and P/B 2.2x against 0.9x [RA] [Certain]. The mechanical base fair value of 596.48 MXN is 27.4% below the close, and the bear 365.93 [Certain]. The macro overlay tilts toward bear (small): the 10y real yield is 2.64%, up 0.21pp over ~3m, and the dollar is firmer, both headwinds for silver and gold [Likely]. NAV is [data unavailable], so reserve value cannot anchor the price [Certain]. Q3 results land on Oct 26 [Certain].

## Bull case
The balance sheet is pristine: net debt/EBITDA -0.14x, Piotroski F 8, Altman Z 5.28 [ST, RA] [Certain]. Cash conversion is real, with TTM FCF/NI 108.8%, FCF margin 21.2% and a 12.59% FCF yield [CF, ST] [Certain]. On current earnings the stock trades about half the peer median on P/E (18.7x) and EV/EBITDA (7.6x) [Certain]. The price is down 13.4% over 6m with RSI 36.2, so part of the real-yield headwind is likely priced [Likely]. If metal prices hold, the mechanical bull of 1,730.18 MXN shows how much gearing remains [Guessing].

## Decision
```json
{
  "ticker": "BMV:PE_OLES",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-financed, cash-generative miner whose cheap multiples rest on peak-cycle metal-price margins, with the price already above the mechanical base fair value.",
  "rationale": "Quality is metal prices, not a structural edge; multiples are low only on peak earnings, while EV/Sales and P/B sit above their 5y medians and price exceeds base fair value. The macro tilt is mildly negative and NAV is unavailable. Good balance sheet, not a compelling entry: AVOID with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 821.97,
  "price_date": "2026-10-23",
  "research_note": "research/BMV-PE_OLES/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25% (statistics page), showing the metal-price peak is unwinding", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 15% (statistics page), returns reverting to the FY2022-FY2024 trough range", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 10% (statistics page), cash conversion no longer supporting the FCF yield", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Q3 2026 results (Oct 26) or later filings show margins sustained near the 39.1% TTM operating margin with net cash intact, which would argue the earnings base is more durable than a peak"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 1073.92, "basis": "Margins hold near the 39.1% TTM operating margin [IS] and the price returns to its 6-month high of 1,073.92 [HI], still well below the mechanical bull of 1,730.18 because macro real-yield headwinds cap a re-rating (macro overlay)."},
    "base": {"probability": 0.45, "target_price_12m": 700, "basis": "Operating margin eases from the 39.1% TTM peak toward the FY2025 29.3% [IS] with EV/EBITDA near 3.9x [RA], landing between the mechanical base fair value of 596.48 and the current price."},
    "bear": {"probability": 0.35, "target_price_12m": 365.93, "basis": "Metal prices fall as real yields rise and the dollar firms (macro overlay tilt toward bear, small, adds probability here), margins compress toward the FY2022-FY2023 7.2%/1.1% range [IS], matching the mechanical bear fair value of 365.93."}
  },
  "entry_price": 477.18,
  "entry_basis": "valuation file: base 596.48 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
