## Monte Carlo calibration backtest — FICO (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +34.7% | -26.9% / +31.6% | +45.6% | -36.8% / +46.1% |
| 2024-09-30 | +6.1% | -26.9% / +31.7% | -4.4% | -36.7% / +45.5% |
| 2024-12-31 | -9.9% | -27.7% / +32.9% | -10.9% | -37.8% / +47.7% |
| 2025-03-31 | -1.0% | -27.7% / +33.0% | -17.2% | -37.8% / +47.2% |
| 2025-06-30 | -16.4% | -30.6% / +37.0% | -3.5% | -41.5% / +53.6% |
| 2025-09-30 | +15.4% | -32.2% / +39.7% | -33.4% | -43.7% / +57.1% |
| 2025-12-31 | -42.3% | -31.3% / +38.3% | -32.5% | -42.4% / +54.6% |
| 2026-03-31 | +17.0% | -34.2% / +43.0% | -14.6% | -46.2% / +61.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
