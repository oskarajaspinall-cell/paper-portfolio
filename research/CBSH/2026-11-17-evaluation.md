# Evaluation: Commerce Bancshares (CBSH) — 2026-11-17
## Bear case
The dip has no stock-specific cause: Q3 EPS of $1.08 came in line, with no earnings-type reaction in 10 sessions, so it is not an overreaction to fix [Certain]. ROE has eased from 17.8% (FY2023) to 15.1% TTM and net margin from 33.1% to 31.4% [Certain]. Net interest income growth is largely acquisition-driven with purchase-accounting accretion `[company-reported]`, so organic growth is unproven [Likely]. Shares are up 2.07% YoY despite buybacks [Certain]. P/B of 1.9x is still well above the 1.4x peer median, so a "cheap vs own history" call can de-rate further toward peers [Likely]. The overlay's bear path (more hikes, a flat curve, HY spreads above ~4.5%) squeezes NIM and book value [Likely]. The fair value is flagged unreliable (methods disagree 3.9x); the FCF-margin jump to 67.3% is noise [Likely]. The price sits only 1.8% above its 200-day average, so trend support is thin [Certain].
## Bull case
A conservative, low-cost-deposit regional bank still earns 15.1% ROE, with 9-month ROA of 1.75% and an efficiency ratio of 58.34% `[company-reported]`, top-tier for the group [Certain]. P/E of 13.3x sits at 7% of its 5y range and P/B at its 5y minimum, so the market already prices little [Certain]. Reverse DCF implies -1.1% year-1 revenue growth, while Q3 EPS rose from $1.01 to $1.08 year on year [Certain]. The P/B + ROE method gives 63.59, above the 55.51 close [Certain]. Beta of 0.60 and the overlay's neutral tilt limit macro downside [Likely]. The buyback reauthorization on 2026-11-03 and a stock plus cash dividend return capital [Certain]. FineMark and Nolan add wealth and investment-banking fees that diversify away from NIM [Likely].
## Decision
```json
{
 "ticker": "CBSH",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds nothing falling over 1 or 3 years; ROE and net margin eased modestly from their FY2023/FY2025 levels while FineMark (2026-01-01) and Nolan (2026-10-01) were absorbed, with 9-month efficiency ratio 58.34% and ROA 1.75% [company-reported] (https://www.sec.gov/Archives/edgar/data/22356/000002235626000213/cbsh-20260930.htm).",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Organic growth stalls under a flat curve and rising deposit costs while acquisition accretion fades, keeping ROE drifting lower and P/B de-rating toward the 1.4x peer median.",
  "veto": null
 },
 "thesis": "A high-return, conservatively run regional bank trading at the bottom of its own 5-year P/E and P/B ranges, but with acquisition-led growth, easing ROE and no stock-specific overreaction to buy into.",
 "rationale": "The fall has no business cause to fade: results were in line and the dip is market drift. Quality is good but ROE and net margin are easing, growth is acquisition-led and the fair value is unreliable. Good but not compelling: AVOID, watched at the margin-of-safety entry price.",
 "price_at_decision": 55.51,
 "price_date": "2026-11-16",
 "research_note": "research/CBSH/2026-11-17.md",
 "triggers": [
  {"text": "TTM ROE (statistics page) rises above 17%, back toward the FY2023 level of 17.8%, showing acquisitions are lifting returns (would raise conviction).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 17}},
  {"text": "TTM ROE falls below 12%, showing the franchise's returns are breaking down.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
  {"text": "TTM net margin falls below 27%, showing deposit costs or credit are eroding profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 27}},
  {"text": "Efficiency ratio in the 10-Q MD&A rises above 62% for two quarters, showing FineMark/Nolan integration costs outrunning revenue."}
 ],
 "scenarios": {
  "bull": {"probability": 0.25, "target_price_12m": 69.74, "basis": "Multiple rebuilds from its 5y-minimum P/B toward the mechanical bull fair value 69.74 [IS,BS,CF,RA,ST] as acquired fee income compounds; macro overlay tilt neutral/small, so no probability change (research/CBSH/2026-11-17-macro.md)."},
  "base": {"probability": 0.5, "target_price_12m": 63.59, "basis": "P/B + sustainable ROE (best method) at 63.59 [RA,ST] with ROE holding near 15.1%; the blended base 64.70 is flagged unreliable, so the single best method is used."},
  "bear": {"probability": 0.25, "target_price_12m": 49.62, "basis": "Overlay bear path (hikes plus HY spreads above ~4.5%, research/CBSH/2026-11-17-macro.md) compresses P/B below its 1.9x 5y low toward peers at 1.4x [RA], taking the price back to the 6-month low of 49.62 [HI]; this sits below the mechanical bear 58.23, which assumes no de-rating."}
 },
 "entry_price": 55.0,
 "entry_basis": "valuation file: base 64.70 x 0.85; a hit triggers re-research, and price is only part of the obstacle (easing ROE, acquisition-led growth).",
 "replaces": null,
 "replacement_reason": null
}
```
