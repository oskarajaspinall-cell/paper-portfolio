# Evaluation: Apple Inc. (AAPL) — 2026-10-10
## Bear case
The price already capitalises perfection. P/E 38.6x, EV/EBITDA 28.9x and EV/Sales 10.4x all sit above their own 5y maxima and 30-73% above peers [Certain]. The reverse DCF needs 31.5% year-1 revenue growth, far beyond anything Apple has delivered [Certain]. Even the mechanical bull fair value (174.96) is 48.0% below the 336.64 close [Certain]. The catalyst path runs the wrong way: reports of ~15% iPhone 18 Pro component-order cuts after a price rise point to softer units into the Nov 2 print [Likely]. Real yields are up +0.56pp in 3 months, almost all real, which hits long-duration premium multiples first (macro overlay) [Certain]. FCF yield of 2.78% offers little cushion if the multiple merely reverts to its 5y median 20.8x EV/EBITDA, roughly the EV/EBITDA-leg fair value of 240.81 [Likely].

## Bull case
This is one of the highest-quality franchises listed: TTM ROIC 101.6%, gross margin up to 48.7% from 41.8% and operating margin to 33.2%, all rising over five years [Certain]. The Services mix shift explains why margins and returns now justify a higher multiple than the 2021-2025 range [Likely]. Shares fell 2.12% YoY on buybacks funded by 106.0% FCF conversion, with immaterial leverage and Piotroski 8 [Certain]. P/FCF of 35.9x is 30% below the peer median, so on cash the premium is less extreme [Certain]. One product cycle's order cut is not moat erosion, and new MacBook/iPad launches plus AI optimism could keep the multiple elevated [Guessing]. Relative strength vs SPY is +14.8pp over 12 months [Certain].

## Decision
```json
{
  "ticker": "AAPL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Apple's rising 100%+ ROIC and margin expansion make it an elite franchise, but at multiples above their own 5-year maxima and an implied 31.5% year-1 growth rate, the price leaves no margin of safety into a softening iPhone 18 cycle.",
  "rationale": "Quality is not in doubt; price is. Every earnings multiple is above its 5y max and the reverse DCF demands growth Apple has never shown, while iPhone 18 order cuts and rising real yields skew 12-month risk down. Good but not compelling: AVOID, watch for multiples back near their 5y median.",
  "price_at_decision": 336.64,
  "price_date": "2026-10-09",
  "research_note": "research/AAPL/2026-10-10.md",
  "triggers": [
    {"text": "TTM gross margin falls below 44%, the FY2023 level, showing pricing power or Services mix is reversing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 44}},
    {"text": "TTM operating margin falls below 29.8%, the FY2021/FY2023 five-year low, erasing the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 29.8}},
    {"text": "TTM ROIC falls below 70%, under the FY2022 five-year low of 73.6%, signalling ecosystem economics are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 70}},
    {"text": "TTM net margin falls below 24%, the FY2024 low, evidencing a structural profitability reset.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 24}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 370, "basis": "Rising ROIC (101.6%) and gross margin (48.7%) [RA,IS] plus buybacks (-2.12% shares [ST]) sustain the premium near today's 38.6x P/E with earnings growth; probability cut by the macro overlay's small bear tilt (research/AAPL/2026-10-10-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 305, "basis": "EV/EBITDA eases from 28.9x to its 5y max 26.0x [RA] as iPhone 18 order cuts (marketwatch.com URL in note) cap upgrades; above the mechanical base 155.60 because the DCF leg ignores the improved margin/ROIC profile."},
    "bear": {"probability": 0.35, "target_price_12m": 240.81, "basis": "Multiples revert to the 5y median 20.8x EV/EBITDA [RA], i.e. the EV/EBITDA-leg base fair value 240.81 [fact sheet]; probability raised by the macro overlay's small bear tilt as real yields rose +0.56pp/3m (research/AAPL/2026-10-10-macro.md)."}
  },
  "entry_price": 240.81,
  "entry_basis": "EV/EBITDA-leg base fair value 240.81 [fact sheet], i.e. EV/EBITDA back at its 5y median 20.8x [RA]; preferred over base 155.60 x 0.8 because the DCF leg (112.99) understates a 100%+ ROIC franchise with rising margins.",
  "replaces": null,
  "replacement_reason": null
}
```
