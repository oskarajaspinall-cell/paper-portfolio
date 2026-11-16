# Evaluation: Arista Networks, Inc. (ANET) — 2026-11-16
## Bear case
The price already assumes everything goes right. The reverse DCF needs 49.4% year-1 revenue growth, above the 38%-40% FY27 guide [Certain]. P/E is 50.0x and EV/EBITDA 44.3x, above its 5y max, with a premium to peers [Certain]. The mechanical base fair value is 73.75 [Certain]. The trend is strong, 17.7% above the 200-day average, but that is the risk: if AI capex growth slows, a stretched multiple de-rates before earnings fall, and beta 1.64 amplifies it [Likely]. Two customers were 16% and 26% of FY2025 revenue [company-reported], so one order pause would hit hard [Likely]. FCF margin fell from 47.9% to 42.2% over 12 months and ROIC is below its 284.8% 2-year high. The 10-Q adds supply-shortage and excess-inventory risk, and gross margin is slipping on component costs [Certain]. Real yields rose 0.47pp in 3m, which squeezes long-duration multiples (macro overlay) [Certain].
## Bull case
This is a superb business that is working. Operating margin is 43.8% TTM, up from 31.4% in FY2021, ROIC is 239.9%, the balance sheet is net cash and FCF conversion is above 100% [Certain]. Q3 beat and the FY27 guide of 38%-40% growth shows AI fabric demand still compounding [Likely]. The FCF-margin dip looks temporary: it reflects working capital and an inventory build for supply-constrained parts while operating margin hit a 2-year high, not lost share or a price cap [Likely]. The EOS software and open-standards design keep hyperscalers loyal, a real moat even if merchant silicon makes it contestable [Likely]. The stock is +42.4% over 12 months with an FCF yield of 2.01% [Certain]. The mechanical DCF likely understates a compounder at this growth rate [Guessing].
## Decision
```json
{
  "ticker": "ANET",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell from 47.9% to 42.2% TTM and ROIC sits below its 2-year high while operating margin reached its 2-year high of 43.8%; the 10-Q attributes pressure to supply commitments and inventory build for constrained components, i.e. working capital for growth, not lost share (https://www.sec.gov/Archives/edgar/data/1596532/000159653226000254/anet-20260930.htm).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The price implies 49.4% year-1 growth versus a 38%-40% guide, with multiples above their 5y max: any AI-capex slowdown or a pause by one of the two customers that were 16% and 26% of revenue would de-rate the stock sharply.",
    "veto": null
  },
  "thesis": "An exceptional, net-cash AI networking franchise whose growth is real but whose price already discounts more growth than management guides.",
  "rationale": "Quality and momentum are outstanding, but the multiple sits above its own 5y range and the price needs growth beyond the guide, so trend strength earns no valuation points and the scorecard sits well below the buy bar. No position; cash is an acceptable outcome.",
  "price_at_decision": 197.29,
  "price_date": "2026-11-13",
  "research_note": "research/ANET/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 58% (62.9% now), showing component costs or pricing pressure from merchant-silicon rivals are structural.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "TTM operating margin falls below 38% (43.8% now), reversing the operating leverage that underpins the thesis.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM FCF margin falls below 30% (42.2% now), showing the inventory build is not temporary working capital.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "A 10-Q/10-K or release discloses that either of the two largest customers cut purchases materially or fell below 10% of revenue without replacement growth."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 270, "basis": "FY27 growth of 38%-40% is delivered and beaten [OV news], operating margin holds at 43.8% [IS] and P/E stays near its 5y max of 52.5x [RA]; the bull is far above the mechanical bull fair value because the DCF fades growth faster than the guide."},
    "base": {"probability": 0.45, "target_price_12m": 205, "basis": "Earnings grow with the guide [OV news] but P/E compresses toward its 5y median of 47.0x [RA], so price roughly tracks today's level; well above the 73.75 base fair value because the mechanical DCF does not capture guided growth."},
    "bear": {"probability": 0.30, "target_price_12m": 115, "basis": "AI-capex slowdown or a large-customer pause de-rates P/E toward its 5y min of 27.4x [RA] on flat TTM earnings; probability moved up a small step for the macro overlay's toward-bear tilt on rising real yields (research/ANET/2026-11-16-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3, so no entry price applies; the obstacle is a multiple above its own 5y range plus high customer and growth-expectation risk, not one price level.",
  "replaces": null,
  "replacement_reason": null
}
```
