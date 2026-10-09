## Monte Carlo calibration backtest — BRO (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 2/8 (25%) |
| 6m | 6/8 (75%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +8.7% | -18.0% / +20.0% | +11.0% | -24.8% / +28.8% |
| 2024-09-30 | +0.4% | -18.3% / +20.3% | +20.1% | -25.4% / +29.3% |
| 2024-12-31 | +19.6% | -18.1% / +20.1% | +6.8% | -25.1% / +28.8% |
| 2025-03-31 | -10.7% | -17.3% / +18.9% | -23.5% | -24.2% / +27.4% |
| 2025-06-30 | -14.3% | -16.0% / +17.5% | -26.0% | -22.4% / +24.6% |
| 2025-09-30 | -13.7% | -16.3% / +17.8% | -32.1% | -22.7% / +25.1% |
| 2025-12-31 | -21.3% | -17.5% / +19.3% | -20.1% | -24.4% / +27.6% |
| 2026-03-31 | +1.5% | -18.7% / +20.8% | -3.6% | -26.0% / +29.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
