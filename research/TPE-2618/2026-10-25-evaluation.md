# Evaluation: EVA Airways Corp. (TPE:2618) — 2026-10-25
## Bear case
This is an airline at or near a profit peak. TTM ROIC of 17.1% compares with 3.8% in FY2021 and 4.0% in FY2022 [RA] [Certain]. Operating margin has already eased from 17.5% in FY2024 to 14.5% TTM, and FCF margin is falling [IS,CF] [Certain]. A P/E of 9.0x on peak-like earnings is not cheap through the cycle. The 5y P/E median is 8.3x, so the stock trades above its own norm [RA] [Certain]. Fuel, cargo rates driven by the AI supply chain, capacity and Taiwan Strait geopolitics are all outside management's control [Likely]. Altman Z of 1.69 and Piotroski F of 5 are mediocre [ST] [Certain]. The mechanical base fair value of 177.35 TWD rests on a through-cycle DCF whose bull case of 538.35 is clearly inflated. The EV/EBITDA leg gives 45.98, close to the 42.20 close [Likely]. Results are due Nov 13, 2026 and could confirm that margins are fading [Guessing].
## Bull case
The balance sheet has been transformed: net debt/EBITDA fell from 3.52x to 0.30x [BS,IS] [Certain]. FCF conversion is 175.7% TTM, the FCF yield is 19.77% and the share count is stable [CF,ST] [Certain]. EV/EBITDA of 4.1x is below its 5y minimum of 4.8x and below the peer median of 4.3x [RA] [Certain]. The reverse DCF implies -27.4% revenue growth in year 1, so a downcycle is already priced [Likely]. The premium long-haul franchise and Taiwan's tech-driven cargo flow support returns above the pre-2023 levels [Likely]. Beta is low at 0.42 [ST] [Certain].
## Decision
```json
{
  "ticker": "TPE:2618",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A de-levered, cash-generative airline that is cheap on current multiples, but those multiples rest on cycle-peak returns in an uncontrollable, geopolitically exposed industry.",
  "rationale": "The cheapness is real but mostly cyclical. Margins are already fading from the FY2024 peak, P/E sits above its own 5y median and the industry has no durable moat. The credible EV/EBITDA fair value is near the price, and the DCF upside is not believable. Good but not compelling, so we hold no position.",
  "price_at_decision": 42.20,
  "price_date": "2026-10-22",
  "research_note": "research/TPE-2618/2026-10-25.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8% (income statement page)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 10% (ratios page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt / EBITDA rises above 1.5x (ratios page)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin turns negative (cash flow page)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 55.00, "basis": "Margins hold near the TTM 14.5% [IS] and EV/EBITDA re-rates from 4.1x to its 5y median of 5.4x [RA]; this sits well below the DCF bull, which extrapolates peak returns."},
    "base": {"probability": 0.45, "target_price_12m": 45.98, "basis": "The EV/EBITDA leg of the fair value (base 45.98 [fact sheet Fair value]) is used instead of the 177.35 blend, because the through-cycle DCF capitalises cycle-peak FCF (FCF margin falling [CF,IS])."},
    "bear": {"probability": 0.30, "target_price_12m": 35.17, "basis": "Operating margin keeps fading from the FY2024 peak of 17.5% [IS] and P/E returns to its 5y low of 7.5x [RA], near the 52-week low of 32.15 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock is already below its own EV/EBITDA range. What blocks conviction 4 is cyclical, peak-like returns with no durable moat and Taiwan Strait risk, and a lower price would not change that.",
  "replaces": null,
  "replacement_reason": null
}
```
