# Evaluation: Sezzle Inc. (SEZL) — 2026-11-15
## Bear case
Credit is turning: 29+ day past-dues rose to about 15.7% of receivables from about 12.9% at year-end and the allowance rose [company-reported] (https://www.sec.gov/Archives/edgar/data/1662991/000166299126000171/szl-20260930.htm) [Certain]. ROIC fell from 118.1% to 94.4% in 12 months, 65.0pp below its 2-year high, and FCF margin slipped from 54.8% to 51.2% [RA-T, CF-T] [Certain]; if the cause is loss provisioning rather than book growth, it is structural [Guessing]. The valuation points come from trend strength, not a discount: the price is 37.4% above its 200-day average after +169.9% in 12 months, every multiple sits above its own 5y maximum and the reverse DCF needs 39.4% year-1 growth [Certain]; any slowdown de-rates a beta-6.60 stock hard [Likely]. BNPL is contestable, unsecured SezzleCash is unproven, a bank charter adds cost, and the macro overlay tilts moderately bear (real yields up, hike-leaning 2y) [Likely].

## Bull case
Q3 2026 was a beat-and-raise: revenue +42.6%, outpacing TTV, with FY26 and FY27 guidance raised (https://www.globenewswire.com/news-release/2026/11/04/3395777/0/en/sezzle-reports-third-quarter-2026-results.html) [Certain]. Economics are exceptional and the operating line is still improving: operating margin 60.0% TTM at a 2-year high, ROCE rising, FCF margin 51.2%, FCF 163.0% of net income [IS-T, RA-T] [Certain]. The ROIC dip looks like capital growing with the receivable book rather than a broken model [Likely]. The balance sheet is clean (net debt/EBITDA 0.09x, Altman Z 14.25, Piotroski 8), shares are shrinking 1.26% and insiders own 44.47% [Certain]. The FCF yield of 5.70% is real, EV/EBITDA 15.0x is below the peer median of 27.3x, and a subscriber base approaching one million adds stickiness [Likely].

## Decision
```json
{
  "ticker": "SEZL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Operating margin is at its 2-year high (60.0% TTM) and ROCE rose 3.2pp while ROIC fell, consistent with capital growing faster than profit as the receivable book expands (note section 2); FCF margin slipped only 3.6pp with revenue +42.6% (GlobeNewswire Q3 release).", "moat": "none", "key_risk": "high", "key_risk_text": "Consumer credit deterioration (29+ day past-dues up to about 15.7% from about 12.9%, 10-Q) combined with an extended price above its own 5y multiple range: a slowdown or loss spike would de-rate a beta-6.60 stock sharply, with the macro overlay tilting toward bear.", "veto": null},
  "thesis": "A highly profitable, fast-growing BNPL platform whose rising past-dues, thin moat and price far above its own multiple history make it good but not compelling.",
  "rationale": "Exceptional margins and a clean balance sheet, but the moat is thin, credit is deteriorating and the price already assumes sustained high growth; the scorecard does not reach the buy bar. Cash is acceptable.",
  "price_at_decision": 154.60,
  "price_date": "2026-11-13",
  "research_note": "research/SEZL/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 50%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "ROIC (TTM) falls below 60%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "29+ day past-due share of receivables (10-Q) rises above 20%"},
    {"text": "Quarterly revenue growth falls below 25% YoY"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 195.71, "basis": "Delivery on the raised FY26/FY27 guidance (GlobeNewswire Q3 release) with operating margin holding near 60.0% [IS] returns the price to its 52-week high of 195.71 [HI], above the mechanical bull 94.57 because the own-history multiples predate the profit step-up."},
    "base": {"probability": 0.4, "target_price_12m": 154.60, "basis": "Growth roughly matches the 39.4% year-1 growth the reverse DCF implies [fact sheet Fair value] and the multiple holds, so the price stays near the last close; above the base fair value 79.34, which is flagged unreliable (methods disagree 2.4x)."},
    "bear": {"probability": 0.35, "target_price_12m": 79.34, "basis": "Rising past-dues (10-Q) and the macro overlay's moderate bear tilt (real yields +0.47pp in 3 months, research/SEZL/2026-11-15-macro.md), which lifts this probability, de-rate P/E from 29.9x toward its 5y range [RA], taking the price to base fair value 79.34; the mechanical bear of -148.73 is not meaningful for a cash-generative business."}
  },
  "entry_price": 63.47,
  "entry_basis": "valuation file: base 79.34 x 0.8",
  "new_evidence": {"type": "method_change", "text": "The 2026-11-07 verdict was a TACTICAL drift assessment (AVOID 2) made before the scorecard (2026-11-09); this is the first CORE evaluation, with conviction set by scripts/scorecard.py."},
  "replaces": null,
  "replacement_reason": null
}
```
