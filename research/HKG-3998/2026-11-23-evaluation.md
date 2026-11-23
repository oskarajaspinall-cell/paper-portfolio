# Evaluation: Bosideng International Holdings Limited (HKG:3998) — 2026-11-23
## Bear case
Gross margin has slipped from 60.1% (FY2022) to 57.2%, the clearest sign of pricing or mix pressure in a single-category, weather-driven winter brand [Certain]. ROCE sits 5.8pp below its 2-year high of 34.3% and FCF margin 9.2pp below its 29.2% peak; ROCE is flat over the last year, so returns have stopped expanding even if they are not falling [Certain]. Interim results land on Nov 25, 2026: a warm winter or inventory build would show first there [Likely]. The stock is down 13.5% over 12 months, the 50-day average sits below the 200-day, and the price is only just above its 200-day average, so there is no trend support [Certain]. Shares rose 1.14% YoY, mild dilution rather than buybacks [Certain]. A persistent China consumer and policy discount can keep the multiple at the floor regardless of fundamentals [Guessing]. Moat breadth (market share) is unverified [Guessing].
## Bull case
ROIC is 68.7% and rising on a rolling basis, operating margin is stable near 19.9% and net margin rose to 14.6% [Certain]. The company is net cash (net debt/EBITDA -2.24x) with Altman Z 5.25 [Certain]. FCF margin recovered 7.8pp over the last year to 20.0%; the FY2024 peak came with FCF/NI of 220.5%, a working-capital swing, so the gap to the 2-year high is normalisation rather than erosion [Likely]. EV/EBITDA of 4.9x and EV/Sales of 1.2x sit below their own 5-year minimums and well below peers, with an 11.97% FCF yield [Certain]. The reverse DCF implies revenue shrinking 12.8% in year 1, which nothing in the margins or cash flow shows [Likely]. Even the mechanical bear fair value of 4.96 sits above the 4.46 close, and the base is 7.66 [Certain].
## Decision
```json
{
  "ticker": "HKG:3998",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "On the rolling view ROIC rose 3.3pp, operating margin is flat (+0.1pp) and FCF margin rose 7.8pp [RA-T, IS-T, CF-T]; the gaps to 2-year highs reflect an FY2024 working-capital peak (FCF/NI 220.5%) [CF,IS].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A warm winter or weaker Chinese consumer demand drives inventory build and markdowns, pushing gross margin toward the 55% trigger; first visible in the Nov 25, 2026 interim results.",
    "veto": null
  },
  "thesis": "China's leading down-jacket brand, net cash with ROIC of 68.7% and an 11.97% FCF yield, trades below its own 5-year minimum EV/EBITDA and EV/Sales, where the price implies a -12.8% revenue decline its stable margins and recovering cash flow do not show.",
  "rationale": "Fundamentals are intact on the rolling view and the valuation remains at the floor of its own history and below peers; nothing has changed since the 2026-11-08 HOLD. Not an ADD: no trend support and interim results are two days out. The position stays at its existing size.",
  "price_at_decision": 4.46,
  "price_date": "2026-11-20",
  "research_note": "research/HKG-3998/2026-11-23.md",
  "entry_price": null,
  "entry_basis": "Already at conviction 4 at today's price, so price is not the obstacle; a lower price would not change the HOLD, and the next step is the Nov 25, 2026 interim results.",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the five-year low of 57.2%, signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM net margin falls below 10%, reversing the five-year rise to 14.6% and indicating the brand premium has eroded.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 40%, a reversion toward FY2022 levels that undercuts the moat thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below the FY2025 five-year low of 12.2%, signalling inventory or working-capital stress from a demand down-cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7.66, "basis": "Results confirm stable margins and the market closes toward the mechanical base fair value of 7.66 [IS,BS,CF,RA,ST,HI], with EV/EBITDA back toward its 5y median of 6.8x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 5.56, "basis": "EV/EBITDA rerates only partly, to the EV/EBITDA method's base value of 5.56 [IS,BS,CF,RA,ST]; below the blended base because a China consumer discount persists [Guessing]."},
    "bear": {"probability": 0.25, "target_price_12m": 3.55, "basis": "A warm winter hits the interim results and gross margin slips further, sending the price back to its 52-week low of 3.55 [HI], below the mechanical bear value of 4.96 because markdowns would cut the TTM base it uses."}
  }
}
```
