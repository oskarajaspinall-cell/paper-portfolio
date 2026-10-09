# Evaluation: T-Mobile US, Inc. (TMUS) — 2026-10-09
## Bear case
The research could not find out why the stock fell again today. No 8-K was filed, the IR pages returned 403, and the only catalyst on record is the Oct 8 SpaceX spectrum deal that hit all three carriers [Certain]. A second leg down on no company news usually means the market is pricing a structural threat: a satellite entrant with its own spectrum, plus deeper promotions (Mint's "any plan for $10/month") [Likely]. TMUS cannot absorb that cheaply. Net debt/EBITDA is 3.42x, Altman Z is 1.80, and buybacks are funded by FCF that depends on pricing power [Certain]. Even after the fall it trades at a premium to peers (EV/EBITDA +24%, P/E +119%) [Certain], so mean reversion could be toward 7.1x, not back to its own history [Likely]. The macro overlay tilts moderately bear: real yields are up 0.61pp in 3m on a levered bond proxy [Certain]. Q3 results land Oct 28 [Certain].
## Bull case
The fundamentals have not moved. ROIC rose from 5.4% to 8.9%, operating margin from 12.5% to 22.1%, and FCF margin from 2.0% to 20.0%, while leverage fell from 4.08x to 3.42x [Certain]. The stock is below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 10.01% FCF yield. That is before today's further fall [Certain]. At 171.31 the reverse DCF already implies -6.1% revenue growth, an outcome no filed figure supports [Certain]. Capital returns are real: shares are down 3.93% YoY and the dividend was raised 15% on Sept 24 [Certain]. Satellite-to-handset capacity is limited by physics, and the incumbents have their own satellite JV [Likely]. A sector-wide sentiment flush on a contracted-revenue franchise has historically been a buying opportunity [Guessing].
## Decision
```json
{
  "ticker": "TMUS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging, 20%-FCF-margin wireless franchise trades below its own 5-year multiple floors, but a two-day, unexplained competitive repricing (SpaceX spectrum, Mint promotions) is unresolved until Q3 results on Oct 28.",
  "rationale": "Today's fall has no filed cause, so it confirms the competitive risk rather than refuting it. Cheapness alone does not make conviction 4 when the open question is whether pricing power and FCF hold. Leverage at 3.42x and a bear-tilted rate backdrop add to that. Q3 results resolve it within three weeks. Cash is acceptable.",
  "price_at_decision": 171.31,
  "price_date": "2026-10-08",
  "research_note": "research/TMUS/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 15%, giving back over a quarter of the 20.0% TTM level and showing that promotions and satellite competition are eroding cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 19.5%, the FY2023 level, reversing the post-merger expansion to 22.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19.5}},
    {"text": "TTM ROIC falls below 8.1%, the FY2024 level, ending the five-year rise to 8.9%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.1}},
    {"text": "Q3 2026 results (Oct 28) or a filing show T-Mobile's own spectrum position or service pricing materially impaired by the SpaceX spectrum deal; conversely, a clean quarter with intact guidance would remove the open question and justify re-research for a BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 220.0, "basis": "The competitive scare fades after a clean Q3, and EV/EBITDA returns to its 5y median of 10.5x [RA], in line with the fact sheet's EV/EBITDA fair value of 220.17. The DCF bull of 324.65 is excluded because its -34.69 to 324.65 range is too unstable for a 3.42x-levered telecom."},
    "base": {"probability": 0.45, "target_price_12m": 175.0, "basis": "Fundamentals hold (FCF margin 20.0% [CF,IS], ROIC 8.9% [RA]) but the satellite/spectrum overhang caps the multiple near its current 8.8x EV/EBITDA [RA], with returns coming from the 10.01% FCF yield [ST] through buybacks; this is well below the mechanical DCF base of 275.91, which the market rejects at an implied -6.1% growth."},
    "bear": {"probability": 0.30, "target_price_12m": 117.0, "basis": "The SpaceX spectrum deal (CNBC, 2026-10-08, fact-sheet headline [OV]) and Mint's $10 promotion force a price war, and EV/EBITDA derates to the 7.1x peer median [P:VZ,P:T,P:CHTR] on 3.42x leverage [BS,IS]. Bear probability is raised by the macro overlay's moderate bear tilt (research/TMUS/2026-10-09-macro.md: real yields +0.61pp in 3m on a levered bond proxy)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock already trades below its own 5-year multiple floors at a 10.01% FCF yield [RA,ST]. What blocks conviction 4 is the unexplained, unresolved competitive event (SpaceX spectrum, promotional pricing), so a lower price alone would not change the decision; the Q3 2026 results on Oct 28 are the re-research trigger.",
  "replaces": null,
  "replacement_reason": null
}
```
