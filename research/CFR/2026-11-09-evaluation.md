# Evaluation: Cullen/Frost Bankers (CFR) — 2026-11-09
## Bear case
The price already pays for quality. P/B is 2.5x, 77% of the way up its 5y range and 104% above the peer median of 1.2x; P/E of 14.7x is 26% above peers [Certain]. The mechanical base fair value of 153.19 sits just below the 155.23 close, and the reverse DCF implies only -0.7% year-1 growth, so there is no margin of safety [Certain]. The macro overlay tilts toward bear: HY spread 3.48% (+0.45 in 1m) and VIX 28.18 are rising, and a risk-off move could compress P/B toward 1.8-2.0x before any NII benefit shows [Guessing]. Net margin has drifted down 2.7pp over five years [Certain]. The Direction change on FCF margin (falling over 5 fiscal years, rising over the last 12 months) reflects bank working-capital noise, not a broken model, so it doesn't threaten the thesis; it also gives no upside signal [Likely]. CRE exposure and fintech deposit competition are risks [Likely].

## Bull case
A high-quality, deposit-rich franchise: ROE 16.3% TTM, up from 10.1% in FY2021, with about 32.9% non-interest-bearing deposits [company-reported] (https://www.sec.gov/Archives/edgar/data/39263/000003926326000056/cfr-20260930.htm), which makes it a winner if rates stay higher [Likely]. Management raised loan growth and NII guidance on the Q3 call, with 9% loan growth and record pipelines (https://stockanalysis.com/stocks/cfr/transcripts/720163-q3-2026/) [Likely]. Buybacks cut the share count 2.26% YoY [Certain]. P/E is below its own 15.1x 5y median, and beta is 0.51 [Certain]. The FCFE DCF gives 210.46, though the fair value is flagged unreliable because the methods disagree 3.2x [Certain]. Steady compounding plus the dividend could beat the market with low volatility [Guessing].

## Decision
```json
{
  "ticker": "CFR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The FCF margin decline is bank working-capital noise (FCF conversion swung 147.9% in FY2024 to 19.6% in FY2025 and 83.9% TTM [CF,IS]) and FCF margin rose from 0.8% to 25.2% over the last 12 months [CF-T]; ROE rose 5.2pp over five years [RA].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating from a full P/B of 2.5x (104% above peers) if credit spreads and VIX keep rising, or CRE credit costs rise (macro overlay; Q3 transcript).",
    "veto": null
  },
  "thesis": "A high-ROE, deposit-rich Texas bank that is well run but already priced at a large premium to peers and at its mechanical base fair value.",
  "rationale": "Quality is real (ROE 16.3%, buybacks, raised guidance) but the price leaves little margin of safety: P/B near the top of its range, a premium to peers, base fair value below the price, and a small bear macro tilt. Good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 155.23,
  "price_date": "2026-11-06",
  "research_note": "research/CFR/2026-11-09.md",
  "triggers": [
    {"text": "ROE falls below 12% (statistics page)", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Net (profit) margin falls below 26%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 26}},
    {"text": "Shares change YoY turns positive (buybacks replaced by dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Non-interest-bearing demand deposits fall below 28% of total deposits (10-Q balance sheet)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 184.44, "basis": "Raised NII and loan-growth guidance is delivered and P/B holds near 2.5x (macro overlay bull), reaching the mechanical bull fair value of 184.44 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 153.19, "basis": "Earnings grow with ROE near 16.3% [RA] but the peer premium keeps the multiple flat, landing at the mechanical base fair value of 153.19; probability shaded toward bear per the macro overlay's small bear tilt."},
    "bear": {"probability": 0.3, "target_price_12m": 107.59, "basis": "HY spread and VIX stress compress P/B toward 1.8-2.0x, its 5y low end [RA] (macro overlay bear), consistent with the mechanical bear fair value of 107.59; probability raised by the overlay's small bear tilt."}
  },
  "entry_price": 122.55,
  "entry_basis": "valuation file: base 153.19 x 0.8; price is the obstacle, not quality.",
  "replaces": null,
  "replacement_reason": null
}
```
