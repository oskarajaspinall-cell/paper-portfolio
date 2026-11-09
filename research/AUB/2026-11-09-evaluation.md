# Evaluation: Atlantic Union Bankshares Corporation (AUB) — 2026-11-09
## Bear case
ROE fell every fiscal year from 9.7% (FY2021) to 6.7% (FY2025) [Certain]; the 10.7% TTM rebound sits roughly at the cost of equity, so there is no demonstrated excess return or moat [Likely]. Shares rose 20.64% YoY, dilution from an acquisition, and the buyback only partly offsets it [Likely]. Q3 2026 showed margin pressure from rising funding costs, with FY26 loan growth and income outlooks toward the lower end of guidance [Likely]. The best valuation method (P/B + ROE, base 30.55) is below the 39.34 price, and the mechanical fair value is flagged unreliable (methods disagree 3.2x) [Certain]. The Direction change in FCF margin (210.9% to 35.9%) reflects bank cash-flow items such as loan sales, not a business deterioration, but it also means FCF yield gives no valuation support [Likely]. Piotroski F of 4 is weak [Certain]. Tier 2 issuance adds leverage [Likely].

## Bull case
P/E of 10.7x is below its own 5y minimum of 11.2x (median 14.4x) and slightly under the peer median of 11.1x [Certain]. P/B of 1.1x is 23% below peers at 1.4x [Certain]. TTM ROE has recovered to 10.7% and net margin to 34.7%, suggesting the FY2025 trough was acquisition-related one-offs rather than structural [Guessing]. Q3 delivered strong loan growth and solid credit quality [Likely], and the $250.0 million buyback [company-reported] (https://www.sec.gov/Archives/edgar/data/883948/000088394826000087/aub-20260930x10q.htm) can lift per-share returns as deal synergies come through [Likely]. Beta of 0.81 and short interest of 0.44% indicate low crowding [Certain]. If ROE holds and the P/E reverts toward its 5y median, there is meaningful upside [Guessing].

## Decision
```json
{
  "ticker": "AUB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The FCF-margin fall (210.9% to 35.9% TTM) is bank cash-flow noise from loan and investment flows, not operations [CF-T]; the FY ROE decline reversed to 10.7% TTM with net margin back to 34.7% after the FY2025 acquisition-related dip [RA, IS] (note section 2).",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Rising funding costs compress net interest margin, as flagged on the Q3 2026 call with outlooks at the lower end of guidance, keeping ROE near the cost of equity (https://stockanalysis.com/stocks/aub/transcripts/711276-q3-2026/).",
    "veto": null
  },
  "thesis": "A post-acquisition regional bank trading below its own 5-year minimum P/E, but with ROE only around its cost of equity, funding-cost pressure and a best-method fair value below the price, so the discount looks deserved rather than mispriced.",
  "rationale": "Cheap on earnings, fair on book: P/B + ROE base sits below the price and the blended fair value is unreliable. Returns do not exceed the cost of equity, there is no demonstrated moat, and funding costs are pressuring margins. Scorecard conviction 2, below the buy bar, so AVOID; cash is acceptable.",
  "price_at_decision": 39.34,
  "price_date": "2026-11-06",
  "research_note": "research/AUB/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls back below 8%, showing the recovery from the FY2025 trough was temporary.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 28%, showing funding-cost pressure is eroding earnings power.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Share count grows a further 25% or more year on year without matching earnings growth (further dilutive M&A).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 25}},
    {"text": "A quarterly release cuts FY26 loan growth or income guidance below the stated range (https://www.atlanticunionbank.com)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 52.0, "basis": "ROE holds near 10.7% TTM [RA] and the P/E re-rates toward its 5y median of 14.4x [RA], below the mechanical bull fair value of 66.53 because the FCFE method is distorted by bank cash flows."},
    "base": {"probability": 0.5, "target_price_12m": 41.0, "basis": "P/E drifts to the peer median of 11.1x [RA, peers] as Q3 funding-cost pressure caps earnings growth (Q3 2026 call); below the unreliable blended base of 46.43 and above the P/B + ROE base of 30.55."},
    "bear": {"probability": 0.25, "target_price_12m": 30.5, "basis": "Funding costs push ROE back toward FY2025's 6.7% [RA] and the stock trades at the P/B + ROE base of 30.55, near the 52-week low of 30.87 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: returns near the cost of equity with no demonstrated moat are the obstacle, not price alone, and the blended fair value is unreliable; no entry price set.",
  "replaces": null,
  "replacement_reason": null
}
```
