# Evaluation: Bank of Ningbo Co., Ltd. (SHE:002142) — 2026-10-19
## Bear case
Returns are eroding every year: ROE has fallen from 14.6% (FY2021) to 11.8% TTM [Certain], consistent with China-wide net interest margin compression that shows no sign of ending [Likely]. The cheapness is relative to its own past, not to peers: P/E of 7.6x and P/B of 0.8x both sit above the peer medians of 6.5x and 0.7x [Certain], so the stock is not even the cheap option among Chinese banks. The fact sheet carries no NPL ratio, NIM, provisioning or capital data, so the credit risk in an SME-heavy book cannot be tested [Certain]; the rising net margin could reflect provision releases rather than franchise strength [Guessing]. Piotroski F-Score is a middling 4 [Certain]. The shares are up 27.8% over 12 months and trade near the 52-week high of 36.49 [Certain], so part of the re-rating has already happened. Q3 results are due Oct 30, 2026 [Certain].
## Bull case
The mechanical fair value puts even the bear case (37.50) above the 34.72 close and the base at 45.00 [Certain]. The reverse DCF implies -5.7% revenue growth next year, pessimistic for a bank whose net income has grown in every year shown [Likely]. P/B sits in the 14th percentile of its 5-year range and P/E in the 28th [Certain]. Net margin has risen to 53.0% TTM from 48.3% in FY2021 [Certain], shares are not being diluted (-0.10% YoY) [Certain], and beta of 0.60 makes it a low-volatility holding [Certain]. A coastal Zhejiang retail/SME deposit franchise has historically earned above-peer returns, which may justify its premium to peers [Guessing].
## Decision
```json
{
  "ticker": "SHE:002142",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A higher-return Chinese regional bank trades near the bottom of its own 5-year P/B range, but ROE is falling every year, it is priced above peers, and the fact sheet carries no credit-quality data to test the downside.",
  "rationale": "Cheap only against its own history while ROE declines and it trades above peers; with no NPL, NIM or capital data, the asset-quality risk in an SME book is untestable. The mechanical fair value assumes a sustainable ROE the trend contradicts. Good but not compelling: AVOID, no position.",
  "price_at_decision": 34.72,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002142/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) rises back above 12.5%, the FY2024 level, showing the five-year decline in returns has reversed.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12.5}},
    {"text": "The Q3 2026 report (due Oct 30, 2026) or later filings disclose stable non-performing-loan and provision-coverage ratios, showing the rising net margin is not driven by provision releases.", "check": {}},
    {"text": "TTM ROE falls below 10%, confirming structural margin compression and making the AVOID firmer.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.00, "basis": "ROE stabilises and P/B re-rates toward the mechanical base fair value of 45.00 from the P/B + ROE and FCFE blend [RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 36.50, "basis": "P/B holds near 0.8x [RA] while book value grows modestly; below the mechanical bear of 37.50 because that model assumes a sustainable ROE whereas ROE has fallen every year to 11.8% TTM [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 30.38, "basis": "Continued NIM compression pushes ROE lower and P/B back to its 5-year low of 0.7x [RA], in line with the peer median of 0.7x [P:SHA:600036]; the mechanical bear does not capture the falling-ROE trend [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default anchor (base 45.00 x 0.8) is already above the 34.72 close. The obstacles are the falling ROE trend and missing credit-quality data, which a lower price would not resolve.",
  "replaces": null,
  "replacement_reason": null
}
```
