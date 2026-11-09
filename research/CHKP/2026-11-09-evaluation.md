# Evaluation: Check Point Software Technologies Ltd. (CHKP) — 2026-11-09
## Bear case
Profitability is eroding, not dipping. Operating margin has fallen every fiscal year from 41.9% (FY2021) to 28.3% TTM, and the rolling view confirms it: down 3.5pp in the last 12 months and 6.3pp below its 2-year high [IS-T] [Certain]. TTM ROIC halved from 58.4% to 29.9% and ROCE fell to 13.7% [RA-T] [Certain]. Q3 revenue fell 1% YoY while security peers grow, which reads as share loss in the core firewall franchise rather than a cyclical trough [Likely]. "Q3 is the trough" is management's claim, not yet evidence [Guessing]. Cheapness is partly a value trap: P/E 17.3x below its 5y minimum is earned by a shrinking-margin business, and the mechanical bear fair value of 146.60 sits barely above the price, so the reverse DCF's 1.6% growth may be fair [Likely]. Israel-based operations add geopolitical exposure [Guessing].
## Bull case
A net-cash franchise (site net debt/EBITDA -2.63x, Altman Z 5.89) converting 128.7% of net income to FCF at a 40.9% FCF margin and 87.2% gross margin [CF,IS,ST] [Certain]. FCF yield is 7.65% and the share count fell 5.13% YoY, so buybacks compound per-share value even with flat revenue [ST] [Certain]. P/FCF 13.1x sits at the bottom of its 5y range and EV/Sales below its minimum [RA] [Certain]. Subscription revenue grew 11% in Q3 and adjusted FCF beat the guidance midpoint; the hardware-to-subscription shift (Firewall-as-a-Subscription) depresses reported revenue and margin temporarily [OV transcript] [Likely]. The price implies only 1.6% growth; a stabilising margin would re-rate toward the base fair value of 165.93 [Likely]. The FCF margin has barely moved (-1.4pp in 12 months), so cash economics are intact [CF-T] [Certain].
## Decision
```json
{
  "ticker": "CHKP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "Operating margin has fallen every fiscal year from 41.9% (FY2021) to 28.3% TTM [IS] and Q3 revenue fell 1% YoY while peers grow (Q3 2026 transcript, https://stockanalysis.com/stocks/chkp/transcripts/719828-q3-2026/); the 'trough' is a management claim not yet visible in the data, and FCF margin is only modestly lower.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Continued share loss in network security to platform peers keeps revenue flat-to-down and operating margin falling below 25%, making the low multiple a value trap.",
    "veto": null
  },
  "thesis": "A net-cash, 40.9%-FCF-margin security franchise trading at the bottom of its own P/FCF range, but with operating margin and ROIC still falling and revenue now declining, so cheapness does not yet compensate for an unproven trough.",
  "rationale": "Cash generation, buybacks and the balance sheet are excellent and the multiple is low, but operating margin has fallen for five years, revenue is now shrinking and the trough is only a management claim. Base fair value offers modest upside and the bear sits near the price: good but not compelling, so AVOID.",
  "price_at_decision": 144.17,
  "price_date": "2026-11-06",
  "research_note": "research/CHKP/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25% (28.3% now), showing the margin erosion is continuing rather than troughing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 36% (40.9% now), showing the cash economics are breaking, not just reported margin.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36}},
    {"text": "TTM gross margin falls below 84% (87.2% now), signalling pricing pressure from platform competitors.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 84}},
    {"text": "Quarterly revenue on the income-statement page returns to year-on-year growth for two consecutive quarters after Q4 2026 with operating margin stable, confirming the stated Q3 trough (would argue for re-research toward a BUY)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 182.65, "basis": "Subscription growth (11% in Q3, transcript) restores revenue growth and EV/Sales returns from 4.6x toward its 5y range, matching the EV/Revenue base value of 182.65 [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 157.56, "basis": "Margins stabilise near 28.3% TTM and buybacks continue; the DCF base of 157.56 is used rather than the blended 165.93 because the EV/Revenue leg assumes a return to historic sales multiples the falling margin does not yet justify [IS-T,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 125.72, "basis": "Revenue keeps declining and operating margin falls toward 25%, so the price revisits the September swing low of 125.72 [HI], below the mechanical bear of 146.60 which assumes the margin decline stops."}
  },
  "entry_price": 132.74,
  "entry_basis": "valuation file: base 165.93 x 0.8, the default 20% margin of safety; at that level the shrinking-margin risk would be priced in with the FCF yield well above its history.",
  "replaces": null,
  "replacement_reason": null
}
```
