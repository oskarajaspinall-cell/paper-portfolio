## Monte Carlo calibration backtest — WRB (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +7.9% | -16.6% / +18.0% | +11.7% | -22.9% / +25.6% |
| 2024-09-30 | +5.4% | -16.5% / +17.9% | +27.5% | -22.8% / +25.3% |
| 2024-12-31 | +21.0% | -17.1% / +18.5% | +23.7% | -23.6% / +26.3% |
| 2025-03-31 | +2.2% | -17.9% / +19.6% | +7.5% | -24.9% / +28.1% |
| 2025-06-30 | +5.1% | -17.4% / +19.0% | -0.7% | -24.1% / +27.0% |
| 2025-09-30 | -5.5% | -16.8% / +18.1% | -13.2% | -23.2% / +25.7% |
| 2025-12-31 | -8.1% | -19.2% / +21.2% | +2.0% | -26.5% / +30.5% |
| 2026-03-31 | +11.1% | -17.6% / +19.1% | +4.3% | -24.3% / +27.6% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
