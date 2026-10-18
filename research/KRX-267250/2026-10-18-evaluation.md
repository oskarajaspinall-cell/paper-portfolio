# Evaluation: HD Hyundai Co., Ltd. (KRX:267250) — 2026-10-18
## Bear case
The cheapness is likely a cyclical peak being priced correctly. TTM operating margin of 13.5% compares with 3.3%-5.6% in FY2021-FY2023, and the 5y trend is driven by the latest year alone [Certain]; refining and construction equipment have little pricing power, so returns can revert when crack spreads or the order cycle turn [Likely]. As a chaebol holdco, net margin is only 3.5% against 13.5% operating, so much of the profit leaks to subsidiary minorities and the holdco discount is structural [Likely]. Altman Z of 1.63 sits in the distress zone [Certain]. The stock is down 39.2% in six months with RSI 23.8 and no identified cause [Certain]; the note rests on the fact sheet alone, with no primary-source check [Certain]. The mechanical fair value is unusable (bear negative, base +892.4%) [Certain]. Q3 results on Oct 30, 2026 may explain the sell-off [Guessing].
## Bull case
On every flow multiple the stock sits at or below its own 5y low and 60-86% below peers: P/E 4.1x, EV/EBITDA 2.8x, P/FCF 1.7x, FCF yield 59.63% [Certain]. The balance sheet has been rebuilt: net debt/EBITDA from 6.59x to 0.14x, Piotroski F-Score 8 [Certain]. ROIC rose from 1.5% to 21.5% TTM and FCF margin turned from -6.9% to 8.4% [Certain]. Shipbuilding, with orderbook scale and LNG/dual-fuel specialisation, has real barriers to entry and USD-denominated contracts [Likely]. Even if margins halve, the valuation leaves a cushion and P/B of 0.3x is only mid-range [Likely]. The RSI 23.8 reading signals a washed-out sell-off that results could reverse [Guessing].
## Decision
```json
{
  "ticker": "KRX:267250",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "HD Hyundai is optically very cheap with a rebuilt balance sheet, but TTM returns look like a cyclical peak inside a structurally discounted holdco, and the unexplained six-month sell-off is unverified by primary sources.",
  "rationale": "Multiples are deep-value, but earnings durability is unproven: margins sit far above their FY2021-FY2023 range, holdco leakage is large, fair value is unusable and no primary source explains the six-month collapse. Good but not compelling; wait for Oct 30 results to show margins holding.",
  "price_at_decision": 157400,
  "price_date": "2026-10-16",
  "research_note": "research/KRX-267250/2026-10-18.md",
  "triggers": [
    {"text": "Q3 2026 results (due Oct 30, 2026) show operating margin holding near the TTM level, confirming earnings are not a one-quarter peak (operating margin staying above the FY2025 8.6% level is the floor)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA rises back above 2x, undoing the deleveraging", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2}},
    {"text": "ROIC falls back under 8%, its FY2022 level", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "A primary filing or IR disclosure identifies the cause of the six-month share-price fall as a business impairment (orderbook cancellation, refining loss, governance event)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 210000, "basis": "Results confirm TTM ROIC of 21.5% [RA] is durable and P/B re-rates toward its 5y max of 0.4x [RA] from 0.3x, still far below the broken mechanical base fair value."},
    "base": {"probability": 0.45, "target_price_12m": 170000, "basis": "Operating margin settles between FY2025 8.6% and TTM 13.5% [IS] and P/E stays near its 5y low end [RA] on the holdco discount; macro overlay tilt is neutral/small, so no probability change (research/KRX-267250/2026-10-18-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 115000, "basis": "Operating margin reverts toward its FY2021-FY2023 range of 3.3%-5.6% [IS], confirming the TTM level was a cyclical peak; the negative mechanical bear fair value is disregarded as a model artefact."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5y lows on EV/EBITDA and EV/Sales [RA]; what is missing is evidence that TTM margins are durable and an explanation of the sell-off, so a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```
