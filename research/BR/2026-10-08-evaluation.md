# Evaluation: Broadridge Financial Solutions, Inc. (BR) — 2026-10-08
## Bear case
The shares fell 32.4% in 12 months and lag SPY by 48.1pp, and the research never says why [Certain]. A de-rating this large in a utility-like franchise usually reflects something in the price that the trailing ratios do not show yet, such as slowing proxy/position growth or AI and tokenization pressure on GTO pricing [Guessing]. On free cash flow, BR is not cheap: P/FCF of 14.1x is 12% above the peer median, and P/B is 66% above it [Certain]. The P/E sits at the 13th percentile of its 5-year range, not below the floor (14.1x), so a fall to that floor is still ordinary downside [Certain]. The net-margin jump to 15.0% from 12.2% may include non-recurring items [Guessing]. Client concentration is a disclosed risk [Certain]. Earnings on Nov 3 could confirm the market's worry [Likely].
## Bull case
Every quality metric has improved for five years [Certain]: ROIC went from 10.6% to 17.5%, operating margin from 13.3% to 17.4% and FCF margin from 7.3% to 17.1%, while net debt/EBITDA fell from 3.14x to 1.72x. FCF conversion of 113.7% shows high earnings quality [Certain]. The P/E of 16.7x is 23% below peers and EV/EBITDA of 11.7x is 13% below them, with a 7.07% FCF yield and a 1.01% shrink in share count [Certain]. ICS is a regulation-anchored proxy utility with high switching costs [Certain]. Tokenized repo (DLR) and DLX are optional extra growth that the price ignores [Likely]. Low short interest (2.61%, down 11.9%) and a Piotroski score of 7 show no sign of distress [Certain]. If fundamentals simply hold, a re-rating toward peer multiples is plausible [Likely].
## Decision
```json
{
  "ticker": "BR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, deleveraging proxy and trade-processing franchise trades near the bottom of its 5-year multiple range, but the cause of its 32.4% de-rating is unexplained and it is not cheap versus peers on free cash flow.",
  "rationale": "Quality is clear but the valuation is only good, not compelling. Multiples sit above their 5-year floors, P/FCF is above the peer median, and the research does not explain the de-rating or show the growth trend. That is conviction 3, below the buy threshold. With Technology already filling from pending INTU and GDDY orders, cash is the better outcome.",
  "price_at_decision": 160.13,
  "price_date": "2026-10-07",
  "research_note": "research/BR/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 14%, back to the FY2023 level, showing the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM gross margin falls below 29%, under the FY2023 level of 29.5%, signalling pricing pressure in ICS or GTO.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 29}},
    {"text": "TTM FCF margin falls below the FY2024 level of 15.4%, showing the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15.4}},
    {"text": "The Nov 3, 2026 results or the 10-Q show the source of the de-rating is cyclical rather than structural, with recurring revenue still growing and margins intact: this would raise conviction toward a BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 209.0, "basis": "With fundamentals intact, P/E re-rates from 16.7x to the 21.8x peer median [RA, P:FIS/SSNC/JKHY/ADP] on unchanged TTM earnings [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 170.0, "basis": "Multiples stay depressed while the 7.07% FCF yield [ST] and 1.01% buyback [ST] give a modest recovery toward the 200-day average of 169.76 [HI]."},
    "bear": {"probability": 0.25, "target_price_12m": 135.0, "basis": "The unexplained 32.4% de-rating [ST] continues and P/E falls to its 5-year minimum of 14.1x [RA], near the 52-week low of 133.83 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
