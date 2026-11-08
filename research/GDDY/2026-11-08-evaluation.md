# Evaluation: GoDaddy Inc. (GDDY) — 2026-11-08
## Bear case
The market is pricing AI disintermediation: the reverse DCF implies -7.5% year-1 revenue growth, and the 10-Q added new risk factors on AI tools that let customers build sites on third-party platforms, which could cut demand or pricing for tools, hosting and domains [Certain]. **Direction change:** TTM ROIC fell from 30.8% to 28.7% over the last year, 8.6pp below its 2-year high of 37.3% [RA-T] [Certain]. The note attributes this to a higher tax provision and fewer stock-compensation tax benefits, since ROCE (+6.5pp) and operating margin (+3.8pp) rose over the same 12 months [Likely]; it does not break the thesis, but returns are no longer improving [Certain]. Growth is only about 6% in Q3, so the re-rating needs durability, not acceleration [Likely]. Altman Z of 1.44 reflects leverage; a securities class action is pending, merits unknown [Guessing]. The mechanical bear fair value of 102.86 sits below the price [Certain].

## Bull case
Fundamentals show no sign of the decline the price assumes: Q3 revenue and bookings each grew about 6% and 2026 revenue guidance sits at the high end of its range [Likely]. Operating margin rose to 26.1% TTM from 12.1% in FY2021 and FCF margin to 33.7%, both still rising over the last 12 months [IS-T, CF-T] [Certain]. The stock trades at 11.6x EV/EBITDA and 8.0x P/FCF, below its own 5-year minimums of 15.7x and 10.6x and far below peers [RA] [Certain]. A 12.57% FCF yield funds buybacks that cut the share count 7.62% in a year, while net debt/EBITDA fell from 4.35x to 1.88x [Certain]. Airo is starting to add to bookings, a sign AI can be a tool GoDaddy sells rather than only a threat [Likely]. Base fair value of 187.26 is well above the 114.38 close, and Piotroski F of 8 confirms quality [Certain].

## Decision
```json
{
  "ticker": "GDDY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A deleveraging, high-return domain and SMB-software franchise with a 33.7% FCF margin trades below its own 5-year minimum EV/EBITDA and P/FCF, where the price implies a revenue decline that growing bookings and high-end guidance do not show.",
  "rationale": "Thesis intact: margins and FCF still rising, guidance at the high end, buybacks accretive at a 12.57% FCF yield. The ROIC dip looks tax-driven, not operating. AI-substitution risk and a bear value below the price keep conviction at 4, not 5. The position sits near its conviction size, so HOLD rather than ADD.",
  "price_at_decision": 114.38,
  "price_date": "2026-11-06",
  "research_note": "research/GDDY/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, reversing most of the five-year improvement from 12.5% (FY2021) to 28.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20%, erasing the post-2023 step-up (FY2024 20.4%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 level of 27.6%, showing the cash gains were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Total bookings growth in the 10-Q/earnings release falls below 4% y/y for two consecutive quarters (AI substitution showing in demand), or net debt/EBITDA on the ratios page rises above 3.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 187.26, "basis": "Bookings growth holds and margins keep rising [IS-T], so the market drops the -7.5% implied decline and the price reaches the blended base fair value of 187.26 [fact sheet Fair value]; set below the mechanical bull of 203.79 because the new AI risk factors (note section 6) argue against a full return to the 5y median EV/EBITDA of 22.7x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 149.08, "basis": "Growth stays near the 6% of Q3 with FCF margin around 33.7% [CF-T]; the EV/Revenue method value of 149.08 [fact sheet Fair value] as a partial re-rating, below the DCF base of 206.35 because AI-disintermediation doubt keeps multiples under their 5y medians [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 94.91, "basis": "AI site-builders erode domain and hosting demand (10-Q risk factors, note section 6) and ROIC keeps sliding from its 37.3% 2-year high [RA-T]: the DCF bear value of 94.91 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Already conviction 4 at the current price; no lower price is needed to justify holding, and the default base fair value x 0.8 sits above the price.",
  "replaces": null,
  "replacement_reason": null
}
```
