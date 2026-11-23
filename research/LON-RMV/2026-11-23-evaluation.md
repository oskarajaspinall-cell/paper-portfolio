# Evaluation: Rightmove plc (LON:RMV) — 2026-11-23
## Bear case
The fall to 533.40 GBX (from the 612.40 high of 13 November) is mostly a fading activist bid premium: Sachem Head's reported push for a sale is unconfirmed, and without a bid the stock trades on a slowing UK housing market [Likely]. The 6 November update guided 2027 revenue growth only "similar to 2026" on a new-homes slump, and November asking prices fell [Likely]. Margins are drifting down: operating margin from 73.4% (FY2021) to 66.7% TTM, 2.3pp below its 2-year high; FCF margin 2.3pp below its 2-year high [Certain]. If the erosion is competition or agent pushback on ARPA rather than investment, the multiple is not cheap at all [Guessing]. The price is 15.0% above its 200-day average; if growth slows further the trend reverses and the stock de-rates [Likely]. Piotroski F of 4 and no computable fair value leave the valuation case resting on own-history multiples alone [Certain].
## Bull case
A dominant, asset-light UK portal: 100.0% gross margin, 66.7% operating margin, 54.3% FCF margin, FCF conversion 109.1%, net cash [Certain]. Rolling ROIC rose over the last year (467.2% to 497.4%), so the five-year ROIC decline has reversed; FCF margin is flat year on year [Certain]. The margin drift is gradual and coincides with AI/product investment and a cyclical new-homes trough, while H1 revenue still grew via ARPA and agency membership [Likely]. Valuation sits at the bottom of its own history: P/E 18.8x near its 5y min of 18.2x, EV/EBITDA 12.9x and P/FCF 16.2x below their 5y minimums, FCF yield 6.18% [Certain]. Buybacks cut shares 2.63% YoY [Certain]. An activist pressing for a sale adds optionality a pure de-rating thesis ignores [Guessing]. The trend is healthy: above both moving averages, with 6-month momentum of +23.5% [Certain].
## Decision
```json
{
  "ticker": "LON:RMV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin is down 1.5pp over the last 12 months while ROIC rose and FCF margin was flat [IS-T, RA-T, CF-T]; the 6 Nov update ties the slowdown to a homebuilding slump (https://www.reuters.com/world/uk/uks-rightmove-sees-2027-revenue-growth-similar-2026-due-homebuilding-slump-2026-11-06/) and H1 cites AI product investment with revenue still growing (https://stockanalysis.com/quote/lon/RMV/transcripts/574251-h1-2026/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A prolonged UK new-homes and housing slump, or agent pushback on ARPA, keeps margins drifting lower while the fading activist premium and an extended price above the 200-day average leave room for a de-rating.",
    "veto": null
  },
  "thesis": "The dominant, net-cash UK property portal trades at the bottom of its own multiple history, but a housing-cycle slowdown, gently eroding margins and a fading activist premium leave the edge short of compelling.",
  "rationale": "Exceptional, cash-generative economics at the low end of its own P/E and EV/EBITDA range, and the dip mostly unwinds an activist spike rather than breaking the business. But no fair value is computable, margins are drifting and 2027 growth is guided flat-to-slow; the scorecard lands below the buy bar, so AVOID.",
  "price_at_decision": 533.4,
  "price_date": "2026-11-20",
  "research_note": "research/LON-RMV/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below 62%, showing the margin drift is structural (competition or ARPA pushback), not investment.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 62}},
    {"text": "TTM ROIC falls below 300%, reversing the last year's rise.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 300}},
    {"text": "Shares outstanding change YoY turns positive by more than 2%, buybacks replaced by dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}},
    {"text": "FCF conversion (FCF/NI, cash flow page) falls below 90%, or the company reports a decline in agency advertiser numbers in a results release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 680, "basis": "A sale process (Sachem Head, Reuters headline in the fact sheet) or a housing recovery re-rates P/E toward its 5y median 23.1x [RA] on TTM earnings."},
    "base": {"probability": 0.5, "target_price_12m": 580, "basis": "Revenue growth guided similar to 2026 (Reuters headline, fact sheet) with buybacks; P/E moves from 18.8x toward the peer median 20.8x [RA, P]."},
    "bear": {"probability": 0.25, "target_price_12m": 460, "basis": "The activist premium fades and the new-homes slump extends margin drift; P/E slips below its 5y min 18.2x [RA] as the trend above the 200-day average (463.68) unwinds [ST, HI]."}
  },
  "entry_price": 480,
  "entry_basis": "No mechanical fair value (no GBP FX rate); anchored instead near the 200-day average 463.68 and the recent swing lows [HI], where P/E would sit below its 5y min of 18.2x [RA] and the discount would carry the case.",
  "replaces": null,
  "replacement_reason": null
}
```
