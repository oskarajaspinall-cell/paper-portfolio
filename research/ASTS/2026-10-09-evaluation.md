# Evaluation: AST SpaceMobile, Inc. (ASTS) — 2026-10-09
## Bear case
ASTS is a pre-commercial capex project priced as a winner: EV/Sales 198.3x, +760% vs the 23.0x peer median, with no computable fair value because FCF and EBITDA are negative [Certain] (FS: RA, Fair value). Operating margin is -410.3% and FCF margin -1,420.7% TTM; shares grew 39.67% YoY, so funding the buildout dilutes holders heavily [Certain] (IS, CF, ST). SpaceX is expanding direct-to-cell service with far deeper capital and an existing carrier partner, attacking the carrier-revenue-share moat directly [Likely] (note §2). Securities class actions allege the company misled investors on its D2C competitive position, the exact thesis pillar [Certain] (note §6). Short interest 24.49% and beta 2.71 mean gap risk both ways [Certain] (ST). Rising real yields are a small extra headwind on long-duration unprofitable equity [Likely] (macro overlay).

## Bull case
The moat could still be real: broadband to unmodified phones needs spectrum priority and a dense LEO constellation, and ASTS claims 60+ operator partners including AT&T and Verizon [Likely] (note §1-2). The balance sheet is funded: net debt/EBITDA -1.74x TTM (net cash) and long-dated convertibles to 2032-2036 [Certain] (BS, note §5). ROCE improved from -70.7% (FY2023) to -8.4% TTM as assets enter service [Certain] (RA). EV/Sales sits at the 19th percentile of its own 5y range and P/B is 19% below peers [Certain] (RA). A favourable FCC outcome at the October 29 meeting or launch cadence could re-rate the stock sharply [Guessing].

## Decision
```json
{
  "ticker": "ASTS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A pre-revenue-scale direct-to-device satellite constellation priced at 198.3x EV/Sales with no fair-value anchor, facing a better-capitalised SpaceX rival and securities litigation over its competitive claims.",
  "rationale": "Not a good business yet (operating margin -410.3%, FCF margin -1,420.7%), no computable fair value, heavy dilution (39.67% YoY), and the core moat is under direct competitive and legal challenge. Probability-weighted 12-month value sits below the price. Speculative optionality is not core quality-plus-value; conviction 2 means no position.",
  "price_at_decision": 56.93,
  "price_date": "2026-10-08",
  "research_note": "research/ASTS/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin turns positive, showing the constellation has reached commercial scale and the revenue-share model works.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 0}},
    {"text": "TTM FCF margin turns positive, removing the need for further dilutive capital raises.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 0}},
    {"text": "The FCC adopts rules after its October 29 meeting that authorise ASTS's commercial direct-to-device service on partner spectrum, and the securities class actions are dismissed or settled immaterially, per a company release or SEC filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 100, "basis": "FCC authorisation and commercial launch with AT&T/Verizon (note §1, §6) let EV/Sales stay well inside its 5y range of 25.7x-932.2x [RA] while revenue ramps; no mechanical fair value exists (negative FCF/EBITDA), so this is a multiple-based estimate."},
    "base": {"probability": 0.4, "target_price_12m": 50, "basis": "EV/Sales mean-reverts toward its 5y median 156.2x [RA] from 198.3x, partly offset by revenue growth as satellites enter service (ROCE -8.4% TTM improving [RA]); fair value is not computable, so the range is anchored on own-history EV/Sales."},
    "bear": {"probability": 0.4, "target_price_12m": 32, "basis": "SpaceX direct-to-cell competition and the D2C class actions (note §2, §6) compress EV/Sales roughly halfway toward the 23.0x peer median [RA] while dilution continues (shares +39.67% YoY [ST]); probability raised by the macro overlay's small tilt toward bear on rising real yields (research/ASTS/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2: price is not the obstacle. Negative margins, heavy dilution, an unresolved securities class action and an unproven moat against SpaceX mean a lower price would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
