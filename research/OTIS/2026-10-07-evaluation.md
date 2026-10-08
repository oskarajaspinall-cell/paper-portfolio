# Evaluation: Otis Worldwide Corporation (OTIS) — 2026-10-07

## Bear case
The de-rating hits the crown jewel. Service earns 91% of segment profit, and Q2 2026 service margin fell 170bp on labour and material inflation, forcing a FY2026 operating-profit guidance cut [Certain]. If that inflation is structural, "below 5y min" multiples are a reset, not a bargain [Guessing]. Leverage is drifting up: net debt/EBITDA 3.04x TTM vs 2.62x FY2021, while FCF conversion fell from 127.9% to 112.9% [Certain]. Buybacks (-2.55% shares) are partly debt-funded in effect, and ROE/P/B are unavailable because equity is negative [Likely]. The CEO retires with no successor until H1 2027, and Q3 results land on Oct 28 with momentum still negative (-27.4% 12m, -14.6% vs 200-day MA) [Certain]. The macro overlay adds a small bear tilt: rising real yields, wider HY spreads and a stronger dollar hit the multiple and FX translation [Likely].

## Bull case
This is a recurring, ~2.5m-unit service annuity with ROIC of 65.3% TTM, still rising over five years, and operating margin of 16.6% that is still near its 5-year high [Certain]. At 66.45 the stock trades at 17.1x P/E, 12.6x EV/EBITDA and 14.8x P/FCF. That is below every 5-year minimum (22.5x / 16.4x / 22.6x) and 19-39% below peers [Certain]. The 6.77% FCF yield funds the dividend and buybacks [Certain]. The price implies the margin squeeze is permanent. Yet TTM FCF margin (11.5%) is actually above FY2025 (10.0%), and management points to modernization backlog +26% YoY and AI-driven pricing [Likely]. Even a partial re-rating toward the 5-year P/E floor gives a strong return, and low beta (0.86) plus Altman Z 3.11 limit the downside [Likely].

## Decision
```json
{
  "ticker": "OTIS",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A service-led elevator franchise with 65% ROIC trades below its own 5-year minimum on every multiple at a 6.77% FCF yield, pricing a transitory service-margin squeeze and CEO transition as permanent impairment.",
  "rationale": "The valuation gap to its own 5-year floor and to peers far exceeds the guided profit cut, and the recurring service base protects the downside. The service-margin squeeze, rising leverage, the CEO transition and a small macro bear tilt cap conviction at 4: 7% core size. This would be the first Industrials holding, and cash covers it.",
  "price_at_decision": 66.45,
  "price_date": "2026-10-06",
  "research_note": "research/OTIS/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2021 5-year low of 15.2%, showing the service-margin squeeze is structural, not transitory.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15.2}},
    {"text": "TTM FCF margin falls below the FY2025 5-year low of 10.0%, showing cash generation is deteriorating with margins.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "Service operating margin (earnings release) falls below 20% for two consecutive quarters, vs 23.2% in Q2 2026, or modernization backlog growth turns negative."}
  ],
  "exit_plan": null,
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 87.0, "basis": "Service margins recover and the P/E re-rates to its 5y minimum of 22.5x [RA] on TTM earnings, still below the 28.1x peer median [P:peers]; probability trimmed for the overlay's small bear macro tilt (research/OTIS/2026-10-07-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 73.0, "basis": "Multiples stay below their 5y range (P/E 17.1x [RA]) and returns come from modest earnings growth plus the 6.77% FCF yield [ST] recycled into buybacks (-2.55% shares [ST])."},
    "bear": {"probability": 0.25, "target_price_12m": 56.0, "basis": "Service-margin inflation persists past Q3 (note §2), EBITDA falls while EV/EBITDA stays near 12.6x [RA] and leverage rises above 3.04x [RA]; probability raised for the overlay's small bear macro tilt from rising real yields and the dollar (research/OTIS/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
