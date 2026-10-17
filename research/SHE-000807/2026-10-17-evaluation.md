# Evaluation: Yunnan Aluminium Co., Ltd. (SHE:000807) — 2026-10-17
## Bear case
The "cheap" multiples come from peak earnings. TTM gross margin of 25.9% and net margin of 16.6% are far above the FY2021-25 range (net 8.0%-10.1%) [Certain]. P/E of 8.0x and EV/EBITDA of 4.4x are below their 5y minimums only because the denominator has spiked [Likely]. On the stock's own normalized history, the EV/EBITDA method gives base value 19.20, below the 25.21 close [Certain]. Aluminium smelting is a commodity: no pricing power or structural barrier protects these returns when the cycle turns [Likely]. The price has fallen 30.8% in six months and sits below both moving averages, which suggests the market already sees a peak [Likely]. Q3 results on Oct 30, 2026 could confirm that margins are mean-reverting [Guessing]. The position would also add single-country CNY commodity-policy risk to a book that already has two China holdings [Certain].
## Bull case
The balance sheet is net cash (net debt/EBITDA -0.89x), FCF conversion is still above 100% (115.2%) and the FCF yield is 14.46%, so the company is paid well while it waits [Certain]. Piotroski F 8 and Altman Z 10.25 show no financial-distress risk [Certain]. The reverse DCF implies -2.1% revenue growth, which is not a heroic hurdle [Certain]. The through-cycle DCF, which already normalizes margins, puts base value at 32.36, above the price [Certain]. Even through FY2022-24, ROIC held at 17%-19%, so this is a better-than-average producer, integrated from alumina into metal [Likely]. If aluminium prices hold, trailing earnings are sustainable and P/E is below its 5y minimum [Guessing]. Macro is context only: CNY/USD has been stable per the overlay [Likely].
## Decision
```json
{
  "ticker": "SHE:000807",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, well-run integrated aluminium producer earning cycle-peak margins, whose low trailing multiples mostly reflect peak earnings rather than a mispriced durable franchise.",
  "rationale": "The blended base fair value is only modestly above the price, and the EV/EBITDA method is below it. The trailing cheapness rests on peak commodity margins with no moat, and results are due within two weeks. Good balance sheet and cash yield, but not compelling: cash is preferred.",
  "price_at_decision": 25.21,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000807/2026-10-17.md",
  "triggers": [
    {"text": "TTM net margin falls below 10%, back under the FY2025 level of 10.1%, confirming the TTM margin spike was a cycle peak now reversing.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 19%, back to the FY2021-24 range, removing the return premium that the bull case relies on.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 11.6%, the FY2024 five-year low, showing cash generation is weakening with the cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11.6}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 35.49, "basis": "Aluminium prices hold near TTM levels, so EBITDA is sustained and EV/EBITDA re-rates to the second method's bull value of 35.49 [RA,IS]; this is still below the 52-week high of 38.23 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 27.97, "basis": "Margins ease partway back toward the FY2021-25 range while net cash and the 14.46% FCF yield [ST] support the blended base fair value of 27.97 (through-cycle DCF 32.36, EV/EBITDA 19.20) [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 19.20, "basis": "Net margin reverts toward the FY2021-25 range of 8.0%-10.1% [IS] and the market values normalized EBITDA near its 5y median of 5.9x, matching the EV/EBITDA base value of 19.20 [RA]."}
  },
  "entry_price": 22.38,
  "entry_basis": "valuation file: base 27.97 x 0.8 (20% margin of safety); at that level even mid-cycle earnings would justify conviction 4, given the net cash.",
  "replaces": null,
  "replacement_reason": null
}
```
