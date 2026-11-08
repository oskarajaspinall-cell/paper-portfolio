# Evaluation: Cathay Pacific Airways Limited (HKG:0293) — 2026-11-08
## Bear case
This is a cyclical airline with earnings near a recovery peak, not a compounder [Likely]. Gross margin has fallen every year from 40.0% (FY2022) to 25.8% TTM and operating margin is down 0.8pp over the last 12 months to 11.3%, so unit economics are fading even as ROIC prints 12.6% [Certain]. The **Direction change** in FCF margin (12.5% to 14.1% over the last year) is driven by cash conversion, with FCF/NI at 137.5% on a heavy, depreciating fleet, not by better operating profit; it does not show the business improving and could reverse when fleet capex rises [Likely]. P/E 7.3x sits 78% up its 5y range and P/B 1.6x is above its 5y max of 1.4x [Certain]. The mechanical base fair value of 76.34 capitalises peak cash flow and is not credible [Likely]. Oil is unmodelled, results are due Nov 12, 2026 and RSI is 72.5 [Certain].
## Bull case
Returns, leverage and capital returns have all moved the right way: ROIC 12.6% and ROCE 12.6% are at their 2-year highs, net debt/EBITDA fell from 11.07x to 2.07x and the share count is down 7.58% year on year [Certain]. FCF yield is 20.16% and P/FCF 5.0x against a peer median of 29.3x; EV/EBITDA of 5.1x is below its own 5y minimum of 5.2x [Certain]. The reverse DCF implies revenue falling 21.7% in year 1, harsher than a normal airline downturn [Likely]. Piotroski F of 7 and a low 0.37 beta point to a healthier balance sheet than the multiple suggests [Likely]. If Hong Kong hub traffic keeps recovering, buybacks plus a modest re-rating could compound per-share value [Guessing].
## Decision
```json
{
  "ticker": "HKG:0293",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged Hong Kong hub airline with recovered returns and a high FCF yield, whose falling gross and operating margins and P/E and P/B near or above their 5-year highs suggest the cycle is already priced near its peak rather than mispriced.",
  "rationale": "Cheap cash-flow multiples are real, but they rest on peak-cycle cash conversion while margins fade over the last 12 months and P/E and P/B sit high in their own ranges. The mechanical fair value is not credible for an airline. Expected value from the scenarios sits near the price: good but not compelling, so AVOID.",
  "price_at_decision": 15.06,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-0293/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin rises above 13.7% (the FY2023 high; 11.3% now), showing margins are re-expanding rather than fading from the peak.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 13.7}},
    {"text": "TTM gross margin rises back above 31.2% (FY2024; 25.8% now), reversing the five-year decline in unit economics.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 31.2}},
    {"text": "TTM ROIC rises above 14% (12.6% now) while net debt/EBITDA stays near 2.07x, evidencing durable rather than cyclical returns.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 14}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 17.5, "basis": "ROIC keeps rising from its 2-year high of 12.6% [RA-T] and buybacks (shares -7.58% YoY [ST]) lift EPS while P/E moves to its 5y max of 7.7x [RA]; well below the mechanical bull of 206.94 because the through-cycle DCF capitalises peak cash conversion of 137.5% [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 15.0, "basis": "Operating margin stays near the flat TTM 11.3% [IS-T] and P/E holds near 7.3x [RA]; consistent with the EV/EBITDA method's base of 15.30 [fact sheet Fair value], not the through-cycle DCF's 106.86, which extrapolates depreciation-flattered FCF."},
    "bear": {"probability": 0.3, "target_price_12m": 10.5, "basis": "Gross margin keeps falling from 25.8% [IS] as yields normalise, earnings drop and P/E reverts toward its 5y min of 5.8x [RA]; near the EV/EBITDA method's bear of 11.12 [fact sheet Fair value], far below the blended bear of 53.51 which we judge not credible for an airline."}
  },
  "entry_price": 13.2,
  "entry_basis": "P/E back at its 5y median of 6.4x [RA] on TTM earnings; the default base fair value 76.34 x 0.8 is above the price and rests on a through-cycle DCF we do not trust for an airline.",
  "replaces": null,
  "replacement_reason": null
}
```
