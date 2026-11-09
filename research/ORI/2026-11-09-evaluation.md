# Evaluation: Old Republic International Corporation (ORI) — 2026-11-09
## Bear case
ORI is not cheap against its own history: P/E 9.0x sits at 49% and EV/EBITDA 7.9x at 53% of their 5y ranges, and P/B 1.6x at 68% prices book toward the upper half [Certain] (RA). The peer discount (P/E -24%, P/B -31%) reflects a title cyclical and modest moat, not mispricing [Likely]. The **Direction change** matters: ROIC fell from 19.6% (FY2021) to 8.2% (FY2023) and the rolling 13.5% is still below the 2-year high of 15.2% (RA-T) [Certain]; the Q2 call cited higher specialty loss ratios and the Q3 call a softer P&C market [Likely], so the rebound may already be peaking as pricing turns. The mechanical bear fair value of 25.15 sits far below the price while the base offers only +15.7% [Certain]. Margin and cash-flow lines are [data unavailable], so underwriting quality cannot be verified from the fact sheet [Certain].

## Bull case
ROE has recovered to 17.9% TTM and ROIC rose from 11.3% to 13.5% over the last 12 months (RA-T) [Certain]; the 5-year "falling" label is anchored on an FY2021 peak, so the drift is normalisation from a high-water mark, not lost franchise [Likely]. Leverage is low (net debt/EBITDA 1.04x site definition), beta 0.53, Piotroski F 6, and the share count is shrinking 1.06% YoY alongside a regular 31.5-cent dividend [Certain]. Title income rose on the Q3 call and the ECM acquisition was described as accretive [Likely]. Higher yields (10y 4.84%) support float income [Likely]. The base fair value of 45.82 and bull 53.08 sit above the 39.61 close, and the stock trades at a discount to WRB, CINF, TRV and CB on every multiple [Certain].

## Decision
```json
{
  "ticker": "ORI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: rolling ROIC rose from 11.3% to 13.5% (RA-T, 3-year flat). The 5y fall is measured from an FY2021 peak of 19.6%, i.e. normalisation with the balance sheet intact (net debt/EBITDA 1.04x), not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A softening P&C pricing cycle (flagged on the Q3 2026 call, /stocks/ori/transcripts/714210-q3-2026/) and higher specialty loss ratios (Q2 call) push ROE back toward the FY2022-23 levels near 10%.",
    "veto": null
  },
  "thesis": "A low-levered, shareholder-returning US specialty and title insurer with recovering ROE trades at a peer discount but only mid-range on its own multiples, leaving moderate upside against a heavy bear tail.",
  "rationale": "Quality has recovered and the balance sheet is sound, but P/E and EV/EBITDA sit mid-range of their own history, P/B in the upper half, and base fair value upside is moderate while the soft-market risk is live. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 39.61,
  "price_date": "2026-11-06",
  "research_note": "research/ORI/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, back toward the FY2022-23 trough (10.5% / 9.5%), showing the soft market is eroding underwriting returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 10%, reversing the rolling recovery from 11.3% to 13.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.04x site definition now), above the FY2023 peak of 1.87x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Shares change YoY turns positive by more than 2%, i.e. buybacks reverse into issuance.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 53.08, "basis": "ROE holds near 17.9% TTM [RA] as title income keeps rising (Q3 call), lifting value to the mechanical bull fair value of 53.08 (P/B + ROE and P/E blend)."},
    "base": {"probability": 0.5, "target_price_12m": 45.82, "basis": "ROIC stays near 13.5% [RA-T] with the softer P&C market offset by float income, in line with the mechanical base fair value of 45.82."},
    "bear": {"probability": 0.25, "target_price_12m": 29.71, "basis": "Soft-market loss ratios (Q2/Q3 calls) cut ROE toward FY2023's 9.5% [RA] and P/B reverts to its 5y median 1.2x [RA]; less severe than the mechanical bear of 25.15 because leverage is low (1.04x) and buybacks continue."}
  },
  "entry_price": 36.66,
  "entry_basis": "valuation file: base 45.82 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```
