## Monte Carlo NEEDS REVIEW — HAS (2026-10-09)
The scenario probabilities are a symmetric default (bull = bear). Per the owner's rule they are not accepted automatically. Evidence currently cited:
- bull: 30% — Wizards of the Coast's margin expansion looks structural, not cyclical: ROIC rose from 10.4% (FY21) to 28.3% TTM, gross margin from 50.5% to 63.8%, and net debt/EBITDA fell from 5.72x to 1.92x (https://stockanalysis.com/stocks/has/financials/ratios/); tabletop/WizCo revenue grew 30%/27% YoY per the 10-Q (https://www.sec.gov/Archives/edgar/data/46080/000004608026000050/has-20260628.htm).
- base: 40% — EV/EBITDA (12.0x) sits just above its own 5-year minimum (11.7x) and P/FCF (10.8x) is near its 5-year minimum (10.4x) (factsheet-2026-10-09.md Valuation table) — the market is pricing 'prove it for more quarters,' consistent with a flat-price base case rather than a re-rating or de-rating.
- bear: 30% — EV/Sales (3.1x) is already above its own 5-year maximum (3.0x, factsheet-2026-10-09.md Valuation table), and 58% of revenue depends on one hit-driven card franchise (Wizards of the Coast tabletop +30% YoY on Magic releases, 10-Q MD&A) — a real risk that the mix-shift/margin cycle normalises.

To accept them, add to the parameters file: `"owner_review": {"approved": true, "note": "<why these probabilities are right>"}` and re-run.
