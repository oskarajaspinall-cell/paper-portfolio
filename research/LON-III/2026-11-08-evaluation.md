# Evaluation: 3i Group plc (LON:III) — 2026-11-08
## Bear case
3i is mainly a leveraged bet on one asset: the May results showed weaker profitability at Action, which a headline says is the bulk of portfolio value, and the shares are down 42.1% over 12 months [Likely]. Returns are still falling. ROIC is 17.3% TTM against 19.6% a year earlier and 5.0pp below its 2-year high of 22.2%, and ROCE follows the same path [Certain]. That points to slower NAV compounding as Action's growth slows, not a one-off. It threatens a thesis built on compounding marks [Likely]. Reported profit is mostly unrealised gains: FCF conversion is only 18.8% [Certain]. FCF margin is also 5.1pp below its 2-year high [Certain]. Piotroski F is 4 and shares rose 1.56% YoY despite the buyback [Certain]. The euro is about 2.6% weaker against sterling, a translation drag (macro overlay) [Likely]. The Nov 12, 2026 results could mark Action down [Guessing].
## Bull case
At 0.8x book, the bottom of its 5y P/B range (0.8x-1.4x), the market already prices in markdowns that may not come [Certain]. P/E of 4.7x sits at its 5y median, far below the 14.6x peer median [Certain]. Returns remain high in absolute terms: ROE 19.1%, operating margin 97.6% [Certain]. The balance sheet is near-unlevered at 0.11x net debt/EBITDA, and Altman Z is 15.99, so there is no forced-seller risk [Certain]. The H2 2026 transcript cites a 22% ROE, 19% NAV growth, a GBP 750m buyback and a higher dividend [Likely]. The CMD transcript says Action grew net sales 16% in 2025, plans at least 400 new stores in 2026 and aims for a US launch [Likely]. If the Nov 12 results show the marks holding, P/B could move back toward its 1.1x median [Guessing].
## Decision
```json
{
  "ticker": "LON:III",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A near-unlevered, high-return private-equity holder trades at 0.8x book, the bottom of its 5-year range, but its value hinges on one unverified-size asset (Action) whose slowing profitability is pulling ROIC and ROCE down a further 2pp+ over the last year.",
  "rationale": "The discount to book is real but justified by concentration in Action, falling rolling returns and weak cash conversion. No mechanical fair value exists, the IR page that would size Action was blocked, and results land on Nov 12. That is good but not compelling: conviction 3, so AVOID and re-research after the results.",
  "price_at_decision": 2525.00,
  "price_date": "2026-11-06",
  "research_note": "research/LON-III/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12% (17.3% now, 34.2% in FY2022), showing Action's slowdown is eroding portfolio returns structurally.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM ROE falls below 12% (19.1% now), showing NAV compounding has slowed to an ordinary rate of return.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Shares change YoY rises above 4% (1.56% now), showing equity-funded dilution rather than buyback-led capital return.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 4}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.11x now), showing the balance sheet is being levered to support the portfolio.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3400, "basis": "Nov 12 results show Action's marks holding and P/B recovers toward its 5y median 1.1x from 0.8x [RA], still below the 52-week high of 4,363.00 [HI]; no mechanical fair value is available [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 2600, "basis": "P/B stays near its 5y low of 0.8x [RA] while ROE of 19.1% [RA] compounds book value slowly; Action slows but is not marked down, and the overlay's euro drag (research/LON-III/2026-11-08-macro.md, context only) is small."},
    "bear": {"probability": 0.30, "target_price_12m": 1900, "basis": "Action is marked down at the Nov 12 results, extending the ROIC fall from 19.6% to 17.3% [RA-T], and the price retests the 6-month low of 1,825.00 seen after the May Action slowdown [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already sits at its 5y-low P/B of 0.8x [RA] and no mechanical fair value exists. The obstacle is unverified exposure to Action and the unresolved Nov 12 results marks, so a lower price on the same evidence would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
