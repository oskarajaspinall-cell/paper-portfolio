# Evaluation: GoDaddy Inc. (GDDY) — 2026-11-16
## Bear case
AI site builders can disintermediate website and hosting demand; the new 10-Q risk factors name this explicitly [Certain], and fewer email seats already offset Q3 bookings [Certain]. Revenue and bookings grew only 6% in Q3 [Certain], so the multiple has de-rated for a reason: this is a low-growth SMB franchise, and Airo's competitive pricing tests could cost margin [Likely]. ROIC fell over the last 12 months (30.8% to 28.7%) and sits 8.6pp below its 2-year high of 37.3% [Certain]; if that reflects mix rather than buyback-shrunk capital, returns have peaked [Guessing]. The price is +23.3% above its 200-day average after a 24.9% six-month run [Certain]: a growth slowdown would de-rate it back toward the bear fair value of 99.77 [Likely]. Altman Z of 1.44 and buyback-depleted equity leave little book cushion [Likely]. Macro overlay is context only.
## Bull case
Cash economics keep improving: TTM operating margin 26.1% and FCF margin 33.7% are at their 2-year highs, and ROCE rose to 28.4% [Certain]. The ROIC dip is the only falling metric and coincides with rising margins and a 7.62% share-count reduction, consistent with a denominator effect, not eroding returns [Likely]. Leverage fell from 4.35x to 1.88x with an undrawn revolver [Certain]. At a 12.60% FCF yield and P/FCF 7.9x, below its 5-year minimum, the reverse DCF prices -6.7% year-1 revenue growth while Q3 beat and 2026 revenue was guided to the high end [Likely]. Airo passed an annualized bookings run rate the company says is now additive [Likely]. Buybacks of $1,311.0m in nine months [company-reported] compound per-share value [Certain]. The base fair value of 181.10 sits well above the price even after the rally [Certain].
## Decision
```json
{
  "ticker": "GDDY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only TTM ROIC is falling (30.8% to 28.7%, RA-T) while ROCE, operating margin and FCF margin all rose to 2-year highs (RA-T, IS-T, CF-T) and shares fell 7.62% (ST): a capital-base/mix effect, not lost economics.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "AI site builders disintermediate website/hosting demand (named in the 10-Q risk factors, https://www.sec.gov/Archives/edgar/data/1609711/000160971126000120/gddy-20260930.htm), slowing bookings and de-rating a price already well above its 200-day average.",
    "veto": null
  },
  "thesis": "A deleveraging, high-return domain and SMB-software franchise with a 33.7% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline that growing bookings and high-end guidance do not show.",
  "rationale": "Thesis intact: margins and FCF at 2-year highs, leverage down, cash multiples below their 5-year minimums. The position already sits near its conviction size, so hold rather than add; AI disintermediation is the risk to watch via bookings and margins.",
  "price_at_decision": 114.12,
  "price_date": "2026-11-13",
  "research_note": "research/GDDY/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year improvement from 12.5% (FY2021) to 28.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20%, erasing the post-2023 step-up (FY2024 20.4%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 level of 27.6%, showing the cash gains were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Total bookings growth in the 10-Q/earnings release falls below 4% y/y for two consecutive quarters (AI substitution showing in demand), or net debt/EBITDA on the ratios page rises above 3.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 196.97, "basis": "Bull fair value 196.97 (DCF-led, fact sheet Fair value): margins hold at 2-year highs and Airo adds to bookings, so the cash multiples re-rate toward their 5-year medians [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 149.08, "basis": "EV/Revenue base of 149.08 [Fair value]: a partial re-rating as mid-single-digit growth continues; set below the DCF-led blended base of 181.10 because AI disruption risk argues against a full return to history."},
    "bear": {"probability": 0.25, "target_price_12m": 99.77, "basis": "Bear fair value 99.77 [Fair value]: AI builders slow bookings and the price gives back its run above the 200-day average of 92.52 [ST,HI]."}
  },
  "entry_price": null,
  "entry_basis": "Already held at conviction 4; the base fair value less 20% sits above today's price, so there is no lower price to wait for. The obstacle to an ADD is sizing, not price.",
  "replaces": null,
  "replacement_reason": null
}
```
