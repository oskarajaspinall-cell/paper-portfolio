# Evaluation: Rorze Corporation (TYO-6323) — 2026-10-11
## Bear case
The edge in a drift trade is a real results beat, and the beat was never verified: the Q2 FY2027 filing text could not be read, so revenue and margin delivery are unknown [Certain]. Volume and a held gap show that buyers came in, but they don't explain why [Likely]. The stock is already stretched: RSI 77.3, +29.5% above its 50-day, and P/E 37.1x and EV/EBITDA 19.1x are above their 5y maxima of 30.3x and 14.6x [Certain]. The 6,286.79 target is just the 2:1 minimum, set about 21% above the 5,199 52-week high with nothing to support it [Certain]. With beta 1.60 [Certain] and US real yields up 0.56pp in 3 months (macro overlay), a crowded, high-multiple name risks a gap back through the 4,557.61 stop [Likely].
## Bull case
A +15.8% close on 5.2x volume the session after the results, with 100% of the jump held, is the classic drift signature [Certain]. The trend behind it is strong: +113.9% over 12 months, +42.5pp relative strength vs SPY over 6 months, and the 50-day 9.0% above the 200-day [Certain]. The quality of the business supports a re-rating: TTM gross margin 42.5% is rising, operating margin 26.6%, ROIC 28.0%, net cash (-1.24x net debt/EBITDA), and Altman Z 8.10 [Certain]. Fab-automation demand could keep upgrades coming [Guessing]. The stock sits at its 52-week high, so no overhead supply from a prior range [Likely].
## Decision
```json
{
  "ticker": "TYO:6323",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A strong, volume-confirmed post-results gap in a high-quality fab-automation name, but the beat itself is unverified and the only target is the mechanical 2:1 minimum far above any tested level.",
  "rationale": "The setup has a clean signature but its edge is unproven: the beat could not be read from the filing, the stock is overbought (RSI 77.3) and above its 5y multiple maxima, and the 6,286.79 target has no evidence behind it. The macro tilt toward bear (real yields) adds gap risk. Conviction 3 is below the buy bar, so AVOID.",
  "price_at_decision": 5134.0,
  "price_date": "2026-10-09",
  "research_note": "research/TYO-6323/2026-10-11.md",
  "exit_plan": {"target": 6286.79, "stop": 4557.61, "time_limit": "2026-12-04"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6286.79, "basis": "The drift completes and the stock holds its premium on rising quality (TTM gross margin 42.5%, ROIC 28.0% [IS,RA]), reaching the 2:1 level above the 5,199 52-week high [HI]; this is above the fair-value bull of 4,319.90 because the model is blind to the current upcycle."},
    "base": {"probability": 0.45, "target_price_12m": 4234.0, "basis": "P/E de-rates from 37.1x to the 30.6x peer median [RA,P] on flat TTM earnings, close to the fair-value bull of 4,319.90 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.30, "target_price_12m": 2011.28, "basis": "Multiples revert toward the 5y medians (P/E 14.4x, EV/EBITDA 10.7x [RA]), matching the fair-value base of 2,011.28; bear weight raised slightly per the macro overlay's small 'toward bear' tilt (DFII10 +0.56pp/3m, research/TYO-6323/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the trade's edge depends on the unverified content of the Q2 FY2027 beat. A lower price would break the drift setup by moving through the 4,557.61 stop instead of offering a better entry, and as a core name the stock trades far above base fair value 2,011.28.",
  "replaces": null,
  "replacement_reason": null
}
```
