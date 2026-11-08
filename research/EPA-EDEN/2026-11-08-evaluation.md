# Evaluation: Edenred SE (EPA:EDEN) — 2026-11-08
## Bear case
Regulation is cutting into the business itself. Operating margin fell from 34.3% to 29.6% over the last 12 months and ROCE from 28.6% to 27.2%, 4.6pp below its 2-year high. Management blames meal-voucher rules in Italy and Brazil [Likely], and the Brazil decree (fee cap, interoperability) is still "not a lot of detail" [Likely]. If interoperability opens the closed network, take rates could keep falling and the reset becomes permanent [Guessing]. On macro, the overlay finds the real about 3% weaker against the euro over 1m and the Selic down 0.45pp over 3m (13.94%), which hits both translation and float income [Certain]. The post-election real fall and Selic hold in the request are not in the overlay's official data [Certain]. FCF margin of 38.2% against 23.6% a year earlier is float-driven, leverage is up from 1.13x to 1.65x, and the bear value of 21.15 sits below the price [Certain].

## Bull case
The price already discounts the bear case. P/E is 11.9x against a 5y median of 32.3x, P/FCF is 5.4x and the FCF yield is 18.51% [Certain]. The reverse DCF implies revenue shrinking 2.9% in year 1, yet Q3 intrinsic growth was 6.6%, FY2026 EBITDA guidance was reaffirmed and 8%–12% growth is targeted for 2027–2028 [Likely]. The margin and ROCE declines are a guided, regulation-driven rebasing, not competitive loss: ROCE at 27.2% is still well above FY2021–23 levels and ROIC is flat at 18.5% [Certain]. Mobility is growing double digits, diversifying away from vouchers [Likely]. Net debt/EBITDA of 1.65x leaves no balance-sheet stress, the dividend rose 10% and the share count is falling [Certain]. The overlay judges Brazil risk mostly priced; base fair value is 38.59 [Likely].

## Decision
```json
{
  "ticker": "EPA:EDEN",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A benefits and mobility payments network with high returns (ROIC 18.5%) is going through a guided, regulation-driven margin reset, yet trades near the bottom of its own 5-year multiple ranges, where the price implies a revenue decline that reaffirmed guidance and 6.6% Q3 intrinsic growth do not show.",
  "rationale": "The fall in margin and ROCE comes from guided regulation, not lost competitiveness, and returns stay high. The price implies shrinkage. Brazil (the decree, the real, the Selic) and Italy are unresolved and move bear odds up a little, so conviction stays 4, not 5. Standard vol-scaled core size, funded by replacing conviction-3 JKHY.",
  "price_at_decision": 24.60,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-EDEN/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 26% (29.6% now, 34.3% a year earlier), turning the guided reset into structural take-rate compression from regulation.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 14%, giving up most of the recovery from 10.0% in FY2023 and signalling the network moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.65x TTM now), showing leverage is building rather than seasonal working capital.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Management cuts or withdraws FY2026 EBITDA guidance or the 2027-2028 growth target, the Brazil decree's implementing rules impose full interoperability, a further country imposes a meal-voucher fee cap, or ROCE on the ratios page falls below 22%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Guided 2027-2028 growth of 8%-12% resumes (Q3 2026 transcript) and P/E re-rates partway from 11.9x toward its 5y median 32.3x [RA]; below the mechanical bull of 55.24 because the 38.2% FCF margin is float-flattered against 23.6% a year earlier [CF-T]."},
    "base": {"probability": 0.45, "target_price_12m": 33.0, "basis": "Operating margin stabilises near the TTM 29.6% [IS-T] with ROIC 18.5% [RA] and EV/EBITDA recovers modestly from 6.8x, a 3% position in its 5y range [RA]; below the mechanical base of 38.59 because that FCFE value extrapolates float-assisted FCF, and probability cut from an even split by the macro overlay's small bear tilt (research/EPA-EDEN/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 21.15, "basis": "The Brazil decree and Italy rules deepen the margin fall from its 34.3% 2-year high [IS-T] while the real weakens and Selic cuts cut float income: the mechanical bear fair value of 21.15 [fact sheet Fair value]; probability raised for the overlay's small toward-bear tilt on Brazil (research/EPA-EDEN/2026-11-08-macro.md)."}
  },
  "replaces": "JKHY",
  "replacement_reason": "JKHY is conviction 3, below the buy bar, with its price above its base fair value; EDEN is conviction 4 with the price well below its base fair value and an expected value above the price, and the order is funded by that sale under the cash reserve."
}
```
