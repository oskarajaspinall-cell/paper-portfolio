# Evaluation: Contemporary Amperex Technology Co., Limited (SHE:300750) — 2026-10-24
## Bear case
The fall is fundamental, not noise: Q3 results on 2026-10-20 showed a sharp profit-growth slowdown that Reuters and SCMP attribute to intensifying EV-battery competition and cooling China auto sales, and the stock fell hard on 2026-10-21 [Likely]. The fact sheet confirms it: TTM gross margin 23.2% vs 25.1% in FY2025, operating margin 16.5% vs 18.0%, and FCF margin roughly halved to 10.3% from 21.4% [Certain]. FCF conversion of 68.1% has already breached the cash-conversion trigger set in the prior note, so the cash-backed-earnings thesis is unsupported today [Certain]. Cheap P/E (12.4x) flatters a peak; on cash, P/FCF 18.5x sits at its 5y median 18.1x [Certain]. Base fair value 230.59 is below the 237.60 close, so the entry price we set no longer carries a margin of safety [Certain]. US pressure on Ford's CATL ties adds customer risk [Likely].
## Bull case
CATL remains the scale and technology leader, with ROIC 54.3% TTM and net cash (net debt/EBITDA -1.99x) [Certain]. Profit still rose in Q3 per the WSJ headline; this is a slowdown, not a decline [Likely]. P/E 12.4x, EV/EBITDA 7.4x and EV/Sales 1.5x are below every 5y low and well below peer medians of 19.3x, 17.3x and 2.4x [Certain]. FCF yield is 5.40% even at depressed TTM cash generation [Certain]. If FCF weakness is working capital or capex timing, conversion recovers toward its FY2025 level of 125.9% [Guessing]. New partnerships such as the Huawei-backed Yinwang battery-swapping deal show demand for its platform [Likely]. Price is 28.1% below the 50-day average with RSI 26.6, and the 2026-10-23 session rebounded 7.8% on 3.2x volume, suggesting capitulation may be near [Guessing].
## Decision
```json
{
  "ticker": "SHE:300750",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A dominant, net-cash battery leader trades below every 5-year multiple low, but Q3 showed competition compressing margins and FCF conversion breaking below 80%, and the price already sits at the mechanical base fair value.",
  "rationale": "The fall reflects a real Q3 profit slowdown from competition, confirmed by lower TTM margins and halved FCF margin; the cash-conversion trigger has fired. Price equals base fair value, so no margin of safety. Quality is still exceptional, so conviction 3, not lower, but below the buy threshold.",
  "price_at_decision": 237.60,
  "price_date": "2026-10-23",
  "research_note": "research/SHE-300750/2026-10-24.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above the FY2024 level of 18.2%, showing the cash-conversion break was timing, not competition (would raise conviction).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 18.2}},
    {"text": "TTM gross margin falls below 19%, under the FY2023 five-year low of 19.1%, confirming a price war is eroding the scale moat.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 19}},
    {"text": "TTM ROIC falls below 40% (54.3% now), showing returns are converging toward commodity battery makers.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Net debt/EBITDA rises above 0x, ending the net-cash balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 312.0, "basis": "Margins stabilise and FCF conversion recovers, so P/E re-rates to its 5y minimum 16.3x [RA] on TTM earnings [IS]; below the 680.55 bull fair value, which assumes growth the Q3 slowdown does not support."},
    "base": {"probability": 0.45, "target_price_12m": 230.0, "basis": "Margins hold near TTM levels (gross 23.2%, operating 16.5% [IS]) with multiples staying below their 5y lows, in line with the 230.59 base fair value [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 175.0, "basis": "Competition cited by Reuters (https://www.reuters.com/business/autos-transportation/chinas-catl-profit-growth-slows-third-quarter-competition-intensifies-2026-10-20/) compresses margins further, matching the EV/EBITDA bear value 174.91 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: margins and FCF conversion are deteriorating after Q3 and the cash-conversion trigger has fired; a lower price would not change the decision until FCF margin and gross margin stabilise in the next reports.",
  "replaces": null,
  "replacement_reason": null
}
```
