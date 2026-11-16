# Evaluation: Zeta Global Holdings Corp. (ZETA) — 2026-11-16
## Bear case
The price already discounts continuation. EV/Sales of 5.4x sits above its 5y max of 4.0x and EV/EBITDA of 60.1x is far above the peer median of 16.3x [Certain]. The mechanical base fair value of 25.99 is well below the 36.65 close [Certain], and the stock is +57.9% above its 200-day average after +93.2% in 12 months [Certain]: an extended price risks a sharp de-rating if growth slows or real yields keep rising (macro overlay: real yield +0.47pp in 3m, tilt toward bear) [Likely]. Quality is thin: ROCE is only 6.8% TTM, ROIC is [data unavailable], and GAAP profit has only just turned positive [Certain]. FCF is flattered by stock compensation of $155.1 million for nine months against operating cash flow of $210.3 million [company-reported], and shares rose 15.82% YoY [Certain]. Gross margin is drifting down to 59.5% [Certain]. A moat is unproven against large marketing suites [Guessing].

## Bull case
The business is clearly working. Operating margin rose from -53.6% to 5.1% TTM and FCF margin from 13.0% to 15.1% over the last year, both at their 2-year highs with no direction change [Certain]. The balance sheet is net cash (net debt/EBITDA -0.49x) [Certain]. The company reported another beat-and-raise quarter with positive GAAP net income [Likely], super-scaled customers rose to 212 from 180 [company-reported], and a possible US tax valuation-allowance release would lift reported earnings [Likely]. Relative strength of +82.8pp versus SPY over 12 months shows the market rewarding the operating turn [Certain]. The EV/Revenue-only fair value is a weak method for a business whose margins are rising, so the gap overstates the downside [Likely].

## Decision
```json
{
  "ticker": "ZETA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Operating margin (0.6% to 5.1%) and FCF margin (13.0% to 15.1%) are rising over the last year [IS-T, CF-T]; ROIC is [data unavailable], ROCE rising to 6.8% [RA-T].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "De-rating of an extended multiple: EV/Sales above its 5y max and price +57.9% above the 200-day average, so any growth slowdown or further real-yield rise compresses the valuation even with fundamentals intact.",
    "veto": null
  },
  "thesis": "A marketing-data platform whose profitability has just turned positive with rising FCF margins and net cash, but whose price sits above its own 5-year EV/Sales range and well above the mechanical fair value, so continuation is fully priced.",
  "rationale": "The operating turn is real, but quality is still low (ROCE 6.8%, ROIC unavailable), dilution is heavy and the price is overextended above its 200-day average with multiples above their own history. The scorecard does not reach the buy bar; good momentum is not a compelling core entry.",
  "price_at_decision": 36.65,
  "price_date": "2026-11-13",
  "research_note": "research/ZETA/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 56%, showing data costs or price competition from large suites eroding the platform's economics.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 56}},
    {"text": "TTM FCF margin falls below 11%, showing the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11}},
    {"text": "Shares change YoY exceeds 20%, i.e. dilution outrunning growth.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 38.80, "basis": "Beat-and-raise continues and the multiple holds, keeping the price around its 52-week high of 38.80 [HI]; above the mechanical bull fair value of 26.49 because EV/Revenue ignores the rising margins."},
    "base": {"probability": 0.45, "target_price_12m": 30.81, "basis": "P/FCF drifts from 36.0x toward its 5y median of 30.0x [RA] while FCF growth offsets part of the de-rating; above the base fair value of 25.99 because EV/Revenue does not credit the 15.1% FCF margin [CF-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 18.98, "basis": "EV/Sales reverts toward its 5y median of 3.7x, the mechanical bear fair value of 18.98 [valuation file]; probability raised slightly per the macro overlay's small toward-bear tilt (real yield +0.47pp in 3m, research/ZETA/2026-11-16-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3, so no entry price is set: the obstacle is low quality (ROCE 6.8%, ROIC unavailable) and heavy dilution as much as price.",
  "replaces": null,
  "replacement_reason": null
}
```
