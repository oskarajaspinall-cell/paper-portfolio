## Monte Carlo calibration backtest — CTAS (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +15.5% | -17.9% / +20.2% | +5.9% | -24.6% / +29.3% |
| 2024-09-30 | -9.2% | -17.8% / +20.1% | +0.8% | -24.4% / +28.7% |
| 2024-12-31 | +11.0% | -19.3% / +22.0% | +20.8% | -26.6% / +31.6% |
| 2025-03-31 | +8.8% | -18.9% / +21.3% | +0.9% | -26.2% / +30.9% |
| 2025-06-30 | -7.3% | -18.2% / +20.3% | -13.0% | -25.3% / +29.1% |
| 2025-09-30 | -6.2% | -17.5% / +19.3% | -18.5% | -24.5% / +27.8% |
| 2025-12-31 | -13.1% | -15.9% / +17.5% | -9.6% | -22.4% / +24.9% |
| 2026-03-31 | +4.0% | -16.7% / +18.2% | +21.3% | -23.4% / +26.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
