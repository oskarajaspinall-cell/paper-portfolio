# Evaluation: Macronix International Co., Ltd. (TPE:2337) — 2026-11-16
## Bear case
Macronix is a memory-cycle price-taker, not a compounder: three loss-making fiscal years (ROIC -4.5%, -6.8%, -6.5%) sit inside five years, so the TTM ROIC of 31.2% and gross margin of 57.7% are peak-cycle figures [Likely]. The 12-month direction change (operating margin -18.7% to 38.1%) is a price-cycle upswing, not a structural improvement, and can reverse as fast [Likely]. A P/E of 7.1x on peak earnings is the classic cyclical trap; P/E and P/B both sit above their five-year maxima [Certain]. The price has fallen 41.7% in 3 months and sits 36.0% below its 200-day average with no news explaining it, consistent with the market discounting a downturn [Likely]. The mechanical fair value base of 59.61 TWD is below the 79.60 close, though flagged unreliable [Certain]. Shares rose 7.29% YoY: dilution, not buybacks [Certain]. Net debt/EBITDA reached 19.72x in FY2024 in the last trough [Certain].
## Bull case
The upswing is real cash, not just accounting: TTM FCF margin is 37.6% and FCF yield 16.22%, with FCF conversion of 114.8% [Certain]. The balance sheet is now net cash (net debt/EBITDA -0.30x), Piotroski F is 7 and Altman Z 4.94, so a downturn is survivable [Certain]. EV/EBITDA of 4.7x is at the bottom of its five-year range and P/FCF of 6.2x sits below its five-year minimum and below the 8.8x peer median [Certain]. If memory pricing holds longer than the market fears, the 52.6% six-month fall leaves room for a re-rating toward the EV/EBITDA method's base of 136.43 TWD [Guessing]. The 12-month change is still +95.8% [Certain].
## Decision
```json
{
  "ticker": "TPE:2337",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all rising (fact sheet Recent direction); the 5-year fiscal decline reflects the FY2023-FY2025 memory downturn, now reversed.", "moat": "none", "key_risk": "high", "key_risk_text": "Peak-cycle memory earnings roll over: TTM margins are far above the five-year norm and the price's 41.7% 3-month fall suggests the market expects a downturn.", "veto": null},
  "thesis": "A commodity memory maker at peak-cycle margins with no moat and a broken price trend; cheap trailing multiples do not compensate for the cycle risk.",
  "rationale": "No moat through the cycle (three loss years in five), current profits likely peak, price far below its 200-day average so no trend strength, and the blended fair value base sits below the price. Cheap EV/EBITDA and P/FCF are on peak cash flows. Good but not compelling: AVOID.",
  "price_at_decision": 79.60,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2337/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, signalling the memory upswing is ending.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM operating margin falls below 20%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt / EBITDA rises above 1.5x on the balance sheet and ratios pages."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 136.43, "basis": "Memory pricing holds and EV/EBITDA stays near the current 4.7x on TTM EBITDA, matching the EV/EBITDA method's base of 136.43 TWD (fact sheet Fair value, RA)."},
    "base": {"probability": 0.45, "target_price_12m": 59.61, "basis": "Margins normalise from the TTM peak toward the five-year record, in line with the blended mechanical base fair value of 59.61 TWD (fact sheet Fair value, IS/CF/RA), though that range is flagged unreliable."},
    "bear": {"probability": 0.35, "target_price_12m": 21.20, "basis": "A memory downturn like FY2023-FY2025 returns ROIC to negative, priced at the through-cycle DCF base of 21.20 TWD (fact sheet Fair value, RA)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: peak-cycle earnings, no moat through the cycle and an unexplained price collapse mean a lower price alone would not lift this to conviction 4; the fair value range is unreliable (methods 6.4x apart).",
  "replaces": null,
  "replacement_reason": null
}
```
