# Evaluation: Advanced Micro Devices, Inc. (AMD) — 2026-11-16
## Bear case
The price already discounts several times today's earnings. EV/EBITDA 78.0x and EV/Sales 19.1x sit above their own 5y maxima and far above peers; the FCF yield is 0.81% [Certain]. Even the EV/EBITDA method's base of 134.56 is far below the 534.06 close [Certain]. The price is 25.8% above its 200-day average after a +107.7% year with beta 2.54: if AI-accelerator growth slows, an extended stock like this de-rates hard, and the macro overlay tilts toward bear on rising real yields (10y TIPS +0.47pp over 3m) [Likely]. FCF margin is 7.4pp below its 2-year high and conversion slipped to 92.6%, while the 10-Q adds capacity purchase commitments, cloud compute commitments and customer warrants, i.e. some demand may be bought [Likely]. Dilution of 1.36% YoY persists, Nvidia's software ecosystem remains the barrier in GPUs, and China export rules add unquantified risk [Likely].
## Bull case
The business is working now. On a rolling basis ROIC rose from 5.2% to 12.8%, operating margin from 9.4% to 17.8% and gross margin to 56.0%, all at 2-year highs [Certain]; the 5-year "falling" label reflects the FY2022-23 trough, not the current direction [Certain]. Q3 revenue grew 45% on Data Center and the MI450 launch [company-reported] (https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm). The balance sheet is net cash (net debt/EBITDA -0.59x), Piotroski 7, Altman Z 13.65 [Certain]. CPU share against Intel looks durable [Likely], and the TensorWave–OpenAI agreement and World Labs deal add AI ecosystem depth [Likely]. P/E 111.4x sits only at 25% of its 5y range, and the recent fall came with a sector-wide sell-off on Nvidia leadership news rather than AMD-specific results [Likely]. If earnings keep compounding, the multiple compresses through growth rather than price [Guessing].
## Decision
```json
{
  "ticker": "AMD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 5-year ROIC/ROCE/operating-margin declines come from the FY2022-23 trough; the rolling 12 months show ROIC 5.2% -> 12.8% and operating margin 9.4% -> 17.8% at 2-year highs [RA-T, IS-T]. The FCF-margin dip from its 22.9% high coincides with new capacity and compute commitments in the Q3 10-Q (https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm), i.e. investment, not lost share.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "At EV/EBITDA above its 5y max and a 0.81% FCF yield, any slowdown in AI-accelerator growth (Nvidia ecosystem, bought demand via warrants/commitments) or a rise in real yields would de-rate the stock sharply with no change in earnings.",
    "veto": null
  },
  "thesis": "A net-cash chip designer whose rolling returns and margins are recovering fast on Data Center AI demand, but whose price already discounts several times today's earnings and cash flow.",
  "rationale": "Fundamentals are improving and the balance sheet is strong, but the valuation sits above its own 5y range on EV/EBITDA and EV/Sales with an FCF yield below the trend-strength floor, so the scorecard gives no valuation points and conviction 2. Good business, not compelling at this price: AVOID.",
  "price_at_decision": 534.06,
  "price_date": "2026-11-13",
  "research_note": "research/AMD/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 50%, reversing the five-year rise to 56.0% and signalling GPU pricing pressure from Nvidia.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "TTM operating margin falls below 12%, giving up most of the rolling recovery from 9.4% to 17.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls back below 8%, showing the returns recovery has stalled.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Data Center segment revenue declines year on year in a 10-Q, or net debt/EBITDA on the ratios page turns positive (net cash gone)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 658.52, "basis": "Rolling margin and ROIC gains continue and Data Center growth holds, taking the price back to its 52-week high of 658.52 [HI] on earnings growth rather than a higher multiple."},
    "base": {"probability": 0.4, "target_price_12m": 502.6, "basis": "Earnings keep growing but the EV/EBITDA multiple, above its 5y max of 61.0x [RA], drifts lower, holding the price near the October swing low of 502.60 [HI]; the macro overlay's moderate bear tilt (research/AMD/2026-11-16-macro.md) shifts weight from bull to bear."},
    "bear": {"probability": 0.35, "target_price_12m": 393.36, "basis": "Real yields rise or AI spending doubts persist and the multiple compresses by a third or more as the macro overlay's bear case describes (research/AMD/2026-11-16-macro.md), back to the 6-month low of 393.36 [HI]; still far above the unreliable mechanical fair value base of 66.47 because the model ignores the improved business."}
  },
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```
