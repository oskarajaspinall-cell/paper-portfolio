# Evaluation: Banco Santander (Brasil) (BVMF:SANB11) — 2026-10-28
## Bear case
Why it fell: no single event. The note found only a technical "oversold" headline. It points to falling profitability, credit stress and high rates, and the Q3 call on 28 Oct confirmed all three [Likely]. ROE has fallen from 14.7% (FY2021) to 11.2% TTM, and net margin from 33.1% to 28.7% [Certain]. At about 11% ROE the bank earns below its cost of equity (risk-free 5.00% plus a 3.0% country premium), so 0.8x book is fair rather than cheap [Likely]. Q3 brought higher provisions in agribusiness, unsecured and card lending, one-off wholesale cases and pressure on client NII. The consumer-finance sale and the mix shift toward high-income clients structurally lower spreads [Likely]. The dividend-discount cross-check is 18.22, far below the price, so the fair-value upside depends on an ROE recovery that management has not delivered [Certain]. Piotroski F is 4 [Certain]. Results are still being priced [Certain].

## Bull case
P/E of 6.7x sits at the bottom of its 5y range (6.6x / 7.3x / 12.7x) and below the 7.8x peer median. P/B of 0.8x compares with a 1.0x 5y median and a 1.5x peer median [Certain]. Base fair value is 34.27 and the reverse DCF implies -8.4% revenue growth, which is a deep-recession price [Certain]. Q3 recurring ROE of 11.9% held near the TTM level. Efficiency is improving, short-term delinquency is falling and newer cohorts look better [Likely]. Management expects NII to improve in 2027 [Likely]. The share count is flat at 0.22% YoY, so capital is not being rebuilt through dilution [Certain]. RSI of 21.5 marks capitulation-level selling [Certain]. If ROE returns toward its FY2022 13.2% level, the stock could re-rate toward book or above [Guessing].

## Decision
```json
{
  "ticker": "BVMF:SANB11",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A sub-scale-return Brazilian bank whose ROE has slid to 11.2%, below its cost of equity, is cheap on book for a reason, and Q3 results confirm deterioration rather than a turn.",
  "rationale": "The price reached our entry level because fundamentals worsened: Q3 showed higher provisions, NII pressure and ROE below target. Cheapness is matched by sub-cost-of-equity returns, and the dividend-discount cross-check sits far below the price. Good value optics, but not compelling; wait for evidence that ROE is stabilising before buying.",
  "price_at_decision": 25.87,
  "price_date": "2026-10-27",
  "research_note": "research/BVMF-SANB11/2026-10-28.md",
  "triggers": [
    {"text": "TTM ROE (statistics) rises above 13.2%, back to its FY2022 level, showing profitability is recovering above the cost of equity; this would make it a BUY candidate.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13.2}},
    {"text": "TTM net margin (statistics) recovers above 33.1%, the FY2021 level, showing credit costs have normalised.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 33.1}},
    {"text": "A subsequent quarterly earnings release confirms NII growth in 2027 alongside falling provisions, validating management's guided improvement."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 34.27, "basis": "ROE recovers as management's 2027 NII improvement and better newer cohorts come through (Q3 transcript /quote/bvmf/SANB11/transcripts/659705-q3-2026/), lifting the stock to the mechanical base fair value of 34.27 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 25.87, "basis": "ROE stays near 11.2% TTM [RA], below the cost of equity, so P/B holds near 0.8x [RA]; below the mechanical base of 34.27, which assumes an ROE recovery that the dividend-discount check of 18.22 does not support [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.35, "target_price_12m": 21.2, "basis": "Agribusiness, unsecured and card provisions keep rising and NII pressure persists (Q3 transcript /quote/bvmf/SANB11/transcripts/659705-q3-2026/), taking value to the P/B + ROE bear case of 21.20 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: quality is deteriorating (ROE and net margin falling, Q3 provisions rising), and the stock already trades below the 27.13 entry level set earlier without becoming a BUY. A lower price would not change the decision; evidence that ROE is stabilising (the triggers) would.",
  "replaces": null,
  "replacement_reason": null
}
```
