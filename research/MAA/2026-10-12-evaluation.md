# Evaluation: Mid-America Apartment Communities (MAA) — 2026-10-12
## Bear case
MAA is a commodity landlord earning a 5.2% ROIC with ROE sliding from 9.0% (FY2021) to 7.0% TTM [Certain] (RA). Leverage is rising, not falling: net debt/EBITDA went from 3.64x (FY2023) to 4.62x TTM [Certain] (BS,IS). The macro overlay rates real yields as the primary driver and tilts toward bear (moderate): the 10y real yield is up 56bp in 3 months to 2.87% with flat breakevens, which raises cap rates and refinancing cost with no rent offset [Likely] (research/MAA/2026-10-12-macro.md). Sunbelt oversupply plausibly keeps rent growth weak, and the stock is down 14.0% over 12 months and trails SPY by 29.6pp [Certain] (HI) with short interest up 12.6% [Certain] (ST), so there is no sign yet that the trend has turned. Cash conversion can't be checked because FCF and margin data are unavailable [Certain] (CF,IS). Q3 results on Oct 28 are a near-term binary [Likely].

## Bull case
On its own history and against peers, MAA is cheap. EV/EBITDA is 15.8x, below its 5y floor of 16.0x and 17% under the 19.1x peer median, and P/B of 2.5x sits at its 5y low [Certain] (RA). The mechanical P/FFO fair value is 138.15 base and 126.35 bear, both above the 116.86 close [Certain] (fact sheet). Apartment demand is non-discretionary. At REITweek, management pointed to falling new supply and multi-year rent growth [Likely] (stockanalysis.com transcript). Redeeming the 8.50% preferred removes expensive capital [Certain] (prnewswire, fact sheet [OV]). If real yields ease, the multiple could re-rate toward its peers [Guessing].

## Decision
```json
{
  "ticker": "MAA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Sunbelt apartment REIT trading below its own 5-year EV/EBITDA and P/B floors, but low and falling returns, rising leverage and a real-rate shock make the discount a fair price for the risk rather than a mispricing.",
  "rationale": "Valuation is cheap on its own history and against peers, but the business earns a 5.2% ROIC, ROE is falling and leverage has climbed to 4.62x. The primary-weight macro overlay tilts toward bear, and the probability-weighted upside is about 8%. That is good but not compelling, so conviction is 3 and we take no position. Revisit at a deeper margin of safety.",
  "price_at_decision": 116.86,
  "price_date": "2026-10-09",
  "research_note": "research/MAA/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 5.0x (4.62x TTM), showing leverage is not stabilising.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.0}},
    {"text": "ROIC falls below 5.0% (5.2% TTM), showing supply pressure on returns is structural rather than cyclical.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5.0}},
    {"text": "ROE falls below 6.5% (7.0% TTM), extending the five-year decline from 9.0%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 6.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 146.12, "basis": "Real yields ease and Sunbelt supply falls as management outlined at REITweek, so the P/FFO multiple reaches the fact sheet's bull fair value of 146.12 [IS,RA,ST], still below the 19.1x peer EV/EBITDA median [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 126.35, "basis": "The base is set at the mechanical bear fair value of 126.35 rather than the 138.15 base, because the macro overlay's moderate tilt toward bear (real yields +56bp/3m, research/MAA/2026-10-12-macro.md) and net debt/EBITDA rising to 4.62x [BS,IS] argue against a full P/FFO re-rating."},
    "bear": {"probability": 0.3, "target_price_12m": 113.95, "basis": "Real yields keep rising and leverage pushes higher (macro overlay), so EV/EBITDA stays below its 16.0x 5y floor [RA] and the price stays near the 52-week low of 113.95 [HI]; the bear-case probability was raised for the overlay's moderate tilt toward bear."}
  },
  "entry_price": 110.52,
  "entry_basis": "valuation file: base 138.15 x 0.8; at that price the margin of safety would make up for the low ROIC and rising leverage.",
  "replaces": null,
  "replacement_reason": null
}
```
