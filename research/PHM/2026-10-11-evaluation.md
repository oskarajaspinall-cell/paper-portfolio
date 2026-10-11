# Evaluation: PulteGroup, Inc. (PHM) — 2026-10-11
## Bear case
PHM looks cheap only against peers. Against its own cycle it is expensive: P/E 11.4x and EV/EBITDA 8.0x are both above their 5-year maximums (118% of range), because earnings are falling faster than the price [Certain] (fact sheet). Returns are fading. ROIC is down to 14.5% from 25.0%, gross margin to 25.6% from 30.2%, and Piotroski is 4/9 [Certain]. The price implies 6.8% year-1 revenue growth, and base fair value of 89.03 sits 20.6% below the 112.12 close [Certain]. Macro is pulling the wrong way. The 10y yield is 5.22% and rose 68bp in 3 months, the Fed is still hiking, and credit spreads are widening (macro overlay, FRED 2026-10-08) [Certain]. Mortgage relief, which a re-rating needs, is not in sight [Likely]. Q3 results on Oct 22 could show higher incentives that push gross margin toward 24% [Guessing].
## Bull case
The balance sheet is sound for a homebuilder. Net debt/EBITDA is 0.42x, FCF/NI conversion is 79.3%, and 57% of lots are held under option rather than owned, which limits capital at risk in a downturn [Certain] (fact sheet; 10-K). Buybacks cut the share count 5.02% YoY, funded by a 7.20% FCF yield [Certain]. The stock trades 16-22% below the peer median on P/E and EV/EBITDA, and P/B of 1.6x sits below its 5y median of 1.8x [Certain]. It already reflects heavy pessimism: -12.2% over 12 months, -27.8pp versus SPY and RSI 36.2 [Certain]. If rates turn, builders typically re-rate from depressed sentiment before earnings recover [Likely], and bull fair value is 134.01 [Certain]. Still, the catalyst depends on rates, and the overlay says it has not arrived [Likely].
## Decision
```json
{
  "ticker": "PHM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-capitalised, buyback-funded homebuilder trades cheaply against peers but above its own 5-year multiples and 20.6% above base fair value, while rising rates work against the margin recovery that a re-rating needs.",
  "rationale": "The balance sheet and capital returns are good, but there is no margin of safety. The price sits above base fair value of 89.03, own-history multiples are above their 5y max, ROIC and margins are still falling, and the primary macro channel (10y at 5.22%, still rising) tilts toward bear. That makes this good but not compelling, so the answer is cash.",
  "price_at_decision": 112.12,
  "price_date": "2026-10-09",
  "research_note": "research/PHM/2026-10-11.md",
  "triggers": [
    {"text": "TTM gross margin falls below 24% (now 25.6%), showing incentive-driven margin erosion beyond what the price already discounts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 24}},
    {"text": "TTM ROIC falls below 10% (now 14.5%), meaning returns no longer clearly exceed the cost of capital through the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 1.0x, eroding the balance-sheet buffer that underpins buybacks in a downturn.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Q3 2026 or later results show net new orders and gross margin stabilising year on year, which would make the earnings trough visible and raise conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 134.01, "basis": "Rates ease and margins stabilise, so the stock re-rates to the fact sheet's bull fair value of 134.01 [IS,BS,CF,RA,ST]. Probability is trimmed because the primary macro overlay (research/PHM/2026-10-11-macro.md) tilts moderately toward bear."},
    "base": {"probability": 0.45, "target_price_12m": 96.78, "basis": "Rates stay elevated and earnings keep normalising from 25.0% to 14.5% ROIC [RA], so the price converges on DCF base value of 96.78 [IS,BS,CF,RA,ST]. That is above the blended base of 89.03 because buybacks (-5.02% shares YoY [ST]) and 0.42x leverage [BS,IS] support the multiple."},
    "bear": {"probability": 0.35, "target_price_12m": 73.53, "basis": "The 10y yield stays above ~5.5% and gross margin breaks 24% (macro overlay, moderate tilt toward bear, raises this probability), and the stock de-rates to the P/E-method base of 73.53 [IS,BS,CF,RA,ST]. That is well above the mechanical 30.75 bear because 57% optioned lots and low leverage limit impairment risk (10-K)."}
  },
  "entry_price": 71.22,
  "entry_basis": "valuation file: base 89.03 x 0.8 [IS,BS,CF,RA,ST]. At that price the same evidence (sound balance sheet, buybacks, cyclical margin pressure) offers enough margin of safety for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
