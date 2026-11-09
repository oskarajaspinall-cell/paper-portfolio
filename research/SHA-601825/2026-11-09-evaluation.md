# Evaluation: Shanghai Rural Commercial Bank Co., Ltd. (SHA:601825) — 2026-11-09
## Bear case
Returns are sliding: ROE fell from 11.3% (FY2021) to 9.5% TTM, below a 10% hurdle, and the decline is steady rather than a one-off [Certain]. Net margin rising to 52.8% while ROE falls means equity is compounding faster than earnings, a sign of lending-spread compression in China's falling-rate environment, which looks structural rather than cyclical [Likely]. Piotroski F of 3 is weak [Certain]. The stock is not cheap against its own history: P/E 7.1x sits at the 92% position of its 5y range and above the peer median 6.6x; P/B 0.6x is at its 5y median [Certain]. The mechanical fair value is flagged unreliable (methods disagree 3.0x; the DDM gives 4.53) [Certain]. The FCF margin drop of 152.1pp is balance-sheet flow noise for a bank, so it neither helps nor hurts, but it leaves no cash-based check on quality [Likely]. Capital ratios and asset quality are [data unavailable] [Certain].
## Bull case
A Shanghai deposit franchise trading at 0.6x book with net margin near five-year highs (52.8% TTM) [Certain]. Share count is stable (0.21% YoY), so there is no dilution [Certain]. The P/B + ROE method gives a base of 12.29 CNY against a 9.04 close, and the reverse DCF implies a -7.5% year-1 revenue decline that a stable lender may not deliver [Certain]. Beta of -0.05 makes it a diversifier [Certain]. The macro overlay finds the CNY stable at 6.6538 per USD and weights macro as context only [Certain]. If ROE stabilises near 9.5%, a re-rating toward the peer P/B of 0.7x is plausible [Guessing].
## Decision
```json
{
  "ticker": "SHA:601825",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The only metric flagged as falling is FCF margin (172.5% to 20.3% TTM [CF-T,IS-T]), which for a bank swings with loan and deposit flows (-52.3% to 572.0% across fiscal years [CF,IS]) rather than operations, while net margin rose to 52.8% [IS]. Separately, ROE has fallen from 11.3% to 9.5% [RA], which the bear case treats as the real, likely structural, weakness.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Continued ROE erosion from net interest margin compression and unseen asset-quality deterioration (capital and NPL data unavailable), leaving the stock a value trap at 0.6x book.",
    "veto": null
  },
  "thesis": "A Shanghai regional bank at 0.6x book whose ROE has slipped below 10% and whose P/E sits near the top of its own 5-year range, so the low book multiple reflects declining returns rather than mispricing.",
  "rationale": "ROE is below the quality hurdle and still falling, P/E is near its 5y high and above peers, and the fair value is flagged unreliable. Book-value cheapness alone is not a high-conviction case; the scorecard gives conviction below the buy bar, so AVOID.",
  "price_at_decision": 9.04,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601825/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE recovers above 11% (statistics page), reversing the five-year decline from 11.3% and showing spread compression has ended.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 11}},
    {"text": "TTM ROE falls below 8.5% (statistics page), confirming structural erosion of returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8.5}},
    {"text": "TTM net margin falls below 45% (statistics page), showing provisions or spread pressure are biting into profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}},
    {"text": "Shares outstanding rise more than 5% year on year (statistics page), indicating a recapitalisation.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.54, "basis": "ROE stabilises near 9.5% [RA] and P/B moves toward the peer median 0.7x [RA], reaching the fact sheet's bear fair value of 10.54 rather than the unreliable base."},
    "base": {"probability": 0.5, "target_price_12m": 9.04, "basis": "P/B holds at its 5y median 0.6x [RA] as ROE drifts lower; the price stays near the 9.04 close, below the flagged-unreliable mechanical base of 12.79 because the falling ROE argues against the P/B + ROE assumption."},
    "bear": {"probability": 0.25, "target_price_12m": 7.36, "basis": "Further ROE erosion pushes P/E back from 7.1x toward its 5y median 6.7x [RA] and the price back to its 52-week low of 7.36 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE is below 10% and still falling, and the fair value is flagged unreliable, so a lower price alone would not lift conviction to 4; a halt in the ROE decline would.",
  "replaces": null,
  "replacement_reason": null
}
```
