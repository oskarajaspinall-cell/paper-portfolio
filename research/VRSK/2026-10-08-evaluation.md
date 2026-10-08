# Evaluation: Verisk Analytics, Inc. (VRSK) — 2026-10-08
## Bear case
The de-rating has an unexplained cause. The stock is down 31.2% over 12 months and lags SPY by 46.9pp (ST,HI) [Certain], yet reported margins keep rising. That points to the market pricing a forward risk the numbers do not yet show: AI disruption of data moats, or fallout from the AccuLynx ruling Verisk "strongly disagrees" with, whose size is unknown [Guessing]. On an FCF basis it is not cheap against peers. P/FCF of 17.8x is in line with the peer median of 18.0x, and EV/EBITDA (+22%) and EV/Sales (+34%) still carry premiums (RA) [Certain]. The 5.63% FCF yield (ST) barely clears a 5.27% 10y Treasury, while real yields are rising (macro overlay) [Certain]. Net debt/EBITDA jumped to 2.68x from 1.83x (RA) [Certain]. Short interest rose 36.9% month on month (ST) [Certain].
## Bull case
This is a near-monopoly P&C data franchise. Over 80% of revenue is subscription, and all top-100 U.S. carriers are customers (10-K) [Certain]. ROIC is 31.7%, gross margin 70.2%, operating margin 44.9% and FCF margin 39.4%, all rising over five years (RA,IS,CF) [Certain]. Every multiple sits below its own 5y minimum: P/E 26.0x vs 28.9x, P/FCF 17.8x vs 26.2x (RA) [Certain]. The share count fell 3.58% YoY (ST) [Certain], and beta is 0.69 (ST) [Certain]. Management guides H2 organic constant-currency growth accelerating to 6%-8% (Barclays transcript) [Likely]. If Q3 results on Nov 5 confirm that, the multiple could re-rate toward its own history [Likely].
## Decision
```json
{
  "ticker": "VRSK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class, subscription-based P&C data franchise has de-rated below its own 5-year multiple floor, but at a 5.63% FCF yield and a P/FCF in line with peers it is fairly rather than compellingly priced, while the cause of the de-rating is unresolved.",
  "rationale": "Quality is excellent, but the valuation is only cheap against its own history: P/FCF matches peers and EV/EBITDA is a 22% premium, while real yields are rising. Several risks are unquantified: the AccuLynx ruling, the cause of the 31% de-rating, and leverage up to 2.68x. That makes this good but not compelling, so conviction is 3 and I hold cash instead.",
  "price_at_decision": 168.68,
  "price_date": "2026-10-07",
  "research_note": "research/VRSK/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, signalling returns compressing toward peer levels.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 65%, below its 5y range, indicating pricing-power erosion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 65}},
    {"text": "Debt/EBITDA rises above 3.5x, constraining the buyback and bolt-on M&A model.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "Subscription/long-term-agreement share of revenue (10-K) falls below 75%, showing loss of the recurring-revenue model."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 205, "basis": "Q3 confirms the guided 6%-8% organic acceleration (Barclays transcript) and P/E re-rates from 26.0x to its 5y minimum of 28.9x [RA], with 3.58% annual share shrink [ST] adding EPS growth."},
    "base": {"probability": 0.45, "target_price_12m": 180, "basis": "P/FCF holds near the 18.0x peer median [RA] while FCF grows with mid-single-digit organic growth and buybacks on a 39.4% FCF margin [CF,IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 135, "basis": "EV/EBITDA converges from 17.2x to the 14.1x peer median [RA] as rising real yields compress premium multiples; probability raised modestly per the macro overlay's small bear tilt (research/VRSK/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
