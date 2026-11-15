# Evaluation: SITC International Holdings Company Limited (HKG:1308) — 2026-11-15
## Bear case
SITC is a commodity freight business priced as if cycle-high earnings were permanent. P/E of 11.4x and EV/EBITDA of 9.8x sit above their 5-year maxima of 8.7x and 7.7x, and far above peer medians of 6.7x and 3.5x [Certain]. The mechanical base fair value of 29.83 HKD is 29.3% below the 42.18 close [Certain]. Returns are already rolling over: rolling ROIC is down 4.4pp to 54.3%, ROCE down 5.1pp and operating margin down 3.3pp, all below 2-year highs [Certain]. This is freight-rate normalisation from elevated levels, not a trough, so further declines are more likely than a rebound [Likely]. ROIC fell to 26.7% in FY2023 when rates reset [Certain]. The valuation points come from trend strength, not discount: if freight earnings slow, an extended multiple de-rates and earnings fall together [Likely]. China trade and tariff exposure is material but unquantified (macro overlay) [Guessing].

## Bull case
This is a genuinely high-return, net-cash operator: TTM ROIC 54.3%, operating margin 33.5%, FCF conversion 99.6% and net debt/EBITDA -0.51x [Certain]. The FCF yield of 8.67% is real cash, and P/FCF of 11.5x sits inside its 5-year range rather than above it [Certain]. Even its FY2023 trough ROIC of 26.7% would be excellent for most industrials, suggesting intra-Asia network density gives it a structurally better cycle than long-haul carriers [Likely]. The trend is healthy: the price is 10.6% above its 200-day average, up 33.5% in 12 months and ahead of SPY by 23.1pp [Certain]. Altman Z of 11.43 means no balance-sheet risk in a downturn [Certain]. If regional freight rates hold, cash returns can carry the shares back toward the 52.15 high [Guessing].

## Decision
```json
{
  "ticker": "HKG:1308",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "Rolling ROIC (-4.4pp), ROCE (-5.1pp) and operating margin (-3.3pp) are falling from cycle-high freight levels [RA-T, IS-T]; this is mean reversion of commodity freight rates with no evidence of a trough or recovery, and FY2023 shows how far returns fall when rates reset (ROIC 26.7%) [RA]. Not a guided reset or investment phase.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Intra-Asia freight rates keep normalising, so earnings fall while the multiple, above its own 5-year maximum, de-rates toward the mechanical base fair value; China trade-volume and tariff exposure is unquantified (macro overlay).",
    "veto": null
  },
  "thesis": "A net-cash, high-return intra-Asia container shipper whose cycle-high earnings are rolling over, trading above its own 5-year multiple range and far above peers, so the trend-led price leaves no margin of safety on a commodity freight cycle.",
  "rationale": "Quality and balance sheet are excellent, but returns are falling from a freight-cycle peak, there is no demonstrable moat, and the price sits well above the mechanical fair value and its own multiple history. Trend strength alone does not offset the de-rating risk. Scorecard conviction is below the buy bar, so AVOID.",
  "price_at_decision": 42.18,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-1308/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 35%, showing the freight cycle is resetting toward the FY2023 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM operating margin falls below 25%, showing rate normalisation is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 20%, showing fleet capex or lower rates are eroding cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Debt/EBITDA rises above 1.0x, signalling the net-cash balance sheet is being spent on ships.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 52.15, "basis": "Regional freight rates hold, TTM margins stay near 33.5% [IS] and the trend carries the price back to its 52-week high of 52.15 [HI]; above the mechanical bull of 31.44 because it assumes the current premium multiple persists."},
    "base": {"probability": 0.45, "target_price_12m": 38.14, "basis": "Returns keep drifting down as in the rolling table (ROIC -4.4pp [RA-T]) and the P/E above its 5-year max of 8.7x [RA] partly de-rates, taking the price to about its 200-day average of 38.14 [HI]; above the mechanical base of 29.83 because the 8.67% FCF yield [ST] supports a premium."},
    "bear": {"probability": 0.35, "target_price_12m": 29.83, "basis": "Freight rates reset as in FY2023 (ROIC 26.7% [RA]) and EV/EBITDA returns to its 5-year median of 7.3x [RA], matching the mechanical base fair value of 29.83; the mechanical bear of 12.68 needs cycle-trough EBITDA on a trough multiple, which the net cash makes less likely."}
  },
  "entry_price": 23.86,
  "entry_basis": "valuation file: base 29.83 x 0.8; at that price a cyclical high-return net-cash shipper would carry a real discount even after a rate reset."
}
```
