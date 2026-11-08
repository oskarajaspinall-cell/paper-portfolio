# Evaluation: Ningbo Deye Technology Group (SHA:605117) — 2026-11-08
## Bear case
The price sits essentially at the mechanical base fair value (81.16 vs 79.89), so there is no margin of safety, and the bear value of 23.89 shows how far a de-rating could go [Certain]. The **Direction change** matters: rolling ROIC jumped from 67.8% to 152.6% and FCF margin from 21.6% to 33.7%, but FCF conversion of 136.1% of net income looks driven by working capital, which reverses [Likely]. Underneath, operating margin is flat at 27.7% and below its 2-year high of 29.4%, and gross margin has eased to 36.5% from 38.0% in FY2025 [Certain]. Product mix, export exposure and the Q3 2026 content are unverified; the stock hit its low of 65.82 the day after the report [Guessing]. EV/Sales and P/B sit well above peers [Certain]. Six-month momentum of -27.5% suggests the market doubts peak earnings [Likely].
## Bull case
Returns are exceptional and real: ROCE 49.5% TTM, ROE 50.0%, net cash (net debt/EBITDA -1.79x), Altman Z 5.64, no dilution (shares -0.26% YoY) [Certain]. Margins stepped up from FY2021 and have held near 27% operating for four years, suggesting a differentiated product [Likely]. Multiples are at the floor of their own history: P/E 19.9x vs a 5y median of 24.6x, EV/EBITDA 15.4x vs 20.8x, P/FCF 14.7x below its 5y minimum, FCF yield 6.82%, and P/E is well below peers [Certain]. The reverse DCF needs only 9.4% year-1 growth, modest for a business with this record [Likely]. Insiders own 23.00%, aligning management [Certain]. If the Q3 reaction was an overreaction, a re-rating toward median multiples offers meaningful upside [Guessing].
## Decision
```json
{
  "ticker": "SHA:605117",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, very high-return electrical equipment maker trades at the bottom of its own multiple ranges, but the price already equals the mechanical base fair value and the durability of its margins and the recent cash surge are unverified.",
  "rationale": "Quality and own-history multiples are attractive, but base fair value offers no margin of safety, the bear value is far below, the FCF surge looks working-capital driven, operating margin sits below its 2-year high, and the business mix and Q3 reception are unresearched. Good but not compelling: AVOID, watch for a lower entry.",
  "price_at_decision": 79.89,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-605117/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 22% (27.7% now), showing the post-2021 margin step-up is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM gross margin falls below 32% (36.5% now), signalling price competition or loss of product differentiation.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 32}},
    {"text": "TTM FCF margin falls below 15% (33.7% now), meaning the cash surge reversed beyond normal working-capital swings.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Rolling ROCE on the trailing ratios page falls below 30% (49.5% now), giving up the recent returns gain and the FY2022-FY2025 level."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 98.0, "basis": "P/E re-rates partway from 19.9x toward its 5y median 24.6x [RA] on held TTM earnings as ROCE stays near 49.5% [RA-T]; below the mechanical bull of 163.96 because that value needs sustained peak growth the evidence does not show."},
    "base": {"probability": 0.45, "target_price_12m": 81.16, "basis": "Operating margin holds near 27.7% [IS-T] and multiples stay near the floor of their 5y range [RA], so the price tracks the mechanical base fair value of 81.16 [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 45.0, "basis": "The working-capital-driven FCF surge (conversion 136.1% TTM vs 85.1% FY2025 [CF,IS]) unwinds and earnings fall from peak, taking value to near the EV/EBITDA method base of 44.92 [fact sheet Fair value]; above the mechanical bear of 23.89 because net cash and ROCE far above the cost of capital limit the downside."}
  },
  "entry_price": 64.93,
  "entry_basis": "valuation file: base 81.16 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
