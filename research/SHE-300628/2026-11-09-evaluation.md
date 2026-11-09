# Evaluation: Yealink Network Technology Co., Ltd. (SHE:300628) — 2026-11-09
## Bear case
Cash is not keeping up with profit. TTM FCF margin fell from 33.0% to 26.2% in a year and sits 20.6pp below its 2-year high, and FCF conversion is 60.8% of net income against 89.5% in FY2024 [Certain]. ROIC is down 8.7pp in the last 12 months [Certain]. The cause is unexplained by allowed sources; if it reflects receivables or inventory build to hold volume in a softening enterprise-hardware market, the 45.7% operating margin overstates cash earning power [Guessing]. On cash multiples the stock is not cheap: P/FCF 28.2x sits above its 5y median and 32% above peers, and the FCF yield is 3.54% [Certain]. The mechanical base fair value of 28.29 CNY is well below the 39.59 close, and the reverse DCF needs 28.4% first-year revenue growth [Certain], though the method spread flags it unreliable. Revenue mix by country is unverified, and insiders control 60.25% [Certain].
## Bull case
This is an exceptional franchise on accounting returns: TTM ROIC 67.2%, ROE 32.4%, gross margin 63.9%, operating margin 45.7% and rising on a year earlier (+2.2pp), ROCE at its 2-year high of 33.2% [Certain]. The balance sheet is net cash (net debt/EBITDA -1.58x, Altman Z 31.56) and shares are flat [Certain]. Because operating margin and ROCE are rising while ROIC and FCF margin fall, the decline looks like working capital or cash build in the denominator, not an eroding P&L [Likely]. P/E 17.0x and EV/EBITDA 14.1x are below their 5y minimums and 19-25% below the peer median [Certain]; a return to the 5y median EV/EBITDA (EV/EBITDA method base 45.47 CNY) is upside without needing growth [Likely]. The DCF base of 19.70 CNY is depressed by the 3.5% China premium on a business with beta 0.53 [Likely].
## Decision
```json
{
  "ticker": "SHE:300628",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and FCF margin fall while TTM operating margin rose +2.2pp to 45.7% [IS-T] and ROCE rose to its 2-year high of 33.2% [RA-T], pointing to working-capital/cash build rather than P&L erosion; cause not confirmed by a primary source (note section 2).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Cash conversion keeps slipping (FCF/NI 60.8% vs 89.5% FY2024) because of receivables/inventory build in a softening enterprise-hardware market, meaning reported margins overstate cash earnings.",
    "veto": null
  },
  "thesis": "A net-cash, very high-return communication-equipment franchise trades below its own 5-year minimum P/E and EV/EBITDA, but falling cash conversion keeps cash multiples full and the mechanical fair value below the price.",
  "rationale": "Quality and balance sheet are excellent and earnings multiples are at five-year lows, but the unexplained FCF-margin and ROIC slide, a P/FCF above its 5y median and a blended fair value below the price leave the skew balanced, not compelling. Scorecard conviction 3: AVOID, with an entry price.",
  "price_at_decision": 39.59,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-300628/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 40%, under the five-year range (42.6%-46.2%), showing the hardware franchise is losing pricing power.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 20%, showing the cash-conversion slip is deepening rather than reversing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 50%, a further break from the 67.2% TTM level.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "TTM gross margin falls below 60%, under the FY2021 five-year low of 61.3%, signalling competitive price pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.47, "basis": "EV/EBITDA re-rates from 14.1x toward its 5y median 16.5x [RA] as FCF conversion recovers, matching the EV/EBITDA method base of 45.47 CNY in the fair value section."},
    "base": {"probability": 0.45, "target_price_12m": 39.59, "basis": "Operating margin holds near 45.7% [IS-T] but P/FCF stays above its 5y median [RA] while conversion is unexplained, so the P/E of 17.0x [RA] holds and the price is roughly unchanged; above the blended base 28.29 because the DCF is depressed by the 3.5% CNY premium."},
    "bear": {"probability": 0.30, "target_price_12m": 22.74, "basis": "FCF margin keeps falling from 26.2% [CF-T] and the market values the stock on cash flow, converging on the mechanical bear fair value of 22.74 CNY."}
  },
  "entry_price": 22.63,
  "entry_basis": "valuation file: base 28.29 x 0.8; at that price the same evidence (cash-conversion uncertainty) would be offset by a clear margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```
