# Evaluation: Tradeweb Markets Inc. (TW) — 2026-11-16
## Bear case
The price already discounts a lot: the reverse DCF implies 19.7% year-1 revenue growth, and the mechanical base fair value of 92.56 sits 30.3% below the 132.74 close, with even the bull case (134.18) barely above it [Certain]. The stock is extended: 20.2% above its 200-day average and RSI 83.0 [Certain]. If volume growth slows, a de-rating toward the peer P/E of 26.1x is the likely path [Likely]. P/FCF of 26.7x is 41% above peers [Certain]. FCF margin is falling over the last year (52.6% to 50.6%) and 3 years, 4.3pp below its 2-year high, even as operating margin rises; FCF/NI fell to 127.0% [Certain]. The cause looks like cash conversion normalising rather than lost share [Likely], but it caps the cash yield at 3.75% [Certain]. The pending Trumid deal, terms unknown, could dilute ROIC again [Likely]. Real yields rose 0.47pp in ~3m, a multiple headwind (macro overlay, context only) [Certain].
## Bull case
Tradeweb is a network-liquidity franchise: dealers and asset managers trade where counterparties already are [Likely]. It is working: ROIC rose to 10.5% TTM from 5.2% in FY2021, operating margin to 44.1% from 33.9%, ROE to 14.5% [Certain], and the last 12 months improved on both ROIC and operating margin [Certain]. Q3 2026 showed growth across credit, wholesale and market data [Certain]. P/E of 31.1x is at the 5% point of its own 5y range [Certain]; the derating has been earnings catching up [Likely]. Buybacks shrink the share count by 0.95% a year and FCF conversion stays above 100% [Certain]. Beta is 0.56, so it is a defensive grower [Certain]. The trend is strong: +20.8% over 12 months, beating SPY by 10.4pp [Certain]. Low ROIC mostly reflects acquisition goodwill, not weak economics [Likely].
## Decision
```json
{
  "ticker": "TW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin electronic fixed-income marketplace with improving returns, but the price already discounts strong growth and has run well ahead of its trend.",
  "rationale": "Quality is improving and the moat is real, but the price sits far above the mechanical base fair value, the reverse DCF needs high growth, and the stock is overbought after a sharp run. Good but not compelling at this price; cash is acceptable.",
  "price_at_decision": 132.74,
  "price_date": "2026-11-13",
  "research_note": "research/TW/2026-11-16.md",
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 52.6% -> 50.6% over 12 months [CF-T,IS-T] while operating margin rose to 44.1% and ROIC to 10.5% [IS-T,RA-T]; FCF/NI normalising to 127.0% as net margin rose [CF,IS], not lost share (Q3 growth across credit, wholesale, market data, https://www.sec.gov/Archives/edgar/data/1758730/000175873026000144/tw-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The extended price (20.2% above the 200-day average, RSI 83.0) de-rates if volume growth slows below what the reverse DCF's 19.7% implies.",
    "veto": null
  },
  "triggers": [
    {"text": "Operating margin (TTM) falls below 40%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "FCF margin (TTM) falls below 45%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 45}},
    {"text": "ROIC (TTM) falls below 8%, e.g. after the Trumid acquisition", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Revenue growth turns negative year on year for two consecutive quarters"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 150, "basis": "P/E holds near 31.1x [RA] as operating margin keeps expanding from 44.1% [IS-T]; above the bull fair value of 134.18 because the DCF misses the margin gains."},
    "base": {"probability": 0.5, "target_price_12m": 128, "basis": "Earnings keep growing but P/E drifts toward the peer median 26.1x [RA,P:*]; above the base fair value 92.56 since the FCFE DCF is anchored on a falling FCF margin [CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 105, "basis": "Volume growth slows, the extended price de-rates toward the 5y P/E low of 28.3x [RA] on flat earnings, and Trumid dilutes ROIC (note section 5); still above bear fair value 42.29, which assumes a collapse in growth."}
  },
  "entry_price": 105,
  "entry_basis": "P/E back near its 5y low of 28.3x [RA] on current earnings, about the bear scenario target; the valuation file default (base 92.56 x 0.8) is overly harsh because the FCFE DCF is anchored on the dipping FCF margin.",
  "replaces": null,
  "replacement_reason": null
}
```
