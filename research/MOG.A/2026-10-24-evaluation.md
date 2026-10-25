# Evaluation: Moog Inc. (MOG.A) — 2026-10-24
## Bear case
The fall from the 448.85 high has not made the stock cheap. EV/EBITDA of 18.8x is still above its 5y maximum of 15.5x, and EV/Sales and P/B are also above their maxima [RA] [Certain]. Even the mechanical bull fair value (219.61) is below the 341.34 close, and the reverse DCF needs 20.7% year-one revenue growth, a demanding bar for a business with operating margins of about 10–12% [Likely]. Part of the TTM margin step-up came from $30 million of IEEPA tariff refunds [company-reported] (https://www.sec.gov/Archives/edgar/data/67887/000162828026051294/mog-20260627.htm), which will not repeat [Certain]. FCF conversion has been erratic (-21.5% in FY2023) [CF,IS] [Certain]. No company-specific cause for the fall shows, so this looks like de-rating after a run, and it may have further to go [Guessing]. Short interest rose 34.1% in a month [ST] [Certain].
## Bull case
Quality is improving: ROIC rose from 8.2% to 13.6% and operating margin from 8.4% to 12.0% [RA,IS] [Certain]. Net debt/EBITDA fell from 2.72x to 1.71x and TTM FCF conversion recovered to 92.9% [BS,CF] [Certain]. Backlog rose in every segment, led by defense, space and data-center pumps [company-reported] (https://www.sec.gov/Archives/edgar/data/67887/000162828026051294/mog-20260627.htm), and Q3 2026 was a record with raised guidance [Certain]. Against peers CW, WWD, HEI and TDG it trades at a discount on P/E and EV/EBITDA [Certain]. The thesis is intact: the fall carries no fundamental news [Likely], and RSI of 32.2 suggests selling is stretched [Guessing]. Results on Nov 20, 2026 could restart momentum [Guessing].
## Decision
```json
{
  "ticker": "MOG.A",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An improving motion-control franchise with rising ROIC and falling leverage, but even after a de-rating from its August high it trades above its own 5-year maximum EV/EBITDA, with a price that implies 20.7% year-one revenue growth.",
  "rationale": "The entry-price hit reflects de-rating, not a fundamental break, but the price still sits above every mechanical fair value and above its own 5y multiple range, while part of TTM margin is one-off tariff refunds. Good business, not a compelling price: AVOID at conviction 3.",
  "price_at_decision": 341.34,
  "price_date": "2026-10-23",
  "research_note": "research/MOG.A/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10.0%, reversing the expansion from 8.4% (FY2021) to 12.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 3.0%, showing the cash recovery to 8.1% was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "TTM ROIC falls below 10.0%, giving back most of the rise to 13.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.71x TTM), showing acquisitions are re-levering the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 410, "basis": "Backlog growth in every segment [company-reported] sustains the re-rating toward the peer median EV/EBITDA of 22.3x [P:CW,P:WWD,P:HEI,P:TDG]; above the mechanical bull fair value because the DCF is anchored on erratic historical FCF (FY2023 -1.1% margin) [CF]."},
    "base": {"probability": 0.45, "target_price_12m": 320, "basis": "Earnings growth roughly offsets a partial EV/EBITDA de-rating from 18.8x toward its 5y range [RA] as the non-recurring tariff refunds drop out of TTM margin [company-reported]; above the base fair value of 152.05 because that blend leans on FCF history that understates the improved ROIC trend [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 260, "basis": "EV/EBITDA reverts to its 5y maximum of 15.5x [RA] on TTM EBITDA with the tariff-refund benefit removed [company-reported], continuing the de-rating seen in the -16.7% 3-month move [HI]."}
  },
  "entry_price": 121.64,
  "entry_basis": "valuation file: base 152.05 x 0.8 (default margin of safety); the obstacle is price, since the business fundamentals are improving.",
  "replaces": null,
  "replacement_reason": null
}
```
