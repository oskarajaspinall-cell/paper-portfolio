# Evaluation: Arch Capital Group Ltd. (ACGL) — 2026-11-23
## Bear case
The cycle is turning against Arch. Reinsurance net premiums written fell 9.3% in Q3 [company-reported] on abundant capacity, and management expects continued property-catastrophe pricing pressure (https://www.sec.gov/Archives/edgar/data/947484/000094748426000152/acgl-20260930.htm) [Likely]. TTM ROIC of 16.5% sits 6.9pp below its 2-year high of 23.3% and is 2.2pp lower over three years [RA-T]; light catastrophe activity flattered Q3, so reported returns overstate the run-rate [Likely]. The P/B + ROE fair value (177.68) assumes an ROE the soft market may not deliver; the P/E leg (99.30) sits below the price [Certain]. The stock is above its 200-day average with a 12-month change of +19.4% [ST]; if earnings fade, an extended price risks a de-rating toward its 5y median P/E of 8.1x [RA] [Likely]. The Pasquesi chair handover removes an architect of the cycle-management culture [Guessing].
## Bull case
Arch is a disciplined, diversified underwriter with ROE of 18.7% TTM and ROIC rising from 12.3% (FY2021) to 16.5% [RA] [Certain], and low leverage at 0.60x net debt/EBITDA [RA] [Certain]. The ROIC dip from the 2024 peak is the expected normalisation of a hard-market, benign-catastrophe year, flat over the last 12 months (+0.4pp) rather than collapsing [RA-T] [Likely]. Mortgage insurance and the insurance segment diversify away from reinsurance pricing [Likely]. Capital goes back to owners: shares fell 6.92% YoY [ST], with Q3 buybacks large relative to operating income [OV] [Certain]. The stock is cheap: P/E 8.9x and EV/EBITDA 7.4x, 14% and 37% below the peer median, EV/EBITDA at the 7th percentile of its own 5y range [RA] [Certain]. It trends well, beating SPY by +15.3pp over 12 months with beta 0.19 [ST] [Certain], and the base fair value is 151.55 [Likely].
## Decision
```json
{
  "ticker": "ACGL",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC is 2.2pp lower over three years and 6.9pp below its 2024-09-30 high of 23.3% [RA-T], but flat over the last year (+0.4pp); the peak was a hard-market, benign-catastrophe year and the balance sheet is intact (net debt/EBITDA 0.60x [RA]). Reinsurance softening is cyclical pricing, not lost franchise (note section 2, sec.gov 10-Q).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A softer reinsurance market plus a normal or heavy catastrophe year pushes ROE toward the low teens, and the stock, above its 200-day average after a +19.4% year, de-rates toward its 5y median P/E.",
    "veto": null
  },
  "thesis": "A disciplined, lowly levered specialty insurer earning high-teens ROE trades below peers and low in its own EV/EBITDA range while in a healthy uptrend, with buybacks compounding per-share value through a softening cycle.",
  "rationale": "Conviction 4 is unchanged a week after entry: returns normalised but flat over the last year, leverage is low, buybacks continue and the stock is cheap versus peers and its own EV/EBITDA history. The position sits near its target size, so HOLD; no new evidence justifies adding.",
  "price_at_decision": 108.82,
  "price_date": "2026-11-20",
  "research_note": "research/ACGL/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, showing the soft cycle is eroding returns beyond a normal cyclical dip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM ROE falls below 14%, well under the 18.7% now, signalling underwriting returns have broken down.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA rises above 1.5x, reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Insurance or reinsurance underwriting income turns negative in two consecutive 10-Qs (sec.gov)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 160.0, "basis": "ROE holds near 18.7% [RA] with benign catastrophes, so P/B re-rates toward the P/B + ROE base of 177.68, held below it and inside the mechanical bull of 169.00 because reinsurance pricing is softening (note section 2)."},
    "base": {"probability": 0.5, "target_price_12m": 122.0, "basis": "Between the P/E leg (99.30) and the P/B + ROE leg (177.68), weighted toward P/E because the note flags the P/B leg's sustainable-ROE assumption as optimistic in a softening reinsurance market; below the 151.55 blended base for that reason, with buybacks (-6.92% shares YoY [ST]) supporting per-share growth."},
    "bear": {"probability": 0.25, "target_price_12m": 88.0, "basis": "A heavy catastrophe year on softer reinsurance pricing (Q3 reinsurance premiums written -9.3% [company-reported], sec.gov 10-Q) cuts earnings and P/E de-rates toward its 5y median 8.1x [RA], near the mechanical bear of 86.01."}
  },
  "entry_price": null,
  "entry_basis": "Already at conviction 4 and held near its target size; price is not the obstacle, and an ADD would need new evidence rather than a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```
