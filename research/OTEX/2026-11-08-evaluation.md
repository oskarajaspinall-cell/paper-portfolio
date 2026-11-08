# Evaluation: Open Text Corporation (OTEX) — 2026-11-08
## Bear case
This is a shrinking, levered roll-up, not a compounder. Total revenue fell 4.0% in the latest 10-Q, and still fell 1.7% after adjusting for divestitures, with Cybersecurity, ITOM, ADM and Analytics all declining [company-reported] (https://www.sec.gov/Archives/edgar/data/1002638/000100263826000098/otex-20260930.htm) [Certain]. FCF margin is falling on both views: down 10.0pp over five years and from 17.5% to 16.3% over the last year, so the rolling trend confirms rather than contradicts the decline [CF-T] [Certain]. That undercuts the DCF that drives the 68.50 base fair value [Likely]. Net debt/EBITDA is 3.10x and Altman Z is 1.35 [ST], and the refinancing at higher coupons raises interest cost, so buybacks compete with deleveraging [Certain]. ROIC of 9.9% is flat and near the cost of capital [RA-T] [Likely]. A new CEO's multi-year plan only arrives in February, so investment weighted to the second half could compress margins first [Guessing].

## Bull case
The price already discounts a collapse. The reverse DCF implies -13.4% year-1 revenue growth, far worse than the reported decline, and even the mechanical bear fair value of 42.63 sits well above the 24.85 close [fact sheet Fair value] [Certain]. Every multiple sits at the bottom of its 5y range: EV/EBITDA 6.8x, P/FCF 7.0x, FCF yield 14.34% [RA, ST] [Certain]. Operating margin rose to 23.0% from 20.5% a year earlier, its 2-year high [IS-T], and ROCE rose to 11.3% [RA-T] [Certain]. Shares fell 5.26% year on year [ST] [Certain]. Content Cloud grew 20.7% and Q1 beat on adjusted EPS with the FY27 outlook maintained (transcript, /stocks/otex/transcripts/726164-q1-2027/) [Likely]. Switching costs in regulated records workloads protect the base [Likely]. Debt is now termed out to 2031/2033 [company-reported] [Certain].

## Decision
```json
{
  "ticker": "OTEX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, cash-generative information-management franchise trades at the floor of its own 5-year multiples, but declining organic revenue, a falling FCF margin and 3.10x leverage make the discount look partly earned until the February multi-year plan shows the core can grow.",
  "rationale": "The valuation is very low and the price implies a far steeper decline than reported. But revenue is still shrinking after divestiture adjustments, FCF margin is falling on the rolling view, leverage is high, interest cost is rising and the strategy reset is still pending. That makes it good but not compelling: conviction 3 does not meet the buy bar.",
  "price_at_decision": 24.85,
  "price_date": "2026-11-06",
  "research_note": "research/OTEX/2026-11-08.md",
  "triggers": [
    {
      "text": "Total revenue growth after divestiture adjustments turns positive in two consecutive quarterly 10-Qs, showing Content and Business Network growth outweighs the declining units.",
      "check": null
    },
    {
      "text": "TTM FCF margin rises back above 18%, above its 17.5% 2-year high, showing cash conversion has stopped eroding.",
      "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 18}
    },
    {
      "text": "Net debt/EBITDA falls below 2.5x (3.10x TTM now), showing deleveraging is real despite the buybacks and the higher-coupon refinancing.",
      "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.5}
    },
    {
      "text": "TTM operating margin falls below 20% (23.0% now), showing the second-half growth investment is eroding profitability, which would confirm the AVOID.",
      "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}
    }
  ],
  "scenarios": {
    "bull": {
      "probability": 0.25,
      "target_price_12m": 36.5,
      "basis": "The February plan shows organic growth led by Content Cloud (+20.7%, Q1 2027 transcript) and the price moves to the EV/Revenue base fair value of 36.56 [fact sheet Fair value]; we stay below the DCF bull because the DCF extrapolates a FCF margin that has fallen 10.0pp over five years [CF,IS]."
    },
    "base": {
      "probability": 0.45,
      "target_price_12m": 28.0,
      "basis": "Organic revenue keeps declining slightly (down 1.7% adjusted, 10-Q [company-reported]) while operating margin holds near 23.0% [IS-T], so EV/EBITDA lifts only modestly from 6.8x, a 3% position in its 5y range [RA]; this is well below the 68.50 mechanical base because the DCF assumes growth and FCF margins the rolling data do not show."
    },
    "bear": {
      "probability": 0.3,
      "target_price_12m": 18.0,
      "basis": "Revenue decline widens, second-half investment and higher refinancing coupons cut the FCF margin further from 16.3% [CF-T], and with net debt/EBITDA at 3.10x and Altman Z 1.35 [ST] the stock breaks its 52-week low of 19.77 [HI]; we put it below the 42.63 mechanical bear, which assumes FCF holds."
    }
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: multiples are already at their 5-year lows and the reverse DCF prices a steep decline. The obstacles are shrinking organic revenue, a falling FCF margin and leverage, so a lower price would not change the decision. Evidence that the core is growing (the February plan, adjusted revenue growth) would.",
  "replaces": null,
  "replacement_reason": null
}
```
