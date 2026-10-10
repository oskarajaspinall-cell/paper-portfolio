# Evaluation: Marathon Petroleum Corporation (MPC) — 2026-10-10
## Bear case
MPC earns the crack spread with no pricing power, and the current spread is a war-driven supply shock (Iran/Hormuz, strikes on Russian refining) that commentary flags as reversal-prone [Likely]. TTM ROIC of 18.1% follows 9.8-9.9% in FY24-25 and 6.1% in FY21 [Certain]: the earnings base is a cyclical peak. The price already capitalises it: P/E 15.8x, EV/EBITDA 10.0x and P/B 6.8x all sit above their 5y maxima [Certain], and the close of 455.03 is 12.4% above base fair value of 398.76, with bear fair value at 99.54 [Certain]. Political risk is live: a possible diesel export ban and White House pressure on fuel prices before the midterms [Likely]. FY25 net debt/EBITDA of 3.24x shows buybacks were partly funded with debt [Likely]. With RSI at 73.5 and the stock up 141.1% in 12 months, the stock has no margin of safety [Certain].
## Bull case
Global refining capacity is short, and inventories are tight [Likely]. Q2 2026 delivered $8.5B adjusted EBITDA with 112% margin capture, and commentary expects Q3 to beat it [Likely]. TTM FCF yield is 10.09%, P/FCF of 9.9x is 23% below the peer median, and EV/EBITDA is 7% below peers [Certain]. Share count fell 6.60% YoY, so per-share compounding continues while spreads last [Certain]. TTM net debt/EBITDA has fallen to 1.72x [Certain]. The reverse DCF implies only -0.6% year-1 revenue growth [Certain]. If disruption persists into 2027, bull fair value is 631.29 [Certain]. Still, this case depends on the duration of a geopolitical shock that cannot be forecast, not on the quality of the business [Guessing].
## Decision
```json
{
  "ticker": "MPC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A no-moat refiner at a war-driven peak in crack spreads, trading above its 5y maximum P/E, EV/EBITDA and P/B and 12.4% above base fair value, so peak earnings are already priced in.",
  "rationale": "Core needs a good business at an attractive valuation; MPC is a cyclical price-taker at peak-cycle earnings, above every 5y multiple maximum and above base fair value, with political export-ban risk. A 10% FCF yield on peak FCF is not cheapness. Conviction 2, so no position; cash is preferable.",
  "price_at_decision": 455.03,
  "price_date": "2026-10-09",
  "research_note": "research/MPC/2026-10-10.md",
  "triggers": [
    {"text": "ROIC (ratios page) stays above 15% for both FY2026 and FY2027, showing a structurally higher mid-cycle return rather than a one-off spike."},
    {"text": "Net debt/EBITDA falls below 1.0x, showing buybacks are funded by organic FCF rather than leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 1.0}},
    {"text": "Annual net margin (income statement) holds above the FY2023 level of 6.5% for a full fiscal year after crack spreads normalise, showing gains are not just buyback-driven ROE inflation."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 631.29, "basis": "Supply disruption (WSJ 2026-10-08 headline [OV]) persists into 2027 and the price reaches the bull fair value of 631.29 (fact sheet Fair value, IS,BS,CF,RA,ST,HI)."},
    "base": {"probability": 0.45, "target_price_12m": 398.76, "basis": "Crack spreads ease from peak and the stock reverts to the blended base fair value of 398.76 (through-cycle DCF 67% + EV/EBITDA 33%, fact sheet Fair value), from P/E 15.8x vs 5y max 13.0x [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 279.17, "basis": "Spreads normalise toward FY24-25 levels (ROIC 9.8-9.9% [RA]) and EV/EBITDA reverts to the base EV/EBITDA fair value of 279.17; this is set above the 99.54 blended bear because buybacks (shares -6.60% YoY [ST]) and 12-month timing make a full trough unlikely."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2, below the entry-price threshold of 3. Business quality, not price, is the obstacle: a cyclical price-taker whose earnings depend on a geopolitical shock.",
  "replaces": null,
  "replacement_reason": null
}
```
