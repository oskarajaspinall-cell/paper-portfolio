# Evaluation: Bath & Body Works, Inc. (BBWI) — 2026-10-31
## Bear case
The cheapness is partly an illusion. TTM earnings and FCF are flattered by about $80 million of tariff refunds and a litigation settlement gain [company-reported] (https://www.sec.gov/Archives/edgar/data/701985/000070198526000029/bbwi-20260801.htm), so the run-rate P/E and P/FCF are higher than 5.9x and 4.5x [Likely]. The franchise is eroding: operating margin fell from 25.5% (FY2022) to 14.8% TTM and gross margin from 48.9% to 43.0% [IS] [Certain]; latest-quarter stores sales fell 5.4% on fewer transactions [company-reported] [Certain]. Net debt / EBITDA has risen to 3.00x with Altman Z at 2.27 [BS,ST] [Certain], leaving no buyback in the outlook [company-reported]. Management guided the coming quarter sharply lower, results are due Nov 19, 2026, and the stock has already rallied 14.1% in three months to an RSI of 71.3 with short interest rising [ST,HI] [Certain]. The turnaround is unproven [Guessing].
## Bull case
The price discounts collapse. The reverse DCF implies -19.5% year-1 revenue growth against a latest quarter down 2.3% [company-reported] [Certain]; even the mechanical bear fair value of 37.42 sits above the 22.77 close [Certain]. ROIC has held in the mid-20s for five years (24.5% TTM) [RA] [Certain], and every multiple sits below its own 5-year minimum and far below peer medians (P/E 14.3x, EV/EBITDA 10.4x) [RA] [Certain]. A 22.45% FCF yield [ST] lets the company delever quickly [Likely]. The Q2 beat and raised full-year guidance, direct returning to growth and wholesale via Ulta and Amazon suggest the "Consumer First Formula" is gaining traction [Likely]; a good holiday quarter could re-rate the shares toward the 5-year median EV/EBITDA of 8.6x [Guessing].
## Decision
```json
{
  "ticker": "BBWI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROIC fragrance brand trades below its own 5-year minimum on every multiple, but falling margins, declining store sales, 3.0x leverage and one-off-flattered TTM earnings mean the discount reflects real erosion rather than a clear mispricing.",
  "rationale": "Cheap on every multiple, but margins have eroded for five years, sales are shrinking, TTM cash flow is flattered by one-offs and leverage is 3.0x. The turnaround is unproven, the next quarter is guided sharply lower and the stock has rallied into results. Good but not compelling: conviction 3, so AVOID.",
  "price_at_decision": 22.77,
  "price_date": "2026-10-30",
  "research_note": "research/BBWI/2026-10-31.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, under every year of the five-year range (43.0% TTM), showing the brand is losing pricing power to promotions.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM operating margin falls below 12%, extending the decline from 25.5% (FY2022) to 14.8% and showing the turnaround is failing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "Net debt / EBITDA rises above 3.5x (3.00x TTM), showing FCF is not deleveraging the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "The 10-Q/10-K MD&A reports Stores net sales declining at a worse rate than the prior quarter for two consecutive quarters with Direct also declining (sec.gov); conversely, stores stabilising with direct growth would argue for conviction 4."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 36.19, "basis": "A strong holiday quarter proves the Consumer First Formula and EV/EBITDA returns to its 5y median 8.6x [RA], the EV/EBITDA base fair value of 36.19 in the fact sheet; the DCF base of 83.87 is not used because it capitalises one-off-flattered FCF (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 25.0, "basis": "Sales keep declining modestly and the multiple stays near its 5y-minimum EV/EBITDA of 6.5x [RA] on TTM EBITDA normalised lower for the tariff refunds and settlement gain [company-reported], so the price holds near the EV/EBITDA bear fair value of 22.82 plus deleveraging; well below the blended base of 67.98 because the DCF treats flattered FCF as recurring."},
    "bear": {"probability": 0.3, "target_price_12m": 15.75, "basis": "The guided-down quarter and weak holiday sales push operating margin further down from 14.8% [IS] with leverage above 3.0x [RA], and the stock falls back to its September swing low of 15.75 [HI], below the mechanical bear fair value 37.42 because that value assumes margins stop eroding."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum multiples and far below base fair value (base 67.98 x 0.8 is above the price). The obstacle is eroding margins, shrinking store sales and an unproven turnaround; evidence of stabilisation in the coming results, not a lower price, would raise conviction.",
  "replaces": null,
  "replacement_reason": null
}
```
