# Evaluation: Moncler S.p.A. (BIT:MONC) — 2026-11-23

## Bear case
Growth has stalled: Q3 revenue was flat, Moncler DTC softened and weaker European tourism and warm weather hurt traffic [Likely]. Returns are drifting down. ROIC is 18.4% TTM, 2.6pp below its 2-year high of 21.0%. ROCE fell from 20.6% to 19.1% over the last 12 months, against its rising 5-year trend [Certain]. If this is luxury demand normalising rather than a cyclical air pocket, the low multiples are a value trap. Luxury stocks are also exposed to US wealth effects from an AI-linked selloff [Likely]. Without a regional revenue split, that sensitivity can't be sized [Certain]. The price has no trend support: it sits 20.5% below the 200-day average and is down 29.5% over 12 months, so a re-rating could take quarters [Certain]. The share count is up 0.28%, so buybacks give no per-share help [Certain]. Wholesale is guided flat for FY26 [Likely].

## Bull case
This is a high-margin brand with no sign of margin erosion. Gross margin is 78.2% and rising over five years, and operating margin is flat at 29.0% (+0.3pp over 12 months) [Certain]. The returns drift reflects softer sales on a fixed store cost base, not lost pricing power [Likely]. FCF margin rose from 21.5% to 25.0% over the last 12 months, and FCF conversion is 125.2% [Certain]. The balance sheet is near net cash (0.10x net debt/EBITDA, Altman Z 6.13) [Certain]. Every multiple sits below its own 5-year minimum: P/E 17.4x against a 21.6x minimum, EV/EBITDA 9.9x against 13.6x and P/FCF 13.9x against 17.4x. The stock is also below its peer median, with a 7.44% FCF yield [Certain]. The reverse DCF implies only 3.1% growth, and nine-month revenue still rose 6% at constant FX [Likely]. Stone Island is growing [Likely]. The mechanical base fair value of 46.59 sits above the price [Certain].

## Decision
```json
{
  "ticker": "BIT:MONC",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists nothing falling on its 1y/3y tests. The rolling ROIC and ROCE drift from their 2024 highs comes with a steady 78.2% gross margin, a flat 29.0% operating margin (+0.3pp) and a rising FCF margin (21.5% to 25.0%) [IS-T, CF-T]. It follows flat Q3 revenue on weaker European tourism (https://www.reuters.com/business/retail-consumer/moncler-reports-flat-q3-revenue-held-back-by-weaker-tourist-spending-europe-2026-10-21/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A prolonged luxury and tourism slowdown, or brand fatigue in Moncler DTC, turns flat revenue into declines and pushes the drifting returns lower.",
    "veto": null
  },
  "new_evidence": {"type": "method_change", "text": "The earlier AVOID at conviction 3 (2026-10-25) predates the conviction scorecard (2026-11-09). On today's fact sheet the scorecard gives conviction 4."},
  "thesis": "A near-net-cash luxury outerwear brand with steady 78% gross and 29% operating margins trades below its own 5-year minimum on every multiple, pricing only low growth through a tourism-led demand dip.",
  "rationale": "Scorecard 4: high and steady quality, near net cash, multiples below their own 5-year minimums and a base fair value above the price. The fall is explained by a tourism-led demand dip that has not broken margins. Python sizes it. Cash is at the floor, so it replaces JKHY, a conviction-3 holding.",
  "price_at_decision": 39.49,
  "price_date": "2026-11-20",
  "research_note": "research/BIT-MONC/2026-11-23.md",
  "triggers": [
    {"text": "TTM gross margin falls below 76%, under every fiscal year since FY2021, signalling lost brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 76}},
    {"text": "TTM operating margin falls below 26%, well under the flat 29.0% now, showing the demand slowdown is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 15%, showing the drift from the 21.0% 2-year high is structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA on the ratios page (site definition, net of cash) rises above 1.0x from 0.10x, signalling a debt-funded deal or cash strain."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 57.68, "basis": "Tourism and DTC traffic recover, and multiples move back toward their 5y minimums (EV/EBITDA 13.6x, P/E 21.6x [RA]), retaking the 6-month high of 57.68 [HI]. This sits below the mechanical bull fair value of 70.07, which assumes faster growth."},
    "base": {"probability": 0.5, "target_price_12m": 46.59, "basis": "Margins hold near 29% operating [IS] and revenue grows modestly, above the 3.1% the reverse DCF implies; the price moves to the mechanical base fair value of 46.59 [valuation file]."},
    "bear": {"probability": 0.25, "target_price_12m": 33.19, "basis": "Flat Q3 revenue turns into declines (https://www.reuters.com/business/retail-consumer/moncler-reports-flat-q3-revenue-held-back-by-weaker-tourist-spending-europe-2026-10-21/) and ROIC keeps drifting from 18.4% [RA-T]; the price falls to the mechanical bear fair value of 33.19."}
  },
  "replaces": "JKHY",
  "replacement_reason": "JKHY sits below the buy bar at conviction 3, and its price already implies growth above the company's framework. Moncler is a conviction-4 idea trading below its own 5-year minimum multiples, with base fair value above the price."
}
```
