# Evaluation: Pinnacle Financial Partners (PNFP) — 2026-11-09
## Bear case
Returns are sub-franchise: ROE 9.6% TTM, flat over five years and below a typical cost of equity [Certain]. Net margin fell from 40.2% to 25.5% TTM, and FCF margin dropped 20.5pp in the last 12 months to 35.8%, 26.0pp below its 2-year high; for a bank the FCF swing is largely balance-sheet noise, but the net-margin slide reflects merger dilution and costs not yet recovered [Likely]. Shares rose 71.92% YoY, so per-share value depends on a March 2027 systems conversion still ahead [Certain]. The price sits at the mechanical base fair value 100.44, which is itself flagged unreliable (methods disagree 4.5x), so there is no margin of safety [Certain]. P/E 13.7x is above peers' 12.2x [Certain]. Macro overlay: VIX up 13.2 in a month and hikes priced raise de-rating and deposit-cost risk for regional banks (small tilt toward bear) [Likely]. Piotroski F of 4 is middling [Certain].

## Bull case
Hiring-led organic growth is working: 222 revenue producers added year to date, loan growth 11% and core deposits 9% per management, with stable credit and FY26 guidance unchanged [Likely]. P/B 1.1x is at its 5y median and below the peer median 1.3x, so a successful integration could close that gap [Likely]. P/FCF 10.5x sits near the bottom of its 5y range and the FCF yield is 9.49% [Certain]. The reverse DCF implies only 1.3% year-1 revenue growth, undemanding for a bank growing in high-growth Southeast metros [Likely]. Merger cost synergies and revenue synergies after conversion could lift ROE back above 10% [Guessing]. The FCFE DCF base of 123.12 shows upside if cash generation holds [Guessing].

## Decision
```json
{
  "ticker": "PNFP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Net margin and FCF margin fall coincide with the merger (shares +71.92% YoY [ST]) and integration costs ahead of the March 2027 conversion; management reports stable credit and unchanged FY26 guidance (https://stockanalysis.com/stocks/pnfp/transcripts/713966-q3-2026/). Bank FCF swings with working capital, so the FCF drop is not a structural signal.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Merger integration and systems conversion (March 2027) slipping or eroding deposits, while a rising risk premium (macro overlay) de-rates regional banks.",
    "veto": null
  },
  "thesis": "A fairly priced Southeast regional bank with hiring-led growth but mediocre ROE and pending merger integration, offering no margin of safety at the mechanical base fair value.",
  "rationale": "ROE near 9.6% is below the quality bar, the price sits at base fair value (flagged unreliable) and P/E is above peers. Growth and the P/B discount to peers are real but already reflected; integration risk remains until March 2027. Not compelling: AVOID, cash is acceptable.",
  "price_at_decision": 100.64,
  "price_date": "2026-11-06",
  "research_note": "research/PNFP/2026-11-09.md",
  "triggers": [
    {"text": "ROE TTM falls below 8% (merger fails to earn its capital)", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "Net (profit) margin TTM falls below 22%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 22}},
    {"text": "Systems conversion slips beyond March 2027 or FY26 guidance is cut (company releases)"},
    {"text": "A sustained rise in charge-offs or non-performing loans in the quarterly release"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 125.0, "basis": "Integration on track and P/B re-rates toward the peer median 1.3x [RA], between the base and bull fair values (100.44 / 140.47) in the fact sheet."},
    "base": {"probability": 0.45, "target_price_12m": 100.44, "basis": "P/B stays near its 5y median 1.1x [RA] with ROE flat around 9.6% [RA], i.e. the mechanical base fair value 100.44."},
    "bear": {"probability": 0.30, "target_price_12m": 78.13, "basis": "Macro overlay tilts small toward bear (research/PNFP/2026-11-09-macro.md: VIX +13.2, hikes priced) so bear weight is raised; P/B de-rates toward its 5y low 1.0x [RA] and integration slips, near the bear fair value 78.13."}
  },
  "entry_price": 80.35,
  "entry_basis": "valuation file: base 100.44 x 0.8 (fair value flagged unreliable; also near the P/B 5y low 1.0x [RA]).",
  "replaces": null,
  "replacement_reason": null
}
```
