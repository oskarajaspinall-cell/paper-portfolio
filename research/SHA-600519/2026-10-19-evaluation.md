# Evaluation: Kweichow Moutai Co., Ltd. (SHA:600519) — 2026-10-19
## Bear case
The cycle has turned: FY2025 brought the first annual revenue and profit decline on record, and 1H2026 showed a further net-profit drop (CNBC, https://www.cnbc.com/2026/08/19/china-economy-moutai-ai-property.html) [Likely]. ROIC has fallen from 51.1% in FY2024 to 37.3% TTM, and gross, operating and net margins are all at five-year lows on a TTM basis [Certain] [RA, IS]. Yet the reverse DCF still prices 11.1% revenue growth in year one [Certain], a bar a shrinking top line does not clear [Likely]. "Cheap vs own history" is relative to a bubble-era 5y median of 29.0x P/E; against peers it is still dear (P/E +45%, EV/EBITDA +70%) [Certain] [RA]. The base fair value of 1,398.49 sits barely above the 1,329.00 close, while the bear value is 701.59 [Certain]: an asymmetric skew to the downside. State-fund selling and domestic rotation into AI are a persistent flow overhang (SCMP) [Likely]. Piotroski F of 4 confirms deteriorating momentum [Certain] [ST].

## Bull case
This is still one of the world's best franchises: 90.3% gross margin, 64.5% operating margin, 33.0% ROE, net cash (net debt/EBITDA -0.49x) [Certain] [IS, RA]. Every multiple sits below its own five-year minimum, P/FCF is 14.2x against a 21.8x floor, and the FCF yield is 7.03% [Certain] [RA, ST]. TTM FCF conversion of 143.3% shows cash generation intact despite the profit dip [Certain] [CF]. Scarcity from multi-year ageing and fixed release supports pricing power through the downturn [Likely]. The EV/EBITDA method values it at 1,904.91 base, and even its bear of 1,371.42 sits above the price [Certain]. Beta of 0.34 and a falling share count add defensiveness [Certain] [ST]. If demand stabilises, a re-rating from trough multiples is plausible [Guessing].

## Decision
```json
{
  "ticker": "SHA:600519",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A world-class, net-cash spirits franchise at five-year-low multiples, but with revenue and profit now declining, the price still implies double-digit growth and the base fair value offers little margin of safety.",
  "rationale": "Quality and cash generation are exceptional and multiples are at five-year lows, but fundamentals are deteriorating, peers are far cheaper, the reverse DCF demands growth the business is not delivering, and base fair value barely exceeds the price. Good but not compelling: conviction 3, no position; wait for a margin of safety.",
  "price_at_decision": 1329.00,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600519/2026-10-19.md",
  "triggers": [
    {"text": "TTM gross margin falls below 88%, signalling discounting or channel stuffing that erodes pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 88}},
    {"text": "TTM ROIC falls below 30%, under the FY2021 level of 38.1%, showing the moat eroding rather than normalising from the FY2024 peak.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM net margin falls below 45%, confirming the 1H2026 profit drop is structural.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}},
    {"text": "Annual revenue (income statement) declines for a second consecutive full year, confirming a structural demand problem rather than destocking."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 1686.52, "basis": "Demand stabilises and margins hold near 90.3% gross [IS], lifting value to the mechanical bull fair value of 1,686.52 as multiples recover from below their 5y minimum [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 1398.49, "basis": "Earnings ease further but the 7.03% FCF yield [ST] and five-year-low multiples [RA] cap de-rating, leaving the stock near the blended base fair value of 1,398.49."},
    "bear": {"probability": 0.3, "target_price_12m": 1145.27, "basis": "A second annual revenue decline (CNBC, https://www.cnbc.com/2026/08/19/china-economy-moutai-ai-property.html) drives the price to the DCF base of 1,145.27; above the mechanical bear 701.59 because net cash and a 0.34 beta [ST] limit a full DCF-bear collapse."}
  },
  "entry_price": 1118.79,
  "entry_basis": "valuation file: base 1,398.49 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
