## Monte Carlo calibration backtest — EXE (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -4.0% | -24.9% / +29.4% | +16.7% | -34.1% / +41.9% |
| 2024-09-30 | +17.7% | -24.6% / +28.9% | +35.9% | -33.7% / +41.4% |
| 2024-12-31 | +15.5% | -23.7% / +27.5% | +24.5% | -32.5% / +39.7% |
| 2025-03-31 | +7.8% | -22.4% / +25.8% | -2.7% | -30.8% / +37.1% |
| 2025-06-30 | -9.7% | -20.6% / +23.1% | -6.1% | -28.3% / +33.0% |
| 2025-09-30 | +4.0% | -22.3% / +25.1% | +8.4% | -30.4% / +35.9% |
| 2025-12-31 | +4.2% | -23.1% / +26.0% | -18.3% | -31.6% / +37.8% |
| 2026-03-31 | -21.6% | -23.2% / +26.3% | -22.6% | -31.8% / +37.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
