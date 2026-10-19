# Evaluation: Valterra Platinum Limited (JSE:VAL) — 2026-10-19
## Bear case
VAL is a price-taker: earnings follow the USD PGM basket, not the management team [Certain]. TTM ROIC of 43.9% and operating margin of 32.8% are near cycle highs; FY2023-24 showed how fast they can drop to 14.4% and 14.6% [Certain]. That makes the 9.1x P/E a peak-earnings multiple, not a low one [Likely]. VAL already trades at a premium to JSE PGM peers: +28% on P/E, +55% on EV/EBITDA, +74% on EV/Sales [Certain]. No mechanical fair value can be computed (NAV and EV/EBITDA both [data unavailable]), so the price has no anchor [Certain]. The macro overlay tilts small toward bear: the dollar index is up ~3% in a month and the 10y real yield is at 2.78%, both pressuring USD commodity prices [Certain]. The price is below its 50- and 200-day averages, and results due Oct 26, 2026 could reset the cycle read [Likely]. EV-driven autocatalyst substitution is a structural demand risk [Likely].

## Bull case
VAL is the scale, lowest-cost PGM producer [Likely]. It has held net cash every year FY2021-TTM, so it can invest and pay dividends through troughs [Certain]. TTM FCF margin is 26.7%, FCF conversion is 114.1% and the FCF yield is 12.66%, with the share count flat (+0.21%) [Certain]. P/E and EV/EBITDA sit in the 17th percentile of VAL's own 5-year range, and P/FCF of 7.9x is near its 5y low and below the peer median [Certain]. Piotroski F is 8 and Altman Z 5.00 [Certain]. The H1 2026 call cited strong FCF and a 70% headline-earnings payout [Likely]. If the PGM basket holds, the margin recovery could extend and the cash returns compound [Guessing].

## Decision
```json
{
  "ticker": "JSE:VAL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, lowest-cost PGM miner with a 12.66% FCF yield, but on near-peak commodity margins, at a premium to peers and with no computable fair value, so the cheap-looking multiples may be a cyclical trap.",
  "rationale": "The balance sheet and cash yield are strong, but the earnings are the PGM price. Margins are near cycle highs, VAL trades at a premium to peers, there is no fair-value anchor, and the macro tilt is toward bear, with results due Oct 26. That makes it good but not compelling: conviction 3, so AVOID.",
  "price_at_decision": 125318.0,
  "price_date": "2026-10-16",
  "research_note": "research/JSE-VAL/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, back to the FY2023-24 trough (14.4% FY2024): the cost-curve edge is not holding through the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 15%, a reversion to the FY2023-24 trough (14.6% FY2024) rather than a sustained recovery.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin turns negative, repeating the FY2023 trough (-3.5%) and undermining the dividend capacity.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA (ratios page) turns positive (net debt) for two consecutive half-years, eroding the net-cash differentiator."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165000, "basis": "TTM margins (32.8% operating [IS]) hold as the PGM basket firms, and P/E re-rates partway from 9.1x toward its 5y median of 19.4x [RA]; probability trimmed for the overlay's small bear tilt (research/JSE-VAL/2026-10-19-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 125000, "basis": "Earnings plateau and P/E stays near 9.1x [RA], with the 12.66% FCF yield [ST] paid out rather than re-rated; there is no mechanical fair value to reconcile with (NAV and EV/EBITDA both [data unavailable] in the fact sheet)."},
    "bear": {"probability": 0.3, "target_price_12m": 85000, "basis": "Dollar strength and a rising real yield soften the USD PGM basket (macro overlay, small tilt toward bear, which raised this probability), and the operating margin reverts from 32.8% TTM toward FY2025's 20.7% [IS], taking the price toward its 52-week low of 95,398 [HI] and below."}
  },
  "entry_price": 97775,
  "entry_basis": "There is no fair value to discount (NAV and EV/EBITDA [data unavailable]), so the anchor is TTM P/E falling from 9.1x to the JSE PGM peer median of 7.1x [RA, P:JSE:IMP/SSW/NPH]. That removes the peer premium, near the 52-week low of 95,398 [HI].",
  "replaces": null,
  "replacement_reason": null
}
```
