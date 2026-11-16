# Evaluation: Hiscox Ltd (LON:HSX) — 2026-11-16
## Bear case
The price already discounts a lot. Base fair value is 1,751.53 GBX, -10.3% below the 1,952.00 close, and P/B of 2.1x sits above its 5y max of 1.7x [Certain]. The 12-month +43.9% run and the price +12.9% above its 200-day average mean that if growth slows, the stock de-rates; the trend points are carrying the valuation [Likely]. The cycle is turning: management is tempering big-ticket growth as rates soften (Q3 call) [Likely]. Python flags a **Direction change**: ROIC is 3.2pp below its 2-year high of 17.8%, and ROE fell from 24.0% (FY2023) to 16.5% TTM [Certain]. This is the hard-market peak normalising, not a break, but a soft cycle can push it further [Likely]. Part of the May rally may be bid speculation that never got confirmed [Guessing]. The two net-debt definitions conflict and the US premium share is unverified [Certain].
## Bull case
Retail is the growth engine and it is growing: 9M premiums up 9.5%, with double-digit retail momentum in Q3 (Q3 transcript) [Likely]. Returns are real and stable on a rolling basis. ROIC TTM is 14.5%, up 0.7pp on a year earlier, versus 7.0% in FY2021 [Certain]. Buybacks cut the share count 3.35% YoY, Piotroski F is 7 and leverage is low [Certain]. P/E of 13.6x is mid-range in its own history (48%) and 14% below peers [Certain]. The FCF yield is 8.99%, though insurer cash flow is noisy [Likely]. Beta of 0.37 makes it a low-correlation compounder [Certain]. Holding back on big-ticket lines as rates soften is the underwriting discipline that keeps returns intact through the cycle [Likely].
## Decision
```json
{
  "ticker": "LON:HSX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC TTM 14.5% is up 0.7pp on a year earlier [RA-T]. It sits 3.2pp below its 2-year high of 17.8%, normalising from the FY2023 hard-market peak as reinsurance and big-ticket rates soften (Q3 call, https://stockanalysis.com/quote/lon/HSX/transcripts/761022-q3-2026-tu/), with low leverage and buybacks intact.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A softening P&C cycle compresses ROE while the price, above base fair value and +12.9% over its 200-day average after a +43.9% year, de-rates if premium growth slows.",
    "veto": null
  },
  "thesis": "A disciplined specialty and retail insurer with mid-teens returns, buybacks and growing retail premiums, but priced above its mechanical fair value as the underwriting cycle softens.",
  "rationale": "Quality and trend are good, but the price sits above base fair value and P/B is above its 5y max as the cycle softens; the scorecard gives conviction 3, below the buy bar. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 1952.00,
  "price_date": "2026-11-13",
  "research_note": "research/LON-HSX/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (14.5% now), showing the soft cycle is breaking underwriting returns rather than normalising them.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM ROE falls below 12% (16.5% now), back toward the FY2022 level.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Shares change YoY turns to dilution above +3% (-3.35% now), ending the buyback.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "Retail premium growth turns negative year on year in a trading update or results release, showing the growth engine has stalled."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 2317.21, "basis": "Retail momentum (Q3 transcript) holds ROE mid-teens and the valuation reaches the fact sheet's bull fair value of 2,317.21 GBX [IS,BS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 1900, "basis": "ROIC stays flat near 14.5% [RA-T] while softening big-ticket rates offset retail growth, so the price drifts between the base fair value of 1,751.53 and the current level [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 1485.18, "basis": "The soft cycle cuts earnings and the P/E de-rates toward its 5y median 10.3x [RA], in line with the P/E method's base value of 1,485.18 GBX."}
  },
  "entry_price": 1401.22,
  "entry_basis": "valuation file: base 1,751.53 x 0.8 (20% margin of safety); at that price the same quality evidence would carry a real discount.",
  "replaces": null,
  "replacement_reason": null
}
```
