# Evaluation: Full Truck Alliance Co. Ltd. (YMM) — 2026-10-19
## Bear case
Growth has slowed to low single digits: the Q2 2026 call summary describes modest net-revenue growth despite double-digit order growth, and Q3 guidance brackets the prior-year quarter, so it is close to flat [Likely] ([OV] transcript and release headlines). TTM FCF margin of 51.4% rests on FCF conversion of 155.8%, well above the roughly 100% of FY2023-FY2025, which points to brokerage working-capital inflows that can reverse; the 10.82% FCF yield likely overstates the run-rate [Likely] [CF,IS]. Piotroski F of 4 is weak [Certain] [ST]. Net margin is helped by interest on net cash, not only by the platform [Guessing]. Beijing already froze new-user registration from July 2021 to June 2022, and VIE and HFCAA risks persist [Certain] (sec.gov 20-F). The stock is down 29.9% over 12 months and trades below its 200-day average, so the market is not yet confirming the re-rating [Certain] [ST,HI].

## Bull case
The quality turn is real. ROIC rose from -76.8% (FY2021) to 16.7% TTM and operating margin to 33.6%, with gross margin steady at 87.3% [Certain] [RA,IS]. The balance sheet is net cash (net debt/EBITDA -5.34x) and the share count is shrinking slightly [Certain] [BS,ST]. P/E of 14.8x, EV/EBITDA of 8.7x and P/FCF of 9.2x all sit below their own 5-year minimums, and well below the peer median on earnings multiples [Certain] [RA]. The reverse DCF implies -7.7% year-1 revenue growth, a decline that rising fulfilled orders do not show [Likely] [fact sheet]. The merged Yunmanman/Huochebang network gives it liquidity a new entrant would struggle to match [Likely] (fulltruckalliance.com). Base fair value of 14.86 sits well above the 8.75 close [Certain] [fact sheet].

## Decision
```json
{
  "ticker": "YMM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 87%-gross-margin freight platform trades below its own 5-year minimum multiples, but stalled revenue growth, working-capital-inflated FCF and PRC regulatory risk make it good rather than compelling.",
  "rationale": "Cheap and improving, but the cheapness rests partly on a TTM FCF figure flattered by conversion far above its history, while guidance points to near-flat revenue. Without growth the multiples have no catalyst to recover, and the regulatory tail is real. Conviction 3: AVOID; cash is acceptable.",
  "price_at_decision": 8.75,
  "price_date": "2026-10-16",
  "research_note": "research/YMM/2026-10-19.md",
  "triggers": [
    {"text": "TTM net margin falls below 20%, signalling renewed fee or regulatory pressure on monetization.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 10%, undoing the post-2022 monetization recovery.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below the FY2024 level of 22.0%, reversing the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "A renewed PRC cybersecurity or antitrust action halts new-user registration or matching-fee collection, as in 2021-22, disclosed in a 20-F/6-K or company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 13.01, "basis": "Revenue growth re-accelerates with fulfilled orders and EV/Sales recovers toward its 5y minimum of 4.1x [RA], matching the EV/Revenue base value of 13.01 [fact sheet]; below the blended 14.86 because the DCF leans on the inflated TTM FCF margin."},
    "base": {"probability": 0.5, "target_price_12m": 9.6, "basis": "Near-flat revenue per the Q3 guidance [OV release headline] keeps P/E near 14.8x and below its 5y minimum [RA]; modest earnings and buybacks only, well short of base fair value because FCF conversion of 155.8% [CF,IS] normalises."},
    "bear": {"probability": 0.25, "target_price_12m": 6.2, "basis": "A renewed PRC regulatory action, as in the 2021-22 registration freeze (sec.gov 20-F), or a working-capital reversal cuts FCF; net cash at -5.34x net debt/EBITDA [BS,IS] keeps the floor well above the mechanical bear of -8.49."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "base", "field": "margin", "value": 0.36, "reason": "TTM FCF margin of 51.4% reflects FCF conversion of 155.8% vs about 100% in FY2023-FY2025 [CF,IS]; the FY2025 FCF margin of 36.0% is a sustainable base."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5-year minimum P/E, EV/EBITDA and P/FCF [RA]. Conviction 4 needs evidence, not a lower price: revenue re-acceleration in reported results and FCF conversion holding near its history.",
  "replaces": null,
  "replacement_reason": null
}
```
