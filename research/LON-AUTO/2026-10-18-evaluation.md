# Evaluation: Autotrader Group plc (LON:AUTO) — 2026-10-18
## Bear case
Every margin line has fallen over five years: gross -4.7pp, operating -7.2pp, FCF margin -14.9pp [Certain]. Management itself flagged retailer-pricing growth decelerating toward a lower historical range, and dealer backlash slowed the Deal Builder rollout [Likely], so the pricing lever that drove the past decade has a ceiling set by retailer tolerance. The stock is not cheap in absolute terms: a 6.91% FCF yield and P/FCF of 14.5x, above the 5y low of 13.1x, while EV/EBITDA, P/FCF and EV/Sales sit at premiums to peers [Certain]. Leverage has moved from net cash to 0.48x as buybacks run ahead of cash generation [Certain]. No mechanical fair value is computable, so the cheapness read is relative only [Certain]. RSI of 73.8 and a close well above both moving averages just before the Nov 5, 2026 results add entry-timing risk [Likely].

## Bull case
A UK marketplace with a two-sided network moat: TTM ROIC 49.0%, ROCE 62.3%, net margin 47.1% and FCF/NI conversion of 100.5%, every year at or above 100% [Certain]. Management cites a large, durable audience lead over its nearest competitor [Likely]. After a 29.6% fall over 12 months, P/E of 16.0x sits in the bottom quarter of its own 5y range and below the peer median of 18.4x [Certain]. Shares outstanding fell 3.65% YoY, and FY2027 guidance anticipates profit growth with margin stability [Likely], so EPS compounds even at flat multiples. Piotroski F of 7 and Altman Z of 18.65 confirm balance-sheet safety [Certain]. Macro is context only: GBP-in/GBP-out revenue, beta 0.72 [Certain].

## Decision
```json
{
  "ticker": "LON:AUTO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An exceptional-return UK car marketplace has de-rated to the bottom quarter of its own P/E range, but falling margins, a visible retailer-pricing ceiling and a 6.91% FCF yield leave the reward good rather than compelling.",
  "rationale": "Quality is outstanding but trending down on every margin line, pricing growth is decelerating by management's own account, and the price is not at a level where de-rating risk is clearly paid for (P/FCF above its 5y low, premium to peers, no fair value computable). Good but not compelling: AVOID, with an entry price at the 5y-low P/FCF.",
  "price_at_decision": 546.00,
  "price_date": "2026-10-16",
  "research_note": "research/LON-AUTO/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 40%, signalling the network-effect moat is eroding faster than the margin decline already seen (49.0% TTM).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM net margin falls below 40%, showing margin compression is structural rather than gradual (47.1% TTM).", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "Net debt/EBITDA rises above 1.0x, showing buybacks are being funded by leverage rather than free cash flow (0.48x TTM).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Management reports retailer price growth stalling or a material loss of audience share to a competitor in the H1 FY2027 results, confirming the pricing ceiling."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 700, "basis": "Profit growth guided for FY2027 [OV transcript] holds and P/E re-rates partway from 16.0x toward its 5y median of 24.2x [RA]; no mechanical fair value is computable [data unavailable], so this rests on own-history multiples."},
    "base": {"probability": 0.5, "target_price_12m": 580, "basis": "P/E holds near 16.0x [RA] while modest profit growth and buybacks (shares -3.65% YoY [ST]) lift EPS; margin trend stays gently down as in the note."},
    "bear": {"probability": 0.3, "target_price_12m": 447, "basis": "Retailer-pricing deceleration and Deal Builder pushback (note, transcript https://stockanalysis.com/quote/lon/AUTO/transcripts/411876-h2-2026/) push P/E back to its 5y low of 13.1x [RA]."}
  },
  "entry_price": 493,
  "entry_basis": "No base fair value is computable [data unavailable — no FX rate for GBP]; anchored instead on P/FCF back at its 5y low of 13.1x [RA] (now 14.5x), where the FCF yield would compensate for the falling-margin trend.",
  "replaces": null,
  "replacement_reason": null
}
```
