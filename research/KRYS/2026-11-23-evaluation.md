# Evaluation: Krystal Biotech, Inc. (KRYS) — 2026-11-23
## Bear case
KRYS is a single-product company. US VYJUVEK nine-month revenue was $274,445k vs $277,145k a year earlier [company-reported] (https://www.sec.gov/Archives/edgar/data/1711279/000171127926000071/krys-20260930.htm), so the core market has plateaued and growth now leans on Europe and Japan [Certain]. Q3 brought pipeline delays into 2027 and lowered guidance; the stock fell sharply on 2026-11-02 [Likely]. The DOJ subpoenas on the sponsored genetic testing program carry a loss that is not estimable [Certain]. At 308.89 the price sits above the mechanical base fair value of 287.31, at P/E 43.5x and EV/Sales 17.0x, far above peers [Certain]; it is below both its 50-day and 200-day averages, so there is no trend support either [Certain]. ROIC fell from 40.4% to 37.5% over 12 months, 3.9pp below its 2-year high [Certain]. Short interest is 12.87% and rising [Certain].
## Bull case
The economics are exceptional: gross margin 94.3%, operating margin 48.4% and FCF margin 66.0% TTM, all with operating and FCF margins at their 2-year highs [Certain]. The ROIC dip is a denominator effect from a growing cash pile and manufacturing build-out while profitability rises, not a weakening franchise [Likely]. VYJUVEK is the first and only corrective therapy for DEB, with in-house HSV-1 vector manufacturing and regulatory exclusivity [Likely]. Net cash (net debt/EBITDA -3.94x), more than $1.2B in cash and investments and a $400M buyback limit downside [Certain]. P/E is near the low of its 5-year range and EV/EBITDA below its 5-year minimum [Certain]. Hailey-Hailey data in December 2026 and the mid-2027 CF readout offer pipeline optionality the EV/Revenue fair value ignores [Guessing].
## Decision
```json
{
  "ticker": "KRYS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only ROIC is falling (40.4% -> 37.5% TTM) while operating margin (+6.0pp) and FCF margin (+21.6pp) rose to 2-year highs [IS-T, CF-T]; cash is funding two manufacturing sites and pipeline R&D (research/KRYS/2026-11-23.md), so the capital base grew faster than returns.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Single-product dependence: US VYJUVEK sales are flat [company-reported] while pipeline readouts slipped into 2027, so the premium multiple rests on the ex-US ramp; the DOJ subpoena adds an unquantified legal overhang.",
    "veto": null
  },
  "thesis": "A highly profitable, net-cash single-product gene-therapy franchise whose price already exceeds its mechanical fair value while US sales are flat and the pipeline has slipped.",
  "rationale": "Quality and balance sheet are excellent, but the price is above base fair value and below its 200-day average, so neither a discount nor trend strength supports it; flat US sales, pipeline delays and an open DOJ inquiry make it good but not compelling. No position.",
  "price_at_decision": 308.89,
  "price_date": "2026-11-20",
  "research_note": "research/KRYS/2026-11-23.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 25%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "FCF margin (TTM) falls below 40%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "Gross margin (TTM) falls below 90%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 90}},
    {"text": "Company-reported US VYJUVEK revenue declines year on year by more than 10% in two consecutive quarters (10-Q) while Europe plus Japan fail to offset it"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 382.54, "basis": "Positive Hailey-Hailey data (December 2026, Jefferies transcript [OV]) and the ex-US ramp re-rate the stock back to its 52-week high of 382.54 [HI]; the mechanical bull of 920.39 is excluded as an EV/Sales extreme near its 5y max 57.4x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 287.31, "basis": "EV/Revenue base fair value of 287.31 (fact sheet Fair value) as flat US sales offset ex-US growth and pipeline news slips into 2027 (research/KRYS/2026-11-23.md)."},
    "bear": {"probability": 0.25, "target_price_12m": 240.74, "basis": "EV/Revenue bear fair value of 240.74 (fact sheet Fair value) if US VYJUVEK declines or the DOJ subpoena inquiry escalates (10-Q, https://www.sec.gov/Archives/edgar/data/1711279/000171127926000071/krys-20260930.htm)."}
  },
  "entry_price": 244.21,
  "entry_basis": "valuation file: base 287.31 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```
