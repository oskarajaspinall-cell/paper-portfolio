# Evaluation: MS&AD Insurance Group Holdings (TYO:8725) — 2026-11-16
## Bear case
The price already discounts the good news. At 5,316.00 JPY it sits above the mechanical base fair value of 4,163.92 and close to the bull value of 5,539.68 [Certain]. P/B of 1.1x is at 90% of its 5y range and EV/Sales is above its 5y max [Certain]. The Direction change is real: TTM ROIC fell 3.9pp to 11.3%, 6.4pp below its 2-year high [Certain]. Part of the recent ROE of 16.1% likely comes from strategic equity sales whose realised gains will not recur [Likely]. Catastrophe losses can reset a year's earnings [Likely]. The price is up 59.7% in 12 months and +17.1% above its 200-day average. If gains normalise and growth slows, an extended price de-rates toward book [Likely]. Results due Nov 19, 2026 could move the stock either way [Certain].
## Bull case
On earnings the stock is cheap: P/E of 8.9x sits at 28% of its 5y range, 25% below peers, with an 11.99% FCF yield [Certain]. Share count is down 6.05% YoY and management guides to higher dividends and significant buybacks, so per-share value compounds [Likely]. The FY2030 adjusted-profit target and the centralised international management give a credible plan [Guessing]. Beta is 0.27, so it diversifies an equity-heavy book [Certain]. The ROIC dip looks like catastrophe and gains noise, not a broken model: ROE is up over 5 years and the 3-year ROIC change is +3.0pp [Likely]. The trend is healthy: above the 200-day average, 50-day well above the 200-day, beating SPY by +49.4pp over 12 months [Certain].
## Decision
```json
{
  "ticker": "TYO:8725",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM ROIC fell from 15.2% to 11.3% (RA-T) while the 3-year change is +3.0pp and TTM ROE is 16.1% (RA); the swing tracks catastrophe losses and realised equity-sale gains flagged on the Q1 2027 call (https://stockanalysis.com/quote/tyo/8725/transcripts/665566-q1-2027/), not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Realised gains from strategic equity sales and benign catastrophe years flatter returns; if they normalise, the extended price (+17.1% above its 200-day average, above base fair value) de-rates toward book.",
    "veto": null
  },
  "thesis": "A cheap-on-earnings Japanese P&C insurer with heavy buybacks, but the price already sits near its mechanical bull value on book and the recent returns rely partly on non-recurring gains.",
  "rationale": "Cheap on P/E and FCF yield, but P/B is near its 5y high, the price is above base fair value, and rolling ROIC is falling. Good but not compelling at this price; the scorecard sets conviction below the buy bar, so AVOID with an entry price.",
  "price_at_decision": 5316.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-8725/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, under the FY2026 level of 8.4%, showing returns are falling structurally.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM ROE falls below 9%, under the FY2026 level of 9.8%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "Shares change YoY turns positive (now -6.05%), meaning buybacks stop.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6500, "basis": "Buybacks continue (shares -6.05% YoY [ST]) and P/E moves toward its 5y median of 11.6x [RA] on stable earnings, above the mechanical bull of 5,539.68 because the model ignores the shrinking share count."},
    "base": {"probability": 0.5, "target_price_12m": 5300, "basis": "P/E stays near 8.9x [RA] as buybacks offset normalising realised gains, leaving the price near the mechanical bull value of 5,539.68 [valuation] rather than the base."},
    "bear": {"probability": 0.25, "target_price_12m": 4163.92, "basis": "Gains and catastrophe luck normalise, ROIC keeps falling from 11.3% [RA-T] and P/B reverts toward its 5y median 0.9x [RA], near the mechanical base fair value of 4,163.92."}
  },
  "entry_price": 3331.14,
  "entry_basis": "valuation file: base 4,163.92 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
