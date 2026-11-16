# Evaluation: Arch Capital Group Ltd. (ACGL) — 2026-11-16
## Bear case
The property-catastrophe and reinsurance cycle is turning: reinsurance net premiums written fell about 9% in Q3 and management expects continued pricing pressure [company-reported] (https://www.sec.gov/Archives/edgar/data/947484/000094748426000152/acgl-20260930.htm) [Certain]. ROIC of 15.9% TTM is already 4.8pp below its 2-year high of 20.7% [RA-T]; the direction change is the soft market feeding through, and it more likely extends than reverses [Likely]. Q3 was flattered by light catastrophe losses, so one heavy cat season could hit earnings hard [Likely]. The mechanical base of 150.47 leans on a P/B + ROE method that capitalises a near-peak ROE; the P/E method gives only 99.30, below the price [Certain]. The price is 12.3% above its 200-day average after a 19.4% year: trend strength can de-rate quickly if earnings slow with the cycle [Likely]. The co-founder chair stepping down adds modest succession uncertainty [Guessing].

## Bull case
Arch is a top-tier underwriter: ROE 18.7% TTM, ROIC 15.9%, with net debt/EBITDA 0.82x and FCF/NI of 128.6% [Certain]. ROIC is flat on a year earlier, not collapsing, and the 5-year trend is rising [Certain]. It trades at 8.9x earnings, 15% below the peer median of 10.6x, and EV/EBITDA sits at the 7th percentile of its 5-year range [Certain]. Shrinking reinsurance volume in a soft market is disciplined capital allocation, returned through buybacks: shares are 6.92% fewer than a year ago [Likely]. Diversification into mortgage and casualty-led insurance cushions the reinsurance softening [Likely]. The stock is in a healthy uptrend, beating SPY by 9.0pp over 12 months with a 15.85% FCF yield, and higher yields lift investment income on its short-duration bond book (macro overlay, context only) [Likely].

## Decision
```json
{
 "ticker": "ACGL",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "ROIC's 3-year fall and gap to its 2024 high reflect the softening reinsurance pricing cycle (reinsurance NPW down about 9% in Q3, https://www.sec.gov/Archives/edgar/data/947484/000094748426000152/acgl-20260930.htm), with ROIC flat year on year, leverage low at 0.82x and buybacks continuing: a cyclical trough with the balance sheet intact, not lost share.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "A soft reinsurance market plus a normal-to-heavy catastrophe year pushes ROE well below its current level, and the extended price de-rates as earnings slow.",
  "veto": null
 },
 "thesis": "A disciplined, lowly levered specialty insurer earning high-teens ROE trades below peers and low in its own EV/EBITDA range while in a healthy uptrend, with buybacks compounding per-share value through a softening cycle.",
 "rationale": "Scorecard conviction 4: high returns, low leverage, a low position in its own multiple range and trend strength outweigh a cyclically softening reinsurance market. The bear case is real, so only the standard core size, which Python volatility-scales. No cap is breached and Financials is unheld, so nothing is replaced.",
 "price_at_decision": 109.61,
 "price_date": "2026-11-13",
 "research_note": "research/ACGL/2026-11-16.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 12%, showing the soft cycle is eroding returns beyond a normal cyclical dip.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 12
   }
  },
  {
   "text": "TTM ROE falls below 14%, well under the 18.7% now, signalling underwriting returns have broken down.",
   "check": {
    "source": "statistics",
    "field": "roe",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "Net debt/EBITDA rises above 1.5x, reversing the deleveraging.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 1.5
   }
  },
  {
   "text": "Reinsurance net premiums written decline by more than 15% year on year for two consecutive quarters in the 10-Q."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 150.47,
   "basis": "ROE holds near 18.7% [RA] and buybacks continue, so the P/B + ROE method's value is realised, matching the mechanical base fair value [fact sheet]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 118,
   "basis": "P/E stays near the current 8.9x [RA] while the 6.92% share-count reduction [ST] lifts per-share earnings through a gently softening cycle; set below the mechanical base because the P/E method gives 99.30 and ROE is likely near peak (note section 3)."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 85.47,
   "basis": "A heavy catastrophe year plus reinsurance pricing pressure (Q3 NPW down about 9% [company-reported]) compresses earnings and the multiple to the mechanical bear fair value [fact sheet]."
  }
 },
 "new_evidence": null,
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/ACGL/2026-11-16-evaluation-2.md",
  "conviction": 4
 }
}
```
