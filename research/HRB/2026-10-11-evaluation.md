# Evaluation: H&R Block, Inc. (HRB) — 2026-10-11
## Bear case
Assisted tax prep is a mature, ex-growth category facing two structural threats HRB itself flags: free government filing and AI-enabled DIY tools that could "reduce the need for third-party tax preparation services" [Likely]. Short interest of 15.49% of float shows a live, informed bear thesis [Certain]. The 12-month change is -12.7%, lagging SPY by 28.4pp, and the stock has already given back from the 58.67 post-results high to 44.05 [Certain]. Gross margin has drifted down 1.3pp over five years and FCF conversion fell from 134.8% to 103.1% [Certain]. The mechanical DCF base of 92.38 assumes historical growth persists; the EV/EBITDA method gives only 54.02, so most of the "upside" rests on a model blind to disruption [Likely]. The portfolio already owns INTU, adding concentrated exposure to US tax-filing economics [Certain].

## Bull case
At 7.7x P/E, 6.4x EV/EBITDA and a 13.92% FCF yield, HRB trades in the bottom 14–18% of its own five-year range and 49–66% below peers [Certain]. Quality is improving, not eroding: operating margin rose to 23.0%, net margin to 18.6% and ROIC (FY) to 65.4% over five years [Certain]. The price implies a -15.4% year-1 revenue decline, while management guides FY2027 revenue growth of +3.9–5.1% and FY2026 beat on EPS [Likely]. Capital returns are large and self-funded: share count -6.17% YoY with net debt/EBITDA flat at 1.11x, plus a further $400m buyback guided [Certain]. Demand is near-mandatory and non-cyclical, beta is 0.39, and Altman Z 3.24 shows no distress [Certain]. Even no rerating compounds via buybacks and FCF; a move toward the 5y median 7.9x EV/EBITDA lifts value meaningfully [Likely].

## Decision
```json
{
  "ticker": "HRB",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A 23%-operating-margin, high-ROIC assisted tax-prep leader trades in the bottom fifth of its own 5-year multiples at a 13.92% FCF yield, where the price implies a -15.4% revenue decline that guided growth and 6% annual share shrinkage do not support.",
  "rationale": "Cheap on every own-history and peer multiple, improving margins, self-funded buybacks and a non-cyclical, low-beta demand base give a favourable skew even on conservative EV/EBITDA-based targets. Disruption risk and INTU overlap keep conviction at 4, not 5: standard 7% core size. Cash, sector and holding limits are not breached.",
  "price_at_decision": 44.05,
  "price_date": "2026-10-09",
  "research_note": "research/HRB/2026-10-11.md",
  "target_weight_pct": 7,
  "triggers": [
    {"text": "TTM gross margin falls below 43%, breaking the five-year low (44.3% TTM, 44.3%-45.7% FY range), signalling price pressure from free/AI filing alternatives.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 43}},
    {"text": "TTM operating margin falls below 20%, under the five-year low of 21.5% (FY2022), showing the margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 five-year low of 15.9%, meaning cash generation no longer funds the buyback and dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Annual revenue (income statement) declines year on year for a full fiscal year, or management discloses a loss of assisted-category share, evidencing real displacement by free or DIY filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 63.00, "basis": "EV/EBITDA rerates toward the top of its 5y range (5y median 7.9x, max 9.3x [RA]) as FY2027 growth guidance is delivered, matching the EV/EBITDA bull fair value of 63.00 [fact sheet Fair value]; below the 110.48 blended bull because the DCF's historical growth ignores disruption risk."},
    "base": {"probability": 0.45, "target_price_12m": 54.02, "basis": "EV/EBITDA returns toward its 5y median 7.9x [RA] on TTM EBITDA, the EV/EBITDA base fair value of 54.02 [fact sheet Fair value]; we deliberately sit below the 92.38 blended base because the DCF capitalises past growth the free-filing/AI debate makes uncertain."},
    "bear": {"probability": 0.30, "target_price_12m": 37.58, "basis": "Disruption fears deepen (short interest 15.49% [ST]) and EV/EBITDA holds near its 5y low 5.8x [RA], the EV/EBITDA bear fair value of 37.58 [fact sheet Fair value], near the 39.50 September swing low [HI]."}
  },
  "entry_price": null,
  "entry_basis": null,
  "replaces": null,
  "replacement_reason": null
}
```
