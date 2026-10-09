## Monte Carlo calibration backtest — CI (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +5.2% | -19.3% / +21.3% | -17.9% | -26.5% / +30.2% |
| 2024-09-30 | -19.5% | -19.3% / +21.3% | -5.7% | -26.5% / +30.1% |
| 2024-12-31 | +17.2% | -19.1% / +21.2% | +18.2% | -26.5% / +30.2% |
| 2025-03-31 | +0.9% | -18.3% / +20.1% | -11.1% | -25.4% / +28.7% |
| 2025-06-30 | -11.9% | -17.3% / +18.7% | -14.4% | -24.0% / +26.9% |
| 2025-09-30 | -2.8% | -19.4% / +21.3% | -7.4% | -26.8% / +30.7% |
| 2025-12-31 | -4.7% | -22.8% / +26.0% | +3.4% | -31.4% / +37.4% |
| 2026-03-31 | +8.6% | -22.9% / +25.9% | +5.0% | -31.2% / +38.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
