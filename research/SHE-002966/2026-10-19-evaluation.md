# Evaluation: Bank of Suzhou Co., Ltd. (SHE:002966) — 2026-10-19
## Bear case
This is an ordinary city commercial bank, not a mispriced compounder. ROE has drifted from 11.0% (FY2022) to 9.2% TTM, below the CAPM cost of equity implied by a 5.10% risk-free rate plus a 3.5% CNY country premium [Certain]. At 7.6x P/E the stock already trades above its own 5-year max of 7.4x and above the 6.7x peer median [Certain]; P/B of 0.6x is only mid-range and in line with peers [Certain]. The bank's own best fair-value method (P/B + ROE) gives a base of CNY 9.09, essentially the CNY 9.00 close [Certain]; the +21.2% blended upside leans on an FCFE DCF built on bank cash flows the note itself calls unreliable [Likely]. NIM is set by PBoC policy, Piotroski is a middling 4, and Q3 results land on Oct 29, 2026 [Certain]. Rising net margin (48.3%) may reflect lower provisioning that can reverse [Guessing].
## Bull case
Earnings quality is steady: ROE has held a narrow 9.2–11.0% band for five years and net margin has risen +6.0pp to 48.3% TTM [Certain]. The franchise sits in affluent Jiangsu with a local deposit base [Likely]. At 0.6x book the market prices a business earning roughly 9% on equity at a deep discount, and the reverse DCF implies -6.4% revenue decline in year 1, which recent history does not show [Likely]. Shares outstanding are near flat (+0.72% YoY), so no dilutive capital raise [Certain]. Beta of 0.13 and +14.1% 3-month momentum point to a low-correlation holding gaining traction [Certain]. Mechanical bull value is CNY 12.40 [Certain].
## Decision
```json
{
  "ticker": "SHE:002966",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A stable but sub-cost-of-equity regional Chinese bank trading above its own 5-year P/E range and in line with peers on P/B, with the bank-appropriate P/B + ROE fair value at the current price.",
  "rationale": "Returns are steady but slipping, not improving; the stock is no longer cheap on its own history or versus peers; the blended upside depends on an FCFE model that is unreliable for banks. Good but not compelling: AVOID, with an entry well below the P/B + ROE base value.",
  "price_at_decision": 9.00,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002966/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE rises above 11% (top of its 5-year 9.2%-11.0% band), showing returns are re-accelerating rather than drifting lower.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 11}},
    {"text": "TTM ROE falls below 8%, below the 5-year range, confirming returns compression (would make any entry price moot).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 42%, its 5-year low, signalling NIM or credit-cost deterioration.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 42}},
    {"text": "Shares outstanding rise more than 5% YoY, a dilutive capital raise beyond the current +0.72% pace.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 12.40, "basis": "Mechanical bull fair value CNY 12.40 [IS,BS,CF,RA,ST] if ROE holds near the top of its 9.2-11.0% band [RA] and the market stops pricing the -6.4% revenue decline the reverse DCF implies."},
    "base": {"probability": 0.5, "target_price_12m": 9.09, "basis": "P/B + ROE base value CNY 9.09 (the bank-appropriate best method) [RA,BS]; below the CNY 10.91 blend because the FCFE leg rests on bank cash flows that swing -110% to +278% and are not distributable (note section 2) [CF]."},
    "bear": {"probability": 0.3, "target_price_12m": 8.10, "basis": "P/B + ROE bear value CNY 8.10 [RA,BS] as ROE keeps drifting below 9.2% and the P/E above its 7.4x 5-year max reverts toward the 7.3x median [RA]."}
  },
  "entry_price": 7.27,
  "entry_basis": "P/B + ROE base 9.09 x 0.8 rather than the blended base, because the FCFE leg is unreliable for a bank (note section 2) [RA,CF].",
  "replaces": null,
  "replacement_reason": null
}
```
