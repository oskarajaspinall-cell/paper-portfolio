# Evaluation: Equinor ASA (EQNR) — 2026-11-15
## Bear case
Equinor is a price-taker on oil and European gas; the TTM rebound (ROIC 22.3% vs 11.6% a year earlier, operating margin 32.1% vs 26.5%) is a commodity recovery, not a better business, and the 3-year direction is still falling [Likely]. The stock is up 66.9% in 12 months and trades 12.1% above its 200-day average, with P/B 2.2x above its 5y maximum and P/FCF at the 83rd percentile of its range [Certain]: an extended price risks a de-rating if prices or growth slow [Likely]. Q3 missed on earnings and revenue, and Visund was shut by a fire with unknown duration [Likely]. The DCF base of 719.28 NOK sits beside a 2,236.97 NOK bull, a spread too wide to anchor on [Likely]. Net margin of 9.8% leaves thin cover for buybacks and dividends if prices fall [Guessing].
## Bull case
Low-cost, long-life Norwegian shelf assets and a near-unlevered balance sheet (net debt/EBITDA 0.12x, Piotroski 7) let Equinor return cash through the cycle [Certain]. Shares are down 7.43% YoY from buybacks, with a fourth 2026 tranche running [Certain]. At 8.9x P/E and 2.2x EV/EBITDA it trades well below the peer medians of 13.4x and 4.5x, with an 11.26% FCF yield [Certain]. The reverse DCF already prices -12.7% year-1 revenue growth, so a fall is partly in the price [Likely]. The 2026 production growth outlook was raised despite the Q3 miss [Likely]. The trend is healthy: above the 200-day average, beating SPY by 56.5pp over 12 months, RSI 46.9 not overheated [Certain].
## Decision
```json
{
  "ticker": "OSL:EQNR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year fall in ROIC, operating margin and FCF margin is normalisation from the FY2022 commodity peak (ROIC 67.2%) with the balance sheet intact (net debt/EBITDA 0.12x [RA]); all three have risen over the last 12 months (ROIC 11.6% -> 22.3% [RA-T]).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Oil and European gas prices normalise from TTM levels, pulling earnings back toward FY2025 (ROIC 10.3%) and de-rating a price that is up 66.9% in 12 months.",
    "veto": null
  },
  "thesis": "A low-cost, near-unlevered North Sea producer returning cash through buybacks, but its TTM earnings ride a commodity recovery the price already reflects.",
  "rationale": "Cheap against peers with an 11.26% FCF yield and a real uptrend, but earnings are commodity-driven and near a cyclical high, own-history multiples sit high in their ranges, and the mechanical DCF is too wide to rely on. Good but not compelling: AVOID.",
  "price_at_decision": 407.60,
  "price_date": "2026-11-13",
  "research_note": "research/OSL-EQNR/2026-11-15.md",
  "triggers": [
    {"text": "ROIC TTM falls below 10% (ratios page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "FCF margin TTM falls below 5%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Net debt / EBITDA rises above 1.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Shares change YoY turns positive (buybacks stop shrinking the count)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 535.9, "basis": "Commodity prices hold, TTM earnings persist and P/E re-rates to its 5y max of 11.7x [RA], still below the peer median of 13.4x; below the DCF bull of 2,236.97 NOK, which the note judges unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 420.0, "basis": "TTM earnings roughly hold and P/E stays near 8.9x [RA] while buybacks (shares -7.43% YoY [ST]) lift per-share value modestly; well below the DCF base of 719.28 NOK because TTM sits above mid-cycle and the DCF spread is too wide to anchor on (note section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 299.06, "basis": "Commodity prices normalise and earnings fall back toward FY2025 (ROIC 10.3% [RA]), matching the mechanical DCF bear of 299.06 NOK [fact sheet Fair value]."}
  },
  "entry_price": 361.8,
  "entry_basis": "P/E back at its 5y median of 7.9x [RA] on TTM earnings (407.60 x 7.9 / 8.9); the DCF base x 0.8 is above the price and the DCF is judged unreliable, so the own-history multiple anchors it.",
  "replaces": null,
  "replacement_reason": null
}
```
