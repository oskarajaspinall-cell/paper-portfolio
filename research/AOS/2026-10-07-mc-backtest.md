## Monte Carlo calibration backtest — AOS (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 6/8 (75%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -1.1% | -19.9% / +22.4% | -17.7% | -27.3% / +32.5% |
| 2024-09-30 | -24.1% | -21.0% / +23.7% | -26.9% | -28.7% / +34.2% |
| 2024-12-31 | -3.6% | -21.0% / +23.9% | -3.1% | -29.0% / +34.5% |
| 2025-03-31 | +0.6% | -21.3% / +24.1% | +11.5% | -29.5% / +35.0% |
| 2025-06-30 | +10.9% | -20.9% / +23.4% | +4.3% | -28.9% / +34.0% |
| 2025-09-30 | -6.0% | -18.6% / +20.5% | -10.2% | -25.9% / +29.6% |
| 2025-12-31 | -4.5% | -18.0% / +19.9% | -7.9% | -25.1% / +28.5% |
| 2026-03-31 | -3.6% | -18.1% / +20.2% | -7.9% | -25.3% / +28.5% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
