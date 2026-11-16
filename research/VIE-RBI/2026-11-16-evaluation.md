# Evaluation: Raiffeisen Bank International AG (VIE:RBI) — 2026-11-16
## Bear case
The re-rating has happened: the stock is up 91.3% in 12 months and trades 20.7% above its 200-day average, with P/E 10.5x and P/B 0.9x both above their own 5-year maxima [RA] [Certain]. If growth slows or Russia flares, an extended price risks a sharp de-rating back toward its own history [Likely]. Quality is mediocre: ROE fell from 19.5% in FY2022 to 7.6% in FY2025 and is 10.2% TTM, below the 15% bar for a high-quality franchise [RA] [Certain]. The Direction change line on FCF margin (down 40.8pp in 12 months) reflects deposit and loan flows, not economics [Likely]. The real risk is binary: sanctions, the Rasperia asset freeze and a short-seller report on Russia ties hit the shares on 2026-09-17 [OV] [Certain]; Russia's profit share is unverified (macro overlay) [Guessing]. The fair value is flagged unreliable; base 59.67 EUR is below the 62.60 EUR close [Certain].
## Bull case
Earnings momentum is real: Q3 2026 brought record net interest income and loan growth, 9M core profit rose, and the FY26 NII view was lifted (Q3 2026 transcript, /quote/vie/RBI/transcripts/662869-q3-2026/) [Likely]. TTM ROE of 10.2% has recovered from 7.6% in FY2025 [RA] [Certain]. Versus peers the stock still trades at a discount: -14% on P/E and -45% on P/B [RA] [Certain]. A Vienna court issued a default judgment against Rasperia (2026-09-22), a step toward recovering frozen value [Likely]. Two CEE/SEE acquisitions add growth [Likely]. A clean Russia exit could close the peer discount, and the FCFE base of 77.41 EUR sits above the price [Guessing]. The trend is strong: the 50-day average is 16.2% above the 200-day [ST] [Certain]. ECB rates edged up, mildly helpful for NII (macro overlay, context only) [Likely].
## Decision
```json
{
  "ticker": "VIE:RBI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The falling metric is FCF margin (60.2% to 19.5% TTM [CF-T]); for a bank it reflects deposit and loan flows, not economics (note section 2). Underlying earnings improved: TTM ROE 10.2% vs 7.6% in FY2025 [RA], record Q3 2026 NII (/quote/vie/RBI/transcripts/662869-q3-2026/).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Russia: a sanctions, court or regulator action forcing a write-off or capital hit on the Russian business (Rasperia asset freeze, short-seller report 2026-09-17 [OV]), on top of a de-rating risk from a price already above its own 5-year multiple range.",
    "veto": null
  },
  "thesis": "A recovering CEE bank with real NII momentum, but mediocre ROE, an unresolved Russia binary and a price already re-rated above its own history leave no margin for error.",
  "rationale": "Scorecard conviction 1: ROE 10.2% is below the high-quality bar, no moat, the Russia sanctions and Rasperia exposure is an unquantified high risk, and multiples sit above their own 5-year range after a 91.3% run, so no valuation or trend points. Peer discount and NII momentum do not offset that.",
  "price_at_decision": 62.60,
  "price_date": "2026-11-13",
  "research_note": "research/VIE-RBI/2026-11-16.md",
  "triggers": [
    {"text": "ROE (statistics page) falls below 7% TTM: the earnings recovery has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "Net margin (statistics page) falls below 15% TTM.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 15}},
    {"text": "A court ruling, sanction or regulator action forces a write-off or capital-ratio hit on the Russian business (company filings)."},
    {"text": "A verified, completed exit or deconsolidation of the Russian business without a material capital hit would remove the main obstacle (company filings)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 77.41, "basis": "Russia resolved cleanly and NII momentum holds: price reaches the FCFE DCF base of 77.41 EUR [fair value section], narrowing the -45% P/B discount to peers [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 59.67, "basis": "Earnings hold near TTM ROE 10.2% [RA] but multiples already above their 5-year max stop expanding: the blended base fair value of 59.67 EUR [fair value section]."},
    "bear": {"probability": 0.25, "target_price_12m": 34.32, "basis": "A Russia write-off or sanctions hit (key risk) de-rates P/B back toward its 5-year range: bear fair value 34.32 EUR [fair value section]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the unresolved Russia sanctions/Rasperia exposure and mediocre ROE would not be fixed by a lower price; the fair value is also flagged unreliable. Re-research on a verified Russia resolution instead.",
  "replaces": null,
  "replacement_reason": null
}
```
