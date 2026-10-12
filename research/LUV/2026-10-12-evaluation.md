# Evaluation: Southwest Airlines Co. (LUV) — 2026-10-12
## Bear case
Southwest is a commodity domestic airline with no visible moat, and it is not generating cash. FCF margin has been negative every year since FY2022 (-1.4% TTM) [Certain]. Even so, buybacks cut the share count 13.01% YoY. Net debt/EBITDA has gone from net cash in FY2024 (-0.40x) to 1.33x TTM, so the balance sheet is paying for the buybacks [Certain]. A $14.8bn aircraft order book runs to 2031, and the company may also order 787 widebodies, so capex will stay heavy [Likely]. It stopped fuel hedging in 2025, which leaves earnings fully exposed to volatile jet fuel [Certain]. At 2.9x, P/B is above its entire 5y range and 38% above peers, and P/E is 97% above peers [Certain]. Base fair value of 42.52 is only 2.1% above the price, with -31.7% to the bear case [Certain]. The macro overlay finds that rising real yields and credit spreads add to this downside skew [Likely].

## Bull case
The recovery is real. TTM ROIC of 8.5% is up from 3.7% in FY2025, operating margin has improved to 3.6%, and the Piotroski F-score is 7 [Certain]. EV/EBITDA of 10.0x is in line with peers (+1%) and below its own 5y median of 10.9x, so the stock is not expensive on the measure the fair-value model uses [Certain]. The industry is cutting capacity because of fuel costs, which supports fares [Likely]. A smaller share count means any earnings recovery adds more per share [Certain]. If Q3 results on Oct 21 show positive FCF, the stock could re-rate toward the 47.07 bull fair value [Guessing]. Short interest is low (4.56%) and falling [Certain].

## Decision
```json
{
  "ticker": "LUV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-moat domestic airline with negative free cash flow, debt-funded buybacks and unhedged fuel, trading at only 2.1% below its base fair value, offers no margin of safety for a 12-month core holding.",
  "rationale": "Core requires a good business at an attractive price; LUV is neither. FCF negative since FY2022, leverage rising to fund buybacks, P/B above its 5y range, and base fair value barely above price against -31.7% bear downside. Macro overlay tilts further toward bear. Conviction 2, so no position.",
  "price_at_decision": 41.66,
  "price_date": "2026-10-09",
  "research_note": "research/LUV/2026-10-12.md",
  "triggers": [
    {"text": "FCF margin turns positive on a TTM basis, ending the negative free-cash-flow run since FY2022.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 0}},
    {"text": "ROIC rises above 10.0% TTM (its FY2022 level), showing returns are structurally improving and not just a cyclical bounce.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "Net debt/EBITDA falls back toward net cash (below 0x, as in FY2022-FY2024), showing buybacks are no longer funded with debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 47.07, "basis": "Positive FCF and ROIC above 8.5% TTM [RA] lift EV/EBITDA toward the upper part of its own history: the bull fair value of 47.07 [IS,RA,ST], given a lower probability per the macro overlay's moderate bear tilt (research/LUV/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 42.52, "basis": "EV/EBITDA stays near its current 10.0x, close to the 10.9x 5y median [RA] on TTM EBITDA: the base fair value of 42.52 [IS,RA,ST], about where the stock trades today."},
    "bear": {"probability": 0.35, "target_price_12m": 28.47, "basis": "Unhedged fuel and negative FCF (-1.4% TTM [CF,IS]) compress EV/EBITDA toward its 7.7x 5y low [RA]: the bear fair value of 28.47; the probability is raised per the macro overlay's moderate bear tilt from rising real yields and HY spreads (research/LUV/2026-10-12-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
