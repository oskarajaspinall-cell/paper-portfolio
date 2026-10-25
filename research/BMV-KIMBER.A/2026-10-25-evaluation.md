# Evaluation: Kimberly-Clark de México (BMV:KIMBER.A) — 2026-10-25
## Bear case
The quality step-up looks cyclical rather than structural. Operating margin was 17.5% in FY2022 and 22.9% TTM. The jump came with lower input costs and a stronger peso, and the Q3 call now flags persistent input-cost pressure, flat sales and weak demand through year-end [Likely]. TTM ROIC of 51.9% and FCF conversion of 132.4% sit well above FY2024-25 levels of 103.4%-105.4%, so trailing cash flow is flattered [Certain]. On those trailing figures P/E 14.3x is only at 27% of its own range and EV/EBITDA 8.5x is near its median, so it is not cheap if margins mean-revert [Certain]. If margins return toward FY2021-22 levels, earnings fall and the bear fair value of 28.23 is reachable [Likely]. The business is Mexico-only with no volume growth, a likely controlled thin float (16.7% institutional) and a falling price trend [Guessing].

## Bull case
This is a category leader in an essential staples market, with TTM gross margin of 40.8% held despite flat Q3 sales, because savings offset cost inflation [Likely]. Net debt/EBITDA is 0.87x, the FCF yield is 9.41% and the share count fell 0.97%, so capital returns are well funded [Certain]. P/FCF of 10.6x sits at 4% of its 5y range, and the stock trades at a steep discount to KMB, PG and CL on every earnings multiple [Certain]. The reverse DCF implies a -5.5% revenue decline, which a staples franchise with record Q1/Q2 2026 revenue is unlikely to deliver [Likely]. Base fair value is 51.50 [Certain]. Beta of 0.18 makes it a defensive diversifier [Certain]. Management expects gradual improvement in 2027 [Likely].

## Decision
```json
{
  "ticker": "BMV:KIMBER.A",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return Mexican tissue and diaper leader with a 9.41% FCF yield and low leverage looks cheap on cash flow, but its earnings sit on cost-cycle-boosted margins just as Q3 brought flat sales and renewed input-cost pressure.",
  "rationale": "Good but not compelling. P/FCF is near its 5y low, but on earnings multiples it is only mid-range on margins that look cyclically high, while Q3 showed flat sales, weak demand guidance and input-cost pressure. The upside depends on margins holding, which is still unproven. Revisit after the FY2026 results.",
  "price_at_decision": 37.86,
  "price_date": "2026-10-23",
  "research_note": "research/BMV-KIMBER.A/2026-10-25.md",
  "triggers": [
    {"text": "TTM gross margin falls below 36%, giving back most of the FY2023-25 step-up from 32.9% and confirming the margin gain was cost-cycle driven.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 36}},
    {"text": "TTM ROIC falls below 30%, back toward FY2021-22 levels of 25.3%-25.8%, showing returns were peak-cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 10%, the FY2021 level of 9.9%, showing cash conversion has normalised down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.87x TTM now), showing payouts are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 56.17, "basis": "Margins hold near the TTM 22.9% operating level and demand recovers in 2027 as management guides on the Q3 call, so earnings re-rate to the P/E-method bull value of 56.17 [fact sheet Fair value], below the 62.00 blended bull because the DCF capitalises a trailing FCF conversion of 132.4% [CF,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 42.62, "basis": "Flat sales and input-cost pressure keep earnings roughly at TTM while P/E returns toward its 5y median of 16.1x [RA], the P/E-method base of 42.62; set below the 51.50 blended base because the DCF leg extrapolates near-peak FCF (FCF conversion 132.4% vs 103.4%-105.4% in FY2024-25 [CF,IS])."},
    "bear": {"probability": 0.3, "target_price_12m": 28.23, "basis": "Input-cost pressure flagged on the Q3 2026 call (https://stockanalysis.com/quote/bmv/KIMBER.A/transcripts/653996-q3-2026/) pushes operating margin back toward the FY2021-22 range of 17.5%-17.8% [IS], matching the fact sheet's bear fair value of 28.23."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the mechanical base fair value less a 20% margin of safety (51.50 x 0.8) already sits above the close. What is missing is evidence that the 40.8% gross margin survives the input-cost pressure and flat demand flagged on the Q3 call. A lower price would carry the same unresolved margin question; the FY2026 results showing margins held would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
