# Evaluation: Engie Brasil Energia (BVMF:EGIE3) — 2026-11-08
## Bear case
Returns are fading while leverage climbs: ROCE fell from 17.1% (FY2021) to 11.3% (FY2025) and the rolling 12 months are only flat at 12.0%, below the 13.5% two-year high [Certain]. Net debt/EBITDA (site definition) rose from 2.34x to 3.56x, so a Selic still at 13.75% weighs on interest cost [Certain]. The July 2026 equity offering dilutes holders and the fact sheet's share count has not yet captured it [Likely]. TTM net margin of 28.9% and FCF margin of 26.1% follow a negative-FCF FY2024, so the cheap P/E 7.8x and P/FCF below its 5y minimum likely rest on non-recurring gains and capex timing [Likely]. EV/EBITDA 8.1x is mid-range and in line with peers, so leverage-adjusted there is no discount [Certain]. The mechanical bear fair value is negative and the base only +14.4% [Certain]. Hydrology and curtailment risks persist [Likely].
## Bull case
Contracted, inflation-indexed generation and transmission revenue with a beta of 0.36 is a defensive cash stream [Likely]. The Q2 2026 call showed adjusted EBITDA growth from new assets, with Jirau and liability prepayment set to lift profitability [Likely]. The equity raise at a price above today's eases leverage [Likely]. The reverse DCF implies -0.7% year-1 revenue growth, undemanding for a business adding capacity [Likely]. FCF yield 9.27% and P/B at its 5y low offer support, and a slowly easing Selic would lower funding costs [Guessing]. Results on Nov 10, 2026 could confirm the post-acquisition earnings step-up [Guessing].
## Decision
```json
{
  "ticker": "BVMF:EGIE3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A contracted Brazilian renewable generator and transmitter looks cheap on P/E and P/FCF, but falling ROCE, rising leverage and dilution leave only modest, leverage-adjusted upside to a fair value whose bear case is negative.",
  "rationale": "Quality is adequate but fading (ROCE down five years, flat over the last year) and leverage is rising; EV/EBITDA is in line with peers, so the apparent cheapness depends on likely non-recurring TTM earnings and FCF. Base upside is modest and the downside wide: good but not compelling, so no position.",
  "price_at_decision": 27.15,
  "price_date": "2026-11-06",
  "research_note": "research/BVMF-EGIE3/2026-11-08.md",
  "triggers": [
    {"text": "Net debt/EBITDA (site definition) rises above 4.0x (3.56x TTM now), showing the Jirau and project spend is outrunning the equity raise.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "TTM FCF margin falls below 10% (26.1% now), showing the cash step-up was capex timing rather than durable conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 18% (28.9% now), under the FY2025 level of 20.1%, confirming TTM profits were flattered by one-offs.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 18}},
    {"text": "TTM ROCE on the ratios page falls below 10% (12.0% now), extending the five-year decline in returns."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.83, "basis": "New wind, solar, transmission and Jirau assets lift EBITDA as the Q2 2026 call described (transcript 539647-q2-2026) and the price reaches the mechanical bull fair value of 33.83 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 28.5, "basis": "Earnings hold but the TTM FCF margin of 26.1% after a negative FY2024 [CF] and unrecorded offering dilution argue for a value between the EV/EBITDA base of 26.37 and the blended base of 31.06 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 23.21, "basis": "ROCE keeps sliding from 12.0% [RA-T] while net debt/EBITDA climbs past 3.56x [RA] and EV/EBITDA derates toward its 5y low of 7.1x [RA]: the EV/EBITDA bear value of 23.21 [fact sheet Fair value], above the not-meaningful negative DCF bear."}
  },
  "entry_price": 24.85,
  "entry_basis": "valuation file: base 31.06 x 0.8; at that price the modest base upside becomes a margin of safety large enough to offset fading returns and rising leverage.",
  "replaces": null,
  "replacement_reason": null
}
```
