# Evaluation: Deutsche Telekom AG (ETR:DTE) — 2026-11-08
## Bear case
The cheapness is mostly an artefact of how cash flow is measured. FCF runs at 327.4% of net income and the 23.64% FCF yield almost certainly leaves out lease and spectrum outflows [Guessing]. That makes the DCF base of 162.14 and the blended 120.67 fair value unusable [Likely]. On earnings, the stock is not cheap: P/E 13.9x is above its 5y median of 12.6x and above peers, and P/B 1.4x sits at the top of its range [Certain]. The last 12 months are flat, not improving: ROIC -0.2pp and FCF margin -0.8pp, with net margin down from 15.9% to 7.3% [Certain]. So the 5-year rise has stalled [Certain]. The value depends on T-Mobile US, where SpaceX mobile entry is a new competitive threat the market is pricing [Likely]. Leverage of 3.13x net debt/EBITDA and Altman Z of 1.13 leave little room for error [Certain].
## Bull case
EV/EBITDA of 5.9x is below its 5y minimum of 7.1x and below the peer median of 7.1x [Certain]. Q3 raised 2026 guidance for the third time this year, management proposed a higher dividend and up to EUR 2 billion of 2027 buybacks, and German broadband adds were positive [Likely]. Over five years, returns and margins rose structurally: ROIC from 5.0% to 8.8%, operating margin from 12.6% to 22.2% [Certain]. Leverage has fallen from 3.98x to 3.13x and the share count is down 1.34% [Certain]. The flat last year looks like a plateau, not decay [Likely]. The macro overlay's only channel, a firmer USD, slightly helps translated earnings (research/ETR-DTE/2026-11-08-macro.md) [Likely]. With beta of 0.34, this is a defensive compounder that the SpaceX headlines have de-rated [Likely].
## Decision
```json
{
  "ticker": "ETR:DTE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging, guidance-raising integrated telecom trades below its own 5-year EV/EBITDA minimum, but its earnings multiples are at or above their history and peers, and its apparent cash-flow cheapness rests on an FCF measure that likely overstates distributable cash.",
  "rationale": "The cheapness shows on EV/EBITDA and FCF, and the FCF figure looks overstated. On P/E and P/B the stock is at or above its own history and peers. The last year is flat and the US SpaceX threat is unresolved. Good but not compelling: AVOID at conviction 3. It becomes a BUY only nearer the 6-month low.",
  "price_at_decision": 25.91,
  "price_date": "2026-11-06",
  "research_note": "research/ETR-DTE/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20% (22.2% now), reversing the post-2023 step-up and showing competition or input inflation is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 7.5% (8.8% now), showing the returns improvement has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7.5}},
    {"text": "Net debt/EBITDA rises above 3.8x (3.13x TTM now), meaning buybacks and spectrum spending are outrunning deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.8}},
    {"text": "TTM FCF margin falls below 20% (24.0% now), showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.36, "basis": "Third guidance raise and the 2027 buyback (Reuters Q3 headline in the fact sheet) re-rate EV/EBITDA from 5.9x toward its 5y minimum of 7.1x [RA], returning to the 52-week high of 34.36 [HI]; below the EV/EBITDA method's 36.17 and far below the DCF, which extrapolates overstated FCF (FCF/NI 327.4% [CF,IS])."},
    "base": {"probability": 0.5, "target_price_12m": 28.0, "basis": "Returns stay flat as the rolling table shows (ROIC 8.8%, operating margin 22.2% [RA-T,IS-T]) and P/E holds near 13.9x [RA] while buybacks and raised guidance add modest earnings growth; well below the mechanical base of 120.67 because that DCF rests on FCF that likely omits lease and spectrum outflows (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 23.53, "basis": "SpaceX mobile entry pressures T-Mobile US (Reuters 2026-11-05 in the fact sheet) and P/E de-rates toward its 5y median of 12.6x [RA], back to the 6-month low of 23.53 [HI]; above the mechanical bear of 72.82, which inherits the same FCF overstatement."}
  },
  "entry_price": 23.53,
  "entry_basis": "Base fair value x 0.8 sits far above the price because the FCF-driven DCF is distorted, so it can't anchor an entry. Use P/E back at about its 5y median of 12.6x [RA], which matches the 6-month low of 23.53 [HI]. That gives a margin of safety on earnings, not on suspect FCF.",
  "replaces": null,
  "replacement_reason": null
}
```
