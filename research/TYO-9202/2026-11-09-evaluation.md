# Evaluation: ANA Holdings Inc. (TYO:9202) — 2026-11-09
## Bear case
The recovery is complete and the cycle is now turning against ANA. ROIC (11.4% TTM vs 12.4% high), operating margin (7.6% TTM vs 10.1% in FY2024) and FCF margin (5.2% TTM vs 6.3% a year earlier, 3.8pp below its 2-year high of 9.0%) are all below their post-pandemic peaks [Certain]. The **Direction change** in FCF margin is driven by heavier fleet capex (FCF conversion 89.9% vs 135.1% in FY2026) [Likely]; fleet renewal is recurring for an airline, so part of it may not reverse [Guessing]. P/FCF 9.9x is above its 5y max of 8.3x [Certain]. The only usable fair value, EV/EBITDA, gives a base of 3,309.83 JPY, close to the 3,237 JPY price: mid-cycle earnings are already paid for [Likely]. Altman Z 1.57 and exposure to fuel, the yen and inbound tourism leave little margin for error [Likely]. RSI 74.5 after the post-results jump argues against chasing [Certain].
## Bull case
ANA is a near-unlevered (net debt/EBITDA 0.15x) half of a Japanese slot duopoly with JAL [Likely], earning ROIC 11.4% with ROIC flat over the last year (+0.2pp) [Certain]. It trades at EV/EBITDA 3.8x (16% of its 5y range, 35% below peers), P/B 1.0x (57% below peers) and a 10.09% FCF yield [Certain]. The reverse DCF implies -22.4% year-1 revenue decline, far worse than results show [Likely]. Q2 FY2027 results on 2026-10-29 drew a +6.3% move on 2.7x volume, with 208% of the jump held, suggesting the market is re-rating delivered earnings [Likely]. Buybacks (shares -1.09% YoY) and the AI-driven Asian air-cargo shift (Reuters, 2026-07-29) add optionality [Guessing]. Beta 0.45 makes it a low-correlation diversifier [Certain].
## Decision
```json
{
  "ticker": "TYO:9202",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC, operating margin and FCF margin are measured from the FY2024 post-pandemic recovery peak; the 1-year FCF margin fall coincides with lower FCF conversion (89.9% vs 135.1%) consistent with fleet capex, while ROIC is flat over 12 months and net debt/EBITDA is 0.15x [RA-T, CF-T, BS]. No share loss or price cap is evidenced.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Airline cyclicality: fuel, yen and inbound-tourism swings compressing an operating margin of 7.6% that is already below its 2-year high, with Altman Z at 1.57.",
    "veto": null
  },
  "thesis": "A near-unlevered Japanese duopoly airline trades at the low end of its own and peers' EV/EBITDA and P/B, but the only reliable fair-value method puts the price near mid-cycle value while cash margins are falling from their post-recovery peak.",
  "rationale": "Cheap against peers, but the mechanical fair value is unreliable and the EV/EBITDA method sits near the price, so the scorecard gives valuation no credit; FCF margin is falling with heavier capex and the scenarios' expected value does not clear the price. Conviction 2: AVOID, no position.",
  "price_at_decision": 3237.0,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-9202/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, showing returns are reverting toward pre-recovery levels.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM operating margin falls below 5%, signalling a cyclical downturn or cost squeeze beyond normalisation.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 5}},
    {"text": "TTM FCF margin falls below 2%, showing fleet capex is consuming the cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.15x TTM now), showing the balance sheet is funding fleet spend or losses.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3610, "basis": "EV/EBITDA method bull 3,610.20 JPY [valuation file]: the multiple moves up from 3.8x toward its 5y median 4.6x [RA] as Q2 FY2027 strength persists; the DCF bull is ignored as the fair value is flagged unreliable."},
    "base": {"probability": 0.5, "target_price_12m": 3310, "basis": "EV/EBITDA method base 3,309.83 JPY [valuation file] on TTM EBITDA with margins flat at 7.6% [IS-T]; the blended base of 11,337.22 is set aside because methods disagree 4.6x."},
    "bear": {"probability": 0.25, "target_price_12m": 2311, "basis": "EV/EBITDA method bear 2,311.25 JPY [valuation file]: FCF margin keeps falling from 5.2% [CF-T] and the multiple returns toward its 5y low of 3.2x [RA] in a fuel or tourism downturn."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
