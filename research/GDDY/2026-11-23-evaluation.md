# Evaluation: GoDaddy Inc. (GDDY) — 2026-11-23
## Bear case
The 10-Q's new risk factors name AI website builders, closed ecosystems and third-party platforms as threats to demand and pricing [Certain]; this is the case the market is pricing, with the reverse DCF implying -10.0% year-1 revenue growth [Certain]. Q3 bookings grew 5.7% [company-reported] and email seats fell at renewal, offset by price rises [Certain]: price-led growth is less durable than volume [Guessing]. The Direction change: TTM ROIC fell from 30.8% to 28.7% and sits 8.6pp below its 2-year high of 37.3% [Certain]; if that reflects capital spent on Airo and new gTLD applications rather than buyback arithmetic, returns may have peaked [Guessing]. The price is below its 50-day average and down 19.9% over 12 months [Certain], so trend support is weak; a bookings slowdown would push it toward the DCF bear of 94.02 [Likely]. Altman Z of 1.44 leaves little book cushion [Likely]. Macro is context only.
## Bull case
Cash economics are at their best: TTM operating margin 26.1% and FCF margin 33.7% are at 2-year highs and ROCE rose to 28.4% [Certain]. ROIC is the only falling metric while margins rise and shares fell 7.62% YoY, consistent with a capital-base effect, not eroding returns [Likely]. Net debt/EBITDA fell from 4.35x to 1.88x [Certain]. At a 14.45% FCF yield, P/FCF 6.9x and EV/EBITDA 10.3x sit below their 5-year minimums [Certain], while Q3 beat and 2026 revenue was guided to the high end [Likely]. Airo passed an annualized bookings run rate the company says is incrementally additive [Likely]. Piotroski F of 8 signals sound fundamentals [Certain]. The base fair value of 186.07 sits far above the 99.53 close, and even the blended bear of 102.26 is above it [Certain].
## Decision
```json
{
  "ticker": "GDDY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only TTM ROIC is falling (30.8% to 28.7%, RA-T) while ROCE, operating margin and FCF margin all rose to 2-year highs (RA-T, IS-T, CF-T) and shares fell 7.62% YoY (ST): a capital-base/mix effect, not lost economics.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "AI site builders disintermediate website/hosting/domain demand (new 10-Q risk factors, https://www.sec.gov/Archives/edgar/data/1609711/000160971126000120/gddy-20260930.htm), turning bookings growth negative.",
    "veto": null
  },
  "thesis": "A deleveraging, high-return domain and SMB-software franchise with a 33.7% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline that growing bookings and high-end guidance do not show.",
  "rationale": "Thesis intact: margins and FCF at 2-year highs, leverage down, cash multiples below their 5-year minimums. The position already sits at its conviction size and cash is near the floor, so hold rather than add; AI disintermediation is watched via bookings and margins.",
  "price_at_decision": 99.53,
  "price_date": "2026-11-20",
  "research_note": "research/GDDY/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year improvement from 12.5% (FY2021) to 28.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20%, erasing the post-2023 step-up (FY2024 20.4%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 level of 27.6%, showing the cash gains were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Total bookings growth in the 10-Q/earnings release turns negative for two consecutive quarters (AI substitution showing in demand), or net debt/EBITDA on the ratios page rises above 3.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 202.48, "basis": "Bull fair value 202.48 [Fair value]: margins hold at 2-year highs and Airo adds to bookings, so cash multiples re-rate toward their 5-year medians (P/FCF 14.9x) [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 149.08, "basis": "EV/Revenue base of 149.08 [Fair value]: a partial re-rating as mid-single-digit bookings growth continues; set below the DCF-led blended base of 186.07 because AI disruption risk argues against a full return to history."},
    "bear": {"probability": 0.25, "target_price_12m": 94.02, "basis": "DCF bear of 94.02 [Fair value]: AI builders slow bookings as the new 10-Q risk factors warn (note section 6), and the multiple stays below its 5-year minimum."}
  },
  "entry_price": null,
  "entry_basis": "Already held at conviction 4; the base fair value less 15% sits above today's price, so there is no lower price to wait for. The obstacle to an ADD is sizing and cash, not price.",
  "replaces": null,
  "replacement_reason": null
}
```
