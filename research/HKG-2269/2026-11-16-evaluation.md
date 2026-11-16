# Evaluation: WuXi Biologics (Cayman) Inc. (HKG:2269) — 2026-11-16
## Bear case
The price already sits at the mechanical base fair value (46.42 vs 46.74 HKD), so there is no discount cushion; the bear value is 26.69 [Certain]. P/E 34.1x is 44% above the peer median [Certain], and after a +40.2% year an extended multiple risks a de-rating if growth slows or the 25 Nov results disappoint [Likely]. The decisive risk is political: a China-based CRDMO serving Western drug developers is exposed to US biosecurity legislation and export controls; the revenue split by customer geography is [data unavailable], so exposure cannot be sized and no official source confirms or rules out a new event [Likely]. Net margin fell over five years to 21.2% even as operating margin recovered, so earnings quality lags the operating story [Certain]. The fair value rests on EV/Revenue alone (rNPV unavailable), and the bear-to-bull spread is wide [Certain].
## Bull case
The business is working: rolling-12-month ROIC rose to 13.9% from 10.5%, operating margin to 32.4% from 27.4% and FCF margin to 18.1% from 8.8% [Certain]. The capex cycle is maturing, with FCF conversion at 85.4% of net income from 54.1% in FY2025 [Certain], and net cash (net debt/EBITDA -1.14x), Altman Z 8.62 and Piotroski 7 make the balance sheet a non-issue [Certain]. EV/EBITDA 17.7x is at 8% of its five-year range and below peers, and P/FCF is below its five-year minimum [Certain]. Switching costs after process validation, another passed FDA GMP inspection and the Fresenius biosimilar option deal support a narrow moat [Likely]. The trend is healthy: 15.6% above the 200-day, ahead of SPY on 3/6/12 months, and the 6.0% dip below the 50-day has cooled RSI to 45.2 [Certain].
## Decision
```json
{
  "ticker": "HKG:2269",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are all rising on both the 5-year view and the rolling 12 months [RA-T, IS-T, CF-T]; only net margin and ROE fell over five years [IS, RA].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "US biosecurity legislation or export controls restrict Western customers from using a China-based CRDMO; exposure unsized because revenue by geography is unavailable, and a de-rating of an extended multiple would follow.",
    "veto": null
  },
  "thesis": "A recovering, net-cash biologics CRDMO whose returns and cash conversion are improving, but priced at its base fair value with an unsized US-China policy tail.",
  "rationale": "Quality and direction are strong and the balance sheet is net cash, but the price equals base fair value and the key political risk cannot be sized. The scorecard gives conviction below the buy bar; good but not compelling is an AVOID.",
  "price_at_decision": 46.74,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-2269/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 27%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 27}},
    {"text": "ROIC (TTM) falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "FCF margin (TTM) falls below 8%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Company-reported half-year revenue growth turns negative, or enacted US biosecurity/export restrictions name the company or cut customer revenue (company filings)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 58.0, "basis": "Margin and FCF gains continue (operating margin 32.4%, FCF margin 18.1% [IS-T, CF-T]) and the stock retests its 52-week high of 58.00 [HI], still below the bull fair value of 98.36."},
    "base": {"probability": 0.5, "target_price_12m": 46.42, "basis": "Price converges on the mechanical base fair value of 46.42 (EV/Revenue, fact sheet Fair value) as EV/EBITDA stays near 17.7x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 28.48, "basis": "A US biosecurity or export-control event de-rates the multiple back to the 52-week low of 28.48 [HI], near the bear fair value of 26.69."}
  },
  "entry_price": 37.14,
  "entry_basis": "valuation file: base 46.42 x 0.8; at that discount the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
