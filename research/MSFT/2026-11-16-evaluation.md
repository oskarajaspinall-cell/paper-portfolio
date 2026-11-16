# Evaluation: Microsoft Corporation (MSFT) — 2026-11-16
## Bear case
Returns are falling fast. ROIC dropped from 30.1% to 25.3% in the last 12 months and FCF margin fell from 26.6% to 17.3%; both Direction change lines confirm this, and FCF/NI is now 42.0% [Certain]. AI datacentre capex drives it, and the 10-Q newly warns that AI pricing could commoditise against hyperscalers and frontier-model partners [Certain]. If payback disappoints, the decline is structural rather than an investment phase [Guessing]. On cash, the stock is expensive: P/FCF 64.9x is above its 5y max of 51.6x, the FCF yield is only 1.54%, and P/E sits at a premium to peers [Certain]. The points come from trend strength (price 18.6% above its 200-day average). If growth or capex returns slow, an extended price risks a de-rating toward the 5y P/E low of 20.7x [Likely], and the macro overlay flags rising real yields hitting exactly this multiple [Likely]. The 70-country Outlook outage adds concentration scrutiny [Guessing].

## Bull case
This is an elite franchise that is still working. Operating margin is at a 2-year high of 47.1% and rising, gross margin is flat at 67.7%, and ROCE has held at 26.0%, so pricing has not cracked; the fall in ROIC and FCF reflects a larger asset base built ahead of revenue [Likely]. The balance sheet is a non-issue: net debt/EBITDA is 0.34x and Altman Z is 8.28 [Certain]. On earnings, the stock is not expensive against its own history, with P/E at the 39% position and EV/EBITDA at 42% of their 5y ranges [Certain]. The uptrend is healthy: up 23.7% over 6 months, +22.1pp versus SPY, not overextended, and RSI is 49.6 [Certain]. The moat (installed base, enterprise distribution, Azure scale) is durable, and Copilot extends it [Likely]. The mechanical fair value is flagged unreliable because the DCF treats the capex surge as permanent [Likely].

## Decision
```json
{
  "ticker": "MSFT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and FCF margin fall because AI datacentre capex grows the asset base ahead of revenue (quarterly property and equipment additions 39,367 million USD [company-reported], https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), while operating margin is at its 2-year high of 47.1% [IS-T] and ROCE is broadly stable: heavy investment, not lost pricing.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "AI capex fails to earn an adequate return as AI pricing commoditises (new 10-Q risk language), keeping FCF conversion depressed and de-rating an extended price whose points come from trend strength.",
    "veto": null
  },
  "thesis": "A wide-moat software franchise with rising operating margin in a healthy uptrend, whose returns and cash conversion are being diluted by an AI capex build whose payback is not yet proven.",
  "rationale": "Scorecard conviction 3: elite quality, a strong balance sheet and a wide moat, but returns and cash conversion are falling and valuation earns only one trend-strength point, with no discount on cash multiples. Good but not compelling, so AVOID under the high-conviction-only owner rule; cash is acceptable.",
  "price_at_decision": 523.88,
  "price_date": "2026-11-13",
  "research_note": "research/MSFT/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20% (25.3% now), showing the AI build is diluting returns beyond an investment phase.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 12% (17.3% now), showing capex keeps outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 42% (47.1% now), showing AI price competition or cost inflation reaching profit.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 42}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) rises above 1.0x (0.34x now) as the capex build becomes debt-funded."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 620, "basis": "Capex payback becomes visible, FCF conversion recovers and P/E moves back toward its 5y median of 35.0x [RA] on earnings supported by a 47.1% operating margin [IS]."},
    "base": {"probability": 0.45, "target_price_12m": 540, "basis": "P/E holds near the current 27.4x [RA] while earnings grow with the rising operating margin [IS] and FCF stays depressed by capex [CF]; this sits far above the mechanical base fair value of 248.42 because that value is flagged unreliable, with the DCF treating the capex surge as permanent."},
    "bear": {"probability": 0.30, "target_price_12m": 400, "basis": "AI pricing commoditises (10-Q risk language, https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm) and P/E de-rates toward its 5y low of 20.7x [RA]; probability raised a small amount for the macro overlay's toward-bear tilt from rising real yields (research/MSFT/2026-11-16-macro.md)."}
  },
  "entry_price": 400,
  "entry_basis": "The mechanical base fair value is flagged unreliable, so it is not used: entry is set where P/E would sit near its 5y low of 20.7x [RA], which on the same evidence would earn real discount points.",
  "replaces": null,
  "replacement_reason": null
}
```
