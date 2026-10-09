# Evaluation: Jack Henry & Associates, Inc. (JKHY) — 2026-10-08
## Bear case
The de-rating may be telling the truth. The 10-K discloses price compression on renegotiated contracts and warns that fintech point solutions may reduce demand for integrated cores [Likely]. Even after the de-rating, JKHY trades at a +31% P/E, +30% P/FCF and +120% P/B premium to FI, FIS, ACIW and QTWO, so it can still fall to peer multiples [Certain]. A 6.80% FCF yield is only modestly above a 5.27% 10y Treasury, a thin cushion if growth slows [Certain]. ROE is down 2.8pp and ROIC down 1.3pp over five years [Certain]. The stock trails SPY by 22.8pp over 6 months and sits 7% below both moving averages, so there is no catalyst evidence yet [Certain]. The blended bear fair value of 107.21 is 26.4% below the close [Certain]. The Investor Day "step-up to 7%-8% by FY2029" may mean slower growth in the years before then [Guessing].

## Bull case
A sticky, mission-critical franchise serving 900+ banks and 700+ credit unions on roughly 6-year contracts [Certain] earns 22.7% ROIC and a 27.3% FCF margin, up 3.1pp over five years, with 138% FCF conversion and 0.09x net debt/EBITDA [Certain]. Every multiple sits in the bottom 3-8% of its own 5-year range [Certain]. The reverse DCF implies only 0.4% year-1 revenue growth, against FY2026 non-GAAP growth of 7.3% and a 7%-8% target [Likely]. Gross and operating margins are rising, and record core wins were cited in September 2026 [Likely]. Buybacks cut the share count by 1.37% [Certain]. With a beta of 0.56, the downside is cushioned [Certain]. The base fair value of 189.78 is 30.3% above the close [Certain]. A Nov 3 print that confirms growth could start closing the gap [Guessing].

## Decision
```json
{
  "ticker": "JKHY",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A 22.7%-ROIC, 27.3%-FCF-margin core-banking franchise with multi-year contracts trades in the bottom decile of its own 5-year multiples, where the price implies just 0.4% growth against 7.3% delivered.",
  "rationale": "Quality is proven and rising, and the balance sheet is nearly debt-free. The price implies near-zero growth against roughly 7% delivered and guided. The premium to peers and renewal price compression keep conviction at 4, not 5. A 7% position takes Technology to about 21%, within the 30% cap, and cash covers it.",
  "price_at_decision": 145.69,
  "price_date": "2026-10-07",
  "research_note": "research/JKHY/2026-10-08.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 20%, reversing the 5-year rising trend (now 27.3%).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM net margin falls below 17%, under the FY2024 trough of 17.2%, signalling renewal price compression is biting.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 19%, the FY2024 trough, evidencing moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "Annual revenue growth (income statement) falls below 5% for two consecutive fiscal years, undercutting the 7%-8% growth target."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 203.00, "basis": "Growth holds near FY2026's 7.3% and multiples re-rate toward the 5y median (EV/EBITDA 22.5x [RA]), reaching the fact sheet's bull fair value of 203.00 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.50, "target_price_12m": 175.62, "basis": "The market partly closes the gap between the reverse DCF's implied 0.4% growth and delivered growth, reaching the base DCF of 175.62 rather than the full 189.78 blend, because the stock's premium to peers (+13% EV/EBITDA [RA,P:*]) caps the re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 107.21, "basis": "Renewal price compression and point-solution competition flagged in the 10-K (https://www.sec.gov/Archives/edgar/data/779152/000077915226000067/jkhy-20260630.htm) slow growth, and the stock falls to the fact sheet's blended bear fair value of 107.21."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
