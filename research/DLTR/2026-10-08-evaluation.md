# Evaluation: Dollar Tree, Inc. (DLTR) — 2026-10-08
## Bear case
This is not a clean dip to the 50-day average. At 116.30 the stock is 5.7% below the 50-day MA (123.27), outside the -5%/+2% pullback band, and 0.6% below the 200-day MA [Certain] [HI]. The trend structure is breaking: swing highs fell from 137.07 to 134.99 and the 21-Sep swing low (111.23) undercut the 27-Aug low (118.11) [Certain] [HI]. Relative strength vs SPY is -9.1pp over 3m and -7.8pp over 6m [Certain] [HI]. The stock sold off after a beat-and-raise [Likely] (Schwab headline, OV), so the good news looks priced, and part of Q2 EPS came from one-off tariff refunds [Likely] (transcript, OV). The next Q3 report date is not shown, and the usual early-December timing [Guessing] would fall inside a 3-month hold, adding gap risk.
## Bull case
The 12-month trend is still up: +36.9%, +21.2pp vs SPY, and the 50-day MA sits 5.3% above the 200-day MA [Certain] [ST]. RSI 47.5 shows the stock has cooled off without breaking down [Certain] [ST]. The fundamentals support it: Q2 beat and FY guidance was raised [Likely] (transcript, OV). TTM ROIC is 13.6%, FCF margin is 9.9% and net debt/EBITDA is down to 2.64x [Certain] [RA, CF, IS]. Valuation leaves little crowding risk: 14.2x P/E and 11.4x EV/EBITDA are below the 5y minimums and peer medians [Certain] [RA]. The 2:1 target of 133.20 sits under the 137.07 August peak [Certain] [HI]. Beta of 0.72 also limits market-driven gap risk [Certain] [ST].
## Decision
```json
{
  "ticker": "DLTR",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A cheap, improving discount retailer in a 12-month uptrend has pulled back, but the dip has slipped below both moving averages with a lower swing low, so the pullback-in-uptrend edge is not clear.",
  "rationale": "The setup is marginal. Price is 5.7% below the 50-day, outside the -5% band, and below the 200-day. The 111.23 low undercut the prior swing low, and 3m relative strength is -9.1pp. The stock sold off on a beat-and-raise. The 2:1 target only just clears, and the unknown Q3 date adds gap risk. Conviction 3, so AVOID; cash is acceptable.",
  "price_at_decision": 116.30,
  "price_date": "2026-10-07",
  "research_note": "research/DLTR/2026-10-08.md",
  "exit_plan": {"target": 133.20, "stop": 107.85, "time_limit": "2026-11-30"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140.87, "basis": "Raised guidance holds and the TTM P/E re-rates from 14.2x to the 17.2x peer median [RA, P:DG/WMT/TGT/FIVE], supported by rising ROIC (13.6% TTM) and FCF margin (9.9%) [RA, CF]."},
    "base": {"probability": 0.50, "target_price_12m": 123.27, "basis": "The multiple stays near its below-5y-minimum level and the price returns to the 50-day MA of 123.27 [HI], with the 9.01% FCF yield [ST] and -6.93% YoY share count [ST] supporting per-share value; macro overlay is context only and does not move this."},
    "bear": {"probability": 0.25, "target_price_12m": 85.88, "basis": "The one-off tariff-refund EPS boost fades and the post-results lower-high/lower-low pattern [HI] continues, so the price retests the 6-month low of 85.88 (2026-05-13) [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
