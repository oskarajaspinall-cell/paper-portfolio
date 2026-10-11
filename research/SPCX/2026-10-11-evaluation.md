# Evaluation: Space Exploration Technologies Corp. (SPCX) — 2026-10-11
## Bear case
At a 2,206.5bn USD market cap SPCX burns cash: FCF margin -141.1% TTM, operating margin -14.9% TTM against +5.3% in FY2024, and ROCE -2.0% [Certain] (IS, CF, RA). No P/E, EV/EBITDA, EV/Sales or P/FCF multiple can be computed, and the fair-value model returns no answer, so the price has no fundamental anchor we can test [Certain] (Valuation, Fair value). Shares outstanding rose 41.79% YoY and Piotroski F is only 3 [Certain] (ST). The reported spectrum purchase points to higher capex before Starlink Mobile earns anything [Guessing] (TipRanks 2026-10-09). The stock has been public for about four months and has traded between 104.83 and 225.64, so it is highly volatile [Certain] (HI). The macro overlay notes the 10y real yield rising +0.56pp over 3 months, which raises the discount rate on cash flows that are still far off [Certain] (research/SPCX/2026-10-11-macro.md).

## Bull case
Gross margin has risen for five straight years, from 41.2% to 51.9% TTM, which points to real unit-cost gains from rocket reuse and Starlink scale [Certain] (IS). The balance sheet is strong: net debt/EBITDA is -10.23x and Altman Z is 20.77, so the investment is funded by cash, not debt [Certain] (BS, RA, ST). Starlink keeps opening markets (Venezuela authorisation) and a direct-to-device mobile service is coming, both of which widen the long-run revenue base [Likely] (Reuters 2026-10-09 headline [OV]). The stock is +12.7% above its 50-day average and +3.3pp ahead of SPY over 3 months [Certain] (ST, HI). Short interest fell 6.5% in a month [Certain] (ST). If operating margin turns positive, the optionality on launch and connectivity is unmatched among peers [Guessing].

## Decision
```json
{
  "ticker": "SPCX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A world-class launch and satellite franchise with rising gross margins, but at a 2,206.5bn USD market cap with -141.1% FCF margin, -14.9% operating margin, 41.79% dilution and no computable valuation anchor, the price cannot be underwritten on fundamentals.",
  "rationale": "A core position needs a good business at an attractive price, and here the price cannot be tested at all. No multiple or fair value is computable, cash burn and dilution are getting worse, and there are only four months of trading history. Rising real yields add pressure. Conviction is 2, below the buy threshold of 4, so this is an AVOID with no position.",
  "price_at_decision": 162.57,
  "price_date": "2026-10-09",
  "research_note": "research/SPCX/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2024 level of 5.3%, showing the investment phase is turning into operating profit.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 5.3}},
    {"text": "TTM FCF margin turns positive, back above the FY2023 level of 1.0%, giving a DCF anchor for valuation.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 1.0}},
    {"text": "TTM gross margin falls below the FY2023 level of 41.2%, which would reverse the reuse cost advantage that is the core of any bull thesis.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 41.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 225.64, "basis": "Starlink Mobile and market openings keep the narrative running and the stock retests its 52-week high of 225.64 [HI], while gross margin keeps rising from 51.9% [IS]; no fair value is computable, so this is a price-history level, not a valuation."},
    "base": {"probability": 0.4, "target_price_12m": 162.57, "basis": "Cash burn (FCF margin -141.1% [CF,IS]) and dilution (41.79% YoY [ST]) offset gross-margin gains (51.9% TTM [IS]), so the price stays near the 162.57 close [HI]; the fair-value model returns no figure [Fair value], so there is no anchor to reconcile to."},
    "bear": {"probability": 0.4, "target_price_12m": 104.83, "basis": "Without a computable fair value, the stock revisits its 52-week low of 104.83 [HI] as operating losses (-14.9% TTM [IS]) persist into the Nov 17, 2026 report [ST]; probability raised by a moderate bear tilt from the macro overlay's rising 10y real yield (+0.56pp/3m, research/SPCX/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: there is no computable fair value, FCF is negative and dilution is ongoing, so a lower price alone would not raise conviction to 4. Re-research when the operating-margin or FCF-margin triggers fire.",
  "replaces": null,
  "replacement_reason": null
}
```
