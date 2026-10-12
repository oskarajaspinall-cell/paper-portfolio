# Evaluation: Solventum Corporation (SOLV) — 2026-10-12
## Bear case
Every quality metric is moving the wrong way since the 2024 3M spin-off: ROIC 12.0% to 5.5%, operating margin 22.9% to 7.6%, FCF margin 23.6% to -1.4% [Certain] (fact sheet RA/IS/CF). Net debt/EBITDA is 4.29x and still rising, Altman Z is 1.74, yet management bought back stock with negative FCF [Certain]. The 10.4x P/E is flattered by a one-off tariff refund [Likely] (Q2 2026 transcript); on cash-based measures the stock is expensive, with EV/EBITDA of 17.3x above its 5y max and 71% over peers [Certain]. Selling the higher-margin HIS unit dilutes RemainCo margins [Likely] (Wells Fargo transcript). Rising real yields and widening HY spreads raise refinancing risk for a levered, cash-negative issuer [Likely] (macro overlay). The mechanical +53% base fair value rests on P/E alone, because the DCF fails on negative cash flow [Certain].

## Bull case
Q2 2026 beat and FY26 adjusted EPS guidance was raised sharply, with organic growth guidance lifted [Likely] (Q2 2026 transcript, fact sheet headlines). The HIS sale has reached initial bids [Likely]. Proceeds could pay down spin-off debt quickly and reset leverage and the Altman Z [Guessing]. Separation and TSA costs that depress FCF are temporary [Likely]. Clarity aligners and the V.A.C. franchise give real brand positions [Likely]. P/E sits at the 11th percentile of its 5y range and 61% below peers [Certain]. The stock has beaten SPY by 17.4pp over 6 months [Certain] (fact sheet HI). If FCF conversion recovers toward its pre-spin level of over 100%, the base fair value of 133.79 is reachable [Guessing].

## Decision
```json
{
  "ticker": "SOLV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A post-spin medtech with collapsing returns, negative free cash flow and 4.29x leverage looks cheap only on a refund-flattered P/E while trading above its 5-year EV/EBITDA range, so its turnaround through the HIS sale is not yet proven.",
  "rationale": "Quality is deteriorating on ROIC, margins and FCF, leverage is high and rising, and the low P/E rests on one-off earnings. EV/EBITDA and EV/Sales are above their 5y highs. Rising rates and credit spreads tilt the risks toward the bear case. The HIS sale is a real catalyst but unproven. Conviction 2, so no position.",
  "price_at_decision": 87.29,
  "price_date": "2026-10-09",
  "research_note": "research/SOLV/2026-10-12.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 9.8% (the FY2024 level), showing the separation cash drag was temporary.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 9.8}},
    {"text": "Net debt/EBITDA falls below 3.75x (FY2025), showing spin-off leverage is being repaid, e.g. from HIS proceeds.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 3.75}},
    {"text": "TTM ROIC rises back above 7.9% (FY2024), showing returns on capital have found a floor and are recovering.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 7.9}},
    {"text": "TTM operating margin rises above 13.2% (FY2024), showing RemainCo margins are rebuilding after the HIS separation.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 13.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 133.79, "basis": "HIS sale proceeds cut net debt/EBITDA from 4.29x [BS,IS] and FCF turns positive, so the market accepts the P/E-based base fair value of 133.79 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 88.42, "basis": "Raised FY26 guidance (Q2 2026 transcript) offsets the expiry of the one-off tariff refund that flatters TTM net margin of 17.3% [IS], so the stock holds around its 50-day average of 88.42 [HI]; this is below the 133.79 base fair value because that P/E method capitalises refund-inflated earnings while the DCF fails on negative FCF [fact sheet Fair value]."},
    "bear": {"probability": 0.35, "target_price_12m": 62.38, "basis": "FCF stays negative (-1.4% TTM [CF,IS]) with leverage above 4x, and rising yields and HY spreads add refinancing cost, so the price revisits its 52-week low of 62.38 [HI], below the 72.37 bear fair value; bear probability raised moderately per the macro overlay's tilt toward bear (research/SOLV/2026-10-12-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC, margins and FCF are deteriorating and leverage is rising, so a lower price on this evidence would not justify conviction 4; re-assess on the triggers (FCF recovery, deleveraging after the HIS sale).",
  "replaces": null,
  "replacement_reason": null
}
```
