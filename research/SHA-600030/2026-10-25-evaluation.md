# Evaluation: CITIC Securities Company Limited (SHA:600030) — 2026-10-25
## Bear case
TTM ROE of 12.2% matches FY2021's 12.0%, the top of the 5y range; it does not show a structurally better business [Likely]. That makes the 9.8x P/E, below the 5y minimum of 13.4x, a peak-earnings multiple, not a bargain [Likely]. ROIC is only 3.6% and Piotroski F is 5 [Certain]. FCF swings from -71.7% to 317.5% of revenue, so the FCFE-based fair value (base 28.27) stands on noisy inputs, and the 39.70% FCF yield means nothing [Certain]. Versus peers the stock trades at a premium (P/E 8.5x and P/B 0.8x peer medians) [Certain]. If A-share turnover fades, a return to FY2023's 7.7% ROE points to the bear value of 18.51 [Likely]. The price is below both moving averages and 12-month relative strength vs SPY is -26.6pp, and Q3 results land on 2026-10-26, so the event risk runs both ways [Certain].

## Bull case
CITIC is China's largest listed broker, with scale and licences that protect its share [Likely]. Operating margin rose to 59.1% TTM from 42.1% in FY2023, and management reported record 2025 revenue and profit with growth in wealth management, investment banking and international business [Likely]. P/B of 1.0x is at the bottom of its 1.0x–1.5x 5y range [Certain]. The reverse DCF implies only 0.5% year-1 revenue growth, a low bar [Certain]. If activity holds, P/E moving back toward its 14.3x median points toward the bull value of 31.13 [Guessing]. Beta of 0.70 keeps market risk low [Certain]. Still, the upside to the base value is small next to the downside, and that is not compelling for a cyclical [Likely].

## Decision
```json
{
  "ticker": "SHA:600030",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale franchise trading at 1.0x book, but its earnings sit near a cyclical peak, so the low P/E overstates value and the upside to base fair value is too small for the downside.",
  "rationale": "ROE is back at its 5y high, not structurally higher. FCF-based fair value is unreliable for a broker. P/B is 1.0x and the P/E sits at a premium to peers. The upside to base value is modest next to a bear case of 18.51. That is good but not compelling, so AVOID; a lower price would raise conviction.",
  "price_at_decision": 25.45,
  "price_date": "2026-10-23",
  "research_note": "research/SHA-600030/2026-10-25.md",
  "triggers": [
    {"text": "ROE falls below 8% TTM (ratios/statistics page): earnings power fading back to the FY2023 trough", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "Operating margin falls below 45% TTM: the margin gain since FY2023 reverses", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "Net margin falls below 35% TTM", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 31.13, "basis": "Activity holds and ROE stays near 12.2% TTM [RA], so the market re-rates toward the mechanical bull fair value of 31.13 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 25.45, "basis": "Earnings stay near peak but the market keeps pricing them as cyclical, holding P/B around 1.0x [RA]; this sits below the 28.27 base fair value because the FCFE input is distorted by client and trading flows (FCF margin -71.7% to 317.5% [CF,IS])."},
    "bear": {"probability": 0.25, "target_price_12m": 18.51, "basis": "Turnover fades and ROE reverts toward FY2023's 7.7% [RA], in line with the mechanical bear fair value of 18.51 [fact sheet Fair value]."}
  },
  "entry_price": 22.62,
  "entry_basis": "valuation file: base 28.27 x 0.8; at that level the stock would trade below 1.0x book (the bottom of its 5y P/B range [RA]), which compensates for peak-cycle earnings.",
  "replaces": null,
  "replacement_reason": null
}
```
