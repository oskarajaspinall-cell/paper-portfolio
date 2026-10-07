# Evaluation: Ameriprise Financial, Inc. (AMP) — 2026-10-07
## Bear case
The core asset, the advisor channel, is leaking: a 2026-09-24 TheFly/Citywire item reports bonuses and platform-fee discounts to stem attrition [Likely]. That fits five years of erosion, with gross margin down 5.5pp to 54.9% and net margin down 6.7pp to 19.9% [Certain] (IS). Retention spend hits margins before it shows up in asset outflows [Guessing]. The headline cash metrics are weak evidence: for a business with an annuity and insurance arm, 204% FCF conversion and a P/FCF of 5.4x probably reflect balance-sheet flows more than owner earnings [Likely]. On earnings, AMP is not cheap against its own history: 12.0x P/E sits below its 12.8x five-year median [Certain] (RA). The macro overlay tilts moderately toward bear. Real yields are up 0.71pp over three months and HY spreads are widening, which marks down AUM-linked fees and the multiple [Likely]. The stock trails SPY by 15.5pp over 12 months [Certain] (HI).

## Bull case
This is a scaled, recurring-fee franchise with 63.4% TTM ROE and an operating margin held near 35% for five years [Certain] (RA, IS). Capital return is heavy. Shares outstanding are down 5.22% YoY [Certain] (ST), and a further $5.5bn buyback was authorised on 2026-09-29 [Certain]. At about 13% of the 43.1bn market cap, that keeps the share count shrinking [Likely]. Valuation is undemanding: 12.0x P/E is a 24% discount to the 15.8x peer median, and EV/Sales of 1.9x is below its five-year minimum [Certain] (RA). The shares are at a 35 RSI after falling from 572.56 [Certain] (ST, HI). If Q3 results on 2026-10-29 show attrition is contained, the multiple could return to its five-year median or higher [Guessing]. Advisor recruits from Merrill Lynch and Wells Fargo in August and September suggest the channel still attracts talent [Likely] (OV).

## Decision
```json
{
  "ticker": "AMP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "AMP is a high-ROE, buyback-heavy wealth franchise at 12.0x earnings, but advisor attrition, five years of margin erosion and a bearish real-rate backdrop leave the P/E only modestly below its own median, so the discount looks deserved rather than mispriced.",
  "rationale": "The quality and capital return are real, but the stock is only cheap against peers and on a P/FCF that insurance flows likely distort. On P/E it sits near its own median. Attrition is an open thesis risk before the 2026-10-29 results, and the macro tilt is to the bear side. The probability-weighted upside is only about 2%. Good but not compelling: conviction 3, AVOID.",
  "price_at_decision": 496.61,
  "price_date": "2026-10-06",
  "research_note": "research/AMP/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin recovers above the FY2024 level of 57.8%, showing fee/advisor-comp erosion has reversed (would raise conviction).", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 57.8}},
    {"text": "TTM net margin recovers above the FY2022 level of 22.0%, confirming retention costs are not compressing profitability (would raise conviction).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 22.0}},
    {"text": "Company filings or results show advisor attrition has stabilised without ongoing bonus/fee-discount programmes, removing the main threat to the fee-generating asset base."}
  ],
  "exit_plan": null,
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 629.0, "basis": "If attrition is contained and buybacks continue, the P/E re-rates to its 5y max of 15.2x [RA] on TTM EPS implied by the 12.0x P/E at 496.61 [RA,HI]. Probability is cut from 0.25 for the moderate bear macro tilt (research/AMP/2026-10-07-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 529.7, "basis": "Stable margins and steady buybacks return the P/E to its 5y median of 12.8x [RA] on TTM EPS. Probability is cut from 0.50 for the moderate bear macro tilt (research/AMP/2026-10-07-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 409.7, "basis": "Advisor attrition (TheFly/Citywire, 2026-09-24) and continued margin erosion [IS], compounded by rising real yields marking down AUM, de-rate the P/E to its 5y min of 9.9x [RA]. Probability is raised from 0.25 for the moderate bear macro tilt (research/AMP/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
