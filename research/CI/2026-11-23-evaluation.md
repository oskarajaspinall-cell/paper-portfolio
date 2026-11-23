# Evaluation: The Cigna Group (CI) — 2026-11-23
## Bear case
Cigna is a thin-margin pass-through business: gross margin fell from 13.2% to 9.1% over five years and operating margin is only 3.8%, so a small regulatory hit to PBM economics hits profit hard [Certain]. Management itself flags 2027 rebate and GLP-1 headwinds and the ACA exit (https://stockanalysis.com/stocks/ci/transcripts/719833-q3-2026/) [Certain]. ROIC sits 2.1pp below its 2-year high of 14.7%, and FCF margin is down 2.8pp over three years, so cash generation per dollar of revenue is shrinking, not compounding [Certain]. The proposed CMS audit rule, followed by Medicare eligibility proposals, shows how quickly policy can reprice the whole group (https://www.tipranks.com/news/healthcare-stocks-unitedhealth-unh-humana-hum-cigna-ci-and-others-fall-on-proposed-crush-rule) [Likely]. A low multiple can stay low for years in a politically exposed industry; the price is below its 200-day average, with no trend support [Likely]. The bear fair value of 262.71 is barely below the price [Certain].

## Bull case
The price implies -3.9% revenue growth in year 1, while Q3 drove higher FY26 EPS guidance (https://stockanalysis.com/stocks/ci/transcripts/719833-q3-2026/) [Certain]. P/E 12.0x and EV/EBITDA 7.5x are below their own 5-year minimums and well under the peer median of 19.4x [Certain]. FCF yield is 11.58% with FCF at 138% of net income, funding buybacks (shares -2.66% YoY) and deleveraging to 1.87x net debt/EBITDA [Certain]. Rolling ROIC is still up 0.8pp on a year earlier, so the gap to the 2-year high is a mild dip, not a break [Certain]. Specialty is expected to rise to ~40% of earnings by 2030, which management links to 10%-14% long-term growth (https://stockanalysis.com/stocks/ci/transcripts/798786-ubs-global-healthcare-conference/) [Likely]. Medicare Advantage exposure looks smaller than UNH/HUM, so the sector sell-off may overstate CI's risk [Guessing]. Base fair value is 411.73 [Certain].

## Decision
```json
{
  "ticker": "CI",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "new_evidence": {"type": "new_information", "text": "Conviction is unchanged at 3; the 2026-11-16 TRIM to the conviction-3 size has been executed, and since then CMS proposed wider Medicare Advantage audits (2026-11-18, https://www.tipranks.com/news/healthcare-stocks-unitedhealth-unh-humana-hum-cigna-ci-and-others-fall-on-proposed-crush-rule), adding sector policy risk that argues against any add."},
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin is down 2.8pp over 3 years and ROIC sits 2.1pp below its 2-year high, but rolling ROIC is +0.8pp vs a year earlier, FCF conversion is 138% of net income, leverage fell to 1.87x and Q3 raised FY26 EPS guidance (https://stockanalysis.com/stocks/ci/transcripts/719833-q3-2026/); the margin drift reflects pass-through drug-spend mix, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "PBM rebate reform and the flagged 2027 rebate and GLP-1 headwinds compress Evernorth profit on a 3.8% operating margin, with sector policy risk (CMS audit rule) keeping the multiple depressed.",
    "veto": null
  },
  "thesis": "A deleveraging PBM and employer-health franchise with ROIC of 12.6% and an 11.58% FCF yield trades below its own 5-year minimum P/E and EV/EBITDA, where the price implies a revenue decline that raised 2026 guidance does not show.",
  "rationale": "Same evidence as the last review plus fresh sector policy risk: cheap on every own-history multiple with strong cash conversion, but thin margins, 2027 rebate and GLP-1 headwinds and the CMS audit proposal keep it below the buy bar. Held at the conviction-3 size it was already trimmed to.",
  "price_at_decision": 270.90,
  "price_date": "2026-11-20",
  "research_note": "research/CI/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, giving up most of the five-year improvement from 8.8% to 12.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 3.5%, under the FY2025 five-year low of 3.7%, showing rebate reform or medical cost pressure is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3.5}},
    {"text": "TTM FCF margin falls below 2.0%, well under the current 2.9%, signalling cash generation and buyback capacity are deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.0}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.87x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 342.42, "basis": "P/E re-rates toward its own history as FY26 guidance is delivered; target is the P/E method's base fair value of 342.42 [IS,RA], well below the DCF bull, which the note calls highly sensitive."},
    "base": {"probability": 0.5, "target_price_12m": 300.0, "basis": "Policy overhang lingers and 2027 headwinds cap the re-rating, so P/E stays below its 5y median 15.1x [RA] and the stock sits between the P/E bear of 279.67 and base of 342.42 rather than near the 411.73 blended base, which leans on the DCF."},
    "bear": {"probability": 0.3, "target_price_12m": 240.0, "basis": "PBM rebate reform or the proposed CMS audit rule (https://www.tipranks.com/news/healthcare-stocks-unitedhealth-unh-humana-hum-cigna-ci-and-others-fall-on-proposed-crush-rule) cuts profit on a 3.8% operating margin [IS], taking the price below the mechanical bear of 262.71 since the 5y P/E minimum of 12.3x [RA] gives no floor under lower earnings."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: even at maximum valuation points the scorecard total cannot reach the ADD threshold, because quality level, balance sheet, moat and policy risk hold it back, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
