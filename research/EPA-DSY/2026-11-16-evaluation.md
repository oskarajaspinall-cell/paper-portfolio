# Evaluation: Dassault Systèmes SE (EPA:DSY) — 2026-11-16
## Bear case
Growth is slow: the raised 2026 revenue target is only 4-5% (https://www.reuters.com/technology/dassault-systmes-raises-2026-growth-target-2026-10-28/) [Certain], while the reverse DCF needs 12.2% year-one growth [Certain]. The DCF base is 18.55 EUR and the blended base 24.97 sits below the 25.98 close; the fair value is flagged unreliable, so the cheap-on-history read rests on a de-rating that may be permanent as peers out-grow it [Likely]. The price is extended: +29.4% above its 200-day average, +24.2% in 3 months, RSI 66.2 [Certain]; if growth slows or ArisGlobal integration dilutes margins, the rally can unwind [Likely]. The FCF-margin direction change (five-year fall from 31.1% to 23.6%, then a rise to 27.3% TTM) is a recovery that is not yet a proven trend [Guessing]. ROCE slipped to 12.6% from 13.2% a year earlier [Certain]. Regional mix is [data unavailable].
## Bull case
A sticky, high-switching-cost franchise in design and PLM software with an 84.2% gross margin [Likely]. Quality is improving: ROIC 16.9% TTM from 10.5% in FY2021, operating margin 25.5% TTM, up 4.0pp in a year, FCF margin up 4.0pp to 27.3% [Certain]. Net cash (net debt/EBITDA -0.57x) and a shrinking share count (-0.94% YoY) [Certain]. Q3 raised full-year guidance [Likely]. The stock trades at or below the bottom of its own five-year range on P/E 26.3x, EV/EBITDA 17.3x and P/FCF 20.0x, with a 5.01% FCF yield, and at a deep discount to ADSK, PTC, CDNS and SNPS [Certain]. The FCF-margin dip looks temporary: the five-year fall starts from an inflated FY2021 and the last 12 months are rising [Likely]. Low beta 0.56 [Certain].
## Decision
```json
{
  "ticker": "EPA:DSY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin are all rising over the last 1 and 3 years [RA-T, IS-T, CF-T]; the five-year FCF-margin fall starts from an inflated FY2021 base.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Revenue growth stays at the guided 4-5% while the extended price needs more; a slowdown or ArisGlobal margin dilution would de-rate the shares.", "veto": null},
  "thesis": "An improving, net-cash design-software franchise trading at the bottom of its own multiple history, but with slow guided growth and an extended price.",
  "rationale": "Quality and balance sheet are strong and multiples sit at five-year lows, but the blended fair value is below the price, growth guidance is modest and the shares are extended after a sharp rally. Good but not compelling at this price.",
  "price_at_decision": 25.98,
  "price_date": "2026-11-13",
  "research_note": "research/EPA-DSY/2026-11-16.md",
  "triggers": [
    {"text": "Gross margin TTM falls below 80% (pricing power or mix broken).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "Operating margin TTM falls below 20% (ArisGlobal or competitive dilution).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "FCF margin TTM falls below 20%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Shares outstanding grow more than 2% YoY (acquisition-funded dilution).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 31.94, "basis": "Margin and FCF gains persist and multiples re-rate toward the mechanical bull fair value 31.94 EUR, helped by the EV/Revenue method base 37.80 [valuation file, RA]."},
    "base": {"probability": 0.5, "target_price_12m": 24.97, "basis": "Growth stays near the guided 4-5% (Reuters 2026-10-28 URL) and the shares settle at the blended base fair value 24.97 EUR [valuation file]."},
    "bear": {"probability": 0.2, "target_price_12m": 16.53, "basis": "Growth slows and the extended rally (+29.4% above the 200-day [ST,HI]) unwinds toward the mechanical bear fair value 16.53 EUR [valuation file]."}
  },
  "entry_price": 19.98,
  "entry_basis": "valuation file: base 24.97 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
