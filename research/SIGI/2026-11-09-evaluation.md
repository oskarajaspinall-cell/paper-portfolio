# Evaluation: Selective Insurance Group (SIGI) — 2026-11-09
## Bear case
Returns are cyclical, not protected: ROIC swung from 12.5% (FY2021) to 7.5% (FY2022) and 7.1% (FY2024), with ROE as low as 6.8% [Certain]. Those troughs came from underwriting and reserve charges, and the Q3 2026 result (combined ratio 96.8%, no prior-year casualty development [company-reported], https://www.sec.gov/Archives/edgar/data/230557/000023055726000027/sigi-20260930.htm) is a single good quarter, not proof the reserve problem is gone [Likely]. Management says remediation is restraining commercial premium growth and Q2 flagged elevated commercial auto frequency (https://stockanalysis.com/stocks/sigi/transcripts/715112-q3-2026/) [Likely]. The low P/E (5% of its 5y range) is matched by peers (P/E +3% vs median), so it is sector de-rating, not a unique discount [Likely]. The headline FCF yield of 19.41% is float growth, not owner earnings [Likely]. New CIO and new head of Standard Lines add execution risk [Guessing]. Base fair value is only +10.2% above the price; the mechanical bear is -44.0% [Certain].
## Bull case
Profitability is at the top of its range and rising: TTM ROIC 12.4% vs 10.8% a year earlier, ROE 14.7%, and Q3 operating ROE 16.9% [company-reported] with no prior-year casualty development [Certain]. No Direction change line is printed; nothing Python tracks is falling [Certain]. Investment income is growing and the 10y yield at 4.84% keeps float reinvestment supportive (macro overlay, context only) [Likely]. Leverage is low (net debt/EBITDA 1.23x), beta 0.21, and capital is returned: $81 million in Q3 [company-reported] with shares down 1.55% YoY [Certain]. Valuation is undemanding on own history (EV/EBITDA at 1% of its 5y range, P/B 26% below peers), and the P/E method alone gives 141.01 [Certain]. If returns hold near today's level, a re-rating toward the 5y median P/E of 16.9x is plausible [Guessing].
## Decision
```json
{
  "ticker": "SIGI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling: TTM ROIC 12.4% vs 10.8% a year earlier [RA-T]; margins and FCF margin are [data unavailable] for this insurer.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Reserve and underwriting reversal (commercial auto frequency, casualty reserves) pushing ROE back toward the FY2024 6.8% trough, as happened in FY2022 and FY2024 [RA].",
    "veto": null
  },
  "thesis": "A well-capitalised regional P&C insurer at a cyclical-high ROE trading near the low end of its own P/E range, but with returns that have repeatedly reverted and only modest upside to base fair value.",
  "rationale": "Good-but-not-compelling: rising returns and a sound balance sheet, but no durable moat, earnings that have twice collapsed on reserves in five years, a discount shared with peers, and base fair value only +10.2% above the price. The scorecard conviction sits below the buy bar, so AVOID; an entry price is set at base fair value less the margin of safety.",
  "price_at_decision": 99.44,
  "price_date": "2026-11-06",
  "research_note": "research/SIGI/2026-11-09.md",
  "triggers": [
    {"text": "ROIC TTM (statistics page) falls below 8%, signalling an underwriting/reserve reversal toward the FY2022/FY2024 troughs.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "ROE TTM (statistics page) falls below 9%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "Quarterly combined ratio (10-Q MD&A) above 100% for two consecutive quarters."},
    {"text": "Adverse prior-year casualty reserve development (10-Q/10-K MD&A table) in any full year."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 134.49, "basis": "Operating ROE holds near the Q3 16.9% [company-reported] and the P/E re-rates toward its 5y median 16.9x [RA], matching the mechanical bull fair value 134.49 [fact sheet]."},
    "base": {"probability": 0.5, "target_price_12m": 109.63, "basis": "Returns stay near TTM ROE 14.7% [RA] and the blended P/B+ROE / P/E base fair value 109.63 [fact sheet] is reached, with P/B near its 5y median 1.8x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 70.0, "basis": "Reserve/underwriting reversal takes ROE back toward the FY2024 6.8% trough [RA] and P/B toward its 5y low 1.4x [RA]; set above the mechanical bear 55.66 [fact sheet] because the balance sheet (net debt/EBITDA 1.23x) and capital returns cushion book value."}
  },
  "entry_price": 87.7,
  "entry_basis": "valuation file: base 109.63 x 0.8 (20% margin of safety); at that price the same evidence would give a larger valuation score.",
  "replaces": null,
  "replacement_reason": null
}
```
