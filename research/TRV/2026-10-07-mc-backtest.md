## Monte Carlo calibration backtest — TRV (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 7/8 (88%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +14.2% | -14.6% / +15.8% | +15.7% | -20.3% / +22.7% |
| 2024-09-30 | +2.7% | -14.7% / +16.1% | +11.8% | -20.6% / +23.0% |
| 2024-12-31 | +8.9% | -17.1% / +18.9% | +10.0% | -23.7% / +26.5% |
| 2025-03-31 | +1.0% | -17.2% / +19.0% | +7.0% | -24.0% / +26.8% |
| 2025-06-30 | +5.9% | -17.1% / +18.8% | +11.8% | -23.8% / +26.7% |
| 2025-09-30 | +5.6% | -16.3% / +17.8% | +3.5% | -22.8% / +25.3% |
| 2025-12-31 | -2.0% | -15.3% / +16.7% | +12.9% | -21.4% / +23.6% |
| 2026-03-31 | +15.2% | -15.4% / +16.7% | +28.2% | -21.5% / +23.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
