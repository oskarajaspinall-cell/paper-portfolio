# Evaluation: Zhejiang Dingli Machinery Co.,Ltd (SHA:603338) — 2026-11-23
## Bear case
Margins are sliding from a peak and the cause is unproven. Operating margin is 22.4%, 5.7pp below its 2-year high of 28.1%, and gross margin fell to 30.6% from 34.2% in FY2025 [Certain]; that looks like price competition or tariff pressure on overseas sales, not a one-off [Likely]. FCF margin is 13.1pp below its 2-year high and FCF conversion swings (34.3% in FY2025) [Certain], so the 4.34% FCF yield is not dependable [Likely]. The mechanical fair value is flagged unreliable, with the through-cycle DCF base at 31.23 CNY against a 58.99 close and a reverse DCF implying 30.6% year-1 growth [Certain]. The price is above its 200-day average; if margins keep slipping, a de-rating can follow [Likely]. The overseas revenue mix, and so tariff and FX exposure, is unverified (macro overlay) [Certain]; the Q3 2026 report was not read [Certain].
## Bull case
A high-return, net-cash niche leader at a low multiple of its own history. TTM ROIC is 26.9% and rose from 24.3% a year earlier; ROCE rose to 18.5% [Certain]. Net debt/EBITDA is -1.66x and Altman Z 4.81, so the balance sheet can ride a cyclical trough [Certain]. EV/EBITDA of 9.7x and P/B of 2.4x sit below their 5y minimums, and P/E of 15.7x is at the 6th percentile of its range and below the peer median of 17.8x [Certain]. FCF margin recovered to 12.1% from 2.9% [Certain], suggesting the FY2025 dip was working capital, not a broken model [Likely]. The EV/EBITDA method alone gives a base of 75.39 CNY [Certain]. Insiders own 45.53%, aligning management [Certain], and the price is in an uptrend, above both averages with relative strength vs SPY positive [Certain].
## Decision
```json
{
  "ticker": "SHA:603338",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC, operating margin and FCF margin come with a recovery over the last 12 months (ROIC 24.3% -> 26.9%, FCF margin 2.9% -> 12.1% [RA-T, CF-T]) and net cash intact (net debt/EBITDA -1.66x [BS]); consistent with a cyclical trough, though gross margin compression to 30.6% [IS] is not yet explained.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Gross and operating margin keep compressing from competition or tariffs on unverified overseas sales, de-rating a stock trading above its 200-day average.",
    "veto": null
  },
  "thesis": "A net-cash aerial-platform leader with ROIC near 27% trading below its own 5-year EV/EBITDA and P/B lows, if margins stabilise.",
  "rationale": "High returns and net cash at a low multiple of history, but margins are below their 2-year highs for an unproven reason, the overseas mix and tariff exposure are unverified and the fair value is unreliable. Good but not compelling: AVOID, watch the entry price.",
  "price_at_decision": 58.99,
  "price_date": "2026-11-20",
  "research_note": "research/SHA-603338/2026-11-23.md",
  "triggers": [
    {"text": "ROIC TTM falls below 20%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Operating margin TTM falls below 18%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "FCF margin TTM falls below 5%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Net cash lost: net debt/EBITDA (debt minus cash and short-term investments, balance sheet) rises above 0x"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 75.39, "basis": "Margins stabilise and EV/EBITDA re-rates toward its own history, matching the EV/EBITDA-method base of 75.39 [fact sheet fair value, RA]."},
    "base": {"probability": 0.45, "target_price_12m": 59.0, "basis": "ROIC holds near 26.9% but operating margin stays near 22.4% [RA-T, IS-T], so the multiple stays near today's 9.7x EV/EBITDA, above the unreliable blended fair value of 45.95 because the through-cycle DCF understates a net-cash compounder."},
    "bear": {"probability": 0.3, "target_price_12m": 41.44, "basis": "Gross margin compression continues (30.6% vs 34.2% [IS]) and the stock revisits its 52-week low of 41.44 [HI], between the blended base 45.95 and bear 28.26 fair values."}
  },
  "entry_price": 39.06,
  "entry_basis": "valuation file: base 45.95 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```
