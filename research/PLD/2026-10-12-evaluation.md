# Evaluation: Prologis, Inc. (PLD) — 2026-10-12
## Bear case
Prologis is a low-return, rising-leverage business going into a transformational deal. ROIC is 4.0% TTM and flat over five years, ROE has fallen from 8.5% to 7.7%, and net debt/EBITDA has risen from 4.89x to 5.24x [Certain] [RA]. The ~$18.8bn Segro acquisition is paid largely in new shares, and a 15,000,000-share offering came in the same week [Certain] (Reuters/PRNewswire per fact sheet). That adds dilution and integration risk [Likely]. FCF yield is negative at -0.37% [Certain] [ST]. Even after the de-rating, EV/EBITDA of 23.9x is 26% above industrial peers [Certain] [ST]. Real yields are up 56bp in 3 months to 2.87% and the 2y yield sits above fed funds, which pushes cap rates and financing costs higher [Certain] (macro overlay, FRED). The stock trails SPY by 20.9pp over 6 months [Certain] [HI]. Q3 results on Oct 15 are a near-term gap risk [Likely].
## Bull case
PLD trades at the bottom of its own 5-year range: EV/EBITDA at the 9th percentile (23.9x vs a 26.4x median) and P/E at the 16th percentile [Certain] [RA]. Management reported record leasing signings and expects mid-single-digit market rent growth as rent gaps close [Likely] (BofA conference transcript, fact sheet [OV]). Data-center development adds an option the multiple does not price [Guessing]. Mechanical base fair value is $146.00, +12.8% upside, with a $161.40 bull case [Certain] (fact sheet fair value). Segro gives a scale European platform for shares at a de-rated price, and the deal could be accretive if real yields fall back [Guessing]. Short interest is only 2.0% of float [Certain] [ST]. Shares grew just 0.33% YoY before the deal closed [Certain] [ST].
## Decision
```json
{
  "ticker": "PLD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale industrial-REIT franchise at the bottom of its own 5-year multiples, but with flat 4% ROIC, rising leverage and a dilutive Segro acquisition, while real yields rise against it.",
  "rationale": "Base upside of +12.8% is thin against falling ROE, leverage rising to 5.24x, Segro dilution and integration risk, and a primary macro headwind from rising real yields. The stock is still 26% above peers on EV/EBITDA. Good but not compelling, so conviction 3 means AVOID; at a 20% margin of safety the risk/reward would justify a BUY.",
  "price_at_decision": 129.49,
  "price_date": "2026-10-09",
  "research_note": "research/PLD/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA (site definition) rises above 6.0x, showing the Segro deal and development spend are stretching the balance sheet beyond the current 5.24x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.0}},
    {"text": "TTM ROIC falls below 3.5%, the 5-year low, signalling lost earning power on capital employed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 3.5}},
    {"text": "TTM ROE falls below 5%, extending the 5-year decline from 8.5% to 7.7%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 5}},
    {"text": "Shares outstanding growth exceeds 5% YoY as more equity is issued for Segro, diluting per-share value beyond the base case.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 161.40, "basis": "Rent gaps close, record leasing holds and real yields reverse, so the P/FFO multiple re-rates to the mechanical bull fair value of 161.40 (fact sheet fair value; BofA transcript [OV]); probability trimmed for the moderate bear macro tilt (research/PLD/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 146.00, "basis": "The P/FFO-proxy multiple recovers toward its own history, in line with EV/EBITDA moving off the 9th percentile of its 5-year range (23.9x vs a 26.4x median [RA]), giving the mechanical base fair value of 146.00."},
    "bear": {"probability": 0.35, "target_price_12m": 112.65, "basis": "Real yields extend above 3.0% and Segro dilution and leverage (5.24x, rising [RA]) compress the multiple to the mechanical bear fair value of 112.65; probability raised for the moderate bear macro tilt (research/PLD/2026-10-12-macro.md)."}
  },
  "entry_price": 116.80,
  "entry_basis": "valuation file: base 146.00 x 0.8 = 116.80; at that margin of safety the integration and leverage risk would be paid for.",
  "replaces": null,
  "replacement_reason": null
}
```
