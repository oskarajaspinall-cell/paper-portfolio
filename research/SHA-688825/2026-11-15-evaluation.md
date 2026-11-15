# Evaluation: CXMT Corporation (SHA:688825) — 2026-11-15
## Bear case
Commodity memory maker whose profits look like a cyclical price spike rather than durable returns [Likely]. Operating margin went from -25.3% in FY2024 to 79.5% TTM, and ROIC from 4.7% in FY2025 to 97.9% TTM [IS-T] [RA-T] [Certain]. FY2022-FY2024 were all loss-making with negative FCF, so there is no through-cycle record [CF] [Certain]. The 8.39% FCF yield [ST] rests on one spike year, since FCF margin was -21.4% in FY2025 [CF] [Certain]. Shares rose 19.71% YoY [ST], so holders are being diluted [Certain]. No fair value, multiple or 5y range can be computed, so no margin of safety can be shown [Certain]. The price is 18.6% below its 50-day average and down 24.4% over 3 months [HI], which may mean the market is pricing a peak in memory earnings [Likely]. China policy and export-control risk sit on top of this [Guessing].

## Bull case
The balance sheet is now clean: net debt/EBITDA is -0.81x TTM and Altman Z is 11.54 [BS] [ST] [Certain]. TTM cash conversion is strong at 163.6% of net income [CF] [Certain]. If memory pricing stays firm, an 8.39% FCF yield on a 2,714.0bn CNY market cap is cheap for a business earning 97.9% ROIC [ST] [RA] [Likely]. Scarce domestic supply inside China may protect volume against foreign rivals [Guessing]. After the pullback toward its 52-week low of 38.11 [HI], the price may already discount some normalisation [Guessing]. The Q3 2026 report filed on 2026-10-30 drew no flagged price reaction, so nothing new appears to have broken [OV] [Likely].

## Decision
```json
{
  "ticker": "SHA:688825",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No ROIC, operating margin or FCF margin decline: all rose over the last year (fact sheet, Recent direction).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Peak-cycle memory profits: the TTM margins are a one-year spike after three loss-making years, and a fall in memory pricing would remove most of the earnings and FCF.",
    "veto": null
  },
  "thesis": "A Chinese memory maker earning spike-level TTM returns after three loss years, with no computable fair value or through-cycle record to show a margin of safety.",
  "rationale": "Scorecard conviction 3, below the buy bar: peak-cycle profits, dilution of 19.71% YoY, no moat evidence and no valuation anchor. A falling price is not a reason to buy, and a lower price would not fix the missing through-cycle evidence. Cash is the better outcome.",
  "price_at_decision": 39.98,
  "price_date": "2026-11-13",
  "research_note": "research/SHA-688825/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 40%, showing the price spike is reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "FCF margin (TTM) falls below 30%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "ROIC (TTM) falls below 15%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Shares outstanding rise a further 10% or more in a year.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 61.80, "basis": "Memory pricing holds and TTM operating margin of 79.5% [IS-T] persists, so the price retests its 52-week high of 61.80 [HI]; no fair value is computable to cross-check."},
    "base": {"probability": 0.4, "target_price_12m": 44.95, "basis": "Margins ease from the one-year spike but stay profitable; the price recovers to the recent swing high of 44.95 [HI], with no mechanical fair value available to reconcile against."},
    "bear": {"probability": 0.35, "target_price_12m": 38.11, "basis": "Memory pricing turns and the FCF margin falls back toward FY2025's -21.4% [CF], so the price revisits its 52-week low of 38.11 [HI] or lower."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: no fair value or through-cycle record can be computed and profits look peak-cyclical, so a lower price would not change the decision until a full cycle of returns is visible.",
  "replaces": null,
  "replacement_reason": null
}
```
