# Evaluation: LG CNS Co., Ltd. (KRX:064400) — 2026-11-08
## Bear case
The stock collapsed from a 153,300 high (2026-06-02) to a 57,700 low (2026-07-30) and no source explains why [Certain]; buying through an unexplained collapse is not underwriting. The Oct 30, 2026 results have passed unseen [Certain]. Recent direction is negative: ROIC fell from 25.2% to 22.8% and ROCE from 18.1% to 16.1% over twelve months, 3.9pp and 4.3pp below 2-year highs; FCF margin is 3.8pp below its 12.4% high [Certain]. The cause is unknown: equity raised (shares +6.01% YoY) swelling capital is the benign reading [Likely], but lost contracts or project write-downs cannot be excluded [Guessing]. Gross margin near 15% means a labour-based integrator with little pricing power [Likely]. FCF conversion swings from 30.0% to 187.9%, so the 7.56% FCF yield is timing-driven [Likely]. Segment, client and foreign-revenue mix are unavailable, and the DCF bear sits -64.9% below the price [Certain].
## Bull case
A net-cash (net debt/EBITDA -1.46x) IT-services group with ROIC 22.8% and operating margin rising from 7.9% to 8.8% over five years [Certain] trades at 14.9x P/E versus a 20.1x peer median and 1.0x EV/Sales versus 1.7x [Certain]. The reverse DCF prices -0.5% year-1 revenue growth, a low bar for a business whose margins have expanded [Likely]. The rolling dip is mostly returns on capital, not profitability: operating margin is down only 0.4pp and FCF margin 0.3pp year on year, consistent with a larger equity base rather than erosion [Likely]. Base fair value of 91,859 sits +24.0% above the 74,100 close [Certain]. Altman Z 4.96 and Piotroski 6 show no balance-sheet stress [Certain]. Relative strength versus SPY is positive over 3, 6 and 12 months [Certain], so the post-collapse base looks to be holding [Likely].
## Decision
```json
{
  "ticker": "KRX:064400",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 20%-plus-ROIC Korean IT integrator trades below peers with a price implying slight revenue decline, but an unexplained collapse from its high, unseen Q3 results, thin margins and no segment or client data leave the evidence too thin for high conviction.",
  "rationale": "Cheap versus peers with net cash and solid returns, but the cause of the halving from the June high is unknown, the Oct 30 results are unseen, own-history multiples and business mix are unavailable, and the rolling ROIC/ROCE dip is unexplained. Good but not compelling: AVOID at conviction 3; re-research once results and the drawdown cause are verifiable.",
  "price_at_decision": 74100.0,
  "price_date": "2026-11-06",
  "research_note": "research/KRX-064400/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18% (22.8% now, 25.2% a year earlier), showing the rolling decline is erosion of returns, not a larger equity base.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 7.5% (8.8% now, 7.9% in FY2021), reversing the five-year margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7.5}},
    {"text": "TTM FCF margin falls below 4% (8.6% now), back toward the FY2022-FY2023 levels of 2.1% and 1.8%, showing the cash step-up was working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt/EBITDA on the ratios page rises above 0x (-1.46x TTM now), meaning the net cash position is lost."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 125000, "basis": "Operating margin holds near 8.8% [IS] with ROIC above 20% [RA] and P/E closes most of the gap to the 20.1x peer median [RA,P]; below the mechanical bull of 143,372 because own 5y multiple history is unavailable to support a full re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 85000, "basis": "Margins stay flat and the reverse-DCF bar of -0.5% growth is beaten modestly [fact sheet Fair value]; below the mechanical base of 91,859 because the unexplained fall from 153,300 [HI] and the softer rolling ROIC [RA-T] warrant a discount; macro overlay is context only."},
    "bear": {"probability": 0.30, "target_price_12m": 45000, "basis": "The drawdown proves to reflect lost contracts, ROIC keeps sliding from its 26.7% 2-year high [RA-T] and FCF conversion reverts toward 30.0% [CF,IS]; above the mechanical bear of 25,976 because net cash of -1.46x net debt/EBITDA [BS] cushions the downside."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the cause of the collapse from the June high, the unseen Oct 30 results and the missing segment/client data are information gaps a lower price would not resolve; re-research once results and the drawdown cause are verifiable.",
  "replaces": null,
  "replacement_reason": null
}
```
