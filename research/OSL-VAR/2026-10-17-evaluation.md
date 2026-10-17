# Evaluation: Vår Energi ASA (OSL:VAR) — 2026-10-17

## Bear case
The cheap trailing multiples are a peak-cycle illusion: TTM ROIC of 25.6% compares with 13.8% in FY2025 and 7.0% in FY2024, so earnings are flattered by high commodity prices [Likely]. On its own history the stock is not cheap: EV/EBITDA sits at 86% and EV/Sales at 93% of their 5y ranges [Certain]. The mechanical fair value puts base at NOK 33.16 and bull at NOK 54.49, below the NOK 55.76 close [Certain]. FCF margin has fallen 10.6pp over five years [Certain]. The pending $1.3bn BlueNord deal adds integration and financing risk not yet in TTM figures [Likely]. The macro overlay tilts moderately toward bear: a fast dollar rise, a 5.10% 10y yield and wider HY spreads [Certain]. Eni's majority control limits minority influence [Likely]. Q3 results on Oct 21, 2026 add event risk after a +71.0% 12-month run [Certain].

## Bull case
On current earnings the stock is cheap against peers: P/E 10.7x vs an 18.1x peer median and P/FCF 4.7x vs 13.4x, with a 21.27% FCF yield [Certain]. Operating margin of 56.2% and gross margin of 88.1% are both rising over five years, Piotroski F is 8 and net debt/EBITDA is only 0.41x [Certain], leaving room to fund BlueNord without strain [Likely]. Q1 and Q2 2026 were record quarters with production on track for guidance [Likely]. BlueNord increases exposure to European gas and key infrastructure, raising reserves and production [Likely]. If oil and gas prices hold, the P/E sits near the bottom of its own 5y range (8%) and could re-rate toward its 11.8x median [Guessing].

## Decision
```json
{
  "ticker": "OSL:VAR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost, low-leverage Norwegian E&P generating a 21.27% FCF yield on peak-cycle earnings, but priced near its own bull fair value with a moderately bearish macro tilt and a pending BlueNord integration.",
  "rationale": "Trailing cheapness rests on cyclically high commodity earnings; own-history EV/EBITDA and EV/Sales are near 5y highs and the close sits above the mechanical bull fair value. Macro overlay tilts toward bear, Q3 results land Oct 21, 2026 and BlueNord is unclosed. Good business, not a compelling price: no position, cash preferred.",
  "price_at_decision": 55.76,
  "price_date": "2026-10-16",
  "research_note": "research/OSL-VAR/2026-10-17.md",
  "triggers": [
    {"text": "TTM net debt/EBITDA rises above 1.0x, showing BlueNord financing or a commodity downturn is straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "TTM ROIC falls below 13%, back to around its FY2025 level, showing the return spike was cyclical rather than structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 15%, confirming the five-year decline in cash generation is continuing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 45%, under its five-year range, signalling cost or volume pressure beyond the tax wedge.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 61.0, "basis": "Commodity prices hold and BlueNord closes cleanly, so P/E re-rates from 10.7x toward its 11.8x 5y median [RA] on TTM earnings [IS], above the 54.49 bull fair value because current earnings exceed the own-history EV/EBITDA model's assumptions."},
    "base": {"probability": 0.45, "target_price_12m": 45.0, "basis": "Earnings normalise from the TTM ROIC of 25.6% toward the FY2025 13.8% [RA] while EV/EBITDA holds near its 2.0x median [RA], placing value between the 33.16 base and 54.49 bull fair value [fact sheet] given the low 0.41x leverage."},
    "bear": {"probability": 0.30, "target_price_12m": 26.0, "basis": "Macro overlay (research/OSL-VAR/2026-10-17-macro.md, toward bear, moderate) raised this probability: a stronger dollar and 5.10% 10y yield cut realisations and the multiple, moving value toward the 17.24 bear fair value [fact sheet], cushioned by the 21.27% FCF yield [ST]."}
  },
  "entry_price": 26.53,
  "entry_basis": "valuation file: base 33.16 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
