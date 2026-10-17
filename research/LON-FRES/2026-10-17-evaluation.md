# Evaluation: Fresnillo plc (LON:FRES) — 2026-10-17
## Bear case
Fresnillo is a price-taker whose TTM returns (ROIC 65.7%, operating margin 59.4% vs 21.0% in FY2024 [IS,RA]) come from metal prices, not a better asset base [Certain]. Production fell on lower ore grades in both Q1 and Q2 2026 (WSJ headlines in fact sheet) [Likely], so volumes are not offsetting any price retreat. The mechanical EV/EBITDA fair value, normalised for peak earnings, puts base at 1,440.45 GBX and bear at 784.72 GBX, both well below the 2,719.00 close [Certain]. P/B of 4.8x sits 68% above peers, capitalising peak ROE [Certain]. The macro overlay (primary weight) tilts moderately bear: the 10y real yield is up +0.43pp/3m to 2.78% and the dollar index rose sharply over one month, both headwinds for gold/silver [Certain]. The 50-day sits below the 200-day (-9.8%) and earnings are due Oct 20, 2026 [Certain].
## Bull case
Trailing multiples are cheap: P/E 11.7x is below its own 5y minimum of 21.1x and the peer median of 14.1x; EV/EBITDA 6.3x is below the peer median of 7.4x [Certain]. Cash generation is real: FCF margin 37.7% TTM, FCF conversion 99.3%, FCF yield 8.52% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.41x) with Piotroski F 7 and Altman Z 12.43, funding the Mexico/Canada pipeline without leverage [Certain]. Management held full-year guidance despite the grade declines [Likely]. If real yields and the dollar stall (credit spreads widening to 3.23% may brake the Fed, per the overlay), metal prices could hold and the stock could rerate toward its 5y median EV/EBITDA of 9.6x [Guessing].
## Decision
```json
{
  "ticker": "LON:FRES",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Fresnillo's cheap trailing multiples rest on peak, price-driven margins while ore grades decline and the macro backdrop (rising real yields, stronger dollar) works against gold and silver.",
  "rationale": "No durable moat: margins are spot-metal pass-through with falling grades, the normalised fair value sits far below the price, and the primary-weight macro overlay tilts moderately bear. Strong cash and net cash do not offset that. Conviction 2 is below the buy threshold; cash is the better holding.",
  "price_at_decision": 2719.00,
  "price_date": "2026-10-16",
  "research_note": "research/LON-FRES/2026-10-17.md",
  "triggers": [
    {"text": "Company-reported production volumes and ore grades stabilise or rise in the next quarterly filing, reversing the Q1/Q2 2026 declines."},
    {"text": "Gross margin [IS] holds above 45% for two more quarters while silver/gold spot prices ease, showing resilience beyond price pass-through."},
    {"text": "ROIC [RA] stays above 30% for full-year FY2026 despite lower average realised metal prices, showing returns durable beyond the cycle peak."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 3900, "basis": "Real yields and the dollar stall (macro overlay macro_bull) so TTM margins hold and EV/EBITDA rerates from 6.3x toward its 5y median 9.6x [RA] on TTM EBITDA [IS]; below the mechanical bull 4,842.12 because declining grades cap volumes."},
    "base": {"probability": 0.45, "target_price_12m": 2400, "basis": "Margins ease from TTM 59.4% toward FY2025's 45.9% operating margin [IS] at roughly peer-median EV/EBITDA 7.4x [RA]; above the mechanical base 1,440.45 because net cash (-0.41x [BS,IS]) and strong FCF conversion support a premium to fully normalised earnings."},
    "bear": {"probability": 0.35, "target_price_12m": 1440.45, "basis": "Real yields and the dollar keep rising (macro overlay tilt moderate toward bear, which raises this probability) so metal prices fall and EBITDA normalises to the fair-value base 1,440.45 on EV/EBITDA [RA,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2 (below the 3 that requires an entry price): the obstacle is price-taker economics with declining ore grades and a bearish macro chain, not just valuation.",
  "replaces": null,
  "replacement_reason": null
}
```
