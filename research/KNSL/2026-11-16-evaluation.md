# Evaluation: Kinsale Capital Group (KNSL) — 2026-11-16
## Bear case
E&S pricing has turned. Q3 gross written premiums fell 4.8% [company-reported], with Commercial Property down 26.8% [company-reported] on "heightened competition" and Casualty up only 0.9% [company-reported] (https://www.sec.gov/Archives/edgar/data/1669162/000166916226000050/knsl-20260930.htm). [Certain] That drives the **Direction change**: ROIC is 3.0pp below its 2-year high of 27.3% and 1.4pp lower over 3 years [RA-T]. [Certain] If softening spreads to casualty, it is a multi-year cycle, not a blip. [Likely] The mechanical base fair value of 297.82 sits well below the price; P/B of 4.6x is still +86% to peers [RA]. [Certain] The 10.92% FCF yield is flattered by float growth (FCF conversion falling to 185.3%) and will shrink as premiums stall. [Likely] Any valuation support comes from trend strength (+12.9% above the 200-day [ST]); an extended price after a +31.8% six-month run risks a de-rating if growth keeps slowing. [Likely] CFO transition adds noise. [Guessing]

## Bull case
Kinsale is the lowest-cost E&S underwriter: a 75.4% combined ratio and 25.6% nine-month operating ROE in Q3 [OV transcript]. [Certain] Returns remain far above peers: ROIC 24.3%, ROE 27.8% TTM, flat on a year earlier [RA-T]. [Certain] The ROIC dip is a soft-market cycle with the balance sheet intact (net debt/EBITDA 0.09x site [RA]) and reserves developing favourably by $19.7 million in Q3 [company-reported] (https://www.sec.gov/Archives/edgar/data/1669162/000166916226000050/knsl-20260930.htm), not lost economics. [Likely] P/E 17.2x and EV/EBITDA 13.2x are below their 5y minimums [RA]. [Certain] Buybacks cut shares 1.83% YoY [ST]. [Certain] Higher yields on float (10y at 5.1%, macro overlay) lift investment income. [Likely] The P/B + ROE method caps ROE below Kinsale's level, so the mechanical base understates value. [Likely]

## Decision
```json
{
  "ticker": "KNSL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC 1.4pp lower over 3 years and 3.0pp below its 2-year high [RA-T] reflects E&S property price competition (Q3 GWP -4.8%, Commercial Property -26.8% [company-reported], 10-Q https://www.sec.gov/Archives/edgar/data/1669162/000166916226000050/knsl-20260930.htm) while the combined ratio stays 75.4% and reserves develop favourably: a cyclical soft market with the balance sheet intact.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The E&S soft market spreads from property to casualty, so premiums keep shrinking and the premium multiple de-rates further after the +31.8% six-month run.",
    "veto": null
  },
  "thesis": "The lowest-cost E&S underwriter, still earning ROE near 28% with a clean balance sheet, trades below its own 5-year multiple range but above peers while a soft market shrinks premiums.",
  "rationale": "Quality and balance sheet are excellent and multiples sit below their own 5-year range, but premiums are shrinking on competition, the mechanical fair value sits below the price and the premium to peers persists. Good but not compelling: no position.",
  "price_at_decision": 395.89,
  "price_date": "2026-11-13",
  "research_note": "research/KNSL/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, showing the soft market is eroding returns beyond a cyclical dip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 1.0x, breaking the clean balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Casualty gross written premiums (10-Q MD&A) decline year on year for two consecutive quarters, showing softening has spread beyond property."},
    {"text": "Prior-year reserve development (10-Q MD&A) turns net adverse in any quarter, or adverse development appears outside construction liability."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 454.79, "basis": "Casualty holds and buybacks continue, so the stock reaches the mechanical bull fair value of 454.79 [valuation file], still below its 5y median P/E of 26.1x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 390, "basis": "P/E stays near today's 17.2x [RA] as premiums stall but ROE near 27.8% [RA] and buybacks hold per-share value; above the mechanical base of 297.82 because the P/B + ROE method caps ROE below Kinsale's level (note section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 300, "basis": "Softening spreads to casualty and the P/E de-rates toward the peer median of 14.3x [RA, peers], close to the mechanical base fair value of 297.82."}
  },
  "entry_price": 238.26,
  "entry_basis": "valuation file: base 297.82 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
