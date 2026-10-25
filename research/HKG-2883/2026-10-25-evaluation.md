# Evaluation: China Oilfield Services Limited (HKG:2883) — 2026-10-25
## Bear case
This is a low-return, cyclical service provider, not a quality franchise. TTM ROE of 8.5% and ROIC of 8.8% [RA] sit below the cost of equity implied by the owner's 3.5% CNY country premium on a 4.96% risk-free rate [Certain]. On that basis a P/B of 1.0x [RA] is close to fair, not a bargain [Likely]. The moat is captive access to CNOOC's offshore programme. The same parent is the dominant customer and the controlling shareholder, so related-party pricing decides margins and minority holders take what is left [Likely]. FY2025 margins and ROIC are the five-year highs of an oil-capex upcycle; if E&P budgets turn, the "below 5y minimum" multiples are just peak earnings [Likely]. FCF conversion of 151.8% reflects depreciation on a fleet that needs reinvestment [Likely]. Q3 2026 results are out but not analysed, Altman Z is 2.45 (grey zone), and 6-month relative strength is -27.2pp [Certain].
## Bull case
Every multiple sits below its own 5y minimum: P/E 7.8x vs 13.8x, EV/EBITDA 4.7x vs 5.8x, P/FCF 8.3x vs 9.8x. Each is roughly half the peer median [RA] [Certain]. FCF yield is 12.00% [ST] and net debt/EBITDA has fallen from 2.00x to 0.66x [BS,IS] [Certain]. The reverse DCF implies -15.0% year-1 revenue growth, against rising ROIC (1.9% to 9.6%) and operating margin (7.6% to 12.4%) [RA,IS] [Likely]. The technology segments delivered 55% of 2025 revenue and 72% of profit (https://stockanalysis.com/quote/hkg/2883/transcripts/379581-h2-2025/) [Likely]. Even the mechanical bear fair value of 13.55 HKD is far above the 7.41 close [Certain]. Beta is 0.63 and the share count is shrinking 0.51% a year [ST] [Certain].
## Decision
```json
{
  "ticker": "HKG:2883",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging Chinese offshore oilfield-services firm trades below its own 5-year minimum multiples at a 12.00% FCF yield, but returns below its cost of equity, a captive parent-customer and an oil-capex cycle make it cheap rather than a good business at an attractive price.",
  "rationale": "The valuation is clearly cheap, but core needs a good business, and this one is not: ROE is below its cost of equity, the moat depends on the parent, margins are cyclical and the Q3 results have not been analysed. That is good but not compelling, so conviction is 3 and the answer is AVOID. Price is not the obstacle.",
  "price_at_decision": 7.41,
  "price_date": "2026-10-23",
  "research_note": "research/HKG-2883/2026-10-25.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9%, giving back most of the rise from 7.6% (FY2022) to 12.4% and showing the offshore capex upcycle has turned.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "TTM ROIC falls below 6%, reversing the improvement to 9.6% (FY2025) and confirming returns stay well below the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "TTM FCF margin falls below 6%, under the FY2022 five-year low of 7.7%, showing fleet reinvestment is consuming the cash yield.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.66x TTM now), undoing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 13.55, "basis": "Multiples recover toward the bottom of their 5y range (P/E min 13.8x [RA]) as offshore capex holds, reaching the mechanical bear fair value of 13.55 [IS,BS,CF,RA]; set below the base 21.43 because a sub-cost-of-equity ROE of 8.5% [RA] does not justify the mid-cycle multiples the fair-value model assumes."},
    "base": {"probability": 0.5, "target_price_12m": 8.1, "basis": "Fundamentals stay steady but the parent-control and China discount persist, so the stock drifts back to its 200-day average of 8.10 [ST,HI] and stays well below the mechanical fair value range, which ignores governance and cyclicality."},
    "bear": {"probability": 0.25, "target_price_12m": 6.09, "basis": "An oil-capex downturn compresses the cyclical-peak FY2025 margins (operating 12.2% [IS]) and the stock retests its 52-week low of 6.09 [HI], below book value (P/B 1.0x [RA])."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below even the mechanical bear fair value of 13.55. What holds conviction at 3 is business quality (ROE below its cost of equity, a captive parent-customer, oil-cycle margins), so a lower price would not change the decision; analysed Q3 2026 results showing durable returns would.",
  "replaces": null,
  "replacement_reason": null
}
```
