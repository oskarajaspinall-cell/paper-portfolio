# Evaluation: Moncler S.p.A. (BIT:MONC) — 2026-11-23
## Bear case
The fall to the entry price is explained by the business, not just the market: Q3 revenue was flat as Moncler DTC softened on weaker European tourism and warm weather [Likely] (https://www.reuters.com/business/retail-consumer/moncler-reports-flat-q3-revenue-held-back-by-weaker-tourist-spending-europe-2026-10-21/). Returns are drifting from their peak: ROIC 18.4% TTM is 2.6pp below its 2-year high and ROCE fell from 20.6% to 19.1% over the last 12 months [Certain] [RA-T]; a second weak winter on a fixed store base would extend that [Likely]. The sector is de-rating on fears that an AI selloff curbs wealthy spending, so cheapness against its own history can deepen [Guessing] (https://www.reuters.com/business/media-telecom/luxury-stocks-slip-fears-ai-falls-will-curb-spending-by-wealthy-2026-11-17/). The price is 20.5% below its 200-day average with a 12-month change of -29.5%: no trend support [Certain] [HI]. The bear fair value of 33.19 sits well below the price [Certain].

## Bull case
A top-tier franchise: gross margin 78.2% TTM, operating margin 29.0% (flat, +0.3pp over 12 months) and FCF margin rising from 21.5% to 25.0% over the last year [Certain] [IS-T, CF-T]. The ROIC/ROCE slip reflects flat revenue on a fixed cost base, not margin damage [Likely]. Net debt/EBITDA is 0.10x and Altman Z 6.13 [Certain] [ST]. Every multiple sits below its own 5-year minimum: P/E 17.4x vs 21.6x, EV/EBITDA 9.9x vs 13.6x, P/FCF 13.9x vs 17.4x, a 7.44% FCF yield, and below peers on P/E and EV/EBITDA [Certain] [RA]. The reverse DCF implies only 3.1% year-1 growth, while nine-month revenue still rose 6% at constant FX [Likely] (/quote/bit/MONC/transcripts/652948-q3-2026/). Base fair value 46.59 is above the price [Certain].

## Decision
```json
{
 "ticker": "BIT:MONC",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds no falling ROIC, operating margin or FCF margin over 1 or 3 years; the ROIC/ROCE gap to the 2-year high reflects flat revenue on weaker European tourism (Reuters 2026-10-21), with operating margin flat at 29.0% (IS-T) and FCF margin up from 21.5% to 25.0% (CF-T).",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Luxury demand weakness (tourism, wealth effects) proves lasting, turning flat revenue into a decline that deleverages the fixed store cost base and extends the ROIC slide.",
  "veto": null
 },
 "new_evidence": {
  "type": "method_change",
  "text": "The earlier AVOID at conviction 3 (2026-10-25) predates the scorecard (2026-11-09); on the same quality evidence the scorecard now sets conviction 4, with the price also lower and FCF margin rising over the last 12 months (CF-T)."
 },
 "thesis": "A 78%-gross-margin, near net-cash outerwear brand with flat margins and rising FCF trades below its own 5-year minimum on every multiple, pricing only 3.1% growth after a tourism-driven flat quarter.",
 "rationale": "Scorecard conviction 4: top-tier margins, near net-cash balance sheet and every multiple below its 5-year minimum, with the fall explained by a tourism and weather soft patch rather than margin damage. Python sizes it; cash is at the floor, so it replaces JKHY, a conviction-3 holding.",
 "price_at_decision": 39.49,
 "price_date": "2026-11-20",
 "research_note": "research/BIT-MONC/2026-11-23.md",
 "triggers": [
  {
   "text": "TTM gross margin falls below 75%, under the FY2021-25 range, signalling loss of brand pricing power.",
   "check": {
    "source": "statistics",
    "field": "grossMargin",
    "op": "<",
    "value": 75
   }
  },
  {
   "text": "TTM operating margin falls below 26%, under every year since FY2021, showing flat sales are deleveraging the cost base structurally.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 26
   }
  },
  {
   "text": "TTM ROIC falls below 14%, extending the slide from 21.0% to 18.4% into clear moat erosion.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "TTM FCF margin falls below 18%, under the FY2022 five-year low of 18.9%, showing inventory or working-capital stress from a weak season.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 18
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.3,
   "target_price_12m": 52.84,
   "basis": "Tourism and weather normalise and EV/EBITDA recovers toward its 5y minimum of 13.6x [RA], matching the EV/EBITDA method's bull value of 52.84 [fact sheet]; below the 70.07 blended bull because flat Q3 revenue (Reuters 2026-10-21) does not support the DCF bull's growth."
  },
  "base": {
   "probability": 0.45,
   "target_price_12m": 46.59,
   "basis": "Margins hold near 29.0% operating [IS] with low growth and the price moves to the mechanical base fair value of 46.59 [fact sheet], still below 5y-median multiples as the sector de-rating persists (Reuters 2026-11-17)."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 33.19,
   "basis": "A second weak winter extends the ROIC slide from 18.4% [RA-T] and takes the stock to the mechanical bear fair value of 33.19 [fact sheet], the DCF bear being lower still at 27.12."
  }
 },
 "replaces": "JKHY",
 "replacement_reason": "Cash is at the 1.5% floor, so the buy needs funding; JKHY is held at conviction 3 and its price already implies growth above the company's framework, while Moncler scores conviction 4 at multiples below its own 5-year minimum.",
 "second_opinion": {
  "file": "research/BIT-MONC/2026-11-23-evaluation-2.md",
  "conviction": 4
 }
}
```
