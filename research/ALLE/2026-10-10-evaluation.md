# Evaluation: Allegion plc (ALLE) — 2026-10-10
## Bear case
The price already exceeds the base fair value: $150.48 vs $142.10, with the DCF leg at $129.74 [Certain] (factsheet, Fair value). Capital efficiency is eroding: ROIC fell from 26.5% (FY21) to 18.8% TTM and ROE from 60.6% to 33.7% [Certain] (RA). Bolt-on M&A such as Overly may keep diluting returns [Likely]. The reverse DCF needs 8.5% year-1 revenue growth, so the market already prices solid growth, while International demand, especially Germany, is weak [Likely] (Q2 2026 transcript, OV). The 10-K warns of private-label, e-commerce and new-entrant competition [Likely] (sec.gov 10-K). Shares fell 15.6% over 12 months and trailed SPY by 31.3pp [Certain] (ST, HI). Q3 results land on Oct 22, so buying now means taking binary event risk on a stock with no margin of safety [Likely].
## Bull case
Specification-driven selling and century-old brands (Schlage, Von Duprin, LCN) create real switching friction [Likely] (10-K). Gross and operating margins are still rising (+3.2pp and +2.6pp over 5 years) and FCF conversion is 101.9% TTM [Certain] (IS, CF). EV/EBITDA (14.0x), P/FCF (19.1x) and P/B (6.0x) are below their 5-year minimums, and P/E of 19.7x is at the 13th percentile of its range [Certain] (RA). The EV/EBITDA fair value is $166.83 [Certain]. Q2 brought double-digit Americas growth and raised guidance, with electronics growing strongly [Likely] (transcript, OV). The balance sheet is conservative at 1.81x net debt/EBITDA [Certain] (RA). Low beta (0.82) and a context-only macro overlay make this a defensive compounder [Likely].
## Decision
```json
{
  "ticker": "ALLE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, specification-moated door-security franchise trading near its 5-year multiple lows, but above its DCF-weighted base fair value while its returns on capital are falling.",
  "rationale": "This is a good business at a fair price, not a compelling one. The price of $150.48 is above the $142.10 base fair value, ROIC has fallen for 5 years, and Q3 results are 12 days away. Low multiples against its own history reflect normalising returns, not mispricing. That leaves conviction at 3, so AVOID and wait for a margin of safety.",
  "price_at_decision": 150.48,
  "price_date": "2026-10-09",
  "research_note": "research/ALLE/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing the specification/brand moat is being competed away rather than normalising off a high base.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 42%, the FY2022 level, showing private-label/e-commerce price competition is biting.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 42}},
    {"text": "TTM FCF margin falls below 12%, under the FY2022 5-year low of 12.1%, showing cash quality is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 168.36, "basis": "Electronics-led growth sustains margin expansion and EV/EBITDA re-rates from 14.0x toward its 5y median of 15.6x [RA], matching the fact sheet's bull fair value of 168.36 and the EV/EBITDA leg of 166.83."},
    "base": {"probability": 0.5, "target_price_12m": 142.1, "basis": "Growth holds near the 8.5% reverse-DCF rate but ROIC keeps drifting down (18.8% TTM [RA]), so the price converges on the DCF-weighted base fair value of 142.10 [factsheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 105.17, "basis": "International weakness (Q2 2026 transcript, OV) and private-label competition flagged in the 10-K compress margins and the multiple, giving the fact sheet's bear fair value of 105.17."}
  },
  "entry_price": 113.68,
  "entry_basis": "valuation file: base 142.10 x 0.8 (20% margin of safety, fact sheet Fair value [IS,BS,CF,RA,ST,HI]); at that price the intact margin and FCF quality would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
