# Evaluation: Fortescue Ltd (ASX:FMG) — 2026-11-17
## Bear case
Returns have roughly halved from the peak: ROIC 38.3% to 17.0%, operating margin 52.3% to 32.1%, and operating margin is still falling over the last year (-1.1pp), 14.6pp below its 2-year high [Certain]. The cause is the iron ore price, which Fortescue cannot set: the moat is cost position, not pricing power [Likely]. The price fall has a stock-specific reason, not just the cycle: first-quarter shipments fell on maintenance and management reportedly warned of a shipment guidance cut if the China Mineral Resources Group talks are not concluded, unverified from a primary source [Likely]. That is a single-buyer access risk a cheap multiple does not protect against [Likely]. Green-energy capex competes with the dividend [Guessing], and governance noise (an executive fired, founder key-person questions) adds discount [Guessing]. The macro overlay leans small toward bear: real yields and the dollar are rising [Certain].
## Bull case
The balance sheet is clean (net debt/EBITDA 0.10x, Altman Z 4.36) and cash conversion is strong (FCF/net income 127.4%, FCF yield 12.61%) [Certain]. The decline looks cyclical, not structural: over the last year ROIC, ROCE and FCF margin were flat to slightly up, and FY2026 delivered record shipments [Likely]. The stock is cheap on its own history and peers: EV/EBITDA 3.6x is below its 5y minimum of 3.7x and below the peer 5.2x, P/FCF 7.9x is below its 5y minimum of 8.6x [Certain]. A concluded CMRG agreement would remove the main overhang and let the multiple move toward its 5y median 4.4x, near the base fair value of 16.70 [Likely]. The market already prices weak ore and China-access risk (12-month change -32.7%) [Likely].
## Decision
```json
{
  "ticker": "ASX:FMG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin and ROIC fell with iron ore prices from FY2022 while the balance sheet stayed intact (net debt/EBITDA 0.10x [BS,IS], Altman Z 4.36 [ST]); over the last year ROIC, ROCE and FCF margin were flat to up [RA-T, CF-T] and FY2026 shipments were a record (https://stockanalysis.com/quote/asx/FMG/transcripts/654293-agm-2026/).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "China Mineral Resources Group talks stall and shipment guidance is cut, hitting volume and margin at a single dominant buyer (https://www.wsj.com/business/fortescue-warns-of-output-guidance-cut-if-china-talks-arent-concluded-soon-3eaed714); unverified from a primary source but management-sourced.",
    "veto": null
  },
  "thesis": "A low-cost, net-cash-like Pilbara iron ore miner trades below its own 5-year minimum EV/EBITDA and P/FCF at a cyclical trough, but an unresolved China buyer negotiation threatens volumes.",
  "rationale": "Cheap and financially strong, with a cyclical rather than structural return decline, but the stock-specific fall reflects an unresolved CMRG negotiation and a reported guidance-cut warning, not an overreaction. Commodity-price exposure limits the moat. The scorecard lands at 3, below the buy bar, so no position.",
  "price_at_decision": 14.42,
  "price_date": "2026-11-16",
  "research_note": "research/ASX-FMG/2026-11-17.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, showing the trough is deepening beyond a normal iron ore cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15%, showing green-energy capex or lower ore prices are eroding cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.0x, ending the clean balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "The company cuts iron ore shipment guidance or announces a failed or loss-making CMRG arrangement in a primary release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 18.88, "basis": "CMRG agreement concludes and margins stabilise, so EV/EBITDA moves toward its 5y max 5.1x [RA], matching the mechanical bull fair value 18.88 [valuation file]; probability trimmed for the overlay's small bear tilt (research/ASX-FMG/2026-11-17-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 16.0, "basis": "Talks drag on but shipments hold; EV/EBITDA recovers part way to its 5y median 4.4x [RA] on TTM EBITDA [IS], a little below the base fair value 16.70 given the overlay's small bear tilt on real yields and the dollar (research/ASX-FMG/2026-11-17-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 12.5, "basis": "Shipment guidance is cut on the CMRG dispute (WSJ headline in the fact sheet) and operating margin keeps falling [IS-T], so EBITDA drops while EV/EBITDA stays below its 5y min 3.7x [RA]; below the bear fair value 14.00 because that holds EBITDA flat; weighted up per the overlay's tilt toward bear (research/ASX-FMG/2026-11-17-macro.md)."}
  },
  "entry_price": 14.195,
  "entry_basis": "valuation file: base 16.70 x 0.85; at that price the same evidence would add discount points, though resolution of the CMRG talks would matter more than price.",
  "replaces": null,
  "replacement_reason": null
}
```
