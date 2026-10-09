## Monte Carlo calibration backtest — CMCSA (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 6/8 (75%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +5.1% | -19.6% / +22.0% | +0.9% | -27.3% / +31.1% |
| 2024-09-30 | -8.2% | -19.2% / +21.4% | -10.7% | -26.7% / +30.6% |
| 2024-12-31 | -2.6% | -19.3% / +21.5% | -5.2% | -26.8% / +30.6% |
| 2025-03-31 | -2.7% | -20.3% / +22.8% | -11.8% | -28.2% / +32.7% |
| 2025-06-30 | -9.4% | -18.8% / +20.9% | -14.4% | -26.2% / +29.7% |
| 2025-09-30 | -5.5% | -18.0% / +20.0% | -2.5% | -25.1% / +28.3% |
| 2025-12-31 | +3.2% | -18.1% / +20.0% | -14.7% | -25.3% / +28.3% |
| 2026-03-31 | -17.3% | -16.9% / +18.5% | -20.7% | -23.6% / +26.4% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
