# Evaluation: PTT Exploration and Production PCL (BKK:PTTEP) — 2026-11-16
## Bear case
The price of 144.50 THB sits on the 143.97 base fair value, built on TTM EBITDA from a period of much higher oil [Certain]. The macro overlay records Brent falling from 126.35 to 92.14 in a month, so forward EBITDA likely drops below TTM and the 43.1% operating margin drifts toward the 35-38% range [Likely]. The rolling-12-month recovery in operating margin (37.7% to 43.1%) and FCF margin (11.3% to 13.8%) is commodity price, not a better business; ROIC remains 2.0pp below its 2-year high of 14.8% [Likely]. Cash conversion is weak: FCF/NI 64.2% TTM, FCF margin 17.3pp under its 2-year high, as capex absorbs cash [Certain]. There is no pricing power; the moat is concession access only [Likely]. The Rolls-Royce bribery prosecution of a former executive adds governance noise [Guessing]. Price is below its 50-day and level with its 200-day average, so there is no trend support [Certain].

## Bull case
This is a low-cost producer: 77.4% gross margin, net debt/EBITDA 0.26x, an 8.26% FCF yield [Certain]. It trades at 2.6x EV/EBITDA against a 5.6x peer median and 7.8x P/E against 12.4x, so a lot of commodity pessimism is arguably priced in [Certain]. Returns recovered over the last year (ROIC 10.7% to 12.7%, ROCE to 16.6%), which shows the asset base still earns well through the cycle [Certain]. The falling 5-year FCF margin reflects heavy investment, not a lost market or a broken model, and the balance sheet can carry it [Likely]. Beta of -0.16 makes it a diversifier [Likely]. If Brent rebounds above about 100, the overlay's bull case moves value toward 163.73 [Guessing].

## Decision
```json
{
  "ticker": "BKK:PTTEP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC, operating margin and FCF margin follow the oil and gas price cycle and heavy capex (FCF/NI 64.2% TTM) with net debt/EBITDA only 0.26x [BS,IS]; all three rose over the last 12 months [RA-T, IS-T, CF-T]. No lost share or broken model is evident.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Brent fell from 126.35 to 92.14 in a month (macro overlay, FRED DCOILBRENTEU); forward EBITDA likely falls below the TTM base that the fair value and the 43.1% margin rest on.",
    "veto": null
  },
  "thesis": "A low-cost, lightly geared Thai upstream producer that is cheap against peers but priced at its base fair value on TTM earnings that the latest oil price fall is likely to erode.",
  "rationale": "No discount to the base fair value, no trend support, and the primary macro driver has turned down sharply, so forward earnings likely fall below the TTM base. Quality and balance sheet are sound, but the scorecard gives conviction 2: no position.",
  "price_at_decision": 144.50,
  "price_date": "2026-11-13",
  "research_note": "research/BKK-PTTEP/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 35% (statistics page)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "Net debt/EBITDA rises above 1.5x (statistics page)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF conversion (FCF/NI, cash flow page) stays below 50% for two further quarters"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 163.73, "basis": "Brent recovers above about 100 and margins hold near 43.1%, reaching the EV/EBITDA bull fair value of 163.73 (fact sheet fair value; macro overlay macro_bull)."},
    "base": {"probability": 0.45, "target_price_12m": 135.0, "basis": "EV/EBITDA near its 5y median 2.9x [RA] on lower forward EBITDA, set below the 143.97 base fair value because the overlay's moderate bear tilt (Brent 92.14 vs 126.35) says TTM EBITDA overstates the run-rate."},
    "bear": {"probability": 0.35, "target_price_12m": 106.83, "basis": "Brent stays near 90 or lower and the margin returns toward 35-38%, taking value to the 106.83 bear fair value; probability raised for the overlay's moderate bear tilt (macro overlay macro_bear)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
