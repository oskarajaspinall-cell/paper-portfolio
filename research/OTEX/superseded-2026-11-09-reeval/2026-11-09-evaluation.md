# Evaluation: Open Text Corporation (OTEX) — 2026-11-09
## Bear case
The core is not growing: total revenue is down 4.0%, and down 1.7% after divestitures, with Cybersecurity, ITOM, ADM and Analytics shrinking [company-reported] (https://www.sec.gov/Archives/edgar/data/1002638/000100263826000098/otex-20260930.htm). [Certain] The direction signal is FCF margin: 16.3% TTM against 17.5% a year earlier [CF-T], and down 10.0pp over five years [CF,IS]. [Certain] The five-year fall dates mostly to the acquisition-driven FY2023 leverage spike (7.21x), not to the last year. [Likely] The latest dip comes with rising operating margin and ROCE, which points to cash costs below EBIT, such as interest and restructuring, rather than lost pricing. [Guessing] That would become structural if the refinancing at higher coupons keeps squeezing FCF. [Likely] Leverage of 3.10x and an Altman Z of 1.35 leave little room for error. [Certain] Buybacks compete with paying down debt. A new multi-year plan due in February could reset expectations lower. [Guessing]

## Bull case
The price already assumes a collapse: the reverse DCF implies -13.4% revenue growth in year 1 against a reported decline of 1.7% after divestitures [company-reported]. [Certain] Every multiple sits at the bottom of its 5y range: P/E 9.4x, EV/EBITDA 6.8x, P/FCF 7.0x, and the FCF yield is 14.34% [RA,ST]. [Certain] Over the last year profitability improved rather than decayed. Operating margin is 23.0% against 20.5% a year earlier, at its 2-year high, and ROCE is 11.3% against 9.6% [IS-T,RA-T]. [Certain] The small FCF-margin dip is therefore an explained financing and transition effect, not a broken franchise. [Likely] Switching costs in regulated records and compliance workloads protect the base. [Likely] Divestitures prepaid debt and the 2027 maturity was pushed to 2031/2033. [Certain] The share count fell 5.26% in a year [ST], and the full-year outlook was maintained (transcript). [Likely] Even the mechanical bear fair value of 42.63 is above the price. [Certain]

## Decision
```json
{
  "ticker": "OTEX",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A switching-cost information-management franchise with a rising operating margin, a 14.34% FCF yield and shrinking share count trades at the floor of its own 5-year multiples, where the price implies a -13.4% revenue collapse that a 1.7% divestiture-adjusted decline does not show.",
  "rationale": "The falling direction is limited to FCF margin and is explained by financing and transition costs. Operating margin and ROCE are rising over the last year. At a 14.34% FCF yield the skew is favourable. Organic decline, 3.10x leverage and the February plan keep conviction at 4, not 5. Python sets the standard volatility-scaled core size.",
  "price_at_decision": 24.85,
  "price_date": "2026-11-06",
  "research_note": "research/OTEX/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20% (23.0% now, 20.5% a year earlier), showing that the margin gains were cost cuts on a shrinking base rather than durable.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 13% (16.3% now), turning the explained FCF dip into structural cash erosion from interest and organic decline.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 13}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.7x (3.10x TTM now), showing buybacks are outrunning deleveraging."},
    {"text": "Total revenue growth after divestiture adjustments is below -4% in two consecutive 10-Qs, or the company withdraws or cuts its full-year outlook, including in the February multi-year plan."}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 45.0, "basis": "The February plan confirms stabilising organic revenue and P/E re-rates toward its 5y median 17.2x [RA] from 9.4x, a value below the mechanical bull of 132.27 and near the mechanical bear of 42.63, because the DCF extrapolates acquisition-inflated revenue growth."},
    "base": {"probability": 0.45, "target_price_12m": 36.56, "basis": "Operating margin holds near 23.0% [IS-T] with revenue roughly flat after divestitures [company-reported, sec.gov 10-Q], valued at the EV/Revenue base fair value of 36.56 [fact sheet Fair value] rather than the blended 68.50, whose DCF leg assumes acquisition-era growth."},
    "bear": {"probability": 0.25, "target_price_12m": 20.0, "basis": "Organic decline deepens and higher refinancing coupons push FCF margin below its 16.3% TTM [CF-T], so P/E stays at its 5y low of 8.4x [RA] on lower earnings, near the 52-week low of 19.77 [HI] and below the mechanical bear of 42.63, which does not model that FCF erosion."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "base", "field": "growth", "value": 0.0, "reason": "The base growth is built from 3y/5y revenue CAGRs inflated by acquisitions, while the latest 10-Q shows revenue down 1.7% after divestitures [company-reported] (https://www.sec.gov/Archives/edgar/data/1002638/000100263826000098/otex-20260930.htm), so flat growth is the honest base."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```
