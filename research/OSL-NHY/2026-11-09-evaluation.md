# Evaluation: Norsk Hydro ASA (OSL:NHY) — 2026-11-09
## Bear case
Hydro is a price-taker in aluminium and the cycle is turning against it. The Q3 core profit missed, and management guided to higher smelting costs and lower realised metal prices (Reuters headline, fact sheet) [Likely]. Alunorte's Brazilian gas supply problem has an uncertain financial impact with no long-term fix yet (WSJ headline) [Likely]. The rolling data already shows it: ROCE fell from 29.4% to 26.7% in 12 months and FCF margin from 4.6% to 3.2%, 2.4pp below its 2-year high [Certain]; the cause is cost and price pressure plus working capital, which may persist if demand stays soft [Likely]. Cash conversion is thin and lumpy (FCF conversion 31.1% in FY2024, 51.7% TTM), so P/FCF of 20.4x is well above peers at 10.5x [Certain]. The mechanical bear value of 28.59 NOK shows how far through-cycle earnings could fall, and the 6-month momentum of -34.9% shows the market agrees [Certain].

## Bull case
The balance sheet is close to net cash (net debt/EBITDA 0.28x) and Altman Z is 3.51, so a downturn is survivable without dilution; shares fell 0.49% YoY [Certain]. Returns are high for a commodity producer: TTM ROIC 23.9% and operating margin 21.7%, both roughly flat over 12 months and up over 3 years [Certain]. The ROCE and FCF dips look cyclical and cost-driven (Alunorte gas, working capital), not a lost cost position: Q3 still delivered record Norwegian smelter output (transcript summary, fact sheet) [Likely]. Low-carbon hydropower smelting is a durable cost and product advantage [Likely]. EV/EBITDA of 2.9x sits near the bottom of its 5y range and below peers at 4.1x, P/B 1.2x is at its range low, and the reverse DCF implies only 0.4% year-1 growth [Certain]. The 25 November investor day could reset capital returns [Guessing].

## Decision
```json
{
 "ticker": "OSL:NHY",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "ROIC and operating margin are falling only from the FY2022 commodity peak (ROIC 38.2% in FY2022) and are up over 3 years on the rolling view [RA-T, IS-T]; the FCF margin and ROCE dip follow Alunorte gas costs, working capital and lower realised prices flagged at Q3 (Reuters and transcript headlines in the fact sheet), with net debt/EBITDA 0.28x [RA] intact: a cyclical trough with a sound balance sheet.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Aluminium price and smelting cost pressure (lower realised prices, Alunorte gas costs with no long-term solution) cut through-cycle earnings further, as the Q3 guidance warned.",
  "veto": null
 },
 "thesis": "A near-net-cash, low-carbon integrated aluminium producer with ROIC of 23.9% trades near the bottom of its own EV/EBITDA and P/B ranges, pricing almost no growth while its cost and FCF dip looks cyclical rather than structural.",
 "rationale": "Scorecard conviction 4: high returns, a strong balance sheet and a low own-history EV/EBITDA and P/B outweigh the Q3 cost and realised-price warning and unresolved Alunorte gas costs, which look cyclical. Probability-weighted scenarios sit above the price. Standard core size, volatility-scaled by Python; the falling FCF margin is the item to watch. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 68.38,
 "price_date": "2026-11-06",
 "research_note": "research/OSL-NHY/2026-11-09.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 15%, showing the cost position no longer earns returns well above the cost of capital through the cycle.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "TTM operating margin falls below 17%, well under the FY2025 five-year low of 19.8%, signalling a structural cost squeeze (Alunorte gas, power).",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 17
   }
  },
  {
   "text": "Net debt/EBITDA rises above 1.0x (0.28x TTM now), showing the balance sheet cushion is being consumed.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 1.0
   }
  },
  {
   "text": "TTM FCF margin turns negative (3.2% now), meaning working capital and capex absorb all cash generation.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 0
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 105.0,
   "basis": "Costs normalise and EV/EBITDA re-rates toward its 5y max 3.6x [RA] on TTM EBITDA [IS], below the mechanical bull 154.41 because Q3 guidance points to lower near-term realised prices."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 80.43,
   "basis": "EV/EBITDA moves back toward its 5y median 3.3x [RA], in line with the mechanical base fair value 80.43 [valuation]; macro overlay is context only and does not shift the odds."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 50.0,
   "basis": "Higher smelting costs, lower realised prices and Alunorte gas costs (Reuters/WSJ headlines in the fact sheet) cut EBITDA while EV/EBITDA stays near its 5y min 2.7x [RA]; above the mechanical bear 28.59 given net debt/EBITDA 0.28x [RA]."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/OSL-NHY/2026-11-09-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```
