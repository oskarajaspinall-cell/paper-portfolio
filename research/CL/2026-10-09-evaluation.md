# Evaluation: Colgate-Palmolive Company (CL) — 2026-10-09
## Bear case
At $88.10 the price sits above every fair-value case: base $73.62 (-16.4%) and even bull $78.65 (-10.7%) [Certain]. The reverse DCF implies 7.6% year-1 revenue growth, against Q2 organic growth of 2.4% and North America shipments that are shrinking [Likely]. P/E of 34.8x is at the 81st percentile of its 5y range and +76% above peers [Certain]. Operating margin (-1.1pp) and net margin (-2.0pp) have drifted lower over five years [Certain]. The macro overlay flags real yields up 61bp in 3m and a stronger dollar. Both pressure a bond-proxy multiple and translated international EPS [Likely]. A brand divestiture is unconfirmed, and nothing suggests it adds value [Guessing]. The stock has also lagged SPY by 12.1pp over 6m [Certain], so there is no momentum support either.

## Bull case
This is a top-tier franchise. ROIC is 45.6% and rising (+5.5pp over 5y), gross margin is steady around 60%, and net debt/EBITDA is only 1.29x [Certain]. Cash quality is better than reported earnings: the FCF margin is 18.3% and FCF/NI is 189.3% [Certain], so P/FCF of 18.2x sits near its 5y low (17.5x) and 6% below peers, with a 5.48% FCF yield [Certain]. The depressed TTM net margin (9.7% vs 14.4% in FY2024) suggests the P/E overstates how expensive the stock is [Likely]. Buybacks cut the share count 1.49% YoY [Certain]. Q2 gross margin expanded 100bps, which points to a pricing-power moat that is intact [Likely]. Selling mass-market personal-care brands could shift the mix toward oral care and Hill's [Guessing].

## Decision
```json
{
  "ticker": "CL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 45.6%-ROIC, 18.3%-FCF-margin staples franchise with an intact moat, but the price already exceeds its bull-case fair value and implies 7.6% growth while North America is shrinking.",
  "rationale": "Quality is excellent and cash conversion makes P/FCF look reasonable, but the price is above all three fair-value cases and implies growth well beyond the 2.4% organic rate. Rising real yields and the dollar tilt the risks to the downside. Good but not compelling, so we AVOID and set an entry price.",
  "price_at_decision": 88.10,
  "price_date": "2026-10-08",
  "research_note": "research/CL/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 58% (FY2022-23 range), undoing the pricing-power thesis.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "TTM ROIC falls below 35%, back toward the FY2021-22 levels, showing returns are no longer structurally rising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 15%, under the FY2023 level of 15.6%, showing the cash-conversion support for the valuation was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "North America organic sales growth (quarterly earnings release) stays negative for two more quarters after Q3 2026, showing the H2 2026 reset failed."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 100.0, "basis": "The North America reset works and P/FCF re-rates from 18.2x toward its 5y median of 21.6x [RA] on an 18.3% FCF margin [CF,IS]; this sits above the bull fair value of 78.65 because the DCF/P/E blend ignores FCF/NI of 189.3% [CF,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 84.0, "basis": "Roughly flat organic growth and a slight multiple de-rating on EV/EBITDA of 15.3x vs a 16.8x 5y median [RA]; moderately tilted down per the macro overlay (research/CL/2026-10-09-macro.md: real yields +61bp/3m). Kept above the 73.62 base fair value because FCF quality and buybacks (-1.49% shares [ST]) support the cash yield."},
    "bear": {"probability": 0.3, "target_price_12m": 68.0, "basis": "P/E compresses toward its 5y minimum of 25.7x [RA] (P/E-method bear 65.15 [fact sheet]) as real yields and the dollar keep rising (research/CL/2026-10-09-macro.md, macro_tilt toward bear, moderate) and North America stays weak (Q2 2026 transcript)."}
  },
  "entry_price": 58.90,
  "entry_basis": "valuation file: base 73.62 x 0.8; at that level the 5.48%-plus FCF yield [ST] and 45.6% ROIC [RA] would justify conviction 4 on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```
