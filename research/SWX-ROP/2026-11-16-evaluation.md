# Evaluation: Roche Holding AG (SWX:ROP) — 2026-11-16
## Bear case
The price has run ahead of the business. P/E 26.4x, EV/EBITDA 14.5x and P/FCF 20.5x all sit above their own 5-year maxima (24.8x, 13.1x, 17.8x) [Certain]; even the mechanical bull fair value of 306.59 CHF is 24.2% below the 404.70 close, and the reverse DCF needs 9.5% year-1 revenue growth, demanding for a mature pharma [Likely]. The case for owning it is trend strength, but that is exactly what an extended price risks: a 12-month gain of +39.4% and RSI 66.4 leave a de-rating toward the 5y median P/E of 20.3x if growth slows or a pipeline readout disappoints [Likely]. ROIC has faded from 38.3% (FY2021) to 28.1% and sits 2.5pp below its 2-year high of 30.6% [Certain]; patent expiries make the moat time-limited [Likely]. US exposure, drug-pricing policy and a stronger dollar are unverified risks to CHF earnings (macro overlay) [Guessing].

## Bull case
Roche is a high-quality, conservatively financed franchise: TTM ROIC 28.1%, operating margin 33.1% (a rolling 2-year high, up 1.2pp in a year), FCF margin 25.0%, FCF conversion 127.6% and net debt/EBITDA 0.98x [Certain]. The ROIC dip below its 2-year high is flat over the last year (-0.5pp) while margins rise, so it is a fade from an elevated base rather than a structural break [Likely]. Against large-cap pharma peers it trades at a discount on P/E, EV/EBITDA and P/FCF [Certain], with a 4.87% FCF yield. Momentum is strong and defensive: +16.8% above its 200-day average with positive relative strength against SPY of +29.0pp over 12 months on a 0.32 beta [Certain]. Steady pipeline news (CHMP recommendation for Gazyva in lupus; https://www.globenewswire.com/news-release/2026/11/13/3402454/0/en/chmp-recommends-eu-approval-of-roche-s-gazyva-gazyvaro-for-systemic-lupus-erythematosus-sle.html) supports continued growth [Likely].

## Decision
```json
{
  "ticker": "SWX:ROP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC is flat over the last 12 months (-0.5pp) while operating margin rose 1.2pp to a 2-year high of 33.1% and FCF margin is flat at 25.0% [RA-T, IS-T, CF-T]; the 2.5pp gap to the ROIC 2-year high is a fade from an elevated base with the balance sheet intact (net debt/EBITDA 0.98x).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating: every earnings and cash multiple sits above its own 5-year maximum after a +39.4% year, so slower growth or a pipeline setback could compress the P/E back toward its 5y median of 20.3x [RA].",
    "veto": null
  },
  "thesis": "A high-return, lowly levered pharma and diagnostics franchise in a strong uptrend, but priced above its own 5-year multiple range and every mechanical fair-value case, so the business is working while the price already discounts it.",
  "rationale": "Quality and balance sheet are excellent and the margin trend is intact, but multiples above their 5-year maxima and a price above even the bull fair value leave no discount and no trend-strength credit. The scorecard gives conviction 3, below the buy bar, so AVOID; cash is an acceptable outcome.",
  "price_at_decision": 404.70,
  "price_date": "2026-11-13",
  "research_note": "research/SWX-ROP/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 24%, well under the 28.1% now, showing the fade is becoming a structural loss of returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 24}},
    {"text": "TTM operating margin falls below 30%, reversing the rise to 33.1% and signalling pricing pressure or patent erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 20%, under the FY2023 five-year low of 20.4%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.98x now), e.g. from a large debt-funded acquisition.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 440, "basis": "Earnings keep growing with operating margin at its 2-year high of 33.1% [IS-T] and the P/E holds near today's 26.4x, still below the peer median of 48.8x [RA, P:LLY]."},
    "base": {"probability": 0.5, "target_price_12m": 375, "basis": "Fundamentals stay steady but the P/E drifts back toward its 5-year maximum of 24.8x [RA]; above the mechanical bull fair value of 306.59 because the DCF is blind to the peer discount and current margin strength."},
    "bear": {"probability": 0.3, "target_price_12m": 285, "basis": "A slowdown or pipeline setback de-rates the P/E toward its 5-year median of 20.3x [RA], consistent with the mechanical base fair value of 285.29 CHF [fact sheet Fair value]."}
  },
  "entry_price": 228.23,
  "entry_basis": "valuation file: base 285.29 x 0.8; price is the obstacle, quality and the margin trend are intact.",
  "replaces": null,
  "replacement_reason": null
}
```
