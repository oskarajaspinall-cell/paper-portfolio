# Evaluation: Chubb Limited (CB) — 2026-10-09
## Bear case
This is a quality franchise at a full price, not a mispricing. P/B of 1.8x sits at the 87th percentile of its 5y range (1.4x-1.8x) and P/E of 12.2x is +16% above the peer median 10.4x [Certain] (fact sheet RA). The market already capitalises a ~15% ROE as permanent just as management flags "softening market conditions and rising loss costs in casualty" on the Q2 2026 call [Likely] (transcript listed in fact sheet). A soft pricing cycle compresses underwriting margins and P/B together. The fair-value skew is unfavourable: bear $250.23 (-27.2%) versus bull $385.88 (+12.2%) [Certain] (fact sheet). Margin and FCF data are [data unavailable], so reserve adequacy cannot be cross-checked [Certain]. Q3 results on Oct 20 add near-term event risk with no edge [Guessing]. Relative strength is weak: -7.0pp/-11.1pp vs SPY over 3m/6m [Certain] (HI).

## Bull case
ROIC has risen from 8.3% (FY2021) to 11.1% TTM, ROE has held 14-16% since FY2023, and net debt/EBITDA fell from 2.59x to 1.68x [Certain] (RA, BS/IS). Shares outstanding are down -2.49% y/y, so capital is returned while the balance sheet strengthens [Certain] (ST). Q2 core operating income rose 14.6% y/y despite a softer market [Likely] (transcript in fact sheet). Higher real yields lift reinvestment income on the float, and the 5.28% risk-free rate is already in the fair-value discount, which still shows base $379.09 (+10.3%) [Certain] (fact sheet; macro overlay). Beta of 0.37 and 1.03% short interest make it a low-volatility compounder [Certain] (ST). But at a 5y-median P/E with P/B near its high, upside rests on earnings growth alone [Likely].

## Decision
```json
{
  "ticker": "CB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Chubb is a deleveraging, buyback-funded P&C franchise with ROIC rising to 11.1%, but at P/B near the top of its 5-year range and a P/E premium to peers entering a softening pricing cycle, the price already reflects its quality.",
  "rationale": "Quality is real but valuation offers no margin of safety: P/B at the 87th percentile of its 5y range, P/E +16% over peers, and a fair-value skew of -27% bear versus +12% bull. Softening casualty pricing caps rerating. Good but not compelling; conviction 3 means no position under the owner rule.",
  "price_at_decision": 343.78,
  "price_date": "2026-10-08",
  "research_note": "research/CB/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 17%, above the FY2023 5-year high of 15.8%, showing underwriting is outrunning the soft market and the premium P/B is earned.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 17}},
    {"text": "TTM ROIC rises above 13%, extending the five-year rise from 8.3% to 11.1% and proving earnings growth beyond the pricing cycle.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 13}},
    {"text": "Net debt/EBITDA (site definition) rises above 2.5x, back to the FY2021-22 level, eroding the balance-sheet buffer and confirming the AVOID.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.30, "target_price_12m": 385.88, "basis": "Fact-sheet bull fair value $385.88 (P/B+ROE blend) as ROE holds near 14.8% [RA] and buybacks continue (-2.49% shares [ST]); probability raised by a small bull tilt per the macro overlay (research/CB/2026-10-09-macro.md: higher reinvestment yields on the float with HY spreads only 3.09%)."},
    "base": {"probability": 0.50, "target_price_12m": 336.74, "basis": "Below the blended base $379.09 because P/B is already at the 87th percentile of its 5y range [RA] and casualty pricing is softening (Q2 2026 transcript in fact sheet), so the P/E method base $336.74 at a near-median 12.2x vs 11.9x [RA] is the better anchor."},
    "bear": {"probability": 0.20, "target_price_12m": 250.23, "basis": "Fact-sheet bear fair value $250.23 as the soft market and rising casualty loss costs (Q2 2026 transcript) push P/B back toward its 1.5x 5y median [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
