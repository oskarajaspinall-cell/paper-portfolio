# Evaluation: Union Pacific Corporation (UNP) — 2026-10-10
## Bear case
At 278.34 UNP trades 35.8% above blended base fair value (178.57) and above even the bull case (211.62); the reverse DCF needs 15.3% year-1 revenue growth, far above its own trend [Certain]. Quality is flat-to-eroding, not improving: operating margin -2.3pp and FCF conversion -16.4pp over five years [Certain]. The proposed $85bn Norfolk Southern deal adds integration, financing and Surface Transportation Board risk, with unions and farm groups opposed and no disclosed financing mix or synergies [Likely]. The macro overlay flags a 10y yield of 5.22% (+68bp in 3 months) and HY spreads +45bp, raising both the discount rate and deal funding cost [Certain]. Short interest is rising (+5.7% month-on-month) [Certain]. The stock lags SPY by 5.9pp over 3 months, so the market is already doubting the story [Likely].

## Bull case
UNP is an irreplicable western rail franchise: ROIC has held 15.1–17.0% for five years, operating margin is 40.8% and Piotroski F-score 8 [Certain]. On peer and own-history multiples it is not stretched: P/E 22.5x is 17% below the peer median, P/FCF 25.4x is 32% below and sits in the bottom 27% of its own 5-year range, and EV/EBITDA 15.1x is mid-range [Certain]. Leverage is falling (net debt/EBITDA 2.26x from 2.89x) and buybacks cut shares 1.50% YoY [Certain]. Management reports carload volumes up 5% and high diesel prices shifting freight from truck to rail [Likely]. An approved NS merger would create the first transcontinental railroad with broad shipper support [Guessing]. But none of this offers a margin of safety: it argues the stock is fairly priced, not cheap [Likely].

## Decision
```json
{
  "ticker": "UNP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, irreplicable rail franchise with flat 16% ROIC trades at mid-range own-history multiples and well above DCF fair value, while an unapproved $85bn Norfolk Southern merger adds execution and financing risk without a margin of safety.",
  "rationale": "Quality is excellent but stable-to-eroding, not improving; the price sits 36% above base fair value and implies 15.3% growth. Mid-range multiples mean fair, not cheap. The contested NS merger and rising real yields skew risk to the downside. Good but not compelling: conviction 3, AVOID; cash is acceptable.",
  "price_at_decision": 278.34,
  "price_date": "2026-10-09",
  "research_note": "research/UNP/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC rises above 17%, the 5-year high (FY2022 17.0%), showing returns are improving rather than flat.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 17}},
    {"text": "TTM operating margin recovers above 42%, reversing most of the five-year decline from 42.9% (FY2021).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 42}},
    {"text": "TTM FCF margin recovers above 28%, back to the FY2021 level, showing cash conversion is structurally restored.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 28}},
    {"text": "The Surface Transportation Board rules on the Norfolk Southern combination and UNP discloses financing terms that keep net debt/EBITDA below 2.8x, as shown in an SEC filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 298.74, "basis": "Volume gains from truck-to-rail diesel shift (Reuters 2026-09-16 headline [OV]) and merger approval re-rate EV/EBITDA toward its 5y max 16.6x [RA], matching the fact sheet's EV/EBITDA bull value of 298.74 rather than the DCF-weighted bull 211.62, which a 5.22% risk-free rate penalises."},
    "base": {"probability": 0.5, "target_price_12m": 254.31, "basis": "EV/EBITDA drifts from 15.1x back to its 5y median 14.0x [RA] on flat ROIC/margins [RA,IS], giving the fact sheet's EV/EBITDA base of 254.31; above the blended base 178.57 because own-history multiples, not the rate-sensitive DCF, set a 12-month price for a stable franchise."},
    "bear": {"probability": 0.3, "target_price_12m": 215.53, "basis": "Merger opposition or costly deal financing plus rising real yields (macro overlay research/UNP/2026-10-10-macro.md: tilt toward bear, small, moving 0.05 from bull to bear) push the stock back to its 52-week low of 215.53 [HI], still above the blended bear fair value of 137.10."}
  },
  "entry_price": 142.86,
  "entry_basis": "valuation file: base 178.57 x 0.8; a price at which the same evidence (stable quality, contested merger) would carry a margin of safety for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
