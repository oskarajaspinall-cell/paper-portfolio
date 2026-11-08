# Evaluation: Aldar Properties PJSC (ADX:ALDAR) — 2026-11-08
## Bear case
The cheap P/E (7.4x, below its 5y minimum of 9.1x [RA]) flatters a developer whose profits are booked ahead of cash [Likely]. The fact sheet's Direction change is the core problem: TTM FCF margin fell from 23.1% to 6.7% in a year, 18.3pp below its 2-year high [CF-T], and FCF/NI is 28.3% TTM [Certain]. That is driven by land and project spend ahead of handovers, funded by debt: net debt/EBITDA rose to 1.17x from 0.53x at FY2025 [BS,IS] [Certain]. On cash, the stock is expensive: P/FCF 25.9x against a 5y maximum of 14.3x [RA] [Certain]. Management revised FY sales and EBITDA guidance down in H1 and cited softer sales, hospitality weakness and regional tensions in Q3 [OV transcripts] [Likely]. Gross margin slid from 40.9% to 36.0% [IS] [Certain]; Altman Z is 1.88 [ST] [Certain]. Returns sit at cycle highs for a single-city developer [Likely]. This threatens the thesis until cash conversion recovers.
## Bull case
Aldar is Abu Dhabi's largest developer with land-bank access and government-linked partners a newcomer cannot copy [Likely]. ROIC rose from 8.2% to 16.1% over five years and holds at 14.0% TTM, flat over the last 12 months [RA-T] [Certain]; ROE is 19.7% [RA] [Certain]. TTM operating margin is at its 2-year high of 28.6% [IS-T] [Certain]. Q3 9M revenue and net profit grew with FY26 guidance maintained, on a record backlog [OV transcript] [Likely]. Every earnings multiple sits below its 5y minimum, P/B is at its 1.1x median, and both the mechanical bear (8.73) and base (10.42) fair values sit above the 7.98 close [fact sheet] [Certain]. The reverse DCF needs 9.9% year-1 growth, below the reported 11% 9M revenue growth [OV] [Likely]. Outside capital (Apollo) validates the platform [Likely]. If working capital unwinds on handovers, FCF re-rates.
## Decision
```json
{
  "ticker": "ADX:ALDAR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return Abu Dhabi developer trades below its own 5-year earnings multiples, but the collapse in cash conversion and rising leverage mean the cheap P/E is not yet backed by free cash flow.",
  "rationale": "Earnings multiples and mechanical fair value look attractive, but TTM FCF margin of 6.7% (from 23.1%), P/FCF above its 5y maximum, rising net debt, trimmed sales guidance and regional tension leave the skew good, not compelling. Conviction 3: AVOID until cash conversion recovers.",
  "price_at_decision": 7.98,
  "price_date": "2026-11-06",
  "research_note": "research/ADX-ALDAR/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (14.0% now), showing the returns step-up was cyclical.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.17x TTM now), showing growth is increasingly debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM FCF margin stays below 5% (6.7% now), showing earnings are not converting to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "TTM operating margin falls below 22% (28.6% now), the FY2022 low, showing pricing or mix pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.42, "basis": "Handovers convert backlog to cash, FCF margin recovers toward its 25.0% 2-year high [CF-T] and P/E moves toward its 5y median 11.0x [RA], reaching the mechanical base fair value; the mechanical bull of 101.10 is not meaningful (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 8.73, "basis": "ROIC holds near 14.0% [RA-T] with FY26 guidance maintained (Q3 transcript [OV]) but FCF stays weak, so P/E recovers only partway toward its 5y minimum 9.1x [RA]: the mechanical bear fair value of 8.73 [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 7.03, "basis": "Softer sales and hospitality weakness from regional tension (Q3 transcript [OV]) cut earnings while net debt/EBITDA keeps rising from 1.17x [BS,IS], and the price revisits its 52-week low of 7.03 [HI]; macro overlay weight is context, so no tilt."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the mechanical bear fair value; the default anchor (base 10.42 x 0.8) sits above the close. Conviction 4 needs FCF conversion to recover and leverage to stabilise, not a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```
