# Evaluation: Bristol-Myers Squibb Company (BMY) — 2026-10-07
## Bear case
The cheapness comes mostly from P/E. P/E of 13.1x sits at the 1st percentile of its 5y range, but EV/EBITDA of 8.2x is at the 31st percentile, essentially its 5y median of 8.1x, and P/FCF of 10.6x sits above its 8.2x/8.5x 5y min/median [Certain] (RA). On cash flow, the stock is not cheap against its own history. The fundamentals that matter for a patent-cliff story are weakening: gross margin is down 5.9pp to 71.7%, FCF margin is down from 32.8% to 23.3%, and net debt/EBITDA is up from 1.47x to 1.80x [Certain] (IS, CF, BS). Eliquis and Revlimid face loss of exclusivity, so legacy revenue keeps eroding while pipeline readouts carry binary risk [Likely] (note §1-2). The peer discount is inflated by LLY's multiple and does not show mispricing [Likely] (RA). An Altman Z of 2.59 is in the grey zone [Certain] (ST).
## Bull case
ROIC rose from 10.8% to 21.7% and ROCE from 9.8% to 22.7% over five years, and the Piotroski F is 7 [Certain] (RA, ST). The Growth Portfolio already supplies 55% of revenue, with 7 assets each above $1bn annualised, so the transition is underway rather than hoped for [Certain] (bms.com investors). Recent proof points include the Camzyos label expansion on 2026-09-30, the Phase 3 EXCALIBER-RRMM iberdomide data and a cell therapy that met its primary endpoint [Certain] (OV news). A 9.40% FCF yield funds the dividend and the pipeline with flat shares (+0.47% YoY) [Certain] (ST). Operating margin expanded 12.7pp to 31.8% [Certain] (IS). With a 5y beta of 0.18, the stock is defensive ballast [Certain] (ST). If Q3 results on Oct 29, 2026 confirm that the growth assets offset legacy erosion, the P/E could re-rate toward its 17.7x median [Guessing] (RA).
## Decision
```json
{
  "ticker": "BMY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "BMY's Growth Portfolio and rising ROIC are real, but on EV/EBITDA and P/FCF the stock trades at or above its own 5-year median while gross margin, FCF margin and leverage are deteriorating into legacy patent cliffs, so the low P/E is not a compelling mispricing.",
  "rationale": "Quality is improving, but the valuation case rests on P/E alone. EV/EBITDA is at its 5y median and P/FCF is above it, while FCF margin, gross margin and leverage are trending the wrong way. The expected 12m return is roughly flat. Good but not compelling: conviction 3, below the buy threshold of 4. Keep the cash.",
  "price_at_decision": 59.59,
  "price_date": "2026-10-06",
  "research_note": "research/BMY/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, reversing the 5-year rise from 10.8% to 21.7% and showing the Growth Portfolio is not replacing legacy returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 20% (23.3% now), extending the decline from 32.8% in FY2021.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 70% (71.7% now), signalling mix erosion from legacy loss of exclusivity is accelerating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 70}},
    {"text": "Growth Portfolio revenue share, per bms.com investor disclosures, falls back below 50% from 55%, showing new drugs are not offsetting legacy LOE."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 74.0, "basis": "Growth Portfolio (55% of revenue, bms.com investors) offsets legacy erosion and EV/EBITDA re-rates to its 5y max of 9.8x [RA] on TTM EBITDA with net debt/EBITDA of 1.80x [BS,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 60.0, "basis": "EV/EBITDA stays near its 5y median of 8.1x [RA] (8.2x now) on flat TTM EBITDA as growth assets and legacy erosion roughly net out."},
    "bear": {"probability": 0.30, "target_price_12m": 48.0, "basis": "The FCF margin decline from 32.8% to 23.3% [CF,IS] continues and P/FCF reverts to its 5y median of 8.5x [RA] from 10.6x."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
