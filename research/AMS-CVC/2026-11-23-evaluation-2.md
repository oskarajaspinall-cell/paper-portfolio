# Evaluation: CVC Capital Partners plc (AMS:CVC) — 2026-11-23
## Bear case
Earnings are carry-heavy and carry needs exits. Management said H1 deal activity was muted and some exits await regulatory approval [Likely]; the macro overlay shows real yields up 0.53pp and high-yield spreads up 0.77pp over 3 months with VIX at 28.44, the conditions that push realisations out [Certain]. The **Direction change** lines matter: operating margin sits 5.9pp and FCF margin 7.7pp below their 2-year highs, and ROIC 5.4pp below its 35.8% peak, so 2024 was a carry peak, not a run-rate [Likely]. FCF conversion fell to 73.4% and Piotroski F is 3 [Certain]. The cheapness on own history is partly an artefact: the 5-year P/E range (median 56.6x) spans the IPO-era distortion [Likely]. Share count rose 1.16%, the IRCA withdrawal shows deal execution risk, and a CFO transition adds noise [Likely]. A credit shock could compress the multiple toward its 12.8x low [Guessing].
## Bull case
A 30.4% ROIC, 51.2% operating margin, 35.3% FCF margin franchise trades at 17.9x earnings, 34% below the BX/KKR/APO/ARES median, with EV/EBITDA (13.4x) and P/FCF (19.8x) below their 5-year minimums and a 5.04% FCF yield [Certain]. The recent direction is better than the peaks suggest: over the last 12 months operating and FCF margins each rose 2.5pp and ROCE 1.7pp, while ROIC was flat, so the gap to 2024 is carry timing normalising, not erosion [Likely]. Management fees on locked-up capital are recurring and LP re-ups follow track record, a narrow moat [Likely]. Leverage fell from 2.73x to 1.15x net debt/EBITDA [Certain]. The reverse DCF needs only 5.2% year-1 revenue growth, undemanding against H1's double-digit AUM and revenue growth described on the call [Likely]. The pipeline (Entain CEE, Parfums de Marly, Aldermore) shows deployment continues [Likely].
## Decision
```json
{
  "ticker": "AMS:CVC",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing is falling over 1 or 3 years: ROIC, operating and FCF margin sit below their 2024 highs, but operating and FCF margin rose 2.5pp each over the last 12 months [IS-T, CF-T] and ROIC was flat; the 2024 peak reflects carry timing, with management citing muted H1 exits awaiting regulatory approval (https://stockanalysis.com/quote/ams/CVC/transcripts/557778-h1-2026/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Tighter credit and higher real yields (macro overlay) delay exits, so carry and FCF conversion slip and the P/E compresses rather than re-rates.", "veto": null},
  "thesis": "A high-return private-markets franchise with recurring locked-up fees trades below its own 5-year multiples and well below US peers, with carry timing the swing factor.",
  "rationale": "Scorecard gives 4 on high, steady returns, low leverage and a real discount to own-history multiples and peers, offset by carry-timing risk under tighter credit. Python sizes it; cash sits near the floor, so it replaces CI, a conviction-3 holding below the buy bar.",
  "price_at_decision": 13.37,
  "price_date": "2026-11-20",
  "research_note": "research/AMS-CVC/2026-11-23.md",
  "new_evidence": {"type": "method_change", "text": "The earlier AVOID 3 (2026-11-08) predates the scorecard (2026-11-09); re-scored under the current rules it lands on the other side of the buy line, and the price has since fallen through that evaluation's entry price."},
  "triggers": [
    {"text": "TTM ROIC (ratios page) falls below 20%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 42%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 42}},
    {"text": "Net debt / EBITDA rises above 2.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "Shares outstanding grow more than 5% year on year (dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 20.3, "basis": "Exits reopen and the P/E moves to the 27.2x peer median [RA, P:BX/KKR/APO/ARES]; below the mechanical bull because a carry-driven multiple stays capped by lumpy realisations."},
    "base": {"probability": 0.45, "target_price_12m": 16.0, "basis": "Fees keep compounding and the P/E recovers part of the gap to peers from 17.9x [RA]; well below the mechanical base 24.54 because that DCF capitalises fee growth without a carry-timing discount."},
    "bear": {"probability": 0.30, "target_price_12m": 9.6, "basis": "Macro overlay tilt toward bear (small): wider spreads delay realisations and the P/E falls to its 5y low 12.8x [RA]; bear probability raised for the overlay's credit tightening."}
  },
  "replaces": "CI",
  "replacement_reason": "CI is held at conviction 3, below the buy bar; CVC clears it at 4 with a deep discount to its own multiples, so the freed cash is better used here (my judgement)."
}
```
