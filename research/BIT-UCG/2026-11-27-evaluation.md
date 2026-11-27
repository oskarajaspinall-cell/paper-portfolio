# Evaluation: UniCredit S.p.A. (BIT:UCG) — 2026-11-27
## Bear case
The re-rating is already paid for: P/B 1.6x sits at the 95th percentile of its 5y range and 31% above the peer median [Certain]. ROE of 16.1% TTM is partly a rate-cycle product, so returns can fade with euro rates [Likely]. The dip has no confirmed stock-specific cause; candidates are Commerzbank integration risk and a possible bigger Generali stake, both capital-allocation questions whose price and funding are unverified [Guessing]. Commerzbank adds German political and job-cut execution risk and an unquantified rise in German exposure [Likely]. The mechanical fair value is flagged unreliable (methods disagree 3.0x), so the apparent discount to base 89.10 is weak evidence [Certain]. The price is below its 200-day average, so there is no healthy uptrend to lean on either [Certain]. Piotroski F of 4 is middling [Certain].

## Bull case
ROE has risen every year from 3.5% in FY2021 to 16.8% in FY2025, with net margin at 45.1% TTM [Certain]. Buybacks cut the share count 1.54% YoY [Certain]. P/E of 10.3x is in line with peers at 10.4x despite a higher ROE than most [Certain]. The Commerzbank takeover is now fully authorised, removing a regulatory overhang, and Commerzbank itself raised its 2026 profit outlook [Likely]. Management targets 15%+ EPS growth and RoTE above 20% per the conference transcript headline [Guessing]. The ECB deposit rate rose to 2.5%, supportive for net interest income (macro overlay, context) [Likely]. The fall came without an earnings-type reaction, so it may be sentiment, not business damage [Likely].

## Decision
```json
{
  "ticker": "BIT:UCG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists nothing falling: ROE rose from 3.5% (FY2021) to 16.1% TTM and rolling FCF margin rose to 68.6% [RA, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Commerzbank integration and capital allocation (deal price, German politics, a possible larger Generali stake) dilute returns while P/B already sits at its 5y high.",
    "veto": null
  },
  "thesis": "A high-ROE pan-European bank with buybacks and an authorised Commerzbank deal, but already at the top of its own book-multiple range with no confirmed cause for the dip.",
  "rationale": "Quality is real and rising, but the dip has no confirmed cause, the price sits below its 200-day average, P/B is at its 5y high and the fair value is unreliable. The same evidence as the 2026-11-16 AVOID; good but not compelling.",
  "price_at_decision": 73.85,
  "price_date": "2026-11-26",
  "research_note": "research/BIT-UCG/2026-11-27.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, giving up most of the five-year rise.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM net margin falls below 35%, signalling the rate tailwind or cost discipline is fading.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}},
    {"text": "Shares change YoY rises above +3%, i.e. the Commerzbank deal is funded by dilution rather than buybacks.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 89.1, "basis": "Commerzbank synergies keep ROE rising and the price reaches the mechanical base fair value 89.10 [IS,BS,CF,RA,ST,HI], above the 52-week high 86.42 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 78.0, "basis": "ROE holds near 16.1% [RA] and P/E stays near the peer median 10.4x [RA]; the price recovers toward its 50-day average 78.27 [ST,HI] with no further re-rating since P/B is already at its 5y high."},
    "bear": {"probability": 0.25, "target_price_12m": 57.36, "basis": "Integration or rate fade cuts returns and P/B de-rates toward the peer median 1.2x [RA], taking the price back to its 52-week low 57.36 [HI]."}
  },
  "entry_price": 66.0,
  "entry_basis": "Base fair value less 15% (89.10 x 0.85) is above the price, and that fair value is flagged unreliable; instead a price near the 2026-06-11 six-month low 69.81 [HI] or below, where P/B would fall back from the top of its 5y range [RA], set at 66.0.",
  "replaces": null,
  "replacement_reason": null
}
```
