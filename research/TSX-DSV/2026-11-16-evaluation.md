# Evaluation: Discovery Mining Ltd. (TSX:DSV) — 2026-11-16
## Bear case
DSV is a price-taking gold miner: ROIC of 90.0% TTM mostly reflects the gold price, not a moat [Likely]. The macro overlay tilts toward bear (moderate): the 10y real yield rose +0.47pp to 2.86% and the dollar strengthened, both adverse for gold [Likely]. Direction is already turning: ROIC sits 19.9pp below its 2-year high, operating margin 3.4pp below its high of 44.4%, and FCF margin fell from 26.9% to 9.5% as capex for Cordero and Timmins ramps [Certain]. Growth is partly funded by dilution, shares up 36.27% YoY [Certain]. The stock trades at a large peer premium (P/E 21.1x vs 9.4x, P/FCF 46.1x vs 11.1x) with FCF yield 2.17% and beta 2.27 [Certain]. There is no computable fair value, and the price is below its 200-day average with -14.5% 3-month momentum, so neither a discount nor a working trend supports it [Certain].
## Bull case
Q3 2026 was a record for production and revenue, with cash rising to fund growth and a net-cash balance sheet (net debt/EBITDA -0.62x) [Likely]. Cordero cleared federal permitting and Dome and Pamour drilling keeps extending mineralization, giving a multi-asset growth pipeline in a stable jurisdiction [Likely]. The FCF-margin drop is investment-driven, not operational: operating margin is still up 7.9pp on the year to 41.1% [Certain] and ROCE rose to 24.1% [Certain]. The 50-day average stays above the 200-day by +15.7% and the 12-month change is +41.3%, so the long uptrend is intact despite the pullback [Certain]. If real yields fall below ~2.4% (overlay macro_bull), gold firms and operating leverage at beta 2.27 drives a re-test of the 13.43 high [Guessing].
## Decision
```json
{
  "ticker": "TSX:DSV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 26.9% -> 9.5% while operating margin rose 7.9pp to 41.1%: the drop is growth capex for Cordero (permitted Oct 2026) and the Timmins pits, per the Q3 2026 release (https://www.globenewswire.com/news-release/2026/11/10/3399263/0/en/discovery-reports-record-gold-production-sales-solid-earnings-strong-cash-generation-in-q3-2026.html); ROIC and margin are small slips from record highs with net cash intact.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "A falling gold price as real yields and the dollar rise (macro overlay, tilt toward bear) compresses margins and the large peer-premium multiple at beta 2.27.",
    "veto": null
  },
  "thesis": "A fast-growing, net-cash gold miner with a permitted pipeline, but its returns are a gold-price windfall and the stock trades at a large peer premium with no computable fair value.",
  "rationale": "Quality is real but commodity-driven with no moat; the multiple is far above peers, FCF yield is thin, dilution is heavy and the price sits below its 200-day average, so neither discount nor trend strength supports conviction 4. The macro overlay leans bear. Cash is the better outcome.",
  "price_at_decision": 9.51,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-DSV/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 30%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "ROIC (TTM) falls below 40%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Net debt / EBITDA rises above 1.5x as growth capex consumes the net cash position", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Shares outstanding growth stays above 20% YoY at the next annual report (dilution continues to fund growth)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 13.43, "basis": "Real yields fall below ~2.4% (overlay macro_bull), gold firms and Q3 record production carries the stock back to its 52-week high of 13.43 [HI]; probability trimmed for the overlay's moderate bear tilt."},
    "base": {"probability": 0.45, "target_price_12m": 9.97, "basis": "Operating margin holds near 41.1% [IS-T] while capex keeps FCF yield near 2.17% [ST]; the stock drifts back to its 200-day average of 9.97 [ST,HI], with no fair value to anchor beyond that."},
    "bear": {"probability": 0.35, "target_price_12m": 7.02, "basis": "Real yields above 3% and a stronger dollar (macro overlay, tilt toward bear, moderate, raising this probability) cut gold and margin, and the P/E premium to peers (21.1x vs 9.4x [RA]) compresses to the 6-month low of 7.02 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
