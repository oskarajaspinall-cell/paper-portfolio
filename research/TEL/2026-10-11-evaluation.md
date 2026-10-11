# Evaluation: TE Connectivity plc (TEL) — 2026-10-11
## Bear case
The price is already paying for growth. The reverse DCF implies 14.7% revenue growth in year 1, above TEL's recent organic trend [Likely] [fact sheet]. The house base fair value is $153.69 and even the bull case is $173.74, 29.6% and 20.4% below the $218.29 close [Certain]. P/B sits at the 86th percentile of its 5y range and EV/Sales at the 68th [Certain] [RA]. The 62% P/E discount to peers mostly reflects APH/GLW's AI premium, not cheapness at TEL [Likely]. ROIC fell from 18.7% to 11.5% over FY21-FY25 before the TTM rebound to 17.5% [Certain] [RA], so returns are cyclical. Auto is the largest end market [Likely]. The stock trails SPY by 19.0pp over 6 months [Certain] [HI]. FY Q4 results on 2026-10-28 are a binary event at a full multiple [Certain] [OV].
## Bull case
Margins are structurally higher. Gross margin is 36.1% TTM vs 32.7% in FY21 and operating margin 20.4% vs 18.2% [Certain] [IS]. FCF margin is 17.2% with 109.9% conversion [Certain] [CF]. Management cited AI/data connectivity orders up 70% this year, plus record orders and backlog supporting FY27 [Likely] (Jefferies/Q3 transcripts [OV]). Leverage is 0.92x net debt/EBITDA, Piotroski is 7 and the share count fell 2.07% YoY [Certain] [ST]. Design-in qualification cycles give sticky, multi-year revenue [Likely]. On EV/EBITDA, 13.7x sits near its 5y median of 13.0x and 21% below peers, so a re-rating toward AI-exposed peers is possible if data revenue keeps compounding [Guessing].
## Decision
```json
{
  "ticker": "TEL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, margin-expanding connector franchise with a credible AI/data growth leg, but at 21.4x P/E and 19.1x P/FCF the price already implies 14.7% year-1 growth and sits above every house fair-value scenario.",
  "rationale": "The business is good and improving, but the valuation leaves no margin of safety. Own-history multiples are mid-range, P/B is near its 5y high, the price is above even the bull fair value, and a binary FY Q4 print comes on 2026-10-28. The probability-weighted 12m value of about $203 is below the $218.29 close. Good, not compelling: AVOID.",
  "price_at_decision": 218.29,
  "price_date": "2026-10-09",
  "research_note": "research/TEL/2026-10-11.md",
  "triggers": [
    {"text": "TTM gross margin falls below 32%, under the FY21-23 trough of 31.5%-32.7%, signalling lost pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 32}},
    {"text": "TTM ROIC falls below 12%, back toward the FY2025 low of 11.5%, showing the return rebound was transitory.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.92x TTM), signalling debt-funded M&A or weakening cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Management commentary shows AI/data connectivity orders decelerating sharply from the 70% growth cited, showing the growth leg was cyclical rather than structural."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 252.56, "basis": "AI/data orders up 70% (Jefferies transcript [OV]) and FY27 backlog re-rate the stock back to its 52-week high of 252.56 [HI], still below the peer median P/E of 56.2x; this is above the mechanical bull fair value of 173.74 because that value cannot capture the new AI leg."},
    "base": {"probability": 0.5, "target_price_12m": 202.18, "basis": "EV/EBITDA holds near its 5y median of 13.0x [RA] on TTM EBITDA, matching the EV/EBITDA method's base value of 202.18 [fact sheet]; the DCF (129.45) is set aside as too punitive at a 5.22% risk-free rate."},
    "bear": {"probability": 0.25, "target_price_12m": 153.69, "basis": "Auto weakness or an AI-order slowdown removes the 14.7% growth the reverse DCF implies, so the price converges on the blended base fair value of 153.69 [fact sheet], close to the EV/EBITDA bear value of 157.86."}
  },
  "entry_price": 185.14,
  "entry_basis": "P/FCF back at its 5y low of 16.2x [RA] on TTM FCF (19.1x at 218.29), roughly a 6.2% FCF yield. This stays above the house base fair value x 0.8 (122.95) because the mechanical DCF ignores the margin step-up and the AI order book.",
  "replaces": null,
  "replacement_reason": null
}
```
