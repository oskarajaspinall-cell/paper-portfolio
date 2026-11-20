# Evaluation: Capital One Financial Corporation (COF) — 2026-11-20

## Bear case
The fall has no company-specific results behind it: the next fact-sheet earnings date shown (Oct 20, 2026) has passed with no reaction in the last 10 sessions, so the drop to 181.76 is credit-cycle and sentiment repricing [Certain]. That repricing may be right. The HY spread is up 0.77pp and VIX 28.44 over ~3m (macro overlay), and the 10-Q shows earnings helped by a Domestic Card allowance release; a reserve build would hit both earnings and the multiple [Likely]. ROE fell from 20.4% (FY2021) to 9.4% TTM, below any quality bar, and the rolling FCF margin fell from 72.2% to 53.7%, though lender FCF is loan-flow noise [Certain]. Shares are up 29.78% YoY from the Discover and Brex deals, so per-share accretion is unproven [Certain]. Berkshire cut its stake [Likely]. The trend is broken: 8.7% below the 200-day [Certain].

## Bull case
At 10.8x P/E (9th percentile of its 5y range) and 1.0x book, 46% below the peer P/B median, the price implies -3.0% revenue growth, i.e. stagnation [Certain]. ROE is recovering from the FY2025 trough of 2.4% to 9.4% TTM and net margin from 7.5% to 22.2%, consistent with deal costs rolling off [Certain]. Owning the Discover network lets COF capture interchange on its own cards, a durable edge few issuers have [Likely]. Capital returns are heavy: $7.9 billion of buybacks in nine months [company-reported] (https://www.sec.gov/Archives/edgar/data/927628/000092762826000152/cof-20260930.htm). The allowance coverage of 4.92% [company-reported] is a cushion, and the HY spread of 3.52% is still low in level [Likely]. Base fair value of 228.30 sits above the price, though the method range is very wide [Certain].

## Decision
```json
{
  "ticker": "COF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROE fell to a 2.4% FY2025 trough on Discover acquisition effects and has recovered to 9.4% TTM [RA]; the rolling FCF margin decline (72.2% to 53.7%) reflects loan-flow swings in a lender's cash flow, not lost share [CF-T; note section 2].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Consumer-credit deterioration (HY spread and VIX rising per the macro overlay) ends allowance releases and forces a reserve build, cutting earnings while the multiple de-rates.",
    "veto": null
  },
  "thesis": "A scale card issuer that now owns its network trades at a trough multiple on recovering ROE, but returns are still low and credit risk is rising.",
  "rationale": "The fall is credit-cycle and sentiment repricing, not new company results, and it does not lift the scorecard to the buy bar: ROE of 9.4% is low, the trend is broken and the credit backdrop is turning. Good but not compelling, so AVOID; cash is an acceptable outcome.",
  "price_at_decision": 181.76,
  "price_date": "2026-11-19",
  "research_note": "research/COF/2026-11-20.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 7%, showing the post-Discover recovery from 2.4% has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "TTM net margin falls below 15%, from 22.2%, signalling provisions or deal costs are eroding profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 15}},
    {"text": "Allowance coverage ratio (10-Q MD&A) is rebuilt above 5.5% on credit deterioration, from 4.92% [company-reported]."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 235, "basis": "ROE keeps recovering and the P/E moves toward the 12.5x peer median [RA] on rising TTM earnings, between the P/E bull 258.54 and FCFE base 228.30 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 195, "basis": "P/E holds near its 5y median 10.9x [RA] with modest earnings growth, between the P/E method base 184.09 and the FCFE base 228.30, the lower method weighted given lender FCF noise [note section 3]."},
    "bear": {"probability": 0.30, "target_price_12m": 140, "basis": "Macro overlay tilt toward bear (small, raised bear weight): HY spread above 5% brings a reserve build and a P/E nearer 8x on lower earnings [macro overlay], above the P/E bear 85.09 as the balance sheet and capital returns stay intact."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE of 9.4% TTM is below the quality bar, so the scorecard cannot reach conviction 4 at any price; a lower price would not change the decision until returns recover.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```
