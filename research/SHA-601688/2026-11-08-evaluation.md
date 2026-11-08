# Evaluation: Huatai Securities Co., Ltd. (SHA:601688) — 2026-11-08
## Bear case
Huatai is a cyclical, licensed broker with no durable moat: ROIC is 2.8% TTM and ROE 8.8% TTM, below the 9.6% of FY2021 [Certain]. The operating margin of 58.3% TTM is near its 2-year high of 59.5%, a market-turnover peak rather than a structural gain, so earnings are at their most flattering point [Likely]. The **Direction change** line (FCF margin 119.9pp below its 2-year high of 236.6%) is driven by trading-book and client-fund swings, not owner earnings; it does not break a thesis but shows the cash figures, and the FCFE fair value of 20.24 built on them, are unreliable [Likely]. Shares rose 4.87% YoY and a convertible issue for the overseas push adds dilution [Certain]. The share is down 16.1% over 12 months, -24.6pp vs SPY, under its 200-day average [Certain]. China policy risk carries a 3.5% country premium [Certain].

## Bull case
The price asks little: P/E 9.4x is below its 5y minimum of 9.6x and P/B 0.7x is 22% below peers [Certain]. The reverse DCF implies -1.1% year-1 revenue growth, while the operating margin rose 12.1pp over the last year and ROIC edged up 0.4pp [Certain]. The P/E cross-check gives a base of 19.13 and the blended base is 20.24, both above the 17.84 close [Certain]. Huatai sponsors large Hong Kong IPOs (Chery) in an active issuance market, and a cash dividend was declared for 2025 [Likely]. A further pickup in mainland turnover would lift earnings with high operating leverage [Guessing]. Beta of 0.60 limits market drawdown sensitivity [Certain]. Still, this is cheap-on-peak cyclicality, not a compounder at a discount.

## Decision
```json
{
  "ticker": "SHA:601688",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-return, cyclical Chinese broker trading at 0.7x book on peak-cycle margins, where the modest discount fairly prices an 8.8% ROE, dilution and policy risk rather than offering a mispriced compounder.",
  "rationale": "ROE of 8.8% and ROIC of 2.8% show no edge; margins sit near a 2-year high so earnings are cyclically flattered, shares are being diluted and the trend is down. The cash-flow-based fair value is unreliable for a broker, and the P/E cross-check offers only modest upside. Not high conviction: AVOID.",
  "price_at_decision": 17.84,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601688/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 11%, clearly above the FY2021 high of 9.6%, showing returns have structurally improved rather than tracking turnover.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 11}},
    {"text": "TTM ROIC rises above 4%, above its 2-year high of 3.4%, showing a sustained step-up in capital efficiency.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 4}},
    {"text": "Share count stops growing: shares change YoY falls below 0% (4.87% now), ending dilution from the convertible-funded overseas push.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 23.0, "basis": "Mainland turnover and Hong Kong issuance stay strong, holding the 58.3% TTM operating margin [IS-T] and P/B re-rating toward its 5y max 1.0x [RA]; below the mechanical bull of 26.62 because that FCFE value extrapolates erratic broker cash flow [CF]."},
    "base": {"probability": 0.45, "target_price_12m": 19.13, "basis": "P/E returns toward its 5y median 10.1x [RA] on flat earnings: the P/E method base of 19.13 [fact sheet Fair value], used instead of the FCFE base 20.24 because FCF conversion swings from -84.4% to 272.9% [CF,IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 14.5, "basis": "Turnover cools and the operating margin reverts from near its 59.5% 2-year high [IS-T] while P/B falls to its 5y min 0.6x [RA]; above the mechanical bear 12.50 because the FCFE bear also rests on unreliable broker cash flow [CF]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
