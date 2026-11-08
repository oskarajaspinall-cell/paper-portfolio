# Evaluation: Petróleo Brasileiro S.A. - Petrobras (BVMF:PETR4) — 2026-11-08
## Bear case
The cheapness is mostly against peers, not against Petrobras's own history: P/E sits at 22% of its 5y range, EV/EBITDA at 77%, and P/FCF of 6.0x and EV/Sales of 1.7x are above their 5y maxima [RA] [Certain]. The peer discount is structural: the state can redirect fuel pricing, dividends and capex, and Lula's re-election on 2026-10-26 (headline-sourced, unverified officially per the macro overlay) raises that risk [Likely]. The rolling-12-month rise in ROIC (14.4% to 18.7%) and operating margin (30.5% to 36.1%) [RA-T, IS-T] is a cyclical rebound still below the 2-year highs, not proof of a reversed 5-year decline [Likely]; FCF margin kept falling to 19.2%, 9.9pp under its 2-year high [CF-T], as investment absorbs cash, threatening distributable cash [Likely]. BRL is 4.7% weaker in ~1m (macro overlay); Brent is not in the data, and Q3 results land Nov 10 [Certain].
## Bull case
A 16.79% FCF yield, 4.4x P/E and 3.3x EV/EBITDA against peer medians of 13.0x and 4.4x [RA, ST] price in a lot of bad news [Certain]. The reverse DCF implies revenue falling 11.4% in year 1, while Q3 output rose from a year earlier and a third Amapá discovery extends the resource base (Reuters URLs in the note) [Likely]. Returns are recovering on a rolling basis (ROIC 18.7%, operating margin 36.1%), leverage is moderate at 1.29x net debt/EBITDA and Piotroski F is 8 [RA-T, ST] [Certain]. The post-election selloff left the stock 11.0% below its 50-day average with RSI 29.2, so part of the political discount is priced (macro overlay) [Likely]. A weaker BRL lifts BRL earnings against USD-priced crude [Likely]. The mechanical DCF base of 88.94 sits well above the price [Certain], though it is a weak guide with NAV/SOTP unavailable [Likely].
## Decision
```json
{
  "ticker": "BVMF:PETR4",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost pre-salt producer with recovering returns trades at a deep peer discount, but that discount reflects state control over pricing and payouts that the re-election sharpens, while against its own history the stock is not cheap on FCF and FCF margin is still falling.",
  "rationale": "Cheap on peers and the mechanical DCF, but not on its own P/FCF or EV/Sales history; the cash-flow trend is weakening, governance risk rose with the election, and the macro tilt is toward bear. Expected value from the scenarios sits near the price. Good but not compelling: AVOID, re-check after the Q3 results and any pricing or dividend policy signal.",
  "price_at_decision": 45.30,
  "price_date": "2026-11-06",
  "research_note": "research/BVMF-PETR4/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, showing the rolling rebound from 14.4% has reversed and returns are leaking to non-commercial priorities.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 12%, well under the current 19.2%, meaning capex or pricing policy is consuming the cash that underpins distributions.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.2x (1.29x TTM now), showing the balance sheet is funding state-directed investment.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.2}},
    {"text": "A company release or official decree changes the fuel-pricing or dividend policy after the election (a confirmed unchanged policy alongside a rising TTM FCF margin would argue for re-research toward conviction 4)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 60.0, "basis": "Payout and pricing policy hold and EV/EBITDA re-rates from 3.3x toward the 4.4x peer median [RA], recovering toward the 59.79 52-week high [HI]; below the mechanical DCF bull of 250.33 because that extrapolates growth a state-controlled, cyclical producer has not shown (FCF margin falling, [CF-T])."},
    "base": {"probability": 0.45, "target_price_12m": 50.0, "basis": "Earnings roughly flat with ROIC near 18.7% [RA-T] and EV/EBITDA staying near its 5y median 3.0x [RA], the price recovering part of the post-election drop toward the 50-day average of 50.88 [ST]; below the mechanical base of 88.94 because own-history P/FCF is already above its 5y max of 4.5x [RA] and NAV/SOTP are unavailable."},
    "bear": {"probability": 0.35, "target_price_12m": 36.0, "basis": "Fuel-price or dividend intervention plus a BRL slide (macro overlay macro_bear) compress P/E back to its 5y median 3.7x [RA] on lower earnings; probability raised from an even weighting for the overlay's small toward-bear tilt (research/BVMF-PETR4/2026-11-08-macro.md); below the mechanical bear of 61.44, which assumes no political value leakage."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the mechanical base fair value is already far above the price, yet the stock is not cheap on its own P/FCF history and the decision hinges on post-election pricing/dividend policy and the falling FCF margin, so a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```
