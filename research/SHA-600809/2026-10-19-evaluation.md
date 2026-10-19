# Evaluation: Shanxi Xinghuacun Fen Wine Factory (SHA:600809) — 2026-10-19
## Bear case
Profitability is falling, not just coming off a peak. TTM operating margin of 38.4% and net margin of 28.4% are both below FY2025's 42.2% and 31.6% [IS], and ROIC has dropped to 55.4% TTM from 110.6% in FY2025 [RA] [Certain]. Cheap multiples sit on falling earnings: a P/E of 14.0x [RA] gets less cheap if profit keeps shrinking [Likely]. Cash quality has weakened: FCF conversion fell from 140.9% in FY2021 to 63.8% in FY2025 [CF,IS], which looks like stock building up in the distributor channel during a baijiu down-cycle [Guessing]. The Piotroski F-score of 3 [ST] confirms the deterioration [Certain]. The mechanical bear fair value of CNY 117.69 is roughly the price, so the price gives no cushion if the slide continues [Certain]. Q3 results are due Oct 29, 2026 [ST] and could show another leg down [Likely].
## Bull case
This is a net-cash franchise (net debt/EBITDA -2.53x TTM [RA]) whose gross margin has held at 73-76% for five years, 73.9% TTM [IS], which points to intact pricing power [Likely]. Every earnings multiple is below its own 5-year minimum: P/E 14.0x vs 17.1x, EV/EBITDA 7.5x vs 11.9x [RA], at a 6.07% FCF yield [ST] [Certain]. It also trades below its peers, with EV/EBITDA 39% under the peer median [RA] [Certain]. The base fair value of CNY 166.26 sits well above the CNY 116.70 close [Certain], and the price implies 8.3% year-1 revenue growth fading to terminal, which is not demanding for a brand at this level of returns [Likely]. FCF margin recovered to 24.1% TTM from 20.2% in FY2025 [CF,IS] [Certain]. If Q3 shows margins stabilising, the stock could re-rate sharply off a 52-week fall of -39.6% [ST] [Guessing].
## Decision
```json
{
  "ticker": "SHA:600809",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return baijiu brand trades below its own 5-year minimum multiples, but margins, returns and cash conversion are still falling into a down-cycle, so the low multiples rest on earnings that have not yet bottomed.",
  "rationale": "Cheap and net cash, but TTM margins and ROIC are still falling, the F-score is weak and Q3 results come in ten days. The bear fair value equals the price, so the price offers no margin of safety if earnings fall further. This is good but not compelling: conviction 3 means AVOID until the results show margins stabilising.",
  "price_at_decision": 116.70,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600809/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 30% (55.4% TTM now), showing the pricing-power moat is eroding rather than normalising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 68% (73.9% TTM now), showing discounting to clear channel inventory.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "TTM net margin falls below 20% (28.4% TTM now), showing the operating-leverage gains are reversing.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 20}},
    {"text": "FCF conversion (FCF/NI) stays below 60% for two consecutive fiscal years, showing reported profit is no longer backed by cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 166.26, "basis": "Q3 shows margins stabilising and the stock re-rates to the blended base fair value of 166.26 [IS,BS,CF,RA,ST], still below its 5y median EV/EBITDA of 20.0x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 119.90, "basis": "Margins keep easing but stay well above the trigger levels, and the price tracks the DCF base of 119.90 [IS,BS,CF,RA,ST] with no re-rating while ROIC keeps falling [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 93.83, "basis": "The channel-inventory down-cycle deepens (FCF conversion 63.8% in FY2025 [CF,IS], F-score 3 [ST]) and the price falls to the DCF bear of 93.83 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the close is already below base fair value 166.26 x 0.8, and the bear value matches the price. The obstacle is the still-falling margin and ROIC trend, so a lower price would not change the decision; evidence that margins have stabilised in the Oct 29 results would.",
  "replaces": null,
  "replacement_reason": null
}
```
