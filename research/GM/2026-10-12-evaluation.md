# Evaluation: General Motors Company (GM) — 2026-10-12
## Bear case
Profitability is falling and the price does not yet show it. Gross margin fell from 14.2% to 10.2%, operating margin from 9.0% to 5.5% and ROE from 17.2% to 3.2% over five years [IS,RA] [Certain]. Q3 US unit sales fell 5.5% with EV sales down across the board, and the Detroit Three are losing share to Asian rivals (Reuters, 2026-10-01) [Likely]. EV/EBITDA of 10.7x sits at the 98th percentile of its own 5y range [RA], so the stock is not cheap on operating earnings [Certain]. The 19.83% FCF yield is flattered by a collapsed net-income base (FCF/NI 738.7%) [CF,IS] [Certain]. Altman Z of 1.27, beta 1.40 and ~$111.7bn of captive-finance debt make GM sensitive to rising real yields, which the macro overlay rates a moderate bear tilt [Likely]. Earnings on Oct 20, 2026 are an unhedged binary [Certain].

## Bull case
On cash flow GM is very cheap: P/FCF of 5.0x sits at the 10th percentile of its 4.3x–11.1x 5y range, and the FCF margin rose to 7.8% TTM from 6.0% in FY2021 [RA,CF] [Certain]. The share count fell 10.37% YoY [ST], so buybacks compound per-share value even with flat profits [Certain]. The reverse DCF implies a -6.4% year-1 revenue decline [Fair value], which already prices continued share loss [Likely]. The mechanical base fair value of 158.74 is +91.9% above the price [Fair value] [Certain]. Automotive liquidity of $24.7bn exceeds the ~$16.0bn of automotive debt (SEC 10-Q), so the headline 6.32x leverage overstates industrial risk [Certain]. Looser fuel-economy rules and the hybrid pivot could steady the mix [Guessing].

## Decision
```json
{
  "ticker": "GM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "GM's cash flow looks cheap and buybacks shrink the share count fast, but margins and ROE are falling, it is losing share, and EV/EBITDA is near its own 5-year high, so the FCF yield reflects a weak earnings base rather than mispriced quality.",
  "rationale": "Cheap P/FCF and 10% share shrinkage are real, but every margin line and ROE has fallen for five years, Q3 units fell 5.5%, EV/EBITDA is at the top of its own range, and macro tilts bear. The +92% base fair value assumes a margin recovery that has not shown up. That is good but not compelling, so we hold cash.",
  "price_at_decision": 82.73,
  "price_date": "2026-10-09",
  "research_note": "research/GM/2026-10-12.md",
  "triggers": [
    {"text": "TTM gross margin recovers above 12% (back to FY2024's 12.3%), showing that pricing and mix have stabilised against Asian competition.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 12}},
    {"text": "TTM operating margin recovers above 7% (versus 5.5% TTM and 6.8% in FY2024), reversing the five-year compression.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 7}},
    {"text": "TTM ROE recovers above 10% (versus 3.2% TTM), showing that net income is no longer eroded by charges.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "Reported US quarterly vehicle sales stop declining year on year for two consecutive quarters as the hybrid lineup ships."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 104.24, "basis": "Margins stabilise and P/FCF returns from 5.0x to its 5y median of 6.3x [RA] on TTM FCF [CF], helped by 10.37% share shrinkage [ST]; this is well below the 158.74 model base, which needs a margin recovery the 5y trend [IS] does not support."},
    "base": {"probability": 0.45, "target_price_12m": 82.73, "basis": "P/FCF near its 5y low (5.0x) and EV/EBITDA near its 5y high (10.7x vs 10.8x max) [RA] cancel out while margins drift (operating 5.5% TTM [IS]), so the price is flat; it sits below the 158.74 base fair value because the through-cycle DCF assumes margins revert, while the EV/EBITDA method's base is only 49.96 [Fair value]."},
    "bear": {"probability": 0.35, "target_price_12m": 71.64, "basis": "Margins stay at TTM lows as share loss continues (Reuters 2026-10-01, Q3 sales -5.5%), matching the mechanical bear fair value of 71.64 [Fair value]; probability raised moderately per the macro overlay's bear tilt (research/GM/2026-10-12-macro.md: rising real yields lift auto-loan APRs and GM Financial funding costs)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value less 20% (158.74 x 0.8) is already above the price, and the issue is five years of falling gross, operating and net margins and ROE [IS,RA] plus active share loss. A lower price would not change the decision; stabilising margins (see triggers) would.",
  "replaces": null,
  "replacement_reason": null
}
```
