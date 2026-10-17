# Evaluation: Pop Mart International Group (HKG:9992) — 2026-10-17
## Bear case
The cheap trailing multiples (P/E 12.4x, EV/EBITDA 7.6x, both below their 5y minimums [RA]) are probably measured on peak, hit-driven earnings: ROIC jumped from 35.8% (FY2023) to 247.8% (FY2025) on one character franchise, and press frames H1 2026 as a sharp growth slowdown while the company hunts for its next blockbuster [Likely] (WSJ headline, 2026-08-20). Cash quality is already slipping: FCF margin 17.9% TTM vs 35.1% FY2024, FCF conversion 54.5% TTM [Certain] [CF,IS]. On a normalised basis the mechanical base fair value is 119.17 HKD, below the 142.20 HKD close, and the bear value 56.27 HKD shows how far a fad unwind could go [Certain] [fair value]. The reverse DCF needs 24.6% year-one revenue growth, demanding against a decelerating franchise [Likely]. Price trend is broken (−18.7% vs 200-day) with no evidence the slowdown has bottomed [Certain] [HI].

## Bull case
This is an exceptionally profitable, net-cash IP business: gross margin 71.7%, operating margin 46.0%, ROE 71.2% TTM, Altman Z 25.24 [Certain] [IS,RA,ST]. Owned IP plus a vertically integrated design-retail flywheel and global store build-out (Times Square, Singapore) give multiple shots at new hits [Likely] (note §1). Trading below its own 5y minimum P/E and EV/EBITDA and below peer medians of 16.7x and 10.4x, the price may already discount a lot of fade [Likely] [RA]. Insiders own 45.29%, shares are flat (−0.24% YoY) [Certain] [ST]. If a second franchise sustains growth, the mechanical bull value of 315.39 HKD shows large convexity [Guessing].

## Decision
```json
{
  "ticker": "HKG:9992",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A superb-margin, net-cash IP toy franchise looks cheap on trailing multiples, but those earnings are likely a single-character peak and the normalised base fair value sits below the price.",
  "rationale": "Quality is outstanding, but low trailing multiples rest on hit-driven peak earnings, growth is decelerating, FCF conversion is falling and base fair value is below the price. Durability of the IP engine is unproven, so good-not-compelling: AVOID, cash preferred. Re-research nearer the margin-of-safety entry or on evidence of a second franchise.",
  "price_at_decision": 142.20,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-9992/2026-10-17.md",
  "triggers": [
    {"text": "TTM gross margin falls below 60%, showing IP pricing power eroding beyond mix shift.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}},
    {"text": "TTM FCF margin falls below 12%, showing cash-conversion deterioration is structural rather than expansion-driven.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 40%, showing the IP moat reverting rather than normalising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Next reported half-year (H2 2026 results) shows revenue declining year on year on the income statement, confirming the Labubu fade is not being replaced by new IP."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 190.0, "basis": "A new franchise sustains growth and EV/EBITDA re-rates toward the 10.4x peer median [RA,P] on TTM EBITDA [IS]; set below the mechanical bull 315.39 because that assumes hyper-growth-era multiples."},
    "base": {"probability": 0.45, "target_price_12m": 120.0, "basis": "Growth keeps decelerating per the H1 2026 slowdown (WSJ headline, 2026-08-20) and the price converges on the mechanical base fair value of 119.17 (DCF 121.94, EV/EBITDA 113.62)."},
    "bear": {"probability": 0.35, "target_price_12m": 64.08, "basis": "Labubu demand fades without a replacement (CNBC headline, 2026-03-25) and earnings normalise, matching the EV/EBITDA bear value of 64.08 in the fact sheet's fair value table."}
  },
  "entry_price": 95.34,
  "entry_basis": "valuation file: base 119.17 x 0.8; at that level the normalised value would carry a margin of safety even if the hit-driven earnings fade.",
  "replaces": null,
  "replacement_reason": null
}
```
