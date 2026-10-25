# Evaluation: International Consolidated Airlines Group S.A. (LON:IAG) — 2026-10-24
## Bear case
The fall has a business cause, not just sentiment: crude resumed rallying and jet-fuel cost fears drove the slide (Invezz headline, 2026-10-08) [Likely]. Q2 profit already dropped 16% on fuel and Middle East disruption (Reuters headline, 2026-07-31) [Certain]. The operating margin of 15.0% is a five-year high, so the 3.3x EV/EBITDA is cheap on peak-cycle EBITDA [Likely]. The macro overlay tilts small toward bear: the broad dollar index rose 2.48 in a month, lifting dollar-linked costs against GBP/EUR revenue, and hedge cover is [data unavailable] [Likely]. The final €500 Mln buyback completes the cash return, so share-count support fades [Guessing]. Piotroski F is only 4 [Certain]. Q3 results on Nov 6, 2026 are an unhedged binary event two weeks away [Certain]. P/B is 2.3x against a peer median of 1.2x [Certain].

## Bull case
Quality has transformed: ROIC 27.5% TTM from -24.6% in FY2021, net debt/EBITDA 0.74x, FCF margin 11.8% [Certain]. The valuation discounts a collapse: EV/EBITDA 3.3x sits below its 5y minimum of 4.4x and below peers at 3.9x, P/FCF is 5.1x against a peer 11.7x, FCF yield 19.59%, and the reverse DCF implies -24.4% year-1 revenue growth [Certain]. Shares fell 8.59% YoY through buybacks [Certain]. No guidance cut, legal action or management change explains the drop; fuel is a cyclical input [Likely]. BA's premium cabin investment and corporate travel diverted from the Middle East support yields (WSJ headline) [Likely]. The stock lags SPY by 9.5pp over 3 months with RSI 32.8, so the overlay judges fuel and dollar pressure largely priced [Likely].

## Decision
```json
{
  "ticker": "LON:IAG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged airline group with 27.5% ROIC and a 19.59% FCF yield trades below its 5y minimum EV/EBITDA, but on near-peak margins exposed to rising dollar-priced fuel ahead of Q3 results.",
  "rationale": "The fall is explained by fuel-cost fears, not a broken business, and the stock is cheap. But margins sit at a cycle high, the usable EV/EBITDA fair value gives only modest upside to base, the macro tilt is toward bear, and Q3 on Nov 6, 2026 will show whether margins held. Good but not compelling: AVOID, re-research after results.",
  "price_at_decision": 394.70,
  "price_date": "2026-10-23",
  "research_note": "research/LON-IAG/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%, giving back most of the recovery to 15.0% and showing fuel costs are not passed through.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.74x TTM now), showing the balance-sheet repair is reversing.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM FCF margin falls below 5%, back toward FY2022-23 levels, undermining the cash-return case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "TTM ROIC falls below 15%, signalling the post-pandemic returns step-up was cyclical.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 492.90, "basis": "Fuel eases and Q3 margins hold near 15.0% [IS], so EV/EBITDA recovers toward its 5y range (min 4.4x [RA]) and the price retests its 6-month high of 492.90 [HI]; the through-cycle DCF bull 6,566.81 is ignored as its bear is negative and unusable."},
    "base": {"probability": 0.45, "target_price_12m": 440.31, "basis": "Margins ease modestly and the multiple stays depressed, so value tracks the EV/EBITDA method's base of 440.31 [IS,RA] rather than the blended 2,087.98, which is distorted by the unusable through-cycle DCF."},
    "bear": {"probability": 0.30, "target_price_12m": 332.70, "basis": "Per the macro overlay (research/LON-IAG/2026-10-24-macro.md, tilt toward bear, small, which raises this probability), rising fuel and a stronger dollar compress margin from its cycle high and the price revisits its 52-week low of 332.70 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades at the EV/EBITDA bear value (395.95) and the blended base fair value is distorted by an unusable through-cycle DCF. The open question is whether margins survived the fuel spike; Q3 results on Nov 6, 2026 decide it, so re-research after them rather than at a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```
