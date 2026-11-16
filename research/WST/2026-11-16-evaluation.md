# Evaluation: West Pharmaceutical Services, Inc. (WST) — 2026-11-16
## Bear case
The price already discounts the recovery. P/E 46.8x sits at 75% of its 5-year range and EV/EBITDA is +109% over peers, with a 1.56% FCF yield [Certain]. The stock is 29.6% above its 200-day average after a 52.1% 12-month gain, so an extended price risks a sharp de-rating if HVP growth merely slows [Likely]. Even the P/E method's base of 390.89 sits below the 416.42 close, and the reverse DCF needs 48.5% year-1 growth [Certain]. The 5-year slide (ROIC 38.1% to 21.6%) is still falling on a 3-year view; the last-12-month rebound (ROIC 18.6% to 21.6%, operating margin 21.1% to 22.9%) is one year of evidence [Certain]. West Vantage is shrinking on a contract expiry, the May 2026 cyberattack leaves a litigation tail, and leadership is changing [Likely]. The macro overlay flags rising real yields as multiple risk for a long-duration stock [Likely].
## Bull case
West's components are written into drug makers' regulatory filings, so share is sticky and failure costs dwarf the part's price [Likely]. The direction change is genuine: post-COVID destocking has reversed, with ROIC, ROCE and operating margin all at their 2-year highs on a rolling basis [Certain], and Q3 organic growth of 11.9% from HVP and GLP-1/biologics demand drove a raised FY guide (transcript headline) [Likely]. The balance sheet is net cash (net debt/EBITDA -0.16x) and shares fell 1.48% YoY on buybacks [Certain]. Exiting the on-body delivery line sharpens capital allocation [Likely]. On its own history the multiple is not extreme: EV/EBITDA 30.0x sits at its 5-year median and P/FCF at 37% of its range [Certain]. A compounder of this quality rarely trades cheaply [Guessing].
## Decision
```json
{
  "ticker": "WST",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC, operating and FCF margin fell over 3 years on post-COVID destocking and mix; the last 12 months reversed (ROIC 18.6% to 21.6%, operating margin 21.1% to 22.9% [RA-T, IS-T]) with Q3 HVP-led organic growth and raised FY guidance (https://www.prnewswire.com/news-releases/west-reports-third-quarter-2026-results-302922802.html); balance sheet net cash.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A de-rating of an extended multiple (P/E 46.8x at 75% of its 5-year range, price 29.6% above its 200-day average) if HVP growth slows or real yields keep rising.",
    "veto": null
  },
  "thesis": "A net-cash, regulatory-locked injectable-components franchise whose returns are recovering, but whose price already discounts that recovery with little margin of safety.",
  "rationale": "High quality, net cash and a temporary, explained decline now reversing; valuation points come only from trend strength, while the value blend sits below the price and the de-rating risk is real. The scorecard gives conviction 3: good but not compelling, so AVOID; cash is acceptable. Entry where P/E nears its 5-year low.",
  "price_at_decision": 416.42,
  "price_date": "2026-11-13",
  "research_note": "research/WST/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 17%, giving up the last-12-month recovery from 18.6% and showing the destocking reversal has failed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 17}},
    {"text": "TTM operating margin falls below 20%, under the FY2024 low of 20.5%, showing HVP mix gains are not holding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 34%, under the FY2024 low of 34.5%, signalling pricing or mix erosion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 34}},
    {"text": "Net debt/EBITDA (balance sheet and income statement) rises above 1.5x from -0.16x TTM, e.g. from a debt-funded deal, or a 10-Q discloses material customer or litigation fallout from the May 2026 cyberattack."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 470, "basis": "HVP and GLP-1 demand keep the raised guidance on track and P/E holds toward its 5-year max of 52.5x [RA], above the P/E-method bull of 428.67 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 400, "basis": "Earnings grow on the recovering margins (operating margin 22.9% TTM [IS-T]) while P/E drifts back toward its 5-year median of 43.9x [RA], in line with the P/E-method base of 390.89; the DCF base of 75.91 is discounted as the fair value is flagged unreliable."},
    "bear": {"probability": 0.30, "target_price_12m": 270, "basis": "Growth slows and the extended multiple de-rates toward the P/E-method bear of 264.76 [fact sheet fair value]; probability raised a small step for the macro overlay's toward-bear tilt on rising real yields (research/WST/2026-11-16-macro.md)."}
  },
  "entry_price": 264.76,
  "entry_basis": "P/E-method bear fair value 264.76 (fact sheet), a P/E near its 5-year low of 29.7x [RA]; the mechanical base 180.90 x 0.8 is not used because the fair value is flagged unreliable (methods disagree 5.1x).",
  "replaces": null,
  "replacement_reason": null
}
```
