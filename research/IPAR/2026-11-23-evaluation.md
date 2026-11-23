# Evaluation: Interparfums, Inc. (IPAR) — 2026-11-23
## Bear case
The price has run ahead of the business. The stock is +69.9% over 12 months and 28.0% above its 200-day average, RSI 68.5, while Q3 sales were only stable and nine-month sales rose 1% [Certain]. The reverse DCF needs 9.6% year-1 revenue growth against roughly flat sales, so the multiple already prices re-acceleration; if FY2027 growth disappoints, an extended price de-rates [Likely]. Returns are slipping: ROIC 18.3% TTM vs 19.6% a year earlier and 23.5% at the FY2024 high, operating margin 17.9% vs 19.3% [Certain]. The moat is contractual: licences belong to brand owners and can be lost at renewal [Likely]. P/B 5.0x sits at 94% of its 5y range and the price is above base fair value of 129.69 [Certain]. The euro's fall against the dollar is a translation drag on European-based sales (macro overlay) [Likely]. Short interest is 10.72% of float [Certain].
## Bull case
A high-return, net-cash licensed fragrance house: ROIC 18.3%, gross margin 59.8%, net debt/EBITDA -0.10x, Altman Z 6.87 [Certain]. Cash conversion has transformed: FCF margin 16.2% TTM and still rising over the last year (12.4% a year earlier), FCF 143.1% of net income, so P/FCF 18.1x sits at only 6% of its 5y range and the FCF yield is 5.52% [Certain]. P/E 25.8x and EV/EBITDA 15.0x are near their 5y medians, not stretched [Certain]. The margin dip is explained by US gift-set delays and flat sales, not lost share; the Puma licence and new FY2027 guidance show the pipeline is fed [Likely]. Insiders own 43.61%, aligning management [Certain]. The trend is strong: relative strength vs SPY is +65.8pp over 12 months [Certain].
## Decision
```json
{
  "ticker": "IPAR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin eased on flat sales the Q3 call attributes to US gift-set delays and regional headwinds, with net cash intact and FCF margin rising (https://stockanalysis.com/stocks/ipar/transcripts/725208-q3-2026/ [RA-T, IS-T]).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "An extended price (28.0% above the 200-day) already implies 9.6% year-1 growth vs flat sales; a growth miss or a lost licence renewal would de-rate it.",
    "veto": null
  },
  "thesis": "A high-return, net-cash licensed fragrance house with transformed cash conversion, but the price already discounts a sales re-acceleration not yet visible.",
  "rationale": "Quality and balance sheet are strong and FCF is improving, but returns and operating margin are slipping on flat sales while the price sits above base fair value after a sharp run. Good but not compelling at this price; the scorecard sets the conviction.",
  "price_at_decision": 137.42,
  "price_date": "2026-11-20",
  "research_note": "research/IPAR/2026-11-23.md",
  "triggers": [
    {"text": "Gross margin (TTM) falls below 56%: pricing power in the licence portfolio is eroding.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 56}},
    {"text": "ROIC (TTM) falls below 15%: the return decline becomes structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "FCF margin (TTM) falls below 10%: the cash-conversion improvement reverses.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Operating margin (TTM) falls below 15%, or a major licence is not renewed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 162.49, "basis": "FY2027 guidance delivers re-acceleration and the mechanical bull fair value of 162.49 is reached (fact sheet fair value, IS,BS,CF,RA)."},
    "base": {"probability": 0.5, "target_price_12m": 129.69, "basis": "Flat-to-modest sales growth leaves the price near the mechanical base fair value of 129.69, with P/E near its 5y median 25.6x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 85.75, "basis": "Growth misses the 9.6% the reverse DCF implies and the extended price de-rates to the P/E-method bear value of 85.75; the DCF bear of 16.44 is ignored as unreliable (fact sheet fair value)."}
  },
  "entry_price": 110.24,
  "entry_basis": "valuation file: base 129.69 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```
