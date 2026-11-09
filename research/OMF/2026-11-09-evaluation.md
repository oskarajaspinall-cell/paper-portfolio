# Evaluation: OneMain Holdings, Inc. (OMF) — 2026-11-09
## Bear case
OMF is a highly levered non-prime lender: long-term debt of $24,074m against equity of $3,391m [company-reported] (https://www.sec.gov/Archives/edgar/data/1584207/000158420726000041/omf-20260930.htm) [Certain]. ROE fell from 40.2% (FY2021) to 22.7% TTM as credit costs normalised [Certain], and Q3 provisions rose 26% on receivables growth and higher net charge-offs (10-Q) [Certain]. The macro overlay tilts toward bear (small): the HY spread widened 0.77pp in 3 months and VIX is 28.18, pressuring securitisation funding before loan yields reprice [Likely]. The stock is not cheap: P/E 8.5x sits mid-range of its 5y band, near peers, while P/B 1.9x is +64% above the peer median [Certain]. The mechanical skew is poor: base fair value 60.48 is only +7.8% above the close, the bear 30.68 is -45.3% [Certain]. Piotroski F of 4 and a data-breach legal probe add noise [Guessing].

## Bull case
ROE of 22.7% TTM is well above any reasonable cost of equity and above FY2024's 16.0%, and rolling ROIC is flat at 2.9% versus a year earlier, so the decline since FY2021 looks like post-pandemic credit normalisation rather than a broken model [Likely]. Q3 managed receivables grew to $28.1bn and management points to improving delinquencies into 2027 (earnings call transcript, /stocks/omf/transcripts/718489-q3-2026/) [Likely]. Capital return is substantial: a $1.05 quarterly dividend and YTD buybacks of $173m [company-reported] (https://www.sec.gov/Archives/edgar/data/1584207/000158420726000041/omf-20260930.htm), with shares down 2.49% YoY [Certain]. The price is down 13.7% over 3 months, so some credit worry is priced, and HY spreads at 3.48% are not stressed [Likely]. A spread retracement toward the bull 66.75 fair value is plausible [Guessing].

## Decision
```json
{
  "ticker": "OMF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: rolling ROIC is flat at 2.9% vs 3.0% a year earlier [RA-T]. The 5-year ROE fall from 40.2% (FY2021) to 22.7% TTM [RA] reflects post-pandemic credit normalisation, with ROE recovered from 16.0% in FY2024.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A turn in the non-prime credit cycle with wider funding spreads: provisions already rose 26% in Q3 (10-Q) and the HY spread widened 0.77pp in 3 months (macro overlay), which would compress earnings and the P/E on a heavily debt-funded balance sheet.",
    "veto": null
  },
  "thesis": "A high-ROE non-prime consumer lender returning heavy capital, but priced mid-range of its own P/E history and at a large P/B premium to peers, so the modest upside to base fair value does not compensate for a leveraged credit-cycle downside.",
  "rationale": "Returns are high and the decline since FY2021 is cyclical, but valuation offers little: P/E near its 5y median and peers, P/B well above peers, base fair value only slightly above the price against a deep bear case, with macro tilting toward bear. Good but not compelling: AVOID; cash is acceptable.",
  "price_at_decision": 56.09,
  "price_date": "2026-11-06",
  "research_note": "research/OMF/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 15% (22.7% now), showing credit costs are structurally eroding returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "Shares change YoY turns positive (-2.49% now), signalling dilution to fund capital.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Provision for finance receivable losses on the income statement grows more than 30% YoY for two consecutive quarters, outpacing receivables growth."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 66.75, "basis": "Spreads retrace and improving delinquencies (Q3 call) let the P/E re-rate toward the mechanical bull fair value of 66.75 [RA,IS]; probability trimmed for the macro overlay's small tilt toward bear (research/OMF/2026-11-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 60.48, "basis": "Earnings hold and P/E stays near its 5y median of 9.2x [RA], matching the mechanical base fair value of 60.48."},
    "bear": {"probability": 0.3, "target_price_12m": 30.68, "basis": "Provisions keep climbing (+26% in Q3, 10-Q) and funding costs rise, compressing P/E toward its 5y low of 4.7x [RA], the mechanical bear of 30.68; probability raised for the macro overlay's tilt toward bear (research/OMF/2026-11-09-macro.md)."}
  },
  "entry_price": 48.38,
  "entry_basis": "valuation file: base 60.48 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
