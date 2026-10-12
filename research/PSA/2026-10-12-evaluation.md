# Evaluation: Public Storage (PSA) — 2026-10-12
## Bear case
Returns are eroding: ROIC fell from 13.5% (FY21) to 11.7% TTM [Certain] (RA). PSA is buying growth with debt. Net debt/EBITDA (site definition) rose from 2.56x to 2.89x after the NSA and Canada deals and the C$400m notes, while shares are flat (+0.14% YoY) [Certain] (RA, ST). Switching costs are low, and new supply in the industry caps pricing power [Likely]. The macro overlay tilts toward bear (moderate): the 10y real yield is up 56bp in 3m and HY spreads are wider. That pushes the P/FFO multiple and refinancing costs the wrong way just as leverage climbs [Likely] (research/PSA/2026-10-12-macro.md). The FCF yield of 3.03% is thin against a 5.22% 10y Treasury [Certain] (ST, fair value section). Short interest is up 15.4% month on month [Certain] (ST). The mechanical bear fair value of 179.69 shows how far the downside could go [Certain].
## Bull case
PSA has unmatched scale and local density in self-storage [Likely]. Q2 2026 raised guidance on better move-in rates and occupancy [Certain] (OV transcript headline). EV/EBITDA of 19.3x sits at the 16th percentile of its 5y range (median 19.7x) [Certain] (RA). P/E of 27.7x is 7% below the peer median [Certain] (RA, peers). Base fair value is 330.19 (+13.9%) [Certain]. The NSA and Canada acquisitions add scale that could lift FFO once integrated [Guessing]. If real yields retrace, the REIT multiple re-rates toward base fair value [Likely] (macro overlay). Leverage of 2.89x is still moderate for a REIT [Likely]. Q3 results on 26 Oct could show integration synergies [Guessing].
## Decision
```json
{
  "ticker": "PSA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class self-storage operator at a below-median EV/EBITDA, but falling ROIC, debt-funded M&A and a rising-real-yield backdrop leave too little margin of safety for a core position.",
  "rationale": "Base upside of +13.9% is modest against a mechanical bear of -38%. ROIC is declining and leverage is rising into higher real yields (moderate bear tilt from the macro overlay). The probability-weighted 12-month value is roughly flat on the price. Good but not compelling, so AVOID; revisit nearer 264 or after integration proves out.",
  "price_at_decision": 289.86,
  "price_date": "2026-10-09",
  "research_note": "research/PSA/2026-10-12.md",
  "triggers": [
    {"text": "ROIC falls below 10% (statistics/ratios), extending the five-year decline from 13.5% to 11.7% TTM", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA (site definition, ratios page) rises above 3.5x from 2.89x TTM as acquisition debt builds"},
    {"text": "A quarterly filing (e.g. Q3 2026 on 2026-10-26) cuts full-year core FFO or occupancy guidance below the level raised with Q2 2026 results"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 345.34, "basis": "Real yields retrace and NSA/Canada integration lifts FFO, so P/FFO re-rates to the fact sheet's bull fair value of 345.34 [IS,RA,ST]. Probability cut by 0.05 for the macro overlay's moderate bear tilt (research/PSA/2026-10-12-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 295.0, "basis": "P/E holds near its 5y median of 28.0x on TTM EPS [RA], about 293-295, below the mechanical base of 330.19 because the macro overlay's higher real yields (DFII10 +56bp/3m) cap any P/FFO re-rating (research/PSA/2026-10-12-macro.md)."},
    "bear": {"probability": 0.3, "target_price_12m": 255.0, "basis": "EV/EBITDA falls to its 5y low of 17.5x [RA] on TTM EBITDA with net debt at 2.96x EBITDA [BS,IS], about 255; probability raised 0.05 for the macro overlay's moderate bear tilt. Set above the mechanical bear of 179.69 because that is a P/FFO trough that ignores the asset base."}
  },
  "entry_price": 264.15,
  "entry_basis": "Valuation file: base 330.19 x 0.8 = 264.15, which is also near EV/EBITDA's 5y low of 17.5x [RA]",
  "replaces": null,
  "replacement_reason": null
}
```
