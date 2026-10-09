# Evaluation: Delta Air Lines, Inc. (DAL) — 2026-10-09
## Bear case
On today's Q3 print, fuel costs outran fares. Adjusted fuel expense rose 62% YoY, FY26 EPS guidance was cut to $5.10-$5.60 from $6.50-$7.50 and FY26 FCF guidance to ~$2.5bn from $3-4bn [Likely] (note §2). TTM operating margin has already slipped to 7.1% from 8.9% in FY25 and ROIC to 10.0% from 12.3% [Certain] [IS][RA]. Yet EV/EBITDA of 9.5x sits above its own 5y maximum of 8.1x [Certain] [RA], and the $82.14 price is 27.1% above base fair value of $59.87. The reverse DCF implies 14.4% year-1 revenue growth [Certain] (fact sheet). With beta 1.34, net debt/EBITDA of 2.19x [Certain] [ST][RA] and real yields up 0.61pp in 3m (macro overlay), downside from both the earnings and the multiple is the larger risk [Likely]. Short interest rose 16.3% month on month [Certain] [ST].
## Bull case
The business is far better than in FY21-22. ROIC went from -5.8% to 12.3% (FY25), FCF conversion is 91.9% TTM and net debt/EBITDA fell from 4.38x to 2.19x [Certain] [RA]. Piotroski F is 7 [Certain] [ST]. Premium and loyalty revenue (American Express co-brand) diversify earnings away from pure ticket pricing [Likely] (note §1). P/E of 13.6x is 24% below peer median and at the 10th percentile of its own 5y range, and P/FCF of 17.8x is 18% below peers [Certain] [RA]. Management says demand is strong and guides Q4 revenue growth with a 7%-9% operating margin [Likely] (fact sheet news). If fuel eases, margins could quickly rebuild toward FY24's 9.4% [Guessing]. Debt paydown continues [Likely] (note §5).
## Decision
```json
{
  "ticker": "DAL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A structurally improved but still fuel-exposed airline trades 27% above its own-history base fair value and above its 5y EV/EBITDA maximum just as fuel costs force a deep FY26 earnings and FCF guidance cut.",
  "rationale": "Quality has improved, but earnings are heading down. The FY26 EPS and FCF guidance was just cut, margins and ROIC are falling on a TTM basis, and EV/EBITDA is above its 5y range. The low P/E rests on earnings that are now being revised down. Rising real yields add a small bearish tilt. There is no margin of safety, so no position.",
  "price_at_decision": 82.14,
  "price_date": "2026-10-08",
  "research_note": "research/DAL/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 9%, back to its FY2024-FY2025 level of 8.9%-9.4%, showing fuel costs are being passed through in fares.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 9}},
    {"text": "TTM FCF margin rises above 6%, back to the FY2025 level of 6.1%, showing cash generation survives the fuel shock.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 6}},
    {"text": "TTM ROIC climbs back above 12%, back to the FY2023-FY2025 range of 12.0%-12.9%, showing returns are durable through the cycle.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 96.0, "basis": "Fuel eases and margins rebuild toward the FY2024 9.4% operating margin [IS], and the stock retakes its 52-week high of 95.68 [HI]. This is well below the mechanical bull of 158.43, which needs the reverse-DCF 14.4% growth that the guidance cut undermines."},
    "base": {"probability": 0.45, "target_price_12m": 72.0, "basis": "Lower FY26 earnings after the guidance cut (note §2) pull EV/EBITDA back from 9.5x toward its 8.1x 5y maximum [RA]. That leaves the price between today's close and the EV/EBITDA-method base of 61.27, above the blended base of 59.87 because peers trade at a 10.3x median [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 50.47, "basis": "Fuel keeps compressing margins and EV/EBITDA reverts to its 5y median of 7.6x [RA], the EV/EBITDA-method bear of 50.47 (fact sheet). The through-cycle DCF bear of -0.21 is a mechanical artefact of a trough year. The probability is raised by 0.05 from bull for the macro overlay's small bearish tilt on rising real yields (research/DAL/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
