# Evaluation: Kimberly-Clark Corporation (KMB) — 2026-10-09
## Bear case
KMB ($32.5bn market cap) is trying to absorb a roughly $40bn Kenvue acquisition, partly by assuming Kenvue's notes, so the 1.60x net debt/EBITDA and 25.4% ROIC describe a company that will not exist after closing [Certain]. EU clearance is still pending, with remedies offered [Likely]. The margin gains (gross 37.6%, up 5.7pp over 5 years) partly reflect moving international tissue into the Suzano JV, so they are not like-for-like [Likely]. The CEO is leaving after closing, which adds integration risk [Certain]. Short interest of 15.85%, up 4.8% in a month, and 35.8pp of 12-month underperformance against SPY show the market is pricing deal risk, not overlooking a bargain [Likely]. The base fair value of 97.75 equals the price, so the stock offers no margin of safety [Certain]. Rising real yields and HY spreads make the deal financing dearer (macro overlay) [Likely].
## Bull case
On standalone numbers KMB is cheap and good. P/E of 16.7x sits at the 1st percentile of its 5-year range and 38% below peers. EV/EBITDA of 10.9x is below its 5-year minimum. The FCF yield is 5.6% [Certain]. ROIC near 25%, a rising operating margin (17.4%) and 93.1% FCF conversion show that the Huggies/Kleenex brand moat is still producing cash [Certain]. The reverse DCF implies only 2.8% growth [Certain]. If Kenvue closes on reasonable terms, the combined staples and consumer-health franchise could re-rate toward peer multiples as synergies show up [Guessing]. A beta of 0.28 limits market drawdowns [Certain].
## Decision
```json
{
  "ticker": "KMB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Standalone KMB looks cheap on trailing multiples, but those figures predate a debt-funded Kenvue acquisition larger than KMB itself, and the price sits at the mechanical base fair value, so there is no margin of safety for unsized deal, leverage and integration risk.",
  "rationale": "The trailing quality and valuation data cannot capture the post-Kenvue balance sheet. Base fair value of 97.75 equals the price, and short interest is rising. Rising rates (small macro tilt toward bear) make the financing dearer. Conviction is 2, below the buy bar, so AVOID and hold cash.",
  "price_at_decision": 97.74,
  "price_date": "2026-10-08",
  "research_note": "research/KMB/2026-10-09.md",
  "triggers": [
    {"text": "The Kenvue deal closes with EU clearance needing no remedies beyond those already offered (Reuters 2026-09-23), removing the deal-completion risk."},
    {"text": "The first reported quarter after closing shows net debt/EBITDA (ratios page) below 3.0x, showing the acquisition leverage is manageable."},
    {"text": "TTM ROIC rises above the FY2024 5-year high of 27.9%, showing returns are growing despite the larger capital base.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 27.9}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 127.37, "basis": "The deal closes cleanly and the standalone discount (P/E 16.7x vs a 23.3x 5-year median [RA]) narrows, reaching the mechanical bull fair value of 127.37 [IS,BS,CF,RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 97.75, "basis": "The price already matches the mechanical base fair value of 97.75, with the reverse DCF implying 2.8% growth [IS,BS,CF,RA,ST], so integration uncertainty holds the multiple flat."},
    "bear": {"probability": 0.3, "target_price_12m": 66.95, "basis": "Post-close leverage and integration problems on a roughly $40bn debt-funded deal (Reuters 2026-09-23 URL in note) take the stock to the bear fair value of 66.95 [IS,BS,CF,RA,ST]; probability raised 5pp for the small toward-bear macro tilt from rising real yields and HY spreads (research/KMB/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
