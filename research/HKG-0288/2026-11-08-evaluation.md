# Evaluation: WH Group Limited (HKG:0288) — 2026-11-08
## Bear case
This is a hog-cycle business priced on cycle-high earnings. FY2023 showed the downside: ROIC 4.8% and operating margin 2.8% [RA, IS] [Certain]. Management guided to 2026 margin pressure from lower hog prices, and nine-month profit fell year on year (Q3 release 2026-10-27, nasdaq headline) [Likely]. The last 12 months are flat rather than improving: operating margin 9.8% vs 10.0% a year earlier and FCF margin 6.5% vs 7.2% [IS-T, CF-T] [Certain], so the 5-year "rising" trend is a rebound from a trough, not a structural step-up. On P/E the stock is not cheap against itself: 7.0x vs a 5y median of 7.5x [RA] [Certain]. The DCF base of 17.64 capitalises near-peak FCF with a floored beta (raw 0.17) [ST] [Likely]. Price momentum is −33.0% over 6 months with no catalyst [HI] [Certain]; China/HK governance discount persists [Likely]; dividend and buyback data are unavailable [Certain].

## Bull case
Even mid-cycle, the cash is real: FCF conversion 119.6%, a 17.19% FCF yield and net debt/EBITDA of 0.33x [CF, ST, RA] [Certain]. EV/EBITDA of 3.8x is below its 5-year minimum of 4.1x and P/FCF of 5.8x sits near its low, against peers TSN/HRL/JBS at 10.1x EV/EBITDA [RA] [Certain]. The reverse DCF implies revenue falling 24.1% in year 1 — a collapse, not a cycle [fact sheet Fair value] [Certain]. Packaged meats, the profit core, grew in H1 2026 through new channels and innovation (Q2 2026 transcript) [Likely], dampening pork-price swings relative to FY2023. The mechanical bear fair value of 8.30 is above the 6.59 close [Certain]. The yuan firmed modestly, a mild translation tailwind (macro overlay, context only) [Likely]. If hog margins merely stabilise, a re-rating toward median EV/EBITDA plus cash returns could deliver attractive returns from a low-beta name [Guessing].

## Decision
```json
{
  "ticker": "HKG:0288",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative, low-leverage pork and packaged-meat producer looks optically cheap on EV/EBITDA and FCF yield, but trades near its own median P/E on cycle-high earnings that management's guided hog-price margin pressure and falling nine-month profit suggest are rolling over.",
  "rationale": "Cash yield and balance sheet are genuinely attractive, but P/E sits near its 5y median on near-peak margins, the last 12 months are flat-to-down, profit is falling and momentum is poor. The DCF base overstates value by capitalising cyclical FCF. Good but not compelling: conviction 3, AVOID; revisit at a bear-case P/E.",
  "price_at_decision": 6.59,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-0288/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 7.5% (9.8% now), showing the hog-price downturn is compressing margins toward the FY2023 trough of 2.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7.5}},
    {"text": "TTM ROIC falls below 11% (15.5% now), confirming FY2024-25 returns were cyclical rather than structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.33x TTM now), above the FY2023 1.43x, showing cash generation has broken down.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Company results show packaged-meat operating profit growing year on year for two consecutive reported periods while pork margins fall, evidencing a durable brand profit floor that would raise conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 8.62, "basis": "Hog margins stabilise and packaged meats keep growing (Q2 2026 transcript), lifting P/E to the mechanical P/E bull value of 8.62 [fact sheet Fair value]; well below the DCF bull of 25.47 because that DCF capitalises the near-peak 6.5% FCF margin [CF-T] that FY2023's 3.1% shows can halve."},
    "base": {"probability": 0.45, "target_price_12m": 7.12, "basis": "Guided 2026 hog-price margin pressure (H2 2025 transcript) trims earnings while the stock holds near its 7.5x 5y median P/E [RA]: the P/E base value of 7.12 [fact sheet Fair value], below the blended base of 17.64 because the DCF leg assumes the cycle-high FCF margin persists."},
    "bear": {"probability": 0.30, "target_price_12m": 5.16, "basis": "Pork margins retrace toward FY2023 (operating margin 2.8%, ROIC 4.8% [IS, RA]) as nine-month profit falls further: the P/E bear value of 5.16 [fact sheet Fair value], near the 5y minimum P/E of 5.5x [RA], below the blended bear of 8.30 whose DCF leg still capitalises current cash flow."}
  },
  "entry_price": 5.16,
  "entry_basis": "The P/E bear fair value of 5.16 [fact sheet Fair value], near the 5y minimum P/E of 5.5x [RA]: at that price a full hog-cycle downturn is priced while the 17.19% FCF yield and 0.33x leverage remain, which would justify conviction 4. The default base x 0.8 (17.64 x 0.8) is above the price and rests on the DCF's cycle-high FCF, so it is not used.",
  "replaces": null,
  "replacement_reason": null
}
```
