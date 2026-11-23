# Evaluation: CVC Capital Partners plc (AMS:CVC) — 2026-11-23
## Bear case
The fall to the entry price has no company-specific results trigger: no earnings-type reaction in the last 10 sessions, and the 3-month move of -11.3% roughly tracks SPY's -9.5% [Certain]. What drives it is the macro chain: HY spreads +0.77pp and real yields +0.53pp in 3 months threaten exits and therefore carry [Likely] (macro overlay). Carry is lumpy: ROIC is 5.4pp below its 2-year high, operating margin 5.9pp and FCF margin 7.7pp below theirs, and FCF conversion fell to 73.4% of net income [Certain]. H1 deal activity was muted, some exits await regulatory approval, and a CFO transition was announced [Likely]. Piotroski F of 3 is weak and the share count is up 1.16% YoY [Certain]. The mechanical fair value range (6.20 to 51.45) is too wide to anchor on [Likely]. P/B of 8.9x sits above peers [Certain].

## Bull case
Fees are recurring on locked-up capital, so a delayed realisation cycle defers carry rather than destroying it [Likely]. The last-12-month direction is up, not down: operating margin +2.5pp, FCF margin +2.5pp, ROCE +1.7pp, with ROIC flat at 30.4% [Certain]; the gaps to the 2-year highs reflect a strong 2024 carry year [Likely]. Leverage fell from 2.73x to 1.15x net debt/EBITDA [Certain]. The stock trades at 17.9x P/E, 6% up its 5-year range and 34% below the BX/KKR/APO/ARES median, with EV/EBITDA (13.4x) and P/FCF (19.8x) below their 5-year minimums and a 5.04% FCF yield [Certain]. The reverse DCF implies only 5.2% year-1 revenue growth, undemanding for a manager whose H1 call cited double-digit AUM and revenue growth [Likely]. The deal pipeline (Entain CEE, Parfums de Marly, Aldermore) shows capital is being deployed [Likely].

## Decision
```json
{
 "ticker": "AMS:CVC",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds nothing falling over 1 or 3 years; the gaps to the 2-year highs date from the strong 2024 carry year, and over the last 12 months operating and FCF margin rose 2.5pp each with ROIC flat (fact sheet RA-T, IS-T, CF-T).",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Tighter credit (HY spread +0.77pp in 3m, macro overlay) delays exits, pushing carry out and compressing the P/E; recurring fee income cushions it.",
  "veto": null
 },
 "new_evidence": {
  "type": "method_change",
  "text": "The 2026-11-08 AVOID at conviction 3 predates the scorecard (2026-11-09); conviction is now set by scripts/scorecard.py on the 2026-11-23 fact sheet."
 },
 "thesis": "A high-return, deleveraging private-markets manager with recurring fees trades below its own 5-year minimum EV/EBITDA and P/FCF and well below peers on P/E, where the price implies modest growth.",
 "rationale": "The fall is market and credit driven, not a broken business: last-12-month margins rose, leverage fell and multiples sit below their own 5-year lows. Scorecard conviction 4, standard core size set by Python; cash is at the floor, so it replaces CI, a below-bar conviction-3 holding.",
 "price_at_decision": 13.37,
 "price_date": "2026-11-20",
 "research_note": "research/AMS-CVC/2026-11-23.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 20%, well under the 30.4% now, showing fee and carry economics have weakened structurally.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 20
   }
  },
  {
   "text": "TTM operating margin falls below 42%, under the FY2023 level of 47.7%, showing fee-related earnings compression rather than carry timing.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 42
   }
  },
  {
   "text": "Net debt/EBITDA rises above 2.0x from 1.15x, reversing the deleveraging.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 2.0
   }
  },
  {
   "text": "Shares change YoY exceeds 5%, showing dilution.",
   "check": {
    "source": "statistics",
    "field": "sharesgrowthyoy",
    "op": ">",
    "value": 5
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.2,
   "target_price_12m": 20.3,
   "basis": "Exits reopen and the P/E moves toward the 27.2x peer median [RA,P:BX,P:KKR,P:APO,P:ARES] on TTM earnings; below the 24.54 base fair value, whose range is too wide to trust."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 16.2,
   "basis": "Fees grow and carry recovers gradually; the stock regains the 16.20 52-week high [HI] as EV/EBITDA moves back toward its 15.7x 5-year minimum [RA], below the mechanical base fair value."
  },
  "bear": {
   "probability": 0.3,
   "target_price_12m": 10.5,
   "basis": "Credit stress delays realisations and FCF conversion falls further; the price revisits the 10.50 52-week low [HI]; probability raised by the macro overlay's small tilt toward bear (2026-11-23-macro.md)."
  }
 },
 "replaces": "CI",
 "replacement_reason": "Cash is at the 1.5% floor, so the buy needs funding; CI is held at conviction 3, below the buy bar, while CVC scores 4 with higher returns, lower leverage and multiples below their own 5-year minimums.",
 "second_opinion": {
  "file": "research/AMS-CVC/2026-11-23-evaluation-2.md",
  "conviction": 4
 }
}
```
