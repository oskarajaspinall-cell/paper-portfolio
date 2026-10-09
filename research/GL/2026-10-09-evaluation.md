# Evaluation: Globe Life Inc. (GL) — 2026-10-09
## Bear case
The stock is not cheap against its own history: P/E 11.0x and EV/EBITDA 9.5x sit mid-range (52nd/43rd percentile), EV/Sales is at the 90th percentile, and P/FCF of 10.4x is above its 5-year maximum of 8.9x [Certain]. The peer discount is the only "cheapness", and GL has carried one historically [Likely]. Cash quality is eroding: FCF/NI fell from 155.9% to 101.7% and net debt/EBITDA rose from 1.40x to 1.89x while buybacks continued [Certain]. Another few quarters of that trend means buybacks are increasingly debt-funded [Likely]. A law-firm solicitation and a 15% rise in short interest point to an unresolved governance overhang, which can re-rate an agency-model insurer quickly [Guessing]. Q3 results on Oct 21 are a near-term binary [Certain]. The P/E method gives only 144.58 base, below the price [Certain].
## Bull case
GL is a high-return franchise: ROE rose from 11.8% to 20.9% and ROIC from 10.3% to 14.1% over five years [Certain]. The exclusive career-agency model is hard to replicate [Likely]. It trades at a 29% P/E discount to peers despite superior ROE [Certain], and shrinks its share count 5.42% a year, backed by a new $2.5bn authorisation [Certain]. FCF still exceeds net income (101.7%), with a 9.66% FCF yield [Certain]. Higher real yields lift reinvestment income on long-duration reserves (macro overlay) [Likely], and beta of 0.44 limits drawdowns [Certain]. The P/B+ROE base fair value of 190.29 implies +14.6% upside [Certain].
## Decision
```json
{
  "ticker": "GL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROE life insurer with steady buybacks trades at a peer discount but mid-range against its own history, with falling cash conversion, rising leverage and an unresolved governance overhang capping the upside case.",
  "rationale": "Good but not compelling. Own-history multiples are mid-range, P/FCF is above its 5y max, cash conversion is falling and leverage is rising. The blended fair value upside (+14.6%) rests on the P/B+ROE method, while P/E gives 144.58. With Q3 results due Oct 21 and a governance watch item, conviction is 3. Cash is preferable.",
  "price_at_decision": 166.08,
  "price_date": "2026-10-08",
  "research_note": "research/GL/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 15%, giving up most of the five-year rise from 11.8% to 20.9% [RA].", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "Shares outstanding stop shrinking (YoY change turns positive vs -5.42% now), showing buybacks have been curtailed.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "FCF/NI conversion (cash-flow and income-statement pages) falls below 90% TTM, from 101.7%, meaning capital returns are no longer cash-funded."},
    {"text": "Net debt/EBITDA (site definition, ratios page) rises above 2.5x, from 1.89x TTM."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 211.47, "basis": "ROE holds near 20.9% [RA] and buybacks continue (-5.42% shares [ST]), so the price reaches the fact sheet's bull fair value of 211.47; macro overlay tilt is neutral/small, so no probability change."},
    "base": {"probability": 0.5, "target_price_12m": 177.95, "basis": "Earnings keep growing but cash conversion keeps sliding (101.7% FCF/NI [CF,IS]), so value tracks the P/E method's bull 177.95 rather than the P/B+ROE-led 190.29 blend, as P/FCF already exceeds its 5y max [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 131.84, "basis": "The governance overhang or a weak Q3 (Oct 21 [ST]) de-rates P/E toward its 5y median 9.6x [RA], matching the P/E bear of 131.84; above the 117.33 blended bear because ROE at 20.9% [RA] does not justify the P/B bear's collapse."}
  },
  "entry_price": 152.23,
  "entry_basis": "valuation file: base 190.29 x 0.8; at that level the P/E discount and mid-range own-history multiples would offer enough margin of safety for the cash-conversion and governance risks.",
  "replaces": null,
  "replacement_reason": null
}
```
