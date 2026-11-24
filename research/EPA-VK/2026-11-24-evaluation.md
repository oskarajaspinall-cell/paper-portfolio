# Evaluation: Vallourec S.A. (EPA:VK) — 2026-11-24
## Bear case
The fall follows real news, not noise: Q3 results on 2026-11-20 showed lower Tubes margin, a US subcontractor problem, Middle East port delays expected to cost again in Q4, and a lower Q1 2027 outlook [Likely]. Returns are already rolling over: ROIC 14.7% TTM vs 18.0% a year earlier and ROCE 15.0% vs a 2-year high of 19.2%, so the 5-year "rising" trend no longer describes the business [Certain]. TTM FCF margin of 12.6% overstates the run rate, as warrant proceeds flattered Q3 cash [Guessing]. The reverse DCF prices -6.7% year-1 revenue growth, and the mechanical bear fair value is negative, so the valuation range is too wide to anchor on [Certain]. Price trend is broken (28.1% below the 200-day, 50-day below 200-day), so no trend-strength support [Certain]. An oil-and-gas capex downturn would turn execution slippage into a cyclical earnings reset [Guessing].
## Bull case
Balance sheet is near net cash (net debt/EBITDA 0.15x) and FCF yield is 13.09%, so the company can absorb a soft patch [Certain]. On EV/EBITDA it trades 39% below peers and on P/FCF 47% below, at 4.9x EBITDA vs a 5y median of 5.2x [Certain]. The Q3 problems are execution and logistics, not demand: management said US pricing was still rising, Tubes volumes grew quarter on quarter and it guided growth momentum through 2027 [Likely]. Recent contract wins (TotalEnergies Absheron, Petrobras Sepia 2) support the order book [Likely]. Proprietary VAM connections and customer qualification give a narrow moat [Likely]. Shares outstanding fell 2.48% YoY [Certain]. Base fair value 18.91 sits above the price [Certain].
## Decision
```json
{
  "ticker": "EPA:VK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC/ROCE fell over the last 12 months on Q3 execution and logistics problems (US subcontractor, Middle East port delays) while management said US pricing was still rising and Tubes volumes grew; balance sheet near net cash (net debt/EBITDA 0.15x) (https://stockanalysis.com/quote/epa/VK/transcripts/679824-q3-2026/, [RA-T])", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Execution slippage merging with an oil-and-gas capex slowdown (lower Q1 2027 outlook) into a lasting margin reset below the 12% operating margin line.", "veto": null},
  "thesis": "A cash-generative, near-net-cash premium tubes maker at a cheap multiple, but returns are falling and the Q3 call widened near-term uncertainty, so the discount is not yet a clear mispricing.",
  "rationale": "Cheap on FCF and EV/EBITDA with a strong balance sheet, but the dip follows a genuine Q3 deterioration (lower margin, wide Q4 guidance, lower Q1 2027 outlook), returns are falling and the fair-value range is unreliable. Not an overreaction that clears conviction 4.",
  "price_at_decision": 14.81,
  "price_date": "2026-11-23",
  "research_note": "research/EPA-VK/2026-11-24.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "ROIC (TTM) falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "FCF margin (TTM) falls below 6%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt / EBITDA (ratios page, debt less cash) rises above 1.0x"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 20.70, "basis": "Q4/Q1 logistics issues clear and margins recover toward the FY2025 level, supporting the through-cycle DCF base of 20.70 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 15.33, "basis": "Margins stay near TTM levels and EV/EBITDA holds near its 5y median 5.2x [RA], matching the EV/EBITDA method base of 15.33; below the blended 18.91 because the DCF leg relies on peak-ish FCF flattered by warrant proceeds (note section 5)."},
    "bear": {"probability": 0.25, "target_price_12m": 10.20, "basis": "A capex downturn plus continued execution slippage cuts EBITDA, giving the EV/EBITDA bear value of 10.20; the negative DCF bear is ignored as unreliable."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the scorecard [RA, RA-T, ST] stays at 3 even with full valuation points, because ROIC, operating and FCF margin are falling and the Q3 execution problems are unresolved; a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
