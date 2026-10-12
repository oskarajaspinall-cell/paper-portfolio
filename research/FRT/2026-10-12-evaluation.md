# Evaluation: Federal Realty Investment Trust (FRT) — 2026-10-12
## Bear case
The discount is a sector re-rating driven by rates, not an FRT-specific mispricing. EV/EBITDA 16.7x and EV/Sales 10.5x are in line with the peer median (+3% / -2%) [Certain], so FRT is only cheap against its own lower-rate history. The macro overlay is primary and tilts moderately bearish: the 10y real yield is 2.87%, up 0.56pp in 3 months, and the 2y yield shows the market no longer prices cuts [Certain]. Leverage is still high at 5.79x net debt/EBITDA [Certain]. Growth is debt-funded: a $400m exchangeable note (dilution risk) plus the ~$508m Summit purchase, with TTM FCF yield at -4.00% [Certain]. Short interest is up 25.9% in a month [Certain]. The mechanical fair value rests on own-history multiples set at lower rates, so it probably overstates upside [Likely].
## Bull case
The operations are strong. Q2 2026 FFO/share rose 7% YoY to $1.88, occupancy was 96%, leasing hit a record and guidance was raised [Likely]. Net debt/EBITDA has fallen from 7.26x to 5.79x over five years and ROE has risen to 12.6% [Certain]. The 59-year dividend-growth record shows durable cash generation through cycles [Certain]. P/E 21.4x is below its 5y minimum of 21.6x and 15% below peers [Certain]. Base fair value is $147.71 (+39%), and even the bear case of $109.35 sits above the price [Certain]. The infill, high-income locations form a real moat [Likely]. If real yields ease, the multiple could re-rate quickly [Guessing].
## Decision
```json
{
  "ticker": "FRT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "High-quality, deleveraging grocery-anchored REIT growing FFO, but its discount to its own history is a rate-driven sector re-rating rather than a company-specific mispricing, with the macro overlay tilting bearish.",
  "rationale": "The business is good and cheap against its own history, but not against peers on EV/EBITDA. The primary macro chain (real yields up 0.56pp in 3 months, no cuts priced) argues for further multiple pressure. Leverage near 5.8x and debt-funded acquisitions add risk. Q3 results on Oct 30 are close. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 106.16,
  "price_date": "2026-10-09",
  "research_note": "research/FRT/2026-10-12.md",
  "triggers": [
    {"text": "Leverage reverses: debt/EBITDA rises above 7.0x, back above the FY2021 level and undoing the five-year deleveraging", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 7.0}},
    {"text": "ROE falls below 9%, undoing the FY2021-to-TTM improvement", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "Occupancy reported in a quarterly release falls below 93%, from 96% at Q2 2026"},
    {"text": "FFO guidance is cut, or the annual dividend increase is not declared"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 140.0, "basis": "Real yields ease toward 2.5% (macro overlay bull) and FFO keeps growing about 7%, so the multiple re-rates toward the lower part of its 5y range (P/E median 33.3x [RA]). The target stays below the $147.71 mechanical base because peers trade at only 16.2x EV/EBITDA [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 115.0, "basis": "P/E holds around its 5y minimum of 21.6x [RA] while FFO/share grows about 7% (Q2 2026 release). This is well below the mechanical base of $147.71 because that figure assumes own-history multiples set at lower rates, and EV/EBITDA is already at the peer median [RA, ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 90.0, "basis": "The macro overlay's moderate bear tilt (DFII10 above 3.25%, multiple compression) raises this probability: the multiple de-rates further, back to around the 52-week low of 90.03 [HI], below the mechanical bear of $109.35 because that figure does not capture a further rise in rates."}
  },
  "entry_price": 90.03,
  "entry_basis": "The 52-week low of 90.03 [HI]. The default (base 147.71 x 0.8 = 118.17) sits above today's price, but the base rests on own-history multiples that the 5.22% risk-free rate undermines. At about 90, P/E would be well below the peer median of 25.1x [RA], so FRT would be cheap against peers as well as its own history.",
  "replaces": null,
  "replacement_reason": null
}
```
