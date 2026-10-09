# Evaluation: Boston Scientific Corporation (BSX) — 2026-10-09
## Bear case
The 56.2% 12-month fall and a P/E of 16.8x, below the 5y minimum of 48.8x, point to a structural growth reset, not a one-off [Likely]. At the Sept 10 conference management said WATCHMAN "faces market headwinds and new competition" while EP growth "moderates". Those two franchises carried the premium [Certain]. The cyberattack means Q3 and FY2026 guidance will be missed. Q3 results land on Oct 28, 2026, so a guidance reset is still ahead [Certain]. TTM net margin jumped to 17.5% from 14.4% while FCF conversion fell to 98.7%, so the 16.8x P/E may be flattered [Likely]. Short interest rose 68.4% in a month and the 50-day average sits 23.2% below the 200-day, so sellers are not done [Certain]. The fact sheet's bear fair value of $31.04 is -26.2% [Certain]. Nothing in the research measures how much WATCHMAN share is being lost [Certain].
## Bull case
The fundamentals are still improving. ROIC rose from 7.4% to 11.2%, operating margin from 15.3% to 20.5% and FCF margin from 11.1% to 17.3% (FY2021 to TTM) [Certain]. The balance sheet is sound: net debt/EBITDA 2.12x, Altman Z 4.80, Piotroski F 7 [Certain]. At a 6.04% FCF yield and EV/EBITDA of 12.6x, 23% below the peer median of 16.5x, the price implies only 3.8% year-1 revenue growth [Certain]. Operations had "substantially recovered" by the Sept 8 8-K, and management sees no long-term financial impact from the cyberattack [Certain]. If WATCHMAN and EP hold up, the DCF base of $54.18 to the blended $58.24 is 29-39% upside [Likely]. Beta is 0.58 and procedure demand does not depend on the economy [Certain].
## Decision
```json
{
  "ticker": "BSX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A medtech with rising returns trades at 16.8x earnings and a 6% FCF yield, but the de-rating reflects management-confirmed WATCHMAN competition and EP moderation that the research cannot yet quantify.",
  "rationale": "Cheap on every multiple with improving returns, but the key swing factor (WATCHMAN and EP durability) is unmeasured. A guidance reset is due at the Oct 28 results. With a 40% bear weight at -26%, the case is good but not compelling. That is conviction 3, below the buy threshold, so we hold cash and reassess after Q3.",
  "price_at_decision": 42.04,
  "price_date": "2026-10-08",
  "research_note": "research/BSX/2026-10-09.md",
  "triggers": [
    {"text": "Q3 2026 or later earnings release shows WATCHMAN and electrophysiology net sales both growing year-on-year despite new competition, evidencing the moat holds (would raise conviction).", "check": null},
    {"text": "TTM operating margin falls below 17% (FY2023 level), showing cyberattack and competitive costs are not normalising.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls back below 8% (FY2024 level), undoing the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 82.57, "basis": "WATCHMAN/EP prove resilient and growth re-accelerates, supporting the fact sheet's DCF bull of $82.57 [IS,CF,RA]; below the $113.49 blended bull because the P/E bull ($175.34) assumes a return to the 48.8x-103.2x own-history P/E range [RA] that management's competition commentary makes unlikely."},
    "base": {"probability": 0.4, "target_price_12m": 54.18, "basis": "Cyberattack disruption proves transitory (8-K, https://www.sec.gov/Archives/edgar/data/885725/000088572526000059/bsx-20260907.htm) and margins hold near the TTM 20.5% [IS]: DCF base $54.18, below the $58.24 blend because the P/E leg anchors on a pre-de-rating multiple history [RA]."},
    "bear": {"probability": 0.4, "target_price_12m": 31.04, "basis": "WATCHMAN competition and EP moderation flagged at the Wells Fargo conference (https://stockanalysis.com/stocks/bsx/transcripts/730622-wells-fargo-21st-annual-healthcare-conference/) prove structural and Q3 resets guidance, taking the price to the fact sheet bear fair value of $31.04."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
