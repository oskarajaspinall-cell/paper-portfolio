# Evaluation: Guangdong Investment Limited (HKG:0270) — 2026-11-09
## Bear case
Returns are utility-like and near the cost of capital: ROIC 8.1% TTM and ROE 9.2% FY2025, flat over five years [Certain]. The Direction change is real: FCF margin fell from 46.8% to 41.6% over the last 12 months, 15.0pp below its 2-year high of 56.5% [Certain]; FY2023-24 FCF conversion above 300% was likely a working-capital or capex swing, so headline FCF yield of 15.14% overstates the run rate [Likely]. P/FCF of 6.6x is already above its 5y maximum of 5.6x [Certain]. The mechanical fair value is unreliable (methods disagree 2.8x) and the dividend-discount value of 6.00 HKD sits below the price [Certain]. Parent GDH controls the company; minority holders depend on its priorities [Likely]. Mainland water tariff regulation is unchecked and the regional revenue split is unverified (macro overlay) [Guessing]. Conglomerate assets (stores, hotels, property) dilute water returns [Likely].
## Bull case
The balance sheet has been repaired: net debt/EBITDA fell from 3.96x (FY2022) to 0.60x TTM [Certain]. Operating margin rose from 26.9% to 38.0% TTM and held flat over the last year, as did ROIC [Certain], so the FCF dip looks like normalisation from a peak, not erosion [Likely]. EV/EBITDA of 7.4x sits at the 9th percentile of its 5y range and well below the peer median of 11.9x [Certain]; P/E 10.9x is below its 5y median of 11.9x [Certain]. The reverse DCF implies -18.0% year-1 revenue growth, a harsh assumption for a regulated water supplier [Likely]. Beta 0.63 and Piotroski F of 6 support a low-risk compounder profile [Certain]. Regulated or contracted water is hard to replicate [Likely].
## Decision
```json
{
  "ticker": "HKG:0270",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Only FCF margin is falling (46.8% to 41.6% TTM) while operating margin and ROIC are flat over the last year [IS-T, RA-T]; FY2023-24 FCF conversion above 300% was a working-capital/capex swing normalising, with net debt/EBITDA at 0.60x [BS,IS] (note section 2).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Mainland water tariff regulation or parent (GDH) priorities cap returns; regional mix and policy unverified (macro overlay).", "veto": null},
  "thesis": "A deleveraged Guangdong water utility on a low EV/EBITDA, but with near-cost-of-capital returns and a normalising FCF margin the earnings multiples are only modestly cheap.",
  "rationale": "Balance sheet and margins are solid, but ROIC of 8.1% is modest, the fair value is flagged unreliable and P/E sits near peers. Good but not compelling; below the buy bar, so AVOID and watch for a lower entry.",
  "price_at_decision": 8.16,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-0270/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 6.0%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6.0}},
    {"text": "Operating margin (TTM) falls below 33%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 33}},
    {"text": "Net debt / EBITDA rises above 2.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "FCF margin (TTM) falls below 30%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.0, "basis": "EV/EBITDA re-rates toward its 5y median 9.3x from 7.4x [RA] on TTM EBITDA [IS] with low net debt [BS]; below the unreliable mechanical bull of 17.16 because the DCF leans on peak FCF."},
    "base": {"probability": 0.5, "target_price_12m": 8.9, "basis": "P/E returns to its 5y median 11.9x from 10.9x [RA] on flat TTM earnings [IS]; below the flagged-unreliable base fair value of 13.08, closer to the P/E method's 9.01."},
    "bear": {"probability": 0.25, "target_price_12m": 7.1, "basis": "P/E falls to its 5y low 9.5x [RA] as FCF margin keeps normalising [CF-T]; above the mechanical bear of -3.20, which the unreliable DCF drives."}
  },
  "entry_price": 7.1,
  "entry_basis": "P/E back at its 5y low of 9.5x [RA]; the base fair value less 20% sits above the price and the fair value is flagged unreliable, so the own-history P/E floor anchors the entry.",
  "replaces": null,
  "replacement_reason": null
}
```
