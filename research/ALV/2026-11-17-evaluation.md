# Evaluation: Autoliv, Inc. (ALV) — 2026-11-17
## Bear case
The fall to the entry level is not a fundamental surprise: Q3 adjusted EPS and revenue missed consensus and full-year margin guidance narrowed to the low end of its range [company-reported] [Certain]. Returns have rolled over from their peak: ROIC is 4.8pp below its 2-year high of 23.3% and ROCE fell from 26.0% to 24.8% over 12 months [Certain]. The cause is raw-material, logistics and tariff cost only mostly passed through [company-reported]; if tariffs persist the gap becomes a lasting margin cap rather than a reset [Guessing]. Guided organic growth is around 0% with weaker vehicle production [Likely]. ALV trades at a premium to every peer multiple (EV/EBITDA +31%), so an LVP downturn with beta 1.37 can de-rate it toward peers [Likely]. China exposure is unquantified [data unavailable]. Price sits below its 200-day average and the 12-month change is -2.1% [Certain].
## Bull case
A global safety oligopoly with certification, liability and launch track record as entry barriers [Likely]. ROIC 18.5% TTM and operating margin 10.2% remain well above FY2021-22 levels; the last-year dip is cost-driven, not share loss, and FCF margin rose from 5.4% to 6.6% [Certain]. Balance sheet is sound at net debt/EBITDA 1.21x [Certain]. Valuation is at the bottom of its own history: EV/EBITDA 6.7x at its 5y low, P/FCF 11.8x below its 5y minimum, FCF yield 8.48% [Certain]. The reverse DCF needs only 1.5% year-1 growth [Certain]. Capital returns are strong: shares down 4.12% YoY and a 15% dividend increase on 2026-11-10 [Certain]. The fall since the 127.25 swing high came with no adverse company news; the dividend raise and MCF acquisition are positive [Likely]. Base fair value 138.05 [Certain].
## Decision
```json
{
 "ticker": "ALV",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds no ROIC, operating or FCF margin falling over 1 or 3 years. ROCE eased from 26.0% to 24.8% on raw-material, logistics and tariff costs only mostly passed through [company-reported] (https://www.sec.gov/Archives/edgar/data/1034670/000119312526429588/alv-20260930.htm), while FCF margin rose from 5.4% to 6.6% [CF-T,IS-T].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "A global light-vehicle production downturn combined with tariff costs that cannot be fully passed through, pushing operating margin back toward its FY2022 level of 7.5% [IS] and de-rating the stock toward peer multiples.",
  "veto": null
 },
 "thesis": "A high-return safety oligopolist with a sound balance sheet and strong buybacks trades at the bottom of its own EV/EBITDA and P/FCF range, pricing growth of only 1.5% that flat-but-stable guidance clears.",
 "rationale": "The fall to the entry level came with no adverse company news (dividend raised, acquisition closed); the business case is intact and valuation sits at 5-year lows on a real discount, not trend. Scorecard conviction 4; Python sizes at the vol-scaled conviction-4 core size, with the funding queue handling any cash shortfall. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 117.37,
 "price_date": "2026-11-16",
 "research_note": "research/ALV/2026-11-17.md",
 "triggers": [
  {
   "text": "ROIC (TTM) falls below 15%",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "Operating margin (TTM) falls below 9%",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 9
   }
  },
  {
   "text": "FCF margin (TTM) falls below 4.5%",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 4.5
   }
  },
  {
   "text": "Net debt/EBITDA on the ratios page rises above 2.0x, or the company discloses loss of a major airbag/seatbelt programme or market share in a quarterly release."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 153.88,
   "basis": "Cost pass-through restores margins toward guidance of about 10.5% [company-reported] and multiples recover, matching the mechanical bull fair value 153.88 [IS,BS,CF,RA,ST,HI]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 138.05,
   "basis": "Flat organic sales with stable returns lets EV/EBITDA drift back from its 5y low of 6.7x toward the median 7.8x [RA], consistent with base fair value 138.05 [IS,BS,CF,RA,ST,HI]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 99.16,
   "basis": "A production downturn plus unrecovered tariff cost de-rates ALV toward peer multiples (EV/EBITDA peer median 5.1x [RA]), revisiting the 52-week low 99.16 [HI] rather than the DCF bear value of 46.40, which the note flags as unreliably wide."
  }
 },
 "new_evidence": {
  "type": "new_information",
  "text": "Since the 2026-11-08 AVOID 3 the board raised the quarterly dividend 15% (https://www.prnewswire.com/news-releases/autoliv-declares-increased-quarterly-dividend-302933998.html, 2026-11-09), signalling confidence in post-Q3 cash flow; the lower price also moved EV/EBITDA to its 5y low and P/FCF below its 5y minimum [RA], lifting the measured discount to the buy line."
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/ALV/2026-11-17-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": 117.34,
 "entry_basis": "Second opinion at conviction 3: valuation file: base 138.05 x 0.85."
}
```
