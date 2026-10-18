# Evaluation: Zhejiang NHU Company Ltd. (SHE:002001) — 2026-10-18

## Bear case
NHU is a commodity vitamin producer, and the "cheap" multiples are measured on near-peak margins [Likely]. Gross margin (42.9% TTM) is back near its FY2021 high of 44.2%, after collapsing to 31.5% in FY2023, when ROIC fell to 9.2% [Certain] (IS, RA). P/E 11.2x below its 5y min is what cyclicals look like at peak earnings [Likely]. The price is -30.5% over six months and below a falling 200-day average (50-day 8.4% under it) [Certain] (HI, ST), consistent with the market pricing a vitamin-price rollover before it shows in TTM figures [Guessing]. Base fair value 26.50 is barely above the 26.14 close, and the bear value 4.34 shows how much a FY2022/23-style trough costs [Certain] (fact-sheet fair value). Q3 results land on Oct 28, 2026 [Certain] (ST), so the key evidence is ten days away. No segment split or pricing data to test any of this [Certain] (note §1).

## Bull case
Through a full cycle NHU stayed profitable with ROIC never below 9.2%, and TTM ROIC is 22.5% with ROE 22.0% [Certain] (RA). Cash conversion has transformed: FCF/NI 91.4% TTM against -15.8% in FY2022, funding net cash (net debt/EBITDA -0.25x) [Certain] (CF, RA). At an 8.18% FCF yield and P/FCF 12.2x against a peer median of 27.5x, the price already discounts some margin fade [Certain] (ST, RA); the reverse DCF implies only 5.3% year-one growth [Certain]. Scale and backward integration likely make NHU a low-cost producer that wins share in troughs [Likely]. Altman Z 6.62 means no distress risk [Certain] (ST). Bull fair value 40.52 is reachable if FY2024/25 margins prove durable [Likely].

## Decision
```json
{
  "ticker": "SHE:002001",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return vitamin and nutrition chemicals producer trading below its own 5-year multiple lows, but on margins near the top of a commodity cycle whose base fair value is roughly the current price.",
  "rationale": "Quality and cash generation are real, but the cheapness rests on near-peak cyclical margins; base fair value offers no margin of safety, the share is in a six-month downtrend, and Q3 results on Oct 28 will test pricing. Good but not compelling: AVOID, with an entry price below base fair value.",
  "price_at_decision": 26.14,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002001/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 35%, signalling the vitamin-pricing cycle has turned down again rather than the FY2024/25 recovery being durable.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 10% (27.0% now), showing capacity spend or pricing is no longer converting to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 12%, showing new Chinese vitamin capacity is eroding returns toward the FY2023 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 40.52, "basis": "FY2024/25 margins (gross 43.6% FY2025 [IS]) prove durable and the mechanical bull fair value of 40.52 is reached."},
    "base": {"probability": 0.45, "target_price_12m": 26.5, "basis": "Margins ease modestly from near-peak levels and the stock tracks base fair value of 26.50 (DCF 27.70 / P/E 24.10 blend, fact-sheet fair value)."},
    "bear": {"probability": 0.3, "target_price_12m": 17.24, "basis": "A vitamin-price downturn like FY2023 (gross margin 31.5% [IS]) drives the P/E bear value of 17.24; the blended bear of 4.34 is not used because its DCF leg (-2.12) assumes a trough persists for a decade, unlike the FY2024 recovery [RA]."}
  },
  "entry_price": 21.2,
  "entry_basis": "valuation file: base 26.50 x 0.8, a margin of safety that would compensate for buying cyclical margins near their high.",
  "replaces": null,
  "replacement_reason": null
}
```
