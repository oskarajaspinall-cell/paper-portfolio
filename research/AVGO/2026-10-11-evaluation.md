# Evaluation: Broadcom Inc. (AVGO) — 2026-10-11
## Bear case
At 361.54 the price implies 41.7% year-1 revenue growth on the reverse DCF, and the stock trades 70% above base fair value 108.49. Even bull fair value 265.65 sits 26.5% below the price [Certain]. The AI-ASIC ramp has to keep running for years. Customer concentration makes that fragile: the top five customers are ~40% of revenue per the 10-K [Certain]. Press reports of $50-60bn in AI-chip financing for OpenAI/Anthropic suggest Broadcom is starting to fund its own customers' demand. That could push leverage up from 0.68x net debt/EBITDA [Likely]. FCF margin (-6.4pp over 5y) and conversion are normalising [Certain]. The macro overlay shows real yields up 56bp and HY spreads up 45bp in 3 months. Both hit the discount rate and financing cost of a beta-1.48 stock [Certain]. Relative strength trails SPY by 11-13pp, so the market is already de-rating it [Certain].
## Bull case
This is an elite franchise. ROIC is 30.7% TTM (from 15.6% in FY21), operating margin 48.8%, gross margin 75.5%, Altman Z 13.08 and net debt/EBITDA only 0.68x [Certain]. On relative multiples it is not expensive. P/E of 46.1x sits at the 25th percentile of its 5y range and 24% below the peer median of 60.7x. EV/EBITDA is 40% below peers and P/FCF 46% below [Certain]. The mechanical fair value uses Broadcom's own pre-AI history, so it undercounts a structural shift in custom-XPU and AI-networking demand [Likely]. Multi-year hyperscaler commitments, such as the reported Anthropic deal, give visibility [Guessing]. VMware adds sticky recurring software cash flow [Likely]. The stock is 27% off its 495.00 high and RSI is 50.1, so sentiment is not stretched [Certain].
## Decision
```json
{
  "ticker": "AVGO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Broadcom is a top-tier, rising-ROIC AI-semis and infrastructure-software franchise, but at 361.54 the price already discounts years of hypergrowth (41.7% implied year-1 growth) with concentrated customers, customer-financing leverage risk and a bearish rate backdrop.",
  "rationale": "Quality is exceptional but the price embeds 41.7% growth and sits above even bull fair value. The probability-weighted 12-month value (~332) is below the price. Macro (real yields, spreads) tilts bearish, and AI-chip financing could add leverage. Good but not compelling: conviction 3 means no position. Revisit near P/E at its 5y median.",
  "price_at_decision": 361.54,
  "price_date": "2026-10-09",
  "research_note": "research/AVGO/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20% (FY2025 level 20.4%; TTM 30.7%), signalling AI-ASIC returns are being competed away.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM net margin falls below 25% (FY2021 level 24.5%), showing the AI mix shift is not sticking.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "TTM operating margin falls below 35%, back toward the FY2021/FY2024 levels of 31.6%/30.6%, showing operating leverage from AI has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "Net debt/EBITDA (balance sheet, income statement) rises above 2.5x as the reported AI-chip customer financing comes onto the balance sheet, or the next 10-K shows top-five customer concentration materially above ~40% or the loss of a named hyperscaler."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 476.05, "basis": "P/E re-rates to the 60.7x peer median [RA,P:NVDA,P:QCOM,P:MRVL,P:AMD] on TTM EPS as custom-XPU wins sustain the 48.8% operating margin [IS]. This is above the mechanical bull fair value of 265.65 because own-history assumptions miss the AI ramp."},
    "base": {"probability": 0.40, "target_price_12m": 361.54, "basis": "P/E holds at 46.1x on flat TTM EPS [RA]: growth offsets the de-rating pressure seen in -11.0pp 12m relative strength [HI,SPY-HI]. Probability is cut toward bear for the macro overlay's moderate bear tilt from real yields +56bp and HY spreads +45bp (research/AVGO/2026-10-11-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 195.25, "basis": "AI capex slows or a concentrated customer (top five ~40% of revenue, FY2025 10-K) cuts orders, and EV/EBITDA reverts to its 18.2x 5y median from 33.7x [RA]. This lands between the base (108.49) and bull (265.65) fair values. Probability is raised for the macro overlay's bear tilt and the financing risk (research/AVGO/2026-10-11-macro.md)."}
  },
  "entry_price": 266.64,
  "entry_basis": "P/E back at its 5y median of 34.0x [RA] on TTM EPS (361.54 x 34.0/46.1), in line with the fact sheet's bull fair value of 265.65. The default base fair value of 108.49 x 0.8 is not used because own-history assumptions do not capture the structurally higher AI-era ROIC (30.7%).",
  "replaces": null,
  "replacement_reason": null
}
```
