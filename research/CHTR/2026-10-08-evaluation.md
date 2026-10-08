# Evaluation: Charter Communications, Inc. (CHTR) — 2026-10-08
## Bear case
This is a levered equity stub, not a cheap compounder. Net debt/EBITDA is 4.41x against 5.2x EV/EBITDA, so small changes in the multiple swing the equity violently [Certain] (ratios page). Altman Z of 0.67 sits in the distress zone [Certain] (statistics page). ROIC has been flat at roughly 8.5% for five years, and FCF margin has fallen from 16.6% to 8.0% [Certain] (ratios, cash flow statement). The moat is being squeezed by fiber at the top and fixed wireless/satellite at the bottom [Likely]. The CFO leaves on October 15, in the middle of the Cox integration [Certain] (PRNewswire). Short interest of 13.93% is still rising [Certain] (statistics page). Real yields and HY spreads have moved higher over 1-3 months, which raises the cost of capital for this balance sheet [Likely] (macro overlay). The low P/E reflects risk the market can see, not neglect [Likely].

## Bull case
Every multiple is below its own 5-year minimum: P/E 2.8x, EV/EBITDA 5.2x and P/B 0.8x, with a 24.91% FCF yield [Certain] (ratios, statistics pages). Gross and operating margins are still rising, to 55.2% and 24.0% [Certain] (income statement). Piotroski F-score is 6, so this is not deteriorating in real time [Certain]. Management guides capex down as the rural build and network upgrade finish, which would mechanically lift FCF margin [Likely] (Goldman Communacopia transcript). Cox adds scale and guided synergies of more than $1bn [Likely] (transcript). The share count fell 11.01% YoY, so cash is going to equity holders [Certain] (statistics page). Because the balance sheet is levered, even a re-rating back to the 5-year minimum EV/EBITDA would lift the equity sharply [Likely].

## Decision
```json
{
  "ticker": "CHTR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Charter is optically very cheap on every multiple, but flat 8.5% ROIC, a falling FCF margin, 4.41x leverage with an Altman Z of 0.67, a mid-integration CFO exit and an adverse rates/credit backdrop make it a distressed-value bet rather than a high-conviction core position.",
  "rationale": "The cheapness is real but explained: high leverage, distress-zone Z-score, structurally contested broadband and FCF margin halved over five years. The capex-decline and Cox-synergy recovery is guided, not yet shown, and the CFO is leaving mid-integration. The macro tilt is moderately bearish. Conviction is 2, below the owner's buy threshold, so we avoid.",
  "price_at_decision": 106.96,
  "price_date": "2026-10-07",
  "research_note": "research/CHTR/2026-10-08.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above the FY2022 level of 10.3%, showing the capex decline is turning into cash rather than staying structural.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 10.3}},
    {"text": "TTM ROIC rises above the FY2024 five-year high of 9.0%, showing Cox synergies are lifting returns rather than just adding scale.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.0}},
    {"text": "The Q3 2026 release (Nov 6, 2026) or later shows broadband subscriber losses stabilising, with Cox synergy delivery on track against the >$1bn guide under the new CFO."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 188.0, "basis": "Capex decline and Cox synergies restore confidence and EV/EBITDA returns to its 5y minimum of 5.8x [RA] from 5.2x; with net debt/EBITDA at 4.41x [BS,IS], most of the EV gain goes to the equity."},
    "base": {"probability": 0.45, "target_price_12m": 115.0, "basis": "EV/EBITDA stays near 5.2x [RA] with flat operating margins (24.0% [IS]); the 24.91% FCF yield [ST] goes into buybacks and debt reduction, offset by continued subscriber pressure, for a modest equity gain."},
    "bear": {"probability": 0.35, "target_price_12m": 55.0, "basis": "Competitive erosion and integration slippage push EV/EBITDA down toward 4.8x against 4.41x net debt/EBITDA [BS,IS] and an Altman Z of 0.67 [ST]; probability raised by the macro overlay's moderate bear tilt from higher real yields and HY spreads (research/CHTR/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
