# Evaluation: TMBThanachart Bank PCL (BKK:TTB) — 2026-11-16
## Bear case
Returns are sub-par: ROE is 9.1% TTM, still below the cost of equity a Thai bank carries, and a local report says Thai banks can no longer rely on strong interest income or high ROE [Likely]. The net-margin gains (23.8% to 41.5%) look mostly harvested [Guessing]. The price has run ahead: 2.72 THB sits above the mechanical bull fair value of 2.33 and the base of 2.24, P/B of 1.0x is above its own 5y max of 0.8x [Certain]. That makes the rally a re-rating, and an extended price risks de-rating if earnings growth (9M profit up only modestly per the transcript headline) stalls [Likely]. The FCF direction change (237.8% to 97.0% TTM) is bank deposit/working-capital noise, not a signal either way [Likely]. ING's sell-down to 11.6% leaves a placement overhang [Guessing]. Leverage and capital ratios are [data unavailable] [Certain].
## Bull case
The bank is working: ROE rose from 5.0% to 9.1% over five years and net margin nearly doubled [Certain]. Shares are down 5.19% YoY, so buybacks are real, and a higher interim dividend was announced (transcript headline) [Likely]. The price is above its 200-day average (+7.4%) with a +48.6% 12-month change, and P/E of 11.7x is still below the peer median of 12.2x [Certain]. Beta is 0.19, a genuine diversifier [Certain]. Fitch held its rating after the ING sale [Certain]. If ROE keeps climbing, P/E could return toward its 5y max of 13.6x [Guessing].
## Decision
```json
{
  "ticker": "BKK:TTB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The only falling metric is FCF margin (237.8% to 97.0% TTM), which for a bank reflects deposit and working-capital swings, not earnings power; ROE and net margin are rising (research/BKK-TTB/2026-11-16.md section 5).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "ROE stuck near 9% as Thai bank interest income fades, de-rating a price already above its own P/B history and all fair-value estimates.",
    "veto": null
  },
  "thesis": "An improving but sub-10% ROE Thai bank whose rally has taken P/B above its own 5-year range and the price above every mechanical fair value, leaving no margin of safety.",
  "rationale": "Quality is below the bar (ROE 9.1%) and the price exceeds even the bull fair value; trend strength alone cannot carry it. Buybacks and the uptrend are real but already priced. Scorecard conviction 3 means AVOID; no position.",
  "price_at_decision": 2.72,
  "price_date": "2026-11-13",
  "research_note": "research/BKK-TTB/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROE falls below 8%, reversing the multi-year improvement.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 38%, under the FY2023 level of 38.2%, showing the margin gains were not durable.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 38}},
    {"text": "Shares outstanding change YoY turns positive, meaning dilution replaces the buyback.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3.18, "basis": "ROE keeps rising and buybacks continue, so the price retests its 52-week high of 3.18 [HI] as P/E moves toward its 5y max of 13.6x [RA]; above the mechanical bull of 2.33 because the model is anchored to the old sub-0.8x P/B history."},
    "base": {"probability": 0.45, "target_price_12m": 2.6, "basis": "ROE holds near 9.1% [RA] and P/E stays around its current 11.7x [RA] with mild de-rating toward peers; above the mechanical base of 2.24 since buybacks support per-share value."},
    "bear": {"probability": 0.3, "target_price_12m": 2.05, "basis": "ROE stalls as Thai interest income fades (Bangkok Post, https://www.bangkokpost.com/business/general/3218110/thai-banks-struggling-to-make-money) and P/B reverts toward its own history, near the dividend-discount fair value of 2.05 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "The obstacle is quality, not price: ROE of 9.1% is below the level the scorecard needs for a 4, so a lower price alone would not make it a BUY; only a sustained ROE improvement would.",
  "replaces": null,
  "replacement_reason": null
}
```
