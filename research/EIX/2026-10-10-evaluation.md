# Evaluation: Edison International (EIX) — 2026-10-10
## Bear case
The cheapness is a liability discount, not a mispricing. Eaton-fire exposure is unresolved: the August ruling was only tentative [Certain], and California killed the liability-protection bill, leaving no new legislative shield [Certain]. The 5.7x P/E rests on a net-margin jump to 19.3% TTM from 7.3% FY2024 that the evidence cannot explain and is probably one-off [Guessing], so the P/E leg (103.87 base) inflates the 70.31 blended fair value; the cleaner dividend-discount base is 53.54, below the 55.30 close [Certain]. FCF is still negative (-2.0% TTM) and net debt/EBITDA is 4.88x [Certain], so the dividend relies on debt and regulatory recovery [Likely]. The 10y Treasury rose 68bp and HY spreads 45bp in 3 months (macro overlay), raising discount and refinancing costs [Certain]. Price trend is broken (-18.7% vs 200-day) and short interest rose 17.4% [Certain].
## Bull case
SCE is a legally protected T&D monopoly whose earnings track CPUC-approved rate base [Certain]. Fundamentals are improving: ROCE 7.1% TTM from 4.8% FY2021, net debt/EBITDA 4.88x from a 6.04x peak, FCF margin -2.0% from -36.9% [Certain]. EV/EBITDA 7.2x and EV/Sales 3.3x sit below their own 5-year minimums and about 40% below peers [Certain], so the market prices a severe Eaton outcome [Likely]. A final ruling rejecting automatic inverse-condemnation liability would remove the main overhang [Likely]; Q2 core EPS rose and 2026 guidance was reaffirmed [Certain]. The dividend was raised again to $0.8775 and declared in September [Certain]. Rerating to the 70.31 base fair value is +27% [Certain].
## Decision
```json
{
  "ticker": "EIX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A regulated California T&D monopoly with improving leverage and returns trades below its own 5-year minimum EV/EBITDA, but the discount reflects an unresolved Eaton-fire liability that the evidence cannot yet size.",
  "rationale": "Below 5-year EV/EBITDA lows, but the low P/E rests on probably one-off earnings, the dividend-discount base (53.54) is below the price, FCF is negative, and rising yields work against a levered utility (macro overlay, moderate bear tilt). Eaton liability is a binary legal event, not a valuation question. Good but not compelling: AVOID.",
  "price_at_decision": 55.30,
  "price_date": "2026-10-09",
  "research_note": "research/EIX/2026-10-10.md",
  "triggers": [
    {"text": "Net debt/EBITDA (statistics page) rises back above 6.0x, the FY2022-FY2024 level, showing wildfire costs outpacing rate-base recovery.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.0}},
    {"text": "TTM FCF margin falls below -5%, reversing the five-year improvement from -36.9% to -2.0%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": -5}},
    {"text": "A final (not tentative) court ruling or settlement in the Eaton-fire litigation, disclosed in an SEC 8-K/10-Q, rejects automatic inverse-condemnation liability or caps SCE's exposure within the AB 1054 wildfire-fund backstop (would raise conviction)."},
    {"text": "The quarterly dividend is cut or frozen versus the current $0.8775 declaration (would confirm cash-flow strain)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 70.31, "basis": "A final Eaton ruling against automatic liability (tentative ruling, Reuters 2026-08-11 as listed in the fact sheet) lets the price rerate to the blended base fair value of 70.31 [IS,BS,CF,RA,ST], still below the 6-month high of 81.62 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 55.00, "basis": "Litigation stays unresolved and value anchors on the dividend-discount base of 53.54 rather than the 70.31 blend, whose P/E leg uses a TTM net margin of 19.3% vs 7.3% FY2024 [IS] that is likely one-off; plus the $0.8775 quarterly dividend [OV]."},
    "bear": {"probability": 0.30, "target_price_12m": 38.22, "basis": "An adverse Eaton liability outcome with no legislative shield (wildfire bill killed, Barrons 2026-09-01 as listed in the fact sheet) drives the price to the bear fair value of 38.22 [IS,BS,CF,RA,ST]; probability raised a moderate step per the macro overlay's bear tilt (10y +68bp, HY spread +45bp in 3 months, research/EIX/2026-10-10-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the decision hinges on the unresolved Eaton-fire liability, a binary legal event; a lower price would only reflect a worse expected outcome. Re-research on a final ruling or settlement (trigger 3).",
  "replaces": null,
  "replacement_reason": null
}
```
