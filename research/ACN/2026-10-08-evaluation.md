# Evaluation: Accenture plc (ACN) — 2026-10-08
## Bear case
This looks cheap for a reason. ROIC has fallen every year, from 42.4% in FY2022 to 26.8% TTM, and ROCE from 31.5% to 22.8% [RA]. That fits AI tooling commoditising labour-based delivery work [Likely]. P/E of 14.5x and EV/EBITDA of 8.4x sit near the 5-year minimums, not below them, and are 7-8% above the peer median [RA,P] [Certain]. The whole IT-services group has de-rated, so there is no relative mispricing to close [Likely]. The stock is already up 38.3% in 3 months after the Q4 beat [HI] [Certain], so part of the rebound is priced. The fact sheet does not give revenue or bookings growth figures, so stabilisation cannot be checked with numbers [Certain]. The FBI-contractor data-breach story adds a public-sector reputational risk of unknown size [Guessing]. Net debt/EBITDA has moved from -0.54x to 0.04x [BS,IS] [Certain].
## Bull case
This is a high-return, cash-rich franchise at a cyclical-low multiple. Operating margin has held at 15.2-15.8% for five years and FCF margin has risen to 15.7% [IS,CF] [Certain]. FCF conversion is 138.9% of net income and the FCF yield is 9.91% [CF,ST] [Certain]. The share count fell 2.36% YoY [ST], so buybacks return cash even with no re-rating [Likely]. P/FCF of 10.1x is at its 5-year floor and 11% below peers [RA,P] [Certain]. Q4 drew a record-bookings headline and an upbeat outlook [OV headlines] [Likely]. The Dell business group shows partners still route AI infrastructure work through Accenture [Likely]. If growth steadies, the multiple has a long way back to its 5-year median P/E of 26.5x [RA] [Guessing].
## Decision
```json
{
  "ticker": "ACN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 15.7%-FCF-margin consulting franchise trades near its 5-year low multiples at a 9.91% FCF yield, but five years of falling ROIC and an AI threat to labour-based delivery make the discount look deserved rather than mispriced.",
  "rationale": "The business is high quality and cash-generative, but returns are falling every year, multiples are only at their 5-year floor and slightly above peers, and the 38.3% three-month rally has already priced part of the Q4 beat. This is good but not compelling: conviction 3, below the buy threshold. Macro is context only and changes nothing.",
  "price_at_decision": 196.64,
  "price_date": "2026-10-07",
  "research_note": "research/ACN/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, confirming the moat is being competed away rather than mean-reverting (TTM 26.8%).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 12%, showing cash-generation quality is deteriorating (TTM 15.7%).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM net margin falls below 9%, showing pricing/cost pressure spreading from returns into the P&L (TTM 11.3%).", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 9}}
  ],
  "exit_plan": null,
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 225, "basis": "Bookings strength stabilises growth and P/FCF re-rates from 10.1x to the 11.3x peer median [RA,P:IBM,P:CTSH,P:INFY,P:EPAM], helped by 2.36% annual share shrink [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 201, "basis": "P/E holds at 14.5x [RA] on TTM EPS lifted only by the 2.36% buyback-driven share-count decline [ST], as ROIC keeps drifting lower from 26.8% [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 170, "basis": "AI-driven pricing pressure extends the five-year ROIC slide (-14.4pp [RA]), cutting EPS by about 8% and compressing P/E to the 13.6x peer median [P:IBM,P:CTSH,P:INFY,P:EPAM]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
