# Evaluation: BOK Financial Corporation (BOKF) — 2026-11-08
## Bear case
This is an adequate bank, not a compounder. ROE fell from 11.6% (FY2021) to 10.1% (FY2025); the TTM 11.2% is a recovery, not a new level [Certain]. The best-fit valuation method, P/B + ROE, gives a base of 115.70, below the 129.48 close. P/B of 1.3x sits at its 5y median, so there is no re-rating cushion [Certain]. The Direction change line shows FCF margin falling from 64.8% to 31.4% over the last year. For a bank this is mostly trading-asset and working-capital noise, but it means the FCFE leg that lifts the blended base to 136.71 rests on unreliable cash flows [Likely]. The macro overlay tilts toward bear (small): HY spreads are up 0.77pp and VIX is 28.18, and a credit surprise would hit provisions and P/B together [Likely]. Short interest of 14.13% is rising, and a controlling holder with 63.62% limits minority influence [Certain].
## Bull case
Operations are improving. Q3 EPS was $2.64 against consensus, loan growth was 11.5%, NIM rose 9 bps to 3.0%, and provisions are guided below $10M [Likely] (transcript). Capital returns are real: the share count is down 4.73% YoY [Certain] and the quarterly dividend was raised 24% to 78c [Likely]. P/E of 11.7x is below its 5y median of 13.1x and the peer median of 12.7x [Certain], and the reverse DCF implies -4.3% revenue growth while guidance is mid-single-digit growth [Likely]. Beta is 0.78. A move in P/B toward the 1.4x peer level would reach roughly the bull fair value of 152.99 [Guessing].
## Decision
```json
{
  "ticker": "BOKF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-run regional bank with improving loan growth and NIM and strong buybacks trades at its own median P/B with best-method fair value below the price, so the skew is balanced rather than compelling.",
  "rationale": "Fundamentals are healthy and capital returns strong, but ROE has not compounded, P/B sits at its 5y median, the best valuation method is below the price, and the higher blended base relies on noisy bank FCF. The macro tilt is toward bear. Good but not compelling: AVOID, with an entry price on margin of safety.",
  "price_at_decision": 129.48,
  "price_date": "2026-11-06",
  "research_note": "research/BOKF/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 9.0%, under the FY2024 low of 9.8%, showing loan growth is not earning its cost of capital.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9.0}},
    {"text": "TTM net margin falls below 24%, under the FY2024 low of 25.8%, signalling deposit-cost or credit pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 24}},
    {"text": "Shares outstanding change YoY turns above +2%, i.e. buybacks reverse into dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}},
    {"text": "A quarterly release shows provision expense above the sub-$10M FY26 guide or NIM falling quarter on quarter."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 152.99, "basis": "Spreads retrace, NIM expands from 3.0% and P/B moves toward the 1.4x peer median [RA]: the mechanical bull fair value of 152.99 [fact sheet Fair value]; probability trimmed for the macro overlay's small toward-bear tilt (research/BOKF/2026-11-08-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 132.0, "basis": "P/B holds near its 5y median 1.3x [RA] while ROE stays around TTM 11.2% [RA]; below the mechanical base of 136.71 because the FCFE leg extrapolates bank FCF that fell from 64.8% to 31.4% of revenue in a year [CF-T], and above the P/B + ROE base of 115.70 because of buybacks of 4.73% [ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 107.46, "basis": "HY spreads widen and provisions rise above the guide, compressing P/B toward its 1.1x 5y low [RA]: the P/B + ROE bear value of 107.46 [fact sheet Fair value]; probability raised for the macro overlay's small toward-bear tilt (research/BOKF/2026-11-08-macro.md)."}
  },
  "entry_price": 109.37,
  "entry_basis": "valuation file: base 136.71 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
