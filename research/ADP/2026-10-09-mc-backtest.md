## Monte Carlo calibration backtest — ADP (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 6/8 (75%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +12.0% | -17.5% / +19.7% | +19.8% | -24.3% / +28.1% |
| 2024-09-30 | +9.1% | -17.7% / +19.6% | +11.4% | -24.5% / +27.9% |
| 2024-12-31 | +2.1% | -16.7% / +18.4% | +3.5% | -23.2% / +26.5% |
| 2025-03-31 | +1.4% | -16.1% / +17.7% | -2.1% | -22.4% / +25.6% |
| 2025-06-30 | -3.4% | -15.3% / +16.8% | -13.7% | -21.4% / +23.9% |
| 2025-09-30 | -10.6% | -13.8% / +15.0% | -29.9% | -19.3% / +21.4% |
| 2025-12-31 | -21.6% | -14.1% / +15.4% | -12.3% | -19.7% / +21.8% |
| 2026-03-31 | +11.9% | -16.2% / +18.0% | +32.9% | -22.6% / +25.4% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
