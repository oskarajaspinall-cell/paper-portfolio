# Evaluation: Range Resources Corporation (RRC) — 2026-11-15
## Bear case
RRC is no longer a standalone investment: an agreed all-stock merger fixes it at 0.987 EQT shares per RRC share [company-reported], so buying RRC buys EQT plus deal-break risk [Certain]. The close of 51.83 is above the mechanical base (46.32) and even the bull (49.18) fair value, P/B 2.5x sits above its 5y maximum and P/E 13.8x is well above the peer median 8.7x [Certain]. The trend points come from a deal jump, not a working business being re-rated: the price is 25.8% above its 200-day average, so a deal break or HSR condition would de-rate it toward standalone value [Likely]. Returns are cyclical: ROIC is down 13.7pp over three years, and operating and FCF margins sit 3.2pp and 3.8pp below their March 2026 highs as gas realisations eased [Certain]. Gas is a price-taker; the moat is cost, not pricing [Likely]. Merger covenants limit buybacks [Likely].
## Bull case
The underlying business is strong and improving over the last year: ROIC TTM 17.1% vs 12.5% a year earlier, operating margin 37.0% vs 27.7%, FCF margin 21.4% vs 17.2% [Certain]. Net debt/EBITDA is 0.55x, Piotroski 8, shares down 1.77% YoY [Certain]. The 3-year decline is the fade from the 2022 gas-price peak with the balance sheet intact, i.e. cyclical, not structural [Likely]. Q3 beat (headline) and the EQT combination targets synergies that accrue to holders through the exchange ratio [Likely]. If gas demand from LNG and power keeps rising, EQT, and so RRC, could rerate further [Guessing]. FCF yield 6.00% is real cash support [Certain].
## Decision
```json
{
  "ticker": "RRC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC (-13.7pp), operating margin and FCF margin are the fade from the 2022 gas-price peak; all three rose over the last 12 months and net debt/EBITDA fell to 0.55x [RA-T, IS-T, RA], so cyclical with the balance sheet intact.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The pending EQT merger: the price is pinned to EQT via the fixed ratio, and a failed vote or HSR block would de-rate RRC toward its standalone base fair value of 46.32 [sec.gov 10-Q].",
    "veto": {"code": "binary_event", "reason": "A pending all-stock merger with EQT (shareholder votes, HSR clearance, a $423 million termination fee [company-reported], https://www.sec.gov/Archives/edgar/data/315852/000119312526434351/rrc-20260930.htm) means the stock's outcome is a deal binary plus EQT's price, which the RRC scorecard cannot see."}
  },
  "thesis": "A strong, low-leverage Appalachian gas producer whose shares now trade as a fixed-ratio proxy for EQT above every mechanical fair value, so the RRC-specific opportunity has been captured by the deal.",
  "rationale": "Fundamentals are good, but the merger converts RRC into EQT stock plus break risk, and the price already sits above the base and bull fair values. There is no RRC-specific edge left to own; a binary-event veto caps conviction at 3, so AVOID.",
  "price_at_decision": 51.83,
  "price_date": "2026-11-13",
  "research_note": "research/RRC/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, showing the cyclical recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 28%, giving back the last year's gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.55x TTM now).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "The EQT merger agreement is terminated or not approved, shown by a Form 8-K on sec.gov, requiring a standalone re-underwrite."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 56.9, "basis": "Deal closes and EQT rerates on gas demand, taking RRC back to its 52-week high of 56.90 [HI] via the fixed ratio (sec.gov 10-Q)."},
    "base": {"probability": 0.6, "target_price_12m": 51.83, "basis": "Deal closes and RRC tracks EQT flat at the fixed ratio, above the mechanical base fair value 46.32 [valuation file] because the price reflects the deal, not RRC's own history."},
    "bear": {"probability": 0.2, "target_price_12m": 46.32, "basis": "Deal blocked or voted down and RRC reverts to its standalone EV/EBITDA base fair value of 46.32 [IS,RA,ST]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: while the EQT merger is pending, a lower RRC price only reflects EQT's price at the fixed ratio, so the same evidence would not justify conviction 4; re-research if the deal terminates.",
  "replaces": null,
  "replacement_reason": null
}
```
