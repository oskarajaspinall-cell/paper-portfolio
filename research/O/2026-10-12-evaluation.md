# Evaluation: Realty Income Corporation (O) — 2026-10-12
## Bear case
O is a rate instrument with thin economics: ROIC 3.6% and ROE 3.2% TTM, flat for five years [Certain] (RA). The cost of equity is rising: 10y Treasury 5.22% (+0.68pp 3m) and real yield 2.87% (+0.56pp 3m), still climbing with no reversal [Certain] (macro overlay, FRED). Growth needs outside capital. Shares rose 4.53% YoY [Certain] (ST), and each new issue at a lower multiple earns less [Likely]. The mechanical fair value rests on a 5.22% risk-free rate. If yields extend, the fair value itself falls [Likely] (macro overlay). Net debt/EBITDA of 5.74-5.85x is still high leverage for a rate-sensitive model [Certain] (RA, BS). Momentum is broken: -12.3% below the 200-day, -23.9pp vs SPY over 12 months, short interest +8.0% month-on-month [Certain] (ST, HI). Q3 results on Nov 2 may show acquisition spreads narrowing [Guessing].

## Bull case
The de-rating is driven by macro, not by the business. EV/EBITDA of 15.3x and P/E of 39.6x are both below their own 5y minimums (15.8x, 45.8x), and P/B is 1.3x vs a 1.5x peer median [Certain] (RA). The base P/FFO-proxy fair value is 60.82, 12.2% above the 54.18 close [Certain] (fact sheet). The balance sheet has delevered from 8.65x to 5.85x net debt/EBITDA [Certain] (BS, IS). The 136th dividend increase and the €528m KKR JV show capital access is intact and that it can fund growth without issuing equity [Certain] (prnewswire, note). Scale and tenant diversification are a durable moat [Likely] (SEC 10-K). RSI of 31.0 means the stock is oversold. If real yields roll over, the multiple can re-rate quickly [Guessing].

## Decision
```json
{
  "ticker": "O",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A delevering, diversified net-lease REIT trades below its own 5-year multiple range, but its thin 3.6% ROIC, 4.53% annual dilution and first-order exposure to still-rising real yields leave too little margin of safety for a high-conviction buy.",
  "rationale": "The upside to base fair value (+12.2%) is modest, and that value rests on a risk-free rate that is still rising. The primary-weight macro overlay tilts moderately toward bear. Returns on capital are flat and low, and growth needs dilutive equity. This is good but not compelling, so conviction is 3 and the stock is an AVOID. Re-research below the entry price or once yields reverse.",
  "price_at_decision": 54.18,
  "price_date": "2026-10-09",
  "research_note": "research/O/2026-10-12.md",
  "triggers": [
    {"text": "Debt/EBITDA rises above 6.5x, reversing the five-year deleveraging from 8.65x to 5.74x (site definition).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "TTM ROIC falls below 3.0%, back toward the FY2022 five-year low of 2.8%, showing acquisitions are earning below their cost.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 3.0}},
    {"text": "Investment-grade share of annualised base rent in the SEC 10-K falls below 25% from 32.2%, signalling weaker tenant credit."},
    {"text": "Share count growth YoY exceeds 8%, showing external growth is increasingly funded by dilutive equity rather than JV/private capital.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 60.82, "basis": "Real yields roll over and the multiple re-rates to the fact sheet's base P/FFO-proxy fair value of 60.82 [IS,BS,CF,RA,ST]. The probability is cut from a neutral weight because of the macro overlay's moderate bear tilt (research/O/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 55.95, "basis": "EV/EBITDA only recovers to its 5y minimum of 15.8x from 15.3x [RA] on flat TTM EBITDA (54.18 x 15.8/15.3). This sits below the 60.82 base fair value because the macro overlay shows the 5.22% risk-free rate still rising (research/O/2026-10-12-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 50.01, "basis": "Yields and HY spreads keep climbing and P/B compresses to its 5y low of 1.2x from 1.3x [RA] (54.18 x 1.2/1.3). The probability is raised for the macro overlay's moderate bear tilt (research/O/2026-10-12-macro.md)."}
  },
  "entry_price": 48.66,
  "entry_basis": "valuation file: base 60.82 x 0.8 [IS,BS,CF,RA,ST]. At that price the 20% margin of safety would offset the rate risk and low ROIC.",
  "replaces": null,
  "replacement_reason": null
}
```
