# Evaluation: SouthState Bank Corporation (SSB) — 2026-11-21
## Bear case
An average-return bank, not a compounder: ROE 10.3% TTM, flat over five years and barely above the 10% quality line [Certain]. The fall to 99.18 follows a Q3 that missed consensus, with a higher provision, lower correspondent-banking fee income and lower interest income [company-reported] per the 10-Q (https://www.sec.gov/Archives/edgar/data/764038/000119312526439976/ssb-20260930.htm) [Certain]. The macro overlay tilts toward bear (small): the 10y at 5.04%, a 10y-2y curve flattened to 0.28pp and a high-yield spread up 0.77pp squeeze NIM and raise credit costs, which could push ROE toward 8% [Likely]. Shares rose 3.19% YoY, so per-share value is diluted [Certain]. The fair value is flagged unreliable (methods disagree 4.7x); the best method, P/B + ROE, gives a base of only 104.25 [Certain]. The price sits below its 200-day average, so there is no trend support [Certain]. FCF margin's five-year fall and twelve-month jump are bank cash-flow noise, not evidence either way [Likely].
## Bull case
The shares are cheap on every usable measure: P/E 10.6x sits below its 5y minimum of 11.6x and P/B 1.1x is near its 5y low and under peers' 1.3x [Certain]. The reverse DCF implies -6.1% revenue growth while management reports loans and deposits each growing 9% annualised, NIM held at 3.78% and guided at 3.75%-3.85% through 2027 with mid- to high-single-digit loan growth (Q3 transcript, https://stockanalysis.com/stocks/ssb/transcripts/715215-q3-2026/) [Likely]. Credit was described as stable, and the higher provision is tied to loan production, not losses [company-reported] [Likely]. The Sun Belt deposit franchise is a narrow but real moat [Likely]. Flat support staffing from 2027 offers operating leverage [Guessing]. The miss looks like an overreaction that leaves the business case intact, but it creates value, not a compelling one [Likely].
## Decision
```json
{
 "ticker": "SSB",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {"decline_cause": "temporary", "decline_evidence": "FCF margin for a bank swings with loan and working-capital flows; it rose from 15.3% to 56.6% over the last 12 months [CF-T], while ROE (10.3% TTM) and net margin (35.0%) are flat over five years [RA, IS]; the Q3 provision rise is tied to loan production per the 10-Q (https://www.sec.gov/Archives/edgar/data/764038/000119312526439976/ssb-20260930.htm).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A flatter curve and widening credit spreads (macro overlay) squeeze NIM and lift provisions, pushing ROE from 10.3% toward 8%.", "veto": null},
 "thesis": "A fairly run Sun Belt regional bank trading below its own 5-year P/E minimum and near its P/B low, but with only average ROE and adverse rate and credit macro.",
 "rationale": "The Q3 miss and the fall look like an overreaction rather than a broken thesis, but ROE near 10% is average, the fair value is unreliable, the best method shows modest upside and macro tilts bearish. Good but not compelling: AVOID; no position.",
 "price_at_decision": 99.18,
 "price_date": "2026-11-20",
 "research_note": "research/SSB/2026-11-21.md",
 "triggers": [
  {"text": "TTM ROE falls below 8%, showing NIM and credit pressure have broken the earnings base.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
  {"text": "TTM net margin falls below 28%, well under the flat five-year level near 31%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
  {"text": "Shares outstanding growth exceeds 6% YoY without acquisition-backed earnings growth.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 6}},
  {"text": "Provision for credit losses rises well above loan-growth needs for two consecutive quarters, per the 10-Q."}
 ],
 "scenarios": {
  "bull": {"probability": 0.25, "target_price_12m": 117, "basis": "NIM holds in the guided 3.75%-3.85% range and P/B re-rates from 1.1x to the peer median 1.3x [RA, P:peers], below the unreliable blended base of 131.53."},
  "base": {"probability": 0.45, "target_price_12m": 104, "basis": "ROE stays near 10.3% and the price tracks the P/B + ROE base of 104.25, the best method [valuation file]; the blended base is ignored as the methods disagree 4.7x."},
  "bear": {"probability": 0.3, "target_price_12m": 90, "basis": "Macro overlay tilt toward bear (small) raised this probability: spreads widen and the curve stays flat, provisions rise and P/B falls to its 5y low of 1.0x [RA]."}
 },
 "entry_price": 90,
 "entry_basis": "P/B back at its 5y low of 1.0x [RA]; the blended base fair value less 15% sits above the price and is unreliable, so it is not used."
}
```
