## Monte Carlo calibration backtest — CF (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +12.3% | -24.3% / +27.8% | +17.6% | -33.2% / +40.4% |
| 2024-09-30 | -0.5% | -23.7% / +26.9% | -8.5% | -32.3% / +39.4% |
| 2024-12-31 | -8.1% | -23.0% / +26.0% | +8.7% | -31.4% / +38.0% |
| 2025-03-31 | +18.3% | -24.3% / +27.7% | +20.4% | -33.2% / +40.1% |
| 2025-06-30 | +1.9% | -24.7% / +28.1% | -13.9% | -33.6% / +40.7% |
| 2025-09-30 | -15.4% | -25.2% / +28.9% | +49.8% | -34.3% / +41.7% |
| 2025-12-31 | +77.1% | -24.8% / +28.2% | +37.8% | -33.7% / +40.9% |
| 2026-03-31 | -22.2% | -25.3% / +28.6% | -15.2% | -34.3% / +42.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
