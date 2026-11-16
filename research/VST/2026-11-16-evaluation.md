# Evaluation: Vistra Corp. (VST) — 2026-11-16
## Bear case
Vistra is a commodity-linked power producer, and its returns swing with power prices: ROCE was 7.4% in FY2025 against 14.1% TTM, and FCF margin is -8.6pp over three years [Certain]. The TTM peak is not proven durable, and GAAP income includes an unrealised hedge gain [Certain]. The mechanical base fair value of 85.17 sits well below the 133.01 close, and the reverse DCF needs 14.3% year-1 revenue growth, so the price still assumes the data-centre demand story [Likely]. The Cogentrix deal adds debt and some dilution, so leverage rises from 2.77x [Likely]. Post-election talk of pausing Texas data-centre development threatens the large-load thesis directly [Guessing]. The trend is broken: price is -12.4% below its 200-day average and -26.7% over 12 months, with no trend support. Rising real yields add a small macro headwind for a beta-1.38 stock (macro overlay, tilt toward bear, small) [Likely].

## Bull case
Rolling returns are improving, not fading: ROCE rose to 14.1% from 7.2% a year earlier and FCF margin to 12.7% from 9.6% [Certain]. Net debt/EBITDA fell to 2.77x from 4.03x in FY2025 [Certain]. Q3 delivered record adjusted EBITDA and narrowed FY26 guidance, and long-term large-load contracts such as the Meta nuclear PPA [company-reported] lock in part of the demand [Certain]. Scarce dispatchable nuclear and gas capacity is hard to replicate while new build faces supply-chain constraints [Likely]. On multiples the stock is cheap: EV/EBITDA 8.2x sits at the 7% position of its 5y range and well below the 17.1x peer median, P/FCF 17.3x against peers at 58.2x, with a 5.78% FCF yield and shares down 1.81% YoY from buybacks [Certain]. The election sell-off to 110.89 may be an overreaction [Guessing].

## Decision
```json
{
  "ticker": "VST",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only the 3-year FCF margin is falling (-8.6pp from the FY2023 peak of 25.6%); over the last 12 months FCF margin rose to 12.7% from 9.6% and ROCE to 14.1% from 7.2% [RA-T, CF-T], so the 3-year fall reflects a cyclical/hedge-driven FY2023 peak, not a broken model.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Earnings are commodity and policy linked: a fall in power prices or a Texas/PJM curb on data-centre load growth (post-election headlines, unverified) would undo the TTM peak returns while the mechanical base fair value already sits far below the price.",
    "veto": null
  },
  "thesis": "A cash-generative independent power producer cheap on EV/EBITDA versus peers and its own history, but on peak-cycle returns, in a broken downtrend, with policy risk to its data-centre demand thesis.",
  "rationale": "The multiples are cheap and returns are improving, but those returns are cyclical highs, the mechanical fair value sits well below the price, the trend is broken and data-centre policy risk is unresolved. The scorecard does not reach the buy bar; good but not compelling is an AVOID.",
  "price_at_decision": 133.01,
  "price_date": "2026-11-13",
  "research_note": "research/VST/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROE falls below 20% (46.3% now), showing the TTM return peak has reverted toward FY2025 levels.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 7%, under the FY2025 level of 7.4%, showing cash generation has rolled over.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA (site definition) rises above 4.0x after the Cogentrix funding.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "Company releases show the Meta PPA terminated, or other large-load power sales cancelled or repriced materially lower."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 189.29, "basis": "Rolling ROCE holding at 14.1% and contracted large-load demand re-rate EV/EBITDA from 8.2x toward its 5y median 14.4x [RA], recovering the 52-week high [HI]; below the mechanical bull 364.43, which assumes growth we cannot verify."},
    "base": {"probability": 0.45, "target_price_12m": 133.01, "basis": "EV/EBITDA stays near 8.2x, well under the 17.1x peer median [RA], as narrowed FY26 guidance is delivered but policy noise caps the multiple; above the unreliable mechanical base 85.17 because the DCF and EV/EBITDA methods disagree widely (note section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 98.12, "basis": "Power prices or Texas data-centre policy pull returns back toward FY2025 ROCE of 7.4% [RA], taking the price to the EV/EBITDA method's base 98.12 [fact sheet fair value]; probability raised by the macro overlay's small tilt toward bear on rising real yields (research/VST/2026-11-16-macro.md)."}
  },
  "entry_price": 68.14,
  "entry_basis": "valuation file: base 85.17 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```
