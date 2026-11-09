# Evaluation: Qilu Bank Co., Ltd. (SHA:601665) — 2026-11-09
## Bear case
A 0.7x P/B on an 11.0% ROE is the market discounting book quality, and nothing we hold can refute it: property and local-government exposure are invisible in the fact sheet, and the results due Oct 30, 2026 were not read [Certain]. Net margin fell from 57.1% (FY2024) to 43.5% (FY2025), cause unverified, which could be rising provisions or margin compression [Guessing]. Piotroski F of 2 is weak and shares outstanding rose 2.32% YoY, diluting holders at a discount to book [Certain]. The Direction change line (FCF margin down over five years, up over 12 months) is deposit and loan flow at a bank, not economics, so it neither threatens nor supports the thesis [Likely]. Valuation is mid-range: P/E 6.8x sits at the 47th percentile of its 5y range and in line with peers, P/B at the 68th [Certain]. The 10.11 base fair value is flagged unreliable (methods disagree 5.8x) [Certain].
## Bull case
ROE has edged up every year from 10.3% to 11.3% (FY2021-FY2025) through a difficult Chinese banking cycle, a steadier record than many regional peers [Certain]. P/B of 0.7x is 11% below peers' 0.8x, and the best-fit P/B + ROE method gives 7.64 CNY base, above the 6.52 close [Certain]. The reverse DCF implies -8.7% year-1 revenue growth, a pessimistic bar for a bank still compounding book [Likely]. Beta of 0.28 makes it a low-correlation diversifier [Certain]. If asset quality proves benign, a P/E re-rating toward the 5y high of 9.1x is possible [Guessing].
## Decision
```json
{
  "ticker": "SHA:601665",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The only falling scored metric is FCF margin, which at a bank reflects deposit and loan flows rather than earning power; it rose over the last 12 months (268.9% -> 293.5%, CF-T) while ROE rose from 10.3% to 11.3% over FY2021-FY2025 [RA].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Undisclosed asset-quality deterioration (property / local-government loans) behind the unexplained net margin fall from 57.1% to 43.5% and the 0.7x P/B; latest results unread.",
    "veto": null
  },
  "thesis": "A steady 11% ROE Chinese city bank at 0.7x book, but asset quality is unverified and the discount looks like a fair price for that risk.",
  "rationale": "Moderate returns, no evident moat, a weak Piotroski score, dilution and an unexplained net margin drop, with valuation only mid-range versus its own history and peers. The headline fair value is flagged unreliable; the best-fit P/B + ROE method gives only modest upside. Good-but-not-compelling is an AVOID.",
  "price_at_decision": 6.52,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601665/2026-11-09.md",
  "triggers": [
    {"text": "ROE falls below 10% TTM (earnings power eroding).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net (profit) margin falls below 40% TTM, extending the FY2025 drop.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "Shares outstanding rise more than 3% YoY (dilution below book).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 8.73, "basis": "Asset quality proves benign and P/E re-rates to its 5y high of 9.1x [RA] on flat TTM earnings."},
    "base": {"probability": 0.45, "target_price_12m": 7.64, "basis": "P/B + ROE base fair value 7.64 [fact sheet Fair value], the best-fit bank method; the 10.11 blend is set aside because it is flagged unreliable and the FCFE input is distorted for a bank (note section 3)."},
    "bear": {"probability": 0.3, "target_price_12m": 5.56, "basis": "Provisions keep pressing the net margin (57.1% to 43.5% [IS]) and P/E reverts to its 5y median 5.8x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: asset quality and the cause of the net margin fall are unverified and the latest results unread; a lower price alone would not lift this to conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
