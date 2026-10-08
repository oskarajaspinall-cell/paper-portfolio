## Monte Carlo calibration backtest — PGR (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +24.0% | -19.4% / +21.3% | +14.8% | -26.7% / +30.3% |
| 2024-09-30 | -4.0% | -17.7% / +19.3% | +13.2% | -24.4% / +27.5% |
| 2024-12-31 | +17.9% | -18.0% / +19.9% | +11.7% | -24.9% / +28.4% |
| 2025-03-31 | -5.3% | -18.0% / +19.9% | -12.6% | -25.0% / +28.4% |
| 2025-06-30 | -7.7% | -17.9% / +19.6% | -13.9% | -24.7% / +28.0% |
| 2025-09-30 | -6.7% | -17.5% / +19.2% | -13.1% | -24.1% / +27.1% |
| 2025-12-31 | -6.9% | -18.4% / +20.0% | +5.1% | -25.4% / +28.8% |
| 2026-03-31 | +12.9% | -17.9% / +19.4% | +3.4% | -24.8% / +27.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
