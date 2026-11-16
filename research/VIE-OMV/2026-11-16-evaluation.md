# Evaluation: OMV Aktiengesellschaft (OMV) — 2026-11-16
## Bear case
The TTM recovery is a commodity spike, not a better business. ROIC rose from 7.4% to 10.7% and FCF margin from 2.9% to 9.0% over the last 12 months on higher energy prices and exceptional refining margins, while operating margin slipped from 18.3% to 17.4% [Certain]. Brent has already round-tripped from $129.95 to $92.14 (macro overlay, FRED), so Q4/Q1 prints face a peak base [Likely]. The 5-year fiscal trend is falling on ROIC, ROCE and FCF margin [Certain]. EV/EBITDA 4.4x sits at 96% of its 5y range and P/B is above its 5y max, so the extended price (+16.1% over the 200-day, +49.8% in 12 months) risks a de-rating as earnings normalise [Likely]. The fair value rests on one DCF with a very wide bear-to-bull spread; SOTP/NAV are unavailable [Certain]. Altman Z 2.00 is weak; no moat beyond integration scale [Likely]. Neptun Deep carries Romania execution and fiscal risk, unverified [Guessing].

## Bull case
OMV is cheap on most lenses: P/E 7.6x versus a 9.8x peer median and 30% into its 5y range, with a 10.60% FCF yield [Certain]. The balance sheet is sound at 0.66x net debt/EBITDA and Piotroski F 7 [Certain]. The reverse DCF already prices -9.7% year-1 revenue growth, so a fade is partly in the price [Certain]. Mechanical DCF base 93.41 EUR sits above the 73.35 close [Certain]. Growth projects (Neptun Deep, Borouge International, sustainable fuels) aim at structural FCF growth independent of the spike (Q3 call / Oct 2026 conference transcripts) [Likely]. The stock is in a healthy uptrend, beating SPY by +39.4pp over 12 months, with low beta 0.20 [Certain]. A renewed Middle East supply shock would re-lift margins [Guessing].

## Decision
```json
{
  "ticker": "VIE:OMV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years. The 5-year fiscal fall is the normalisation from the FY2022 price peak, and the last 12 months are rising again on prices (Q3 2026 call, https://stockanalysis.com/quote/vie/OMV/transcripts/632415-q3-2026/) with the balance sheet intact (net debt/EBITDA 0.66x [RA]).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Brent and refining margins normalise from the Iran-war spike (Brent already back to $92.14 from $129.95, macro overlay), taking TTM FCF margin and ROIC back toward FY2025 levels and de-rating a multiple at the top of its 5y range.",
    "veto": null
  },
  "thesis": "A cheap, well-financed integrated oil major whose current returns are inflated by a commodity and refining-margin spike that is already reversing.",
  "rationale": "Cheap on P/E and FCF yield with a sound balance sheet, but TTM profitability is cycle-peak, there is no moat, the multiple sits near its 5y high and Brent has already given back the spike. Good but not compelling: AVOID; cash is an acceptable outcome.",
  "price_at_decision": 73.35,
  "price_date": "2026-11-13",
  "research_note": "research/VIE-OMV/2026-11-16.md",
  "triggers": [
    {"text": "ROIC TTM falls below 7% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "FCF margin TTM falls below 4%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt / EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Operating margin TTM falls below 12%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 90.0, "basis": "Middle East disruption persists and FCF margin holds near 9.0% TTM [CF-T,IS-T]; price moves toward but below the DCF base 93.41 [fact sheet fair value], as SOTP/NAV are unavailable to confirm it."},
    "base": {"probability": 0.5, "target_price_12m": 70.0, "basis": "Partial fade already priced (reverse DCF -9.7% year-1 revenue [fact sheet]); earnings ease from the spike and EV/EBITDA drifts from 4.4x toward its 3.4x 5y median [RA], offset by Neptun Deep progress; below the DCF base because that model capitalises peak TTM cash flow."},
    "bear": {"probability": 0.3, "target_price_12m": 54.0, "basis": "Brent normalisation (macro overlay tilt toward bear, small, raising this probability) takes FCF margin back toward FY2025 5.8% [CF,IS] and the price back near the 6-month low of 53.90 [HI]; above the mechanical bear 26.36, which assumes a deeper collapse than the balance sheet implies."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades on a low P/E with a high FCF yield; the issue is cycle-peak profitability and no moat, so a lower price on the same evidence would not lift conviction to 4. (Valuation file: base 93.41 x 0.8 sits above the current price.)",
  "replaces": null,
  "replacement_reason": null
}
```
