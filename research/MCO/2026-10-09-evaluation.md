# Evaluation: Moody's Corporation (MCO) — 2026-10-09
## Bear case
The price already assumes a lot. The fact sheet's DCF/FCFE fair value is 204.61 base and 273.78 bull, 55.4% and 40.3% below the 458.69 close. The reverse DCF needs 27.0% revenue growth in year 1, far above the 9% MA ARR growth management reported [Certain]. "Below its own 5-year range" means little when that range was set at 32.8x-44.5x P/E. MCO still trades above the peer median on every multiple: EV/EBITDA +24%, P/FCF +35% [Certain]. The macro overlay is moderately bear-tilted. The 10y real yield is up +0.61pp in 3 months, which raises MCO's own discount rate (beta 1.35), and HY spreads widened +0.39pp, a threat to issuance-driven MIS transaction revenue [Likely]. The stock has lagged SPY by -21.8pp over 12 months, and Q3 results on Oct 21 are a near-term binary event [Certain].

## Bull case
This is a regulated ratings duopoly (NRSRO barrier) with TTM ROIC of 32.0%, operating margin of 46.2% and FCF conversion of 106.2% [Certain]. Q2 2026 revenue grew 15% and adjusted EPS 31%, and issuance guidance was raised [Likely]. MA is 99% recurring with 95% retention, and first-time MIS mandates are up 45%, which builds future monitoring fees [Likely]. P/E 29.1x, EV/EBITDA 21.1x and P/FCF 26.8x are all below their own 5-year minimums [Certain]. The P/E method's fair value (base 584.78) sits above the price [Certain]. Net debt/EBITDA of 1.51x supports returning more than 130% of FCF, with shares down 2.07% YoY [Likely]. If real yields stabilise, the multiple could move back toward its own history [Guessing].

## Decision
```json
{
  "ticker": "MCO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class ratings duopoly whose quality is beyond doubt, but whose price still sits at a premium to peers and far above its own cash-flow fair value just as real yields lift its discount rate.",
  "rationale": "Quality earns conviction 3, not 4. Cash-flow valuation (DCF base 204.61, 27.0% implied growth) and peer premia (P/FCF +35%) leave no margin of safety. The macro overlay tilts toward the bear case, and Q3 results on Oct 21 are an unhedged binary. Good but not compelling, so AVOID and keep the cash.",
  "price_at_decision": 458.69,
  "price_date": "2026-10-08",
  "research_note": "research/MCO/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20% (vs 32.0% TTM, FY2022 trough 17.4%), signalling erosion of ratings/analytics returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 40% (vs 46.2% TTM), signalling pricing or cost pressure in MIS/MA.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 28% (vs 36.4% TTM), signalling weaker cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Debt/EBITDA rises above 2.5x (vs 1.51x TTM net), signalling debt-funded M&A or buybacks straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 540, "basis": "Real yields stabilise and P/E re-rates to its own 5y minimum of 32.8x [RA], in line with the P/E-method bear value of 516.34, plus earnings growth from 15% Q2 revenue growth (transcript), toward the 52-week high of 546.88 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 460, "basis": "Multiples stay at today's below-history levels (P/E 29.1x [RA]) while recurring growth (MA 9% ARR, transcript) offsets modest de-rating; this sits between the DCF bull (273.78) and P/E bear (516.34) because the two methods disagree sharply [IS,RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 370, "basis": "The macro overlay (research/MCO/2026-10-09-macro.md) tilts moderately toward the bear case and moves weight here: rising real yields and widening HY spreads slow issuance and push EV/EBITDA toward the 17.0x peer median from 21.1x [RA]; still above the DCF bull of 273.78 because DCF at a 5.28% risk-free rate understates a 32% ROIC franchise's terminal value."}
  },
  "entry_price": 340,
  "entry_basis": "This is a level where P/FCF falls to the 19.9x peer median [RA], down from 26.8x at 458.69, which removes the peer premium. The default (base 204.61 x 0.8) is not used: a DCF at a 5.28% risk-free rate with beta 1.35 is overly punitive against the P/E-method base of 584.78, and the owner's methods disagree.",
  "replaces": null,
  "replacement_reason": null
}
```
