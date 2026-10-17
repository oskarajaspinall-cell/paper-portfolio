# Evaluation: Giant Network Group Co., Ltd. (SHE:002558) — 2026-10-17
## Bear case
Profits look like they peaked on one title. Operating margin jumped from a 24.2-28.3% FY2021-24 band to 46.9% TTM, which fits one or two recent hits carrying sales, not a structural improvement [Likely] (IS). Chinese gaming has low switching costs and needs a steady run of new hits [Likely]. The market is pricing a fade: the stock is down 47.6% over 12 months and 30.8% over three months, trades 35.1% below its 200-day average and is near its 52-week low of 20.86 [Certain] (ST, HI). We have no news, guidance or title-level data that explains the fall [Certain] (note §6). Q3 results land on Oct 30 [Certain] (ST). The mechanical bear fair value is 10.97, and the DCF bear is 0.23 [Certain] (fair value). Shares grew 3.20% YoY [Certain] (ST). We already hold NetEase, a China gaming name, so this adds concentrated exposure to the same theme [Certain] (state).

## Bull case
The balance sheet is strong. Net cash exceeds EBITDA every year, Altman Z is 13.48 and Piotroski F is 7 [Certain] (RA, ST). Cash generation is real: TTM FCF margin is 52.1% and FCF conversion is 134.8%, giving a 10.61% FCF yield [Certain] (CF, ST). Every multiple except P/B is below its own 5-year minimum: P/E is 12.7x against a 16.5x low and EV/EBITDA 8.5x against 21.5x [Certain] (RA). The reverse DCF already assumes revenue falls 4.9% in year 1, so the price allows for a partial fade [Certain] (fair value). If even part of the margin step-up holds, base fair value of 40.28 is well above the price [Likely]. Beta of 0.64 means macro is a background factor, not a driver [Certain] (ST; macro overlay `context`).

## Decision
```json
{
  "ticker": "SHE:002558",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 52%-FCF-margin Chinese game developer trading below its own 5-year minimum multiples, but its earnings surge rests on hit-driven content whose durability the sharp, unexplained price collapse calls into question.",
  "rationale": "Cheap on every own-history multiple with an excellent balance sheet, but the margin surge looks hit-driven, the decline is unexplained and Q3 results are two weeks away. It would also add to existing China-gaming exposure. Good but not compelling: AVOID until results show revenue durability.",
  "price_at_decision": 20.95,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002558/2026-10-17.md",
  "triggers": [
    {"text": "TTM gross margin falls below 85%, below the FY2021-24 band, showing the high-margin title mix is fading.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 85}},
    {"text": "TTM operating margin falls back below 28.3%, the top of the FY2021-24 band, showing the margin surge was a single-title spike.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.3}},
    {"text": "TTM ROIC falls back to 8.3% or lower, the FY2021-24 range, erasing the FY2025/TTM improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.3}},
    {"text": "Quarterly revenue (income statement) declines year on year in the Oct 30 Q3 report and the following quarter, confirming the hit cycle is rolling over (a growth result would instead support re-research toward conviction 4)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 40.28, "basis": "The TTM margin step-up (operating margin 46.9% [IS]) largely holds and the price re-rates to the blended base fair value of 40.28 [fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 20.95, "basis": "Revenue fades about as fast as the reverse DCF already implies (-4.9% in year 1 [fair value]), so the price stays near the current 20.95 despite the 10.61% FCF yield [ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 10.97, "basis": "The hit title fades and operating margin reverts to the FY2021-24 band of 24.2-28.3% [IS], in line with the mechanical bear fair value of 10.97 [fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every own-history minimum multiple. Conviction 4 needs evidence that revenue and margins are durable (the Oct 30 Q3 results and an explanation for the fall), so a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
