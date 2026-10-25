# Evaluation: Tele2 AB (STO:TEL2.B) — 2026-10-25
## Bear case
The screen's cheapness is an accounting mirage. TTM operating margin 41.5%, ROIC 22.6% and ROE 45.1% sit far above the FY2025 levels of 24.1%, 11.2% and 20.6%, most likely inflated by the one-off Baltic Tower gain, so P/E 10.9x and EV/EBITDA 7.3x overstate value [Likely]. On non-earnings measures the stock is not cheap: EV/Sales 4.5x is at its 5y max and P/B 4.6x near the top of its range, while P/FCF 11.9x sits at 88% of its range and roughly in line with peers [Certain]. The close of 159.85 equals base fair value 160.32, leaving no margin of safety [Certain]. Growth is low single digit (organic service revenue +2% in Q3) and FY EBITDAaL guidance was narrowed [Likely]. Freya's dual-class control and stake-building are an overhang [Certain].
## Bull case
A defensive, deleveraging cash machine: FCF margin 30.8%, FCF yield 8.40%, net debt/EBITDA down from 3.11x to 1.45x, beta 0.34 [Certain]. FY returns and margins rose steadily from FY2021 to FY2025 on cost discipline [Certain]. Q3 delivered record equity-free cash flow and capex-to-sales guided below 10%, supporting higher dividends after the large FY2025 increase [Likely]. The price implies only -0.4% year-1 revenue growth, a low bar against reported low-single-digit organic growth [Certain]. Freya raising its economic stake toward its 27% vote share could eventually lead to a bid or a tighter float [Guessing]. A fair-value blend with a bull case of 206.42 offers upside if the DCF holds [Certain].
## Decision
```json
{
  "ticker": "STO:TEL2.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A well-run, deleveraging Nordic telecom with a strong FCF yield, but its headline cheapness rests on one-off-inflated TTM earnings and the price already sits at base fair value.",
  "rationale": "Good but not compelling: the price equals base fair value, cash-based multiples are mid-to-high in their own ranges and near peers, and growth is low single digit. The low P/E and EV/EBITDA reflect a likely one-off gain. Conviction 3, so AVOID under the owner rule; revisit with a margin of safety.",
  "price_at_decision": 159.85,
  "price_date": "2026-10-23",
  "research_note": "research/STO-TEL2.B/2026-10-25.md",
  "triggers": [
    {"text": "TTM gross margin falls below 41%, under the FY2021-25 range, signalling price competition is eroding the network-leadership moat.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 41}},
    {"text": "TTM FCF margin falls below 22%, under the five-year low, showing cash generation can no longer fund the dividend and deleveraging.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 22}},
    {"text": "Net debt/EBITDA on the ratios page rises back above 2.5x, reversing the deleveraging after the Baltic Tower deal."},
    {"text": "Organic service revenue in the quarterly report turns negative for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 206.42, "basis": "Steady organic growth and record equity-free cash flow (Q3 2026 transcript [OV]) let the market pay the mechanical bull fair value of 206.42 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 160.32, "basis": "Low-single-digit growth with stable margins keeps the stock at its blended base fair value of 160.32 [IS,BS,CF,RA,ST,HI], consistent with the near-zero growth the reverse DCF implies."},
    "bear": {"probability": 0.25, "target_price_12m": 110.8, "basis": "Once the one-off TTM gain drops out (note section 2), EBITDA normalises and the stock is valued at the EV/EBITDA method's base of 110.80 [IS,BS,CF,RA,ST], above the full bear blend of 91.34 given low beta and falling leverage."}
  },
  "entry_price": 128.26,
  "entry_basis": "valuation file: base 160.32 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
