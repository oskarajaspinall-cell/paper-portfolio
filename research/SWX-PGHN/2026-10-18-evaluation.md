# Evaluation: Partners Group Holding AG (SWX:PGHN) — 2026-10-18
## Bear case
The cheapness may be the earnings base resetting, not mispricing. H1 performance income fell sharply and the company named new co-CEOs on 2026-09-01 [Certain] (https://www.wsj.com/finance/investing/partners-group-shares-slide-after-drop-in-performance-fees-ceo-change-82686164). Quality is trending down: ROIC fell 29.3pp over five years, and operating and net margins are both lower [Certain] [RA, IS]. Leverage has moved from net cash in FY2021 to 1.76x net debt/EBITDA [Certain] [RA]. The best-method DCF base (658.11 CHF) sits only modestly above the price. Most of the blended fair-value upside comes from P/E reverting to a five-year range that a structurally lower fee mix may not earn again [Likely]. A wound-down London trust and a "flexibility" rework of the evergreen PE strategy suggest pressure from redemptions in the wealth channel [Guessing]. The macro overlay tilts small toward bear: rising yields and wider HY spreads slow the exits that crystallise carry [Likely] (2026-10-18-macro.md).
## Bull case
On every own-history multiple except P/B, PGHN trades below its five-year minimum: P/E 13.3x against a 20.2x minimum and a 28.9x peer median [Certain] [RA, P]. FCF yield is 12.33% and the share count is shrinking [Certain] [ST]. The reverse DCF implies only 1.9% year-1 revenue growth, and even the mechanical bear fair value (652.93 CHF) sits above the price [Certain] (fact sheet). Margins remain exceptional (operating 59.7% TTM) and FCF conversion is 162.8%, so management fees on long-lock AUM keep generating cash while performance fees are cyclical [Likely]. The firm is still launching products (a global private-credit strategy, 2026-10-09) [Certain] [OV]. If exits reopen, performance fees and the multiple could both recover [Guessing].
## Decision
```json
{
  "ticker": "SWX:PGHN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, cash-generative private-markets manager trades below its five-year multiple range, but falling performance fees, a leadership change, rising leverage and an adverse rate/credit backdrop leave it unclear whether the earnings base has reset lower.",
  "rationale": "Cheap on history and peers, with a 12.33% FCF yield, but the DCF base gives only modest upside; the rest depends on a P/E re-rating while returns, margins and performance fees trend down and macro tilts toward bear. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 607.40,
  "price_date": "2026-10-16",
  "research_note": "research/SWX-PGHN/2026-10-18.md",
  "triggers": [
    {"text": "TTM net margin falls below 40%, confirming structural rather than cyclical fee compression (48.0% now).", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "Net debt/EBITDA rises above 2.5x, signalling leverage is funding operations rather than temporary commitments (1.76x now).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM ROE falls below 40%, undermining the capital-light return profile (75.4% now).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 40}},
    {"text": "The next results release (around 2027-03-16) shows performance income stabilising or rising y/y with fee-earning AUM still growing, the evidence that would lift conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 854.30, "basis": "Exits reopen as yields and spreads ease (macro_bull, 2026-10-18-macro.md), performance fees recover and the stock re-rates to the blended base fair value 854.30 CHF from a 13.3x P/E against a 20.2x five-year minimum [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 658.11, "basis": "Management fees hold while performance income stays subdued after the H1 drop (WSJ, fact sheet news); the stock trades to the best-method DCF base 658.11 CHF [IS,CF], with no P/E re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 516.18, "basis": "Rising yields and wider HY spreads keep exits slow and lift the discount rate; the macro overlay's small toward-bear tilt (2026-10-18-macro.md) adds weight here, and the stock falls to the DCF bear 516.18 CHF [IS,CF] as leverage rises from 1.76x [RA]."}
  },
  "entry_price": 526.49,
  "entry_basis": "Best-method DCF base 658.11 x 0.8 [IS,CF]: the blended base (854.30) leans on a P/E reverting to a five-year range that falling fees may not support, so the DCF is the margin-of-safety anchor; the default blended base x 0.8 is above the current price.",
  "replaces": null,
  "replacement_reason": null
}
```
