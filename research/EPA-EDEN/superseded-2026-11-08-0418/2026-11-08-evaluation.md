# Evaluation: Edenred SE (EPA:EDEN) — 2026-11-08
## Bear case
The 2026-10-25 "quality is rising" call was wrong. Over the last 12 months operating margin fell from 34.3% to 29.6% and ROCE from 28.6% to 27.2%, and ROIC sits below its 20.3% 2-year high [Certain] (IS-T, RA-T). The cause is regulation: meal-voucher rule changes in Italy and Brazil, lower Brazilian float income and data/AI spending, with FY2026 EBITDA guided down like-for-like [Likely] (Q3 2026 transcript). That threatens the thesis if it spreads. The Italian antitrust case is unquantified [Likely]. Leverage has risen from 1.13x to 1.65x net debt/EBITDA [Certain] (RA). The 38.2% FCF margin is float-flattered; a year earlier it was 23.6%, so the FCF-based fair value of 38.59 may be overstated [Likely]. The price is 10.9% below its 50-day average after a -14.9% three-month move: the market is still de-rating the stock [Certain] (HI).

## Bull case
The margin reset is guided, explained and regulatory. It is not a surprise loss of share: Q3 reaffirmed FY2026 EBITDA guidance, intrinsic growth was 6.6%, and management targets growth again for 2027–2028 [Likely] (Q3 2026 transcript). Even after the reset, returns are high and stable: TTM ROIC of 18.5% is above every fiscal year except FY2025, and ROCE is 27.2% [Certain] (RA). The price already discounts far worse. P/E is 11.9x against a 5-year median of 32.3x, and EV/EBITDA is 6.8x against 19.6x, both near the bottom of their 5-year ranges and below peers [Certain] (RA). The reverse DCF implies -2.9% revenue growth in year 1 [Certain]. Even if the float-assisted FCF yield of 18.51% normalises, earnings alone support a higher value, and the P/E method's base of 66.65 is above the FCFE base [Certain]. Buybacks (-0.97% shares) and a raised dividend add support [Likely].

## Decision
```json
{
  "ticker": "EPA:EDEN",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A benefits and mobility payments network with stable-high returns (ROIC 18.5%) is going through a guided, regulation-driven margin reset, yet trades near the bottom of its own 5-year P/E and EV/EBITDA ranges, where the price implies a revenue decline that reaffirmed guidance and 6.6% Q3 intrinsic growth do not show.",
  "rationale": "The re-check confirms the earlier evaluation missed falling trailing margins and returns: the quality case is now stable-high rather than rising. Valuation still prices shrinkage, and the decline is explained and guided. Regulatory spread, rising leverage and float-flattered FCF keep conviction at 4, not 5. The standard vol-scaled core size applies, funded by the queued JKHY swap.",
  "price_at_decision": 24.60,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-EDEN/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 26%, extending the guided reset (29.6% now, 34.3% a year earlier) into structural take-rate compression from regulation.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 14%, giving up most of the recovery from 10.0% in FY2023 and signalling the network moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "Management cuts or withdraws the FY2026 EBITDA guidance or the 2027-2028 growth target in a results release, or a further country imposes a meal-voucher fee cap."},
    {"text": "Net debt/EBITDA on the ratios page rises above 2.5x (1.65x TTM now), or ROCE on the ratios page falls below 22%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.00, "basis": "Guided 2027-2028 growth resumes after the rebasing year (Q3 2026 transcript) and P/E re-rates partway from 11.9x toward its 5y median 32.3x [RA]; set below the mechanical bull of 55.24 because FCF margin of 38.2% is float-flattered versus 23.6% a year earlier [CF-T]."},
    "base": {"probability": 0.50, "target_price_12m": 33.00, "basis": "Margins stabilise near the TTM 29.6% [IS-T] with ROIC 18.5% [RA] and EV/EBITDA recovers modestly from 6.8x, a 3% position in its 5y range [RA]; set below the mechanical base of 38.59 because that FCFE value extrapolates float-assisted FCF (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 21.15, "basis": "Italy/Brazil regulation spreads and the operating margin keeps falling from its 34.3% 2-year high [IS-T] while leverage rises toward 2x from 1.65x [RA]: the mechanical bear fair value of 21.15 [fact sheet Fair value]."}
  },
  "replaces": "JKHY",
  "replacement_reason": "JKHY is conviction 3, below the buy bar, and trades above its base fair value. EDEN at conviction 4 has a wider gap to its base fair value, and its earnings multiples sit near 5y lows. This is the queued automatic downgrade swap, confirmed on re-check."
}
```
