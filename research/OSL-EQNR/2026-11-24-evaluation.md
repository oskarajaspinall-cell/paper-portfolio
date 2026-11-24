# Evaluation: Equinor ASA (OSL:EQNR) — 2026-11-24
## Bear case
The 12-month rebound is commodity price, not business improvement: ROIC went 12.8% to 22.9% and operating margin 26.5% to 32.1% on the trailing view [RA-T, IS-T] while European gas sits elevated on a Hormuz crisis (headline [OV]) [Likely]. That is a cyclical upswing, so the **Direction change** lines flag a peak-ish TTM, not a turned trend; over 3 years every return metric is still falling [RA-T] [Certain]. If gas normalises, FY2025-type returns (ROIC 10.3%, FCF margin 5.6%) return and P/E of 8.3x on peak-ish earnings is not cheap [Likely]. P/B sits at the 85% point of its 5y range and P/FCF above its median [RA] [Certain]. The price is above the 200-day average, so any trend-strength credit is exposed to a de-rating if prices roll over [Likely]. The dip came from a cyberattack (stopped) and an ex-dividend date: no mispricing [Likely].
## Bull case
Balance sheet is near net cash (net debt/EBITDA 0.12x) with Piotroski 7 [ST] [Certain]. FCF yield is 12.02% and the share count fell 7.43% YoY, so cash returns are real and continuing, with a fourth buy-back tranche announced [ST, OV] [Certain]. EV/EBITDA of 2.0x is well below the 4.2x peer median and P/E 8.3x below the peer 10.7x [RA] [Certain]. The fall since our last research was event-driven (cyberattack stopped with no production impact) and was followed by an 18-year VNG gas supply deal, which supports long-dated European demand [Likely]. The reverse DCF implies a -15.5% year-1 revenue fall, so a lot of normalisation is priced [Likely]. Low-cost Norwegian shelf reserves and pipeline access to Europe give a narrow cost edge [Likely].
## Decision
```json
{
  "ticker": "OSL:EQNR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-FCF-yield Norwegian producer whose current returns are lifted by elevated gas prices; the cyberattack dip did not change the business or create a clear discount.",
  "rationale": "The fall is event-driven and does not break the business, but it also does not remove the obstacle from 2026-11-15: TTM returns look above mid-cycle on commodity prices, multiples sit near their own medians, and the DCF is unreliable. Cash returns and the balance sheet are strong, but the scorecard stays below the buy bar.",
  "price_at_decision": 380.5,
  "price_date": "2026-11-23",
  "research_note": "research/OSL-EQNR/2026-11-24.md",
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year fall in ROIC, operating and FCF margin is normalisation from the FY2022 commodity peak (ROIC 67.2% [RA]) with the balance sheet intact (net debt/EBITDA 0.12x [ST]); the trailing view has since risen (ROIC 12.8% to 22.9% [RA-T]). Cyclical, not lost share or a broken model.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "European gas and oil prices normalise from crisis-elevated levels (Hormuz headline [OV]), pulling returns back toward FY2025 (ROIC 10.3%, FCF margin 5.6% [RA, CF]) and de-rating a price that sits above its 200-day average.",
    "veto": null
  },
  "triggers": [
    {"text": "ROIC TTM falls below 10% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "FCF margin TTM falls below 5% (statistics page)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Net debt / EBITDA rises above 1.0x (statistics page)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Share count stops shrinking: shares change YoY turns positive (statistics page)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 454.6, "basis": "Gas stays elevated and EV/EBITDA moves to its 5y max 2.4x [RA], taking the price back to the 52-week high of 454.60 [HI]; the mechanical bull DCF (2,400.83) is flagged unreliable and ignored."},
    "base": {"probability": 0.45, "target_price_12m": 380.5, "basis": "P/E holds near its 5y median 7.9x [RA] as earnings ease from the TTM level while buybacks (shares -7.43% YoY [ST]) offset; flat price, below the unreliable DCF base of 771.87 because TTM earnings look above mid-cycle."},
    "bear": {"probability": 0.30, "target_price_12m": 320.92, "basis": "Gas normalises and returns fall back toward FY2025 (ROIC 10.3% [RA]); the mechanical bear fair value of 320.92 [IS,BS,CF] near the 6-month low 304.70 [HI]."}
  },
  "entry_price": 304.7,
  "entry_basis": "The base fair value is flagged unreliable (base x 0.85 sits above the price), so the anchor is the 6-month low of 304.70 [HI], near the bear fair value 320.92, where even normalised FY2025 earnings would leave a clear discount.",
  "replaces": null,
  "replacement_reason": null
}
```
