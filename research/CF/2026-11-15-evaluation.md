# Evaluation: CF Industries Holdings (CF) — 2026-11-15
## Bear case
CF earns near its cycle top: TTM ROIC 25.4% is a 2-year high and operating margin 38.5% is near its 2-year high [Certain]. Over three years ROIC, ROCE, operating and FCF margin are all lower, and FCF margin sits 4.2pp below its 2-year high as capex for Blue Point One rises [Certain]. P/FCF 8.8x and P/B 3.2x are above their 5y maxima, so the cash-flow discount has gone [Certain]. The price is 6.2% above its 200-day average after a 47.6% 12-month gain; if nitrogen prices or the US gas spread turn, earnings and the multiple fall together and the extended price de-rates [Likely]. The mechanical base of 187.81 leans on a through-cycle DCF fed by above-mid-cycle earnings, so it likely overstates value [Likely]. CHS minority distributions mean common-holder cash is below headline FCF [Certain]. Yazoo City stays idle until 2027 [company-reported].
## Bull case
CF is the world's largest ammonia producer with a structural feedstock-cost advantage over European and Asian marginal producers [Likely]. Net debt/EBITDA is 0.21x, Piotroski 7, and shares fell 7.59% in a year on buybacks, with an 11.37% FCF yield [Certain]. P/E 8.8x and EV/EBITDA 4.8x sit below their 5y medians and well below peers [Certain]. The price implies -13.4% revenue growth in year 1, so a downcycle is already priced [Certain]. Last 12 months are improving: ROIC up from 18.8% to 25.4% and ROCE from 16.6% to 20.8% [Certain]; the 5-year ROCE fall is the 2022 spike rolling off, not lost share [Likely]. Management sees constructive nitrogen markets into 2027 and projects adding to mid-cycle EBITDA by 2030 (transcript headline) [Guessing]. Low beta of 0.54 [Certain].
## Decision
```json
{
  "ticker": "CF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC, ROCE, operating and FCF margin reflect the 2022 nitrogen price spike rolling off (ROCE 45.2% in FY2022) and higher Blue Point One capex, while the last 12 months are rising (ROIC 18.8% to 25.4%) with net debt/EBITDA at 0.21x [RA, RA-T, BS]: a cyclical normalisation with the balance sheet intact, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A nitrogen price downturn or a narrower US gas cost advantage cuts earnings from above-mid-cycle levels (TTM ROIC at a 2-year high), de-rating a price that sits above its 200-day average after a 47.6% 12-month gain.",
    "veto": null
  },
  "thesis": "A low-cost, under-levered ammonia leader buying back stock at an 11.37% FCF yield, but earning near cycle highs, so the low earnings multiples partly reflect peak profits.",
  "rationale": "Quality, balance sheet and buybacks are strong and the trend is healthy, but earnings sit near cycle highs, cash multiples are above their 5y maxima and the mechanical base relies on peak-fed DCF inputs. The scorecard sets the conviction; below 4, so no position.",
  "price_at_decision": 125.09,
  "price_date": "2026-11-13",
  "research_note": "research/CF/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, the FY2024 trough area, showing the cost advantage no longer earns high returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 28%, under the FY2024 five-year low of 29.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.21x TTM now), showing buybacks and Blue Point One capex are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin falls below 18% (26.2% now) while buybacks continue.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 187.81, "basis": "Nitrogen stays constructive into 2027 per the Q3 transcript headline [OV] and the price re-rates to the mechanical base fair value of 187.81 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 140.42, "basis": "Earnings normalise from a 2-year-high ROIC [RA-T] and EV/EBITDA moves toward its 5y median of 5.7x [RA], matching the EV/EBITDA leg of 140.42 rather than the peak-fed DCF."},
    "bear": {"probability": 0.25, "target_price_12m": 76.39, "basis": "A nitrogen downcycle, which the price's implied -13.4% year-1 revenue growth only partly reflects [fact sheet], cuts EBITDA and the multiple to the EV/EBITDA bear leg of 76.39."}
  },
  "entry_price": 110.0,
  "entry_basis": "Near the 2026-10-09 and 2026-11-04 swing low of 110.61 [HI] and the bear fair value of 111.56: the default base 187.81 x 0.8 is above the price and relies on peak-fed DCF inputs, so it would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
