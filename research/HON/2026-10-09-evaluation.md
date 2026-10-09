# Evaluation: Honeywell International Inc. (HON) — 2026-10-09
## Bear case
The cheap headline multiples are an artefact. P/E 8.0x and EV/EBITDA 10.7x sit far below HON's 5y minimums because TTM profit includes a one-off disposition gain [Likely]. The cleaner DCF puts base fair value at 199.75, 3.3% below the 206.60 close, so there is no margin of safety [Certain]. The fundamentals are getting worse: ROIC fell from 21.4% to 13.5%, operating margin from 21.7% to 18.7%, and net debt/EBITDA rose from 1.05x to 3.03x [Certain]. TTM FCF margin is 10.5% against 14.5% in FY2025 [Certain]. The macro overlay tilts moderately toward the bear case, because rising real yields raise both the discount rate and the refinancing cost on leverage at a 5-year high [Likely]. Results land on Oct 22 while the Aerospace separation is still in progress, so the earnings base is hard to judge [Likely]. The stock trades 10.4% below its 200-day average and trails SPY by 29.7pp over 6 months [Certain].

## Bull case
HON is still a good business: 36.5% gross margin, 18.7% operating margin and 13.5% ROIC, with recurring aftermarket and licensing revenue [Certain]. The price implies only 2.8% year-1 revenue growth [Certain]. Management has set growth and margin targets through 2029 and describes strong orders and backlog [Likely]. The Dangote refinery wins support the UOP/process-technology franchise [Likely]. If the 10.5% TTM FCF margin is depressed by separation costs and recovers toward the 14.5% FY2025 level, the 6.12% FCF yield looks cheap [Guessing]. Buybacks cut the share count 1.87% YoY [Certain]. The DCF bull case of 284.73 is 37.8% above the close [Certain]. Short interest of 2.49% is low [Certain].

## Decision
```json
{
  "ticker": "HON",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A still-profitable automation franchise whose returns, margins and leverage have deteriorated for five years trades roughly at its DCF base fair value, with separation-distorted TTM multiples flattering the apparent discount.",
  "rationale": "The price sits about at the DCF base value, so there is no margin of safety. ROIC, operating margin, FCF margin and leverage are all trending the wrong way. Separation noise and the Oct 22 results cloud the earnings base, and the macro overlay tilts toward the bear case. Conviction 2 is below the buy threshold.",
  "price_at_decision": 206.60,
  "price_date": "2026-10-08",
  "research_note": "research/HON/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above the FY2025 level of 14.5%, showing the separation-related cash drag has rolled off.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 14.5}},
    {"text": "TTM operating margin returns above the FY2024 level of 20.9%, showing the automation-led margin targets are being delivered.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20.9}},
    {"text": "TTM ROIC rises back above the FY2024 level of 16.4%, reversing the five-year decline.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 16.4}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 284.73, "basis": "FCF margin recovers from 10.5% TTM toward 14.5% FY2025 [CF,IS] and the 2029 margin targets gain credibility, lifting value to the DCF bull fair value 284.73 [fact sheet Fair value]; probability trimmed for the overlay's moderate bear tilt (research/HON/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 199.75, "basis": "Separation completes with margins near 18.7% TTM operating [IS] and the price converges on the DCF base fair value 199.75 [fact sheet Fair value], consistent with the 2.8% growth the reverse DCF implies."},
    "bear": {"probability": 0.3, "target_price_12m": 164.78, "basis": "ROIC keeps falling from 13.5% [RA] while net debt/EBITDA rises past 3.03x [RA] and real yields climb, compressing value to the DCF bear fair value 164.78 [fact sheet Fair value]; probability raised for the overlay's moderate bear tilt (research/HON/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
