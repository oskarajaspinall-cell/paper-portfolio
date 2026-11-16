# Evaluation: Broadcom Inc. (AVGO) — 2026-11-16
## Bear case
The price already assumes a lot. At 347.01 USD it sits above even the mechanical bull fair value of 266.18, and the reverse DCF implies 40.4% year-1 revenue growth [Certain]. Concentration is rising: the top five end customers were about 55% of Q3 revenue, against about 40% a year earlier [company-reported] (https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm). Broadcom also guarantees about $29 billion of customer lease obligations to a financial partner [company-reported] (same URL), which is off-balance-sheet credit risk tied to AI labs [Likely]. The 10-Q now warns that the AI upturn "may not be sustainable" [Certain]. The trend is broken: the price is 5.6% below its 200-day average, 3-month momentum is -16.9%, and with beta at 1.51, rising real yields press on a 2.51% FCF yield (macro overlay, tilt toward bear, small) [Likely]. FCF conversion has slipped to 103.0% [Certain].

## Bull case
This is an excellent business that is getting better. TTM ROIC is 30.7%, up from 18.1% a year earlier, and operating margin is 48.8%, both at their 2-year highs [Certain] (https://stockanalysis.com/stocks/avgo/financials/ratios/?p=trailing). The **Direction change** in FCF margin (-6.4pp over five fiscal years) mostly reflects the FY2024 VMware trough, when FCF margin was 37.6%. Over the last 12 months it rose from 41.6% to 44.2% [Certain], so the decline is explained and temporary [Likely]. Net debt/EBITDA is down to 0.68x and Piotroski F is 7 [Certain]. Switching costs in custom XPU design are a real moat [Likely]. Relative to peers, EV/EBITDA is 10% below the median and P/FCF 28% below it [Certain]. The selloff after the Nvidia CEO headlines is sector-wide and unverified [Guessing].

## Decision
```json
{
  "ticker": "AVGO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin is falling on the 3-year and 5-year view because of the FY2024 VMware trough (37.6% [CF,IS]). It has risen over the last 12 months from 41.6% to 44.2% [CF-T,IS-T], and ROIC rose from 18.1% to 30.7% [RA-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Top-five customer concentration (about 55% of Q3 revenue [company-reported], sec.gov 10-Q) and the $29 billion lease guarantee mean a cut in one hyperscaler's AI spending would hit revenue and the multiple together, at a price that already implies 40.4% year-1 growth.",
    "veto": null
  },
  "thesis": "A best-in-class AI semiconductor and infrastructure-software franchise with rising returns and low leverage, but the price already implies 40.4% year-1 growth and sits below its 200-day average, so neither a discount nor trend strength supports a buy.",
  "rationale": "Quality, direction and the balance sheet are excellent, but the valuation earns no points: the price is above even the mechanical bull fair value, and the stock trades below its 200-day average, so it gets no trend-strength points either. Rising customer concentration and lease guarantees add risk. Conviction 3 means AVOID. Cash is acceptable.",
  "price_at_decision": 347.01,
  "price_date": "2026-11-13",
  "research_note": "research/AVGO/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 40% (48.8% now), showing AI mix or VMware pricing gains are reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM ROIC falls below 20% (30.7% now), giving up the last year's improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 35%, under the FY2024 trough of 37.6%, showing cash conversion is breaking down (for example, through XPU leasing).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35}},
    {"text": "The 10-Q shows top-five customer share rising further, a payment under the AI lease guarantee, or quarterly revenue lower year on year."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 495.0, "basis": "AI XPU demand carries ROIC and margins further above their 2-year highs [RA-T] and the stock retests its 52-week high of 495.00 [HI]."},
    "base": {"probability": 0.4, "target_price_12m": 344.9, "basis": "Growth roughly matches what the price implies, so the stock holds near its 50-day average of 344.90 [ST,HI]. This is well above the mechanical base of 108.77, because the through-cycle DCF ignores the AI ramp in ROIC from 18.1% to 30.7% [RA-T]."},
    "bear": {"probability": 0.35, "target_price_12m": 266.18, "basis": "A customer spending cut or a real-yield de-rating takes the price to the mechanical bull fair value of 266.18 [fact sheet]. The macro overlay's small tilt toward bear (research/AVGO/2026-11-16-macro.md) moves weight from bull to bear."}
  },
  "entry_price": 266.18,
  "entry_basis": "Valuation file: bull fair value 266.18 [IS,BS,CF,RA,ST,HI], used instead of the default base 108.77 x 0.8, which ignores the AI ramp in ROIC [RA-T]. At that level the price would no longer exceed every fair-value case. The anchor is the evaluator's judgement.",
  "replaces": null,
  "replacement_reason": null
}
```
