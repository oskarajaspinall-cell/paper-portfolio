# Evaluation: General Mills, Inc. (GIS) — 2026-10-12
## Bear case
FY2026 broke the franchise's earnings pattern: net margin fell to -0.5% (TTM -4.9%), ROE to -1.0% (TTM -10.5%) and FCF margin to 8.5% TTM from a 10.4–14.5% range [Certain]. The cause isn't shown, so we can't say it was a one-off write-down [Guessing]. Operating margin has slid from 19.0% to 15.6% while net debt/EBITDA rose from 2.83x to 3.86x [Certain]. That points to pricing power under pressure in a weak consumer environment, not just a cyclical dip [Likely]. Against peers GIS isn't cheap: P/FCF is 35% above and EV/EBITDA 7% above the peer median [Certain]. Piotroski 4, Altman Z 2.38 and 8.42% short interest all point the same way [Certain]. The macro overlay flags a real-rate rise of +56bp in 3 months hitting a levered issuer while it refinances [Certain]. A new CEO arrives in the middle of this [Certain].
## Bull case
On its own history GIS is at trough multiples: EV/EBITDA 8.9x and EV/Sales 1.7x are both below their 5y minimums, and P/FCF of 11.2x sits at the floor [Certain]. The FCF yield is 8.96% [Certain]. Gross margin has stayed flat at 33.7%, within its five-year band, so the brands still hold price [Certain]. TTM ROIC of 13.8% suggests the FY2026 loss was largely non-cash [Likely]. The reverse DCF implies -5.4% revenue growth, so the price already assumes decline [Certain]. Base DCF fair value of $48.97 is +51.6% above the price [Certain]. Shares are shrinking 2.80% a year, the $0.61 dividend was just reaffirmed and the note tenders show active liability management [Certain]. An insider CEO keeps the plan continuous [Likely].
## Decision
```json
{
  "ticker": "GIS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A branded-foods franchise at trough own-history multiples and a 8.96% FCF yield, but with falling margins, FCF and returns and leverage rising to 3.86x, so cheapness is not yet backed by stabilising fundamentals.",
  "rationale": "Cheap against its own history but not against peers. Operating margin, FCF margin and net income are all deteriorating, leverage is rising and the FY2026 loss is unexplained. The macro overlay adds refinancing and discount-rate risk. A good-but-not-compelling setup is an AVOID; conviction 4 needs evidence that margins and cash flow have stabilised, not a lower price.",
  "price_at_decision": 32.29,
  "price_date": "2026-10-09",
  "research_note": "research/GIS/2026-10-12.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 10.4%, back inside its FY2022-FY2025 range, showing the cash-conversion collapse was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 10.4}},
    {"text": "TTM operating margin recovers above the FY2025 level of 17.3%, showing pricing power and cost savings are offsetting volume pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 17.3}},
    {"text": "TTM net margin recovers above the FY2025 level of 11.8%, confirming the FY2026 loss was a one-off charge rather than structural.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 11.8}},
    {"text": "Net debt/EBITDA (ratios page) falls back below the FY2024 level of 2.99x, showing deleveraging under the new CEO."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 46.0, "basis": "FCF margin returns to its 10.4-14.5% FY range [CF,IS] and EV/EBITDA re-rates from 8.9x toward its 9.1x-11.7x 5y min-median [RA]; capped below the $48.97 DCF base [fact sheet Fair value] because the rising real-rate chain lowers the top of the range (moderate bear tilt, research/GIS/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 36.0, "basis": "Margins stabilise near TTM 15.6% operating / 8.5% FCF [IS,CF]; EV/EBITDA drifts back toward its 9.1x 5y floor [RA], below the $38.30 DCF bear value because the DCF assumes historical margins that FY2026 broke."},
    "bear": {"probability": 0.35, "target_price_12m": 26.0, "basis": "Operating and FCF margins keep falling while net debt/EBITDA rises above 3.86x [RA] and refinancing costs climb; moderate bear tilt from the macro overlay (research/GIS/2026-10-12-macro.md) lifts this probability from 0.30 to 0.35, and P/FCF of 11.2x [RA] holds on lower FCF."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock is already below its 5y minimum EV/EBITDA and EV/Sales [RA]; the problem is falling margins, FCF and returns, rising leverage and an unexplained FY2026 loss. A lower price would not change the decision; a recovery in fundamentals (triggers) would.",
  "replaces": null,
  "replacement_reason": null
}
```
