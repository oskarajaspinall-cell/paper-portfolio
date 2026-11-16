# Evaluation: Royal Gold, Inc. (RGLD) — 2026-11-16
## Bear case
RGLD is a leveraged bet on the gold price that macro isn't supporting: the 10y TIPS yield rose to 2.86% and the dollar firmed over ~3m while the stock gained +32.8% in 12 months (macro overlay) [Likely]. Gold is ~73% of revenue [company-reported] and costs are few, so a gold fall goes straight to margin and the multiple [Likely]. The returns are already slipping. Rolling ROIC fell from 14.0% to 11.5% and operating margin from 67.5% to 63.1% [RA-T, IS-T] [Certain], and the shares rose 27.57% YoY to pay for the acquisitions [ST] [Certain]. The mechanical base fair value of 113.66 sits far below 256.89 [Certain]. Part of the price support is trend strength, so a slower gold market or slower growth risks a de-rating from a P/B already above its 5y max [Likely]. Pueblo Viejo is ~10.5% of revenue, and nobody has checked the Dominican Republic politics [Guessing].
## Bull case
A royalty/stream model with 86.6% gross margin, 63.1% operating margin and FCF conversion of 138.8% [IS, CF] [Certain]. The fall in ROIC is acquisition capital that isn't fully earning yet, not erosion [Likely]. The debt was repaid in full on 19 Oct 2026 and a buyback is running [company-reported] [Likely]. Q3 set records for revenue, GEO sales and operating cash flow, and guidance was backed [OV] [Likely]. On cash and earnings it is cheap: P/FCF 18.7x is below its 5y minimum, P/E is 4% into its range and EV/EBITDA is 25% below peers, with a 5.36% FCF yield [RA, ST] [Certain]. Beta is 0.46, and the stock is above its 200-day average without being overextended [ST] [Certain]. The mechanical fair value runs on 5y-average EBITDA, so it misses the enlarged portfolio [Guessing].
## Decision
```json
{
 "ticker": "RGLD",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {"decline_cause": "temporary", "decline_evidence": "Rolling ROIC 14.0% -> 11.5% and operating margin 67.5% -> 63.1% [RA-T, IS-T] follow the late-2025 Sandstorm/Horizon acquisitions whose capital is not yet fully earning (note section 2); balance sheet intact with net debt/EBITDA -0.03x and debt fully repaid after quarter end [company-reported].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A fall in the gold price (~73% of revenue) as real yields and the dollar rise (macro overlay) would cut revenue, margin and the multiple; with the price partly supported by trend strength, a de-rating is the main risk.", "veto": null},
 "thesis": "A high-margin, debt-free royalty and streaming franchise trading low in its own earnings and cash-flow multiple ranges, but whose value hinges on a gold price that rising real yields and a firmer dollar are not supporting.",
 "rationale": "The business is high quality and the multiples look cheap, but rolling returns are falling, the mechanical value is far below the price and the macro tilt leans against gold. The scorecard gives conviction 3, which is good but not compelling, so the decision is AVOID with an entry price.",
 "price_at_decision": 256.89,
 "price_date": "2026-11-13",
 "research_note": "research/RGLD/2026-11-16.md",
 "triggers": [
  {"text": "TTM ROIC falls below 10%, showing the acquired streams are not earning their capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
  {"text": "TTM operating margin falls below 58%, showing mix or cost pressure is structural rather than an acquisition lag.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 58}},
  {"text": "TTM FCF margin falls below 55%, showing cash conversion is weakening outside deal years.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 55}},
  {"text": "Net debt/EBITDA rises above 1.5x, i.e. debt-funded deals again outrun cash flow.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
 ],
 "scenarios": {
  "bull": {"probability": 0.25, "target_price_12m": 302.49, "basis": "Gold holds and the acquired streams ramp, so EV/EBITDA moves back towards its 5y median 16.6x [RA]. That matches the mechanical bull fair value of 302.49."},
  "base": {"probability": 0.45, "target_price_12m": 265.0, "basis": "Record Q3 cash flow and backed guidance [OV] keep EV/EBITDA near today's 14.9x [RA], with modest per-share growth from buybacks. This sits well above the mechanical base of 113.66 because that figure uses 5y-average EBITDA from before the 2025 acquisitions."},
  "bear": {"probability": 0.30, "target_price_12m": 190.0, "basis": "The macro overlay's small tilt toward bear (real yields and the dollar rising) is applied here as a larger bear weight. Gold falls, and EV/EBITDA compresses towards its 5y min 13.3x [RA] on lower EBITDA, near the 6-month low of 186.32 [HI]."}
 },
 "entry_price": 90.93,
 "entry_basis": "valuation file: base 113.66 x 0.8 (default margin of safety on the mechanical base fair value [IS,BS,CF,RA,ST,HI]).",
 "replaces": null,
 "replacement_reason": null
}
```
