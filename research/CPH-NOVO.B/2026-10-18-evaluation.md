# Evaluation: Novo Nordisk A/S (CPH:NOVO.B) — 2026-10-18
## Bear case
The cheapness is narrower than the P/E suggests. P/E 9.9x is flattered by weak cash conversion: FCF/NI has fallen to 65.1% from 101.9% in FY2021 and FCF margin to 23.0% [Certain] (CF,IS), so the FCF yield is only 6.61% [Certain] (ST) and P/FCF 15.1x [Certain] (RA). The reverse DCF shows the price already implies 7.4% year-1 revenue growth [Certain] (fact sheet fair value), which is not a collapse scenario. ROIC has fallen to 39.2% from 88.6% in FY2023 [Certain] (RA). Lilly's oral pill winning EU committee backing makes GLP-1 a real two-player price competition [Likely] (https://www.reuters.com/legal/litigation/eli-lillys-weight-loss-pill-wins-backing-europe-2026-10-16/), and TTM margins may be the peak, not the base [Guessing]. The shares are down 22.7% in 3 months with no cited cause in the research [Certain] (HI), and results arrive Nov 4, 2026 [Certain] (ST). A NAION liability suit adds an unquantified tail [Guessing].
## Bull case
Novo still earns a 49.0% operating margin, up from 42.1% in FY2021, with gross margin near 82% [Certain] (IS); returns fell because of capacity build-out, not pricing collapse [Likely] (note §5). The balance sheet is conservative at 0.55x net debt/EBITDA [Certain] (BS,IS). Every multiple sits below its own 5y minimum and below peers: EV/EBITDA 7.1x vs a 18.9x peer median [Certain] (RA, peers). Even the mechanical bear fair value of 278.08 DKK is above the 259.60 close, and the base is 515.35 [Certain] (fact sheet fair value). If capex normalises, FCF conversion recovers toward history and the cash yield rises sharply [Guessing]. Beta of 0.38 makes it a defensive diversifier [Certain] (ST); the macro tilt is neutral/small [Certain] (macro overlay).
## Decision
```json
{
  "ticker": "CPH:NOVO.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An elite-margin GLP-1 franchise trades below its own 5-year minimum multiples, but falling cash conversion and an emerging two-player price war with Lilly mean the low P/E may reflect peak earnings rather than mispricing.",
  "rationale": "Good but not compelling: margins are elite, yet the 6.61% FCF yield is modest versus holdings bought at higher yields, the reverse DCF already implies healthy growth, and the competitive trajectory is unresolved until the Nov 4, 2026 results. Cash is acceptable; re-research after the print.",
  "price_at_decision": 259.60,
  "price_date": "2026-10-16",
  "research_note": "research/CPH-NOVO.B/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 78%, from 82.0%, showing oral GLP-1 competition is damaging pricing/mix.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "TTM operating margin falls below 40%, from 49.0%, showing competitive pricing is hitting profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 low of 19.1%, showing capex is structurally outrunning earnings quality.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 369.61, "basis": "Margins hold through the Lilly launch and P/E re-rates to about its 5y minimum of 14.1x [RA], matching the P/E-method bear value of 369.61 DKK (fact sheet fair value); below the 515.35 base because a full return to the 35.1x median ignores the structural competition shift (note §2)."},
    "base": {"probability": 0.45, "target_price_12m": 278.08, "basis": "Earnings plateau as Lilly's oral pill gains EU backing (Reuters URL in fact sheet) and the stock settles near the mechanical bear fair value of 278.08 DKK (fact sheet fair value); the macro overlay's tilt is neutral/small, so probabilities are unchanged."},
    "bear": {"probability": 0.30, "target_price_12m": 232.32, "basis": "Price competition compresses margins and FCF conversion keeps falling from 65.1% [CF,IS], pulling value to the DCF bear of 232.32 DKK (fact sheet fair value), near the 52-week low of 224.25 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the base fair value less margin of safety is above the price, and the decision hinges on whether margins and cash conversion hold against Lilly's oral competition, which the Nov 4, 2026 results will show; a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
