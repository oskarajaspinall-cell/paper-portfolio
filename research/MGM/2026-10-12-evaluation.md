# Evaluation: MGM Resorts International (MGM) — 2026-10-12
## Bear case
MGM is a lessee, not an owner. A $23.9bn VICI lease liability fixes ~$736m/yr of rent on top of $6.1bn of funded debt, so lease-inclusive net debt/EBITDA is 12.25x and Altman Z is 0.82 [Certain]. ROIC of 3.6% TTM is below any reasonable cost of capital, and gross margin has fallen 4.8pp over five years to 44.2% [Certain]. Net margin collapsed from 13.3% to 2.4%, so the 20.3% FCF yield is flattered by a capital-light structure whose fixed rent hits equity first in a downturn [Likely]. The stock is down 37% in 3 months after the People Inc. proposal was withdrawn, and management is now reportedly weighing a bid for an unrelated media company. That would be a capital-allocation red flag [Guessing]. Rising real yields (+56bp/3m) are a small extra headwind (macro overlay) [Likely]. Q3 results on Oct 28 are an unresolved event [Certain].

## Bull case
On cash flow, the price already assumes a lot of bad news. P/FCF is 4.9x, below its 5y low of 6.8x and half the 9.7x peer median, and the reverse DCF implies a -7.7% revenue decline [Certain]. FCF margin has held at 8.4% TTM while buybacks cut the share count 9.11% YoY, with $1.4bn still authorised [Certain]. BetMGM turned equity-income positive in H1 2026 after years of losses, a structural improvement [Certain]. Piotroski F of 7 and rising ROIC since FY22 suggest operations are not deteriorating [Likely]. RSI of 13 at a fresh 52-week low, with VIX calm, points to forced, idiosyncratic selling that could reverse once M&A uncertainty clears [Likely]. Short interest of 10.51% could fuel a squeeze on a clean Q3 [Guessing].

## Decision
```json
{
  "ticker": "MGM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "MGM is optically cheap on free cash flow, but its lease-heavy, 12x-levered structure, sub-cost-of-capital ROIC and an unresolved capital-allocation overhang (a possible bid for People Inc.) make it a value trap until the M&A path and Q3 results are clear.",
  "rationale": "The 20.3% FCF yield is real but sits on fixed VICI rent, 3.6% ROIC and Altman Z 0.82. Management may pursue an unrelated media acquisition, and Q3 lands Oct 28. Good but not compelling: conviction 3, so no position. Cash is acceptable.",
  "price_at_decision": 29.27,
  "price_date": "2026-10-09",
  "research_note": "research/MGM/2026-10-12.md",
  "triggers": [
    {"text": "ROIC falls below 2%, reversing the recovery since FY22 and confirming returns stay far below the cost of capital", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 2}},
    {"text": "Lease-inclusive debt/EBITDA rises above 13x, showing fixed VICI rent outpacing EBITDA", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 13}},
    {"text": "Gross margin falls below 42%, extending the 5-year decline from 49.2%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 42}},
    {"text": "MGM announces a signed acquisition of People Inc. or another unrelated media business (8-K), or BetMGM equity income turns negative again in the 10-Q"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 40.6, "basis": "M&A overhang clears and Q3 holds FCF margin near 8.4% [CF,IS], so P/FCF re-rates from 4.9x to its 5y low of 6.8x [RA]; this is far below the mechanical bull fair value of 391.53 because the DCF treats lease-light FCF as if no $23.9bn VICI liability existed (sec.gov 10-Q)."},
    "base": {"probability": 0.45, "target_price_12m": 31.0, "basis": "P/FCF stays near 4.9x [RA], with a 9.11% YoY share-count reduction [ST] adding modest per-share accretion; deliberately below the 129.85 base fair value, which the note judges distorted by lease-driven DCF/EV inputs (research/MGM/2026-10-12.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 22.0, "basis": "A value-destroying People Inc. bid or weak Q3 pushes net debt/EBITDA above 12.25x [BS,IS] and the stock through its 29.18 52-week low [HI]; probability raised by a small toward-bear tilt from rising real yields and HY spreads (research/MGM/2026-10-12-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at a P/FCF of 4.9x [RA] the stock is already below every own-history low. Conviction is capped by the unresolved People Inc. capital-allocation question and the Oct 28 Q3 results. The default anchor (base 129.85 x 0.8) is far above the price and not meaningful. Re-research once the M&A path is clear.",
  "replaces": null,
  "replacement_reason": null
}
```
