# Evaluation: Archrock, Inc. (AROC) — 2026-11-09
## Bear case
The stock is down 29.6% over six months and 19.5% below its 200-day average: the market is pricing a peak in the compression cycle [Guessing]. Q3 revenue missed, aftermarket revenue fell and costs outpaced revenue, lowering adjusted gross margin [Certain]. ROIC of 11.2% is only moderate for a capital-heavy lessor and Altman Z of 1.28 reflects leverage of 2.73x net debt/EBITDA [Certain]. The FCF margin jump from 1.3% to 20.3% is mostly lower growth capex, not better economics; the Direction change line (FCF margin falling over 5 fiscal years, rising over 12 months) reflects capex timing, and if bookings require fleet additions again FCF falls back [Likely]. Fair value is flagged unreliable (DCF base 45.46 vs EV/EBITDA base 12.88), and the EV/EBITDA method alone sits below the price [Certain]. Peer fleet additions or softer gas volumes could cap pricing [Guessing].
## Bull case
Compression is a must-run, fee-based service; utilisation was 94.3% with record bookings and FY2026 EBITDA guidance reaffirmed (earnings call transcript headline, fact sheet) [Likely]. Every return metric rose over five years and the last 12 months: ROIC +1.4pp, operating margin +2.5pp to a 2-year high of 38.8% [Certain]. Leverage fell from 4.91x to 2.73x and near-dated notes were refinanced [Certain]. P/E of 14.2x and EV/EBITDA of 8.3x are both below their own 5-year minimums and under peers [Certain]. The reverse DCF implies only 2.2% year-1 revenue growth, a low bar [Likely]. FCF yield is 6.27% with a rising dividend; adjusted EPS beat in Q3 [Likely]. Macro is context only for a US-only fee business (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "AROC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 1 and 3 years (RA-T, IS-T, CF-T); the 5-year FCF margin fall is the FY2021 starting point, reversed as growth capex eased.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A compression-cycle peak: softer gas volumes or peer fleet additions cap pricing and utilisation, while leverage of 2.73x amplifies any EBITDA decline.", "veto": null},
  "thesis": "A deleveraging, fee-based US gas-compression lessor with rising margins and returns trades below its own 5-year minimum P/E and EV/EBITDA, but moderate ROIC, leverage and a possible cycle peak keep the skew from being compelling.",
  "rationale": "Cheap on its own history with improving returns, but ROIC is moderate, leverage is still 2.73x, fair value is unreliable and Q3 showed revenue and aftermarket softness. Good but not compelling: AVOID with an entry price.",
  "price_at_decision": 27.54,
  "price_date": "2026-11-06",
  "research_note": "research/AROC/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, reversing most of the rise from 3.9% (FY2021) to 11.2%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 34%, showing compression pricing has peaked.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 34}},
    {"text": "Net debt/EBITDA rises above 3.5x (2.73x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "Contract operations revenue in the 10-Q declines year on year for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 42.0, "basis": "Record bookings and 94.3% utilisation sustain margins at the 38.8% 2-year high [IS-T] and P/E re-rates toward the 21.9x peer median [RA], near the 52-week high of 42.23 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 33.0, "basis": "EV/EBITDA returns to its 5y median 9.4x [RA] on TTM EBITDA with leverage of 2.73x [RA]; this sits between the EV/EBITDA and DCF fair values, which disagree (fact sheet flags fair value unreliable)."},
    "bear": {"probability": 0.25, "target_price_12m": 20.0, "basis": "A compression-cycle peak trims EBITDA and the multiple stays below its 5y minimum 8.5x [RA], with 2.73x leverage magnifying the equity fall; above the mechanical EV/EBITDA bear of 10.35 because fee-based contracts and 94.3% utilisation limit the EBITDA drop [fact sheet]."}
  },
  "entry_price": 22.0,
  "entry_basis": "Fair value is flagged unreliable, so base 34.60 x 0.8 is not used; 22.0 sits just below the 52-week low of 22.88 [HI], where EV/EBITDA would be well under its 5y minimum 8.5x [RA] on unchanged EBITDA.",
  "replaces": null,
  "replacement_reason": null
}
```
