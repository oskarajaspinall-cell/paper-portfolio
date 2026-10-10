# Evaluation: HP Inc. (HPQ) — 2026-10-10
## Bear case
Returns are eroding, not cycling: ROIC fell from 54.6% (FY21) to 27.6% TTM, operating margin from 8.9% to 6.5%, net margin from 10.3% to 4.1% [Certain]. FY26 Personal Systems growth was price/mix and memory-cost pass-through on falling units, not demand [Certain]; HP has now withheld FY2027 guidance and plans for a mid-single-digit decline in PC units [Certain]. PCs earn a 4.6% segment margin against Dell and Lenovo, so cost inflation is hard to pass on [Likely]. Buybacks have pushed net debt/EBITDA from 0.70x to 1.33x and Altman Z is 1.60, while the macro overlay shows real yields and HY spreads widening, raising funding and discount-rate risk [Certain]. P/E sits at the 88th percentile of its 5y range, so the stock is not cheap against its own history [Certain]. The base DCF of 46.74 extrapolates margins that are still falling [Likely].
## Bull case
FCF yield is 14.25% and P/FCF 7.0x, near the bottom of its 5y range (21st percentile), with FCF conversion of 158.3% TTM [Certain]. The reverse DCF implies a -9.3% revenue decline in year 1, so the guided PC-unit drop looks largely priced in [Likely]. Printing's supplies annuity runs an 18.1% operating margin and funds a steady payout; shares fell 2.89% YoY [Certain]. Base fair value of 40.22 is +33.2% upside, against a bear of 26.91 (-10.9%) [Certain]. AI-PC and workstation launches could hold the premium mix [Guessing]. Short interest of 8.07% fell 10.6% month on month, which could fuel a re-rating if FY27 is better than feared [Guessing].
## Decision
```json
{
  "ticker": "HPQ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "HPQ is optically cheap on cash flow, but falling returns, withheld FY2027 guidance on lower PC units and rising leverage into tightening credit conditions mean the low multiple is earned rather than a mispricing.",
  "rationale": "The FCF yield and the reverse-DCF are real positives, but ROIC and margins are falling every year, FY27 visibility is gone, and leverage plus Altman Z 1.60 meet a bear-tilted macro. Probability-weighted value sits near the current price. That is good but not compelling, so cash is better.",
  "price_at_decision": 30.20,
  "price_date": "2026-10-09",
  "research_note": "research/HPQ/2026-10-10.md",
  "triggers": [
    {"text": "Operating margin recovers above its FY2024 level of 7.9%, showing the margin erosion has reversed rather than continued", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 7.9}},
    {"text": "ROIC climbs back above its FY2024 level of 30.0%, breaking the 5-year decline in returns", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 30.0}},
    {"text": "HP reinstates FY2027 guidance showing Personal Systems revenue holding up despite lower PC units (price/mix still offsetting volume), per an 8-K or results release", "check": null}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 40.22, "basis": "FY27 PC-unit decline is offset by AI-PC mix, Printing margins hold, and the stock re-rates to the blended base fair value of 40.22 [IS,CF,RA]; probability reduced because the macro overlay tilts moderately toward bear (research/HPQ/2026-10-10-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 30.92, "basis": "EV/EBITDA holds near its current 7.2x versus its 5y median of 6.8x [RA] on flat EBITDA, which is the EV/EBITDA method's 30.92 [RA,IS]; weighted below the DCF base because margins are still falling [IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 23.98, "basis": "Mid-single-digit FY27 PC-unit decline (8-K 2026-09-21, https://www.sec.gov/Archives/edgar/data/47217/000114036126037170/ef20082499_form8k.htm) compresses EBITDA and the multiple to the EV/EBITDA bear of 23.98 [RA]; probability raised moderately because rising real yields and HY spreads hit a leveraged, thin-equity balance sheet (research/HPQ/2026-10-10-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns and margins are still falling (ROIC 54.6% to 27.6%, operating margin 8.9% to 6.5% [RA,IS]) and FY2027 guidance is withheld, so a lower price on this same evidence would not justify conviction 4. Base fair value of 40.22 less the 20% margin of safety is also above the 30.20 close, so it cannot serve as an entry anchor.",
  "replaces": null,
  "replacement_reason": null
}
```
