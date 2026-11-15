# Evaluation: Kanzhun Limited (HKG:2076) — 2026-11-15
## Bear case
The ADR fell more than 20% on 2026-11-12 with no stated cause, and no company release explains it [Certain]. A move that large, eight sessions before Q3 results on Nov 25, 2026, may reflect information the market has and we do not: a PRC regulatory or sector event, or weak hiring demand [Guessing]. Reported profit flatters: net margin 52.8% exceeds operating margin 34.8%, and FCF conversion fell to 96.4% from 162.1% in FY2025 [Certain]. FCF margin sits 4.0pp below its 2-year high of 54.9%, a pullback from a peak rather than a structural break so far [Likely]. Shares rose 4.74% YoY despite the return plan [Certain]. The stock is 18.4% below its 200-day average and -40.3% over 12 months, so there is no trend support [Certain]. VIE structure and China-only revenue keep policy risk binary [Likely].
## Bull case
On the fact sheet's figures this is a net-cash (net debt/EBITDA -5.79x), 85.9%-gross-margin platform whose operating margin rose to 34.8% from 23.2% a year earlier and ROCE to 14.0% from 10.6% [Certain]. At 8.6x P/E, 5.0x EV/EBITDA and an 11.27% FCF yield it trades below the minimum of its own 5-year range on every multiple [Certain]. The reverse DCF needs only 8.9% year-1 revenue growth, below the 14.1% Q2 growth the company reported [Likely]. Base fair value 66.29 sits well above the 48.54 close [Certain]. The direct-chat two-sided network is a real moat [Likely]. If Q3 results confirm growth, the fall looks like an overreaction [Guessing].
## Decision
```json
{
  "ticker": "HKG:2076",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Operating margin, ROCE and FCF margin all rose over the last 1 and 3 years [IS-T, RA-T, CF-T]; FCF margin is 4.0pp below its 2-year high of 54.9% but 3.4pp above a year earlier, a pullback from a peak.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "An unexplained ADR fall of more than 20% on 2026-11-12, days before Q3 results on Nov 25, 2026, may signal a PRC regulatory action or a demand break that would invalidate the margin thesis; no company or official source confirms either.",
    "veto": {"code": "binary_event", "reason": "The cause of the 2026-11-12 collapse is unknown and Q3 results land on Nov 25, 2026; we cannot establish that the fall is an overreaction rather than new information, which an entry_hit buy requires."}
  },
  "thesis": "A net-cash Chinese recruitment platform with rising margins trades below its own 5-year minimum multiples, but an unexplained collapse just before Q3 results leaves the business case unverified.",
  "rationale": "Fundamentals and valuation are attractive, but a price fall alone is never a reason to buy: the cause of the 2026-11-12 drop is unknown and Q3 results are due Nov 25, 2026. Until results or a filing show the business intact, the evidence does not support high conviction. Cash is acceptable.",
  "price_at_decision": 48.54,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-2076/2026-11-15.md",
  "new_evidence": {"type": "price_move", "text": "Price fell from 68.55 at the 2026-11-08 HOLD 4 to 48.54 on 2026-11-13, an unexplained ADR collapse on 2026-11-12 that raises the key risk to high."},
  "triggers": [
    {"text": "TTM operating margin falls below 25% (34.8% now), showing AI-tool and marketing spend or weaker hiring demand is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 40% (50.9% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "Revenue on the income statement declines year on year for two consecutive quarters."},
    {"text": "A PRC regulatory action restricting BOSS Zhipin's operations, data or VIE structure is disclosed in a company release or filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 87.15, "basis": "Q3 results confirm growth and the stock retests its 52-week high of 87.15 [HI], still below the bull fair value of 119.68 and its 5y P/E minimum of 24.3x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 57.27, "basis": "P/FCF re-rates from 8.9x to the peer median 10.5x [RA, peers], below the base fair value 66.29 because the unexplained fall and lower FCF conversion of 96.4% [CF,IS] cap the re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 35.9, "basis": "The fall reflects a regulatory or demand break and the stock trades to the mechanical bear fair value of 35.90 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unexplained 2026-11-12 collapse and Q3 results on Nov 25, 2026 are. A lower price would not change the decision; the Q3 release or a company filing explaining the fall would.",
  "replaces": null,
  "replacement_reason": null
}
```
