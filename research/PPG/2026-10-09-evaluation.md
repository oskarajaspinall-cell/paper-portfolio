# Evaluation: PPG Industries, Inc. (PPG) — 2026-10-09
## Bear case
The cheapness is relative to an inflated history: the 5y median P/E of 27.8x and P/FCF of 34.4x came from depressed FY2022 earnings and cash flow, so "below the 5y minimum" overstates the discount [Likely] (RA). Mechanical base fair value is $100.06, 5% below the $105.46 close, and the price already implies 8.2% year-one revenue growth, demanding for a GDP-plus coatings business [Certain] (fact sheet fair value). Returns are flat (ROIC 11.6% TTM, +0.8pp over 5y), ROE is trending down and FCF conversion swings from 46% to 149% [Certain] (RA, CF). The tape confirms no catalyst yet: -11.5pp/-18.4pp vs SPY over 3m/6m, below both moving averages, 50-day under 200-day [Certain] (HI). Rising real yields and a firmer dollar weigh on DCF value and translated non-US earnings (macro overlay, tilt toward bear) [Likely]. Q3 results on Oct 27 can still show Refinish weakness [Guessing].

## Bull case
PPG trades at 15.1x P/E and 10.8x EV/EBITDA, 25% and 12% below SHW/AXTA/RPM, with a 6.04% FCF yield [Certain] (RA, ST). Margins are better than five years ago: gross 41.2% (+2.6pp), operating 13.2% (+3.0pp), showing pricing power in a consolidated oligopoly [Certain] (IS). Q2 2026 delivered a sixth straight quarter of organic growth, Aerospace backlog and the best Industrial Coatings organic growth in five years, with Refinish destocking described as behind it [Likely] (transcript). Leverage is moderate at 2.14x net debt/EBITDA, share count fell 2.53% and Altman Z is 3.72 [Certain] (ST, RA). The EV/EBITDA method puts base value at $156.95, so if the market re-credits the margin step-up, the bull fair value of $127.17 is reachable [Likely] (fact sheet fair value).

## Decision
```json
{
  "ticker": "PPG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A good but not great coatings franchise with improved margins trades at a peer and own-history discount, but flat returns, a price above mechanical base fair value and no visible catalyst leave the margin of safety too thin for a core position.",
  "rationale": "Cheap versus peers, but the 5y multiple ranges are inflated by FY2022, base fair value ($100.06) sits below the price, ROIC is flat and relative strength is poor ahead of Q3 results. The macro tilt is toward bear. Good but not compelling, so conviction 3: AVOID, with an entry price at base fair value less 20%.",
  "price_at_decision": 105.46,
  "price_date": "2026-10-08",
  "research_note": "research/PPG/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 39.0%, the FY2021 five-year low, showing pricing power against raw-material costs has been lost.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 39.0}},
    {"text": "TTM operating margin falls below 10.4%, the FY2021 level, reversing the five-year margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.4}},
    {"text": "TTM ROIC falls below 9.8%, the FY2022 five-year low, showing returns are deteriorating rather than inflecting.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9.8}},
    {"text": "Aerospace or Industrial Coatings organic growth turns negative for two consecutive quarters in the earnings releases, showing the stated growth engines have stalled."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 127.17, "basis": "Aerospace/Industrial organic growth continues (Q2 2026 transcript) and the market re-credits the +3.0pp operating-margin step-up [IS], lifting value to the fact sheet's bull fair value of $127.17, still below the EV/EBITDA method's base of $156.95."},
    "base": {"probability": 0.45, "target_price_12m": 105.46, "basis": "Multiples stay near current 15.1x P/E and 10.8x EV/EBITDA [RA] as flat ROIC of 11.6% [RA] earns no re-rating; held at the $105.46 close, between the $100.06 base fair value and peer-median EV/EBITDA of 12.2x."},
    "bear": {"probability": 0.30, "target_price_12m": 93.39, "basis": "Refinish weakness and FX drag cut earnings and the stock retests its 52-week low of $93.39 [HI]; probability raised from 0.25 by the macro overlay's small tilt toward bear (research/PPG/2026-10-09-macro.md: rising real yields and dollar), set above the $39.58 bear fair value because that DCF bear uses trough FCF while the EV/EBITDA bear is $105.74."}
  },
  "entry_price": 80.05,
  "entry_basis": "valuation file: base 100.06 x 0.8; at that level the 20% margin of safety would compensate for flat returns and volatile FCF conversion.",
  "replaces": null,
  "replacement_reason": null
}
```
