# Evaluation: Otis Worldwide Corporation (OTIS) — 2026-10-17
## Bear case
The price has reached the blended base fair value of 71.95, so the mechanical cushion is gone; the DCF alone (base 59.53) sits below the close [Certain]. Leverage keeps drifting the wrong way: net debt/EBITDA is 3.04x TTM versus 2.62x in FY2021 [Certain]. Q2 2026 brought lower margins and a guidance cut on operating profit and EPS (Q2 transcript headline) [Certain], and New Equipment volume declined while FCF conversion trends down [Likely]. The macro overlay flags a real-yield rise (10y at 5.10%) and a sharp one-month dollar move that could hit Q4 translation [Likely]. A CEO succession is due in H1 2027 [Certain]. Short interest rose 13.2% month-on-month into the Oct 28 print [Certain]. If Q3 confirms service-margin pressure, the multiple discount may be deserved, not an anomaly [Guessing].
## Bull case
The thesis was never "reach one DCF number"; it was that a 65.3% ROIC service franchise trades below its own 5-year minimum on every multiple, and it still does: P/E 18.3x vs a 22.5x minimum, EV/EBITDA 13.3x vs 16.4x, P/FCF 15.9x vs 22.6x [Certain]. It also trades below the JCI/HON/KONE peer median on every multiple [Certain]. Quality has not slipped: operating margin 16.6% and FCF margin 11.5% TTM sit above the triggers, and ROIC/ROCE keep rising [Certain]. Service organic volume grew 9% in H1 2026 and UpLift delivered ~$200m run-rate savings [company-reported] (https://www.sec.gov/Archives/edgar/data/1781335/000178133526000113/otis-20260630.htm). The 6.30% FCF yield funds the dividend and a 2.55% share-count reduction [Certain]. The EV/EBITDA method alone values the shares at 96.78 base, so the DCF is the conservative leg [Likely].
## Decision
```json
{
  "ticker": "OTIS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A service-led elevator franchise with rising ROIC still trades below its own 5-year minimum on every multiple and below peers, pricing a transitory margin squeeze and CEO transition as permanent impairment.",
  "rationale": "Fair value was reached only on the conservative DCF leg; the multiple-discount thesis is intact, quality metrics are stable or improving and no trigger is near. Leverage drift, a guidance cut and a small bearish macro tilt cap conviction at 4, so no ADD; the existing position stays at its size into the Oct 28 results.",
  "price_at_decision": 71.33,
  "price_date": "2026-10-16",
  "research_note": "research/OTIS/2026-10-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2021 5-year low of 15.2%, showing the service-margin squeeze is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15.2}},
    {"text": "TTM FCF margin falls below the FY2025 5-year low of 10.0%, showing cash generation is deteriorating with margins.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.5x (3.04x TTM now), showing capital returns are being debt-funded."},
    {"text": "Service operating margin in the earnings release falls below 20% for two consecutive quarters, or modernization backlog growth turns negative."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 92.0, "basis": "EV/EBITDA moves back toward its 5y minimum of 16.4x [RA] on stable TTM EBITDA, close to the EV/EBITDA method's base 96.78 [fact sheet fair value]; above the blended bull 72.62 because the DCF leg's own-history growth caps it while the business has improved (ROIC rising to 65.3% [RA])."},
    "base": {"probability": 0.5, "target_price_12m": 78.0, "basis": "Margins hold at 16.6% operating [IS] with 9% service organic volume growth [company-reported, 10-Q] and a 6.30% FCF yield [ST], so the multiple recovers part of the gap to peers (EV/EBITDA peer median 16.7x [P]); above the blended base 71.95 because the DCF leg ignores the multiple discount to own history."},
    "bear": {"probability": 0.25, "target_price_12m": 56.55, "basis": "Q3 confirms the Q2 guidance cut and margin pressure while net debt/EBITDA keeps rising from 3.04x [RA]; the mechanical bear fair value 56.55 [fact sheet]; bear weight raised slightly per the macro overlay's small bearish tilt on real yields and the dollar (research/OTIS/2026-10-17-macro.md)."}
  },
  "entry_price": 57.56,
  "entry_basis": "valuation file: base 71.95 x 0.8; the level at which the same evidence would justify adding to the position.",
  "replaces": null,
  "replacement_reason": null
}
```
