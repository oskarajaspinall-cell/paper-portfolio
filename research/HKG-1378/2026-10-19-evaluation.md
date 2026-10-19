# Evaluation: China Hongqiao Group Limited (HKG:1378) — 2026-10-19
## Bear case
This is a price-taking commodity producer reporting what look like peak-cycle numbers: TTM ROIC 19.5%, ROE 22.9% and gross margin 27.9% all sit at or above the top of their FY2021-25 ranges [Certain]. FY2022 showed how fast that reverses: gross margin 13.8%, FCF margin -0.9% [Certain]. The shares are down 49.7% over six months and trade 32.9% below the 200-day average, with no results reaction to explain it [Certain]. That pattern usually means the market is pricing a turn in aluminium/alumina prices that trailing figures cannot yet show [Likely]. A low P/E on peak earnings is the classic cyclical trap. P/E of 6.3x is actually above its 5y median of 4.8x [Certain]. The mechanical bear value is HKD 2.53 [Certain]. Shares grew 5.38% YoY [Certain]. The cost-curve edge cannot be verified from an allowlisted source [Certain]. Macro tilts moderately toward bear: dollar and real-yield surge (overlay) [Likely].

## Bull case
The balance sheet is far stronger than at the last trough: net debt/EBITDA is 0.26x versus 1.76x in FY2022 [Certain], so a downturn is survivable without distress. TTM FCF yield is 20.58% and P/FCF 4.9x, 60% below the peer median [Certain]. Cash conversion is 125.1% of net income [Certain]. EV/EBITDA of 3.8x sits below its 5y median of 4.6x [Certain]. The reverse DCF implies -14.3% year-1 revenue growth [Certain], which already discounts a meaningful downturn [Likely]. The through-cycle DCF base of HKD 46.07 and the blended base of HKD 35.83 sit well above the HKD 19.64 close [Certain]. If H2 2026 results on Nov 20, 2026 show margins holding, the sell-off would look overdone [Guessing]. RSI of 31.6 shows the stock is near oversold [Certain].

## Decision
```json
{
  "ticker": "HKG:1378",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A strongly deleveraged, high-FCF aluminium producer looks cheap on trailing cash flow, but trailing returns sit at the top of the cycle while the share price has halved in six months, signalling a commodity downturn the figures do not yet show.",
  "rationale": "Cheap on trailing FCF with a clean balance sheet, but earnings look cyclically peaked, the six-month collapse is unexplained, there is no verifiable cost moat, dilution continues and macro tilts bearish. The probability-weighted outcome sits near the price: good but not compelling, so AVOID until H2 2026 results show whether margins hold.",
  "price_at_decision": 19.64,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-1378/2026-10-19.md",
  "triggers": [
    {"text": "H2 2026 results (due Nov 20, 2026, stockanalysis.com filings) show gross margin holding at or above the FY2025 level of 25.1%, showing the share-price fall was not a margin turn; this would justify re-research for a BUY."},
    {"text": "TTM gross margin falls below 15%, back toward the FY2022 trough of 13.8%, confirming the cyclical downturn the price anticipates.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.26x TTM now), rebuilding toward the FY2022 peak of 1.76x and removing the balance-sheet cushion.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 28.0, "basis": "H2 2026 results show TTM gross margin near 27.9% [IS] and EV/EBITDA re-rates from 3.8x toward its 5y median 4.6x [RA], between the EV/EBITDA method's base 15.34 and bull 25.02 and the 6-month swing area [HI]; below the mechanical 35.83 base because that DCF capitalises cycle-high margins."},
    "base": {"probability": 0.45, "target_price_12m": 20.0, "basis": "Margins ease from the TTM 27.9% toward the FY2025 25.1% [IS] while EV/EBITDA stays near 3.8x [RA], leaving the shares roughly flat; macro overlay's moderate bear tilt (dollar/real yields, research/HKG-1378/2026-10-19-macro.md) keeps re-rating off the table."},
    "bear": {"probability": 0.35, "target_price_12m": 11.0, "basis": "Gross margin reverts toward the FY2022 trough of 13.8% [IS] as the six-month -49.7% fall [HI] anticipates; value converges between the EV/EBITDA method's bear 8.75 and base 15.34 [fact sheet fair value]; probability raised for the overlay's moderate bear tilt (research/HKG-1378/2026-10-19-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades well below base fair value; the open question is whether peak-cycle margins hold through the H2 2026 results (Nov 20, 2026), so a lower price on the same evidence would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
