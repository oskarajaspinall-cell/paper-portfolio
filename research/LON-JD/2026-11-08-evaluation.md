# Evaluation: JD Sports Fashion Plc (LON:JD) — 2026-11-08
## Bear case
Returns are falling, and the last year confirms it. ROCE fell 2.2pp in 12 months to 11.6%, and operating margin is 7.0%, 2.2pp below its 2-year high of 9.3% [RA-T, IS-T] [Certain]. The cause is company-specific: management cut full-year profit guidance in August on pricing pressure and weak US sales, and first-half profit then fell 19.7% (Reuters 2026-09-23) [Certain]. JD resells other companies' brands and depends on Nike's turnaround, so its moat is thin [Likely]. The FCF margin rose to 8.4%, but that is working capital and lease depreciation (conversion 189.7%), not better economics, so the rise does not offset the margin fall [Likely]. Net debt/EBITDA rose from 0.87x to 2.32x [Certain]. The shares are up 40.2% in six months, so some recovery is already priced [Certain]. Beta is 1.65 [Certain]. There is no fair-value anchor [Certain].
## Bull case
The price already assumes decline. P/E is 8.4x, below its 5y minimum of 9.3x. EV/EBITDA is 4.3x, under its 5.7x low. P/FCF is 4.3x, a 23.38% FCF yield [RA, ST] [Certain]. The full-year outlook was maintained at the half-year despite North American weakness (Reuters 2026-09-23) [Certain]. Piotroski F is 7, and shares outstanding fell 3.37% YoY on buybacks [ST] [Certain]. If margins merely stabilise near 7.0%, that cash flow supports a re-rating toward the 5y EV/EBITDA median of 6.3x [Guessing]. A recovery at Nike, JD's main supplier, would lift full-price sell-through [Guessing]. The new chair adds governance renewal [Likely]. Macro is context only: the GBP/USD move is small (overlay) [Certain].
## Decision
```json
{
  "ticker": "LON:JD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deeply discounted multi-brand sportswear retailer whose cheapness reflects falling returns, a guidance cut and rising leverage rather than a mispriced quality franchise.",
  "rationale": "Valuation is very low, but ROCE, ROIC and operating margin are all still falling on a rolling basis after a profit-guidance cut. Leverage is rising, the moat is thin as a reseller dependent on Nike, and there is no fair-value anchor. Good but not compelling: until margins stabilise, conviction is 3, so no position.",
  "price_at_decision": 95.34,
  "price_date": "2026-11-06",
  "research_note": "research/LON-JD/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 8.5% (the level a year earlier; 7.0% now), showing the US pricing pressure has passed.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 8.5}},
    {"text": "TTM ROIC rises back above its 2-year high of 12.6% (11.0% now), showing returns have stopped eroding.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 12.6}},
    {"text": "A company release reports North American like-for-like sales returning to growth while net debt/EBITDA on the ratios page falls back below 2.0x (2.32x now)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 130.0, "basis": "Margins stabilise near the TTM 7.0% [IS] on the maintained full-year outlook (Reuters 2026-09-23), and EV/EBITDA re-rates from 4.3x toward its 5y minimum of 5.7x [RA]; the fact sheet has no fair value to reconcile against (no GBP FX rate)."},
    "base": {"probability": 0.45, "target_price_12m": 95.0, "basis": "Operating margin drifts but stays near 7.0% [IS-T] and the stock holds its below-range 8.4x P/E [RA], with buybacks (shares -3.37% YoY [ST]) offset by leverage at 2.32x [BS]; macro is context only (research/LON-JD/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 68.0, "basis": "The rolling decline continues (ROCE down 2.2pp in 12 months [RA-T]) as US weakness and pricing pressure persist after the August guidance cut (Reuters 2026-08-20), so earnings fall at a constant low multiple, back toward the 63.98 52-week low [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the shares already trade below their own 5y minimum P/E and EV/EBITDA, and the blocker is deteriorating returns and margins after a guidance cut. A lower price would not change the decision; stabilising margins (the triggers) would.",
  "replaces": null,
  "replacement_reason": null
}
```
