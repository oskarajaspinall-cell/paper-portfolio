# Evaluation: Raymond James Financial, Inc. (RJF) — 2026-10-12
## Bear case
This is a fairly priced, steady compounder, not a mispricing. P/E of 13.8x sits at 41% of its own 5y range and P/B 2.4x at 49%, both near their medians [Certain]. Base fair value of $171.36 is only +8.2% above $158.38, and the P/E method alone gives $155.60, below the price [Certain]. Returns are flat, not rising: ROIC 12.2% and ROE 18.4% show no 5y improvement [Certain]. Cash conversion is erratic (FCF margin 67% to -32% to 9.5% TTM) and P/FCF of 21.1x is above its 5y max, so the cash-flow case can't be checked independently [Certain]. Piotroski 4/9 is middling [Certain]. Earnings are rate-sensitive both ways, through cash-sweep NII and the discount rate, and the 10y real yield is up 56bp in 3 months [Likely]. The stock trails SPY by 19.8pp over 12 months, and nothing obvious will close that gap [Certain].
## Bull case
A well-run wealth platform at a peer discount. P/E is 16% and P/B 27% below the peer median [Certain]. ROE has held at 17.0-18.9% for five years, and operating margin has held at 18.8-21.2% through rate and capital-markets cycles [Certain]. Recruiting is strong: advisors bringing $56bn of client assets joined in FY26 YTD, and Q3 revenue grew 16% [Likely]. The reverse DCF implies only 2.8% year-1 growth, which looks undemanding [Likely]. The share count is down 3.82% YoY, and roughly 86% of earnings is returned to shareholders [Likely]. Hiring Jefferies bankers adds to Capital Markets [Likely]. The bull fair value of $201.16 (+27%) is reachable if multiples move back toward peers [Guessing]. Still, these are good-but-priced attributes. The upside to base fair value is small, and no catalyst stands out before Q4 results on Oct 28 [Likely].
## Decision
```json
{
  "ticker": "RJF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steady 18%-ROE wealth platform trading at a peer discount but near the middle of its own 5-year multiple range, with only single-digit upside to base fair value.",
  "rationale": "Quality is stable, not improving, and the valuation is mid-range on its own history (P/E 41%, P/B 49% of 5y range) with +8.2% to base fair value. The peer discount alone is not compelling. Conviction 3 means no position; revisit near the margin-of-safety entry price.",
  "price_at_decision": 158.38,
  "price_date": "2026-10-09",
  "research_note": "research/RJF/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin falls below the 5y low of 18.8%, showing the fee/NII mix is losing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18.8}},
    {"text": "TTM ROE falls below the 5y low of 17.0%, breaking the stable-returns record.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 17.0}},
    {"text": "Share count grows year on year, ending the buyback-driven per-share compounding.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Quarterly net new assets or recruited client assets turn negative year on year in the Q4 FY26 or later results, ending the AUA-growth thesis."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 201.16, "basis": "Recruiting ($56bn recruited assets, 16% Q3 revenue growth per the Q3 transcript) keeps compounding and the peer P/E discount (13.8x vs 16.5x [RA]) narrows, reaching the fact sheet's bull fair value; the macro overlay's neutral tilt does not change this probability (research/RJF/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 171.36, "basis": "ROE holds near 18.4% and P/E stays near its 5y median of 13.6x [RA], so the stock converges on the base fair value (DCF/P-E blend [IS,RA]); the macro overlay is neutral and leaves this unchanged (research/RJF/2026-10-12-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 143.55, "basis": "Higher real yields (10y real yield +56bp/3m per research/RJF/2026-10-12-macro.md) raise the discount rate, or rate cuts compress cash-sweep NII, pushing the price toward the bear fair value, consistent with the P/E-method bear of 139.34 [RA]."}
  },
  "entry_price": 137.09,
  "entry_basis": "valuation file: base 171.36 x 0.8; near the 52-week low of 138.82 [HI], where the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
