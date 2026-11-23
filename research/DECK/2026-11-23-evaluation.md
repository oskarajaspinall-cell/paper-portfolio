# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-11-23
## Bear case
Management cut its sales outlook on 2026-10-22 and blamed aggressive rival discounting, weaker domestic DTC traffic and mixed product updates [Certain]. HOKA and UGG are fashion-driven brands; a moat built on full-price selling can erode fast once growth slows [Likely]. TTM ROIC fell to 66.5% from 72.7% a year earlier and sits far below its 2-year high of 131.4% (the Direction change line) [Certain]; if that reflects weaker demand rather than invested-capital normalisation, the high-return story is fading [Guessing]. TTM gross margin of 58.9% is flattered by non-recurring IEEPA tariff refunds [company-reported], so the underlying margin is lower than it looks [Certain]. The price is 20.3% below its 200-day average with 6-month relative strength of -13.7pp: no trend support, and a cheap multiple can stay cheap or fall further if earnings decline [Likely]. The European 3PL transition raised chargeback reserves [Certain].

## Bull case
This is a net-cash brand owner (net debt/EBITDA -0.48x) with FY2026 ROIC of 104.4%, TTM operating margin of 23.6% flat on a year earlier and ROCE at its 2-year high of 45.7% [Certain]. The ROIC drop is a denominator effect (cash build, invested capital), not margin erosion, since operating and FCF margins are flat over the last year [Likely]. Every multiple sits below its 5y minimum: P/E 10.3x versus a 13.9x low, EV/EBITDA 7.0x versus 9.3x, a 10.12% FCF yield [Certain]. The reverse DCF prices revenue shrinking 3.4% in year 1, harsher than a slowed-but-positive outlook (Q2 revenue still grew 3.5% and margin expectations rose) [Likely]. Shares fell 6.97% YoY; buybacks at this multiple compound per-share value if the brands hold [Certain]. Base fair value 111.00 sits well above the price [Certain].

## Decision
```json
{
  "ticker": "DECK",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM ROIC fell (72.7% -> 66.5%, RA-T) and FCF margin is -1.1pp over 3 years but flat over the last year at 18.9% (CF-T); operating margin is flat at 23.6% and ROCE rose to its 2-year high of 45.7% (IS-T, RA-T), so the drop reflects cash build and invested capital rather than lost pricing; the guidance cut slowed growth but kept it positive (research/DECK/2026-11-23.md).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Rival discounting and slowing HOKA/UGG growth force markdowns that erode the full-price gross margin, turning a valuation discount into a value trap.",
    "veto": null
  },
  "thesis": "A net-cash, very high-return footwear brand owner with flat margins and ROCE at its 2-year high trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 10.12% FCF yield, pricing a revenue decline its slowed-but-positive outlook does not show.",
  "rationale": "Same evidence as the 2026-11-15 HOLD: margins intact, ROIC dip explained by capital build, multiples below their 5y floor. The guidance cut and discounting cap conviction at the hold level; cash sits near the 1.5% floor (owner rule: residual cash), so there is no room to add without a swap. Keep the current size.",
  "price_at_decision": 77.94,
  "price_date": "2026-11-20",
  "research_note": "research/DECK/2026-11-23.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 55.6%, showing rival discounting or markdowns are eroding full-price discipline.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 14%, showing working capital or margin stress rather than a seasonal swing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 55%, showing the decline from 72.7% is no longer capital build but eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 55}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 135.0, "basis": "Discounting fades and growth holds, so P/E re-rates toward its 5y median of 17.6x [RA] on TTM earnings, below the 180.08 mechanical bull."},
    "base": {"probability": 0.5, "target_price_12m": 100.0, "basis": "Margins stay near 23.6% [IS-T] and P/E recovers toward its 5y minimum of 13.9x [RA], between the P/E-method base of 84.84 and the blended base fair value of 111.00."},
    "bear": {"probability": 0.25, "target_price_12m": 60.0, "basis": "Rival discounting [Reuters 2026-10-22, note] erodes gross margin toward the FY2024 55.6% [IS] once tariff refunds lapse, earnings fall and the multiple stays below its 5y minimum; above the 37.78 mechanical bear because net cash and buybacks support the floor."}
  },
  "entry_price": null,
  "entry_basis": "Held at conviction 4; the scorecard already gives the buy-level conviction, so no lower entry price applies.",
  "replaces": null,
  "replacement_reason": null
}
```
