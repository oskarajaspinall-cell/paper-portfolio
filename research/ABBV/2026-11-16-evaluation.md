# Evaluation: AbbVie Inc. (ABBV) — 2026-11-16
## Bear case
The price already discounts success. EV/EBITDA of 18.6x, EV/Sales of 9.0x and P/FCF of 27.6x all sit above their own 5y max, and EV/EBITDA is 34% above peers [RA] [Certain]. The reverse DCF needs 15.5% year-1 revenue growth, and the mechanical base value of 180.45 is -38.8% from the close; only the bull case (301.26) covers it [Certain]. After a +41.5% six-month run, 22.5% above the 200-day average, any slowdown in Skyrizi/Rinvoq would de-rate the stock hard [Likely]. Cash quality is slipping: FCF margin fell from 33.0% to 28.6% in a year and ROIC sits 7.6pp below its 2-year high of 27.4% [RA-T, CF-T] [Certain]. The cause is unverified [Guessing]. On policy, the Botox Medicare-negotiation appeal and the 340B pilot are open risks [Likely]. The CSO's interest in obesity deals points to more acquired-R&D spending [Guessing].
## Bull case
This is a strong franchise that is working. Gross margin of 73.7% and operating margin of 36.6% are at their 2-year highs, and operating margin is up 2.5pp in the last 12 months [IS-T] [Certain]. ROCE of 23.1% is rising [RA-T] [Certain]. Q3 revenue rose 10.5% operationally, and FY guidance went up on immunology and neuroscience growth (transcript, fact sheet news) [Likely]. Skyrizi and Rinvoq keep gaining labels (10-Q), which extends the post-Humira growth runway [Likely]. A voluntary agreement with the US government exempts the company from tariffs and future price mandates for three years (10-Q) [Certain]. Leverage is moderate at 2.21x net debt/EBITDA, with Piotroski F of 7 [ST] [Certain]. Defensive demand, beta 0.19, and relative strength of +39.9pp vs SPY over 6 months [HI] [Certain].
## Decision
```json
{
  "ticker": "ABBV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and FCF margin are falling while operating margin (36.6%, 2-year high) and ROCE (23.1%) are rising and FY guidance was raised on Q3 (transcript in fact sheet news); the gap points to acquired-pipeline spending and capital intensity rather than lost share, though the note could not verify the cause.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The price sits above its own 5y max on EV/EBITDA, EV/Sales and P/FCF and implies 15.5% year-1 revenue growth; any immunology slowdown or pricing-policy hit (Botox appeal, 340B) would de-rate an extended stock.",
    "veto": null
  },
  "thesis": "A high-margin immunology-led pharma franchise that is executing well, but whose price already discounts sustained double-digit growth at multiples above its own 5-year range.",
  "rationale": "The business is working: margins are at 2-year highs and guidance was raised. But the stock trades far above every own-history cash multiple and the mechanical base value, and FCF margin and ROIC are slipping. The scorecard gives low conviction, so this is an AVOID. Only a much lower price would change the verdict.",
  "price_at_decision": 295.03,
  "price_date": "2026-11-13",
  "research_note": "research/ABBV/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing acquired-pipeline spending is permanently diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 22%, extending the decline from 33.0% into a structural cash-conversion problem.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 22}},
    {"text": "TTM gross margin falls below 68%, under the five-year range, signalling price erosion from policy or competition.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "TTM operating margin falls below 30%, reversing the recent expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 330, "basis": "Skyrizi/Rinvoq growth keeps pace with the reverse-DCF 15.5% implied growth and multiples stay above their 5y max [RA]; this sits above the mechanical bull value of 301.26 because the model is blind to the label expansion in the 10-Q."},
    "base": {"probability": 0.5, "target_price_12m": 275, "basis": "Growth continues per the raised guidance but EV/EBITDA eases toward the peer median of 13.8x [RA]; the target is above the mechanical base of 180.45 because the DCF is built on the lower FCF margin of 28.6% [CF-T] and does not capture the franchise growth."},
    "bear": {"probability": 0.25, "target_price_12m": 190, "basis": "An immunology slowdown or Botox appeal loss (10-Q) de-rates the stock toward its 5y median EV/EBITDA of 12.0x [RA], near the 52-week low of 190.75 [HI] and between the mechanical bear and base values."}
  },
  "entry_price": 144.36,
  "entry_basis": "valuation file: base 180.45 x 0.8 [IS,BS,CF,RA,ST,HI]. Price is the obstacle; the franchise quality is intact.",
  "replaces": null,
  "replacement_reason": null
}
```
