# Evaluation: Prio S.A. (BVMF:PRIO3) — 2026-11-16
## Bear case
Prio takes the oil price it is given; its edge is cost and execution on acquired fields, not a barrier [Likely]. Earnings still don't turn into cash: FCF yield is -1.22% and TTM FCF margin -2.4% after three years of deeply negative FCF paid for with debt, which took net debt/EBITDA to 3.24x in FY2025 [Certain]. The 12-month recovery (ROIC 7.7% to 16.2%, operating margin 23.4% to 36.9%) is real, but operating margin is still 13.6pp below its 2-year high and the rebound leans on record volumes and higher oil prices, both cyclical [Likely]. The price is up 58.2% in 12 months and sits at a premium to Brazilian peers on P/E (+75%) and P/B (+130%); if Brent or production growth slows, that premium can de-rate quickly [Likely]. No fair value is computable, so the discount can't be checked [Certain]. Brazil tax or regulatory risk is unverified [Guessing].
## Bull case
The five-year decline is an investment cycle, not a broken model: the Peregrino and Wahoo build-out depressed FY2025 returns, and the last 12 months show the payoff, with ROIC back to 16.2%, ROCE to 16.3% and FCF margin up from -65.1% to -2.4% [Certain]. Leverage fell from 3.24x to 1.14x net debt/EBITDA, and Q3 2026 brought record production with net debt down to $3.460B per the call summary [Likely]. EV/EBITDA of 4.1x is below its own 5-year minimum of 4.5x and P/E of 8.1x sits below its 5y median of 9.2x [Certain]. Piotroski F of 7 points to improving fundamentals [Certain]. Management targets 200k barrels/day in 2027; once capex eases, FCF could turn strongly positive [Guessing]. The trend is intact: the price is above its 200-day average and the 50-day sits above the 200-day [Certain].
## Decision
```json
{
  "ticker": "BVMF:PRIO3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The FY2025 trough followed acquisition and development spending funded by debt; over the last 12 months ROIC rose 7.7% to 16.2%, operating margin 23.4% to 36.9% and FCF margin -65.1% to -2.4%, while net debt/EBITDA fell from 3.24x to 1.14x [RA-T, IS-T, CF-T, BS].", "moat": "none", "key_risk": "high", "key_risk_text": "Brent falls or capex stays high, so FCF stays negative and the peer premium de-rates after a +58.2% year; the oil price is outside management's control.", "veto": null},
  "thesis": "A low-cost Brazilian offshore producer coming out of a debt-funded build-out, whose returns are recovering but whose free cash flow is not yet proven.",
  "rationale": "Returns and leverage are recovering, but FCF is still negative, there is no moat beyond cost execution, the price already carries a peer premium after a strong year, and no fair value can be computed. Scorecard conviction 2: below the buy bar.",
  "price_at_decision": 63.29,
  "price_date": "2026-11-13",
  "research_note": "research/BVMF-PRIO3/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Operating margin (TTM) falls below 25%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "Net debt / EBITDA rises above 2.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "FCF margin (TTM) is still negative after two further quarterly reports: growth capex never converts to cash"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.0, "basis": "FCF turns positive as capex eases and EV/EBITDA re-rates from 4.1x toward its 5y median of 5.8x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 66.0, "basis": "P/E holds near 8.1x [RA] on earnings supported by record Q3 2026 production (transcript, /quote/bvmf/PRIO3/transcripts/664368-q3-2026/) while FCF stays near breakeven."},
    "bear": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Lower Brent compresses the 36.9% operating margin [IS-T] and the P/E premium to peers (median 4.6x [RA,P]) narrows."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is unproven free cash flow, no moat and high oil-price risk, not price alone; a lower price would not by itself justify conviction 4, and no fair value is computable to anchor one.",
  "replaces": null,
  "replacement_reason": null
}
```
