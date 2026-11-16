# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-16
## Bear case
NetEase is a hit-driven games company, not a network-effect platform: one weak release cycle could dent the margins that drive the thesis [Likely]. China regulation of game licensing and spending is the dominant risk and cannot be modelled [Likely]. Results land on Nov 19, 2026, so the next print is a near-term event risk [Certain]. The 12-month change is -12.0%, trailing SPY by 22.4pp, and the 50-day average sits below the 200-day [Certain]; any trend-strength support is thin, and with the price only just above its 200-day average a soft print could push it back below and de-rate it if growth slows [Likely]. P/E is 25% above the peer median [Certain]. The mechanical bear value is 144.00 HKD [Certain]. Insiders own 45.32% and the share count is still up 0.39% YoY despite buybacks [Certain]. ROIC is [data unavailable] on the fiscal view.
## Bull case
Quality is high and still improving on the rolling view: operating margin 35.2% vs 31.4% a year earlier, FCF margin 43.5%, ROCE 23.3% at its 2-year high, with no Direction change flag [Certain]. Cash conversion is 156.0% of net income and net debt/EBITDA is -3.76x, a large net cash cushion [Certain]. Yet EV/EBITDA (8.7x) and P/FCF (10.6x) sit below their own 5-year minimums and EV/EBITDA is 57% below peers, with a 9.47% FCF yield [Certain]. The reverse DCF implies revenue falling 3.1% in year 1, which margins rising across every tracked measure do not support [Likely]. Base fair value is 217.15 HKD, above the 190.40 close [Certain]. Ongoing buybacks and a new Sony Music licensing deal for Cloud Music add modest support [Likely]. Macro is context only: CNY and HKD are stable (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists nothing falling: ROIC, operating margin and FCF margin are all above a year earlier on the rolling view (operating margin 35.2% vs 31.4%, FCF margin 43.5% vs 41.2%) [IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "China game regulation or a weak release cycle compresses margins; with the price only just above its 200-day average after a -12.0% year, a soft Nov 19 print could also de-rate the stock.",
    "veto": null
  },
  "thesis": "A net-cash games franchise with operating margin rising to 35.2% and a 43.5% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline its improving fundamentals do not show.",
  "rationale": "Thesis intact and unchanged since the 2026-11-15 HOLD: rising margins, net cash and multiples below their own 5-year floors. Base fair value upside is moderate and results are due Nov 19, so hold at the existing size rather than add; the China/HK cap leaves little room in any case.",
  "price_at_decision": 190.40,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-9999/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in a company filing or release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 244.07, "basis": "Margins keep expanding and the multiple recovers toward its 5y median EV/EBITDA of 10.4x [RA], matching the mechanical bull fair value 244.07 HKD [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 217.15, "basis": "Margins hold near the TTM 35.2% operating margin [IS-T] and the DCF/EV-Revenue blend base fair value 217.15 HKD is reached as the implied revenue decline fails to appear."},
    "bear": {"probability": 0.25, "target_price_12m": 144.00, "basis": "A weak release cycle or PRC game regulation compresses margins (note section 6), consistent with the mechanical bear fair value 144.00 HKD [IS,CF,RA]."}
  },
  "entry_price": 173.72,
  "entry_basis": "valuation file: base 217.15 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
