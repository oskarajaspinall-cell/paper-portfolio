# Evaluation: Bank of Suzhou Co., Ltd. (SHE:002966) — 2026-11-16
## Bear case
Returns are sub-par and drifting: ROE 9.2% TTM against 11.0% in FY2022, below the 10% a quality franchise needs [Certain] [RA]. Net margin rose to 48.7% [IS] but ROE did not follow, so there is no visible operating edge [Likely]. The price already discounts this: P/E 8.0x sits above its 5y maximum of 7.4x and above the 6.8x peer median [Certain] [RA]. The gains are trend, not value: the stock trades +13.7% above its 200-day average [HI]; if Chinese bank earnings stall, an extended multiple de-rates toward its 7.3x median [Likely]. The Direction change line (FCF margin 128.4% to 54.9%) is deposit-flow noise, not an operating signal [Likely], but it means the FCFE leg (15.43) inflating the blended fair value is unreliable; the returns-anchored P/B+ROE base of 9.31 is below the price [Certain]. Beta 0.08 hides PBoC-policy and credit risk [Likely].
## Bull case
A wealthy-region Jiangsu lender trading at 0.7x book, below the 0.8x peer median [Certain] [ST]. Net margin has risen every year to 48.7% [Certain] [IS], and the share count fell 6.07% YoY [Certain] [ST], though whether that is a buyback is unconfirmed [Guessing]. The trend is working: 12-month change +13.6%, 50-day above the 200-day by 9.7%, and +17.1pp relative strength vs SPY over 3 months [Certain] [HI]. The reverse DCF implies -6.1% revenue growth, which flat ROE does not show [Likely]. Macro overlay weight is `context`, so no tilt [Certain].
## Decision
```json
{
  "ticker": "SHE:002966",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "new_evidence": {"type": "method_change", "text": "The 2026-10-19 AVOID at conviction 3 predates the 2026-11-09 scorecard; Python now sets conviction 2 on the same quality picture (ROE below the bar, no real discount)."},
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The falling FCF margin (128.4% to 54.9% TTM [CF-T]) reflects bank deposit and loan flows, not operations; net margin kept rising to 48.7% [IS] and ROE moved only from 9.4% (FY2025) to 9.2% TTM [RA].",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Chinese bank margin and credit pressure flattens earnings while P/E sits above its 5y maximum, so the stock de-rates toward its own median.",
    "veto": null
  },
  "thesis": "A steady but sub-10%-ROE regional Chinese bank whose uptrend has pushed P/E above its own 5-year range, leaving average quality without a discount.",
  "rationale": "ROE of 9.2% fails the quality bar and the returns-anchored P/B+ROE value sits below the price; the blended fair value leans on an unreliable FCFE leg. Good trend, average business: not high conviction, so AVOID.",
  "price_at_decision": 9.63,
  "price_date": "2026-11-13",
  "research_note": "research/SHE-002966/2026-11-16.md",
  "triggers": [
    {"text": "ROE (TTM) recovers above 11.0%, the FY2022 level, showing returns are improving rather than drifting.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 11}},
    {"text": "ROE (TTM) falls below 8.0%, showing credit costs or margin compression are breaking the earnings base.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "Net margin (TTM) falls below 44.0%, reversing the five-year rise.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 44}},
    {"text": "Shares outstanding change YoY turns positive by more than 5% (dilutive recapitalisation).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 11.35, "basis": "P/B moves from 0.7x toward the 0.8x peer median [ST] as ROE holds, reaching the blended base fair value of 11.35 (valuation file)."},
    "base": {"probability": 0.5, "target_price_12m": 9.63, "basis": "ROE flat near 9.2% [RA]; P/B stays near 0.7x while P/E above its 5y max of 7.4x [RA] caps re-rating, so the price holds near today's 9.63 (P/B+ROE base 9.31 just below)."},
    "bear": {"probability": 0.25, "target_price_12m": 8.31, "basis": "Bank earnings stall and the extended P/E de-rates toward its 7.3x median [RA], in line with the P/B+ROE bear value of 8.31 (fact sheet fair value)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE of 9.2% [RA] is below the quality bar and there is no moat, so a lower price alone would not lift the same evidence to conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
