# Evaluation: Ameriprise Financial, Inc. (AMP) — 2026-11-23
## Bear case
The fall to the entry level has no stock-specific shock behind it [Likely]; the worry is slow erosion. Operating margin has slipped 1.2pp in a year to 34.9% and gross margin is down from 61.7% in FY2021 to 54.6% TTM [Certain]. Recruiting competition for advisors is intense and lower short rates would cut sweep and bank spread income [Guessing]. Legacy annuity, universal life and long-term care books keep forcing assumption cuts: an unfavorable unlocking of $91 million this quarter [company-reported] (https://www.sec.gov/Archives/edgar/data/820027/000082002726000054/amp-20260930.htm), and certificate deposits have seen outflows for eleven quarters [company-reported]. Reported FCF (17.59% yield) includes insurance and bank balance-sheet flows, so the headline cash conversion overstates what can be returned [Likely]. ROIC is off its 2-year high, but that figure is distorted by a tiny equity base [Likely]. A further equity drawdown hits fees directly; beta is 1.12 [Certain].
## Bull case
A high-return, buyback-funded compounder at a low multiple [Likely]. ROE is 72.0% TTM and rising over five years; ROCE is flat at 4.1%, so the ROIC drop is a denominator effect, not a business break [Likely]. FCF margin is 36.4% TTM, up 4.8pp in a year [Certain]. Shares fell 5.85% YoY and a new multi-year repurchase authorization was announced [Likely] (https://stockanalysis.com/stocks/amp/transcripts/713968-q3-2026/). Q3 adjusted EPS rose and assets reached a record per management [Likely]. P/E 11.1x sits at 24% of its 5y range and 19% below peers; P/FCF 5.7x is near its 5y low [Certain]. The reverse DCF prices in -1.8% revenue growth [Certain], against a base fair value of 566.06 [Certain]. The 3-month fall tracks the market's risk-off move (SPY -9.5%), not a company event [Likely]; the macro overlay rates macro as context only.
## Decision
```json
{
  "ticker": "AMP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin is down 1.2pp over 12 months, driven by an unfavorable $91 million actuarial unlocking in Q3 versus a favorable item a year ago (10-Q MD&A, https://www.sec.gov/Archives/edgar/data/820027/000082002726000054/amp-20260930.htm); ROE and FCF margin are rising and ROCE is flat (RA-T), so it is a charge, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Advisor recruiting competition and lower short rates compress wealth-management margins while legacy insurance books keep needing assumption cuts.",
    "veto": null
  },
  "thesis": "A high-ROE, buyback-funded wealth manager trading at a low P/E and P/FCF versus its own history and peers, with the price implying shrinking revenue.",
  "rationale": "Quality and cash returns are strong and the price fall is market-driven, not a broken thesis, but the scorecard lands at 3 with only a moderate discount to the value blend. Below 4 it is an AVOID under the high-conviction-only owner rule.",
  "price_at_decision": 480.29,
  "price_date": "2026-11-20",
  "research_note": "research/AMP/2026-11-23.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 32%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 32}},
    {"text": "FCF margin (TTM) falls below 28%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "ROE (TTM) falls below 50%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 50}},
    {"text": "Share count stops shrinking (shares change YoY turns positive)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 658.3, "basis": "Buybacks and steady advisor growth lift the stock to the DCF base value of 658.30 [IS,CF,RA], below the blended bull 851.85 because legacy-book charges cap the multiple (note section 6)."},
    "base": {"probability": 0.5, "target_price_12m": 566.06, "basis": "P/E drifts back toward its 5y median 12.8x [RA] as the -1.8% revenue growth the reverse DCF implies proves too pessimistic; matches the mechanical base fair value 566.06."},
    "bear": {"probability": 0.25, "target_price_12m": 395.11, "basis": "Lower short rates and recruiting costs push operating margin down further and P/E toward its 5y low 9.9x [RA]; matches the mechanical bear fair value 395.11."}
  },
  "entry_price": 427,
  "entry_basis": "Valuation file base 566.06 x 0.85 sits above today's price, so the anchor is the scorecard: near 427 the value-blend upside reaches the top 30% band (one more valuation point, total 9 = conviction 4), with P/FCF then below its 5y low 5.6x [RA].",
  "replaces": null,
  "replacement_reason": null
}
```
