# Evaluation: ANTA Sports Products Limited (HKG:2020) — 2026-10-18
## Bear case
Returns are fading as capital is deployed: ROIC fell from 36.4% (FY2021) to 23.3% TTM and ROE from 28.6% to 24.8% [Certain] (RA). Management is now buying minority stakes in Western brands, most recently the 29.06% Puma stake for about €1.5bn, a brand ANTA does not control and must turn around alongside FILA and Amer Sports [Likely] (gurufocus URL in note). The net-cash cushion has already thinned, net debt/EBITDA moving from -1.05x (FY2023) to -0.60x TTM [Certain] (BS, IS). US political commentary tying Wilson and Louisville Slugger to Chinese ownership adds a geopolitical tail [Guessing] (foxnews URL). The cheap multiples may reflect a lasting de-rating of Chinese consumer names rather than mispricing: the stock trails SPY by -24.3pp over 12 months [Certain] (HI). For this portfolio, it would be a fourth Greater-China holding and push Consumer Discretionary to the 30% cap alongside the pending Bosideng order [Likely] (state.json).

## Bull case
Operating quality is improving, not deteriorating: operating margin rose to 24.3% TTM and FCF margin to 24.0%, gross margin holds at 62.3%, and FCF conversion is 127.2% [Certain] (IS, CF). H1 2026 revenue grew 12.9% with an operating margin of 27% (transcript headline, OV) [Likely]. Yet every multiple sits below its own 5-year minimum: P/E 11.9x vs 13.2x, EV/EBITDA 6.4x vs 10.1x, P/FCF 9.3x vs 10.5x, at a 10.81% FCF yield [Certain] (RA, ST). The reverse DCF implies -3.2% year-1 revenue growth, and even the mechanical bear fair value of HKD 90.55 sits above the 77.95 close [Certain] (fair-value table). Piotroski 7 and Altman Z 4.63 confirm balance-sheet strength [Certain] (ST). Macro is context only [Certain] (macro overlay).

## Decision
```json
{
  "ticker": "HKG:2020",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 62%-gross-margin multi-brand sportswear leader trades below its own 5-year minimum on every multiple, but falling ROIC and a pivot to large minority stakes in Western turnaround brands (Puma) leave capital allocation unproven.",
  "rationale": "Valuation is compelling and margins are rising, but ROIC has fallen for five years and the Puma stake opens an unproven M&A phase. It would also be a fourth Greater-China name and push Consumer Discretionary to the sector cap, requiring a replacement we cannot justify. Good, not compelling: AVOID until the Puma economics show in reported returns.",
  "price_at_decision": 77.95,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-2020/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing the Amer Sports/Puma expansion is structurally diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 58%, showing discounting or channel mix is overcoming premiumisation.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "TTM FCF margin falls below 15%, showing the minority stakes have become cash drags.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Positive change of mind: FY2026 annual results show TTM ROIC stabilised at or above the FY2025 level of 22.4% after the Puma stake, with the balance sheet still net cash on the ratios page."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 115.64, "basis": "Margins keep rising and the Puma stake proves accretive, so the price reaches the mechanical base fair value of HKD 115.64 (fair-value table, DCF + EV/EBITDA)."},
    "base": {"probability": 0.5, "target_price_12m": 90.55, "basis": "Double-digit H1 2026 growth (OV transcript) holds but returns keep drifting lower, so multiples recover only to the mechanical bear fair value of HKD 90.55, still below the 5y-minimum P/E of 13.2x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 66.85, "basis": "Puma integration and a softer China consumer extend the ROIC decline (36.4% to 23.3% [RA]) and the de-rating, sending the price back to its 52-week low of 66.85 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below even the mechanical bear fair value; conviction is capped by the unproven Puma capital allocation and five-year ROIC decline, which only reported FY2026 returns can resolve, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
