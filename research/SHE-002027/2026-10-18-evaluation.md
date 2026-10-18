# Evaluation: Focus Media Information Technology Co., Ltd. (SHE:002027) — 2026-10-18
## Bear case
The cheapness depends on which multiple you look at. EV/EBITDA of 8.0x and P/FCF of 9.7x sit far below their 5y minimums [RA] [Certain], but P/E of 21.9x is inside its 5y range and in line with the peer median of 22.1x [RA] [Certain]. For a screen-lease-heavy network that gap points to lease costs falling below EBITDA and FCF. FCF conversion of 226.1% of net income [CF,IS] fits that reading, so FCF-based value (including the DCF behind the 6.57 base) is likely overstated [Likely]. Net margin fell from 42.0% to 23.1% in FY2025 and is only 27.0% TTM [IS]. The cause is undisclosed [Certain], so the earnings base may have reset [Guessing]. The price is down 33.7% over 12 months and sits below its 200-day average [ST] [Certain]. Q3 results on Oct 28, 2026 [ST] land before any thesis can be checked [Certain].
## Bull case
This is a high-return, net-cash franchise: TTM ROIC is 60.4%, gross margin 71.6%, operating margin 45.3%, and net debt/EBITDA is -1.46x [RA,IS] [Certain]. Operating margin is flat-to-up across five years [IS] [Certain], so the FY2025 net-margin drop looks like a below-the-line item rather than weaker core economics [Likely]. Piotroski 7 and Altman Z 10.36 [ST] confirm the balance sheet's strength [Certain]. The reverse DCF implies -1.5% year-1 revenue growth [Certain], which prices in stagnation for China's largest elevator-media network, whose density is a costly-to-replicate moat [Likely]. Insiders own 23.72% and the share count is flat [ST] [Certain]. Even the mechanical bear fair value of 5.05 sits close to the price [Certain].
## Decision
```json
{
  "ticker": "SHE:002027",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "China's dominant elevator-media network earns very high operating returns with net cash, but on earnings (P/E 21.9x, inside its 5y range and at the peer median) it is fairly priced, and the apparent deep discount on EV/EBITDA and P/FCF likely reflects lease accounting rather than true cheapness.",
  "rationale": "Quality is real, but the valuation case rests on EBITDA and FCF figures that lease costs probably flatter, while P/E shows no discount. An undisclosed FY2025 net-margin drop, a falling price and results due Oct 28, 2026 leave the edge good but not compelling. Adding a fourth China name would also concentrate the portfolio. AVOID; the stock is a buy on an earnings de-rating.",
  "price_at_decision": 5.16,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002027/2026-10-18.md",
  "triggers": [
    {"text": "TTM net margin recovers above 30% (statistics page), showing the FY2025 drop to 23.1% was one-off and restoring the earnings base the bull case needs.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 30}},
    {"text": "TTM ROIC falls below 25% (statistics page), showing the elevator-network moat is eroding to competition.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM operating margin falls below 40% (statistics page), under the FY2024 level of 40.1%, showing advertiser demand or slot pricing is weakening.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7.63, "basis": "Net margin returns toward its FY2021-FY2024 40%+ level [IS] and the market pays the fact sheet's EV/EBITDA-method base value of 7.63 [RA], below the 8.63 bull blend because EBITDA likely includes lease costs."},
    "base": {"probability": 0.45, "target_price_12m": 5.6, "basis": "Earnings hold near the TTM 27.0% net margin [IS] at roughly today's 21.9x P/E [RA], with modest upside from buyback-free cash build; this sits below the 6.57 base fair value because the DCF capitalises lease-flattered FCF (FCF/NI 226.1% [CF,IS])."},
    "bear": {"probability": 0.3, "target_price_12m": 4.63, "basis": "Q3 results on Oct 28, 2026 [ST] confirm the FY2025 net-margin drop to 23.1% [IS] is structural and P/E de-rates toward its 5y median 19.7x [RA], back to the 52-week low of 4.63 [HI]."}
  },
  "entry_price": 4.45,
  "entry_basis": "P/E back at its 5y minimum of 18.9x [RA] on TTM earnings (21.9x at 5.16); the default base 6.57 x 0.8 sits above the price and relies on lease-flattered FCF, so an earnings-based anchor is used.",
  "replaces": null,
  "replacement_reason": null
}
```
