# Evaluation: Prosperity Bancshares (PB) — 2026-11-09
## Bear case
Returns are mediocre and falling: ROE is 6.5% TTM against 8.3% in FY2021, and net margin 36.0% TTM against 43.4% in FY2025 [Certain]. Three acquisitions closed in one year (American, Southwest, Stellar), and MD&A now flags deposit attrition, cost overruns and failed synergies [Certain]. Shares rose 8.89% YoY, so growth is bought with stock [Certain]. The transcript headline points to flat-to-slight loan growth, leaving the 2027 case on cost savings [Likely]. The stock is not cheap on earnings: P/E 13.2x is above the peer median of 11.7x and P/FCF 14.6x sits at 78% of its 5y range [Certain]. The price exceeds the (unreliable) base fair value of 69.91 [Certain]. The FCF-margin direction change (rising to 42.4% over 12 months, still 17.2pp below its 2-year high) reflects volatile bank cash flows rather than a clear trend [Likely]. The macro overlay tilts small toward bear: HY spreads +0.77pp in 3 months and VIX 28.18 [Certain].

## Bull case
A conservative Texas deposit franchise with beta 0.65, CET1 13.46% and Q3 net charge-offs of .05% per the Q3 headline [Likely]. P/B of 0.9x sits at 19% of its 5y range and below peers at 1.3x, so weak returns are already priced [Certain]. The ROE dip is largely cyclical (FY2023 rate squeeze, partly recovered to 7.2% in FY2025) plus merger expenses and acquisition goodwill swelling equity [Likely]. Management guides 2027 EPS growth from margin expansion and cost savings, and the board raised the dividend to 0.64 USD a quarter [Likely]. The reverse DCF implies -2.4% year-1 revenue growth, undemanding if the merged banks hold earnings [Likely]. Q3 EPS of 1.67 beat consensus [Likely]. Still, upside to the bull fair value of 85.00 needs synergies that are not yet evidenced [Guessing].

## Decision
```json
{
  "ticker": "PB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin is down over 3 years but rising over the last 12 months, 26.3% to 42.4% [CF-T], typical of volatile bank cash flows; ROE fell mainly in FY2023 (6.1%) on the rate cycle and partly recovered to 7.2% in FY2025 [RA], with the TTM dip to 6.5% coinciding with three 2026 mergers, merger expenses and goodwill swelling equity (10-Q https://www.sec.gov/Archives/edgar/data/1068851/000119312526338254/pb-20260630.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Integration of three simultaneous acquisitions fails to deliver the cost savings the 2027 EPS case relies on, with deposit attrition (MD&A, 10-Q) and a credit cycle turn on top.",
    "veto": null
  },
  "thesis": "A conservative Texas deposit franchise trading below book, but with single-digit ROE, dilutive serial acquisitions and a price already above its mechanical base fair value, the upside depends on unproven merger synergies.",
  "rationale": "Quality is low (ROE 6.5% TTM) and valuation is only cheap on book; on earnings and FCF it trades above peers and near the top of its range, and the price sits above base fair value. The scorecard gives low conviction; synergy upside is not evidenced yet. No position.",
  "price_at_decision": 71.87,
  "price_date": "2026-11-06",
  "research_note": "research/PB/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE stays below 5% after the 2027 integration, showing merger synergies fail to lift returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 5}},
    {"text": "TTM net margin falls below 30% (36.0% now), showing integration costs or provisions are eroding earnings.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "Shares change YoY stays above 15% on further issuance, showing acquisitions are dilutive rather than accretive.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 15}},
    {"text": "Net charge-offs above 0.50% in a quarterly release on https://www.prosperitybankusa.com, or a Texas credit event forcing large provisions."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 85.00, "basis": "Synergies lift ROE back toward its FY2021 8.3% [RA] and P/B re-rates toward the peer 1.3x [RA], reaching the mechanical bull fair value of 85.00 [fact sheet]."},
    "base": {"probability": 0.5, "target_price_12m": 69.91, "basis": "ROE stays near 6.5% TTM [RA] with flat-to-slight loan growth (Q3 transcript headline [OV]), so the stock settles at the mechanical base fair value of 69.91 [fact sheet]."},
    "bear": {"probability": 0.3, "target_price_12m": 56.66, "basis": "Integration slippage plus wider credit spreads compress P/B toward its 5y low of 0.8x [RA], the mechanical bear fair value of 56.66; bear probability raised slightly per the macro overlay's small bear tilt (research/PB/2026-11-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: low quality (ROE 6.5% TTM) and unproven integration of three deals keep the score low; a lower price alone would not lift conviction to 4 without evidence that synergies raise ROE.",
  "replaces": null,
  "replacement_reason": null
}
```
