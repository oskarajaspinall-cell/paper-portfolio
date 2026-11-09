# Evaluation: Oil and Natural Gas Corporation Limited (NSE:ONGC) — 2026-11-09
## Bear case
ONGC is a price-taker with state-capped returns. TTM ROIC of 8.7% sits below the discount rate the fair value uses (4.84% risk-free plus a 2.0% India premium plus equity risk), and ROIC is down 5.0pp over three years [Certain]. The Direction change is real: operating margin is 9.5% TTM versus 11.2% at FY2026 and 10.3% a year earlier, and FCF margin slipped to 8.0% from 8.7% [Certain]. The driver is realised crude and gas prices plus HPCL refining losses, which management doesn't control [Likely]. The government sets part of the pricing and directs capital (HPCL, Venezuela operatorship talks), so the cash behind an 18.88% FCF yield may be spent at low returns rather than returned [Likely]. The low multiples (P/E 5.9x, P/B 0.7x) have persisted for five years; the stock is a value trap until capital allocation changes [Likely]. The base fair value of 704.94 is flagged unreliable [Certain].
## Bull case
On every measure the stock is priced for decline: EV/EBITDA of 3.8x and P/FCF of 5.3x are below their 5-year minimums, and the reverse DCF implies year-1 revenue shrinking 17.5% [Certain]. Yet Q2 FY27 revenue and profit rose strongly on better realisations with stable production (https://stockanalysis.com/quote/nse/ONGC/transcripts/724760-q2-26-27/) [Likely]. The balance sheet is improving: net debt/EBITDA fell to 1.23x, FCF conversion is 111.3% and the share count is flat [Certain]. On a rolling basis ROIC is flat (8.7% vs 8.5% a year earlier), so the 3-year fall reflects the FY2023-24 commodity peak rolling off rather than a broken asset base [Likely]. Peers trade at a P/E of 8.5x and P/B of 1.3x [Certain]; even a partial close of that gap, plus the cash yield, is a reasonable 12-month return [Guessing].
## Decision
```json
{
  "ticker": "NSE:ONGC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC (-5.0pp), operating margin (-3.3pp) and FCF margin (-2.1pp) [RA-T, IS-T, CF-T] track the commodity cycle: rolling ROIC is flat year on year (8.7% vs 8.5%), Q2 FY27 profit rose on better realisations with production stable (https://stockanalysis.com/quote/nse/ONGC/transcripts/724760-q2-26-27/), and net debt/EBITDA fell to 1.23x [BS,IS], so the balance sheet is intact through the trough.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Government-directed pricing and capital allocation (HPCL refining losses, overseas ventures such as the Venezuela operatorship talks) absorb the cash flow at sub-cost-of-capital returns, keeping the stock a permanent value trap.",
    "veto": null
  },
  "thesis": "A state-controlled Indian upstream producer with a sound balance sheet and an 18.88% FCF yield trades below its own 5-year minimum EV/EBITDA and P/FCF, but sub-par, commodity-driven returns and state-directed capital allocation limit how much of that cash reaches minority holders.",
  "rationale": "Cheap on every multiple with a strong balance sheet, but ROIC below the cost of equity, no durable moat and state control of pricing and capital mean the discount has persisted for five years. Good but not compelling: AVOID at the scorecard conviction of 2.",
  "price_at_decision": 234.80,
  "price_date": "2026-11-08",
  "research_note": "research/NSE-ONGC/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 7%, under the FY2025 five-year low of 7.7%, showing returns are deteriorating beyond the commodity cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "TTM FCF margin falls below 6%, back near the FY2023 low of 5.6%, showing cash generation is being absorbed by capex or state-directed investment.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.23x TTM now), above the FY2025 five-year high of 1.81x, signalling debt-funded overseas or downstream investment.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM operating margin falls below 8%, under the FY2023 five-year low of 8.7%, showing realisation or pricing pressure is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 338.00, "basis": "P/E re-rates to the peer median of 8.5x [P:NSE:OIL, P:NSE:RELIANCE, P:NSE:IOC, P:LON:SHEL] on TTM earnings as Q2 FY27 realisations hold; well below the mechanical bull fair value, which is flagged unreliable."},
    "base": {"probability": 0.50, "target_price_12m": 275.00, "basis": "P/E returns to its 5y median of 6.9x [RA] on TTM earnings with production stable per the Q2 FY27 transcript; below the unreliable mechanical base fair value of 704.94, which the persistent state-ownership discount does not support."},
    "bear": {"probability": 0.25, "target_price_12m": 179.00, "basis": "P/E falls to its 5y low of 4.5x [RA] as realisations slip and operating margin keeps falling from 11.2% toward the FY2023 level of 8.7% [IS]; this sits below the mechanical bear fair value of 356.79, which assumes no state-discount persistence."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is sub-cost-of-capital returns, no moat and state-directed capital allocation, not price; a lower price alone would not lift this evidence to conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
