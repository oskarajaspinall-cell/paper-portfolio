# Evaluation: Bank of Chengdu Co., Ltd. (SHA:601838) — 2026-10-18

## Bear case
Returns are fading: ROE has slid from 17.7% (FY2022) to 14.2% TTM [RA] even as net margin rose to 62.5% [IS], which points to NIM compression or balance-sheet growth outrunning earnings [Likely]. The stock is not cheap on its own history: 6.1x P/E sits above its 5y max of 5.8x and P/B of 0.8x is a premium to the 0.7x peer median despite the falling ROE [RA] [Certain]. The mechanical fair value rests on P/B + ROE and FCFE, but bank FCF is noise (FCF margin swung from -456.9% to 346.1% [CF,IS]) and the dividend-discount method puts value at 8.94-11.12 CNY, below the price [Certain]. Asset quality (NPLs, provisioning, capital ratios) and dividend payout are [data unavailable], so the key bank risks, Sichuan local-government and property credit, cannot be tested [Likely]. Piotroski F-Score is only 4 [ST] [Certain].

## Bull case
A 14.2% ROE bank at 0.8x book and 6.1x earnings [RA] is optically cheap, and the reverse DCF implies -11.0% revenue growth in year 1, a pessimistic assumption for a bank still growing profits [Likely]. Even the bear mechanical fair value of 27.44 CNY sits above the 19.09 CNY close [Certain]. Net margin has risen five years running to 62.5% [IS], the share count fell 0.35% YoY [ST], and the regional deposit franchise carries licensing barriers [Likely]. The 0.11 beta [ST] adds diversification to the portfolio [Certain]. The price trend is constructive: above both moving averages with +10.5% 6-month momentum [HI] [Certain].

## Decision
```json
{
  "ticker": "SHA:601838",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A regional Chinese bank on a modest P/E and P/B whose ROE is declining and whose asset quality cannot be verified from available data, so the apparent discount to mechanical fair value is not a reliable margin of safety.",
  "rationale": "Valuation is only fair against its own history (P/E above the 5y max, P/B mid-range and above peers) while ROE trends down. Fair value leans on bank FCF that is noise, and DDM sits below the price. Without NPL or capital data the credit risk cannot be sized. Good but not compelling: AVOID, keep cash.",
  "price_at_decision": 19.09,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601838/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE recovers above 16% (the FY2024 level), showing the five-year decline in returns has reversed rather than become structural.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 16}},
    {"text": "TTM ROE falls below 12%, confirming the return decline is structural rather than cyclical.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM net margin falls below 55%, signalling credit costs or operating expense outgrowing revenue.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 55}},
    {"text": "Shares outstanding rise more than 5% year on year, indicating a dilutive capital raise to rebuild regulatory capital.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 22.5, "basis": "P/B re-rates to its 5y max of 0.9x [RA] on modest book growth as ROE stabilises near 14.2% [RA]; still below the mechanical bear fair value of 27.44 because the stock has never sustained a P/B above 0.9x in five years [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 19.8, "basis": "P/B holds near its 5y median of 0.8x [RA] with retained earnings adding modestly to book while ROE drifts lower; the mechanical base of 32.65 is discounted because its FCFE leg uses bank cash flow that swings from -456.9% to 346.1% of revenue [CF,IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 14.3, "basis": "P/B falls back to its 5y min of 0.6x [RA] as ROE continues its decline from 17.7% and regional credit costs rise, closer to the dividend-discount value of 8.94-11.12 CNY [IS,BS,CF,RA,ST]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the mechanical base fair value is already well above the close, yet the falling ROE trend and unavailable asset-quality and capital data mean a lower price alone would not lift conviction to 4; a re-look needs ROE stabilisation (trigger) instead.",
  "replaces": null,
  "replacement_reason": null
}
```
