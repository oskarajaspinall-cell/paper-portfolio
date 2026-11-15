# Evaluation: Airbnb, Inc. (ABNB) — 2026-11-15
## Bear case
The price already discounts a lot: P/E 35.1x sits above its 5y maximum of 32.8x and EV/EBITDA is 66% above peers [Certain]. The reverse DCF implies 31.8% year-1 revenue growth against Q3 growth of 19% [company-reported], and the mechanical base fair value of 94.44 is far below the 186.78 close [Certain]. The trend points come from strength, not a discount. The stock is 25.3% above its 200-day average after a 53.5% year, so if growth slows the de-rating could be sharp [Likely]. Returns are slipping. Rolling ROCE fell from 30.0% to 25.7% and FCF margin from 38.4% to 36.0% (direction change) [Certain]. Management blames RNPL timing and a property purchase [company-reported], but a weaker cash profile could also persist [Guessing]. AI agents could bypass the fee model [Guessing]. Rising real yields and a weaker euro hit a rate-sensitive multiple and EMEA revenue at 47.2% [Likely].
## Bull case
This is an asset-light network with net cash and no dilution. Gross margin is 83.1%, ROE 35.8%, net debt/EBITDA -3.20x, and shares are down 3.98% YoY [Certain]. Growth is speeding up again. Q3 beat, guidance was raised, and the 11.7% reaction on 2.9x volume is still 84% held [Certain]. The ROCE and FCF dips look like timing: the FCF margin is still 36.0%, the operating margin is flat at 22.5% over 12 months, and management ties the cash dip to RNPL and a one-off property purchase [Likely]. On cash, the stock is not stretched. P/FCF of 21.9x is in line with peers and in the lower part of its own range, and the FCF yield is 4.57% [Certain]. The multiples that look high reflect depressed GAAP earnings relative to cash [Likely]. Unique supply is a moat hotel chains cannot copy [Likely].
## Decision
```json
{
  "ticker": "ABNB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Rolling ROCE and FCF margin are falling while operating margin is flat; the 10-Q attributes the FCF dip to reserve-now-pay-later timing and a New York property purchase, and Q3 growth accelerated with raised guidance (https://www.sec.gov/Archives/edgar/data/1559720/000155972026000032/abnb-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "An extended price (P/E above its 5y max, 25.3% over the 200-day average, reverse DCF needing 31.8% growth) de-rates if growth slows, with AI-agent disintermediation and rising real yields as catalysts.",
    "veto": null
  },
  "thesis": "A net-cash, high-margin travel marketplace with re-accelerating growth whose price already discounts growth well above what it is delivering.",
  "rationale": "Quality and momentum are real, but the price sits above its own 5y P/E range and far above the mechanical fair value, and rolling returns are slipping. The scorecard sets the conviction; below 4, so AVOID under the owner rule that only high conviction is bought.",
  "price_at_decision": 186.78,
  "price_date": "2026-11-13",
  "research_note": "research/ABNB/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 18%, breaking the post-2022 range (22.5% now).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM FCF margin falls below 30% (36.0% now), meaning the dip is economics, not RNPL timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 80% (83.1% now), signalling fee pressure from AI agents or direct booking.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "Quarterly revenue growth (income statement, YoY) falls below 8%, showing re-acceleration has reversed."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 214.62, "basis": "Growth keeps accelerating after the raised guidance [Reuters URL in note] and the price reaches the mechanical bull fair value of 214.62 [fact sheet Fair value]."},
    "base": {"probability": 0.42, "target_price_12m": 186.78, "basis": "Cash earnings grow while P/E drifts back from 35.1x toward its 5y range [RA], so the price roughly holds; probability trimmed slightly for the small toward-bear macro tilt (research/ABNB/2026-11-15-macro.md)."},
    "bear": {"probability": 0.33, "target_price_12m": 155.0, "basis": "Growth slows and P/FCF de-rates from 21.9x to its 5y median of 18.2x [RA] while real yields rise; probability raised for the small toward-bear macro tilt (research/ABNB/2026-11-15-macro.md); above the mechanical bear fair value because the DCF ignores the 36.0% FCF margin's durability."}
  },
  "entry_price": 149.1,
  "entry_basis": "P/FCF back near its 5y median of 18.2x [RA] at today's FCF, a level the 200-day average of 149.10 [ST] marks; the mechanical base 94.44 x 0.8 is not used because the DCF ignores the business's cash margins.",
  "replaces": null,
  "replacement_reason": null
}
```
