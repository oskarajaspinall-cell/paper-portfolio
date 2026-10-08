# Evaluation: Masco Corporation (MAS) — 2026-10-07
## Bear case
The discount is thinner than it looks: P/E 15.7x sits just under the 5y median 16.6x, and EV/EBITDA 11.0x against an 11.9x median [Certain] [RA]. TTM margins (operating 17.8%, FCF 14.8%) are flattered by a one-time Q2 2026 tariff refund, so the "cheap on FCF" signal partly rests on non-recurring cash [Likely] [Q2 2026 transcript]. ROIC has slipped from 32.7% to 30.8% [Certain] [RA]. Home Depot is ~38% of sales, giving one buyer pricing leverage [Certain] [10-K]. The macro overlay is a moderate bear tilt: 10y real yields up 0.71pp in 3 months keep mortgage rates and remodel demand under pressure with no relief priced [Likely] [macro overlay]. Beta 1.29 and -17.1pp 12m relative strength show no catalyst yet [Certain] [ST]. Q3 results on Oct 28 could reset guidance [Guessing].

## Bull case
A 30.8% ROIC, 37.2% gross-margin brand franchise (Delta, Behr) trades at 12.1x P/FCF, below its 5y minimum 12.8x, and 18-37% below peers on P/E, EV/EBITDA and P/FCF [Certain] [RA]. The 8.29% FCF yield funds a 4.66% annual share-count reduction plus a rising dividend, compounding per-share value even without a re-rating [Certain] [ST]. Leverage is stable at 1.95x net debt/EBITDA, Altman Z 3.86 [Certain] [RA, ST]. Management raised FY2026 guidance and targets higher margins by 2028 [Likely] [Q2 2026 transcript]. A rate pivot would re-rate housing-linked multiples quickly [Guessing].

## Decision
```json
{
  "ticker": "MAS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROIC branded building-products franchise trading below its 5y P/FCF minimum, but the discount to its own P/E and EV/EBITDA medians is modest, TTM cash flow is flattered by a one-off tariff refund and a rising real-yield backdrop delays any housing-led re-rating.",
  "rationale": "Quality is genuine and buybacks support per-share value, but the valuation gap to its own history is narrow on earnings multiples, the FCF yield is partly one-off, ROIC is drifting lower, Home Depot concentration is high and the macro overlay tilts moderately bearish. Good, not compelling: conviction 3 means AVOID; cash is acceptable.",
  "price_at_decision": 69.93,
  "price_date": "2026-10-06",
  "research_note": "research/MAS/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 34%, under the 5-year range low, showing tariff and input costs are not being passed through.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 34}},
    {"text": "TTM ROIC falls below 28%, below the 5-year range, confirming the returns drift is structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}},
    {"text": "TTM FCF margin falls below 9%, under the 5-year low, once the one-off tariff refund drops out.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 9}},
    {"text": "The Home Depot share of net sales or Behr exclusive distribution arrangement changes materially, as disclosed in an SEC 10-K/10-Q or 8-K."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 77.0, "basis": "EV/EBITDA re-rates to its 5y median 11.9x [RA] on TTM EBITDA with net debt/EBITDA 1.95x [RA]; probability cut from 0.25 by the macro overlay's moderate bear tilt (research/MAS/2026-10-07-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 70.0, "basis": "EV/EBITDA holds at 11.0x [RA] as buybacks (-4.66% shares YoY [ST]) offset fading of the one-off tariff refund (Q2 2026 transcript)."},
    "bear": {"probability": 0.35, "target_price_12m": 58.0, "basis": "EV/EBITDA compresses to its 5y minimum 9.5x [RA] as real yields keep remodel demand soft; probability raised from 0.25 per the macro overlay's moderate bear tilt (research/MAS/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
