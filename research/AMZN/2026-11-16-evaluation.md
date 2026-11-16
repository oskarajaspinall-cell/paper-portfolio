# Evaluation: Amazon.com, Inc. (AMZN) — 2026-11-16
## Bear case
Cash conversion has broken: TTM FCF margin is -5.9% against 1.5% a year earlier and FCF yield is -1.63% [Certain]. Nine-month capex of $175.7bn against $92.3bn [company-reported] has pulled TTM ROIC down to 10.9% from 15.0%, 6.8pp below its 2-year high, and ROCE to 10.6% [Certain]. Whether the AI capacity earns its cost is unproven [Likely]. The 21.1x P/E flatters: net margin (16.9%) above operating margin (13.1%) reflects Anthropic mark-ups, not operations [Certain]. The price (266.66) sits above even the mechanical bull fair value (254.91), and EV/Sales is above its 5y maximum [Certain]. The trend is only moderate (+9.0% over the 200-day), so an extended price risks a de-rating if AWS growth slows, made worse by a beta of 1.50 and real yields up 0.47pp in ~3m (macro overlay) [Likely]. Net debt/EBITDA has risen to 1.04x from 0.38x [Certain].
## Bull case
Operating quality is still improving: operating margin is at its 2-year high of 13.1% and gross margin has risen to 51.4% from 42.0% as advertising and AWS grow in the mix [Certain]. The ROIC and FCF decline is a denominator effect of heavy investment, not lost share or price caps, because operating margin rose over the same 12 months [Likely]. AWS backlog of about $578 billion with a 6.1-year average life [company-reported] underwrites the capex [Likely]. EV/EBITDA of 16.7x sits below its 5y minimum and 24% under peers [Certain]. The balance sheet is intact (Altman Z 3.77) and capital is being recycled through the Blackstone data-centre sale [Likely]. The moat (logistics scale, Prime, AWS switching costs) is wide [Likely]. The Leo launch failure is a cost, not a thesis break [Likely].
## Decision
```json
{
  "ticker": "AMZN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC, ROCE and FCF margin fell over 12 months while operating margin rose to its 2-year high of 13.1% [IS-T]; the cause is nine-month capex of $175.7bn vs $92.3bn [company-reported] (https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), heavy investment with the balance sheet intact (net debt/EBITDA 1.04x).",
    "moat": "wide",
    "key_risk": "high",
    "key_risk_text": "AI capex fails to earn its cost of capital, keeping FCF negative and ROIC falling, while the price, above mechanical fair value, de-rates if AWS growth slows or real yields rise further.",
    "veto": null
  },
  "thesis": "A wide-moat retail, advertising and cloud franchise with rising operating margins is in a heavy AI-capex cycle that has turned FCF negative and cut ROIC, at a price above its mechanical fair value.",
  "rationale": "The business is strong and the decline looks investment-driven, but FCF is negative, so there is no FCF yield to support trend-strength points and no discount to fair value. Payback on the capex is unproven. Good but not compelling: AVOID, with an entry price where a real discount would exist.",
  "price_at_decision": 266.66,
  "price_date": "2026-11-13",
  "research_note": "research/AMZN/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 11%, reversing the mix gains that underpin the thesis.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM ROIC falls below 8% while capex still grows, showing the investment is not earning its cost.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA exceeds 2.5x, meaning the capex has become debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM gross margin falls below 48%, showing the advertising/AWS mix shift has reversed.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 48}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 287.20, "basis": "AWS backlog of about $578 billion [company-reported] converts and operating margin keeps rising, so EV/EBITDA moves from 16.7x toward its 5y median 19.6x [RA], retesting the 52-week high of 287.20 [HI]; above the mechanical bull because EV/Revenue alone ignores the margin gains."},
    "base": {"probability": 0.45, "target_price_12m": 241.22, "basis": "Capex payback stays unproven and FCF negative, so the price drifts to the mechanical base fair value of 241.22 on EV/Revenue [valuation file], with EV/Sales above its 5y max [RA] the anchor."},
    "bear": {"probability": 0.30, "target_price_12m": 196.00, "basis": "ROIC keeps falling and real yields rise further (macro overlay tilt toward bear, small, raising this probability), de-rating the stock to its 52-week low of 196.00 [HI]; above the mechanical bear of 119.62 because operating margin at 13.1% [IS-T] does not support an EV/Revenue trough multiple."}
  },
  "entry_price": 192.98,
  "entry_basis": "valuation file: base 241.22 x 0.8; at that price the stock would trade at a real discount to fair value, which negative FCF currently denies it through trend strength.",
  "replaces": null,
  "replacement_reason": null
}
```
