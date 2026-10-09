## Monte Carlo calibration backtest — NFLX (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 0/8 (0%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +2.2% | -34.6% / +43.6% | +32.5% | -46.2% / +62.9% |
| 2024-09-30 | +28.3% | -33.4% / +41.8% | +32.0% | -44.8% / +60.3% |
| 2024-12-31 | +2.9% | -32.1% / +39.9% | +45.8% | -43.3% / +57.5% |
| 2025-03-31 | +41.7% | -29.8% / +36.1% | +29.6% | -40.5% / +52.2% |
| 2025-06-30 | -8.5% | -26.3% / +31.3% | -28.6% | -35.8% / +44.8% |
| 2025-09-30 | -22.0% | -26.2% / +31.0% | -22.8% | -35.6% / +44.9% |
| 2025-12-31 | -1.1% | -25.3% / +29.8% | -21.9% | -34.7% / +42.7% |
| 2026-03-31 | -21.0% | -26.8% / +31.9% | -23.9% | -36.5% / +45.3% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
