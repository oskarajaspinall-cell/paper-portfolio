# Evaluation: East West Bancorp, Inc. (EWBC) — 2026-11-09
## Bear case
The stock is priced for perfection. P/B 2.0x is above its 5y maximum of 1.9x and well above the peer median of 1.2x, and P/E 12.5x sits at 95% of its 5y range [Certain]. Mechanical fair value is flagged unreliable (methods disagree 3.8x); the best-fit P/B + ROE base of 121.79 is below the close of 128.84 [Certain]. The macro overlay tilts toward bear: VIX 28.18 and a widening HY spread have not yet de-rated the stock, and a move toward 1.7x book would cut it sharply [Likely]. The cross-border China franchise is a material but unquantified exposure named in the 10-Q [Certain]. The **Direction change** line: FCF margin is falling over five fiscal years while rising over the last 12 months (58.6% -> 64.6%); for a bank FCF mostly reflects working-capital swings, so it is not a clean quality signal either way [Likely]. TCE eased to 10.02% from 10.54% [company-reported] [Certain].

## Bull case
EWBC is a best-in-class regional bank: ROE 16.6% TTM, flat over five years, and a Q3 2026 efficiency ratio of 34.40% [company-reported] point to a durable cost and niche cross-border deposit advantage [Likely]. Q3 delivered record revenue, NII and EPS, with FY NII growth guidance raised and charge-off guidance lowered [Likely]. P/E 12.5x is still 9% below the peer median of 13.7x, the FCF yield is 10.58% and the share count is shrinking (-0.41% YoY) [Certain]. The reverse DCF implies -0.9% year-1 revenue growth, undemanding if ROE holds [Likely]. The rolling FCF margin is at its 2-year high, so the five-year fall is not a sign of a broken model [Likely]. The premium to book is earned by returns far above peers [Likely].

## Decision
```json
{
  "ticker": "EWBC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only the FCF margin is falling (3-year, -4.0pp); over the last 12 months it rose from 58.6% to 64.6% to a 2-year high [CF-T], ROE is flat at 16.6% TTM [RA], and bank FCF largely reflects working-capital swings, not lost share or a broken model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A risk-off move (VIX 28.18, HY spread widening, per the macro overlay) or US-China stress raises provisions and compresses a P/B multiple already above its 5y maximum.",
    "veto": null
  },
  "thesis": "A high-ROE, low-cost cross-border bank with record Q3 results, but priced above its own 5-year P/B range and near the top of its P/E range, leaving little margin of safety into a risk-off macro backdrop.",
  "rationale": "Quality is real (ROE 16.6%, efficiency 34.40% [company-reported]) but valuation is stretched against its own history, the fair value is unreliable with the best-fit method below the price, and the macro overlay tilts toward bear. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 128.84,
  "price_date": "2026-11-06",
  "research_note": "research/EWBC/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 13%, well under the five-year range (15.7%-19.1%), showing the return premium over peers is eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 13}},
    {"text": "TTM net margin falls below 45%, under the five-year low of 48.9%, signalling funding-cost or provision pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}},
    {"text": "Net interest margin in the 10-Q MD&A falls below 3.2%, or the TCE ratio falls below 9%."},
    {"text": "Net charge-offs rise materially above the lowered guidance, or the company discloses a material US-China regulatory or trade action affecting its cross-border business."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 160.0, "basis": "Record Q3 NII and lowered charge-off guidance [OV transcript] carry earnings higher and P/E moves toward the peer median 13.7x [RA], short of the fair-value bull 168.23."},
    "base": {"probability": 0.5, "target_price_12m": 133.0, "basis": "ROE holds near 16.6% [RA] and P/E stays near 12.5x on modest earnings growth, between the P/B + ROE base 121.79 and the blended base 138.43 (flagged unreliable)."},
    "bear": {"probability": 0.3, "target_price_12m": 110.0, "basis": "Per the macro overlay (tilt toward bear, small; probability moved toward bear), a risk-off shift compresses P/B toward its 5y median 1.7x [RA] and lifts provisions."}
  },
  "entry_price": 110.74,
  "entry_basis": "valuation file: base 138.43 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
