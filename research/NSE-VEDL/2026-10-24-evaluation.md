# Evaluation: Vedanta Limited (NSE:VEDL) — 2026-10-24
## Bear case
The cheapness is probably not real. The stock is down 69.2% in six months, but trailing earnings, EBITDA and FCF still look like the pre-demerger group's, so P/E 4.5x, EV/EBITDA 3.9x and the 21.06% FCF yield set a smaller company's price against a larger company's profits [Likely]. Mechanical fair value (base 377.55 INR) is built on that same mismatch, so it can't be relied on [Likely]. Which segments the parent kept is unverified [Certain]. The returns are cyclical rather than proof of a moat: ROIC fell from 22.9% in FY2022 to 12.7% in FY2026, and net debt/EBITDA reached 2.88x in FY2025 [Certain]. Governance and regulatory risk is live: the Orissa HC bauxite ruling went against the company, and the contentious Niyamgiri push has been revived [Likely]. Results on Oct 28, 2026 could reset every figure [Certain].
## Bull case
If the retained business generates even part of the historical cash, the price is very low. The group delivered a 24.2% FCF margin and 107.1% FCF conversion in FY2026, with net debt/EBITDA back to 0.61x and Piotroski F 7 [Certain]. Every earnings multiple sits below its own 5-year minimum and well below the peer median of 10.9x P/E and 6.4x EV/EBITDA [Certain]. Even the mechanical bear fair value of 306.33 INR is above the 226.50 INR close [Certain]. Shares outstanding are barely changing (0.13% YoY), the zinc expansion in South Africa shows reinvestment in growth, and RSI 28.7 suggests selling is close to exhausted [Likely]. The Oct 28 results may give the first clean post-demerger figures [Likely].
## Decision
```json
{
  "ticker": "NSE:VEDL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Headline multiples far below history and peers most likely come from a demerger perimeter mismatch between the post-split price and pre-split consolidated financials, so the value case can't be verified.",
  "rationale": "The evidence for value rests on financials that probably describe a larger pre-demerger group, so neither the multiples nor fair value can be trusted. Add cyclical returns and governance/regulatory overhangs, and conviction is low. No position; re-research once post-demerger results (Oct 28) allow a like-for-like valuation.",
  "price_at_decision": 226.50,
  "price_date": "2026-10-23",
  "research_note": "research/NSE-VEDL/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin on post-demerger reported numbers falls below 15%, showing the retained business lacks the group's historical profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 2.5x, back toward the FY2025 peak of 2.88x, showing the parent's leverage is a balance-sheet risk.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM FCF margin turns negative on post-demerger figures, showing the historical cash generation does not carry over.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 306.33, "basis": "Post-demerger results show the parent keeps enough of the cash generation behind the FY2026 24.2% FCF margin [CF,IS] to support the mechanical bear fair value of 306.33 INR; base and bull fair value are set aside because they rest on the pre-demerger perimeter (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 226.50, "basis": "Like-for-like multiples turn out close to peers once the perimeter mismatch flagged in the note's section 3 is resolved, so the price holds around the 226.50 INR close [HI] rather than re-rating to the 377.55 INR base fair value."},
    "bear": {"probability": 0.30, "target_price_12m": 180.00, "basis": "The retained business earns cyclical, lower returns (ROIC fell from 22.9% to 12.7% FY2022-FY2026 [RA]) and the bauxite and Niyamgiri regulatory overhangs persist (note section 6), extending the 69.2% six-month fall [HI] below the 223.35 INR 52-week low."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the multiples and fair value rest on pre-demerger financials that probably don't match the current company, so a lower price on the same evidence would not justify conviction 4. Re-research on the post-demerger results.",
  "replaces": null,
  "replacement_reason": null
}
```
