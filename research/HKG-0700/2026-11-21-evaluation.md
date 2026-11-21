# Evaluation: Tencent Holdings Limited (HKG:0700) — 2026-11-21
## Bear case
The cheapness is on earnings, not cash: FCF margin collapsed from 28.5% to 3.6% TTM, FCF yield is 1.10% and P/FCF 90.8x sits far above its 5y range [Certain]. Q3 capex rose more than sixfold for AI infrastructure and non-IFRS operating profit fell while revenue growth slowed to 8% (transcript, SCMP) [Likely]. That spend has no proven return [Guessing], and US remote-access chip rules will delay model training, per management (Fortune) [Likely], so Tencent may spend more for a weaker AI position. ROIC is off its 2-year high of 18.1% and Piotroski F is only 4 [Certain]. The fair value is one method (EV/Revenue) because the DCF fails on a negative base cash-flow margin [Certain], so the apparent discount is unreliable. The price is in a downtrend: 25.7% below its 200-day average, -44.7% over 12 months [Certain]; there is no trend-strength support, and China policy risk sits on top.
## Bull case
WeChat's network effects are among the most durable moats in global internet [Likely]. Operating margin is flat at 32.2% TTM, near its 2-year high, and the 5-year trend is strongly up (ROIC 13.0% to 16.5%, gross margin 43.9% to 56.6%) [Certain]: the core business is intact and the FCF drop is a capex choice, not lost share [Likely]. Excluding new AI products, operating profit grew 8% (transcript) [Likely]. The balance sheet funds the build-out (net debt/EBITDA 0.25x, Altman Z 3.86) and the share count is shrinking 1.04% a year [Certain]. P/E 11.5x and EV/EBITDA 9.1x are below their 5y minimums and well below peers [Certain]; even the mechanical bear fair value of 423.59 HKD is above the price [Certain]. If capex normalises or AI cloud monetises, FCF re-converts and the multiple can recover [Guessing].
## Decision
```json
{
 "ticker": "HKG:0700",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "FCF margin fell 28.5% -> 3.6% TTM [CF-T] while operating margin stayed flat at 32.2% [IS-T]: the drop is a sixfold step-up in AI infrastructure capex (SCMP, https://www.scmp.com/tech/big-tech/article/3374902/tencent-profit-dips-sixfold-increase-ai-infrastructure-spending-sacrifices-margin), funded from a balance sheet at 0.25x net debt/EBITDA [BS]; ROIC's -0.9pp slip is small. Heavy investment, not lost share, though its return is unproven.",
  "moat": "wide",
  "key_risk": "high",
  "key_risk_text": "The AI capex step-up fails to earn its cost of capital while US chip curbs delay Tencent's models (Fortune, https://fortune.com/2026/11/20/tencent-alibaba-us-chip-curbs-cloud-ai/), so FCF stays depressed and the low earnings multiple is a value trap; China regulation adds on top.",
  "veto": null
 },
 "new_evidence": {
  "type": "new_results",
  "text": "Q3 2026 results released 2026-11-18 (https://stockanalysis.com/quote/hkg/0700/filings/4006933/): revenue growth slowed to 8% and AI capex cut TTM FCF margin to 3.6% [CF-T], while the price fell to 344.00 from above the 415.602 entry price."
 },
 "thesis": "A wide-moat platform with flat 32.2% operating margin trades below its 5y minimum earnings multiples and below even its mechanical bear fair value, where the price assumes the AI capex surge never converts back to cash.",
 "rationale": "The fall is a capex-driven FCF reset and chip-curb sentiment, not a break in the core franchise: margins and returns hold, the balance sheet funds the spend. Scorecard conviction 4 despite a high key risk; Python sizes it. China/HK cap and cash floor require a replacement.",
 "price_at_decision": 344.0,
 "price_date": "2026-11-20",
 "research_note": "research/HKG-0700/2026-11-21.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 28%, showing AI costs or competition are eroding the core franchise, not just cash flow.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 28
   }
  },
  {
   "text": "TTM ROIC falls below 12%, showing the capex build-out is diluting returns.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 12
   }
  },
  {
   "text": "TTM FCF margin (cash-flow page, trailing) still below 10% after two further quarterly reports, i.e. the spend is not converting to cash."
  },
  {
   "text": "Revenue growth stays below 8% YoY for two consecutive quarters (income statement)."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 557.55,
   "basis": "Capex peaks and AI cloud monetises, FCF re-converts and EV/Revenue returns to the mechanical base fair value 557.55 [valuation file, RA]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 423.59,
   "basis": "Core earnings hold with operating margin flat [IS-T] but FCF stays weak, so the multiple recovers only toward the mechanical bear fair value 423.59, still below the 5y P/E minimum 14.8x [RA]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 300.0,
   "basis": "Capex keeps FCF near 3.6% margin [CF-T] and chip curbs delay AI (Fortune), so P/E stays below its 5y minimum on flatter earnings and the price breaks the 339.60 52-week low [HI]; below the mechanical bear because the DCF fails on negative cash-flow margin."
  }
 },
 "replaces": "HKG:0291",
 "replacement_reason": "The China/HK group is at the 25% cap and cash is near the 1.5% floor, so a China/HK holding must go. Tencent's ROIC of 16.5% beats the brewer's 11.9% and its WeChat network moat is wider, at a deeper discount to its own history; selling the largest China/HK weight frees enough room for Tencent at full size.",
 "second_opinion": {
  "file": "research/HKG-0700/2026-11-21-evaluation-2.md",
  "conviction": 4
 }
}
```
