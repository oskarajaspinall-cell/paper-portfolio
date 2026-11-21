# Evaluation: T. Rowe Price Group (TROW) — 2026-11-21
## Bear case
The client base is shrinking: Q3 net outflows of $28.3 billion, including target-date outflows, and management expects outflows to stay elevated [company-reported] [Certain]; October added $10.8B more [Certain]. Active equity is losing share to passive, a structural shift no cheap multiple reverses [Likely]. Margins held only because markets lifted average AUM [Certain]; with beta 1.45, VIX at 28.44 and real yields up 0.53 in ~3m (macro overlay), a market fall would hit fees and operating leverage at once [Likely]. The 5-year fall in ROIC, operating and FCF margin from the FY2021 peak shows how far earnings move with markets; the last 12 months' rise (operating margin 31.7% to 34.2%) is market-lifted, not flow-driven, so it can reverse [Likely]. Short interest is 13.01% and rising [Certain]. The price is below its 200-day average: no trend support [Certain].
## Bull case
The price already discounts shrinkage: P/E 10.2x and EV/EBITDA 6.1x sit below their 5-year minimums and well below peers, and the reverse DCF implies -0.7% year-1 revenue growth [Certain]. The business still earns TTM ROIC 21.0% with net cash (net debt/EBITDA -0.96x) [Certain], and the last 12 months improved on every rolling measure: the 5-year decline is the unwinding of a market-driven FY2021 peak, with current levels back in the FY2024-25 range, not a broken model [Likely]. A 7.42% FCF yield funds buybacks (shares -2.44% YoY) and the dividend [Certain]. ETF, SMA and fixed-income demand offset part of the active-equity bleed [Likely]. Base fair value 120.41 sits well above the price [Certain].
## Decision
```json
{
 "ticker": "TROW",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds ROIC, operating margin and FCF margin rising over the last 1 and 3 years (ROIC 19.3% -> 21.0%, operating margin 31.7% -> 34.2%, FCF margin 16.2% -> 20.7% [RA-T, IS-T, CF-T]); the 5-year fall is from the market-driven FY2021 peak.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Persistent active-equity net outflows (Q3 $28.3 billion [company-reported], management expects them to stay elevated) combined with a market fall shrink AUM and fees faster than the price discounts.",
  "veto": null
 },
 "thesis": "A net-cash, 21% ROIC active manager with rising rolling margins trades below its own 5-year minimum P/E and EV/EBITDA, where the price implies slightly shrinking revenue that market-supported fees and buybacks need not deliver.",
 "rationale": "The fall to the entry price tracked the market (relative strength vs SPY roughly flat over 3 months), not a stock-specific break; rolling returns and margins still rise and the business is net cash. Price was the obstacle and it is removed. Conviction 4 from the scorecard; Python sizes it. Cash sits near the floor, so it replaces JKHY. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 100.99,
 "price_date": "2026-11-20",
 "research_note": "research/TROW/2026-11-21.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 30%, showing outflows are now eroding profitability beyond market support.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 30
   }
  },
  {
   "text": "TTM ROIC falls below 15%, under the FY2023 trough of 16.5%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "TTM FCF margin falls below 16%, back under the level of a year earlier.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 16
   }
  },
  {
   "text": "Quarterly net outflows worse than $40 billion, or quarter-end AUM below $1,700 billion, in the company's AUM releases."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.2,
   "target_price_12m": 148.14,
   "basis": "Outflows stabilise and the P/E re-rates to the P/E method's bull value 148.14, below the blended bull 164.73 since flows cap the multiple (fact sheet fair value, note section 3)."
  },
  "base": {
   "probability": 0.45,
   "target_price_12m": 120.41,
   "basis": "Margins hold near 34.2% TTM [IS-T] and the price moves to the mechanical base fair value 120.41 as the below-minimum P/E normalises; probability trimmed toward bear for the macro overlay's small bear tilt (beta 1.45, VIX 28.44)."
  },
  "bear": {
   "probability": 0.35,
   "target_price_12m": 89.48,
   "basis": "A market fall plus elevated outflows push AUM toward $1,700bn and compress margin (macro overlay bear), price to the bear fair value 89.48; probability raised for the overlay's small bear tilt."
  }
 },
 "replaces": "JKHY",
 "replacement_reason": "Cash is close to the 1.5% floor, so the buy needs funding. JKHY sits below the buy bar at conviction 3 and its latest thesis says its price already implies growth above the company's framework; TROW is at conviction 4, net cash, below its own 5-year minimum multiples, with more upside to base fair value.",
 "second_opinion": {
  "file": "research/TROW/2026-11-21-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": 100.0,
 "entry_basis": "Second opinion at conviction 3: Price is the obstacle: per the valuation file, the scorecard's value blend (base fair value 120.41 with the scenario expected value) reaches the next upside band just below the current close, taking the total to the buy line; base 120.41 x 0.85 sits above the price, so the scorecard re-score level is used instead."
}
```
