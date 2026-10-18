# Evaluation: Harmony Gold Mining Company Limited (JSE:HAR) — 2026-10-18
## Bear case
The record returns come from the gold price, not the business. Operating margin went from 8.9% (FY2022) to 41.0% and ROE from -3.3% to 48.0% [Certain], and the company has no pricing power [Likely]. A 6.2x P/E on what may be peak-cycle earnings can be a value trap, not a discount [Likely]. The macro overlay is primary-weight and tilts moderately toward bear: real yields are up 0.43pp in 3 months and the dollar is firming, both classic gold headwinds [Likely] (research/JSE-HAR/2026-10-18-macro.md). FCF conversion fell to 53.7% from 75.0% as copper capex rose [Certain], and Eva Copper carries permitting risk to its 2028 first-copper date [Likely]. The fair-value model can't be computed (no NAV, no ZAR FX input), so nothing anchors the valuation [Certain]. The 12-month change is -21.2% and results are due Oct 23, 2026, which is a binary event [Certain].

## Bull case
The balance sheet is near net cash (0.02x net debt/EBITDA) and ROIC is 41.0% TTM [Certain]. P/E and EV/EBITDA sit in the 12th and 18th percentiles of their own 5-year ranges, 53% and 30% below the peer medians (AU, GFI, NEM, SSL) [Certain]. FCF yield is 8.86% and dilution was only 0.80% despite the CSA and Eva Copper deals [Certain]. Management reports an 11-year record of meeting production guidance, record dividends, and acquisition one-offs mostly behind it [Likely]. Copper adds a second commodity [Likely]. If real yields roll over, operating leverage could lift margins further and close the peer gap [Guessing].

## Decision
```json
{
  "ticker": "JSE:HAR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A near-net-cash gold miner with record returns trades at the bottom of its own and peers' multiples, but those earnings are a gold-price peak facing rising real yields and a firmer dollar.",
  "rationale": "The low multiple is the market pricing in cyclical margins, and there's no computable fair value to show otherwise. A primary-weight macro overlay tilts toward bear, and results land Oct 23. That's good but not compelling, so it's an AVOID and we hold cash.",
  "price_at_decision": 28491.0,
  "price_date": "2026-10-16",
  "research_note": "research/JSE-HAR/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing the structural improvement from the FY2022 low of 12.1%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 8%, roughly half the TTM 15.9%, showing cost inflation or capex is eroding the margin gains.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Debt/EBITDA rises above 1.0x, showing capex and dividends are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Gold production guidance is missed for a full fiscal year, or Eva Copper's guided 2028 first-copper date slips by more than a year without a replacement growth driver."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 42888, "basis": "Real yields and the dollar roll over and gold extends, lifting margins above the 41.0% operating margin [IS], and the P/E re-rates from 6.2x toward its 10.4x 5y median [RA], taking the price back to its 42,888.00 52-week high [HI] (macro_bull, research/JSE-HAR/2026-10-18-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 29000, "basis": "Gold holds, earnings stay near TTM levels and the P/E stays near the bottom of its 5.3x-12.1x range [RA] because the market won't capitalise peak margins, so the price stays close to the 28,491.00 close [HI]; probability trimmed for the overlay's moderate bear tilt (research/JSE-HAR/2026-10-18-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 21352, "basis": "Rising real yields (2.78%) and a firmer dollar push gold lower and margins revert toward the FY2025 29.1% operating margin [IS], sending the price back to its 21,352.00 52-week low [HI]; probability raised moderately for the overlay's bear tilt (research/JSE-HAR/2026-10-18-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price isn't the obstacle. The multiple already sits near its 5y low [RA], and the problem is that peak-cycle, gold-driven earnings face macro headwinds, with no computable fair value [data unavailable]. A lower price on the same evidence would just track a lower gold price, so it wouldn't raise conviction. Re-research after the Oct 23 results or a turn in real yields.",
  "replaces": null,
  "replacement_reason": null
}
```
