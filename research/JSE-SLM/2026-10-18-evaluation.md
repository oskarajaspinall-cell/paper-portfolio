# Evaluation: Sanlam Limited (SLM) — 2026-10-18
## Bear case
On the two multiples that matter for a life insurer, SLM is not cheap: P/E 9.5x is above the 8.0x peer median and P/B 1.6x sits at its own 5y median and above the 1.4x peer median [Certain]. The striking EV/EBITDA (1.4x) and P/FCF (7.0x) readings are distorted by policyholder float and investment cash flows, and the net-debt sign conflict is unresolved [Likely]. No mechanical fair value is computable (no ZAR FX rate), so there is no independent anchor for upside [Certain]. ROIC of 61.3% is not meaningful for an insurer [Likely]. Severe-weather claims and currency volatility hit 2026 earnings, and the cash Santam buy-in concentrates short-term-insurance risk with only "modest" accretion per management [Likely]. The stock is below its 200-day average and has lagged SPY by 20.6pp over 12 months [Certain].
## Bull case
ROE has risen from 12.5% in FY2021 to 19.9% TTM, with no dilution (shares flat YoY) [Certain]. P/E sits in the lower third of its own 5y range (8.1x-12.9x), and FCF conversion is 134.5% TTM, supporting dividends and a fully funded cash offer for Santam [Certain]. Management guided 2026 earnings to CPI plus 3% with a stronger second half, and Q2 showed strong new business and net client cash flows [Likely]. Beta of 0.51 makes it a diversifying, defensive financial in a portfolio with no Financials exposure [Certain]. A re-rating to the 5y median P/E of 10.8x as weather headwinds fade is plausible [Guessing].
## Decision
```json
{
  "ticker": "JSE:SLM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A pan-African insurer with rising ROE and strong cash conversion, but priced in line with or above peers on P/E and P/B, with no computable fair value and a pending Santam buy-in that adds concentration rather than a clear mispricing.",
  "rationale": "Quality is improving, but the stock is not discounted on the insurer-relevant multiples (P/E, P/B above peer medians), the cheap EV/EBITDA and P/FCF readings are float-distorted, and fair value cannot be computed. Good but not compelling: AVOID, revisit nearer the bottom of its own P/E range.",
  "price_at_decision": 8500.00,
  "price_date": "2026-10-16",
  "research_note": "research/JSE-SLM/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 15%, reverting toward FY2021-22 profitability.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "Shares outstanding rise more than 5% year on year, i.e. a dilutive raise to fund the Santam buy-in.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}},
    {"text": "FCF conversion (FCF/net income) stays below -20% for two consecutive fiscal years, showing cash no longer backs reported earnings."},
    {"text": "Net debt/EBITDA on the ratios page (site definition) moves from net cash to above 1.0x net debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11500, "basis": "Weather and currency headwinds fade and P/E re-rates toward its 5y max of 12.9x [RA] on TTM earnings, helped by Santam accretion per the 2026-10-05 transcript."},
    "base": {"probability": 0.5, "target_price_12m": 9300, "basis": "ROE holds near 19.9% [RA] and P/E drifts from 9.5x toward, but short of, its 5y median 10.8x [RA]; no fair value cross-check is available (no ZAR FX rate in the fact sheet)."},
    "bear": {"probability": 0.3, "target_price_12m": 7250, "basis": "Continued severe-weather claims (Q2 2026 call) compress earnings and P/E falls to its 5y min of 8.1x [RA], near the peer median 8.0x."}
  },
  "entry_price": 7250,
  "entry_basis": "Fair value unavailable (no ZAR FX rate), so anchored on P/E back at its 5y low of 8.1x [RA] on TTM earnings, roughly in line with the 8.0x peer median; at that level the improving ROE would be clearly unpriced.",
  "replaces": null,
  "replacement_reason": null
}
```
