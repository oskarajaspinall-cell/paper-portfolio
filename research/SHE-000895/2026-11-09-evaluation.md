# Evaluation: Henan Shuanghui Investment & Development (SHE:000895) — 2026-11-09
## Bear case
Returns are rolling over: TTM ROIC 20.6% is 3.7pp below its 2-year high of 24.3%, ROCE fell from 32.1% to 28.1% and FCF margin from 10.8% to 6.7% in twelve months [Certain]. The balance sheet moved from net cash to 0.72x net debt/EBITDA, and the cause is unexplained without the Q3 filing [Certain]. Profit rests on the hog/pork spread, so a cyclical input-cost swing can compress margins quickly [Likely]. The mechanical fair value is below the price in all three cases (base 15.17 vs 24.52 close), and the reverse DCF implies 20.2% year-1 revenue growth, demanding for a mature processor [Certain], though the fair value is flagged unreliable. The stock is cheap only modestly: P/E 17.8x sits near its 5y median of 18.0x and P/FCF 22.0x is above the peer median [Certain]. China country risk premium applies [Certain].
## Bull case
A high-return, branded processed-meat leader: ROE 22.5%, ROCE 28.1%, gross margin up from 13.6% (FY2021) to 18.8% TTM, operating margin stable at 11.3% [Certain]. The recent decline in returns and FCF coincides with steady margins and a shift to modest net debt, consistent with capital or working-capital deployment rather than a broken model [Likely]. EV/EBITDA 11.3x sits at the 6% position of its 5y range and P/B 3.8x is below its 5y minimum [Certain]. The P/E method (base 24.91) suggests the price is roughly fair, with a 4.54% FCF yield and flat share count [Certain]. Brand, scale and cold-chain distribution give a narrow moat [Likely]. Beta near zero to the US market diversifies [Likely].
## Decision
```json
{
  "ticker": "SHE:000895",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC, ROCE and FCF margin fell over the last year while gross margin rose to 18.8% TTM and operating margin held at 11.3% [IS-T]; the drop coincides with net debt/EBITDA moving from -0.31x to 0.72x [BS,IS], pointing to capital/working-capital deployment, not lost pricing; cause unconfirmed by a primary source.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Hog/pork input-cost cycle compresses the processing spread while FCF conversion stays weak (80.6% TTM).",
    "veto": null
  },
  "thesis": "A high-return, branded Chinese meat processor with stable margins trades near the bottom of its own EV/EBITDA range, but falling returns and FCF, an unexplained shift to net debt and a price near the P/E-based value leave no compelling margin of safety.",
  "rationale": "Quality is high and margins are steady, but ROIC, ROCE and FCF margin fell over the last year with the cause unconfirmed, P/E sits near its 5y median and the mechanical value is below the price. Good but not compelling: AVOID, with an entry price where valuation would compensate.",
  "price_at_decision": 24.52,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-000895/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15% (20.6% now), showing the return decline is structural rather than capital deployment.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 16% (18.8% now), signalling the hog/pork spread or brand pricing has broken.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 16}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.72x TTM now), showing payouts or capex are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Fiscal-year FCF conversion (FCF/NI, cash flow page) falls below 50% for a full year."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 27.63, "basis": "FCF margin recovers toward its 2-year high of 11.8% [CF-T] and P/E re-rates toward its 5y median-to-upper range [RA], revisiting the 6-month high of 27.63 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 24.91, "basis": "Margins hold at 11.3% operating [IS-T] and the stock trades at the P/E-method base value of 24.91 [valuation file], above the DCF-led blend because the reverse DCF's 20.2% implied growth shows the DCF is too harsh for a stable processor."},
    "bear": {"probability": 0.25, "target_price_12m": 20.0, "basis": "A hog-cycle squeeze extends the ROIC/FCF decline [RA-T] and P/E falls to its 5y low of 16.0x [RA], below the P/E-method bear of 22.09 but above the unreliable DCF-led bear of 7.77."}
  },
  "entry_price": 19.93,
  "entry_basis": "P/E-method base 24.91 x 0.8 [valuation file]: the blended base 15.17 is flagged unreliable (methods disagree 2.4x), so the margin of safety is taken on the P/E method, the one consistent with a stable-margin processor.",
  "replaces": null,
  "replacement_reason": null
}
```
