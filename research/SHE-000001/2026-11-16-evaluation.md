# Evaluation: Ping An Bank Co., Ltd. (SHE:000001) — 2026-11-16
## Bear case
Returns are eroding: ROE fell from 11.0% (FY2022) to 8.2% (FY2025) and 8.1% TTM [RA] [Certain], and the FY2025 call summary says revenue and net profit declined [Likely]. That looks like structural margin pressure in a crowded Chinese banking market (competing on price, even with toys for young customers) rather than a one-off [Guessing]. A rising net margin of 47.2% reflects cost control on a shrinking top line, not growth [Likely]. P/E of 5.7x sits near its 5y median of 5.5x [RA], so it is not cheap against its own history [Certain]. The fair value is flagged unreliable (methods disagree 3.5x) [Certain]. The price is near its 52-week high and 8.2% above its 200-day average [HI] [Certain]: if earnings keep shrinking, that trend rally can reverse. Property and corporate loan quality is the key unseen risk; capital ratios are [data unavailable] [Likely]. Q3 2026 results were not read [Certain].
## Bull case
P/B of 0.4x sits at the bottom of its 5y range and 15% below peers; P/E is 22% below the peer median of 7.4x [RA] [Certain]. Shares outstanding fell 4.32% YoY [ST], unusual for a bank and supportive of per-share value [Certain]. Management reported improving asset quality, cost control and retail transformation and pointed to a return to growth in 2026 [Likely]. The stock is in a mild uptrend (50-day above 200-day by 4.4%, +10.3pp vs SPY over 3 months) with a low beta of 0.46 [ST,HI] [Certain]. If ROE stabilises, a re-rating toward the 5y median P/B of 0.5x is plausible [Guessing].
## Decision
```json
{
  "ticker": "SHE:000001",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A cheap-on-book Chinese joint-stock bank whose ROE is steadily falling, with no evident moat and unverifiable loan quality, so the low multiple looks deserved.",
  "rationale": "ROE has fallen for three years to 8.1% with declining revenue; P/E is at its own 5y median, the fair value is unreliable, and capital data is missing. Good-but-not-compelling at best; no position.",
  "price_at_decision": 12.07,
  "price_date": "2026-11-13",
  "research_note": "research/SHE-000001/2026-11-16.md",
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "ROE fell from 11.0% (FY2022) to 8.1% TTM [RA] while the FY2025 call summary reports declining revenue and net profit (https://stockanalysis.com/quote/she/000001/transcripts/403365-h2-2025/); price competition in Chinese banking suggests margin pressure, not a one-off.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Property and corporate loan losses on top of shrinking revenue push ROE further down; capital ratios are unavailable to gauge the buffer.",
    "veto": null
  },
  "triggers": [
    {"text": "ROE (statistics page) falls below 7%, showing the decline is accelerating.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "Net margin (statistics page) falls below 44%, meaning cost control no longer offsets revenue decline.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 44}},
    {"text": "Shares outstanding change YoY turns positive (dilution / capital raise).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "A reported return to revenue growth with ROE stable or rising in the next annual results would argue for re-examining the AVOID."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 15.0, "basis": "ROE stabilises and P/B re-rates toward its 5y median of 0.5x [RA]; below the mechanical bull of 19.58 because that fair value is flagged unreliable."},
    "base": {"probability": 0.5, "target_price_12m": 12.0, "basis": "P/E holds near its 5y median of 5.5x [RA] on flat-to-lower earnings; below the base fair value of 18.49 because the model is flagged unreliable (methods disagree 3.5x)."},
    "bear": {"probability": 0.25, "target_price_12m": 9.99, "basis": "Continued ROE decline [RA] and loan-quality worries send the price back to its 52-week low of 9.99 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the falling ROE and declining revenue are the issue, and the base fair value is unreliable, so a lower price alone would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
