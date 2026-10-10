# Evaluation: Ralph Lauren Corporation (RL) — 2026-10-10
## Bear case
The quality is real, and the price already pays for it in full. Every multiple sits above its own 5-year maximum: P/E 23.4x vs a 21.1x max, EV/EBITDA 14.6x vs 13.5x, P/B 8.1x vs 7.0x [Certain] (fact sheet RA). RL trades at a +46% P/E premium to peers [Certain]. The reverse DCF implies 20.5% year-1 revenue growth, well above what the business has delivered [Certain]. Even the mechanical bull fair value of $267.39 is 28% below the $371.28 close [Certain]. FCF conversion has fallen from 137% (FY2025) to 79% (FY2026) [Certain], so cash is not keeping pace with reported profit [Likely]. About 59% of revenue is earned outside the US (10-K), so the rising dollar and real yields in the macro overlay add translation and discount-rate pressure [Likely]. The stock also lags SPY by -18.1pp over 6 months [Certain], which leaves room for the multiple to fall back toward its 17.9x median [Guessing].
## Bull case
This is a brand that has visibly improved. ROIC rose from 15.2% to 28.4% over five years, gross margin rose to 70.3% and operating margin to 16.2% [Certain] (fact sheet RA/IS), all while the 10-K describes a promotional retail backdrop [Likely]. Q1 FY2027 revenue grew 13%, and management raised the outlook on more full-price selling [Likely] (transcript via fact sheet). The balance sheet is clean: net debt/EBITDA is 0.67x, Altman Z 6.04 and Piotroski F 7 [Certain]. The share count fell 2.32% YoY [Certain]. A business with structurally higher returns can deserve a multiple above its own history, so the own-history fair value may understate it [Likely]. Short interest of 7.49% gives fuel for a squeeze if Q2 results on Nov 5, 2026 beat [Guessing].
## Decision
```json
{
  "ticker": "RL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality brand with ROIC rising to 28.4% and record margins, but priced above its own 5-year maximum on every major multiple and for 20.5% implied growth, leaving no margin of safety.",
  "rationale": "Quality is clearly improving, but the price already discounts more than continued delivery. Multiples are above their 5-year maximum, the stock trades at a P/E premium to peers, the price is far above even the bull fair value, and macro leans toward the bear case. Good but not compelling, so AVOID; the stock re-enters the watch list nearer its own-history P/E.",
  "price_at_decision": 371.28,
  "price_date": "2026-10-09",
  "research_note": "research/RL/2026-10-10.md",
  "triggers": [
    {"text": "TTM gross margin falls below the FY2023 5-year low of 64.9%, breaking the pricing-power and full-price-mix thesis.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 64.9}},
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year rise from 15.2% to 28.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below the FY2024 level of 12.2%, showing the margin expansion was cyclical rather than structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 421.6, "basis": "Results on Nov 5, 2026 extend the 13% Q1 growth and the raised outlook (note, transcript [OV]); the 23.4x P/E [RA] holds and the stock retests its 52-week high of 421.60 [HI]. Probability is cut by 0.05 for the overlay's small tilt toward bear (research/RL/2026-10-10-macro.md). This is above the mechanical bull of 267.39 because the own-history DCF ignores the step-up in ROIC to 28.4% [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 335.0, "basis": "P/E de-rates from 23.4x to its 5-year maximum of 21.1x [RA] on TTM EPS [IS] while margins hold. This is above the base fair value of 194.98 because the own-history DCF assumes growth the improved-margin business has outrun (fact sheet fair value)."},
    "bear": {"probability": 0.3, "target_price_12m": 284.0, "basis": "P/E reverts to its 5-year median of 17.9x [RA] as FX and real-yield pressure caps growth well below the 20.5% the reverse DCF implies (fact sheet fair value; research/RL/2026-10-10-macro.md, tilt toward bear, small). The probability includes the macro shift. This is still above the mechanical bear of 59.00, because a DCF bear that low ignores the 0.67x leverage and 28.4% ROIC [RA]."}
  },
  "entry_price": 284.0,
  "entry_basis": "P/E back at its 5-year median of 17.9x [RA] on TTM EPS (371.28 x 17.9/23.4). The default base fair value x 0.8 (194.98 x 0.8 = 156) understates a business whose ROIC has nearly doubled [RA]. At the own-history median multiple, this evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
