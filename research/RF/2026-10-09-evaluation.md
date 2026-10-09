# Evaluation: Regions Financial Corporation (RF) — 2026-10-09
## Bear case
Returns are eroding while the multiple has expanded. ROE fell from 13.8% (FY2021) to 11.9% TTM and net margin from 36.2% to 30.8% [Certain] [RA, IS], yet P/B of 1.3x sits above its own 5-year maximum and 12% above peers [Certain] [RA]. Paying a record book multiple for a declining ROE leaves no margin of safety: base fair value of 27.45 is only +1.4% above the 27.07 close, against -16.4% to the bear value [Certain] [fact sheet]. Piotroski F-Score of 3 flags weak fundamental momentum [Certain] [ST]. The macro overlay tilts moderately bearish: the 10y real yield rose 61bp in 3 months, pressuring AOCI and tangible book [Likely] (research/RF/2026-10-09-macro.md). Short interest is up 11.7% month on month [Certain] [ST], Treasurer and senior-executive turnover precedes Q3 results on Oct 16 [Certain] [OV], and RF has lagged SPY by 18.3pp over 6 months [Certain] [HI].
## Bull case
On earnings, RF is cheap: P/E of 11.0x is 15% below the 13.0x peer median [Certain] [RA]. It returns capital hard. The share count fell 3.95% YoY [Certain] [ST] and the FCF yield is 7.71% [Certain] [ST]. ROE of 11.9% TTM is up from the FY2024 trough of 10.7% [Certain] [RA], and net margin recovered from 28.7% to 30.8% [Certain] [IS], so the five-year decline may be bottoming [Likely]. A steep curve (10y-2y +51bp) supports NIM if yields plateau [Likely] (macro overlay), and RF's prime-rate hike to 7.00% shows asset yields repricing [Certain] [OV]. The FCFE DCF gives 31.52 base [Certain] [fact sheet]. The reverse DCF implies -2.2% year-1 revenue growth, a low bar [Certain] [fact sheet]. Still, this is a fair price for an average bank, not a mispricing [Likely].
## Decision
```json
{
  "ticker": "RF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A buyback-heavy regional bank trades at a P/E discount to peers but at a P/B above its own 5-year range while ROE has fallen for five years, leaving roughly no upside to base fair value and a bearish rate overlay.",
  "rationale": "Price sits at base fair value (27.45) with -16.4% to bear versus +12.6% to bull. P/B is above its 5-year maximum despite lower ROE, the F-Score is 3, and the primary macro overlay tilts bearish ahead of Q3 results. A decent franchise at a full price earns conviction 3 at most, below the buy threshold.",
  "price_at_decision": 27.07,
  "price_date": "2026-10-08",
  "research_note": "research/RF/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE recovers above 13% (statistics page), reversing the five-year decline from 13.8% and justifying the premium P/B.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13}},
    {"text": "TTM net (profit) margin rises above 32%, showing the recovery from the FY2024 trough of 28.7% is durable.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 32}},
    {"text": "Q3 2026 results (Oct 16, 2026) show tangible book value falling versus Q2 2026 from AOCI losses, confirming the macro bear chain."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 30.48, "basis": "ROE recovery from 10.7% (FY2024) to 11.9% TTM continues and yields plateau, so P/B holds near 1.3x, reaching the fact sheet's bull fair value 30.48 [RA, fact sheet]."},
    "base": {"probability": 0.45, "target_price_12m": 27.45, "basis": "ROE holds near 11.9% TTM and buybacks (-3.95% shares YoY [ST]) offset some P/B drift toward its 1.2x 5y median, giving the base fair value 27.45 (P/B+ROE 67% / FCFE 33% blend) [fact sheet]."},
    "bear": {"probability": 0.35, "target_price_12m": 22.64, "basis": "Bear weight raised by a moderate amount per the primary macro overlay (research/RF/2026-10-09-macro.md: 10y real yield +61bp/3m erodes AOCI/tangible book) as P/B unwinds from above its 1.3x 5y max toward range, reaching bear fair value 22.64 [RA, fact sheet]."}
  },
  "entry_price": 21.96,
  "entry_basis": "valuation file: base 27.45 x 0.8 (20% margin of safety); at that level the declining-ROE and macro risks would be priced in.",
  "replaces": null,
  "replacement_reason": null
}
```
