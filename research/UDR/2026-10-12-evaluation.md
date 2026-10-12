# Evaluation: UDR, Inc. (UDR) — 2026-10-12
## Bear case
UDR's economics are thin. ROIC is only 3.8% TTM and FCF yield 2.97% [Certain] (fact sheet RA, ST), while net debt/EBITDA is still 5.76x [Certain] (RA). The macro overlay (primary weight, tilt toward bear, moderate) shows the 10y real yield up +0.56pp in 3 months to 2.87% and the Fed hiking on 2026-09-16 [Certain] (research/UDR/2026-10-12-macro.md). That rise goes straight into REIT cap rates and refinancing costs. The "below 5y minimum" multiples were all set in a lower-rate world, so they are a weak anchor [Likely]. The 84.5% upside to the P/FFO-proxy base fair value rests on own-history multiples, and FFO is not shown on stockanalysis.com, so it cannot be checked [Likely]. Short interest rose 24.7% in a month [Certain] (ST). Development spending is rising, which adds lease-up risk [Likely] (note §5).
## Bull case
The business is improving while the stock falls. ROIC rose from 1.5% to 3.8% and leverage fell from 7.29x to 5.76x over five years [Certain] (RA). Q2 2026 beat expectations and management raised full-year revenue, NOI and FFOA guidance [Certain] (Business Wire 2026-07-27, fact sheet OV). EV/EBITDA of 17.0x is below its own 5y minimum of 18.4x and 11% below the 19.1x peer median [Certain] (RA, peers). Shares fell 1.03% YoY, so there is no dilution [Certain] (ST). After a -14.0% 3-month move and -17.6pp versus SPY, much of the rate shock looks priced [Likely] (HI, macro overlay). A Fed pause at the late-October FOMC could re-rate a low-beta (0.71) name toward peers [Guessing] (macro overlay).
## Decision
```json
{
  "ticker": "UDR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An improving, deleveraging apartment REIT trades below its own 5-year minimum EV/EBITDA and below peers, but low returns on capital, a 2.97% FCF yield and rising real yields cap the re-rating.",
  "rationale": "Valuation is cheap versus history and peers, and the fundamentals are improving, but the 3.8% ROIC and 5.76x leverage leave UDR exposed to a primary macro headwind tilted toward bear. The mechanical upside cannot be verified without FFO data. The case is good but not compelling, so conviction is 3 and the answer is AVOID; cash is acceptable.",
  "price_at_decision": 34.12,
  "price_date": "2026-10-09",
  "research_note": "research/UDR/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 6.5x, reversing the five-year de-leveraging from 7.29x to 5.76x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "TTM ROIC falls below 2.5%, reversing the five-year improvement to 3.8%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 2.5}},
    {"text": "The Q3 2026 earnings release (due Oct 28, 2026) cuts the full-year FFOA per share guidance that was raised in Q2, showing operating momentum has stalled."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 46.5, "basis": "A Fed pause eases real yields (macro overlay, macro_bull) and EV/EBITDA returns to its 5y median of 21.1x [RA] on unchanged TTM EBITDA and 5.76x net debt [RA]; this is below the mechanical bull fair value of 70.07 because own-history P/FFO multiples were set at lower rates."},
    "base": {"probability": 0.45, "target_price_12m": 38.4, "basis": "Raised Q2 guidance holds (Business Wire 2026-07-27) and EV/EBITDA recovers only to its 5y minimum of 18.4x [RA], not the 62.96 base fair value, because the macro overlay (primary, moderate tilt toward bear) caps the re-rating while real yields are rising."},
    "bear": {"probability": 0.35, "target_price_12m": 31.1, "basis": "Real yields keep rising and the Fed stays higher for longer (macro overlay macro_bear, tilt moved weight to this case), so EV/EBITDA compresses to about 16x from 17.0x [RA] on 5.76x leverage [RA]; this is below the 40.72 mechanical bear because that figure assumes own-history multiples set in a lower-rate regime."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5y minimum EV/EBITDA, and the 62.96 x 0.8 = 50.37 default sits above the price. What blocks a BUY is rising real yields (primary macro headwind) and unverifiable FFO coverage of a 2.97% FCF yield, so a lower price on the same rate backdrop would not lift conviction to 4; a real-yield reversal or a Q3 FFOA beat would.",
  "replaces": null,
  "replacement_reason": null
}
```
