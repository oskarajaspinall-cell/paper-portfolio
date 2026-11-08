# Evaluation: Dropbox, Inc. (DBX) — 2026-11-08
## Bear case
Revenue barely moves: the 10-Q says growth has declined, the mix is shifting to cheaper plans, and the Q3 call guided preliminary FY2027 revenue to flat [Certain]. The reverse DCF already prices shrinkage, but EV/Revenue alone gives 31.03, below the 34.66 close, so the 49.40 base depends on a DCF that assumes slow decay [Certain]. The balance sheet is stretched: net debt/EBITDA rose from 1.14x (FY2023) to 3.41x TTM, Altman Z is 0.53, and the Tigris Data purchase adds M&A risk on top [Certain]. The Direction change lines matter: TTM ROIC fell from 64.9% to 33.7% and ROCE from 74.5% to 41.4% while operating margin stayed flat. That points to a debt-funded, shrinking capital base rather than collapsing profit [Likely]. It doesn't break the thesis, but returns are inflated by buybacks, not by growth [Likely]. FCF margin is also 2.7pp below its 2-year high [Certain].
## Bull case
This is a cash machine priced for liquidation. FCF margin is 36.1%, the FCF yield is 12.27% and P/FCF is 8.2x, near its 5y low of 7.5x [Certain]. Operating margin rose from 14.2% (FY2021) to 26.6% TTM, and another ~9% workforce cut was announced [Certain]. Shares outstanding are down 18.02% YoY, so per-share FCF compounds even on flat revenue [Certain]. Q3 was a beat-and-raise, and paying users rose to 18.20 million [company-reported] [Certain]. If revenue merely holds flat rather than the shrinkage the price implies, the DCF base of 49.40 is reachable [Likely]. Insiders own 40.06%, and short interest of 17.75% of float is falling, which could fuel a squeeze [Likely].
## Decision
```json
{
  "ticker": "DBX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Dropbox is a high-margin, buyback-driven cash generator priced for decline, but flat-to-shrinking revenue, rising leverage and new AI M&A make the cheapness a value-trap risk rather than a clear mispricing.",
  "rationale": "Cheap on FCF, but the upside rests on a DCF that EV/Revenue does not confirm. Flat FY2027 guidance, rising net leverage, a weak Altman Z and a fresh acquisition leave the probability-weighted outcome only modestly above the price. That is good but not compelling, so no position.",
  "price_at_decision": 34.66,
  "price_date": "2026-11-06",
  "research_note": "research/DBX/2026-11-08.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 23%, showing cost cuts can no longer offset flat revenue", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "FCF margin falls below 32%, undermining the cash-yield thesis", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 32}},
    {"text": "Debt/EBITDA rises above 4.0x as buybacks and the Tigris deal are debt-funded", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "Paying users (10-Q key metrics) fall below 17.5 million for two consecutive quarters, excluding the FormSwift wind-down"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 49.40, "basis": "Revenue holds flat instead of the -6.4% the reverse DCF implies, and buybacks (shares -18.02% YoY [ST]) lift per-share FCF to the base fair value of 49.40 [IS,CF,RA]."},
    "base": {"probability": 0.45, "target_price_12m": 37.00, "basis": "Flat FY2027 revenue per the Q3 call (fact-sheet transcript headline [OV]); P/FCF stays below its 5y median of 10.4x [RA], and the buyback-driven per-share FCF gain adds only a modest rise above the close."},
    "bear": {"probability": 0.30, "target_price_12m": 23.69, "basis": "Paying-user conversion and renewals weaken (new 10-Q risk language, note), and net debt/EBITDA of 3.41x [BS,IS] plus Tigris M&A risk compress the value to the mechanical bear fair value of 23.69."}
  },
  "entry_price": 31.70,
  "entry_basis": "Not the default (base 49.40 x 0.8 sits above the price, because the DCF overstates a no-growth business, as EV/Revenue 31.03 shows). The entry is P/FCF back at its 5y low of 7.5x [RA] on current FCF, where the cash yield alone would compensate for flat revenue and leverage.",
  "replaces": null,
  "replacement_reason": null
}
```
