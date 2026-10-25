# Evaluation: EssilorLuxottica (EPA:EL) — 2026-10-24
## Bear case
The drift setup fails on reward:risk. The honest drift stop is 161.6 EUR (reaction-day low 163.1 less a quarter ATR), so 2:1 needs 220.4, but the only evidenced resistance is the 198.70 six-month high, roughly 0.9:1 [Certain]. The beat was revenue only, with guidance confirmed, not raised, and smartglasses growth slowing sharply [Likely] (https://www.reuters.com/business/essilorluxottica-tops-estimates-q3-despite-slowdown-growth-of-smart-glasses-2026-10-20/). RSI 78.5 and a close 19.2% above the 50-day show the jump is already extended; the 50-day sits 18.4% below the 200-day and the 12-month change is -41.8%, a bounce in a downtrend [Likely]. Price is above base fair value 163.41 and the reverse DCF needs 12.8% year-1 growth [Certain]. Regulatory scrutiny of smartglasses adds gap risk [Likely] (https://www.reuters.com/business/media-telecom/essilorluxotticas-smart-glasses-boom-runs-into-tougher-regulatory-scrutiny-2026-10-20/).

## Bull case
The reaction was real: +15.5% on 3.4x volume with 132% of the jump held, the textbook drift signature [Certain]. Q3 revenue rose 7.2% at constant currency with wearables up 20% and Asia Pacific double-digit, and FY 2026 plus five-year guidance was confirmed [Likely] (fact sheet transcript headline [OV]). EV/EBITDA 14.2x sits below its 5y minimum 16.9x and below peers [Certain], so crowding risk is moderate. Balance sheet is sound: Altman Z 3.66, net debt/EBITDA 2.29x [Certain]. A break above 198.70 could open a run toward the bull fair value of 241.25 [Guessing].

## Decision
```json
{
  "ticker": "EPA:EL",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 revenue beat drove a high-volume gap, but the volatility stop and the 198.70 resistance leave reward:risk well under 2:1 on an overbought bounce inside a downtrend.",
  "rationale": "The drift signal is real, but the only evidenced target, the 198.70 six-month high, gives about 0.9:1 against the ATR-based stop at 161.6; reaching 220.4 needs a breakout that fair value, RSI 78.5 and the downtrend do not support. The rule fails, so AVOID; cash is acceptable.",
  "price_at_decision": 181.20,
  "price_date": "2026-10-23",
  "research_note": "research/EPA-EL/2026-10-24.md",
  "exit_plan": {"target": 198.70, "stop": 161.6, "time_limit": "2026-12-18"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 241.25, "basis": "Wearables growth of 20% and confirmed five-year guidance [OV transcript] lift the stock to the mechanical bull fair value 241.25 [IS,RA], consistent with P/E returning toward its 5y range [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 163.41, "basis": "Growth stays solid but short of the 12.8% year-1 growth the reverse DCF implies, so the price converges on the blended base fair value 163.41 [IS,BS,CF,RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 125.44, "basis": "Smartglasses slowdown and regulatory scrutiny (https://www.reuters.com/business/media-telecom/essilorluxotticas-smart-glasses-boom-runs-into-tougher-regulatory-scrutiny-2026-10-20/) with ROIC only 5.4% [RA] pull the price to the bear fair value 125.44."}
  },
  "replaces": null,
  "replacement_reason": null
}
```
