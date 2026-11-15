# Evaluation: Bank of Chengdu Co., Ltd. (SHA:601838) — 2026-11-15
## Bear case
ROE has fallen every year since FY2022, from 17.7% to 14.3% in FY2025 and 13.3% TTM [RA], while net margin rose [IS]: equity is compounding faster than profit, so returns keep diluting with no reset in sight [Likely]. The re-rating is done: P/E of 6.6x sits above its 5y maximum of 5.8x [RA] and P/B of 0.8x is at its median and above peers' 0.7x [RA]; the 20.4% 12-month gain and a price 13.3% above the 200-day average [ST] leave room for a de-rating back toward the 5.5x median if earnings growth slows [Likely]. Asset quality, NPLs and capital ratios are not on the fact sheet, so the main risk for a Sichuan regional lender (property and local-government credit) is unmeasured [Certain]. The fair value is flagged unreliable, with methods 3.8x apart and the dividend discount at 9.93 [ST] [Certain]. Piotroski F is 4 [ST] [Certain].

## Bull case
A 13.3% ROE [RA] is still a solid level for a bank, earned at only 0.8x book [RA] and 6.6x earnings, below the peer median of 7.0x [RA] [Certain]. Net margin has risen to 63.1% TTM from 60.2% in FY2021 [IS], so revenue is converting to profit better, not worse [Certain]. The trend is working: price above both moving averages, 50-day 6.9% over the 200-day, and relative strength positive against SPY over 3, 6 and 12 months [HI] [Certain]. Dilution is mild at 1.37% YoY [ST] [Certain]. Chengdu is a fast-growing western hub and the local deposit franchise may be sticky [Guessing]. The P/B + ROE fair value base of 30.13 [ST] sits well above the price even after its unreliability flag [Certain].

## Decision
```json
{
  "ticker": "SHA:601838",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no 1y or 3y decline in the scored metrics; on the 5y fiscal view ROE fell from 17.7% (FY2022) to 13.3% TTM [RA] while net margin rose [IS], which the note attributes to equity growing faster than profit.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Asset-quality deterioration in Sichuan property and local-government credit, unmeasured because NPLs and capital ratios are not on the fact sheet; plus a de-rating from a P/E above its 5y maximum if growth slows.",
    "veto": null
  },
  "thesis": "A regional Chinese bank still earning a solid ROE at below-peer earnings multiples is in a working uptrend, but its ROE keeps falling and it has already re-rated above its own 5-year P/E range with asset quality unseen.",
  "rationale": "The trend is working and the multiples are low in absolute terms, but ROE keeps falling, the stock trades above its own 5-year P/E maximum, the fair value is unreliable and asset quality is invisible. Good but not compelling: AVOID, consistent with the October verdict.",
  "price_at_decision": 20.64,
  "price_date": "2026-11-13",
  "research_note": "research/SHA-601838/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROE falls below 11% (13.3% now), showing return dilution is accelerating.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 11}},
    {"text": "TTM net margin falls below 55% (63.1% now), showing credit costs or margin pressure are hitting profit.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 55}},
    {"text": "Shares outstanding grow more than 5% YoY (1.37% now), signalling a recapitalisation.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}},
    {"text": "A company filing reports a material rise in non-performing loans or a capital raise to meet regulatory minimums."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 23.2, "basis": "P/B rises to its 5y maximum of 0.9x [RA] as the uptrend and positive relative strength [HI] continue; below the unreliable mechanical fair value, which the DDM at 9.93 contradicts [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 21.5, "basis": "P/B holds at its 0.8x 5y median [RA] while book grows from a 13.3% ROE [RA], less the dividend; mechanical fair value set aside as flagged unreliable (methods 3.8x apart) [ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 17.2, "basis": "P/E de-rates from 6.6x back to its 5y median of 5.5x [RA] as ROE keeps falling and the extended trend (13.3% above the 200-day [ST]) reverses."}
  },
  "entry_price": 17.2,
  "entry_basis": "P/E back at its 5y median of 5.5x [RA] (the base fair value x 0.8 is above the price and flagged unreliable, so it cannot anchor an entry).",
  "replaces": null,
  "replacement_reason": null
}
```
