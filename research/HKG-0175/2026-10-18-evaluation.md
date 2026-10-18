# Evaluation: Geely Automobile Holdings Limited (HKG:0175) — 2026-10-18

## Bear case
Geely is an auto maker with an operating margin of 4.1% TTM and a modest moat, selling into a China market where September retail passenger-car sales fell 28.0% YoY (WSJ headline) [Likely]. The cheap multiples rest on cash flow that may not last: FCF conversion of 283.7% TTM is far above earnings, which points to working-capital funding (supplier payables) rather than repeatable cash, so the 33.77% FCF yield likely overstates owner earnings [Guessing]. Shares rose 5.57% YoY [Certain]. Control sits with the unlisted Geely Holding Group, and its deal flow (NIO Power, Ford España) brings related-party risk [Likely]. The price is falling: 6-month momentum -39.3%, below both moving averages [Certain]. Results are due Oct 29, 2026, so the price-war damage is still unknown [Certain]. The macro overlay is moderate toward bear (rising US/HK yields, firm CNY) [Likely].

## Bull case
Returns have changed: ROIC rose from 3.6% (FY2021) to 24.3% TTM, ROE to 17.4%, and operating margin from 1.8% to 4.1% [Certain]. The balance sheet is net cash (net debt/EBITDA -2.65x) [Certain]. On P/E 8.4x and EV/EBITDA 3.9x, the stock sits at or below its own 5-year minimum and well under the peer medians of 14.2x and 5.8x [Certain]. Even the mechanical bear fair value of 41.46 HKD is far above the 15.01 close [Certain]. September sales of 292,168 vehicles were the year's best month, with NEV sales at a record (company release headline) [Likely]. Overseas expansion (Canada entry in 2027, Google services in cars abroad) adds a growth option outside the China price war [Likely]. Gross margin held at 17.3% TTM through the price war [Certain].

## Decision
```json
{
  "ticker": "HKG:0175",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Chinese auto maker with sharply higher returns trades below its own 5-year minimum multiples, but thin margins in a collapsing domestic market and working-capital-driven cash flow make the cheapness a possible value trap.",
  "rationale": "Cheap and improving, but not compelling: operating margin of 4.1% gives little room in a price war, FCF quality is doubtful, results on Oct 29 are an open risk, the macro tilt is toward bear, and the portfolio already carries China and Consumer Discretionary exposure. Good but not high conviction, so AVOID.",
  "price_at_decision": 15.01,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-0175/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 14.1%, the FY2022 trough, showing price-war erosion worse than the last cycle.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 14.1}},
    {"text": "TTM operating margin falls below 2.5%, the FY2024 level, showing the NEV scale gains have reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 2.5}},
    {"text": "TTM ROIC falls below 10.5%, the FY2024 level, showing the returns improvement was cyclical rather than structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10.5}},
    {"text": "Reported results show operating margin holding at or above the 4.1% TTM level through the China price war, with FCF supported by earnings rather than payables; this would raise conviction (text-only, checked against the next results release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 19.4, "basis": "EV/EBITDA re-rates from 3.9x to the 5.8x peer median [RA, P:HKG:1211] on TTM EBITDA with the net cash kept; still far below the mechanical fair value, whose through-cycle DCF relies on the 283.7% FCF conversion [CF,IS] and a 0.48 beta [ST] that we do not trust."},
    "base": {"probability": 0.45, "target_price_12m": 15.5, "basis": "P/E stays near its 5y floor of 8.4x [RA] as the price war keeps operating margin around 4.1% TTM [IS] and earnings roughly flat, with the stock carried by net cash rather than re-rated."},
    "bear": {"probability": 0.3, "target_price_12m": 10.5, "basis": "Operating margin falls back to the FY2024 2.5% [IS] as China retail sales keep falling (WSJ headline, factsheet news), cutting earnings at an unchanged trough P/E [RA]; bear weight raised moderately per the macro overlay's tilt toward bear (research/HKG-0175/2026-10-18-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades far below the mechanical base fair value of 67.90 HKD and its own 5-year minimum multiples. What blocks a BUY is unresolved earnings and cash-flow quality in a price war, so a lower price would not change the decision; the Oct 29, 2026 results showing margins holding would.",
  "replaces": null,
  "replacement_reason": null
}
```
