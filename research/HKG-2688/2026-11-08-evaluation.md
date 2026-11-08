# Evaluation: ENN Energy Holdings Limited (HKG:2688) — 2026-11-08
## Bear case
Returns are in structural decline, not a dip: ROCE fell from 15.8% to 11.5% and ROE from 23.0% to 13.0% over FY2021-FY2025, net margin from 8.3% to 5.3% [Certain]. The Direction change line (FCF margin falling over five years but rising to 4.3% from 2.4% in the last 12 months) is one year after three weak ones and [Likely] partly working-capital timing, so it does not yet repair the thesis. Regulated pricing caps the gas spread and capex absorbs most earnings [Likely]. The failed ENN Natural Gas take-private removed the bid floor [Certain] and leaves a controlling group with related-party risk [Likely]. Mechanical base fair value of 50.43 sits barely above the 48.72 close, while the bear value of 27.61 is far below [Certain]. China regulatory risk is unverified this run (macro overlay) [Certain]. Piotroski F of 4 is weak [Certain].

## Bull case
The price is below its own 5-year minimum on every multiple: P/E 7.6x vs 8.6x, EV/EBITDA 5.0x vs 6.7x, P/FCF 9.7x vs 14.3x, with a 10.29% FCF yield [Certain]. The reverse DCF implies -1.6% revenue growth, so stagnation is already priced [Certain]. Leverage is moderate (net debt/EBITDA 0.94x site definition) and the share count is not rising [Certain]. TTM FCF conversion of 78.6% and the rolling-year ROCE rebound to 12.6% hint the erosion is bottoming [Likely]. Franchise exclusivity in concession cities is durable [Likely], and the CNY has firmed slightly (macro overlay) [Certain]. If returns stabilise, a re-rating toward the 5y median P/E of 11.7x is plausible [Guessing].

## Decision
```json
{
  "ticker": "HKG:2688",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Chinese city-gas franchise trading below its own 5-year minimum multiples, but with returns eroding for five years and the mechanical base fair value barely above the price, the cheapness looks earned rather than mispriced.",
  "rationale": "Cheap on history, but ROCE, ROE and net margin have fallen for five years, the FCF rebound is only one year old, the buyout floor is gone and base fair value offers little upside against a deep bear case. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 48.72,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2688/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 15%, showing the five-year return erosion has reversed rather than bottomed.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 15}},
    {"text": "TTM FCF margin rises above 5%, above every fiscal year since FY2021, confirming the cash rebound is durable rather than working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 5}},
    {"text": "TTM net margin falls below 4.5%, confirming spread compression is deepening (a further reason to stay away).", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 4.5}},
    {"text": "Net debt/EBITDA (site definition) rises above 1.5x, showing capex is outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 58.64, "basis": "Rolling-year ROCE rebound to 12.6% [RA-T] and FCF margin 4.3% [CF-T] persist and the multiples lift off their below-minimum levels [RA]: the mechanical bull fair value of 58.64 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 50.43, "basis": "Returns stabilise near TTM ROCE 12.6% [RA] with no re-rating while the failed buyout and China discount persist: the mechanical base fair value of 50.43 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 27.61, "basis": "The five-year fall in ROCE and net margin [RA, IS] resumes and the FCF rebound proves working-capital timing (research note section 2): the mechanical bear fair value of 27.61 [fact sheet Fair value]."}
  },
  "entry_price": 40.34,
  "entry_basis": "valuation file: base 50.43 x 0.8; at that level the below-minimum multiples would compensate for the eroding returns.",
  "replaces": null,
  "replacement_reason": null
}
```
