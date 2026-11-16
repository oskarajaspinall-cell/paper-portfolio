# Evaluation: H&R Block, Inc. (HRB) — 2026-11-16
## Bear case
Assisted tax prep faces slow substitution by DIY, free filing and AI tools; the Q1 filing shows rising retention and technology spend and higher legal accruals, which looks defensive [Likely]. Gross margin has drifted down to 43.7% and FCF margin is still below its FY2022 21.6% over three years, so the rolling recovery to 18.8% may be a timing swing, not a trend [Likely]. Retail office closures shrink the owned footprint [Likely]. Short interest of 15.02% shows a crowded bear view [Certain]. The price sits 25.7% above its 200-day average after a strong six months; if growth slows or the Investor Day on 3 December disappoints, an extended price risks a de-rating back toward the September swing low [Likely]. Fair value is flagged unreliable (methods disagree 2.2x), so the DCF upside cannot be leaned on [Certain]. New CEO and accounting officer add execution risk [Guessing].
## Bull case
Returns are exceptional and rising on a rolling basis: ROIC TTM 48.4% vs 43.5% a year earlier, ROCE 47.0% [Certain]. Operating margin is steady at 22.3% [Certain]. FCF margin rose from 15.3% to 18.8% over the last year, so the five-year decline is reversing; it came from investment, not lost pricing [Likely]. At 8.9x P/E and a 12.39% FCF yield the stock sits in the lower half of its own range and far below peers [Certain], while the reverse DCF implies -11.6% year-1 revenue against Q1 revenue growth and reaffirmed FY2027 guidance [Likely]. Buybacks cut shares 6.36% YoY, compounding per-share value [Certain]. Beta 0.41 and a price above its 200-day average show a business that is working with low market sensitivity [Certain]. Net debt/EBITDA 1.69x is seasonal and moderate [Likely].
## Decision
```json
{
  "ticker": "HRB",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell over three years but rose from 15.3% to 18.8% in the last 12 months [CF-T,IS-T]; the dip reflects retention and technology investment named in the Q1 10-Q (https://www.sec.gov/Archives/edgar/data/12659/000001265926000036/hrb-20260930.htm), with operating margin flat at 22.3% and FY2027 guidance reaffirmed (https://www.globenewswire.com/news-release/2026/11/09/3398946/0/en/h-r-block-reports-fiscal-2027-first-quarter-results-and-reaffirms-fiscal-2027-outlook.html).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "DIY/free/AI filing erodes assisted volumes and pricing, which would also de-rate a price now well above its 200-day average.",
    "veto": null
  },
  "thesis": "A very high-return, buyback-compounding assisted tax-prep franchise with recovering cash margins trades at a low multiple that prices shrinkage its reaffirmed guidance does not show, against a slow substitution risk.",
  "rationale": "Scorecard sets the conviction. Returns and cash margins are improving and the multiple is low, but substitution risk is real and fair value is unreliable. Holding keeps the existing position within its conviction size; no ADD below the buy bar.",
  "price_at_decision": 50.01,
  "price_date": "2026-11-13",
  "research_note": "research/HRB/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 35% (48.4% now), showing the returns franchise is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM operating margin falls below 19% (22.3% now), under the five-year range, showing price pressure from free/AI filing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 14% (18.8% now), meaning the cash recovery reversed.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "A 10-K/10-Q reports a year-on-year decline in U.S. assisted returns or revenue, or FY2027 guidance is cut below the reaffirmed range."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 72.0, "basis": "P/E re-rates to its 5y max 12.8x [RA] on TTM earnings as guidance is met and Investor Day targets land; still below the unreliable DCF base."},
    "base": {"probability": 0.5, "target_price_12m": 57.0, "basis": "P/E returns to its 5y median 10.2x [RA] on TTM earnings with buybacks and reaffirmed FY2027 guidance; below the mechanical base because the fair value is flagged unreliable and the EV/EBITDA method sits near the price."},
    "bear": {"probability": 0.25, "target_price_12m": 39.5, "basis": "Substitution worries de-rate the stock back to the September swing low 39.50 [HI], toward the low end of its 5y P/E range 6.6x [RA]."}
  },
  "entry_price": 46.3,
  "entry_basis": "P/FCF back at its 5y median 7.5x [RA] from 8.1x on TTM FCF; the mechanical base less 20% is above the price and the fair value is flagged unreliable, so it is not used.",
  "replaces": null,
  "replacement_reason": null
}
```
