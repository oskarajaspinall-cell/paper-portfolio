# Evaluation: Simon Property Group, Inc. (SPG) — 2026-10-11
## Bear case
SPG is not cheap on the metrics that matter for a REIT. EV/EBITDA of 20.3x sits at the 76th percentile of its 5y range and 18% above peers; EV/Sales is at the 85th percentile and 40% above peers [Certain] [RA]. The 14.1x P/E "discount" is a depreciation artefact [Certain]. Leverage of 5.54x net debt/EBITDA and beta 1.33 make the stock a discount-rate instrument [Certain] [ST, RA]: the 10y real yield is up 0.56pp in 3 months and HY spreads widened, so cap rates and refinancing costs are moving against it [Certain] (macro overlay, FRED). The $800m September note issue will reprice at higher coupons [Likely]. Piotroski 4/9 and rising short interest (+13% m/m) add caution [Certain] [ST]. The stock is below its 50- and 200-day averages and has lagged SPY by 12.8pp over 3 months [Certain] [HI]; nothing yet says the rate pressure is over [Likely].
## Bull case
The franchise is improving: ROIC has risen from 7.4% to 9.3% and net debt/EBITDA (site definition) fell from 6.85x to 5.54x since FY2021 [Certain] [RA]. Q2 2026 brought robust NOI and FFO growth, record retailer sales and a raised 2026 FFO guide [Likely] (Q2 release headline). Class-A malls and outlets are scarce, irreplaceable real estate with tenant pricing power [Likely]. The owner's P/FFO-proxy fair value puts base at $258.08 (+29.4%) and bear at $194.92, only 2.3% below the $199.42 close [Certain] (fact sheet Fair value). A 4.25% FCF yield funds distributions and buybacks [Certain] [ST]. The sell-off is a rate move, not an earnings shock; if real yields reverse, the multiple can re-rate quickly [Likely] (macro overlay).
## Decision
```json
{
  "ticker": "SPG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A de-levering, improving Class-A mall REIT whose P/FFO fair value shows upside, but whose EV/EBITDA is rich against its own history and peers while rising real yields push its cap rate and refinancing cost the wrong way.",
  "rationale": "Fundamentals are improving and the P/FFO model shows upside. But EV/EBITDA and EV/Sales sit high in their 5y ranges and above peers, and the primary-weight macro overlay tilts toward bear: rising real yields hit a 5.5x-levered REIT directly. That is good but not compelling, so conviction 3 means AVOID until the price or the rate backdrop improves.",
  "price_at_decision": 199.42,
  "price_date": "2026-10-09",
  "research_note": "research/SPG/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, reversing the five-year rise from 7.4% to 9.3% [RA].", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA rises above 6.5x, undoing the de-leveraging from 6.85x to 5.54x [RA].", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "Management cuts full-year 2026 real-estate FFO per share guidance on the Q3 2026 release (Nov 5, 2026) or later, contradicting the Q2 raise."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 258.08, "basis": "Real yields reverse and FFO growth from the raised 2026 guide re-rates the stock to the P/FFO-proxy base fair value of 258.08 (fact sheet Fair value; Q2 release headline [OV])."},
    "base": {"probability": 0.45, "target_price_12m": 204.24, "basis": "FFO growth is offset by EV/EBITDA (20.3x) drifting toward its 5y median of 18.2x [RA], leaving the price near its 200-day average of 204.24 [ST], slightly above the 194.92 bear fair value."},
    "bear": {"probability": 0.30, "target_price_12m": 172.19, "basis": "Per the macro overlay (research/SPG/2026-10-11-macro.md, primary weight, moderate tilt toward bear), real yields and HY spreads keep rising, and with 5.54x leverage EV/EBITDA falls to its 5y median of 18.2x [RA]. That takes the price back to the 52-week low of 172.19 [HI], below the 194.92 bear fair value, which the P/FFO proxy cannot see. The tilt moved about 10pp of probability from base and bull to bear."}
  },
  "entry_price": 172.19,
  "entry_basis": "The default anchor (base 258.08 x 0.8 = 206.46) is above the current price, so the obstacle is the rich EV/EBITDA and the rate backdrop, not the P/FFO model. At the 52-week low of 172.19 [HI], EV/EBITDA would be back near its 5y median of 18.2x [RA], so the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
