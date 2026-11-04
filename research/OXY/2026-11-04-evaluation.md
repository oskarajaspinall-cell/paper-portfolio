# Evaluation: Occidental Petroleum Corporation (OXY) — 2026-11-04
## Bear case
The fall that hit our entry price has no company-specific cause: no negative headline since 2026-10-26, and the note's best explanation is a crude move ahead of Q3 results on Nov 9, 2026 [Guessing]. That is the problem. OXY is a price-taker with cyclical returns: ROIC went from 26.1% in FY2022 to 4.3% in FY2025 [RA] [Certain]. The cheap P/E of 8.9x rests on a TTM net margin of 30.3% that includes the OxyChem gain and an Iran/Hormuz risk premium in crude [Likely]. On cash, the stock is not cheap: P/FCF of 13.3x is above its 5y maximum of 10.6x [RA] and FCF margin has fallen from 29.1% to 18.9% [CF,IS] [Certain]. Shares grew 1.82% YoY [ST] [Certain]. If the geopolitical premium fades, FCF falls and the multiple offers little cushion [Likely]. The fair value model is unavailable, so there is no mechanical anchor [Certain].
## Bull case
Deleveraging is real: net debt/EBITDA fell to 0.76x TTM from 1.90x in FY2025 after OxyChem proceeds repaid debt [company-reported] [Certain]. Gross margin is rising, 73.3% TTM, and Piotroski F is 7 [Certain]. EV/EBITDA of 5.2x sits at 31% of its 5y range and below the peer median of 7.6x; P/B and P/FCF are also below peers [RA] [Certain]. Management guides flat 2027 spending and output with debt reduction first, so more FCF can flow to equity and the dividend, raised to $0.28 [company-reported] [Likely]. Q3 realized oil prices rose year on year [Likely]. The uptrend is intact: the price is above its 200-day average and up 43.0% over 12 months [Certain]. A balance sheet this clean makes OXY a lower-risk way to hold crude exposure [Likely].
## Decision
```json
{
  "ticker": "OXY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged Permian producer that is cheap on peak-like earnings but not on free cash flow, so the stock's value depends on crude holding its geopolitical premium rather than on a durable business edge.",
  "rationale": "The dip has no company-specific cause, but it does not change the evidence. P/FCF is above its 5y high, earnings are inflated by a one-off gain and elevated crude, ROIC is cyclical and Q3 results are days away. The balance sheet is clean but the setup is good, not compelling. Conviction 3, so AVOID.",
  "price_at_decision": 60.43,
  "price_date": "2026-11-03",
  "research_note": "research/OXY/2026-11-04.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 1.9x (0.76x TTM now), reversing the post-OxyChem deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.9}},
    {"text": "TTM FCF margin falls below 12% (18.9% now), showing cash generation cannot support debt reduction and the dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM gross margin falls below 65% (73.3% now), showing the cost and realization gains have reversed.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 65}},
    {"text": "Management reverses the flat 2027 spending and output plan or the debt-reduction priority in a filing or results release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 70.0, "basis": "EV/EBITDA moves from 5.2x toward its 5y median of 6.2x [RA] on TTM EBITDA as net debt/EBITDA stays at 0.76x [RA] and crude holds its premium; set by hand because the fact sheet's fair value is unavailable (FRED fetch failed)."},
    "base": {"probability": 0.45, "target_price_12m": 58.0, "basis": "Flat 2027 output and spending (https://www.reuters.com/business/energy/occidental-sees-flat-spending-output-2027-keeps-focus-debt-reduction-2026-08-06/) with the OxyChem gain dropping out of TTM earnings keeps the multiples near today's levels, around the 50-day average of 60.18 [ST]; no mechanical fair value to reconcile."},
    "bear": {"probability": 0.30, "target_price_12m": 42.0, "basis": "The Iran/Hormuz premium fades (Q2 10-Q) and P/FCF of 13.3x falls back toward its 5y median of 8.4x [RA] on lower FCF, near the 52-week low of 38.80 [HI]."}
  },
  "entry_price": 48.2,
  "entry_basis": "Fair value unavailable, so anchored on cash flow instead: P/FCF back at its 5y maximum of 10.6x [RA] (13.3x now) on TTM FCF, the level at which the cash yield would justify conviction 4 despite cyclical earnings.",
  "replaces": null,
  "replacement_reason": null
}
```
