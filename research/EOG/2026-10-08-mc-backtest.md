## Monte Carlo calibration backtest — EOG (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 6/8 (75%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +4.0% | -25.7% / +29.9% | -1.1% | -35.1% / +43.4% |
| 2024-09-30 | -1.0% | -25.0% / +29.0% | +4.9% | -34.3% / +42.0% |
| 2024-12-31 | +5.9% | -24.8% / +28.7% | +2.0% | -33.9% / +41.7% |
| 2025-03-31 | -3.7% | -24.4% / +28.2% | -5.7% | -33.3% / +40.9% |
| 2025-06-30 | -2.1% | -23.9% / +27.6% | -12.8% | -32.9% / +39.8% |
| 2025-09-30 | -10.9% | -23.2% / +26.6% | +29.9% | -31.9% / +38.4% |
| 2025-12-31 | +45.9% | -21.6% / +24.3% | +30.3% | -29.6% / +35.0% |
| 2026-03-31 | -10.7% | -21.1% / +23.6% | -4.7% | -29.0% / +33.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
