# Evaluation: OMV Aktiengesellschaft (VIE:OMV) — 2026-11-27
## Bear case
TTM earnings are a price spike, not a better business: the Q3 call credits higher energy prices and exceptional refining margins in the wake of the Iran war, offsetting weaker Chemicals and disrupted Middle East liftings [Likely]. The Direction change lines (ROIC 7.1% -> 11.0%, ROCE 12.5% -> 14.3%, FCF margin 2.9% -> 9.0%) are therefore cyclical, while the 5-year trend falls (ROIC 11.9% FY2021 to 5.3% FY2025) and operating margin is flat-to-down at 17.4% vs 18.3% [Certain]. P/E 7.1x and the 11.34% FCF yield rest on that peak; EV/EBITDA 4.2x sits at 88% of its 5y range and P/B 1.2x above its 5y max [Certain]. The fall since 16 November has no company-specific explanation, consistent with margins normalising [Guessing]. The price sits above its 200-day average after a +42.2% year: an extended stock de-rates if the spike fades [Likely]. No evident moat; Altman Z 2.00 [Certain].

## Bull case
The balance sheet is strong: net debt/EBITDA 0.66x and Piotroski F 7, so a cyclical trough is survivable [Certain]. The reverse DCF already prices -11.9% year-1 revenue growth, i.e. a fade, and the mechanical DCF base is 97.50 EUR vs 68.00 [Certain]. P/E is 24% below the peer median [Certain]. Growth is not just price: Neptun Deep in Romania is guided to add about €500 million a year at plateau (Reuters headline), with Borouge International and FCF growth targeted by management [Likely]. Beta 0.20 makes it a diversifier against a falling S&P 500, and relative strength vs SPY is +35.5pp over 12 months [Certain]. The recent dip pulled RSI to 40.7 and the price 5.5% below its 50-day average without any reported deterioration [Certain].

## Decision
```json
{
  "ticker": "VIE:OMV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds nothing falling over 1 or 3 years; the 5-year falls in ROIC, ROCE and FCF margin are a cyclical comedown from the FY2022 commodity peak, and all three rose over the last 12 months on higher energy prices and refining margins (Q3 2026 call, https://stockanalysis.com/quote/vie/OMV/transcripts/632415-q3-2026/), which is itself the risk.", "moat": "none", "key_risk": "high", "key_risk_text": "TTM earnings rest on an Iran-war spike in refining margins and energy prices; a normalisation reverses the TTM gains and de-rates a stock that is up 42.2% in a year (https://www.reuters.com/business/energy/omv-posts-highest-quarterly-operating-profit-since-2022-fuel-prices-soar-2026-10-29/).", "veto": null},
  "thesis": "A low-leverage integrated producer on a low P/E, but its earnings sit on a cyclical refining and energy-price spike with no moat to keep them.",
  "rationale": "The dip has no company-specific cause, so it neither breaks nor repairs the case; the obstacle from 16 November (peak-cycle earnings, no moat, high normalisation risk) is unchanged. Strong balance sheet and Neptun Deep growth are not enough for conviction 4. Cash is acceptable.",
  "price_at_decision": 68.00,
  "price_date": "2026-11-26",
  "research_note": "research/VIE-OMV/2026-11-27.md",
  "triggers": [
    {"text": "ROIC TTM falls below 7% (ratios page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "FCF margin TTM falls below 4%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt / EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Operating margin TTM falls below 12%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.00, "basis": "Margins hold and P/E moves toward its 5y median 8.8x [RA] on TTM earnings, helped by Neptun Deep progress (Reuters 2026-10-29); below the DCF base 97.50 because that DCF extrapolates peak-cycle TTM cash flow."},
    "base": {"probability": 0.45, "target_price_12m": 66.00, "basis": "Refining margins partly normalise as the reverse DCF already implies (-11.9% year-1 revenue [ST]); earnings ease while P/E edges up, leaving the price near today's level."},
    "bear": {"probability": 0.30, "target_price_12m": 52.00, "basis": "The Iran-war margin spike reverses (Q3 call) and EV/EBITDA returns to its 5y median 3.4x [RA] on lower EBITDA; above the mechanical bear 27.77 because net debt/EBITDA 0.66x [RA] limits equity damage."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default base 97.50 x 0.85 is above today's price, and the block is peak-cycle earnings with no moat, so a lower price on the same evidence would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```
