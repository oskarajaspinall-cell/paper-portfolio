# Evaluation: Visa Inc. (V) — 2026-11-15
## Bear case
The price already assumes perfection. Every multiple sits above its 5y maximum (P/E 34.8x vs a 33.0x max, P/FCF 36.4x vs 30.4x) [Certain], and the reverse DCF implies 23.6% year-1 revenue growth [Certain]. That is an extended price: if growth merely slows, a de-rating toward the 27.8x median P/E costs more than years of earnings growth return [Likely]. Cash is weakening under flat earnings: FCF margin fell from 53.9% to 48.1% in the last 12 months, 8.7pp below its 2-year high, and FCF conversion slipped to 93.8% [Certain]; the note could not tie this to one cause [Guessing]. The 10-K expanded risk factors on conflicting court decisions over the Reg II debit cap, a Fed proposal for further cuts and the reintroduced Credit Card Competition Act [Certain]; any of these is a binary hit to pricing. M&A (BioCatch, Prisma) may start to replace buybacks [Guessing].

## Bull case
This is one of the few genuinely wide moats: a two-sided network with 97.7% gross margin and 66.3% operating margin, flat for five years [Certain]. Returns are still rising on the rolling view: ROIC 56.4% from 49.6% a year earlier, ROCE 48.5% at its 2-year high [Certain]. The balance sheet is near-unlevered (net debt/EBITDA 0.28x, Altman Z 8.32) and the share count is down 3.00% YoY [Certain]. The FCF dip sits between stable earnings and cash, consistent with legal-settlement, tax and partly one-off World Cup/Olympics marketing items the 10-K cites rather than a broken model [Likely]. The trend is strong and fundamental: 22.7% above the 200-day average, up 25.6% over 12 months and 15.2pp ahead of SPY [Certain]. The mechanical DCF is harsh on a capital-light compounder; the P/E method gives 304.69-351.60 [Certain].

## Decision
```json
{
  "ticker": "V",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell 53.9% -> 48.1% TTM while operating margin (66.3%) and net margin stayed flat, so the gap is between earnings and cash; the FY2026 10-K cites legal settlements, tax items and one-off World Cup/Olympics marketing (https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm). ROIC and ROCE are rising on the rolling view.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "US interchange regulation (Reg II debit cap rulings, the Fed's proposed cuts, the Credit Card Competition Act) cutting pricing, compounded by a de-rating from multiples above their 5y maximum if growth slows.",
    "veto": null
  },
  "thesis": "A wide-moat, near-unlevered payments network with rising returns and a strong, fundamentally backed uptrend is a good business that is working, though priced above every 5-year multiple maximum with US interchange regulation unresolved.",
  "rationale": "The scorecard gives 4: top quality, rising returns, a clean balance sheet, a wide moat and trend strength in place of a discount. The scenarios show limited upside and real de-rating risk, so this is a minimum-conviction position, sized by Python at the conviction-4 core size scaled for volatility.",
  "price_at_decision": 425.76,
  "price_date": "2026-11-13",
  "research_note": "research/V/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 45%, giving up most of the rise from 40.1% (FY2022) to 56.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 45}},
    {"text": "TTM operating margin falls below 62%, breaking the flat five-year range around 66-67% and showing pricing pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 62}},
    {"text": "TTM FCF margin falls below 42%, showing the cash decline from 53.9% is structural rather than settlements and one-offs.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 42}},
    {"text": "A final US rule or court decision that materially lowers the Reg II debit interchange cap, or enactment of the Credit Card Competition Act."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 490, "basis": "P/E holds near today's 34.8x [RA] as rising ROIC (56.4% TTM [RA-T]) and buybacks (shares -3.00% YoY [ST]) grow earnings, above the P/E-method bull of 351.60 because the trend premium persists."},
    "base": {"probability": 0.5, "target_price_12m": 440, "basis": "P/E eases toward its 33.0x 5y maximum [RA] while earnings growth and buybacks more than offset it; above the mechanical base 222.83 because the DCF is harsh on a capital-light network (note, section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 300, "basis": "An adverse Reg II ruling or the Credit Card Competition Act (10-K risk factors, note section 6) de-rates P/E toward its 27.8x 5y median [RA], near the P/E-method bear of 304.69."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
