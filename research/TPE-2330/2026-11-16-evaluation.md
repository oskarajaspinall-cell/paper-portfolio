# Evaluation: Taiwan Semiconductor Manufacturing Company Limited (TPE:2330) — 2026-11-16
## Bear case
The price already assumes the AI build-out keeps compounding: the reverse DCF needs 43.1% year-1 revenue growth, EV/EBITDA 15.0x, EV/Sales 11.0x and P/B 8.2x all sit above their own 5y maxima, and the FCF yield is only 2.58% [Certain]. The mechanical base fair value of 905.97 TWD is far below the 2,350.00 close [Certain]. The model fades growth from history and understates this business, but even its bull case of 1,729.27 sits below the price [Certain]. TTM margins are at peaks: operating margin 58.0% against a FY2023 trough of 42.6%, ROIC 60.3% against 32.0% [Certain]. If AI capex slows, a key customer's leadership turmoil spreads or chip sentiment keeps falling, an extended price risks a de-rating on top of cyclically lower earnings [Likely]. Taiwan geopolitics and US export policy are unhedgeable tail risks, and the US revenue share is unverified [Guessing].

## Bull case
The best-quality franchise in semiconductors, and still improving: ROIC 60.3% TTM, up 13.2pp in a year; operating margin 58.0%, up 8.4pp; gross margin 65.8%; FCF margin 29.9% [Certain]. Nothing in the rolling-12-month table is falling [Certain]. Net cash (net debt/EBITDA -0.89x), no dilution and Piotroski F 7 [Certain]. A near-monopoly in leading-edge AI-chip manufacturing, with challengers such as Rapidus still unproven (https://www.fool.com/investing/2026/11/14/why-a-rising-tsmc-challenger-could-reshape-the-chi/) [Likely]. P/E 22.7x is below its 5y median 23.7x and 20% below the peer median 28.3x, so earnings growth, not multiple expansion, has driven the 54.9% 12-month gain [Certain]. The trend is healthy: 5.9% above the 200-day average, RSI 38.8 after a sector sell-off, not overextended [Certain]. A weaker TWD is a modest tailwind (macro overlay, context only) [Likely].

## Decision
```json
{
  "ticker": "TPE:2330",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No ROIC, operating margin or FCF margin decline: rolling-12-month ROIC +13.2pp, operating margin +8.4pp, FCF margin +5.4pp [RA-T, IS-T, CF-T].",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "An AI capex slowdown cutting peak margins while the price sits above its own 5y EV/EBITDA, EV/Sales and P/B maxima, so earnings and the multiple fall together; Taiwan geopolitics is the tail risk.",
    "veto": null
  },
  "thesis": "The world's leading-edge foundry, with record and still-rising returns and net cash, is priced for continued AI-driven compounding, with multiples above their own 5y ranges and a thin FCF yield.",
  "rationale": "Quality is exceptional and improving, but the price leaves no margin of safety: the mechanical fair value, even its bull case, sits below the close and several multiples exceed their 5y maxima. The scorecard does not reach the buy bar; a good business at a full price is an AVOID, and cash is acceptable.",
  "price_at_decision": 2350.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2330/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 40%, giving up most of the climb from the FY2023 low of 32.0% and signalling the AI pricing power is fading.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM operating margin falls below 50%, back under the FY2025 level of 50.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 20%: capex absorbing cash flow without matching revenue.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 56.1%, signalling leading-edge pricing or utilisation is slipping.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3000, "basis": "Margins keep expanding (TTM operating margin 58.0% and rising [IS-T]) and P/E moves toward its 5y max of 26.9x [RA]; above the mechanical bull because the model fades growth from history and misses the margin step-up (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 2450, "basis": "P/E holds near its 5y median 23.7x [RA] on modestly higher earnings; above the mechanical base of 905.97 [valuation] because that through-cycle DCF ignores the improved returns (ROIC 60.3% TTM [RA-T])."},
    "bear": {"probability": 0.30, "target_price_12m": 1500, "basis": "An AI capex pause takes margins toward the FY2023 trough (operating margin 42.6% [IS]) and EV/EBITDA back to its 5y median 13.5x [RA]; still above the mechanical bear of 482.10, which assumes a deeper reset than the net-cash balance sheet implies."}
  },
  "entry_price": 1500,
  "entry_basis": "Not the default valuation file anchor (base 905.97 x 0.8), which the model's growth fade makes meaningless for this business; instead our bear scenario target, where the value blend would show a discount and P/E and EV/EBITDA would sit in the lower third of their 5y ranges [RA], earning the valuation points the scorecard needs for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
