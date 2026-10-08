# Evaluation: Incyte Corporation (INCY) — 2026-10-07
## Bear case
The low multiple is mostly a patent-cliff discount, not a mispricing. Jakafi/Jakavi patents expire around late-2028 and the 10-K names single-franchise dependence as a principal risk [Certain]. A 14.4x P/E and 12.1x P/FCF on peak-franchise earnings are not cheap if those earnings step down within roughly two years [Likely]. The pipeline's guided 15–20% CAGR applies post-2029, so there is a gap before it arrives [Likely]. The fact sheet gives no Jakafi revenue split, so we cannot size the gap [Certain]. FY2024 shows how fragile reported returns are: operating margin fell to 2.0% and ROIC to 0.6% [Certain]. Shares rose 3.08% YoY, so deal funding dilutes holders, and short interest rose 6.6% month on month [Certain]. Momentum is weak: the stock sits 8.4% below its 50-day average going into the Oct 27 results [Certain].
## Bull case
The quality is clear today. TTM operating margin is 31.7%, FCF margin 33.0%, ROIC 86.5% and FCF conversion 119%, with net cash at -2.3x EBITDA [Certain]. EV/EBITDA (9.6x), P/E (14.4x) and P/FCF (12.1x) all sit below their own 5-year minimums and 16–28% below peers, with an 8.4% FCF yield [Certain]. Diversification is visible. Atebrioz was approved, Niktimvo was approved in Brazil and the Opzelura partnership was expanded, all since September [Certain]. Five late-stage programs are guided to support growth after 2029 [Likely]. If Opzelura and Niktimvo grow fast enough to offset part of the Jakafi cliff, the multiple could re-rate to its 5-year floor or better [Guessing]. The cash pile funds bolt-on deals without leverage [Likely]. Beta is 0.74 and the macro overlay rates macro as context only [Certain].
## Decision
```json
{
  "ticker": "INCY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 33%-FCF-margin franchise trades below its own 5-year minimum multiples, but the discount mainly reflects a late-2028 Jakafi patent cliff whose size the available data cannot measure.",
  "rationale": "The stock is cheap on trailing cash flow, but trailing cash flow is peak-Jakafi cash flow. The data gives no Jakafi revenue split, and the pipeline payoff is post-2029. The cliff could justify the discount. With share dilution and weak momentum into earnings, this is good but not compelling: conviction 3, so AVOID under the owner rule.",
  "price_at_decision": 112.73,
  "price_date": "2026-10-06",
  "research_note": "research/INCY/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2025 level of 26.2%, showing that pipeline launches and deal spending are eroding the profit base ahead of the Jakafi cliff.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26.2}},
    {"text": "TTM FCF margin falls below the FY2025 level of 26.3%, meaning the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 26.3}},
    {"text": "Non-Jakafi products (Opzelura, Niktimvo, Atebrioz and others) fail to rise as a share of total product revenue over the next four quarters, as disclosed in 10-Q/10-K filings.", "check": null},
    {"text": "Shares outstanding keep growing faster than the current 3.08% YoY, showing that deal funding is diluting holders further.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3.08}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 133.0, "basis": "Diversification evidence (the Atebrioz approval and Opzelura expansion in the news feed [OV]) re-rates P/FCF from 12.1x to its 5y minimum of 14.3x [RA] on TTM FCF [CF], close to the 52-week high of 132.60 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 118.0, "basis": "The market keeps discounting the late-2028 Jakafi cliff (10-K, note section 2), so P/E only edges back to its 5y minimum of 15.1x from 14.4x [RA] on flat TTM earnings [IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 95.0, "basis": "Cliff fears grow and dilution continues (shares +3.08% YoY [ST]), so EV/Sales falls from 3.2x to its 5y minimum of 2.7x [RA], near the 6-month low of 92.18 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
