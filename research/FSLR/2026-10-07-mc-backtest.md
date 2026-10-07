## Monte Carlo calibration backtest — FSLR (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 1/8 (12%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -7.2% | -39.4% / +51.6% | -29.5% | -52.2% / +74.1% |
| 2024-09-30 | -28.6% | -39.8% / +51.9% | -50.2% | -52.6% / +75.3% |
| 2024-12-31 | -30.3% | -39.1% / +51.1% | -16.7% | -51.9% / +73.5% |
| 2025-03-31 | +19.5% | -39.0% / +50.9% | +72.8% | -51.8% / +73.4% |
| 2025-06-30 | +44.6% | -38.9% / +50.6% | +77.3% | -51.7% / +72.8% |
| 2025-09-30 | +22.6% | -39.5% / +51.3% | -13.5% | -52.4% / +74.6% |
| 2025-12-31 | -29.4% | -38.8% / +50.6% | -11.4% | -51.6% / +72.7% |
| 2026-03-31 | +25.6% | -39.3% / +50.8% | -6.6% | -52.0% / +74.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
