# Evaluation: China Resources Beer (Holdings) Company Limited (HKG:0291) — 2026-11-15
## Bear case
Earnings are shrinking even as operations improve: ROE has fallen to 6.3% from 20.1% in FY2021 and net margin to 7.2% from 13.7% [Certain]. The gap to a 14.9% operating margin points to below-the-line charges whose cause is unresearched; if they recur, the P/E of 20.9x is not cheap and sits in line with peers [Likely]. ROIC of 11.9% is below the FY2022 16.0% and only moderate [Certain]. FCF conversion of 213.2% of net income may be flattered by working capital or capex under-spend [Guessing]. The price is 28.5% lower over 12 months, 11.9% below its 200-day average and trails SPY by 38.9pp, so the market is pricing weak China beer demand; the reverse DCF implies -7.0% revenue growth [Certain]. Revenue is essentially all mainland China, a single-market consumer exposure [Likely]. No catalyst until results due Mar 19, 2027 [Certain].
## Bull case
The operating business is getting better: operating margin rose to 14.9% from 9.0% in FY2021, gross margin to 42.3% from 39.2%, and FCF margin is 15.3%, up 2.4pp in the last year and at its 2-year high [Certain]. On a rolling basis ROIC, ROCE and operating margin are flat, so there is no Direction change against the thesis [Certain]. Net cash is 1.55x EBITDA [Certain]. Cash multiples sit below their own 5-year minimums: EV/EBITDA 6.0x vs a 9.1x low, P/FCF 9.8x vs 14.3x, with a 10.20% FCF yield and EV/EBITDA 7% below peers [Certain]. The price implies shrinking revenue that rising margins and cash do not show [Likely]. The mechanical base fair value of 34.15 HKD is well above the 20.46 close, even with a 3.5% country risk premium; CNY and the HKD peg are stable (macro overlay, context only) [Certain]. None of the four thesis thresholds is breached on fact-sheet figures [Certain].
## Decision
```json
{
  "ticker": "HKG:0291",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "new_evidence": {"type": "trigger_fired", "text": "The weekly tripwire flagged a core trigger on the holding bought after the 2026-11-09 BUY; HOLD is the holding's form of the unchanged conviction 4, and fact-sheet figures (https://stockanalysis.com/quote/hkg/0291/statistics/, 2026-11-15) show no threshold breached."},
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no ROIC, operating-margin or FCF-margin decline over 1 or 3 years: ROIC is flat (11.9% vs 12.4%), operating margin 14.9% and FCF margin 15.3% at its 2-year high [RA-T, IS-T, CF-T]; the ROE and net-margin fall sits below the operating line, with net cash of 1.55x EBITDA intact [BS].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "China beer demand weakens or below-the-line charges recur so that earnings keep shrinking and margins roll over; the price already implies -7.0% revenue growth.",
    "veto": null
  },
  "thesis": "A net-cash Chinese brewer with rising operating and FCF margins trades below its own 5-year minimum cash multiples, pricing shrinkage that its improving operations do not show.",
  "rationale": "No thesis threshold is breached on fact-sheet figures: operating margin 14.9%, FCF margin 15.3%, ROIC 11.9% and net cash. The net-cash trigger's statistics check likely read a gross debt ratio, so it is restated as a text trigger on the balance sheet. Evidence is unchanged since the BUY; hold at current size.",
  "price_at_decision": 20.46,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-0291/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12.0% (14.9% now), reversing the mix and pricing gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.0}},
    {"text": "TTM FCF margin falls below 10.0% (15.3% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "TTM ROIC falls below 10.0% (11.9% now), below the FY2025 low of 10.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10.0}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, balance sheet / ratios page) turns positive from -1.55x TTM, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.15, "basis": "Rising margins and the 10.20% FCF yield [ST] re-rate the stock to the mechanical base fair value of 34.15 HKD (DCF 67% + EV/EBITDA 33%) [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 28.04, "basis": "Margins hold at 14.9% operating and 15.3% FCF [IS,CF-T] and the price moves to the base DCF of 28.04 HKD, below the blend because EV/EBITDA stays under its 9.1x 5y minimum [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.74, "basis": "Below-the-line charges recur and China demand shrinks as the reverse DCF's -7.0% implies, taking the price to the mechanical bear fair value of 16.74 HKD [IS,BS,CF,RA]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is already 4, so the current price is a buy level; a lower price is not the obstacle.",
  "replaces": null,
  "replacement_reason": null
}
```
