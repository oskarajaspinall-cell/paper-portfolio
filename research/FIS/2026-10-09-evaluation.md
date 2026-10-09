# Evaluation: Fidelity National Information Services, Inc. (FIS) — 2026-10-09
## Bear case
FIS has re-levered again: net debt/EBITDA is 5.82x TTM, up from 4.06x at FY2025, after ~$7.7bn of new debt bought Issuer Solutions [Certain]. Altman Z is 0.35 and Piotroski F is 4 [Certain]. The 15.94% FCF yield looks large, but most of the enterprise value is debt, so a small fall in EBITDA or a small rise in refinancing cost hits the equity hard [Likely]. FCF margin has dropped from 48.1% to 23.1% and the TTM 27.6% net margin comes from Worldpay gains, not operations [Certain]. Real yields rose 0.61pp and HY spreads rose 0.39pp over three months, which works directly against this balance sheet (macro overlay, moderate tilt toward bear) [Certain]. The price is 25.6% below its 200-day average and down 49.9% over 12 months, while short interest rose 16.5% [Certain]. Integration risk is not yet visible in reported numbers [Guessing].

## Bull case
This is mission-critical bank core software on multi-year contracts with high retention (10-K) [Likely]. Operating margin rose from 15.3% to 21.7% and ROIC from 0.9% to 6.6% [Certain]. Every multiple sits below its own 5-year minimum, and P/FCF is 6.3x against a 15.8x peer median [Certain]. The reverse DCF implies a -11.9% revenue decline. Record core-banking wins and Gartner Leader status (Business Wire) point the other way [Likely]. Even the mechanical bear fair value of 59.49 is 73.2% above the 34.34 close [Certain]. Buybacks continue, with shares down 2.80% YoY [Certain]. If leverage falls back toward ~4x after the November 4 results, the equity re-rates sharply [Guessing].

## Decision
```json
{
  "ticker": "FIS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A sticky bank-core-software franchise with rising operating margins trades below every 5-year multiple floor, but 5.82x leverage, a 0.35 Altman Z and rising real yields make the cheapness a balance-sheet bet rather than a quality-at-a-discount one.",
  "rationale": "The valuation is compelling, but the equity is a leveraged stub on freshly debt-funded M&A. The distress-zone Z-score and falling FCF margin are not yet offset by evidence of deleveraging, and the macro tilt moves against it. That is good but not compelling, so conviction is 3: AVOID. Revisit after Nov 4 results show leverage falling.",
  "price_at_decision": 34.34,
  "price_date": "2026-10-08",
  "research_note": "research/FIS/2026-10-09.md",
  "triggers": [
    {"text": "Debt/EBITDA (statistics page) falls below 4.0x, back toward the FY2025 4.06x, showing Issuer Solutions deleveraging is on track.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 4.0}},
    {"text": "TTM FCF margin rises above 27%, reversing the fall from FY2025 24.9% to TTM 23.1% and showing integration costs are running off.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 27}},
    {"text": "TTM operating margin rises above 23%, beating the FY2024 high of 22.9% and showing Issuer Solutions adds to margins.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 23}},
    {"text": "Banking Solutions and Capital Market Solutions both report positive revenue growth for two consecutive quarters (10-Q segment disclosure), refuting the -11.9% decline the reverse DCF implies."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 59.49, "basis": "Leverage falls toward ~4x and the market re-rates the stock to the mechanical bear fair value of 59.49 [ST,RA]. That is roughly EV/EBITDA back to its 14.9x 5y minimum [RA] from 10.8x, magnified by debt."},
    "base": {"probability": 0.45, "target_price_12m": 40.0, "basis": "EV/EBITDA moves partway toward the 12.0x peer median [RA,P:FI] on stable TTM EBITDA [IS]. The 5.82x leverage [BS,IS] keeps the stock well below the 99.35 DCF-led base fair value, which ignores integration and refinancing risk."},
    "bear": {"probability": 0.35, "target_price_12m": 26.0, "basis": "Deleveraging stalls as real yields and HY spreads keep rising (macro overlay research/FIS/2026-10-09-macro.md, moderate tilt toward bear moved weight to this case). EV/EBITDA compresses further from 10.8x [RA], and with debt over half of EV the equity falls disproportionately."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
