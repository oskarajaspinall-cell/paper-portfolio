# Evaluation: Central Bancompany, Inc. (CBC) — 2026-11-15
## Bear case
The price already pays for the improvement. P/E 20.2x against an 11.9x peer median, P/B 2.4x against 1.4x and P/FCF 19.1x against 7.5x [Certain] [RA]. Both mechanical legs that matter sit below the 38.15 close: P/B + ROE base 19.57, FCFE base 33.12 (flagged unreliable) [Certain]. The reverse DCF needs 8.9% year-1 revenue growth, high for a bank [Likely]. Trend-strength credit comes from an extended price: +30.0% over the 200-day average, +81.2% in 12 months, RSI 73.7 [Certain]; if NIM gains slow, a de-rating toward peer multiples is the main risk [Likely]. Q3 EPS was just under consensus per a headline [Likely]. Shares rose 7.56% YoY [Certain]; a 31.19% insider stake risks a holder overhang [Guessing]. The FCF margin direction change (5y falling, TTM 28.1% -> 44.6%) looks like lumpy bank cash flow, not a structural break [Likely]. Macro tilts small toward bear: a 10y-2y slope near 0.24pp squeezes funding (macro overlay) [Likely].
## Bull case
The franchise is improving. ROE rose from 10.2% (FY2021) to 12.6% TTM and net margin from 32.3% to 40.8% [Certain] [RA, IS]. Q3 brought NIM up 12 bps YoY and benign credit, and management expects further NII and margin gains [Likely] (https://stockanalysis.com/stocks/cbc/transcripts/723782-q3-2026/). A new $100M buyback was authorised with Q2 [Likely] (https://stockanalysis.com/stocks/cbc/transcripts/656118-q2-2026/). Rolling FCF margin is at its 2-year high of 44.6% and the FCF yield is 5.24% [Certain] [CF-T, ST]. Insiders own 31.19%, aligning controlling holders with outside shareholders [Certain]. The stock is beating SPY by +70.8pp over 12 months, a business that is visibly working [Certain]. HY spreads of 3.2% show calm credit (macro overlay) [Certain]. Still, the upside needs the premium multiple to hold, a thin base for a 12-month buy [Guessing].
## Decision
```json
{
  "ticker": "CBC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "new_evidence": {"type": "method_change", "text": "The 2026-11-09 AVOID at conviction 2 predates the owner request of 2026-11-15 that scores trend strength (price above the 200-day average, a real FCF yield) in place of a discount; the same evidence now scores 3. Decision unchanged: AVOID."},
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years. FCF margin fell only on fiscal years (FY2024 38.3% to FY2025 22.9% [CF,IS]); the rolling 12 months rose from 28.1% to 44.6%, a 2-year high [CF-T], while ROE rose to 12.6% TTM [RA].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "De-rating toward peer multiples (P/E 20.2x vs 11.9x, P/B 2.4x vs 1.4x [RA]) from an extended price (+30.0% over the 200-day average) if NIM gains stall on a flat curve (macro overlay).",
    "veto": null
  },
  "thesis": "An improving Missouri regional bank with rising ROE and margins, but priced at a large premium to peers and above its mechanical fair value after an 81.2% run.",
  "rationale": "Quality is good and rising, but valuation is the obstacle: a large premium to peers on P/E, P/B and P/FCF, a reverse DCF needing 8.9% growth, and a probability-weighted value below the price. Macro tilts small toward bear. Not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 38.15,
  "price_date": "2026-11-13",
  "research_note": "research/CBC/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROE falls below 10%, giving up the rise from 10.2% (FY2021) to 12.6% and showing the earnings improvement has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 34%, back under its FY2024 level of 34.6%, showing NIM gains or credit have reversed.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 34}},
    {"text": "Shares change YoY rises above 8%, so dilution continues instead of buybacks shrinking the count.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 8}},
    {"text": "A later earnings release reverses the Q3 'benign credit' description or reports a year-on-year fall in NIM."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 38.97, "basis": "NIM and ROE keep rising and the premium multiple holds; FCFE DCF bull 38.97 (fact sheet Fair value, IS,BS,CF,RA,ST)."},
    "base": {"probability": 0.45, "target_price_12m": 33.12, "basis": "Earnings grow as guided on the Q3 call, but the P/E premium to the 11.9x peer median [RA] partly narrows; FCFE DCF base 33.12 (fact sheet Fair value), used over the unreliable blend."},
    "bear": {"probability": 0.35, "target_price_12m": 24.09, "basis": "A flatter curve and rising 2y stall NIM and the multiple compresses toward peers (macro overlay research/CBC/2026-11-15-macro.md, tilt toward bear, small, which raised this probability); blended base fair value 24.09 (fact sheet Fair value)."}
  },
  "entry_price": 26.5,
  "entry_basis": "Above the default (valuation file: base 24.09 x 0.8), because that blend is flagged unreliable and its P/B + ROE leg ignores the rising ROE; instead the FCFE base of 33.12 x 0.8, a 20% margin of safety on the cash-flow method.",
  "replaces": null,
  "replacement_reason": null
}
```
