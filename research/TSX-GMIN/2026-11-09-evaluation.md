# Evaluation: G Mining Ventures Corp. (TSX:GMIN) — 2026-11-09
## Bear case
The price already pays for the good news. EV/EBITDA of 20.0x sits above its whole 5y range (15.9x-17.5x) and far above the 6.9x peer median; EV/Sales of 14.9x is roughly triple peers [Certain]. The mechanical base fair value of 49.78 CAD leaves only a thin margin over the 47.21 close [Certain]. Returns are set by the gold price, not a competitive barrier, so the 65.9% operating margin is cyclical [Likely]. Direction change: FCF margin fell from 6.5% to -16.3% over the last year as Oko West construction capex outran operating cash [Likely]; that is temporary investment, not operating decay, but it leaves the stock with a negative FCF yield until a project in Guyana is delivered on time [Likely]. Shares rose 4.36% YoY [Certain]. The macro overlay tilts toward bear (small): higher real yields and a firmer dollar would hit margin and multiple together [Likely]. Results on Nov 12, 2026 add near-term gap risk [Certain].
## Bull case
The business has transformed: ROIC 23.8% TTM from -3.8% in FY2023, and rising over the last 12 months as well (+12.5pp) [Certain]. The balance sheet is net cash (net debt/EBITDA -0.40x), Piotroski F is 8 and Altman Z is 10.63 [Certain], so Oko West is funded without stress [Likely]. P/E of 22.0x is below its 5y minimum of 23.9x [Certain]. Management targets annual production near 1 million ounces across key assets with first gold at Oko West expected next September [Likely], which would turn FCF sharply positive and make today's EV/EBITDA look backward-looking [Guessing]. A new buyback (2026-08-28) signals confidence [Certain]. The 6-month fall of 13.5% from the 56.66 high has reset some of the enthusiasm [Certain].
## Decision
```json
{
  "ticker": "TSX:GMIN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling (6.5% to -16.3% TTM [CF-T,IS-T]) while ROIC and operating margin rise; the note attributes it to Oko West construction capex with first gold expected next September (https://stockanalysis.com/quote/tsx/GMIN/transcripts/634674-mining-forum-americas-2026/), and net debt/EBITDA is -0.40x [BS,IS].",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "A lower gold price (macro overlay: higher real yields, firmer dollar) compressing both the 65.9% operating margin and the 20.0x EV/EBITDA multiple, or a delay at Oko West.",
    "veto": null
  },
  "thesis": "A newly high-return, net-cash gold producer funding a growth project, but priced above its own EV/EBITDA history and peers with little margin to mechanical fair value.",
  "rationale": "Quality and balance sheet are strong and the FCF dip is investment-driven, but valuation offers little room: EV/EBITDA above its 5y range and peers, base fair value barely above the close, and returns are a gold-price derivative with no moat. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 47.21,
  "price_date": "2026-11-06",
  "research_note": "research/TSX-GMIN/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Operating margin (TTM) falls below 55%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 55}},
    {"text": "Net debt/EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Oko West first gold delayed beyond the first half of 2028 per company releases"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 58.74, "basis": "Oko West stays on schedule and the gold price holds, so ROIC 23.8% and the 65.9% operating margin [RA,IS] persist and the price retakes its 52-week high of 58.74 [HI], above the mechanical bull of 52.02."},
    "base": {"probability": 0.45, "target_price_12m": 49.78, "basis": "Margins hold but EV/EBITDA stays near its own history, in line with the mechanical base fair value of 49.78 CAD (EV/EBITDA method) [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 37.0, "basis": "Gold softens on higher real yields and a firmer dollar (macro overlay research/TSX-GMIN/2026-11-09-macro.md, tilt toward bear, small, which raised this probability), so the multiple compresses toward its 5y median 16.7x [RA] on lower EBITDA, near the late-October swing low of 36.89 [HI]."}
  },
  "entry_price": 39.82,
  "entry_basis": "valuation file: base 49.78 x 0.8 (owner margin of safety); at that price the valuation pillar would support conviction 4 on the same quality evidence.",
  "replaces": null,
  "replacement_reason": null
}
```
