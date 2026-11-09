# Evaluation: Sunny Optical Technology (HKG:2382) — 2026-11-09
## Bear case
Sunny is a cyclical, commoditised hardware supplier: gross margin of 19.5% TTM against 23.3% in FY2021, and ROIC fell to a 5.5% trough in FY2023, so the "below 5-year minimum" multiples are measured against a 2021 peak that is unlikely to return [Certain]. ROIC is down 5.1pp over the last 12 months (27.0% to 21.9%) even while margins rose, which points to a heavier capital base (vehicle/XR build-out) earning less per unit invested [Likely]. The mechanical fair value is flagged unreliable; the DCF alone (56.87) sits below the price and P/FCF is above peers [Certain]. Segment and geographic mix are unverified, so exposure to handset-volume cuts or export restrictions is unknown [Certain]. China policy and politics were not checked in the overlay [Certain]. Results due Nov 26, 2026 can reset the picture either way [Likely].

## Bull case
The business is in a verified recovery: operating margin 8.5% TTM vs 7.1% a year earlier, FCF margin 9.0% vs 3.1%, ROCE up from 8.9% to 12.4% [Certain]. H1 2026 revenue grew 11.5% with pan-IoT/XR and vehicle diversifying away from handsets (transcript) [Likely]. The ROIC dip looks temporary, a denominator effect from investment, since every margin and ROCE rose over the same 12 months [Likely]. The balance sheet is net cash (net debt/EBITDA -2.25x), Piotroski 7, Altman Z 3.87, no dilution [Certain]. At P/E 12.3x and EV/EBITDA 7.1x it trades below its own 5-year minima and well under peers on P/E and EV/EBITDA, while the reverse DCF only asks for 8.7% year-1 growth, below what H1 delivered [Certain].

## Decision
```json
{
  "ticker": "HKG:2382",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Python flags ROIC falling (27.0% to 21.9% over 12 months); over the same period operating margin (7.1% to 8.5%), FCF margin (3.1% to 9.0%) and ROCE (8.9% to 12.4%) all rose [RA-T, IS-T, CF-T], consistent with an investment-driven capital base rather than lost share; the 5-year decline is the FY2023 cyclical trough with net cash intact.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Handset optics pricing pressure in a commoditised market (gross margin 19.5% vs 23.3% FY2021 [IS]) could push margins back toward the FY2023 trough; segment mix is unverified.",
    "veto": null
  },
  "thesis": "A net-cash optical-components leader in a cyclical margin recovery trades below its own 5-year minimum multiples, but its returns are cyclical, its fair value is unreliable and its segment exposure is unverified.",
  "rationale": "Scorecard gives conviction 3: quality, direction and balance sheet score well, but with the blended fair value unreliable the value-blend upside is modest, the moat is only narrow in commoditised optics and segment mix is unverified. Good but not compelling, so AVOID (owner rule: only high conviction is bought); cash is acceptable.",
  "price_at_decision": 64.05,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2382/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 6%, back toward the FY2024 level of 5.9%, showing the recovery has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6}},
    {"text": "TTM ROIC falls below 15%, showing the ROIC slide is structural rather than an investment denominator effect.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 4%, back near the FY2024 level of 3.6%, showing the cash recovery was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "TTM gross margin falls below 18%, under the FY2024 level of 18.3%, signalling handset pricing pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 18}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 95.0, "basis": "Margin recovery continues and P/E moves toward the peer median 19.6x [RA,P], below the mechanical bull 113.33 because the 5y median multiples reflect the 2021 peak."},
    "base": {"probability": 0.5, "target_price_12m": 72.0, "basis": "Earnings grow with H1 2026 revenue growth of 11.5% [OV transcript] while multiples stay near their 5y lows; set below the unreliable blended base 85.50 and between it and the DCF base 56.87."},
    "bear": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Handset pricing pushes operating margin back toward the FY2024 5.9% [IS] on an unchanged 7.1x EV/EBITDA [RA]; above the mechanical bear 31.38, which assumes a trough-like outcome with net cash ignored."}
  },
  "entry_price": 56.0,
  "entry_basis": "Near the DCF base fair value 56.87 (valuation file), used instead of base 85.50 x 0.8 because the blended base is flagged unreliable and that level sits above the price.",
  "replaces": null,
  "replacement_reason": null
}
```
