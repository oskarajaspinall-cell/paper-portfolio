# Evaluation: First Solar, Inc. (FSLR) — 2026-11-23

## Bear case
The entry hit is a falling price, not new information. Earnings are cheap only on credit-boosted profit: P/FCF is 67.9x and the FCF yield 1.47% [Certain], and FCF conversion fell to 12.5% TTM from 77.7% in FY2025 [Certain]. The **Direction change** is real: FCF margin fell from 12.2% to 4.6% in twelve months as government grants receivable, inventories and trade receivables built up (10-Q) [Certain]. Underneath, Q3 sales fell 22.8% on module volume down 22.0% with customer contract terminations [company-reported] (https://www.sec.gov/Archives/edgar/data/1274494/000127449426000212/fslr-20260930.htm), and bookings were moderated by Section 232 uncertainty [Likely]. The moat is policy-made, so a tariff or tax-credit change can remove it at a stroke [Likely]. The trend is broken (34.7% below the 200-day, RSI 33.0), short interest is 11.04% and beta 1.71 [Certain]; the price already sits under the mechanical bear value, which says the market prices a bookings cliff [Likely].

## Bull case
On reported profit this is a net-cash (net debt/EBITDA -0.52x), high-return business: ROIC 19.8%, operating margin 37.7% at its 2-year high, Q3 gross margin 57.9% [company-reported] [Certain]. P/E 8.4x and EV/EBITDA 5.8x sit below their 5-year minimums and far below peers [Certain]. The FCF slump is working capital: the production-credit receivable and inventory, plus South Carolina capex, should convert to cash as credits are collected [Likely]. Section 232 is cited as likely to lift US module prices, and a $500M buyback signals management sees value [Likely]. Altman Z 6.61 means no balance-sheet stress while the policy picture clears [Certain].

## Decision
```json
{
  "ticker": "FSLR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell from 12.2% to 4.6% as nine-month operating cash flow turned negative on a build in government grants receivable, inventories and trade receivables plus South Carolina capex (10-Q https://www.sec.gov/Archives/edgar/data/1274494/000127449426000212/fslr-20260930.htm); ROIC and operating margin are rising.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Bookings and volume keep falling (Q3 sales -22.8%, contract terminations [company-reported]) while profit depends on US tariff and tax-credit policy that can change; earnings may not turn into cash.",
    "veto": null
  },
  "thesis": "A net-cash, high-return US module maker trades below its own 5-year minimum earnings multiples, but falling volumes, contract terminations and weak cash conversion make the policy-made earnings unproven.",
  "rationale": "Cheap on earnings and net cash, but the fall since the last review is price, not new evidence: volumes and bookings are shrinking, FCF is barely positive and the moat rests on policy. The scorecard stays below the buy bar; no position.",
  "price_at_decision": 137.59,
  "price_date": "2026-11-20",
  "research_note": "research/FSLR/2026-11-23.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, showing pricing power and credits no longer protect margins.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin turns negative, i.e. credit receivables are not converting to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "TTM ROIC falls below 15%, giving up the post-2022 return level.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Quarterly net sales fall below $1.0bn with further customer contract terminations disclosed in the 10-Q."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 240, "basis": "Section 232 lifts US module prices and the credit receivable converts to cash, so EV/EBITDA re-rates toward its 5y min of 10.1x [RA]; below the mechanical bull of 303.53 because volumes are shrinking."},
    "base": {"probability": 0.5, "target_price_12m": 160, "basis": "Earnings hold but bookings stay moderated, so the multiple recovers only part way toward the mechanical base of 173.44 [IS,RA]; trimmed for the Q3 volume fall [company-reported] in the note."},
    "bear": {"probability": 0.3, "target_price_12m": 100, "basis": "Further contract terminations and a policy change cut EBITDA while EV/EBITDA stays near today's 5.8x [RA]; below the mechanical bear of 148.49, which assumes TTM EBITDA holds."}
  },
  "entry_price": 127,
  "entry_basis": "Base x 0.85 (valuation file: base 173.44) is above today's price, so the anchor is the level where the value blend of base fair value and these scenarios' expected value sits 30%+ above the price, the scorecard's top valuation band, lifting the total to the buy threshold; the policy and bookings risk is unchanged, so a hit means re-research, not a buy.",
  "replaces": null,
  "replacement_reason": null
}
```
