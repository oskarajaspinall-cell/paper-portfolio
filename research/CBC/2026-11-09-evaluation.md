# Evaluation: Central Bancompany, Inc. (CBC) — 2026-11-09
## Bear case
The price already pays for the improvement. P/E 20.0x against a 12.5x peer median, P/B 2.4x against 1.6x and P/FCF 18.9x against 9.9x [Certain] [ST]. Every fair-value method sits below the 37.75 close: P/B + ROE base 20.37, FCFE base 34.50, blended base 25.08 [Certain] (flagged unreliable, so weighed lightly). The reverse DCF needs 7.6% year-1 revenue growth [Likely]. The stock is up 77.7% in 12 months with RSI 76.7, so the re-rating ran ahead of earnings [Certain]. Q3 EPS of 48c was just under consensus per a headline [Likely]. Shares rose 7.56% YoY despite a buyback [Certain]. FCF margin fell over five fiscal years (FY2025 conversion 59.2%), but the rolling 12 months rebounded from 28.1% to 44.6%. That looks like normal bank cash-flow noise, not a structural break [Likely]. The macro overlay tilts small toward bear: VIX at 28.18 and a widening HY spread threaten the premium multiple [Likely].
## Bull case
The quality is real and improving. ROE has risen from 10.2% (FY2021) to 12.6% TTM, and net margin from 32.3% to 40.8% [Certain] [RA, IS]. Q3 brought higher NIM and "benign" credit, and management expects further NII and margin gains [Likely] (https://stockanalysis.com/stocks/cbc/transcripts/723782-q3-2026/). A new $100M buyback was authorised [Likely]. Insiders own 31.19%, which aligns the controlling holders with outside shareholders [Certain]. Beta of 0.06 and a domestic book mean no country risk [Certain]. The FCFE bull case of 40.63 sits slightly above the price [Certain]. Even so, the upside rests on continued multiple expansion at a premium to peers, and that is a stretched base for a 12-month buy [Guessing].
## Decision
```json
{
  "ticker": "CBC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROE rose from 11.3% in FY2025 to 12.6% TTM [RA], and rolling FCF margin rose from 28.1% to 44.6% [CF-T]; the 5y FCF fall is bank cash-flow noise that the latest 12 months have reversed.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The multiple compresses toward peers (P/E 20.0x vs 12.5x, P/B 2.4x vs 1.6x [ST]) as VIX and HY spreads rise (macro overlay); every fair-value method sits below the price.",
    "veto": null
  },
  "thesis": "A well-run, improving Missouri regional bank whose ROE and margins are rising, but the price already sits at a large premium to peers and above every mechanical fair-value method after a 77.7% run.",
  "rationale": "The quality is good and rising, but the valuation is the obstacle. The stock trades at a premium to peers on P/E, P/B and P/FCF, the reverse DCF needs 7.6% growth, and the probability-weighted value sits below the price. The macro overlay tilts toward the bear case. Not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 37.75,
  "price_date": "2026-11-06",
  "research_note": "research/CBC/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 10%, giving up the rise from 10.2% (FY2021) to 12.6% and showing the earnings improvement has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 34%, back to its FY2024 level of 34.6% or lower, showing NIM gains or credit have reversed.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 34}},
    {"text": "Shares change YoY stays above 7.56%, so dilution continues instead of buybacks shrinking the count.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 7.56}},
    {"text": "A later earnings release reverses the Q3 'benign credit' description or reports a fall in NIM."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 40.63, "basis": "NIM and ROE keep rising and the premium multiple holds; FCFE DCF bull 40.63 (fact sheet Fair value, IS,BS,CF,RA,ST)."},
    "base": {"probability": 0.45, "target_price_12m": 34.5, "basis": "Earnings grow as guided on the Q3 call, but the P/E premium to the 12.5x peer median [ST] partly narrows; FCFE DCF base 34.50 (fact sheet Fair value)."},
    "bear": {"probability": 0.35, "target_price_12m": 25.08, "basis": "Wider HY spreads and a flatter curve compress the multiple toward peers (macro overlay research/CBC/2026-11-09-macro.md, tilt toward bear, small, which raised this probability); blended base fair value 25.08 (fact sheet Fair value)."}
  },
  "entry_price": 27.6,
  "entry_basis": "Above the default (valuation file: base 25.08 x 0.8), because that blend is flagged unreliable and its P/B + ROE leg ignores the rising ROE. Instead, a level where the price sits well below the FCFE base of 34.50 with a 20% margin of safety, i.e. FCFE base 34.50 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
