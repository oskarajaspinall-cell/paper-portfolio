# Evaluation: SM Investments Corporation (PSE:SM) — 2026-11-07
## Bear case
The cheapness is largely sector-wide: P/E 7.3x sits roughly in line with the Philippine conglomerate peer median of 7.5x, EV/EBITDA is above peers and P/B 0.7x is well above the peer 0.4x [Certain]. So a re-rating needs the whole local market to recover, not SM alone [Likely]. The mechanical DCF runs on consolidated FCF and probably overstates a family-controlled holding company that trades at a persistent discount [Guessing]. Altman Z of 1.81 and Piotroski F of 5 show a balance sheet that is not pristine, and consolidated bank and property leverage may flatter the leverage and FCF comparisons [Likely]. Insiders own 44.24% and institutions only 6.0%, so minority holders depend on the family's capital choices [Certain]. The note has no segment mix or primary-source check [Certain]. Results land on Nov 11, 2026, and the stock is down 22.3% over 12 months with the 50-day below the 200-day average [Certain].
## Bull case
Fundamentals have improved steadily for five years: ROIC up from 7.5% to 10.0%, operating margin from 20.0% to 23.6%, FCF margin from 8.0% to 16.0%, and FCF/net income of 119.5% TTM [Certain]. Net debt/EBITDA fell from 3.88x to 2.53x and the share count is shrinking slightly [Certain]. Every multiple is below its own five-year minimum, with a 16.46% FCF yield, and the reverse DCF implies a -15.4% year-1 revenue decline that these margins do not suggest [Certain]. Even the mechanical bear fair value of 905.49 PHP sits well above the 561.00 close [Certain]. A beta of 0.38 makes it a diversifier for the portfolio [Certain]. If domestic consumption holds up, the falling multiples and rising returns reverse together [Guessing].
## Decision
```json
{
  "ticker": "PSE:SM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging Philippine conglomerate with five years of rising ROIC and margins trades below its own 5-year minimum multiples at a 16.46% FCF yield, but in line with equally de-rated local peers and with an unverified holding-company discount.",
  "rationale": "Quality trend and cash conversion are real, but the discount is sector-wide, the DCF likely overstates a family-controlled holdco, the segment mix and leverage are unverified from primary sources, and results are due Nov 11, 2026. Good but not compelling: conviction 3, AVOID; cash is acceptable.",
  "price_at_decision": 561.00,
  "price_date": "2026-11-06",
  "research_note": "research/PSE-SM/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20%, erasing the five-year expansion from 20.0% (FY2021) to 23.6%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 8%, giving up most of the improvement from 7.5% (FY2021) to 10.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 10%, showing the cash-conversion step-up (16.0% TTM vs 8.0% in FY2021) was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA on the ratios page rises back above 3.0x (2.53x TTM), reversing the deleveraging."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 720, "basis": "Rising ROIC and margins [RA,IS] pull P/E back to its 5y minimum of 9.4x [RA]; still below the mechanical bear fair value 905.49 because the DCF on consolidated FCF likely overstates a holdco (note section 3)."},
    "base": {"probability": 0.50, "target_price_12m": 600, "basis": "P/E stays near the de-rated peer median of 7.5x [RA, peers] with modest earnings growth, as the sector-wide discount persists (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 470, "basis": "Weak results on Nov 11, 2026 [OV] or wider holdco discount push the price back toward the 52-week low of 486.20 [HI] and below, given Altman Z 1.81 [ST]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its mechanical bear fair value and its own 5y minimum multiples; the obstacles are the unverified holdco discount, segment mix and consolidated leverage, which a lower price would not resolve.",
  "replaces": null,
  "replacement_reason": null
}
```
