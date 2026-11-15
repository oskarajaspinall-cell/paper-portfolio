# Evaluation: FactSet Research Systems Inc. (FDS) — 2026-11-15
## Bear case
AI is the existential question: the new 10-K risk factors say clients may build their own tools and reduce demand, and short interest of 10.99% of float, up 21.4% in a month, shows the market takes it seriously [Certain]. Operating margin fell to 29.1% from 32.3% a year earlier, the fact sheet's Direction change; management blames restructuring, variable pay and one-time CEO costs [company-reported], but a margin reset can also be the cost of defending share [Guessing]. ROIC 18.0% is down from 23.2% five years ago [Certain]. The mechanical DCF puts base fair value at 247.28, well below the 332.69 close, and the reverse DCF needs 11.9% year-1 growth versus 6.7% organic [Certain]. The points come from trend strength: the price is 31.5% above its 200-day after a 64.8% six-month run, so any growth slowdown against the ~6% organic baseline risks a sharp de-rating [Likely].
## Bull case
FactSet is a recurring-subscription workflow business with 28.6% FCF margin, FCF/NI of 132.6% and net debt/EBITDA of 1.42x [Certain]. Switching costs embedded in client workflows are a durable moat [Likely]. Despite the rally, it trades near the bottom of its 5y range on every multiple (P/E 22.8x vs a 29.9x median; P/FCF 16.6x) and well below MSCI, SPGI, MCO and VRSK [Certain]. The margin dip is largely explained by one-offs and restructuring [company-reported], while ROCE rose to 23.6% and FCF margin rose in the last year [Certain]. The Investor Day reaffirmed fiscal 2027 and set a ~6% organic, ~10% EPS baseline [Likely], and buybacks cut the share count 4.62% [Certain]. Private-markets partnerships (Hamilton Lane, Nasdaq Private Market) and the AI ecosystem push suggest FactSet is a beneficiary of connected data, not a victim [Guessing]. The trend is strong: 12-month change +22.4% with RSI 58.6 [Certain].
## Decision
```json
{
  "ticker": "FDS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The 10-K attributes the operating-margin fall (32.3% to 29.1%) to restructuring charges, higher variable pay and one-time CEO pay costs [company-reported] (https://www.sec.gov/Archives/edgar/data/1013237/000162828026066391/fds-20260831.htm); FCF margin and ROCE rose over the same year and organic growth was 6.7%.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "AI lets clients build their own tools (new 10-K risk factor) and slows organic growth, which would de-rate a price already 31.5% above its 200-day average.", "veto": null},
  "thesis": "A high-return subscription data franchise trading near the bottom of its own 5y multiple range, whose margin dip looks restructuring-driven, but with AI disintermediation the open question.",
  "rationale": "The scorecard gives conviction 3: strong returns, balance sheet and trend, but the DCF base sits below the price and AI disintermediation is an unresolved medium risk. Good but not compelling, so AVOID; a deeper discount to fair value would make it a buy.",
  "price_at_decision": 332.69,
  "price_date": "2026-11-13",
  "research_note": "research/FDS/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM, income statement) falls below 27% as restructuring costs roll off.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 27}},
    {"text": "ROIC (TTM) falls below 15%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Organic revenue growth (10-K/10-Q MD&A) below 4% for two consecutive quarters."},
    {"text": "Client count (10-K/10-Q) declines year on year, signalling AI-driven disintermediation."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 436.31, "basis": "P/E re-rates toward its 5y median of 29.9x [RA] as the margin recovers, matching the fact sheet's P/E-method base of 436.31 [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 340, "basis": "P/E stays near today's 22.8x [RA] while EPS grows on the reaffirmed fiscal 2027 outlook and buybacks (shares -4.62% [ST]); above the DCF base of 247.28 because the DCF ignores the multiple sitting at its 5y low."},
    "bear": {"probability": 0.25, "target_price_12m": 214.11, "basis": "AI disintermediation slows growth below the reverse-DCF's implied 11.9% and the price returns to the DCF bear fair value of 214.11 [IS,CF,RA]."}
  },
  "entry_price": 197.82,
  "entry_basis": "valuation file: base 247.28 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
