# Evaluation: The Cooper Companies, Inc. (COO) — 2026-10-12
## Bear case
This is a value trap with falling quality, not a mispriced compounder. ROIC has slid from 8.0% (FY21) to 5.0% TTM, below any reasonable cost of capital [Certain] [RA]. Operating margin fell from 16.8% (FY25) to 12.9% TTM while gross margin held near 66%, so the squeeze is in operating costs, not one-off pricing [Certain] [IS]. September brought the second guidance cut of the year, blamed on U.S. channel-inventory reduction; two cuts make the "temporary" framing hard to trust [Likely] (SEC Q3 release). Leverage rose to 2.84x net debt/EBITDA, which limits buybacks if earnings keep falling [Certain] [RA]. Governance is unresolved: Jana wants a new CEO and asset sales, and a securities investigation is open [Likely] (Reuters, PRNewswire headlines [OV]). Short interest rose 14.0% in a month [Certain] [ST]. The mechanical bear fair value is $13.65 [Certain] (fact sheet).
## Bull case
Contact lenses are a recurring, replacement-driven franchise with ~66% gross margin [Certain] [IS]. The stock trades below its 5-year minimum EV/EBITDA (13.9x vs 15.3x), P/FCF (15.2x vs 30.0x) and P/B (1.2x vs 1.7x) [Certain] [RA]. FCF margin is 16.0% TTM with 119% conversion, a 6.56% FCF yield, and the share count is down 2.33% YoY [Certain] [CF,ST]. The reverse DCF implies only 5.6% year-1 growth [Certain] (fact sheet). The blended base fair value of $71.49 is +31.5% above the price [Certain]. Jana's campaign could force a CEO change or a CooperSurgical sale that unlocks value [Guessing]. If destocking really is a one-off, earnings rebound off a depressed base [Guessing].
## Decision
```json
{
  "ticker": "COO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A recurring contact-lens franchise is cheap against its own history, but falling ROIC (5.0% TTM), operating margin down to 12.9%, two guidance cuts and an open activist/legal overhang make the discount look earned rather than mispriced.",
  "rationale": "Valuation is attractive but the quality trend is the wrong way: returns are below the cost of capital, margins are falling, leverage is rising and the destocking story is unverified. The upside depends on governance change [Guessing], not on fundamentals. Good but not compelling at conviction 3, so no position. Cash is an acceptable outcome.",
  "price_at_decision": 54.37,
  "price_date": "2026-10-09",
  "research_note": "research/COO/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2025 level of 16.8%, showing the channel-inventory hit was temporary and cost pressure has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 16.8}},
    {"text": "TTM ROIC rises above 6%, breaking the five-year decline from 8.0% to 5.0%.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 6}},
    {"text": "Net debt/EBITDA falls below 2.5x, back under the FY2025 level of 2.51x, restoring room for buybacks.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.5}},
    {"text": "CooperVision organic revenue growth (company earnings release) is positive in both Americas and Asia-Pacific for two consecutive quarters, confirming destocking was a one-off and not share loss."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.0, "basis": "Jana forces a CEO change or CooperSurgical sale and margins recover, re-rating EV/Sales toward its 5y minimum 4.0x [RA] from 3.1x; held below the mechanical bull fair value 96.80 and the 52-week high 89.83 [HI] because ROIC stays weak."},
    "base": {"probability": 0.45, "target_price_12m": 62.0, "basis": "Destocking ends but operating margin stays near 12.9% TTM [IS]; price moves to roughly the midpoint of the DCF base 53.39 and blended base 71.49 (fact sheet), discounting the P/E leg because TTM EPS includes a net margin of 13.5% above the FY25 9.2% [IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 43.5, "basis": "A third guidance cut and continued margin compression cut EPS by about a fifth at the current 18.7x P/E [RA]; above the mechanical bear 13.65, which assumes a collapse that 66% gross margin [IS] and 16.0% FCF margin [CF] do not support."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC and operating margin are falling, the destocking explanation is unverified and the activist and securities-investigation overhang is unresolved, so a lower price would not change the decision; the base fair value 71.49 x 0.8 = 57.19 is already above the price. Revisit when the triggers above are met.",
  "replaces": null,
  "replacement_reason": null
}
```
