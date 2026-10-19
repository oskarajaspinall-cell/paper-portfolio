# Evaluation: Shanghai Allist Pharmaceuticals Co., Ltd. (SHA:688578) — 2026-10-19
## Bear case
The market is pricing an earnings reset we cannot see. The stock fell from 138.30 to a low of 75.55 CNY, -34.1% over 3 months, with no company headline to explain it [Certain] [HI, OV]. When a cash-rich, high-margin drug company de-rates to below its 5y minimum on every multiple, the usual reason is a known threat to its main product: China volume-based procurement, competition or loss of exclusivity [Guessing]. We cannot test that, because product mix, patent life and pipeline are [data unavailable], and the rNPV method fails for the same reason [Certain]. TTM ROIC has already slipped to 52.1% from 76.0% in FY25 [Certain] [RA]. Q3 results are due Oct 28, 2026, so the gap risk is immediate [Certain] [ST]. Fair value rests on EV/Revenue alone, which assumes revenue holds [Certain]. Low institutional ownership (16.1%) adds a persistent liquidity discount [Likely] [ST].
## Bull case
On the reported numbers this is exceptional quality at a distressed price. Gross margin has held at 94.0-96.8% for five years, operating margin is 43.5% TTM and FCF conversion is 95.1% [Certain] [IS, CF]. The balance sheet holds net cash (net debt/EBITDA -1.56x) and dilution is minimal at 0.34% [Certain] [RA, ST]. At 13.8x P/E, 14.4x P/FCF and a 6.92% FCF yield, it trades below its own 5y minimums and far below peers on 75.5x P/E [Certain] [RA]. Even the mechanical bear fair value of 100.83 CNY is above the price [Certain]. If Q3 shows the franchise intact, the de-rating reverses toward the 5y range [Likely]. The macro overlay says the fall was stock-specific, not a macro shock [Likely].
## Decision
```json
{
  "ticker": "SHA:688578",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, ~96% gross-margin China drug franchise trading below its 5y multiple range, but an unexplained one-third de-rating ahead of Q3 results means its earnings durability cannot be verified.",
  "rationale": "The multiples are compelling, but the market is clearly discounting something product-specific (procurement, competition or exclusivity) that the available data cannot test: no product mix, patent or pipeline data, and rNPV is unavailable. With Q3 results due in nine days, buying blind would mean guessing at the core risk. That is conviction 3, so AVOID; Q3 results decide.",
  "price_at_decision": 81.79,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-688578/2026-10-19.md",
  "triggers": [
    {"text": "Gross margin falls below 90%, signalling pricing pressure (procurement/competition) on the patented franchise", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 90}},
    {"text": "ROIC falls below 30%, showing the FY23-25 step-up in returns was not durable", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Operating margin falls below 30%, indicating an earnings reset in the core drug franchise", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM revenue growth turns negative in the Q3 2026 or later reports (income statement), indicating the franchise is losing share"}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 112.0, "basis": "Q3 confirms the franchise intact and P/E re-rates to its 5y minimum 18.9x [RA] on TTM earnings [IS]; below the EV/Revenue base fair value 123.66 because that single method ignores the product risk the price signals."},
    "base": {"probability": 0.4, "target_price_12m": 85.0, "basis": "Earnings hold near TTM levels but the unexplained de-rating persists at about 13.8x P/E [RA] given low 16.1% institutional ownership [ST]; below the mechanical bear fair value 100.83 because EV/Revenue assumes revenue is safe."},
    "bear": {"probability": 0.3, "target_price_12m": 60.0, "basis": "The drawdown proves to be a product-level hit (procurement or competition, per the Bear case) and earnings reset lower, as the ROIC slide from 76.0% to 52.1% [RA] may foreshadow, taking the price below the 75.55 low [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every fair-value case. The obstacle is an unexplained de-rating and missing product, patent and pipeline data; a lower price would not change the decision, only the Q3 2026 results (Oct 28, 2026) showing revenue and margins intact would.",
  "replaces": null,
  "replacement_reason": null
}
```
