# Evaluation: PDD Holdings Inc. (PDD) — 2026-10-07

## Bear case
Returns are falling, not just low-rated: ROE fell from 44.9% (FY2024) to 22.7% TTM, ROCE from 34.2% to 21.9%, and gross margin from 66.2% (FY2021) to 56.3% [Certain]. Domestic subsidy wars with Alibaba and JD look structural, and Temu's growth depends on tariff and de-minimis rules PDD cannot control; the EU's €3 parcel fee is a first step [Likely]. Substantially all revenue comes from Chinese merchants, with no dividend or buyback, so the net cash may never reach minority holders [Certain]. A P/E of 8.6x may be a value trap if returns keep sliding toward peer levels [Guessing]. The shares are -41.6% over 12 months with the 50-day below the 200-day, so the market has not yet found a floor [Certain].

## Bull case
Even after the compression, PDD earns a 24.6% TTM FCF margin, a 21.9% operating margin and 22.7% ROE, with net cash of 4.56x EBITDA and an Altman Z of 5.53 [Certain]. Valuation sits below its own 5-year low on P/E, EV/EBITDA, EV/Sales and P/B; the FCF yield is 14.8% and EV/EBITDA of 3.1x is 84% below the BABA/JD/MELI/SE median [Certain]. At these multiples the price already assumes a further severe decline in returns. Any stabilisation in gross margin would give a large re-rating, while the cash pile protects the downside [Likely]. FCF conversion still runs above 100% (120.3% TTM), so earnings are backed by cash [Certain].

## Decision
```json
{
  "ticker": "PDD",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 3,
  "thesis": "A net-cash, still highly cash-generative marketplace priced below its own 5-year-low multiples, which already discounts more erosion in returns than the fundamentals show.",
  "rationale": "A 14.8% FCF yield, net cash and 22.7% ROE give a margin of safety. Falling margins, China/VIE governance and Temu's tariff exposure, with no capital returns, cap conviction at 3 (5%), not more. The portfolio is all cash, so no limit is breached.",
  "price_at_decision": 78.40,
  "price_date": "2026-10-06",
  "research_note": "research/PDD/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin falls below 50% TTM: subsidy competition is structurally eroding the model.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "ROE falls below 15%: the Pinduoduo flywheel has lost its return advantage over peers.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "FCF margin falls below 15%: cash generation no longer supports the valuation case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Balance sheet turns net debt (net debt/EBITDA above zero) or FCF/NI stays below 100% for two consecutive fiscal years."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```
