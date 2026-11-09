# Evaluation: Avanza Bank Holding AB (publ) (STO:AZA) — 2026-11-09
## Bear case
The price already assumes excellence: P/E 20.0x is +41% above the Swedish bank peer median 14.2x and P/B 6.7x against 1.9x [Certain]. The reverse DCF needs 12.7% year-1 revenue growth [Certain], and every mechanical method (P/B+ROE 135.11, DDM 166.69, FCFE 290.20) sits below the 368.50 close [Certain]. Returns are slowly fading: ROIC 34.2% TTM is 4.6pp below its 2-year high of 38.8% and down 1.7pp in a year [Certain]. The driver is lower market volatility hitting trading income and moderated mortgage growth in Q3 [Likely]. That is cyclical, but it shows earnings swing with retail activity. A VIX spike (macro overlay, context only) could help or hurt. FCF margin falling from 509.0% to 200.0% reflects deposit flows, not earnings, so it is noise rather than evidence [Likely]. Balance-sheet leverage data are [data unavailable] and Piotroski F is 4 [Certain].
## Bull case
Avanza earns ROE 36.9% TTM with a 62.8% operating margin, roughly triple a typical bank's returns [Certain]. The low-cost platform, brand and sticky savings balances look like a real moat [Likely]. Customer growth and record fund inflows continued in Q3, with operating profit of SEK 920 million, the second-highest quarter ever [Likely] (https://stockanalysis.com/quote/sto/AZA/transcripts/530433-q3-2026/). The operating margin is up 1.5pp over 3 years [Certain], and returns have held at about 35-37% since FY2022 [Certain]. FY2021's 52.0% ROE was a boom year, so the 5-year "falling" label mostly measures a normalisation from that peak [Likely]. P/E sits in the bottom quarter of its 5y range (22% position) [Certain]. Dilution is minimal at 0.32% YoY [Certain], and beta is 0.65 [Certain]. The mechanical fair value is flagged unreliable, since its methods disagree 2.1x [Certain].
## Decision
```json
{
  "ticker": "STO:AZA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC fade from the FY2021 retail-trading boom and lower Q3 2026 trading income on weaker volatility, while customer growth and fund inflows stayed strong and operating margin is up over 3 years (transcript https://stockanalysis.com/quote/sto/AZA/transcripts/530433-q3-2026/; RA-T, IS-T); FCF margin swings are deposit flows, not earnings.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Retail trading activity and Swedish rates fall together, compressing commissions and net interest income while the stock trades at a large premium to peers.", "veto": null},
  "thesis": "A high-return Swedish savings platform with a real franchise, but priced for continued excellence with no valuation support beyond its own P/E history.",
  "rationale": "Quality is top-tier and the return fade looks cyclical, but the price sits far above every mechanical method and at a large premium to peers, so the evidence gives no margin of safety. Good but not compelling is an AVOID (owner rule: high conviction only).",
  "price_at_decision": 368.50,
  "price_date": "2026-11-06",
  "research_note": "research/STO-AZA/2026-11-09.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 30%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 30}},
    {"text": "Operating margin (TTM) falls below 55%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 55}},
    {"text": "ROIC (TTM) falls below 28%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}},
    {"text": "Shares outstanding growth exceeds 3% YoY", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 409.20, "basis": "Customer growth and record fund inflows continue (Q3 transcript) and the stock revisits its 52-week high 409.20 [HI], with P/E staying inside its 5y range up to 25.2x [RA]; above the mechanical bull 224.37 because that model's P/B+ROE leg ignores the sustained ~37% ROE."},
    "base": {"probability": 0.50, "target_price_12m": 370.00, "basis": "ROE holds near 36.9% [RA] and P/E stays near its current 20.0x, below the 5y median 21.0x [RA], so the price tracks earnings; it sits well above the unreliable mechanical base 186.81 because the methods disagree 2.1x [fact sheet]."},
    "bear": {"probability": 0.25, "target_price_12m": 318.40, "basis": "Lower trading activity extends the ROIC fade (4.6pp below the 2-year high [RA-T]) and P/E de-rates to its 5y low 18.5x [RA], taking the price back to the 52-week low 318.40 [HI]."}
  },
  "entry_price": 149.45,
  "entry_basis": "valuation file: base 186.81 x 0.8 [RA,IS,BS,CF,ST]. The fair value is flagged unreliable, so a hit triggers a full re-research, not a buy.",
  "replaces": null,
  "replacement_reason": null
}
```
