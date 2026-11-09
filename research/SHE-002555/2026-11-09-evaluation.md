# Evaluation: 37 Interactive Entertainment Network Technology Group (SHE:002555) — 2026-11-09
## Bear case
Returns are eroding fast and the last year accelerated it: ROIC fell from 33.4% to 17.7% TTM, operating margin from 19.1% to 13.9% and FCF margin from 20.3% to 10.5% [RA-T, IS-T, CF-T] [Certain]. These Direction change lines are the core of the bear case: gross margin has slid every year from 84.8% to 75.9% (FY2025) [IS], pointing to rising user-acquisition costs or weaker titles, a structural squeeze on a hit-driven model rather than a guided one-off [Likely]. No company source confirms a temporary cause [Certain]. The stock is not cheap on depressed earnings: P/FCF 22.9x is above its 5y max and P/E 17.4x sits above its 5y median [RA] [Certain]; the reverse DCF needs 26.1% year-1 revenue growth and the DCF base is 7.52 CNY [Certain]. Piotroski F of 4 is weak [ST] [Certain]. China game-licensing and spending-limit risk is standing [Guessing].
## Bull case
The balance sheet is a fortress: net cash (net debt/EBITDA -2.07x) and Altman Z 4.51 [BS, ST] [Certain], so the trough is survivable and dilution is negligible (0.08%) [Certain]. Absolute returns remain respectable (ROIC 17.7%, ROE 14.8%) [RA] [Certain]. Against peers it trades at a large discount on P/E (-40%) and EV/EBITDA (-54%) and P/B 2.6x is below its 5y min [RA] [Certain]. The shares are down 26.9% over 12 months, so much decline is priced [Likely]. Q3 2026 results drew a +8.7% reaction on 2.9x volume [HI], hinting results beat a low bar [Guessing]. Insiders own 39.82%, aligning management [ST] [Certain]. If a new title lifts revenue, operating leverage on a 77.1% gross margin is large [Likely].
## Decision
```json
{
  "ticker": "SHE:002555",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "Gross margin has fallen every fiscal year from 84.8% (FY2021) to 75.9% (FY2025) [IS] and ROIC from 61.1% to 17.7% TTM [RA]; no company-reported guided reset or one-off was found (note sections 2 and 6), so the decline reads as rising costs/weaker titles in a hit-driven model.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Continued margin and return erosion from a thin title pipeline and rising user-acquisition costs, plus standing China game-licensing/spending-limit risk; the last 12 months show the erosion accelerating.",
    "veto": null
  },
  "thesis": "A cash-rich Chinese game publisher whose returns and margins are eroding quickly, trading above its own-history earnings multiples on depressed profits.",
  "rationale": "Quality is falling fast with no evidenced temporary cause, the stock is not cheap on its own history (P/FCF above 5y max, mechanical DCF well below price), and the moat is weak. The net-cash balance sheet limits downside but does not make it a high-conviction buy. AVOID; cash is acceptable.",
  "price_at_decision": 16.32,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-002555/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin TTM recovers above 19% (back to its FY2025 level), showing the margin squeeze was temporary.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 19}},
    {"text": "FCF margin TTM recovers above 19.9% (its FY2025 level).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 19.9}},
    {"text": "ROIC TTM recovers above 30% (back toward its FY2025 level of 30.8%).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 17.86, "basis": "A new hit title restores margins toward FY2025 levels (operating margin 19.2% [IS]), matching the mechanical bull fair value of 17.86 CNY [valuation file]."},
    "base": {"probability": 0.5, "target_price_12m": 13.39, "basis": "Returns keep drifting lower (ROIC down 15.7pp in a year [RA-T]) and the stock re-rates toward the EV/Revenue bear value of 13.39 CNY, between the DCF base of 7.52 and EV/Revenue base of 16.40 in an unreliable fair-value range [valuation file]."},
    "bear": {"probability": 0.3, "target_price_12m": 9.05, "basis": "Margin erosion continues (FCF margin 10.5% TTM vs 20.3% a year earlier [CF-T]) or a China game-regulation shock hits, taking the price to the mechanical bear fair value of 9.05 CNY [valuation file]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: returns and margins are deteriorating with no evidenced temporary cause and the moat is weak, so a lower price on the same evidence would not justify conviction 4; a recovery in the triggers above would.",
  "replaces": null,
  "replacement_reason": null
}
```
