# Evaluation: Churchill Downs Incorporated (CHDN) — 2026-11-08
## Bear case
This is a levered, average-return business. Net debt/EBITDA is 4.65x and Altman Z is 1.50 [Certain]. ROIC of 9.2% sits below FY2021's 11.4% and is flat over the last year [Certain], so returns barely clear a normal cost of equity [Likely]. The discount is to CHDN's own former premium, not to peers: EV/EBITDA of 11.4x is above the 10.6x peer median [Certain]. Q3 revenue grew by only $10 million [Likely], and TTM operating margin of 25.8% is below its 26.1% two-year high [Certain], so the old growth premium may not come back. The planned sale of nine regional properties ($280 to $300 million Adjusted EBITDA [company-reported]) has no disclosed price or mix [Certain]. HRM revenue depends on regulators, as the 2025 Louisiana court-driven exit showed [Certain]. Buybacks at 4.65x leverage add risk [Likely]. Short interest is 8.50% and rising [Certain]. The DCF bear value of 25.89 shows how much the value depends on leverage [Certain].
## Bull case
Every multiple is below its own 5-year minimum: P/E 15.1x against a 23.0x median, P/FCF 12.7x against 40.6x, and a 7.89% FCF yield [Certain]. The price implies -4.7% year-1 revenue growth, yet Q3 set records for revenue and Adjusted EBITDA [Likely]. The last 12 months are improving: ROCE rose 1.8pp to 12.6% and FCF margin rose 2.0pp to 17.6%, with FCF conversion at 116.5% [Certain]. Leverage has come down from 8.86x in FY2022 [Certain]. The Derby is a unique asset [Likely]. Share count is down 4.77% YoY, a new $750M buyback was approved [Certain], and asset-sale proceeds expected by year-end would speed up deleveraging [Likely]. Even the EV/EBITDA method's bear value of 127.51 is above the 97.94 close [Certain]. A new Henry County, Virginia HRM venue has local approval [Certain].
## Decision
```json
{
  "ticker": "CHDN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Derby-anchored racing, HRM and gaming operator with improving cash conversion trades below its own 5-year minimum multiples, but ROIC near the cost of capital, 4.65x leverage and an unpriced sale of nine regional properties make the skew good rather than compelling.",
  "rationale": "The price is cheap against its own history and the FCF yield is strong, but the stock is not cheap against peers on EV/EBITDA. Returns are modest, the balance sheet is stretched and the sale terms are unknown. The mechanical fair value is driven by a leverage-sensitive DCF. Conviction 3, below the buy bar: AVOID. Re-research once the sale terms are disclosed.",
  "price_at_decision": 97.94,
  "price_date": "2026-11-06",
  "research_note": "research/CHDN/2026-11-08.md",
  "triggers": [
    {"text": "Net debt/EBITDA falls below 4.0x (4.65x TTM now), showing that asset-sale proceeds and FCF have actually cut leverage (would raise conviction).", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 4.0}},
    {"text": "TTM ROIC rises above 11%, back to the FY2021 level of 11.4% (9.2% now), showing the remaining Derby/HRM/TwinSpires mix earns clearly above its cost of capital (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 11}},
    {"text": "TTM FCF margin falls below 12% (17.6% now), which would break the cash-conversion leg of the case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "A company filing or release discloses completed regional-property sale terms with proceeds directed to debt reduction (re-research), or a loss of HRM authorisation in Kentucky or Virginia."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 150.0, "basis": "The regional sale closes on good terms by year-end (Q3 transcript), leverage keeps falling from 4.65x [RA] and the $750M buyback (GlobeNewsWire 2026-10-28) shrinks the share count, so EV/EBITDA moves back above its 5y minimum of 13.6x [RA]; this is well below the mechanical bull of 319.76 because the DCF extrapolates growth and a premium rating the business no longer earns."},
    "base": {"probability": 0.5, "target_price_12m": 115.0, "basis": "FCF margin holds near 17.6% [CF-T] and EV/EBITDA moves partway from 11.4x toward its 5y minimum of 13.6x [RA]; this is below the EV/EBITDA method's base of 211.88 and the blended base of 231.67 because a return toward the 19.5x median is not supported when the multiple already sits above the 10.6x peer median [RA] and ROIC is flat at 9.2% [RA-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 74.0, "basis": "Sale terms disappoint or an HRM regulatory loss like Louisiana's (sec.gov 10-Q) cuts EBITDA while leverage stays near 4.65x and Altman Z near 1.50 [ST], sending the price back to around its 52-week low of 73.08 [HI]; this is above the mechanical bear of 25.89 because FCF conversion of 116.5% [CF,IS] and a peer-level multiple support the equity."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum multiples and below every mechanical fair value except the DCF bear. What holds conviction at 3 is the unresolved regional-property sale and the 4.65x leverage, so a lower price on the same evidence would not change the decision. Re-research when the sale terms are disclosed.",
  "replaces": null,
  "replacement_reason": null
}
```
