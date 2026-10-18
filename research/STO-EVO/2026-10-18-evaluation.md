# Evaluation: Evolution AB (publ) (STO:EVO) — 2026-10-18
## Bear case
The multiple is low because the top line has stalled: the Q4 2025 call reported a year-on-year revenue decline and Q1 2026 another, with Europe hit by regulation and Asia by cybercrime copying the product [Certain] (OV transcripts). Operating margin has slipped from 61.3% to 57.8% and net margin from 56.6% to 51.8% [Certain] [IS]; the mechanical base fair value assumes growth the business is not currently delivering [Likely]. Part of revenue relies on Asian markets EVO cannot police, so the regulatory risk is structural, not cyclical [Likely]. A large holder (Candle Lake) crossed the mandatory-bid threshold and bid below the current price [Likely] (WSJ, Reuters headlines [OV]); with insiders at 34.37% [ST] and a shrinking float, minorities could be squeezed out cheaply over time [Guessing]. Results land on Oct 23, 2026 [ST], so the trend question resolves within days [Certain]. Consumer Discretionary is already the portfolio's most crowded sector [Certain].
## Bull case
A net-cash (-0.85x net debt/EBITDA [RA]) B2B content franchise earning 31.2% ROIC [RA] with a 60.2% FCF margin and 116.3% FCF conversion [CF,IS] trades at 13.6x P/E and 11.1x P/FCF, the bottom of its own five-year range and below peers on P/E and P/FCF [RA] [Certain]. The price implies -3.7% year-1 revenue growth [OV] while even the bear fair value of 888.09 SEK sits above the close [Certain]. Shares fell 3.23% YoY [ST] and management launched a record buyback [Likely] (Q2 2026 transcript). North America and Latin America keep setting records and new exclusive titles are selling well [Likely] (OV transcripts). A deep-pocketed holder accumulating is a valuation floor and potential catalyst [Guessing].
## Decision
```json
{
  "ticker": "STO:EVO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 31%-ROIC live-casino franchise at the bottom of its own five-year multiples, but with a stalled top line, compressing margins, structural regulatory exposure and an unresolved controlling-holder overhang, it is cheap for reasons the next results must disprove.",
  "rationale": "Valuation and cash returns are compelling, but revenue has been declining year on year, margins are falling, and a holder bidding below market clouds minority outcomes. Results arrive in five days. Adding a third Consumer Discretionary name would push the sector near its cap. Good but not compelling: AVOID, re-check after the print.",
  "price_at_decision": 800.00,
  "price_date": "2026-10-16",
  "research_note": "research/STO-EVO/2026-10-18.md",
  "triggers": [
    {"text": "TTM operating margin falls below 50%, confirming regulatory and piracy pressure is structurally eroding the 57.8% TTM level.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "TTM ROIC falls below 20%, reversing the five-year rise from 22.7% to 31.2%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 50%, under the FY2021 five-year low of 52.9%, showing margin pressure has reached the cash line.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 50}},
    {"text": "Quarterly reports return to year-on-year revenue growth for two consecutive quarters (would lift conviction); continued declines confirm the AVOID."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1320.58, "basis": "Revenue returns to growth as North America/LATAM offset Europe (Q2 2026 transcript [OV]), so the price re-rates to the mechanical base fair value of 1,320.58 SEK [OV]."},
    "base": {"probability": 0.5, "target_price_12m": 888.09, "basis": "Revenue flat-to-down and margins drifting lower [IS] keep multiples near the floor of their five-year range [RA]; buybacks (shares -3.23% YoY [ST]) carry the price to the bear fair value of 888.09 SEK, below the mechanical base because that assumes growth EVO is not currently delivering."},
    "bear": {"probability": 0.25, "target_price_12m": 668.26, "basis": "Further European regulation and Asian piracy deepen the revenue decline and the takeover overhang caps the price, valuing EVO at the EV/EBITDA bear value of 668.26 SEK [OV]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: even the bear fair value is above the close. The obstacle is the declining revenue trend, regulatory exposure and the unresolved Candle Lake ownership situation; a lower price would not change the decision, evidence of renewed growth would.",
  "replaces": null,
  "replacement_reason": null
}
```
