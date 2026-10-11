# Evaluation: Norwegian Cruise Line Holdings Ltd. (NCLH) — 2026-10-11
## Bear case
The balance sheet carries all the risk. Net debt/EBITDA is 6.08x TTM, barely improved on FY2024's 5.82x, and the Altman Z of 0.35 is in the distress zone [Certain]. TTM FCF margin is -11.7%, so newbuilds are debt-funded: NCLH upsized a senior-notes deal to $950m on 2026-09-30 [Certain]. At this leverage, equity is a thin slice of EV. A small cut to the 8.8x EV/EBITDA multiple or to EBITDA moves the share price several times as much [Likely]. The macro overlay shows HY spreads up 0.45pp and the 10y up 0.68pp over 3 months, making each refinancing dearer [Certain]. Short interest is 20.86% of float and rose 31.2% in a month [Certain]. TTM ROIC of 8.3% sits below a cost of equity built on a 5.22% risk-free rate and a 1.96 beta, so the business may not earn its cost of capital [Likely].
## Bull case
Cruising is a three-player oligopoly with long newbuild lead times [Likely]. NCLH trades below its own 5-year minimum on every multiple: 8.8x EV/EBITDA vs a 10.0x minimum, and 9.8x P/E vs a 12.4x minimum. That is a 38-57% discount to the CCL/RCL/MAR median [Certain]. Operating margin has recovered to 15.3% and gross margin to 42.5% [Certain]. Shares fell 2.87% YoY [Certain]. Mechanical EV/EBITDA fair value is 20.59 / 24.20 / 35.90, all above the 15.57 close [Certain]. With a 20.86% short float, a good Q3 print (due Nov 3) could force short covering [Guessing]. Leverage works both ways, so a re-rating to the 5-year minimum multiple would lift the equity sharply [Likely]. Carnival's strong results on 2026-09-29 suggest industry demand is healthy [Likely].
## Decision
```json
{
  "ticker": "NCLH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A deeply discounted cruise operator whose recovered margins are offset by 6.08x net debt/EBITDA, negative FCF and a distress-zone Altman Z, so the discount is largely compensation for balance-sheet risk rather than mispricing.",
  "rationale": "The cheapness is real, but the equity is a levered option on refinancing conditions. FCF is negative, leverage is not falling, and new debt keeps being issued while spreads and yields widen. ROIC barely covers the cost of capital. That is not the good-business-plus-valuation profile a core position needs, so no position.",
  "price_at_decision": 15.57,
  "price_date": "2026-10-09",
  "research_note": "research/NCLH/2026-10-11.md",
  "triggers": [
    {"text": "Net debt/EBITDA falls below 5.0x (vs 6.08x TTM), showing real deleveraging rather than debt-funded growth.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 5.0}},
    {"text": "TTM FCF margin turns positive (vs -11.7%), ending reliance on new debt to fund the newbuild programme.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 0}},
    {"text": "TTM ROIC rises above 10% (vs 8.3%), clearly beating the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "Altman Z-score rises above 1.8 (vs 0.35), leaving the distress zone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 24.20, "basis": "EV/EBITDA re-rates toward its 5y range (min 10.0x / median 10.6x [RA]) as spreads ease; this matches the mechanical base fair value of 24.20 rather than the 35.90 bull, because 6.08x leverage [BS,IS] and Altman Z 0.35 [ST] argue against a full peer-style multiple."},
    "base": {"probability": 0.45, "target_price_12m": 16.50, "basis": "EV/EBITDA stays near today's 8.8x, below its 10.0x 5y minimum [RA], because deleveraging stalls with FCF margin at -11.7% [CF,IS] and debt funding newbuilds (the $950m notes, per the note); this sits below the mechanical bear fair value of 20.59 because that model assumes the multiple returns to its own history."},
    "bear": {"probability": 0.35, "target_price_12m": 11.00, "basis": "The macro overlay (research/NCLH/2026-10-11-macro.md, moderate tilt toward bear) cites HY spreads +0.45pp and the 10y +0.68pp over 3m, which de-rate EV/EBITDA below 8.8x [RA]; at 6.08x net debt/EBITDA [BS,IS] a small EV cut takes the equity below the 13.63 52-week low [HI]; bear probability raised for the overlay."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5y minimum multiples and under the mechanical bear fair value. The block is the balance sheet (6.08x net debt/EBITDA, -11.7% FCF margin, Altman Z 0.35), so a lower price would not change the decision; the triggers above would.",
  "replaces": null,
  "replacement_reason": null
}
```
