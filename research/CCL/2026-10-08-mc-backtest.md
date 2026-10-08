## Monte Carlo calibration backtest — CCL (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 2/8 (25%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +18.2% | -40.3% / +53.8% | +66.8% | -53.2% / +78.1% |
| 2024-09-30 | +35.3% | -40.8% / +54.7% | +7.2% | -53.9% / +79.9% |
| 2024-12-31 | -20.8% | -39.3% / +51.8% | +8.7% | -51.9% / +75.7% |
| 2025-03-31 | +37.2% | -39.1% / +51.3% | +54.1% | -51.6% / +74.2% |
| 2025-06-30 | +12.3% | -37.1% / +48.1% | +12.6% | -49.4% / +69.6% |
| 2025-09-30 | +0.3% | -34.9% / +44.3% | -20.6% | -46.6% / +64.5% |
| 2025-12-31 | -20.8% | -34.1% / +43.3% | -4.3% | -45.8% / +62.2% |
| 2026-03-31 | +20.9% | -34.4% / +43.6% | -7.0% | -46.3% / +62.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
