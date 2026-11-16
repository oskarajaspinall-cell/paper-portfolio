# Evaluation: Grupo México (BMV:GMEXICO.B) — 2026-11-16
## Bear case
This is a copper price trade priced at peak margins. TTM operating margin 53.4% is the two-year high and matches FY2021's 53.0% peak, after which it fell to 40.9% by FY2023 [Certain]. The last-12-month rise in ROIC (18.7% to 24.9%) and operating margin (44.2% to 53.4%) comes mostly from higher metal prices, not a structural change, so it contradicts but does not overturn the falling 5-year trend [Likely]. P/B 3.6x and EV/Sales 4.6x are above their 5-year maxima and EV/EBITDA 7.6x sits near its 8.1x max [Certain]; the mechanical base fair value of 88.08 MXN, and even the bull case of 210.22 MXN, sit below the 220.15 MXN close [Certain]. An extended price on peak earnings risks a double hit, lower EBITDA and a lower multiple, if copper eases [Likely]. A controlling holder (insiders 19.37%) limits minority protection [Likely]. Revenue split by country is unknown, so Peru risk is unsized [Certain].
## Bull case
Grupo México owns low-cost, long-life copper deposits plus a hard-to-replicate rail franchise, a narrow moat [Likely]. Balance sheet is strong: net debt/EBITDA 0.36x, Altman Z 4.88 [Certain]. It trades well below peers: P/E -47%, P/FCF -59%, EV/EBITDA -16% versus SCCO, FCX and ANTO [Certain], with a 7.24% FCF yield and a falling share count (-1.73% YoY) [Certain]. The trend is working: price is 4.5% above its 200-day average, the 50-day is 8.1% above the 200-day, and the 12-month change is +38.5% [Certain]. The Q3 call cites mining cost improvements and record transportation results, with 2027 rail volume guidance of 5%–8% growth [Likely]. Declining out of the Belgrano Cargas bid hints at capital discipline [Guessing]. The peso is about 3.5% weaker over ~1m, which lifts the MXN value of USD earnings [Likely].
## Decision
```json
{
  "ticker": "BMV:GMEXICO.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are rising or flat (ROIC 18.7% to 24.9%, operating margin 44.2% to 53.4% [RA-T, IS-T]); the 5-year fall reflects the FY2021 copper peak, not a structural loss.", "moat": "narrow", "key_risk": "high", "key_risk_text": "Copper-driven margins at a cyclical high (operating margin 53.4%, matching the FY2021 peak [IS]) revert while the multiple sits near its 5-year max, de-rating an extended price.", "veto": null},
  "thesis": "A high-quality, low-leverage copper and rail group, cheap against peers but priced on peak-cycle margins well above its own-history fair value.",
  "rationale": "Quality and balance sheet are strong and the trend is working, but earnings sit at a cyclical peak and the price exceeds even the mechanical bull fair value, so the expected 12-month value sits below the price. Good, not compelling: AVOID at the scorecard's conviction.",
  "price_at_decision": 220.15,
  "price_date": "2026-11-13",
  "research_note": "research/BMV-GMEXICO.B/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 45%, showing the margin gain was price-driven and reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "ROIC (TTM) falls below 18%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA exceeds 1.5x, e.g. through a debt-funded acquisition.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "FCF margin (TTM) falls below 20% for two consecutive quarters.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 248.59, "basis": "Metal prices hold, TTM margins persist and EV/EBITDA moves toward its 5y max 8.1x [RA], retesting the 52-week high 248.59 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 200.0, "basis": "Margins ease from the two-year high [IS-T] and EV/EBITDA drifts below the current 7.6x toward its range [RA]; still above the mechanical base 88.08 because peers trade at 9.1x [RA,P]."},
    "bear": {"probability": 0.30, "target_price_12m": 120.0, "basis": "Copper reverts and operating margin returns toward the FY2023 40.9% [IS] while EV/EBITDA de-rates toward its 5y median 5.2x [RA], between the mechanical bear 74.88 and base 88.08."}
  },
  "entry_price": 70.46,
  "entry_basis": "valuation file: base 88.08 x 0.8; price on peak-cycle earnings is the obstacle, not quality.",
  "replaces": null,
  "replacement_reason": null
}
```
