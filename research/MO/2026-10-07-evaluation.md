# Evaluation: Altria Group, Inc. (MO) — 2026-10-07
## Bear case
The cheapness is mostly an illusion. P/FCF of 12.5x and EV/Sales of 6.7x sit above their 5-year maxima, and EV/EBITDA of 8.7x is at the 83rd percentile of its range, so MO is expensive against its own history [Certain]. The low P/E against peers reflects a US-only cigarette franchise in structural volume decline, and that discount is justified [Likely]. The one growth category, oral nicotine and vapor, is under new pressure: the FDA authorised Juul2 and is reportedly speeding up approvals, so competitors can enter faster [Likely]. Altria suing the FDA signals regulatory friction rather than control [Likely]. FCF conversion has fallen from 332.8% to 114.3% [Certain]. As a bond proxy, MO faces a 10y real yield up 71bp in 3 months while the market still prices more hikes (macro overlay) [Certain]. Relative strength already trails SPY by 12.1pp over 12 months [Certain].
## Bull case
This is an exceptional cash machine: ROIC is 46.1% and rising, operating margin is 76.0%, FCF margin is 44.6% and the FCF yield is 7.98% [Certain]. Leverage is moderate at 1.41x net debt/EBITDA, down from 1.93x [Certain]. The dividend was raised 4.7% to $1.11, shares fell 1.0% YoY, and Altman Z of 5.34 and Piotroski F of 7 show no strain [Certain]. With a beta of 0.49 and a P/E of 14.3x, 45% below the peer median, a stable franchise plus capital returns could compound even without a re-rating [Likely]. Faster FDA approvals could also help Altria's own pouch and NJOY pipeline [Guessing]. If real yields plateau, the bond-proxy de-rating reverses (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "MO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 46%-ROIC, 45%-FCF-margin cigarette franchise is high quality, but it already trades above its own 5-year P/FCF and EV/Sales maxima while volumes decline, nicotine-alternative competition is accelerating and rising real yields pressure its bond-proxy multiple.",
  "rationale": "Quality is not in doubt. Valuation is: P/FCF and EV/Sales are above their 5-year maxima, and EV/EBITDA is at the 83rd percentile. The peer P/E discount reflects US-only regulatory concentration. Faster FDA approvals threaten the only growth category, and the macro tilt is moderately bearish. Good but not compelling: conviction 3, so AVOID and keep the cash.",
  "price_at_decision": 68.55,
  "price_date": "2026-10-06",
  "research_note": "research/MO/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC rises above 50% while gross margin holds above 85%, showing pricing power is accelerating rather than just offsetting volume decline (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 50}},
    {"text": "TTM FCF margin rises above 48%, showing cash generation is expanding beyond the five-year range and would justify the above-range P/FCF (would raise conviction).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 48}},
    {"text": "TTM gross margin falls below 80%, showing cigarette price/mix can no longer offset volume decline (confirms AVOID).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "Altria discloses in an SEC filing that oral nicotine (on!) or NJOY volumes are growing faster than the US category despite the FDA's faster approvals for competitors (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 77.06, "basis": "Real yields plateau (macro overlay macro_bull), so the 45% P/E discount to peers [RA] narrows enough to retest the 52-week high of 77.06 [HI], supported by a 7.98% FCF yield [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 67.11, "basis": "Fundamentals hold (ROIC 46.1% [RA], FCF margin 44.6% [CF,IS]) and P/E settles at its 5-year median of 14.0x versus 14.3x now [RA], implying a roughly flat price; the macro overlay's moderate bear tilt caps any re-rating."},
    "bear": {"probability": 0.3, "target_price_12m": 54.7, "basis": "EV/EBITDA reverts from 8.7x toward its 5-year median of 7.1x [RA] as real yields extend their +71bp 3m rise (macro overlay, moderate tilt toward bear, which raises this probability) and faster FDA pouch/vape approvals erode share [OV], taking the price to about the 52-week low of 54.70 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
