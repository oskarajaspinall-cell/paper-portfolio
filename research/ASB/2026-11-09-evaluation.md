# Evaluation: Associated Banc-Corp (ASB) — 2026-11-09
## Bear case
This is an ordinary regional bank, not a franchise: ROE of 10.2% TTM is barely above FY2021's 8.6% after FY2023-24 troughs of 4.5% and 2.8% [Certain], and the note finds the deposit and relationship advantage replicable [Likely]. The share count rose 7.92% YoY on the American National deal, so per-share returns depend on integration delivering [Certain]. Near-term provisions are flattered by ASU 2025-08 and deal costs are still running through [Likely]. The discount is modest: P/E 10.8x is only 7% below peers and P/B 1.1x 18% below [Certain]; the stock is already up 19.5% in 12 months [Certain]. The mechanical fair value is flagged unreliable (methods disagree 3.2x) [Certain]. The FCF margin direction change (4.1pp below its 2-year high) is bank cash-flow noise from loan flows, not a structural signal [Likely]. Macro: VIX 28.18 and a widening HY spread point to multiple compression first, provisions later (macro overlay) [Likely].

## Bull case
Profitability is recovering after the mortgage repositioning: ROE 10.2% TTM vs 2.8% in FY2024, net margin 32.2% vs 12.9% [Certain]. Net interest margin rose to 3.14% for nine months from 3.02% [company-reported] (https://www.sec.gov/Archives/edgar/data/7789/000000778926000260/asb-20260930.htm), Q3 beat and the American National conversion is complete [Likely]. P/E sits at 6% of its 5y range and P/FCF 6.7x is 27% below peers with a 15.30% FCF yield [Certain]. The reverse DCF implies -7.0% revenue growth, which recent results do not show [Likely]. The dividend was raised to 25c [Certain]; beta is 0.81 and short interest negligible [Certain]. Rolling FCF margin is +0.8pp over the last year and +16.8pp over three years, so the 2-year-high gap is not deterioration [Certain].

## Decision
```json
{
  "ticker": "ASB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1y or 3y: FCF margin is +0.8pp over the last 12 months and +16.8pp over 3 years [CF-T]; ROE and net margin are rising [RA, IS].",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "A risk-off credit turn (VIX and HY spread rising, macro overlay) lifts provisions from a base flattered by ASU 2025-08 while acquisition dilution (shares +7.92% YoY) caps per-share returns.",
    "veto": null
  },
  "thesis": "A recovering Midwest regional bank with ROE back above 10% trades near the bottom of its own 5-year P/E range, but at only a modest discount to peers and with no durable moat, so the skew is fair rather than compelling.",
  "rationale": "Recovery in ROE and NIM is real, but quality is ordinary, the peer discount is small, the mechanical fair value is unreliable and macro tilts toward bear. Good but not compelling is an AVOID under the high-conviction-only owner rule; cash is acceptable.",
  "price_at_decision": 30.36,
  "price_date": "2026-11-06",
  "research_note": "research/ASB/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 8%, back toward the FY2021 level of 8.6% and showing the post-repositioning recovery has failed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 25%, reversing most of the recovery from 12.9% (FY2024) to 32.2%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "Net interest margin in the 10-Q/10-K MD&A falls below 3.00% for a quarter (sec.gov filings)."},
    {"text": "Provision for credit losses in the 10-Q exceeds 100 million USD for a nine-month period (sec.gov filings)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 36.86, "basis": "NIM expansion continues and the P/E re-rates toward the 11.6x peer median [RA] as VIX normalises (macro overlay bull), reaching the mechanical bull fair value [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 32.0, "basis": "ROE holds near 10.2% [RA] and P/E stays near its 10.0x 5y median [RA] on modestly higher earnings, landing below the base fair value 33.85 because that figure is flagged unreliable (methods disagree 3.2x)."},
    "bear": {"probability": 0.30, "target_price_12m": 25.5, "basis": "Risk-off persists (macro overlay tilt toward bear, small, which raises this probability) and the P/E compresses to its 9.1x 5y minimum [RA] as provisions rise; the mechanical bear 6.60 is not used as it comes from an unreliable P/B+ROE bear."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
