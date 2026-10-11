# Evaluation: Emaar Properties PJSC (DFM:EMAAR) — 2026-10-11
## Bear case
A 5.2x P/E [Certain] on what are probably peak-cycle earnings is not cheap. ROIC (25.3% TTM vs 7.3% FY2021) and net margin (35.8% vs 13.6%) sit at five-year highs [Certain], and a developer's earnings revert when the cycle turns [Likely]. The turn may be starting: FCF margin fell from 72.1% (FY2022) to 46.9% TTM and FCF conversion from 263.2% to 131.0% [Certain]. The 50-day average is 10.6% below the 200-day and the stock trails SPY by 32.3pp over 12 months [Certain], which reads as the market discounting a Dubai downcycle [Likely]. The overlay points the same way: the AED peg passes a 5.22% US 10y yield and a stronger dollar into buyer costs (moderate bear tilt) [Likely]. Iranian strikes on Dubai in March 2026 add tail risk that management reassurance cannot rule out [Likely]. NAV is [data unavailable], so the asset backing cannot be checked [Certain].
## Bull case
Even on reduced earnings the margin of safety is wide. P/E 5.2x, EV/EBITDA 3.5x and EV/Sales 1.8x are all below their 5-year minimums (6.0x, 5.3x, 2.4x) [Certain], with a 24.99% FCF yield and a net-cash balance sheet (-0.76x net debt/EBITDA) [Certain]. The price implies -29.0% revenue in year one [Certain], so a full halving of the FCF margin would still leave a double-digit yield [Likely]. The prime Dubai land bank and recurring mall/hospitality income are hard to replicate [Likely], and P/B 0.9x is near the 5-year median (0.8x) despite ROE of 24.2% [Certain]. Dilution is negligible (0.27% YoY) [Certain]. If US rates roll over, the peg passes the easing straight through to Dubai mortgage costs [Likely], and P/E could re-rate toward its 7.6x median [Guessing].
## Decision
```json
{
  "ticker": "DFM:EMAAR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Dubai developer with a 24.99% FCF yield trades below its 5-year minimum P/E and EV/EBITDA, but on probably peak-cycle earnings, with cash conversion already falling and rates and geopolitics both working against it.",
  "rationale": "Cheap on paper, but the multiples sit on peak-cycle returns. FCF margin has fallen from 72.1% to 46.9%, NAV can't be checked, and the macro overlay tilts moderately bearish through the USD peg. The 5-year P/FCF (3.8x median) shows the market has always priced Emaar this way. Good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 11.38,
  "price_date": "2026-10-09",
  "research_note": "research/DFM-EMAAR/2026-10-11.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 30%, showing the cash-conversion decline from the 72.1% FY2022 peak is a cyclical downturn, not normalisation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 45%, toward the FY2021 low of 41.6%, showing pricing power is eroding as Dubai supply arrives.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 45}},
    {"text": "TTM ROIC falls below 12%, giving back most of the rise from 7.3% (FY2021) to 25.3% and confirming peak-cycle returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "The Q3 2026 results (Nov 6, 2026) show the FCF margin stabilising at or above the 46.9% TTM level with operating margin held near 45%, which would ease the peak-earnings concern and could lift conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 16.63, "basis": "P/E re-rates to its 7.6x 5y median [RA] on TTM EPS as US rates roll over and the AED peg eases Dubai mortgage costs (macro overlay bull path). Well below the 52.82 DCF base because that DCF capitalises peak FCF with a floored beta and NAV unavailable [fair value section]."},
    "base": {"probability": 0.45, "target_price_12m": 11.38, "basis": "P/E holds at 5.2x [RA] on flat TTM EPS: the discount to the 6.0x 5y minimum persists while FCF margin keeps normalising (72.1%→46.9% [CF,IS]). The probability was moved from 0.50 and the price-implied -29.0% reverse-DCF growth is taken as plausible given the moderate bear macro tilt (research/DFM-EMAAR/2026-10-11-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 8.71, "basis": "Net margin reverts from 35.8% TTM to the FY2022 level of 27.4% [IS] at an unchanged 5.2x P/E [RA] as the Dubai cycle turns; the probability was raised from 0.25 for the overlay's moderate bear tilt (rates and dollar rising through the AED peg, research/DFM-EMAAR/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. At 5.2x P/E and a 24.99% FCF yield [ST], a lower price would not resolve the open question: whether earnings are at a cyclical peak (FCF margin falling from 72.1% to 46.9% [CF,IS], NAV [data unavailable]). The base fair value x 0.8 (42.26) is above the price and is not a usable anchor. Conviction 4 needs fundamental evidence (the Q3 2026 FCF and operating margins holding), not a lower quote.",
  "replaces": null,
  "replacement_reason": null
}
```
