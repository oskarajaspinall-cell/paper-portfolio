## Monte Carlo calibration backtest — JKHY (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 7/8 (88%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +4.4% | -17.0% / +18.8% | +6.7% | -23.9% / +26.7% |
| 2024-09-30 | +0.8% | -16.1% / +17.6% | +2.1% | -22.6% / +25.0% |
| 2024-12-31 | +1.3% | -16.3% / +17.8% | +1.5% | -22.8% / +25.3% |
| 2025-03-31 | +0.2% | -18.1% / +20.1% | -15.8% | -25.2% / +28.4% |
| 2025-06-30 | -15.9% | -17.4% / +19.2% | +5.1% | -24.2% / +27.2% |
| 2025-09-30 | +25.0% | -17.2% / +18.9% | +3.3% | -24.0% / +26.9% |
| 2025-12-31 | -17.3% | -17.4% / +19.0% | -26.9% | -24.3% / +27.2% |
| 2026-03-31 | -11.5% | -18.0% / +19.9% | -2.8% | -25.2% / +28.3% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
