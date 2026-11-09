# Evaluation: Edenred SE (EPA:EDEN) — 2026-11-09
## Bear case
Regulation is cutting into the core product. Operating margin fell from 34.3% to 29.6% over the last 12 months, and ROCE from 28.6% to 27.2%. Both Direction change lines trace to meal-voucher fee rules in Italy and Brazil (Q3 2026 transcript) [Likely]. If more countries copy them, this becomes a permanent cap on take-rates, not a one-off reset [Guessing]. FCF of 38.2% of revenue against 23.6% a year earlier is probably flattered by client-fund float, so the FCFE fair value of 38.59 overstates the value that recurs [Likely]. Latin America is 30% of revenue [company-reported]. The overlay tilts small toward bear: a weaker real against the euro and Selic cuts reduce translation and float income (research/EPA-EDEN/2026-11-09-macro.md) [Likely]. Leverage rose from 1.13x to 1.65x [Certain]. The mechanical bear value of 21.15 sits below the price, and the Brazil decree details are unverified [Certain].

## Bull case
This is a high-return network at a trough multiple. ROIC is 18.5% and ROIC was flat over the last year (19.1% to 18.5%), while FCF margin rose and conversion is 210.2% of net income [Certain]. P/E of 11.9x and EV/EBITDA of 6.8x sit at 8% and 3% of their 5-year ranges, EV/EBITDA is below peers' 9.1x, and the FCF yield is 18.51% [Certain]. The reverse DCF implies -2.9% revenue growth, yet Q3 intrinsic growth was 6.6%, FY2026 EBITDA guidance was reaffirmed and 8%–12% growth is targeted for 2027–2028 (Q3 transcript) [Likely]. Q3 core earnings beat company-compiled consensus, so the margin drop looks like a step-down that is already guided, not lost share [Likely]. The dividend was raised 10% and shares fell 0.97% [Certain]. Mobility is growing at double digits [Likely]. The stock fell 14.9% over 3 months on unchanged guidance, and part of that is a risk-off premium [Guessing].

## Decision
```json
{
 "ticker": "EPA:EDEN",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "The 12-month fall in operating margin (34.3% to 29.6%) and ROCE comes from a one-time regulatory step-down in Italy and Brazil meal vouchers. FY2026 EBITDA guidance was reaffirmed, Q3 intrinsic growth was 6.6% and 8%-12% growth is targeted for 2027-2028 (Q3 2026 transcript, /quote/epa/EDEN/transcripts/654778-q3-2026-tu/). ROIC was flat over the year and FCF margin rose [RA-T, CF-T]. This is not lost share.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Further meal-voucher fee caps or interoperability rules (Brazil implementing rules, Italy, or a new country) would turn the reset into structural take-rate compression. The Brazil details are unverified.",
  "veto": null
 },
 "thesis": "A high-return benefits and mobility payments network is going through a regulation-driven margin reset that management has guided, yet trades near the bottom of its own 5-year multiple ranges at a price implying revenue decline that reaffirmed guidance and 6.6% Q3 intrinsic growth do not show.",
 "rationale": "The scorecard gives conviction 4. Returns are high and the balance sheet is sound, the multiples sit at their 5-year lows and the price discounts shrinkage. Regulation risk, float-flattered FCF and a bear value below the price keep it from 5. Same evidence as the 2026-11-08 BUY 4. Standard volatility-scaled core size, set by Python. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 24.6,
 "price_date": "2026-11-06",
 "research_note": "research/EPA-EDEN/2026-11-09.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 26% (29.6% now, 34.3% a year earlier): the guided reset is turning into structural take-rate compression from regulation.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 26
   }
  },
  {
   "text": "TTM ROIC falls below 14%, giving up most of the recovery from 10.0% in FY2023: the network moat is eroding.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "Net debt/EBITDA rises above 2.5x (1.65x TTM now): leverage is building, not seasonal working capital.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 2.5
   }
  },
  {
   "text": "Management cuts or withdraws FY2026 EBITDA guidance or the 2027-2028 growth target, Brazil's implementing rules impose full interoperability, or another country imposes a meal-voucher fee cap."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 45.0,
   "basis": "Guided 2027-2028 growth of 8%-12% resumes (Q3 2026 transcript) and P/E re-rates partway from 11.9x toward its 5y median of 32.3x [RA]. Set below the mechanical bull of 55.24 because the 38.2% FCF margin is float-flattered against 23.6% a year earlier [CF-T]."
  },
  "base": {
   "probability": 0.45,
   "target_price_12m": 33.0,
   "basis": "Operating margin holds near the TTM 29.6% [IS-T] with ROIC at 18.5% [RA], and EV/EBITDA recovers modestly from 6.8x, at 3% of its 5y range [RA]. Set below the mechanical base of 38.59 because that FCFE value extrapolates float-assisted FCF. Probability cut from an even split for the macro overlay's small toward-bear tilt (research/EPA-EDEN/2026-11-09-macro.md)."
  },
  "bear": {
   "probability": 0.3,
   "target_price_12m": 21.15,
   "basis": "Brazil and Italy rules deepen the margin fall from its 34.3% 2-year high [IS-T] while a weaker real and Selic cuts reduce float income: the mechanical bear fair value of 21.15 [fact sheet Fair value]. Probability raised for the overlay's small toward-bear tilt (research/EPA-EDEN/2026-11-09-macro.md)."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/EPA-EDEN/2026-11-09-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```
