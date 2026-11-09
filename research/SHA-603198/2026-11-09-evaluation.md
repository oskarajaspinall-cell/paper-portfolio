# Evaluation: Anhui Yingjia Distillery (SHA:603198) — 2026-11-09
## Bear case
Returns are in a multi-year slide, not a blip: ROIC fell from 59.6% in FY2023 to 26.0% TTM and is still down 2.7pp in the last 12 months; ROCE 22.0% is 14.2pp below its 2-year high [RA-T] [Certain]. Operating margin sits 5.1pp below its 2-year high of 45.9% [IS-T] [Certain]. Nothing in the note explains the cause; weaker baijiu demand or pricing is plausible, and that would be structural for a regional, mid-tier brand facing national premium peers [Guessing]. The low P/E (17.5x, 7% of its 5y range) partly reflects lower earnings, not only a lower price, after a 21.0% three-month rally [Likely]. The mechanical base fair value of 36.38 CNY is below the 44.61 close, and the reverse DCF needs 23.5% year-1 revenue growth [Likely]. FCF conversion was 24.6% in FY2025; the TTM rebound is unexplained and may be working-capital timing [Guessing].
## Bull case
This is still a high-quality franchise at a trough multiple: gross margin 73.1% TTM is up from 66.7% in FY2021, which argues pricing power is intact [IS] [Certain]. Net cash (net debt/EBITDA -1.18x) and no dilution (shares +0.17%) mean the balance sheet can carry a down-cycle [BS,ST] [Certain]. P/E 17.5x and EV/EBITDA 11.1x sit near 5y lows and below the peer medians of 20.6x and 12.0x; P/FCF 24.3x is below its 5y minimum [RA] [Certain]. The EV/EBITDA method gives a base of 62.25 CNY, and the fair value is flagged unreliable, so the DCF-led blend may understate value [Likely]. FCF margin recovered to 23.2% TTM from 8.0% a year earlier [CF-T] [Certain]. If the return decline is a cyclical baijiu trough rather than lost share, a re-rate toward the 5y median multiple is available [Guessing].
## Decision
```json
{
  "ticker": "SHA:603198",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "ROIC down from 59.6% (FY2023) to 26.0% TTM and still falling over the last 12 months [RA-T]; operating margin 5.1pp below its 2-year high [IS-T]; no guided reset, investment programme or one-off was found to explain it (note section 2), so it cannot be called temporary on the evidence.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Continued baijiu demand/pricing weakness for a regional mid-tier brand keeps compressing returns and operating margin, so the low multiple is on still-falling earnings.",
    "veto": null
  },
  "thesis": "A net-cash, high-gross-margin baijiu maker trading near 5-year low multiples, but with returns still falling for unexplained reasons and the price above the mechanical base fair value.",
  "rationale": "Cheap on own-history multiples with a strong balance sheet, but ROIC and operating margin keep falling with no evidenced temporary cause, Q3 results unread, and the base fair value sits below the price. Good but not compelling: AVOID, with an entry price on the valuation file.",
  "price_at_decision": 44.61,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-603198/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (trailing) falls below 20%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Operating margin (trailing) falls below 38%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "FCF margin (trailing) falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Gross margin (trailing) falls below 68%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 62.25, "basis": "Return decline proves cyclical and EV/EBITDA re-rates toward its 5y median 15.9x [RA], in line with the EV/EBITDA method base of 62.25 CNY (fact sheet fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 44.61, "basis": "Earnings stabilise with gross margin near 73.1% [IS] and the P/E stays near 17.5x, below its 5y median [RA]; above the blended base fair value of 36.38 because the flagged-unreliable DCF leg looks too low for a net-cash business."},
    "bear": {"probability": 0.3, "target_price_12m": 36.38, "basis": "ROIC keeps falling from 26.0% [RA-T] as demand weakens and the price converges to the blended base fair value of 36.38 CNY (fact sheet fair value)."}
  },
  "entry_price": 29.1,
  "entry_basis": "valuation file: base 36.38 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
