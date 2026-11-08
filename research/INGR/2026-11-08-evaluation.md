# Evaluation: Ingredion Incorporated (INGR) — 2026-11-08
## Bear case
The five-year improvement is reversing now. Every rolling metric is falling: ROIC 12.0% vs 15.0% a year earlier, operating margin 12.0% vs 14.6%, FCF margin 4.8% vs 7.6% [RA-T, IS-T, CF-T] [Certain]. The causes are the Argo thermal event, raw-material and manufacturing costs, peso effects and a Colombia earthquake (10-Q) [Certain]. Q3 then missed and FY26 guidance was cut on tapioca inflation and soft US/Canada demand [Likely]. Whether Argo is a one-off or a lasting cost problem is unresolved [Guessing]. FCF conversion is 61.6% TTM [Certain]. The Tate & Lyle deal lifts consolidated debt to up to about $6.0 billion from $1.8 billion [company-reported]. It brings antitrust risk across four jurisdictions and a sold sterling put [Certain]. The overlay flags a weaker peso and real as an unsized LATAM drag [Likely]. The mechanical DCF bear is negative, so the downside isn't bounded by the model [Certain].
## Bull case
The stock is cheap on every lens. P/E is 10.4x against a 5y median of 13.0x and a peer median of 15.2x. EV/EBITDA of 6.0x and P/B of 1.3x sit below their 5y minimums [RA] [Certain]. The reverse DCF implies revenue shrinking 2.2% in year 1, while guidance calls for flat sales [Likely]. T&HS posted its 10th straight quarter of volume growth, and Tate & Lyle would lift specialty to more than half of revenue, with cost synergies cited by management [Likely]. Leverage is low today at 0.72x net debt/EBITDA. The share count fell 2.81% and the dividend was raised [Certain]. Beta is 0.62. If Argo recovers, margins could move back toward the FY2025 14.4% and the base fair value of 108.91 [Guessing].
## Decision
```json
{
  "ticker": "INGR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A specialty-tilting ingredients maker trades below its own 5-year minimum EV/EBITDA and P/B, but returns, margins and cash conversion are all falling over the last 12 months after a guidance cut, while a debt-funded Tate & Lyle deal adds integration and leverage risk.",
  "rationale": "Valuation is undemanding, but the last year reverses the fiscal-year improvement on every rolling metric. The Q3 miss and guidance cut leave Argo's recovery unproven, and the pending deal more than triples debt. Expected value sits only modestly above the price. That is good but not compelling: conviction 3, AVOID. Re-examine once margins visibly recover.",
  "price_at_decision": 91.72,
  "price_date": "2026-11-06",
  "research_note": "research/INGR/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2025 level of 14.4%, showing Argo and input-cost pressure were transitory.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 14.4}},
    {"text": "TTM ROIC recovers above 15.0%, the level of a year earlier, reversing the last-12-month decline.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15.0}},
    {"text": "TTM FCF margin recovers above 7.6%, the level of a year earlier, restoring cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 7.6}},
    {"text": "The 10-Q or earnings release confirms Argo back at full production with T&HS volume growth continuing, and the Tate & Lyle financing is set on terms that keep net debt/EBITDA below 3.0x pro forma."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 118.0, "basis": "Argo recovers and T&HS volume growth continues, lifting earnings back toward FY2025 margins; the target sits between the P/E-method base 114.94 and bull 122.03 [fact sheet Fair value], well below the mechanical bull of 256.79 because that DCF range is unreliably wide."},
    "base": {"probability": 0.45, "target_price_12m": 100.0, "basis": "Margins stabilise near TTM 12.0% [IS-T] and P/E recovers part way from 10.4x toward its 5y median of 13.0x [RA]; below the mechanical base of 108.91 because FY26 guidance was just cut and rolling returns are still falling [RA-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 78.0, "basis": "Argo and tapioca costs persist and deal leverage weighs, so P/E holds near its 5y minimum of 9.6x [RA] on lower earnings; below the P/E-method bear of 84.64 but far above the negative DCF bear, given 0.72x net debt/EBITDA today [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5y minimum EV/EBITDA and P/B, and the obstacles are falling returns and margins after the guidance cut, an unproven Argo recovery and the pending debt-funded Tate & Lyle deal, so a lower price on the same evidence would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
