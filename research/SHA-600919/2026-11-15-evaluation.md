# Evaluation: Bank of Jiangsu (SHA:600919) — 2026-11-15
## Bear case
The re-rating is done: P/E of 7.0x and P/B of 0.7x both sit above their five-year maxima of 5.9x and 0.6x [RA], with no peer discount left [Certain]. ROE has slipped from a 12.7% FY2022 peak to 10.8% TTM [RA], so returns are softening while the multiple expands [Certain]. The best-fit method (P/B + ROE) puts base value at 13.87 CNY, barely above the 13.23 close; the higher blend leans on an FCFE model the fact sheet itself flags unreliable (methods disagree 4.2x) [Certain]. The FCF-margin Direction change (700.1% to 527.2%) is deposit/loan flow noise for a bank, not a business signal [Likely]. The valuation points come from trend strength (price 16.2% above its 200-day, RSI 67.5): if Chinese bank margins or credit quality slip, an extended price risks de-rating back to its historical range [Likely]. NPLs and capital ratios are not visible, so credit risk is unmeasured [Certain].
## Bull case
Net margin has risen 4.7pp over five years to 52.7% [IS], a sign of cost discipline and stable provisioning [Certain]. ROE near 11% is respectable for a Chinese regional bank and flat over five years (+0.2pp) [RA] [Certain]. The share count fell 2.07% YoY [ST], so capital is being returned [Certain]. The trend is working: up 18.9% over 12 months, 50-day 9.0% above the 200-day, and relative strength over SPY across 3, 6 and 12 months [HI] [Certain]. A -0.10 beta [ST] makes it a diversifier against US holdings [Likely]. If ROE holds, P/B could keep normalising toward peers as Chinese banks re-rate [Guessing].
## Decision
```json
{
  "ticker": "SHA:600919",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Only FCF margin is flagged falling (700.1% to 527.2% TTM [CF-T]); for a bank this reflects deposit and loan flows, not economics, while ROE is flat over five years (+0.2pp) and net margin rose 4.7pp [RA,IS].", "moat": "none", "key_risk": "high", "key_risk_text": "Extended valuation (P/E and P/B above their 5y maxima [RA]) de-rates if Chinese bank NIM or credit quality weakens; asset quality is not visible on the fact sheet.", "veto": null},
  "thesis": "A fairly run Chinese regional bank with flat ~11% ROE whose re-rating has already taken P/E and P/B above their five-year ranges, leaving little margin of safety.",
  "rationale": "Quality is average (ROE 10.8%, no moat) and the best-fit P/B + ROE value is near the price; the blended upside rests on an FCFE method unsuitable for banks. Trend strength alone does not make this high conviction. AVOID.",
  "price_at_decision": 13.23,
  "price_date": "2026-11-13",
  "research_note": "research/SHA-600919/2026-11-15.md",
  "new_evidence": {"type": "price_move", "text": "Price rose from 12.00 at the 2026-10-25 verdict to 13.23 on 2026-11-13, and the Q3 2026 report was filed on 2026-10-29 (https://stockanalysis.com/quote/sha/600919/filings/3902735/)."},
  "triggers": [
    {"text": "TTM ROE (ratios page) falls below 9.5%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9.5}},
    {"text": "Net (profit) margin falls below 48%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 48}},
    {"text": "Share count grows more than 3% YoY (dilutive equity raise)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 15.42, "basis": "ROE holds near 11% [RA] and P/B keeps normalising toward peers, matching the P/B + ROE bull value of 15.42; the blended bull of 20.28 is not used because it leans on the unreliable FCFE method [fair value section]."},
    "base": {"probability": 0.5, "target_price_12m": 13.87, "basis": "Flat ROE of 10.8% [RA] supports the P/B + ROE base of 13.87, below the blended 17.29 because the FCFE leg is flagged unreliable for a bank (methods disagree 4.2x)."},
    "bear": {"probability": 0.25, "target_price_12m": 12.51, "basis": "ROE keeps drifting down from its 12.7% peak [RA] and the above-range P/B de-rates, in line with the P/B + ROE bear value of 12.51."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3: quality (average ROE, no moat, unseen asset quality) is the obstacle, not price."
}
```
