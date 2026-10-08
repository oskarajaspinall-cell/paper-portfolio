# Evaluation: Arch Capital Group Ltd. (ACGL) — 2026-10-07

## Bear case
Earnings multiples flatter peak-cycle profits. P/E of 7.4x and EV/EBITDA of 6.4x look cheap only because TTM earnings include unusually strong underwriting; the Insurance segment combined ratio has already worsened to 98.5% in Q2-26 from 93.4% as property pricing softens [Certain]. On book value, the right anchor for an insurer, ACGL is not cheap: P/B of 1.4x sits near its 5y median of 1.5x and only 5% below peers [Certain]. ROE has already eased from 28.4% (FY23) to 19.9% TTM [Certain], and a soft market would push it lower still [Likely]. The business has no moat beyond underwriting skill and capital [Likely]. Q3 results on Oct 27 could show a second weak Insurance quarter [Guessing]. The stock has lagged SPY by 20.4pp over 6 months [Certain], so the market already doubts the cycle, and the catalyst for a re-rating is unclear [Likely].

## Bull case
ACGL is a top-tier underwriter with returns rising over five years: ROIC 12.3% to 17.1% TTM, ROE 16.3% to 19.9% [Certain]. Leverage is low (0.57x site net debt/EBITDA) [Certain] and FCF conversion is 129.0% [Certain], which funds heavy buybacks: shares fell 5.02% YoY, $1.9bn repurchased in H1-26 with $2.2bn left [Certain]. Buying back stock at 1.4x book with a ~20% ROE adds value per share [Likely]. Reinsurance underwriting improved (76.6% combined ratio YTD) and the Mortgage segment is a high-margin offset [Likely]. Higher real yields (US 10y TIPS 2.95%, per the macro overlay) lift investment income on the float, cushioning softer pricing [Likely]. With beta of 0.26 [Certain], it diversifies a portfolio of growth names. P/E is 25% below peers and EV/EBITDA is below its 5y minimum [Certain].

## Decision
```json
{
  "ticker": "ACGL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, buyback-heavy specialty (re)insurer looks cheap on peak-cycle earnings, but on book value it trades near its 5y median while the Insurance segment's underwriting margin is already softening.",
  "rationale": "Quality and capital return are real. But P/B of 1.4x sits near its 5y median and only 5% below peers, so the low P/E mostly reflects peak-cycle earnings as the soft market arrives. A small macro tailwind does not offset this. Good but not compelling: conviction 3, below the buy threshold. Cash is acceptable.",
  "price_at_decision": 94.82,
  "price_date": "2026-10-06",
  "research_note": "research/ACGL/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, showing the softening underwriting cycle has eroded returns to below cost-of-capital levels.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 12%, back below the FY2021 level of 12.3%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition) rises above 1.0x, signalling leverage is funding capital return or covering losses.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Insurance segment combined ratio (10-Q) exceeds 100% for two consecutive quarters, confirming underwriting losses rather than a margin dip; conversely a return below 95% would reopen a buy case."}
  ],
  "scenarios": {
    "bull": {"probability": 0.27, "target_price_12m": 122.0, "basis": "P/B re-rates to its 5y max of 1.8x [RA] from 1.4x as underwriting holds and buybacks (shares -5.02% YoY [ST]) compound book per share; probability raised slightly per the macro overlay's small toward-bull tilt from higher real yields lifting float income (research/ACGL/2026-10-07-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 102.0, "basis": "P/B drifts to its 5y median of 1.5x [RA] as ROE stays near 19.9% TTM [RA] while Insurance-segment softness (combined ratio 98.5% Q2-26, per the note's 10-Q citation) caps any further re-rating."},
    "bear": {"probability": 0.28, "target_price_12m": 81.0, "basis": "Soft market cuts earnings and P/E falls to its 5y minimum of 6.3x [RA] from 7.4x on TTM earnings [IS]; probability trimmed slightly per the macro overlay's small toward-bull tilt (research/ACGL/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
