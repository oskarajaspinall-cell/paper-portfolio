# Evaluation: NVR, Inc. (NVR) — 2026-10-09

## Bear case
Returns are in a clear downtrend: ROIC fell from 86.5% (FY2022) to 36.7% TTM and operating margin from 21.7% to 15.7% [Certain]. Yet the stock still trades at 15.5x P/E, the 86th percentile of its 5y range and 27% above the peer median of 12.2x [Certain]. The mechanical base fair value of 5,141.87 sits 14.3% below the 6,002.55 close, and the price already implies 7.3% year-1 revenue growth in a housing market with no rate relief [Certain]. The macro overlay shows the 10y yield up 0.72pp in three months, driven by real yields, which keeps mortgage affordability under pressure [Certain]. Piotroski F of 4 and a 19.4% jump in short interest confirm deterioration is still underway [Certain]. Q3 results on Oct 20, 2026 could show further order and margin erosion [Likely].

## Bull case
NVR's land-light LPA model (94% of 180,100 lots controlled via option deposits) avoids the land write-downs that hurt peers in downturns, and returns remain exceptional at 36.7% ROIC and 31.5% ROE [Certain]. The balance sheet carries no net debt and Altman Z is 13.62 [Certain]. Buybacks shrank the share count 7.92% YoY with a fresh $750m authorisation, compounding per-share value through the cycle [Certain]. FCF conversion recovered to 91.7% and the FCF yield is 6.60% [Certain]. The stock is down 23.9% over 12 months, and a fall in yields would lift orders and margins together, pushing toward the 7,678.69 bull fair value [Guessing].

## Decision
```json
{
  "ticker": "NVR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "NVR is the highest-quality, land-light US homebuilder, but returns and margins are still falling while the stock trades near the top of its own 5-year multiple range and above peers, with real yields rising against it.",
  "rationale": "Quality is exceptional, but returns and margins are still falling and the stock sits at the 86th percentile of its own P/E range, 27% above peers and 14.3% above base fair value. The primary macro overlay leans toward the bear case. Good but not compelling at this price, so AVOID and wait for the entry price.",
  "price_at_decision": 6002.55,
  "price_date": "2026-10-08",
  "research_note": "research/NVR/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 20% (21.8% now), showing affordability pressure is eroding pricing beyond a cyclical dip.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 25% (36.7% now), showing the land-light return advantage is fading.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "Shares outstanding stop shrinking (YoY change above 0%, vs -7.92% now), showing cash generation can no longer fund buybacks.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "LPA deposits at risk rise materially as a share of lots controlled without a matching rise in closings (next 10-Q/10-K), signalling the capital-light sourcing model is deteriorating."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 7678.69, "basis": "Yields roll over and margins stabilise, so the price reaches the fact sheet's bull fair value of 7,678.69 [IS,BS,CF,RA]; the macro overlay's moderate bear tilt (research/NVR/2026-10-09-macro.md) cuts this probability."},
    "base": {"probability": 0.45, "target_price_12m": 5725.3, "basis": "The P/E re-rates from 15.5x to its 5y median of 14.8x [RA], giving the P/E-method base of 5,725.30; this is above the blended base of 5,141.87 because the buyback-driven per-share compounding (-7.92% shares [ST]) is better captured by P/E than by the DCF."},
    "bear": {"probability": 0.35, "target_price_12m": 3738.7, "basis": "Real yields keep rising (DFII10 +0.61pp over 3m, research/NVR/2026-10-09-macro.md) and margins compress further, so the price falls to the fact sheet's bear fair value of 3,738.70 [IS,BS,CF,RA]; the overlay's moderate bear tilt raises this probability."}
  },
  "entry_price": 4113.5,
  "entry_basis": "valuation file: base 5,141.87 x 0.8. At that price the same quality would come with a real margin of safety against the falling-returns and rate risk.",
  "replaces": null,
  "replacement_reason": null
}
```
