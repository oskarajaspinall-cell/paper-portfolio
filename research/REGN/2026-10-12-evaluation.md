# Evaluation: Regeneron Pharmaceuticals, Inc. (REGN) — 2026-10-12
## Bear case
Returns are in structural decline, not a dip: ROIC 60.1% to 13.5%, gross margin 67.0% to 44.5%, operating margin 56.0% to 26.9% from FY2021 to TTM, falling every year [Certain] [RA, IS]. Legacy Eylea is eroding to Eylea HD and competitors, and Dupixent, the remaining engine, is profit-shared with Sanofi, so Regeneron does not capture its full upside [Certain] (SEC 10-K). The new Sanofi immunology assets will not have pivotal data before 2027-28 [Likely]. The stock is not cheap against its own history: P/E 18.5x and P/FCF 19.8x sit above their 5y medians [Certain] [RA]. Base fair value of 780.30 is only +4.5% above 746.54, while bear is -11.8% [Certain]. Piotroski F of 5 fits a business past peak margins [Likely]. The Q3 report on Oct 30, 2026 could show further margin compression [Guessing].

## Bull case
The balance sheet holds net cash on both definitions (net debt/EBITDA -1.12x), Altman Z is 6.47 and FCF conversion is 86.9% [Certain] [BS, ST, CF]. Shares fell 4.76% YoY as buybacks continue [Certain] [ST]. On a peer basis REGN is cheap: P/E 18.5x vs a 29.7x median, EV/Sales 3.8x vs 6.9x, and P/B 2.4x is below its 5y minimum [Certain] [RA]. TTM operating margin of 26.9% is a tick above FY2025's 25.8%, which hints that the erosion may be bottoming [Likely] [IS]. The Sanofi deal brings $1bn upfront and shares long-acting immunology costs [Certain] (Reuters). Trevogrumab's muscle-preservation data with GLP-1s and ubamatamab's early responses give the pipeline optionality [Likely]. If that optionality comes through, the bull fair value of 937.17 (+25.5%) is reachable [Guessing].

## Decision
```json
{
  "ticker": "REGN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash biologics franchise that is cheap against peers but fairly priced against its own history, with returns and margins still falling as Eylea erodes and Dupixent economics are shared with Sanofi.",
  "rationale": "Base fair value is only +4.5% above the price, and the bear case is -11.8%. Margins and ROIC have fallen for five straight years, and the pipeline catalysts are 2027-28 events. The balance sheet and buybacks limit the downside but do not create a compelling asymmetry. That is good but not compelling, so the decision is AVOID until price or fundamentals improve.",
  "price_at_decision": 746.54,
  "price_date": "2026-10-09",
  "research_note": "research/REGN/2026-10-12.md",
  "triggers": [
    {"text": "TTM gross margin recovers above 48%, showing the Eylea-driven margin erosion has bottomed and reversed.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 48}},
    {"text": "TTM ROIC rises back above the FY2024 level of 18.6%, showing returns have stopped falling.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 18.6}},
    {"text": "TTM operating margin rises back above the FY2023 level of 32.3%, showing Dupixent and Eylea HD growth are outpacing legacy Eylea erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 32.3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 937.17, "basis": "Margins stabilise, as hinted by TTM operating margin of 26.9% vs FY2025's 25.8% [IS], and EV/Sales re-rates from 3.8x toward its 5y median of 4.4x [RA], which is the own-history bull fair value."},
    "base": {"probability": 0.45, "target_price_12m": 780.30, "basis": "EV/Sales holds near its own-history base and buybacks (shares -4.76% YoY [ST]) offset continued Eylea erosion, giving the fact sheet's base fair value."},
    "bear": {"probability": 0.30, "target_price_12m": 658.69, "basis": "Gross margin keeps falling on its five-year path from 67.0% to 44.5% [IS], and the multiple settles near the bottom of its 5y EV/Sales range of 3.6x [RA], giving the own-history bear fair value."}
  },
  "entry_price": 624.24,
  "entry_basis": "valuation file: base 780.30 x 0.8; at that level the net-cash balance sheet and buybacks would give enough margin of safety against continued margin erosion to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
