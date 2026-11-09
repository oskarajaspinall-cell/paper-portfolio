# Evaluation: Central Japan Railway Company (TYO:9022) — 2026-11-09
## Bear case
Returns are low for the capital tied up: ROIC 6.0% TTM [RA] sits well below any reasonable cost of capital, so the high 40.4% operating margin [IS] does not translate into value creation [Certain]. The recovery from FY2022 has plateaued: ROIC slipped from 6.5% to 6.0% over the last year and operating margin is flat [RA-T, IS-T] [Certain]. The **Direction change** in FCF margin (14.9% -> 10.1% over 12 months [CF-T]) is most plausibly Chuo Shinkansen capex, which is multi-year, so weak FCF conversion (37.9% of net income) is likely to persist rather than reverse [Guessing]. Leverage is the weak point: net debt/EBITDA 4.25x and Altman Z 1.58 [ST], with deleveraging stalled [Certain]. The fair value is unreliable (bear DCF negative), and the reverse DCF already implies 7.5% year-1 revenue growth, demanding for a mature line [Likely]. RSI 68.5 after a run off the June low [Likely].
## Bull case
The Tokaido Shinkansen is a near-monopoly trunk corridor with no practical substitute at scale, giving a durable moat and 40.4% operating margins [IS] [Likely]. The stock is cheap on earnings: P/E 7.7x sits at the 19th percentile of its 5y range and below the 13.5x peer median, and EV/EBITDA 8.3x is at the 3rd percentile of its own range [RA] [Certain]. The share count is falling 2.52% a year [ST] [Certain]. The FCF dip is investment, not lost demand: operating margin and ROCE held flat while FCF fell, which points to capex rather than a broken model [Likely]. The EV/EBITDA method's base of 4,903.75 sits above the price without relying on the fragile DCF [Certain]. Beta 0.19 makes it a diversifier [Certain].
## Decision
```json
{
  "ticker": "TYO:9022",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 14.9% -> 10.1% TTM [CF-T] while operating margin (40.8% -> 40.4%) and ROCE (8.1% flat) held [IS-T, RA-T]: consistent with heavy investment (Chuo Shinkansen capex, research note section 2, tagged Guessing), not lost demand; ROIC's dip from 6.5% to 6.0% is small.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Megaproject capex keeps FCF conversion weak and leverage stuck around 4.25x net debt/EBITDA, so low ROIC (6.0%) never rises enough to earn its cost of capital.",
    "veto": null
  },
  "thesis": "A near-monopoly Shinkansen franchise trading near the bottom of its own P/E and EV/EBITDA ranges, but with low returns on a heavy, leveraged asset base and capex-depressed free cash flow.",
  "rationale": "Cheap on earnings with a real corridor moat, but ROIC of 6.0% is low, leverage is 4.25x, FCF is falling on capex and the DCF fair value is unreliable. Scorecard conviction 2: AVOID. Quality and leverage, not price, are the obstacle.",
  "price_at_decision": 4172.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-9022/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 36%: the corridor's pricing power is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 36}},
    {"text": "ROIC (TTM) falls below 5%: the recovery in returns has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5}},
    {"text": "Net debt/EBITDA rises above 5.5x: capex is re-leveraging the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.5}},
    {"text": "FCF margin (TTM) falls below 5%: capex is consuming nearly all cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4992.19, "basis": "Capex peaks and FCF margin recovers toward its 14.9% 2-year high [CF-T], lifting the price to the mechanical blended base fair value [valuation file]."},
    "base": {"probability": 0.45, "target_price_12m": 4172.00, "basis": "Returns stay flat (ROIC 6.0%, operating margin 40.4% [RA-T, IS-T]) and the P/E holds near 7.7x [RA], leaving the price roughly unchanged; below the EV/EBITDA base of 4,903.75 because leverage and capex cap re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 3419.17, "basis": "FCF keeps falling on Chuo capex and leverage stays above 4x [ST], so the market prices the EV/EBITDA bear case of 3,419.17 [valuation file]; the negative DCF bear is ignored as a capex artefact."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: low ROIC (6.0%) and 4.25x leverage cap the score (quality and balance-sheet points are zero), so a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```
