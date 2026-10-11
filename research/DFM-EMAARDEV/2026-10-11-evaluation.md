# Evaluation: Emaar Development PJSC (DFM:EMAARDEV) — 2026-10-11
## Bear case
Earnings look like a cycle peak. FY2025 ROIC of 293.2% against 24.7% in FY2021, and a gross margin up 20.0pp, point to peak Dubai off-plan pricing [Likely]. The market is clearly pricing reversion: P/E 3.9x is below its 5y minimum, yet P/B 1.2x sits 42% above peers. So the market is marking down the earnings stream, not the assets [Likely]. The macro is moving against demand. The US 10y is 5.22% (+68bp over 3m) and the dollar index is up 2.9% in a month; through the AED peg, both hurt buyer affordability (overlay: tilt toward bear, small) [Likely]. This is single-city, single-sector exposure. Institutions own only 6.3%, so this is a thin float controlled by a parent, and minorities may not get the net cash [Guessing]. Price trend is weak: -12.8% vs the 200-day, the 50-day is below the 200-day, and the stock lags SPY by 24.1pp [Certain].
## Bull case
The stock is extremely cheap on cash, not just on accounting earnings. FCF yield is 33.10%, FCF conversion has been above 100% in each of the last five years (TTM 129.4%), and the balance sheet is net cash (net debt/EBITDA -3.03x) [Certain]. EV/EBITDA of 0.6x means the market values the operating business at almost nothing beyond its cash [Certain]. Even if net margin halves back to FY2021's 20.8%, today's price would still be about 8x the lower earnings [Likely]. Quality is improving, not decaying: ROE is 40.8%, Altman Z 3.30, Piotroski 6 [Certain]. The trade is not crowded (beta 0.45, near its 52-week low of 12.05) [Certain]. If Dubai demand holds, the P/E simply returning to its 5y minimum of 4.3x gives about 10% upside, plus cash [Likely].
## Decision
```json
{
  "ticker": "DFM:EMAARDEV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 33%-FCF-yield Dubai developer is optically very cheap, but its earnings sit at a cyclical peak (ROIC 293%) in a single city while rates and the dollar are moving against buyers, and minority access to the cash is unproven.",
  "rationale": "The cheapness is real, but it is the market's rational discount on peak-cycle Dubai earnings, not a mispricing we can evidence. Tightening macro (secondary weight, bear tilt) and a controlled thin float cap conviction at 3. Under the owner rule that is an AVOID, and cash is acceptable.",
  "price_at_decision": 12.82,
  "price_date": "2026-10-09",
  "research_note": "research/DFM-EMAARDEV/2026-10-11.md",
  "triggers": [
    {"text": "TTM net margin falls below 30%, showing margins are normalising from the 42.5% peak faster than the price implies.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin turns negative, showing presales and collections have stalled and the cash-ahead-of-cost model is breaking.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "TTM ROE falls below 25%, close to the FY2022 5y low of 23.4% [RA], showing returns are reverting to ordinary developer levels.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 25}},
    {"text": "Company filings show a dividend or distribution policy that passes the net cash on to minority shareholders, which would remove the cash-access discount (this would lift conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 17.75, "basis": "Dubai absorption holds and P/E re-rates to its 5y median of 5.4x [RA] on TTM EPS implied by 12.82 / 3.9x [ST,HI]. This is far below the mechanical DCF bull of 190.48, because that DCF extrapolates peak FY2025 ROIC and FCF margin [RA,CF]."},
    "base": {"probability": 0.45, "target_price_12m": 14.1, "basis": "Earnings hold near TTM levels and P/E moves back to its 5y minimum of 4.3x [RA]. Set well below the DCF base of 86.98, which capitalises a 76.6% FY2025 FCF margin [CF,IS] that this cyclical developer is unlikely to sustain."},
    "bear": {"probability": 0.35, "target_price_12m": 8.7, "basis": "Net margin reverts from 42.5% to the FY2021 level of 20.8% [IS] at the 5y median P/E of 5.4x [RA]. Probability raised from 0.30 by the macro overlay's small bear tilt (US 10y +68bp/3m, dollar +2.9%/1m, research/DFM-EMAARDEV/2026-10-11-macro.md). Below the DCF bear of 41.60 because the DCF ignores the cycle."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. At 3.9x P/E the stock is already below its 5y minimum, so a lower price would not change the decision. The blockers are Dubai cycle visibility under tightening rates and unproven minority access to the net cash. The base fair value x 0.8 (69.58) is above the price and anchors nothing.",
  "replaces": null,
  "replacement_reason": null
}
```
