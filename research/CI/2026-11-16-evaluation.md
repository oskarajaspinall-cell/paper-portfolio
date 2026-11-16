# Evaluation: The Cigna Group (CI) — 2026-11-16
## Bear case
Cigna's profit pool rests on PBM rebate and pharmacy economics that policy is actively targeting; management itself flags 2027 headwinds from rebate reform, GLP-1 costs and the ACA exit [Likely]. If reform caps rebate spreads, the low multiple is a fair price for a shrinking earnings stream, not a discount [Guessing]. Margins are thin by construction: gross margin fell 3.9pp over five years and FCF margin is down 2.8pp over three years to 2.9%, sitting below its 2-year high of 3.6% [Certain]. Rolling ROIC of 12.7% is below its 2-year high of 14.3% [Certain]. Peers trade higher but are themselves depressed, so the peer discount proves little [Likely]. The base fair value leans on a DCF whose bull case is far above its base, so the model upside is fragile [Likely]. Q3 net income fell year on year on the absence of prior-year business-sale gains [Certain].
## Bull case
The stock trades at P/E 13.2x, 8% of its 5-year range, and EV/EBITDA 8.1x, below its 5-year minimum, with a 10.40% FCF yield [Certain]. The reverse DCF implies -1.5% revenue growth in year 1, while Q3 beat and FY26 guidance was raised [Certain]. Returns are rising: ROIC up from 8.8% in FY2021 to 12.7%, ROE 15.6% [Certain]. Cash conversion is strong (FCF/NI 138.0%), leverage has fallen to 1.87x from 2.84x, and the share count fell 2.66% YoY, so buybacks compound per-share value [Certain]. Earnings are mainly fee-based rather than underwriting risk, which explains why CI avoided the managed-care cost blow-ups [Likely]. Beta 0.25 and short interest 2.38% mean a defensive, uncrowded holding [Certain]. Price is above its 200-day average without being extended [Certain]. Macro is context only for this name (overlay) [Likely].
## Decision
```json
{
  "ticker": "CI",
  "decision": "TRIM",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin is down 2.8pp over three years from a FY2023 high of 5.2%, but the last 12 months are flat (+0.1pp), FCF/NI is 138.0%, ROIC and ROCE are rising and Q3 raised FY26 guidance (https://www.prnewswire.com/news-releases/the-cigna-group-reports-strong-third-quarter-2026-results-raises-2026-outlook-302930018.html); the margin dilution reflects low-margin pharmacy revenue growth, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "PBM rebate reform and GLP-1 cost pressure in 2027 (Q3 2026 call, https://stockanalysis.com/stocks/ci/transcripts/719833-q3-2026/) could structurally compress Evernorth spreads.",
    "veto": null
  },
  "thesis": "A deleveraging PBM and employer-health franchise with rising ROIC of 12.7% and a 10.40% FCF yield trades near the bottom of its own 5-year P/E range and below its EV/EBITDA minimum, where the price implies a revenue decline that raised 2026 guidance does not show.",
  "rationale": "Cheap on its own history with rising returns and raised guidance, but only one-point quality and balance-sheet scores plus open 2027 PBM reform risk leave the scorecard below the hold band. Conviction 3 means trimming to the smaller conviction-3 size, not selling: the thesis is intact.",
  "price_at_decision": 297.00,
  "price_date": "2026-11-13",
  "research_note": "research/CI/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, giving up most of the five-year improvement from 8.8% to 12.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 3.5%, under the FY2025 five-year low of 3.7%, showing rebate reform or medical cost pressure is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3.5}},
    {"text": "TTM FCF margin falls below 2.0%, well under the current 2.9%, signalling cash generation and buyback capacity are deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.0}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.87x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 408.94, "basis": "Guidance delivery and manageable 2027 reform re-rate the stock to the mechanical base fair value of 408.94 [IS,BS,CF,RA,ST,HI], consistent with the reverse DCF's undemanding -1.5% implied growth."},
    "base": {"probability": 0.50, "target_price_12m": 342.42, "basis": "P/E recovers from 13.2x toward its 5y median of 15.1x [RA], matching the P/E method's base value of 342.42 in the fact sheet, below the DCF-led blend because 2027 headwinds cap the re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 261.15, "basis": "PBM rebate reform compresses Evernorth spreads (Q3 call, https://stockanalysis.com/stocks/ci/transcripts/719833-q3-2026/) and the stock falls to the mechanical bear fair value of 261.15 [IS,BS,CF,RA,ST,HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores near its maximum, so a lower price would not lift the scorecard to the buy threshold; the gap is middling returns and leverage and the unresolved 2027 PBM rebate reform.",
  "new_evidence": {"type": "method_change", "text": "The 2026-11-08 HOLD at conviction 4 predates the scorecard (2026-11-09); the same evidence now scores 7, conviction 3."},
  "replaces": null,
  "replacement_reason": null
}
```
