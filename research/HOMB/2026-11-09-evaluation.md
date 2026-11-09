# Evaluation: Home BancShares, Inc. (HOMB) — 2026-11-09
## Bear case
Credit is turning before the price reflects it. Non-performing loans rose to $200.8 million from $85.0 million, led by one $92.1 million relationship on non-accrual, and allowance coverage fell to 162.45% from 350.17% [company-reported] (https://www.sec.gov/Archives/edgar/data/1331520/000133152026000124/homb-20260930.htm), yet no Q3 provision was booked [Certain]. A loss there would cut ROE toward the 9.5% tripwire [Likely]. The macro overlay adds widening HY spreads (+0.45pp in a month) and a VIX of 28.18, a small tilt toward bear [Likely]. Valuation offers no cushion: P/B 1.3x is at its 5y median and above peers, P/FCF 13.8x sits at 83% of its range and above peers [Certain]. FCF margin is down -17.8pp over five years and -7.0pp over three; the last-12-month rise (35.5% to 39.1%) still leaves it 9.7pp below its 2-year high [Certain]. The fair value is flagged unreliable (methods disagree 3.0x) [Certain].

## Bull case
A steady, high-earning regional bank at a modest multiple. ROE is 11.1% TTM and flat over five years; net margin 43.5% is flat too, so earnings power is not eroding [Certain]. The FCF-margin decline looks like bank cash-flow noise rather than a broken model: it has risen over the last 12 months while ROE and net margin held, and Q3 net interest margin of 4.53% was close to 4.56% a year earlier [company-reported] (https://www.sec.gov/Archives/edgar/data/1331520/000133152026000124/homb-20260930.htm) [Likely]. P/E 12.2x is at the 20th percentile of its 5y range, and the reverse DCF implies -3.8% year-1 revenue growth, i.e. stagnation [Certain]. Capital returns are rising: a 9.5% dividend increase and a larger buyback authorisation [Certain]. If the large non-accrual loan resolves cleanly, P/B can re-rate toward 1.4x [Guessing].

## Decision
```json
{
  "ticker": "HOMB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin falls over 5y/3y but rose over the last 12 months (35.5% to 39.1%) [CF-T]; ROE (11.1% TTM) and net margin (43.5%) are flat over five years [RA,IS], so the decline reflects lumpy bank cash-flow items, not lost earnings power.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Credit: non-performing loans up to $200.8 million on a $92.1 million non-accrual relationship, coverage down to 162.45%, no Q3 provision [company-reported]; a loss would push ROE toward 9.5%.",
    "veto": null
  },
  "thesis": "A steadily profitable Southern regional bank at a low-end P/E, but with rising non-performing loans, thin coverage and no valuation cushion on P/B.",
  "rationale": "Quality is solid but not high (ROE 11.1%), P/B is at its 5y median and above peers, the fair value is unreliable and credit is deteriorating with no provision booked. Good but not compelling; cash is acceptable.",
  "price_at_decision": 29.86,
  "price_date": "2026-11-06",
  "research_note": "research/HOMB/2026-11-09.md",
  "triggers": [
    {"text": "ROE TTM falls below 9.5% (statistics page)", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9.5}},
    {"text": "Net margin falls below 38% (statistics page profit margin)", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 38}},
    {"text": "Non-performing loans / total loans rises above 1.75% in the 10-Q (from 1.19% at 30 Sep 2026) [company-reported]"},
    {"text": "Net interest margin in the 10-Q MD&A falls below 4.2%"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 37.2, "basis": "The non-accrual loan resolves and P/E returns to its 5y high of 15.2x [RA] on TTM earnings, consistent with P/B re-rating toward 1.4x (macro overlay bull)."},
    "base": {"probability": 0.5, "target_price_12m": 31.8, "basis": "Earnings hold with ROE near 11.1% [RA] and P/E returns to its 5y median 13.0x [RA]; below the unreliable blended base fair value 34.34 because the P/B + ROE best method gives 29.14."},
    "bear": {"probability": 0.3, "target_price_12m": 25.48, "basis": "A loss on the $92.1 million relationship returns provisions and P/B compresses toward 1.1x, the P/B + ROE bear value 25.48 [fact sheet]; probability raised by the macro overlay's small toward-bear tilt (research/HOMB/2026-11-09-macro.md)."}
  },
  "entry_price": 27.47,
  "entry_basis": "valuation file: base 34.34 x 0.8 (equal to the bear fair value 27.47); at that level P/E would sit near its 5y low of 11.5x [RA], compensating for the credit risk if non-performing loans stop rising.",
  "replaces": null,
  "replacement_reason": null
}
```
