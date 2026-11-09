# Evaluation: Motiva Infraestrutura de Mobilidade (BVMF:MOTV3) — 2026-11-09
## Bear case
Cash generation is falling: TTM FCF margin is 21.8%, down from 44.4% a year earlier, and FCF/NI is 71.7% [Certain]. Operating margin fell from 37.7% to 33.5% in twelve months and ROIC sits 2.5pp below its 2-year high of 11.5% [Certain]. The likely drivers are heavy concession capex and portfolio changes, not lost traffic, but no primary source confirms how much is temporary [Guessing]. Leverage is high at 3.72x net debt/EBITDA with Altman Z of 1.40, and the Selic is 13.75%, so funding is expensive [Certain]. The 5.0x P/E is flattered by one-off gains (net margin 30.3% TTM) [Likely]. On EBITDA the stock is not cheap: 7.3x sits 81% up its 5y range and in line with peers at 7.2x [Certain]. The fair value is flagged unreliable (methods disagree 3.0x) [Certain]. Concessions are finite and regulated, and approval delays slow investment returns [Likely].
## Bull case
Toll concessions give quasi-monopoly, inflation-linked revenue, a durable if finite moat [Likely]. The airport sale simplified the portfolio and reduced leverage, and Q3 adjusted EBITDA grew per the call [Likely] (https://stockanalysis.com/quote/bvmf/MOTV3/transcripts/673430-q3-2026/). FCF yield is 14.49% even after the FCF margin drop, and the reverse DCF implies -9.9% year-1 revenue, too pessimistic for contractual toll indexation [Likely]. P/B of 1.6x is below its 5y median of 1.9x and ROE is 16.9% TTM [Certain]. The Selic is easing slowly, which would lower financing costs [Likely]. If capex normalises, FCF margin could recover toward its 5-year range of 27.0%-37.2% [Guessing].
## Decision
```json
{
  "ticker": "BVMF:MOTV3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin (44.4% to 21.8%) and operating margin (37.7% to 33.5%) fell with heavy concession capex and portfolio changes (airport sale, Minas_SP acquisition) per the Q3 2026 call (https://stockanalysis.com/quote/bvmf/MOTV3/transcripts/673430-q3-2026/); ROCE rose to 11.0% and the call reports adjusted EBITDA growth, so not lost traffic, though the temporary share is unconfirmed.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Leverage of 3.72x net debt/EBITDA with Altman Z 1.40 at a 13.75% Selic while FCF margin has halved: if capex stays high and approvals slip, cash may not cover debt service and growth.",
    "veto": null
  },
  "thesis": "A Brazilian toll-road concessionaire with inflation-linked revenue looks cheap on earnings, but at a mid-range EV/EBITDA in line with peers, with halved FCF margin and high leverage, the skew is not compelling.",
  "rationale": "Cheap P/E is inflated by one-off gains; on EBITDA the stock is fairly priced versus history and peers. Mediocre ROIC, halved FCF margin and high leverage at a high Selic, with the fair value flagged unreliable, give a low scorecard conviction. AVOID, no position.",
  "price_at_decision": 14.95,
  "price_date": "2026-11-06",
  "research_note": "research/BVMF-MOTV3/2026-11-09.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 4.5x (3.72x TTM), showing deleveraging from the airport sale has reversed.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "TTM operating margin falls below 30% (33.5% now), showing the margin decline is structural rather than mix.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 8% (9.0% now), showing new concessions earn below the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 15% (21.8% now), showing capex is outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 20.83, "basis": "Capex normalises and FCF margin recovers toward its 5-year range [CF,IS], returning the price to its 52-week high of 20.83 [HI]; well below the unreliable DCF fair value, which the sheet flags."},
    "base": {"probability": 0.45, "target_price_12m": 15.98, "basis": "EV/EBITDA holds near its 5y median and peers (6.9x / 7.2x [RA]), in line with the EV/EBITDA method's bull value of 15.98 [valuation]; the DCF base is set aside as unreliable (methods disagree 3.0x)."},
    "bear": {"probability": 0.3, "target_price_12m": 12.5, "basis": "FCF margin stays depressed and leverage of 3.72x [BS,IS] weighs at a 13.75% Selic (macro overlay), pushing the price toward the EV/EBITDA base of 13.29 and the 52-week low of 11.92 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 1: price is not the main obstacle; mediocre returns, a halved FCF margin and high leverage would need to improve before a lower price could justify a buy.",
  "replaces": null,
  "replacement_reason": null
}
```
