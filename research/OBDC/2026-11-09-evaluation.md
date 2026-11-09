# Evaluation: Blue Owl Capital Corporation (OBDC) — 2026-11-09
## Bear case
Earnings power is weakening beneath a steady headline: TTM ROE has halved to 4.7% from 9.4% in FY2025 and net margin fell to 20.8% from 33.9%, so marks and costs are absorbing income [Certain]. The **Direction change** in operating margin (76.1% -> 75.1% over 12 months, against a rising 5-year trend) is small but points the same way as rate-driven funding costs and fee drag [Likely]. P/E of 16.3x sits above its 5y max: the stock is not cheap on earnings, only on book [Certain]. Shares rose 4.53% YoY, diluting per-share growth [Certain]. The macro overlay flags a fresh risk-premium shock (HY spread +0.77pp in 3m, VIX 28.18) that the price has barely reflected; non-accruals, PIK share and software exposure are [data unavailable], so credit risk cannot be sized [Likely]. Returns near the cost of equity give no moat [Likely]. The fair value is flagged unreliable [Certain].

## Bull case
P/B of 0.8x is below its 5y range and 20% under the 1.0x peer median, while Q3 NAV per share rose to 14.32 and adjusted NII covered the dividend, per the Q3 headline and transcript [Likely]. The earnings engine looks intact: ROIC is flat at 8.1% year on year and operating margin, at 75.1%, remains near its 2-year high of 76.4% [Certain]. The ROE drop is below the line (unrealised marks), which can reverse if credit stays stable, as the Q3 call reported [Likely]. Higher policy rates lift floating-rate income, and the price implies only 2.3% year-1 growth [Certain]. Accretive buybacks below NAV add per-share value [Likely]. Beta of 0.70 limits market drawdowns [Certain]. If credit holds, a re-rating toward the peer P/B plus the dividend gives a respectable total return [Guessing].

## Decision
```json
{
  "ticker": "OBDC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin fell only -1.0pp to 75.1% [IS-T] while ROIC is flat at 8.1% vs 8.1% a year earlier [RA-T]; the earnings engine is intact and Q3 NAV per share rose to 14.32 with NII covering the dividend (https://stockanalysis.com/stocks/obdc/transcripts/726407-q3-2026/).",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "A credit-cycle turn: HY spreads +0.77pp in 3m and VIX 28.18 (macro overlay) could raise non-accruals and cut NAV marks; non-accrual data is unavailable.",
    "veto": null
  },
  "thesis": "A discounted-to-book floating-rate direct lender whose NII engine is intact, but whose upside depends on credit losses staying low as spreads widen.",
  "rationale": "Cheap on book (P/B 0.8x, below its 5y range) but not on earnings (P/E above its 5y max), no moat, ROIC 8.1%, ROE halved, credit data unavailable and the macro overlay tilts toward bear. Scorecard conviction 2: AVOID; cash is acceptable.",
  "price_at_decision": 10.94,
  "price_date": "2026-11-06",
  "research_note": "research/OBDC/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 72%: the NII engine is eroding, not just marks.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 72}},
    {"text": "ROIC (TTM) falls below 6.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6.5}},
    {"text": "Share count growth exceeds 8% YoY (dilution below NAV).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 8}},
    {"text": "ROE (TTM) stays below 5% for two more quarters, i.e. NAV erosion rather than a timing effect.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 13.57, "basis": "Credit holds and P/B moves from 0.8x toward the 1.0x peer median [RA,P:ARCC] on Q3 NAV of 14.32, retesting the 52-week high of 13.57 [HI]; below the mechanical bull of 39.90, which the fact sheet flags unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 11.9, "basis": "NII covers the dividend and P/B drifts back toward its 5y median of 0.9x [RA], in line with the mechanical base fair value of 11.90 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.35, "target_price_12m": 9.81, "basis": "Spreads widen further and marks fall (macro overlay tilt toward bear, small, moved probability from base to bear), sending the price back to its 52-week low of 9.81 [HI], below the mechanical bear of 10.16."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
