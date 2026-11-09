# Evaluation: NICE Ltd. (TLV:NICE) — 2026-11-09
## Bear case
The fact sheet prints four **Direction change** lines, and they all point down. Over the last 12 months ROIC fell from 16.7% to 10.2%, operating margin from 21.9% to 17.2% and FCF margin from 26.5% to 17.6% [Certain]. Gross margin is also slipping (66.4% FY2025, 64.0% TTM) [Certain]. A restructuring charge does not explain a gross-margin fall. Mix and pricing pressure would, and that is the AI-disruption threat to seat-based contact-centre pricing [Likely]. Management itself pointed to slower AI ramps and softness in non-core streams. It cut 5% of the workforce [Likely]. The net-cash cushion has thinned from -1.40x to -0.34x net debt/EBITDA [Certain]. Low multiples on falling TTM earnings may be a value trap rather than a discount [Likely]. Revenue mix by country and the Israeli shekel cost base are unverified (macro overlay) [Guessing].
## Bull case
The price already assumes a bleak outcome: the reverse DCF implies -14.2% year-1 revenue growth [Certain]. Yet Q3 revenue grew 8% year on year, beating the guidance range, and FY26 EPS guidance was raised [Likely]. EV/EBITDA (7.3x), EV/Sales (1.8x) and P/B (1.6x) all sit below their 5-year minimums. EV/EBITDA is also far below the peer median of 19.1x [Certain]. Cash generation is still strong: a 9.16% FCF yield and FCF conversion of 146.8% [Certain]. Buybacks cut the share count by 5.35% [Certain]. The 5-year record (ROIC 10.3% to 18.7%) shows a franchise that can earn high returns [Certain]. The 2026 Gartner CCaaS Leader placement suggests its competitive position is intact [Likely]. The workforce cut points to restored margins rather than a broken model [Guessing]. The mechanical fair value is flagged unreliable, so the case rests on multiples, not on that number [Certain].
## Decision
```json
{
  "ticker": "TLV:NICE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Q3 revenue grew 8% and beat the guidance range, FY26 EPS guidance was raised and a 5% workforce cut signals restructuring costs in the TTM (Business Wire release 2026-11-04, https://www.businesswire.com/news/home/20261104629389/en/NiCE-Exceeds-Revenue-and-EPS-Guidance-Ranges-Reporting-8-Year-Over-Year-Revenue-Growth-in-Third-Quarter-2026/); the gross-margin slip (66.4% to 64.0% [IS]) is the part not yet explained.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "AI-native customer-service tools erode seat-based CCaaS pricing, turning the gross and operating margin dip into a permanent reset (slower AI ramps cited on the Q3 call, transcript on [OV]).",
    "veto": null
  },
  "thesis": "A still-growing, cash-generative contact-centre and AI customer-service software franchise trades below its own 5-year minimum EV/EBITDA and EV/Sales, but its rolling returns and margins are falling and the AI threat to seat pricing is unresolved.",
  "rationale": "The scorecard gives conviction 3, below the buy bar. The stock is cheap against its own history and its peers, but TTM ROIC is only 10.2% and falling, gross margin is slipping, and with the fair value unreliable the value-blend upside is modest. AI pressure on seat pricing is unresolved, so AVOID and no position.",
  "price_at_decision": 31520.0,
  "price_date": "2026-11-06",
  "research_note": "research/TLV-NICE/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15% (17.2% now), showing the margin fall is lost pricing rather than restructuring and investment.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 14% (17.6% now), showing cash generation is deteriorating structurally rather than resetting.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM gross margin falls below 62% (64.0% now), confirming AI-driven price/mix pressure on the seat-based model.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62}},
    {"text": "TTM ROIC falls below 8% (10.2% now), showing deployed capital is not earning its keep.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45740.0, "basis": "The beat-and-raise holds and margins recover toward the FY2025 22.2% operating margin [IS]; the stock regains its 52-week high of 45,740 [HI], still far below the mechanical bull because that fair value is flagged unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 37000.0, "basis": "Margins stabilise near TTM (17.2% operating [IS-T]) and EV/EBITDA lifts a little from 7.3x, below its 5y minimum of 7.7x [RA], toward the recent swing highs near 38,180 [HI]; well below the mechanical base of 82,023.60, which is flagged unreliable."},
    "bear": {"probability": 0.30, "target_price_12m": 24260.0, "basis": "Gross margin keeps falling from 64.0% [IS] as AI erodes seat pricing, and the price revisits the 52-week low of 24,260 [HI]; macro is context only (research/TLV-NICE/2026-11-09-macro.md)."}
  },
  "entry_price": 28600.0,
  "entry_basis": "P/FCF back at its 5y low of 9.9x [RA] (10.9x now); the base fair value less 20% is above the price because the fair value is flagged unreliable."
}
```
