# Evaluation: Invesco Ltd. (IVZ) — 2026-10-12
## Bear case
GAAP earnings are broken, not just noisy: net margin was negative in FY2023 (-1.7%), FY2025 (-4.4%) and TTM (-0.9%), and ROE is -0.6% TTM [Certain] (factsheet:IS,RA). The cause is not disclosed on stockanalysis.com, so "one-off" is an assumption [Likely]. Quality is eroding: operating margin fell from 25.0% (FY2021) to 18.9% TTM and gross margin -4.9pp, consistent with the fee compression the 10-K discloses [Likely]. ~19% of AUM sits in the single QQQ Trust, so fees track the Nasdaq-100 [Certain] (note). The macro overlay flags real yields up 56bp in 3 months while IVZ rallied +23%/12m on a beta of 1.63, an unpriced downside to AUM and the multiple [Guessing] (macro overlay). With no fair value computable and P/B 1.3x above its 5y max, there is no valuation anchor [Certain] (factsheet).

## Bull case
The cash engine is strong and improving: FCF margin rose from 14.1% (FY2021) to 27.8% TTM, giving a 14.74% FCF yield and P/FCF of 6.8x, below its own 5y min and 64% under the 18.6x peer median [Certain] (factsheet:CF,ST,RA). ROIC recovered to 9.1% TTM from 4.8% in FY2024 [Certain] (factsheet:RA). The Q2 2026 call cited record net inflows, double-digit revenue growth and margin expansion [Likely] (factsheet:OV transcript). Leverage is light at 0.49x net debt/EBITDA, and the share count fell 1.04% YoY [Certain] (factsheet). If net income turns durably positive, the P/FCF and EV/Sales discount (2.0x vs 2.6x peers) could close [Likely].

## Decision
```json
{
  "ticker": "IVZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Invesco's cash generation is cheap at 6.8x P/FCF, but repeated GAAP losses, falling margins and a QQQ-linked, high-beta AUM base exposed to rising real yields leave too little confidence for a core position.",
  "rationale": "Cheap on cash flow, but net margin has been negative in two of the last three fiscal years and TTM, operating margin has fallen 7.4pp in five years, no fair value is computable, and the macro overlay tilts moderately toward the bear case. That is good but not compelling, so no position. Earnings quality, not price, is the obstacle.",
  "price_at_decision": 29.51,
  "price_date": "2026-10-09",
  "research_note": "research/IVZ/2026-10-12.md",
  "triggers": [
    {"text": "Net margin restored durably positive (above 10%), showing the GAAP losses were one-off; would justify re-research for a BUY", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 10}},
    {"text": "Operating margin falls below 15%, under the FY2023 trough: fee compression overwhelming scale", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "ROIC falls back below 5%, undoing the FY2025/TTM recovery", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5}},
    {"text": "Debt/EBITDA rises above 1.5x, showing balance-sheet strain", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 35.0, "basis": "Net margin turns positive and EV/Sales recovers from 2.0x toward its 5y median 2.4x [RA] on the rising FCF margin (27.8% TTM [CF,IS]), near the 33.66 52-week high [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 29.5, "basis": "EV/EBITDA stays near its 9.5x peer-median level [RA] as FCF strength is offset by continued GAAP losses (net margin -0.9% TTM [IS]); no mechanical fair value is computable [factsheet], so the target is held at the current multiple."},
    "bear": {"probability": 0.3, "target_price_12m": 24.0, "basis": "Per the macro overlay (research/IVZ/2026-10-12-macro.md, tilt toward bear, moderate, which raised this probability), higher real yields mark down QQQ-linked AUM and EV/EBITDA compresses to its 5y min 8.4x [RA] on lower EBITDA, near the 6-month low of 23.25 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: P/FCF 6.8x is already below its 5y min [RA] and no base fair value is computable. The obstacle is earnings quality (negative net margin TTM and in FY2023/FY2025 [IS]); a lower price would not change the decision, only durably positive net income would.",
  "replaces": null,
  "replacement_reason": null
}
```
