# Evaluation: SLB N.V. (SLB) — 2026-10-12
## Bear case
Returns are rolling over from a cyclical peak: ROIC fell from 17.3% (FY24) to 11.6% TTM and operating margin from 17.6% to 14.2% [RA,IS] [Certain]. Yet the stock trades on 23.7x TTM P/E, above its own 5y max of 22.3x and 12% above peers [RA] [Certain], so earnings are falling while the multiple rises. The base fair value of 49.50 is only 1.1% above the 48.95 close, leaving no margin of safety, and the reverse DCF already needs 6.4% year-1 growth [Certain]. Shares rose 7.57% YoY [ST], and net debt/EBITDA climbed back to 1.18x before a ~$3.4bn cash Kelvion deal outside the core business [Certain]. Rising real yields push the DCF value below price (macro overlay) [Likely]. An oil-capex downturn points to the 20.84 bear value [Likely].

## Bull case
SLB is the scale leader in a concentrated oilfield-services oligopoly [Likely]. It keeps winning long-cycle work: a 15-year TotalEnergies DrillPlan deal, four Aramco well-construction contracts and a OneSubsea award in Rovuma [OV news] [Certain]. FCF margin holds at 12.0% with 141% FCF/NI conversion [CF,IS], and P/FCF of 16.6x is in line with peers and in the bottom 10% of its own range [RA] [Certain]. EV/EBITDA of 11.0x is below its 5y median of 11.6x [RA] [Certain]. If activity holds and Kelvion gives SLB a second growth market in data-centre cooling, the bull fair value of 65.85 (+34.5%) is reachable [Guessing]. The 12-month change of +44.1% shows the market has rewarded the cycle [ST] [Certain].

## Decision
```json
{
  "ticker": "SLB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality but cyclical oilfield-services leader whose returns are fading from the FY2024 peak trades at its base fair value and above its own 5-year P/E range, so the risk-reward offers no margin of safety.",
  "rationale": "Price sits at base fair value (49.50 vs 48.95) while ROIC and margins fall from their peak. P/E is above its 5y max, dilution is 7.57%, and the debt-funded Kelvion deal adds execution risk. The probability-weighted target is below price. A good franchise, but not compelling at this price: AVOID and keep the cash.",
  "price_at_decision": 48.95,
  "price_date": "2026-10-09",
  "research_note": "research/SLB/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 15%, back toward the FY2023-FY2024 levels (15.6%-17.3%), showing the post-peak decline in returns has reversed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}},
    {"text": "TTM operating margin rises back above 16.6% (FY2023 level), showing pricing power survives the slowdown in activity.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 16.6}},
    {"text": "Share count turns to net shrinkage (YoY shares change below 0%), showing capital returns are no longer offset by dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}},
    {"text": "TTM ROIC falls below 10%, confirming structural decline in returns (would make any entry price irrelevant).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 65.85, "basis": "Activity holds, contract wins (TotalEnergies, Aramco, Rovuma [OV]) lift margins back toward the FY2024 peak, reaching the fact sheet's bull fair value of 65.85."},
    "base": {"probability": 0.5, "target_price_12m": 49.5, "basis": "Returns stabilise near TTM ROIC 11.6% [RA] and the stock tracks the base fair value of 49.50 (DCF/EV-EBITDA blend), roughly where it trades now."},
    "bear": {"probability": 0.3, "target_price_12m": 32.17, "basis": "Oil-capex slowdown continues the margin fade and EV/EBITDA de-rates toward its 5y low of 7.7x [RA], in line with the EV/EBITDA bear value of 32.17; bear probability raised slightly for the macro overlay's small bear tilt from rising real yields (research/SLB/2026-10-12-macro.md)."}
  },
  "entry_price": 39.6,
  "entry_basis": "valuation file: base 49.50 x 0.8 = 39.60, a 20% margin of safety on the same cyclical quality evidence.",
  "replaces": null,
  "replacement_reason": null
}
```
