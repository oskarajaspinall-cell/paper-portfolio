# Evaluation: Wise Group plc (WSE) — 2026-10-18
## Bear case
Profitability is in a two-year decline: operating margin 44.7% TTM against 56.2% in FY2024, ROE 27.2% against 51.0% [Certain] [IS,RA]. The headline cheapness is not real: P/FCF 1.5x and a 67% FCF yield come from customer-balance movements, so the DCF-led fair value (base 108.64) is built on float, not owner cash [Likely]. On the cleaner multiples Wise trades at a premium to peers: P/E 22.7x against a 10.5x peer median, P/B 5.8x against 2.3x [Certain] [RA]. A securities class action alleges undisclosed AML/CTF compliance failures [Certain]; a regulator fine or licence action would hit the licensing moat directly, and the outcome cannot be sized [Guessing]. Short interest rose 18.4% month on month [Certain] [ST]. The macro overlay tilts moderately toward bear: rising real yields press the multiple, and any rate cuts would remove float income [Likely] (research/WSE/2026-10-18-macro.md).

## Bull case
Wise is a net-cash network business (net debt/EBITDA -4.32x) shrinking its share count by 1.53% a year [Certain] [BS,IS,ST]. Q2 beat expectations, and management narrowed FY27 revenue growth to the upper part of its range on stronger customer growth and cross-border volumes [Likely] (https://www.reuters.com/technology/money-transfer-firm-wise-raises-revenue-growth-outlook-cross-border-volumes-jump-2026-10-16/). P/E sits at the floor of its 5y range (22.3x min, 23.4x median) and EV/EBITDA at 5.6x is below both its own 5y minimum of 8.7x and the peer median [Certain] [RA]. Margins of 84.2% gross and 44.7% operating are still exceptional for payments [Certain] [IS]. Elevated short rates help float income [Likely] (macro overlay). If the litigation fades, a re-rating toward the 5y EV/EBITDA floor is plausible [Guessing].

## Decision
```json
{
  "ticker": "WSE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-margin cross-border payments network with raised revenue guidance, but returns and margins are falling for a second year, the apparent cash cheapness is customer float, and an unresolved AML/CTF class action threatens the licensing moat.",
  "rationale": "Good franchise, not compelling. On undistorted multiples it trades at a premium to peers while margins compress. The fair value is inflated by float and the litigation can't be sized. Macro tilts moderately to bear. Conviction 3 means no position; cash is the better holding until the litigation and margin trend clear.",
  "price_at_decision": 10.98,
  "price_date": "2026-10-16",
  "research_note": "research/WSE/2026-10-18.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 54%, back to the FY2025 level, showing the take-rate/cost compression has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 54}},
    {"text": "TTM ROE recovers above 37%, the FY2025 level, ending the two-year decline in returns.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 37}},
    {"text": "The AML/CTF securities class action is dismissed or settled with no regulator fine, consent order or licence action in a material market, as shown in company filings or releases."},
    {"text": "TTM gross margin falls below 80%, confirming continuing take-rate pressure (would harden the AVOID).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 14.36, "basis": "Guidance upgrade holds and the litigation fades, so EV/EBITDA moves back toward its 5y minimum of 8.7x [RA], matching the fact sheet's EV/EBITDA bear value of 14.36 rather than the float-inflated DCF; probability trimmed for the macro overlay's moderate bear tilt (research/WSE/2026-10-18-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 11.32, "basis": "Revenue grows per the narrowed guidance (Reuters URL in the note) but margins stay compressed, so P/E settles near its 5y median of 23.4x [RA] on TTM earnings; far below the mechanical base fair value because that DCF capitalises a float-driven 301% FCF margin [CF,IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 8.5, "basis": "Operating margin keeps falling from 44.7% [IS] and the AML/CTF litigation escalates toward regulator action, cutting earnings at a P/E held near its 5y low of 22.3x [RA]; probability raised for the macro overlay's moderate bear tilt from rising real yields (research/WSE/2026-10-18-macro.md)."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "bear", "field": "margin", "value": 0.199, "reason": "Reported FCF margin (301% [CF,IS]) is customer-balance float, not owner cash (research/WSE/2026-10-18.md section 5); TTM net margin 19.9% [IS] is the cleaner cash proxy."},
    {"method": "dcf", "scenario": "base", "field": "margin", "value": 0.199, "reason": "Reported FCF margin (301% [CF,IS]) is customer-balance float, not owner cash (research/WSE/2026-10-18.md section 5); TTM net margin 19.9% [IS] is the cleaner cash proxy."},
    {"method": "dcf", "scenario": "bull", "field": "margin", "value": 0.262, "reason": "Float-inflated FCF replaced by net margin; bull assumes a recovery to the FY2025 net margin of 26.2% [IS]."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: an unresolved AML/CTF class action with possible regulator consequences, two years of falling margins and returns, and a fair value distorted by float mean a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```
